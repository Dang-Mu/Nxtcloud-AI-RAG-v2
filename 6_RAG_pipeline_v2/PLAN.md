# RAG Chatbot 구조 개선 계획
## React 기반 사용자/관리자 인터페이스 분리

---

## 📋 현재 상황

`rag_chatbot.py` (Streamlit)에서 **관리자와 사용자 기능이 섞여있음**

```
rag_chatbot.py (단일 파일)
├─ 📤 관리자: 문서 업로드, 삭제
└─ 💬 사용자: 질문, 답변
```

**문제**: 관리자와 사용자 인터페이스가 동일 파일에서 관리됨

---

## 🎯 개선 목표

**기존 백엔드 로직은 그대로 유지**하고, **프론트엔드만 React로 분리**:

1. **관리자 페이지**: 문서 업로드, 삭제, 가이드라인 관리
2. **사용자 페이지**: 질문, 답변, 대화 기록

---

## 📁 디렉토리 구조

### 백엔드 (기존 유지)
```
backend/
├── rag_chatbot.py        # 기존 로직 (수정 최소화)
├── lambda/
│   └── lambda_function.py # 기존 PDF 처리
└── db/
    └── create_db.py      # 기존 DB 스키마
```

### 프론트엔드 (신규 - React)
```
frontend/
├── package.json
├── src/
│   ├── index.tsx
│   ├── App.tsx
│   ├── pages/
│   │   ├── UserPage.tsx      # 사용자 페이지 (질문/답변)
│   │   └── AdminPage.tsx     # 관리자 페이지 (문서 관리)
│   ├── components/
│   │   ├── ChatInterface.tsx     # 채팅 UI
│   │   ├── DocumentUpload.tsx    # 파일 업로드
│   │   ├── DocumentList.tsx      # 문서 목록
│   │   ├── DocumentDelete.tsx    # 삭제 모달
│   │   └── GuidelineForm.tsx     # 가이드라인 입력
│   ├── services/
│   │   └── api.ts           # API 호출
│   ├── styles/
│   │   └── globals.css
│   └── types/
│       └── index.ts         # TypeScript 타입
└── public/
```

---

## 🔄 기능 분류

### 사용자 페이지 (`UserPage.tsx`)

**역할**: 문서에서 정보 찾기

```
화면 구성:
┌─────────────────────────────────┐
│  🔍 문서 기반 질의응답 시스템    │
└─────────────────────────────────┘

📚 사용 가능한 문서
├─ 학사규정 (2024)
│  ❓ 질문 가능: 졸업요건, 수강신청
│  💡 예: "4년 안에 졸업?"
│
└─ 학생생활안내
   ❓ 질문 가능: 기숙사, 장학금
   💡 예: "1학년 기숙사?"

─── 채팅 ───
[사용자]: "졸업요건이 뭐야?"
[답변]: "대학생이 졸업하기 위해..."
        📚 참고한 문서 (페이지 정보)

💬 질문 입력: _________________
[🗑️ 대화 초기화]
```

**기능**:
- ✅ 업로드된 문서 목록 + 가이드라인 표시
- ✅ 채팅 인터페이스 (질문 입력)
- ✅ 답변 + 참고 문서 표시
- ✅ 대화 기록 초기화

**Streamlit 코드 위치**:
```python
# 기존 rag_chatbot.py의 다음 부분 참고
- st.title("🔍 문서 기반 질의응답 시스템")
- search_query = st.chat_input(...)
- 질문 처리 로직 (lines 215-267)
```

---

### 관리자 페이지 (`AdminPage.tsx`)

**역할**: 문서 관리 (업로드, 삭제)

```
화면 구성:
┌─────────────────────────────────┐
│  👨‍💼 문서 관리                    │
└─────────────────────────────────┘

📤 새 문서 업로드
┌──────────────────────┐
│ 파일 선택            │
│ [파일 선택...]       │
│                      │
│ 제목:                │
│ [입력...]            │
│                      │
│ 설명:                │
│ [입력...]            │
│                      │
│ 카테고리:            │
│ [규정 ▼]            │
│                      │
│ 질문 가능 주제:      │
│ [+ 졸업요건]         │
│ [+ 수강신청]         │
│                      │
│ 예시 질문:           │
│ [+ "4년 안에?"]      │
│                      │
│ [🚀 업로드]         │
└──────────────────────┘

─── 등록된 문서 목록 ───
| # | 제목 | 카테고리 | 등록일 | 작업 |
|---|------|----------|--------|------|
| 1 | 학사규정 2024 | 규정 | 2024-01-20 | [수정][🗑️]
| 2 | 학생생활안내 | 학사 | 2024-01-15 | [수정][🗑️]
```

**기능**:
- ✅ PDF 파일 업로드
- ✅ 문서 제목/설명 입력
- ✅ 카테고리 선택
- ✅ 질문 가능 주제 입력
- ✅ 예시 질문 입력
- ✅ 등록된 문서 목록 조회
- ✅ 문서 삭제 (확인 모달)
- ✅ 가이드라인 수정

**Streamlit 코드 위치**:
```python
# 기존 rag_chatbot.py의 다음 부분 참고
- with st.sidebar: (lines 139-197)
  - st.file_uploader(...)
  - st.button("🚀 처리 시작")
  - 파일 업로드 로직 (lines 163-192)
```

---

## 🔌 백엔드 API 엔드포인트

### 기존 Streamlit 앱을 간단한 API로 변환

> **주의**: Lambda는 여전히 S3 이벤트로 자동 트리거됨. 추가 작업 불필요.

#### 사용자 기능

```
GET /api/documents
응답:
{
  "documents": [
    {
      "id": 1,
      "title": "학사규정 2024",
      "category": "규정",
      "queryable_topics": ["졸업요건", "수강신청"],
      "example_questions": ["4년 안에 졸업?"]
    }
  ]
}

POST /api/chat
요청:
{
  "query": "졸업요건이 뭐야?",
  "session_id": "user_123"
}

응답:
{
  "response": "대학생이 졸업하기 위해서는...",
  "sources": [
    {
      "content": "...",
      "page": 1
    }
  ]
}

DELETE /api/chat-history/{session_id}
응답:
{
  "status": "success"
}
```

#### 관리자 기능

```
GET /api/admin/documents
응답: 모든 문서 목록

POST /api/admin/documents
요청: 문서 업로드 (multipart/form-data)
- file: PDF 파일
- title: 문서 제목
- description: 설명
- category: 카테고리
- queryable_topics: 질문 주제 (JSON)
- example_questions: 예시 질문 (JSON)

응답:
{
  "status": "success",
  "document_id": 1,
  "message": "문서가 업로드되었습니다"
}

DELETE /api/admin/documents/{doc_id}
응답:
{
  "status": "success",
  "message": "문서가 삭제되었습니다"
}

PUT /api/admin/documents/{doc_id}
요청: 가이드라인 수정
응답: 업데이트된 문서 정보
```

---

## 🏗️ React 컴포넌트 구조

### UserPage.tsx
```typescript
export default function UserPage() {
  // 1. 문서 목록 + 가이드라인 표시
  // 2. 채팅 인터페이스
  // 3. 질문 입력 & 답변 표시
  // 4. 참고 문서 표시
}
```

### AdminPage.tsx
```typescript
export default function AdminPage() {
  // 1. 문서 업로드 폼
  // 2. 등록된 문서 목록 (테이블)
  // 3. 삭제/수정 기능
  // 4. 가이드라인 관리 폼
}
```

### 공유 컴포넌트

**ChatInterface.tsx**
- 메시지 표시
- 질문 입력
- 스트리밍 답변 표시

**DocumentUpload.tsx**
- 파일 선택
- 메타데이터 입력
- 업로드 진행률

**DocumentList.tsx**
- 테이블로 문서 목록 표시
- 검색/필터링

**DocumentDelete.tsx**
- 확인 모달
- 삭제 실행

**GuidelineForm.tsx**
- 카테고리 선택
- 주제/예시 질문 입력

---

## 📋 DB 스키마 확장 (필요시)

기존 `documents` 테이블에 추가:

```sql
-- 기존 테이블
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    content TEXT,
    embedding vector(1536),
    metadata JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 신규: 문서 메타데이터 (선택사항)
CREATE TABLE document_metadata (
    id SERIAL PRIMARY KEY,
    document_id INT REFERENCES documents(id),
    title VARCHAR(255),
    description TEXT,
    category VARCHAR(50),
    queryable_topics JSONB,      -- ["졸업요건", "수강신청"]
    example_questions JSONB,     -- ["4년 안에?"]
    uploaded_by VARCHAR(255),
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

또는 **기존 metadata JSONB 확장**:
```python
metadata = {
    "page": 1,
    "title": "학사규정 2024",
    "category": "규정",
    "queryable_topics": ["졸업요건"],
    "example_questions": ["4년?"]
}
```

---

## 🚀 구현 순서

### Phase 1: 백엔드 최소 수정
1. 기존 `rag_chatbot.py`를 FastAPI 또는 Flask로 래핑
   - 현재 로직은 그대로 유지
   - 간단한 API 엔드포인트만 추가

### Phase 2: React 프론트엔드
2. React 프로젝트 생성
3. 사용자 페이지 구현
4. 관리자 페이지 구현
5. API 클라이언트 구현

### Phase 3: 통합
6. 프론트엔드 ↔ 백엔드 연결
7. 전체 테스트

---

## 📊 데이터 흐름 (간단함)

### 사용자 질문
```
React (UserPage)
  ↓ POST /api/chat {"query": "..."}
Streamlit 백엔드 (기존 로직)
  ↓ 임베딩 생성 → 유사 문서 검색 → LLM 답변
React (UserPage)
  ↓ 답변 표시
```

### 관리자 문서 업로드
```
React (AdminPage)
  ↓ POST /api/admin/documents {file, metadata}
Streamlit/FastAPI 백엔드
  ↓ S3 업로드
  ↓ Lambda 자동 트리거 (S3 이벤트)
  ↓ PDF 처리 & 임베딩 생성
React (AdminPage)
  ↓ "업로드 완료" 메시지
```

---

## ✅ 최종 효과

| 항목 | Before | After |
|------|--------|-------|
| UI | Streamlit (한 페이지) | React (사용자/관리자 분리) |
| 사용자 경험 | 섞여있음 | 깔끔함 |
| 관리자 경험 | 섞여있음 | 명확함 |
| 기존 로직 | - | 그대로 유지 |
| 개발 복잡도 | - | 낮음 |

---

## 🛠️ 필요한 것

1. **FastAPI 또는 Flask**: 기존 로직을 API로 래핑
2. **React**: 프론트엔드 UI
3. **기존 코드**: rag_chatbot.py, lambda_function.py (수정 최소화)

---

## 💡 핵심 포인트

- ✅ **백엔드 로직은 그대로**
- ✅ **프론트엔드만 React로 분리**
- ✅ **관리자/사용자 페이지 명확히 분리**
- ✅ **Lambda는 S3 이벤트로 자동 처리** (추가 구성 불필요)
- ✅ **복잡함 제거**

