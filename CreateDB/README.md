# CreateDB — PostgreSQL RDS 자동 배포

AWS Default VPC에 PostgreSQL RDS 인스턴스를 만들고, 사용자/DB/테이블(pgvector 포함)을 자동으로 초기화합니다.

> **AWS 프리티어 최적화** — 단일 AZ, db.t3.micro, 성능 개선 도우미 OFF

---

## 이게 뭐예요?

`./deploy.sh` 한 번 실행하면 다음이 자동으로 만들어져요:

```
RDS 인스턴스 (nxtcloud-postgres)
└─ 초기 DB: nxtcloud_db ⭐ (RDS 생성 시 자동 생성)
   │
   ├─ db_01  (소유자: user_01)
   │  ├─ document_files          # 원본 파일 메타데이터
   │  └─ documents (pgvector)    # 임베딩 벡터 저장
   │
   └─ db_02  (소유자: user_02)
      ├─ document_files
      └─ documents (pgvector)
```

`num_users` 값을 바꾸면 user_03, db_03... 도 자동 생성됩니다.

---

## 사전 요구사항

| 도구 | 버전 | 설치 방법 |
|------|------|-----------|
| Terraform | 1.0+ | https://www.terraform.io/downloads |
| AWS CLI | 2.x | `brew install awscli` |
| Python | 3.8+ | `brew install python3` |

**AWS 자격증명 설정:**

```bash
aws configure --profile default
# AWS Access Key ID, Secret Key, region, output 입력
```

---

## 빠른 시작 (3단계)

### 1️⃣ 설정 파일 생성

```bash
cp config.example.yaml config.yaml
```

`config.yaml`을 열어 **반드시 변경할 값**:

```yaml
aws_profile:            "default"             # AWS CLI 프로필명
aws_region:             "us-east-1"           # 배포 리전
db_instance_identifier: "nxtcloud-postgres"   # ⚠️ 환경별로 유일한 이름 (예: workshop-team-a)
db_master_password:     "your-secure-pwd"     # ⚠️ 강력한 비밀번호로 변경 (8자 이상)
num_users:              2                     # ⚠️ 워크숍 참가자/학생 수에 맞춰 설정
```

> 비밀번호에 `/`, `@`, `"`, 공백은 사용할 수 없어요.
> `db_instance_identifier`는 같은 계정/리전 안에서 유일해야 합니다.

### 2️⃣ 배포 실행

```bash
./deploy.sh
```

배포 진행 단계:
1. AWS 자격증명 확인
2. Terraform 초기화 (1분)
3. RDS 인스턴스 생성 (**5~10분 소요**)
4. `init_database.py` 자동 실행 → DB/사용자/테이블 생성

성공하면 마지막에 엔드포인트가 출력돼요:

```
[DEBUG]   엔드포인트:  nxtcloud-postgres.xxxxx.us-east-1.rds.amazonaws.com
[DEBUG]   포트:        5432
```

### 3️⃣ 접속 테스트

```bash
# 엔드포인트 가져오기
ENDPOINT=$(terraform output -raw endpoint)

# 마스터 DB 접속
psql -h $ENDPOINT -U postgres -d nxtcloud_db

# DB 목록 확인
\l

# 사용자 db_01에 접속해서 테이블 확인
psql -h $ENDPOINT -U user_01 -d db_01
\dt
```

> `psql`이 없다면 `brew install postgresql` 또는 DBeaver / TablePlus 같은 GUI 클라이언트로 접속하셔도 됩니다.

---

## 정리 (삭제)

```bash
./destroy.sh
```

확인 프롬프트(`yes` 입력)를 거친 후 RDS 인스턴스와 모든 데이터를 삭제합니다.
**주의: DB 데이터는 복구되지 않아요.**

---

## 설정 항목

전체 설정은 `config.example.yaml`에 주석과 함께 있어요. 자주 바꾸는 항목만 정리하면:

| 항목 | 기본값 | 설명 |
|------|--------|------|
| `aws_profile` | `default` | AWS CLI 프로필 |
| `aws_region` | `us-east-1` | 배포 리전 |
| **`db_instance_identifier`** | `nxtcloud-postgres` | **반드시 변경** — 계정/리전 내 유일한 이름 |
| `instance_class` | `db.t3.micro` | 프리티어. 운영용은 `db.t3.medium`+ |
| `allocated_storage` | `20` | GB. 프리티어 최대 20 |
| `database_name` | `nxtcloud_db` | 초기 DB 이름 (자동 생성) |
| `db_master_username` | `postgres` | 마스터 사용자명 |
| **`db_master_password`** | — | **반드시 변경** — 강력한 비밀번호 |
| **`num_users`** | `2` | **반드시 변경** — 워크숍 참가자/학생 수에 맞춰 설정 |

### 고정 설정 (변경 불가)

비용 절감을 위해 다음 값은 코드에 고정되어 있어요:

| 설정 | 값 | 이유 |
|------|----|----|
| `skip_final_snapshot` | `true` | 삭제 시 스냅샷 비용 발생 안함 |
| `performance_insights_enabled` | `false` | 비용 절감 |
| `enabled_cloudwatch_logs_exports` | `[]` | 비용 절감 |
| `publicly_accessible` | `true` | 외부 접속 허용 (보안그룹 0.0.0.0/0) |

> **운영 환경**에서는 `publicly_accessible`을 `false`로, 보안그룹 CIDR을 회사 IP로 제한하세요.

---

## 파일 구조

```
CreateDB/
├── config.yaml             # 배포 설정 (gitignored, 직접 생성)
├── config.example.yaml     # 설정 템플릿
│
├── deploy.sh               # 배포 (config 읽고 terraform apply)
├── destroy.sh              # 삭제 (확인 프롬프트 후 destroy)
│
├── main.tf                 # RDS, 보안그룹, 서브넷 그룹 정의
├── variables.tf            # Terraform 변수
├── outputs.tf              # endpoint 출력
│
├── init_database.py        # DB/사용자/테이블 자동 초기화 (terraform apply 시 호출)
└── requirements.txt        # Python 의존성 (psycopg2-binary)
```

---

## 트러블슈팅

### `AWS 자격증명 확인 실패`

→ `aws configure --profile <프로파일명>` 으로 자격증명 등록 후 `config.yaml`의 `aws_profile`과 일치시키세요.

### `db_master_password를 안전한 값으로 변경하세요`

→ `config.yaml`에서 `db_master_password`가 기본값(`your-secure-password`) 그대로면 차단됩니다. 변경 후 다시 실행하세요.

### RDS 생성은 됐는데 `init_database.py` 실행에서 실패

→ `init_database.log` 파일을 확인하세요. 보통 보안그룹이 외부 IP를 막고 있는 경우인데, `main.tf`의 보안그룹은 기본적으로 `0.0.0.0/0` 5432를 열어둡니다. 회사 방화벽이 아웃바운드 5432를 막고 있다면 다른 네트워크에서 시도해보세요.

### 다시 배포하고 싶어요

→ `./destroy.sh` 후 `./deploy.sh` 다시 실행하세요. 같은 식별자(`db_instance_identifier`)로 재생성하면 시간이 약간 걸릴 수 있습니다 (스냅샷 정리).

### `terraform.tfstate`가 사라졌어요

→ Terraform 상태 파일이 없으면 `destroy.sh`로는 리소스를 지울 수 없습니다. AWS 콘솔에서 직접 RDS 인스턴스를 삭제해야 해요.

---

## 비용 안내

프리티어 기준 (12개월):
- db.t3.micro: 월 750시간 무료
- 20GB gp3 스토리지: 무료
- 백업 스토리지: DB 사이즈만큼 무료

프리티어 종료 후 예상 비용 (us-east-1, 24/7 가동):
- db.t3.micro: 약 $13/월
- 스토리지 20GB: 약 $2.3/월
- **합계: 약 $15/월**

테스트 후 사용하지 않으면 반드시 `./destroy.sh`로 삭제하세요.
