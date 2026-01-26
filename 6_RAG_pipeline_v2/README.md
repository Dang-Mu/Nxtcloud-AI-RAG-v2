# RAG Chatbot v2 - React 기반 개선된 아키텍처

계획서(`PLAN.md`)에 따라 구현된 **관리자/사용자 인터페이스 분리** 프로젝트입니다.

## 📁 프로젝트 구조

```
6_RAG_pipeline_v2/
├── backend/                    # FastAPI 백엔드
│   ├── main.py                # API 엔드포인트
│   ├── rag_chatbot.py         # 기존 로직 (참고용)
│   ├── requirements.txt
│   ├── lambda/                # Lambda 함수 (기존)
│   └── db/                    # DB 초기화 스크립트 (기존)
│
└── frontend/                   # React 프론트엔드
    ├── package.json
    ├── public/
    │   └── index.html
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
    │   │   ├── globals.css
    │   │   ├── ChatInterface.css
    │   │   ├── DocumentUpload.css
    │   │   ├── DocumentList.css
    │   │   ├── Modal.css
    │   │   ├── UserPage.css
    │   │   └── AdminPage.css
    │   └── types/
    │       └── index.ts         # TypeScript 타입
    └── .env (필요시 생성)
```

## 🚀 시작하기

### 1. 백엔드 설정

```bash
cd backend

pip install -r requirements.txt

export REACT_APP_API_URL=http://localhost:8000/api
python main.py
```

API는 `http://localhost:8000`에서 실행됩니다.

### 2. 프론트엔드 설정

```bash
cd frontend

npm install

REACT_APP_API_URL=http://localhost:8000/api npm start
```

프론트엔드는 `http://localhost:3000`에서 실행됩니다.

## 🔌 API 엔드포인트

### 사용자 기능

| 메서드 | 엔드포인트 | 설명 |
|--------|----------|------|
| `GET` | `/api/documents` | 문서 목록 조회 |
| `POST` | `/api/chat` | 질문 전송 및 답변 받기 |
| `DELETE` | `/api/chat-history/{session_id}` | 채팅 기록 초기화 |

### 관리자 기능

| 메서드 | 엔드포인트 | 설명 |
|--------|----------|------|
| `GET` | `/api/admin/documents` | 모든 문서 조회 |
| `POST` | `/api/admin/documents` | 새 문서 업로드 |
| `PUT` | `/api/admin/documents/{doc_id}` | 문서 가이드라인 수정 |
| `DELETE` | `/api/admin/documents/{doc_id}` | 문서 삭제 |

## 🎯 주요 특징

✅ **관리자 페이지**
- 📤 PDF 문서 업로드
- 🏷️ 카테고리, 주제, 예시 질문 설정
- 📋 문서 목록 관리
- ✏️ 문서 가이드라인 수정
- 🗑️ 문서 삭제

✅ **사용자 페이지**
- 📚 사용 가능한 문서 확인
- 💬 문서 기반 질문/답변
- 📖 참고 문서 정보 표시
- 🗣️ 대화 기록 초기화

✅ **기술 스택**
- **백엔드**: FastAPI, LangChain, AWS Bedrock, PostgreSQL
- **프론트엔드**: React, TypeScript, Axios
- **스토리지**: AWS S3
- **자동화**: AWS Lambda (S3 이벤트 트리거)

## 🔧 환경 변수

### 백엔드 (`.env`)

```
DB_HOST=localhost
DB_NAME=rag_db
DB_USER=postgres
DB_PASSWORD=****
S3_BUCKET=your-bucket
AWS_REGION=us-east-1
```

### 프론트엔드

```
REACT_APP_API_URL=http://localhost:8000/api
```

## 📊 데이터 흐름

### 사용자 질문

```
React (UserPage) 
  → POST /api/chat 
  → FastAPI (임베딩 생성 → 유사 문서 검색 → LLM 답변)
  → 답변 표시 (참고 문서 포함)
```

### 관리자 문서 업로드

```
React (AdminPage)
  → POST /api/admin/documents
  → FastAPI (S3 업로드)
  → Lambda 자동 트리거 (S3 이벤트)
  → PDF 처리 & 임베딩 생성
```

## 📝 개발 가이드

### 새 컴포넌트 추가

1. `src/components/`에 파일 생성
2. TypeScript 타입 정의 (`src/types/index.ts`)
3. 해당 CSS 파일 생성
4. 페이지에서 import 및 사용

### 새 API 엔드포인트 추가

1. `backend/main.py`에 라우트 추가
2. Pydantic 모델 정의 (요청/응답)
3. `frontend/src/services/api.ts`에 클라이언트 메서드 추가

### 스타일 커스터마이징

- CSS 변수: `globals.css`의 `:root`에서 정의
- 색상, 글꼴, 간격 등 커스텀 가능

## 🧪 테스트

```bash
cd frontend
npm test
```

## 🐛 문제 해결

### API 연결 오류

- 백엔드가 실행 중인지 확인
- `REACT_APP_API_URL` 환경 변수 확인
- CORS 설정 확인

### 데이터베이스 연결 오류

- PostgreSQL 서비스 실행 확인
- `.env` 파일의 DB 자격증명 확인

### 문서 업로드 실패

- S3 버킷 권한 확인
- AWS 자격증명 확인

## 📚 참고

- [계획서](./PLAN.md) - 전체 아키텍처 설명
- [FastAPI 문서](https://fastapi.tiangolo.com/)
- [React 문서](https://react.dev/)

## 📄 라이선스

MIT License
