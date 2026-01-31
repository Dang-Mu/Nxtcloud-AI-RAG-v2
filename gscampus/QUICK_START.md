# 🚀 빠른 시작

## 1단계: terraform.tfvars 생성

```bash
cp terraform.tfvars.example terraform.tfvars
```

terraform.tfvars 파일을 열어 다음을 편집하세요:

```hcl
aws_profile         = "default"        # AWS CLI 프로필명
aws_region          = "us-east-1"      # 리전
db_master_password  = "your-password"  # 안전한 비밀번호로 변경
```

## 2단계: Terraform 실행

```bash
terraform init
terraform apply
```

## 3단계: 엔드포인트 확인

```bash
terraform output endpoint
```

## 4단계: 연결 테스트

```bash
# terraform output 결과: nxtcloud-postgres.xxxxx.us-east-1.rds.amazonaws.com:5432

# 호스트만 추출 (포트 제거)
ENDPOINT=$(terraform output -raw endpoint | cut -d: -f1)

# 마스터 DB (nxtcloud_db)로 연결
psql -h $ENDPOINT -U postgres -d nxtcloud_db -c "SELECT version();"

# 또는 db_01에 user_01로 연결
psql -h $ENDPOINT -U user_01 -d db_01 -c "\dt"
```

---

## 📋 실제 생성되는 database_name

**terraform apply 후 자동 생성:**

```
RDS Instance 생성 완료
└─ nxtcloud_db (자동 생성됨) ⭐
   ├─ database_name = "nxtcloud_db"
   ├─ 소유자: postgres
   └─ 역할: init_database.py의 진입점

init_database.py 자동 실행
├─ nxtcloud_db에 접속
├─ db_01 생성 (user_01 소유)
├─ db_02 생성 (user_02 소유)
├─ 테이블 및 인덱스 생성
└─ 완료!
```

**데이터베이스 목록 확인:**

```bash
psql -h $ENDPOINT -U postgres -d nxtcloud_db -c "\l"

# 출력:
#     Name      | Owner    
# ───────────────┼──────────
#  nxtcloud_db   | postgres  ⭐ RDS가 자동 생성 (database_name 값)
#  db_01         | user_01   (init_database.py 생성)
#  db_02         | user_02   (init_database.py 생성)
#  postgres      | postgres  (기본)
#  template0     | postgres  (기본)
#  template1     | postgres  (기본)
```

---

## 🔧 설정

### 변수로 설정 (terraform.tfvars)
| 설정 | 값 | 의미 |
|------|----|----|
| **aws_profile** | default | AWS CLI 프로필명 |
| **aws_region** | us-east-1 | AWS 리전 |
| **instance_class** | db.t3.micro | AWS 프리티어 (무료) |
| **allocated_storage** | 20GB | 프리티어 범위 (무료) |
| **database_name** | nxtcloud_db | RDS 생성시 자동으로 생성되는 초기 DB |
| **db_master_username** | postgres | 마스터 사용자명 |
| **db_master_password** | - | 마스터 비밀번호 (필수 입력) |

### 고정 설정 (변수 없음)
| 설정 | 값 | 의미 |
|------|----|----|
| **skip_final_snapshot** | true | 삭제시 스냅샷 안 만들기 (비용 절감) |
| **performance_insights_enabled** | false | 성능 개선 도우미 OFF (비용 절감) |
| **publicly_accessible** | true | Public 접근 활성화 |

---

**소요 시간:** 약 15-20분 (RDS 생성 시간 포함)
