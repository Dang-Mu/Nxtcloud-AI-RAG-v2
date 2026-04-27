#!/bin/bash
set -e

# 색상 코드
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# 함수: 에러 메시지 출력
error() {
    echo -e "${RED}[ERROR]${NC} $1"
    exit 1
}

# 함수: 성공 메시지 출력
success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

# 함수: 정보 메시지 출력
info() {
    echo -e "${YELLOW}[INFO]${NC} $1"
}

# 함수: 디버그 메시지 출력
debug() {
    echo -e "${BLUE}[DEBUG]${NC} $1"
}

# 함수: 구분선
separator() {
    echo "=========================================="
}

# 함수: YAML 파일에서 값 읽기
get_yaml_value() {
    local key=$1
    local file=$2
    grep "^${key}:" "$file" | sed 's/^[^:]*:[[:space:]]*//' | sed 's/"//g' | sed "s/'//g"
}

# 스크립트 시작
separator
info "CreateDB 배포 시작 (PostgreSQL RDS)"
separator

# 스크립트 위치로 이동
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

# 사전 요구사항 확인
command -v terraform >/dev/null 2>&1 || error "Terraform이 설치되어 있지 않습니다. https://www.terraform.io/downloads"
command -v aws >/dev/null 2>&1 || error "AWS CLI가 설치되어 있지 않습니다."
command -v python3 >/dev/null 2>&1 || error "Python 3가 설치되어 있지 않습니다."

# 설정 파일 확인
CONFIG_FILE="config.yaml"

if [ ! -f "$CONFIG_FILE" ]; then
    error "설정 파일이 없습니다: $CONFIG_FILE\n사용법: cp config.example.yaml config.yaml 후 값을 수정하세요."
fi

# 설정 파일 읽기
info "설정 파일 읽는 중: $CONFIG_FILE"

AWS_PROFILE_CONFIG=$(get_yaml_value "aws_profile" "$CONFIG_FILE")
AWS_REGION=$(get_yaml_value "aws_region" "$CONFIG_FILE")
DB_INSTANCE_IDENTIFIER=$(get_yaml_value "db_instance_identifier" "$CONFIG_FILE")
POSTGRES_VERSION=$(get_yaml_value "postgres_version" "$CONFIG_FILE")
POSTGRES_FAMILY_VERSION=$(get_yaml_value "postgres_family_version" "$CONFIG_FILE")
INSTANCE_CLASS=$(get_yaml_value "instance_class" "$CONFIG_FILE")
ALLOCATED_STORAGE=$(get_yaml_value "allocated_storage" "$CONFIG_FILE")
DATABASE_NAME=$(get_yaml_value "database_name" "$CONFIG_FILE")
DB_MASTER_USERNAME=$(get_yaml_value "db_master_username" "$CONFIG_FILE")
DB_MASTER_PASSWORD=$(get_yaml_value "db_master_password" "$CONFIG_FILE")
NUM_USERS=$(get_yaml_value "num_users" "$CONFIG_FILE")

# 기본값 설정
AWS_PROFILE_CONFIG=${AWS_PROFILE_CONFIG:-default}
AWS_REGION=${AWS_REGION:-us-east-1}
DB_INSTANCE_IDENTIFIER=${DB_INSTANCE_IDENTIFIER:-nxtcloud-postgres}
POSTGRES_VERSION=${POSTGRES_VERSION:-17.6}
POSTGRES_FAMILY_VERSION=${POSTGRES_FAMILY_VERSION:-17}
INSTANCE_CLASS=${INSTANCE_CLASS:-db.t3.micro}
ALLOCATED_STORAGE=${ALLOCATED_STORAGE:-20}
DATABASE_NAME=${DATABASE_NAME:-nxtcloud_db}
DB_MASTER_USERNAME=${DB_MASTER_USERNAME:-postgres}
NUM_USERS=${NUM_USERS:-2}

# 필수 값 검증
if [ -z "$DB_MASTER_PASSWORD" ] || [ "$DB_MASTER_PASSWORD" = "your-secure-password" ]; then
    error "db_master_password를 안전한 값으로 변경하세요 (config.yaml)"
fi

# AWS 프로파일 환경 변수 설정
export AWS_PROFILE=$AWS_PROFILE_CONFIG

# AWS 자격증명 확인
info "AWS 자격증명 확인 중..."
aws sts get-caller-identity --profile "$AWS_PROFILE_CONFIG" >/dev/null 2>&1 || \
    error "AWS 자격증명 확인 실패. 'aws configure --profile $AWS_PROFILE_CONFIG' 실행하세요."

success "AWS 자격증명 확인 완료"

# 설정 정보 출력
separator
info "배포 설정"
debug "  AWS 프로파일:       $AWS_PROFILE_CONFIG"
debug "  AWS 리전:           $AWS_REGION"
debug "  RDS 인스턴스:       $DB_INSTANCE_IDENTIFIER"
debug "  PostgreSQL 버전:    $POSTGRES_VERSION"
debug "  인스턴스 타입:       $INSTANCE_CLASS"
debug "  스토리지:            ${ALLOCATED_STORAGE}GB"
debug "  초기 DB:            $DATABASE_NAME"
debug "  마스터 사용자:        $DB_MASTER_USERNAME"
debug "  사용자/DB 개수:      $NUM_USERS"
separator

# ============================================
# Step 1: Terraform 초기화
# ============================================
info "Step 1: Terraform 초기화 중..."
terraform init -input=false
success "Terraform 초기화 완료"

# ============================================
# Step 2: Terraform apply
# ============================================
separator
info "Step 2: RDS 인스턴스 배포 중... (5-10분 소요)"
info "  - VPC/서브넷/보안그룹 생성"
info "  - RDS PostgreSQL 인스턴스 생성"
info "  - init_database.py 자동 실행 (DB/사용자/테이블 생성)"
separator

terraform apply -auto-approve \
    -var="aws_profile=$AWS_PROFILE_CONFIG" \
    -var="aws_region=$AWS_REGION" \
    -var="db_instance_identifier=$DB_INSTANCE_IDENTIFIER" \
    -var="postgres_version=$POSTGRES_VERSION" \
    -var="postgres_family_version=$POSTGRES_FAMILY_VERSION" \
    -var="instance_class=$INSTANCE_CLASS" \
    -var="allocated_storage=$ALLOCATED_STORAGE" \
    -var="database_name=$DATABASE_NAME" \
    -var="db_master_username=$DB_MASTER_USERNAME" \
    -var="db_master_password=$DB_MASTER_PASSWORD" \
    -var="num_users=$NUM_USERS"

success "RDS 배포 완료"

# ============================================
# 배포 결과 출력
# ============================================
separator
success "모든 배포 완료!"
separator

ENDPOINT=$(terraform output -raw endpoint)

info "접속 정보:"
debug "  엔드포인트:        $ENDPOINT"
debug "  포트:             5432"
debug "  마스터 DB:         $DATABASE_NAME"
debug "  마스터 사용자:      $DB_MASTER_USERNAME"

separator
info "접속 테스트 (psql 설치 시):"
echo "  psql -h $ENDPOINT -U $DB_MASTER_USERNAME -d $DATABASE_NAME"
echo ""
info "생성된 DB/사용자 확인:"
echo "  psql -h $ENDPOINT -U $DB_MASTER_USERNAME -d $DATABASE_NAME -c '\\l'"
echo ""
info "삭제 시: ./destroy.sh"
separator
