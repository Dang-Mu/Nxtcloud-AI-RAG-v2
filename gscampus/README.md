# NxtCloud PostgreSQL Setup

Default VPC를 사용하여 PostgreSQL RDS를 생성하고 자동으로 초기화합니다.
**AWS 프리티어 최적화** (단일 AZ, db.t3.micro, 성능 개선 도우미 OFF)

## 📋 전제 조건

- AWS CLI 설치 및 프로필 설정
- Terraform 1.0+
- Python 3.8+
- psycopg2 (`pip install -r requirements.txt`)

## 🚀 빠른 시작

### 1단계: 설정 파일 생성

```bash
cp terraform.tfvars.example terraform.tfvars
```

terraform.tfvars 파일을 편집하여 다음을 설정하세요:
- `aws_profile`: AWS CLI 프로필명
- `db_master_password`: 데이터베이스 비밀번호

### 2단계: 실행

```bash
terraform init
terraform apply
```

### 3단계: 엔드포인트 확인

```bash
terraform output endpoint
```

## 📊 생성되는 데이터베이스 구조

**terraform apply 후 실제 생성되는 구조:**

```
RDS Instance (nxtcloud-postgres)
└─ Database: nxtcloud_db ⭐
   ├─ 역할: RDS 초기화 시 자동 생성 (database_name 변수값)
   ├─ 소유자: postgres (마스터 사용자)
   ├─ 목적: init_database.py 스크립트의 진입점
   │
   ├─ db_01 (init_database.py가 생성)
   │  ├─ 소유자: user_01
   │  ├─ document_files (테이블)
   │  └─ documents (테이블, pgvector)
   │
   └─ db_02 (init_database.py가 생성)
      ├─ 소유자: user_02
      ├─ document_files (테이블)
      └─ documents (테이블, pgvector)
```

### **database_name = "nxtcloud_db" 실제 생성 예시**

```bash
# terraform apply 실행
$ terraform apply

# 5-10분 후 RDS 생성 완료
$ terraform output endpoint
nxtcloud-postgres.xxxxx.us-east-1.rds.amazonaws.com:5432

# 마스터 사용자로 접속
$ psql -h nxtcloud-postgres.xxxxx.us-east-1.rds.amazonaws.com \
        -U postgres \
        -d nxtcloud_db  # ⭐ 이것이 database_name 값 (자동 생성됨)

# 데이터베이스 확인
postgres=# \l
                                    List of databases
     Name      | Owner    | Encoding | Collate | Ctype | Access privileges
───────────────┼──────────┼──────────┼─────────┼───────┼─────────────────────
 nxtcloud_db   | postgres | UTF8     | C       | C     |  ⭐ 자동 생성된 초기 DB
 db_01         | user_01  | UTF8     | C       | C     |  (init_database.py 생성)
 db_02         | user_02  | UTF8     | C       | C     |  (init_database.py 생성)
 postgres      | postgres | UTF8     | C       | C     |  (기본 DB)
 template0     | postgres | UTF8     | C       | C     |  (기본 DB)
 template1     | postgres | UTF8     | C       | C     |  (기본 DB)
```

## 📋 변수 설명

| 변수 | 기본값 | 설명 |
|------|--------|------|
| `db_instance_identifier` | nxtcloud-postgres | RDS 인스턴스 이름 |
| `postgres_version` | 15.4 | PostgreSQL 버전 |
| `instance_class` | db.t3.micro | 프리티어 인스턴스 타입 |
| `allocated_storage` | 20 | 저장소 크기 (GB, 프리티어 최대) |
| **`database_name`** | **nxtcloud_db** | **RDS 생성시 자동 생성되는 초기 DB** |
| `db_master_username` | postgres | 마스터 사용자명 |
| `db_master_password` | - | 마스터 비밀번호 (반드시 설정) |

## 🔧 고정 설정 (변수 없음)

| 설정 | 값 | 설명 |
|------|----|----|
| **skip_final_snapshot** | true | 삭제시 스냅샷 생성 안함 (비용 절감) |
| **performance_insights_enabled** | false | 성능 개선 도우미 OFF (비용 절감) |
| **enabled_cloudwatch_logs_exports** | [] | CloudWatch 로그 OFF (비용 절감) |
| **publicly_accessible** | true | Public 접근 활성화 |

## 🧹 정리

```bash
terraform destroy
```

## 파일 설명

| 파일 | 설명 |
|------|------|
| main.tf | RDS 및 리소스 정의, 성능 개선 도우미 OFF |
| variables.tf | 입력 변수 정의 |
| outputs.tf | endpoint 출력 |
| terraform.tfvars.example | 설정 예제 |
| init_database.py | DB 초기화 스크립트 |
| QUICK_START.md | 3단계 시작 가이드 |

## ⚠️ 주의

- terraform.tfvars는 .gitignore 설정됨 (비밀번호 보안)
- RDS 생성에는 5-10분 소요
- init_database.py는 terraform apply 후 자동 실행
- 프리티어 범위: db.t3.micro, 20GB 스토리지, 750시간/월
- 성능 개선 도우미 비활성화 (프리티어 최적화)
