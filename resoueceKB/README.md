# resoueceKB — Bedrock Knowledge Base 일괄 삭제

이름에 특정 **키워드가 포함된 Bedrock Knowledge Base**와 거기에 딸린 IAM Role / S3 버킷을 한 번에 정리해주는 스크립트입니다.

> 워크숍/교육 환경에서 학생들이 만든 KB를 학기 종료 후 일괄 삭제할 때 유용해요.

---

## 이게 뭐예요?

`python3 delete-kb.py -p <프로필>` 한 번 실행하면:

```
1. Bedrock Knowledge Base 목록 조회 (keyword 포함된 것만)
   ↓
2. 각 KB에 연결된 Data Source / S3 버킷 / IAM Role 수집
   ↓
3. 삭제 대상 목록 출력 → 사용자 확인 (y/n)
   ↓
4. 순서대로 삭제:
   - Data Source 삭제
   - Knowledge Base 삭제
   - S3 버킷 비우기 + 삭제 (모든 버전 포함)
   - IAM Role 삭제 (인라인/관리형 정책 detach 후)
```

⚠️ **삭제된 데이터는 복구되지 않아요.**

---

## 사전 요구사항

| 도구 | 버전 | 설치 방법 |
|------|------|-----------|
| Python | 3.8+ | `brew install python3` |
| boto3 | latest | `pip install boto3` |
| AWS CLI | 2.x | `brew install awscli` |

**AWS 자격증명 설정:**

```bash
aws configure --profile default
# Bedrock + IAM + S3 삭제 권한이 있는 계정 자격증명
```

필요한 IAM 권한:
- `bedrock:ListKnowledgeBases`, `GetKnowledgeBase`, `DeleteKnowledgeBase`
- `bedrock:ListDataSources`, `GetDataSource`, `DeleteDataSource`
- `iam:ListRolePolicies`, `DeleteRolePolicy`, `ListAttachedRolePolicies`, `DetachRolePolicy`, `DeleteRole`
- `s3:ListBucket`, `DeleteObject`, `DeleteObjectVersion`, `DeleteBucket`

---

## 빠른 시작 (3단계)

### 1️⃣ boto3 설치

```bash
pip install boto3
```

### 2️⃣ 삭제 대상 설정 (⚠️ 반드시 수정)

`delete-kb.py` 파일을 열어 **상단 두 값**을 변경하세요:

```python
### 지워야하는 리소스 키워드 ###
keyword = "kmucd1-"          # ⚠️ 삭제할 KB 이름에 포함된 키워드 (대소문자 무시)

### 대상 리전 지정 ###
region_name = 'us-east-1'    # ⚠️ KB가 만들어진 리전
```

**`keyword` 작동 방식:**
- 이름에 이 문자열이 포함된 KB만 삭제 대상
- 예: `keyword = "kmucd1-"` → `kmucd1-team1-kb`, `kmucd1-team2-kb` 모두 매칭
- 너무 짧거나 일반적인 단어(예: `"test"`, `"kb"`)는 의도치 않은 삭제 위험

### 3️⃣ 실행

```bash
python3 delete-kb.py -p default
```

`-p` 옵션은 AWS CLI 프로파일명입니다.

**실행 흐름:**

```
시작

찾은 Knowledge Base 목록:

[KB] kmucd1-team1-kb (ID: ABCD1234)
  IAM Role : AmazonBedrockExecutionRoleForKnowledgeBase_xxx
  S3 버킷  : kmucd1-team1-data-bucket

[KB] kmucd1-team2-kb (ID: EFGH5678)
  IAM Role : AmazonBedrockExecutionRoleForKnowledgeBase_yyy
  S3 버킷  : kmucd1-team2-data-bucket

이 모든 KB / IAM Role / S3 버킷을 삭제하시겠습니까? (y/n):
```

- `y` 입력 → 모든 대상 일괄 삭제
- `n` 입력 → 각 KB마다 개별 확인 (선택 삭제 가능)

---

## 주의사항

### 🚨 삭제는 되돌릴 수 없습니다

- KB가 삭제되면 임베딩된 모든 벡터 데이터가 사라집니다
- S3 버킷이 비워지고 삭제되면 원본 문서도 모두 사라집니다
- IAM Role이 삭제되면 그 Role을 사용하던 다른 리소스도 영향받을 수 있습니다

### 키워드를 신중하게 선택하세요

| ❌ 위험한 키워드 | ✅ 안전한 키워드 |
|---|---|
| `"kb"` (모든 KB 매칭) | `"kmucd1-"` (특정 워크숍만) |
| `"-"` (대부분의 이름 매칭) | `"workshop-2026q1-"` (시기 명시) |
| `"test"` (너무 일반적) | `"sandbox-team-a-"` (구체적) |

### 사전 검증

실행 전에 AWS 콘솔에서 키워드 매칭 결과를 미리 확인하세요:
1. Bedrock 콘솔 → Knowledge bases 메뉴
2. 검색창에 `keyword` 값 입력
3. 매칭되는 KB 목록 확인

---

## 트러블슈팅

### `botocore.exceptions.NoCredentialsError`

→ AWS 자격증명이 설정되지 않았어요. `aws configure --profile <프로필명>` 실행 후 동일한 프로필명을 `-p` 옵션으로 넘기세요.

### `AccessDeniedException`

→ 사용 중인 IAM 사용자/역할에 권한이 부족합니다. 위 [사전 요구사항](#사전-요구사항)의 IAM 권한 목록을 참고해 정책을 추가하세요.

### `ConflictException: Knowledge base in use`

→ KB가 다른 곳(Agent, Application 등)에서 참조되고 있어요. 참조하는 리소스를 먼저 삭제하거나 disconnect 후 재시도하세요.

### S3 버킷 삭제 실패

→ 버전 관리가 활성화된 버킷에 삭제 마커가 남아있을 수 있어요. AWS 콘솔에서 직접 "비어 있음" 상태 확인 후 삭제하세요.

### "지정된 키워드가 포함된 Knowledge Base를 찾을 수 없습니다"

→ `keyword` 값과 `region_name`이 실제 KB와 일치하는지 확인하세요. 다른 리전에 KB가 있을 수 있어요.

---

## 파일 구조

```
resoueceKB/
├── delete-kb.py        # 메인 스크립트 (keyword, region_name을 직접 수정)
├── README.md           # 사용 가이드 (이 파일)
└── guide.html          # HTML 가이드 (브라우저로 열기)
```
