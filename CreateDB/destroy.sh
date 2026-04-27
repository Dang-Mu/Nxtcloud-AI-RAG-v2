#!/bin/bash
set -e

# 색상 코드
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
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
info "CreateDB 리소스 삭제"
separator

# 스크립트 위치로 이동
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

# 설정 파일 확인
CONFIG_FILE="config.yaml"

if [ ! -f "$CONFIG_FILE" ]; then
    error "설정 파일이 없습니다: $CONFIG_FILE"
fi

# 설정 파일 읽기
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

# AWS 프로파일 환경 변수 설정
export AWS_PROFILE=$AWS_PROFILE_CONFIG

# 삭제 대상 표시
echo ""
echo -e "${RED}경고: 다음 AWS 리소스가 모두 삭제됩니다.${NC}"
echo -e "  - RDS 인스턴스: $DB_INSTANCE_IDENTIFIER (리전: $AWS_REGION)"
echo -e "  - 데이터베이스: $DATABASE_NAME, db_01 ~ db_${NUM_USERS} (모든 데이터 포함)"
echo -e "  - 보안 그룹 / 서브넷 그룹 / 파라미터 그룹"
echo ""
echo -e "${RED}이 작업은 되돌릴 수 없습니다. DB 데이터가 영구히 삭제됩니다.${NC}"
echo ""
read -p "정말 삭제하시겠습니까? (yes/no): " CONFIRM

if [ "$CONFIRM" != "yes" ]; then
    info "삭제가 취소되었습니다."
    exit 0
fi

# ============================================
# Terraform destroy
# ============================================
separator
info "RDS 인스턴스 삭제 중... (5-10분 소요)"
separator

if [ ! -f "terraform.tfstate" ] && [ ! -d ".terraform" ]; then
    info "Terraform 상태 파일 없음 — 삭제할 리소스가 없습니다."
    exit 0
fi

terraform init -input=false

terraform destroy -auto-approve \
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

separator
success "모든 리소스 삭제 완료!"
separator
