# 업데이트 로그

## 2026-06-15 (일일 누적 — 사례 6건)

### 추가된 사례
- **[01-엔터프라이즈-사내지식.md]** SK하이닉스 GaiA — 반도체 특화 사내 생성형 AI 플랫폼. Native RAG+LLM → 에이전트 → Agentic AI → A2A 오케스트레이션 4단계 로드맵 공개. Biz 특화 에이전트(장비보전·글로벌정책분석·HR·회의) 2025-07 베타.
- **[02-프로덕션-아키텍처.md]** Databricks Instructed Retriever — 메타데이터 인식 멀티스텝 검색 플랜 생성. InstructedRetriever-4B (TAO + Offline RL), StaRK-Instruct recall 35-50% ↑·답변 정확도 70% ↑. Instructed-Retriever-1(2026-06-04)은 MoE + 병렬 처리로 검색 3배 빠름.
- **[03-에이전트-툴유즈-MCP.md]** 카카오페이 결제 MCP Agent Toolkit (2025-08) — MCP 표준으로 결제 API 8개를 AI 에이전트 도구로 노출, LangChain·Vercel·OpenAI SDK 멀티프레임워크 지원. 핀테크 MCP 최초 공개 사례.
- **[03-에이전트-툴유즈-MCP.md]** arXiv 2603.07379 SoK: Agentic RAG (2026-03) — Agentic RAG를 POMDP로 형식화, 에이전트 위상·계획·메모리·툴 조정 5축 분류, 평가 방법론 부재·신뢰성 리스크 지적.
- **[03-에이전트-툴유즈-MCP.md]** arXiv 2606.04435 CHARM — Agentic RAG 멀티스텝 파이프라인의 cascading hallucination 감지·차단 프레임워크. 89.4% 감지율·82.1% 에러 전파 감소.
- **[04-산업별-사례.md]** 올거나이즈 한국어 RAG 리더보드(금융·공공·의료·법률·커머스) — 실제 업무 문서(표·이미지 포함) 기반 5개 도메인 한국어 RAG 공개 벤치마크. 테스트 데이터 전체 공개.

### 파일 업데이트 요약
- 01-엔터프라이즈-사내지식.md: 한국 사례 11→12건 (SK하이닉스 GaiA 추가)
- 02-프로덕션-아키텍처.md: Instructed Retrieval 신기술 섹션 신설
- 03-에이전트-툴유즈-MCP.md: 카카오페이 MCP·SoK 논문 한국 사례 추가, "2026년 주목할 신규 연구" 섹션 신설 (CHARM 논문)
- 04-산업별-사례.md: 올거나이즈 한국어 RAG 리더보드 추가
- 00-요약-트렌드.md: 한국 사례 목록 업데이트 (SK하이닉스 추가)
- sources.md: 출처 8건 추가 (SK하이닉스 뉴스룸 1, AWS 블로그 1, Databricks 블로그 2, arXiv 2, 카카오페이 MCP 1, 올거나이즈 1)

### 검증 메모
- URL 살아있음 검증: 이 실행 환경에서 WebFetch가 HTTP 403(봇 차단)을 반환. 죽은 링크(404)가 아닌 접근 차단이며, 동일 URL에 대해 복수의 독립 검색 결과가 페이지 존재·내용을 확인함.
  - news.skhynix.co.kr/ai-platform-gaia-launching-2025/ → 403 / 검색 스니펫 다수 확인
  - databricks.com/blog/instructed-retriever-… → 403 / VentureBeat·InfoWorld·TechTarget 등 독립 보도 내용 일치 확인
  - arxiv.org/abs/2606.04435 → 403 / 제목·저자·수치 복수 검색 결과로 확인
- 단언 톤다운: 0건 (단언 표현 없음)
- 중복 폐기: 0건 (Kanana-2 기존 문서 중복 확인 후 폐기)
- 발굴 시도 → 최종 채택: 약 11건 시도 → 6건 채택
- 브랜치: `daily/rag-trends-2026-06-15`

## 2026-06-10 (초기 셋업)
- 리서치 폴더 구조 생성
- 4개 도메인 병렬 초기 리서치 시작

## 2026-06-10 (03 도메인 초기 작성)
- 03-에이전트-툴유즈-MCP.md 작성: Agentic RAG 정의 분화, MCP 표준화, 코딩 에이전트 논쟁, 메모리 시스템, RAG vs Long Context/Fine-tuning, 한국 사례(네이버 플레이스·LY Flava·카카오 PlayMCP/Kanana), 실패 모드
- sources.md에 80+개 출처 추가 (Anthropic 공식, MCP 사례, CRAG/Self-RAG, 코딩 에이전트, 메모리 벤더, 멀티에이전트, OpenAI/Google, 브라우저 에이전트, 컨퍼런스, 한국 사례)

## 2026-06-10 (04 산업별 사례 작성)
- 04-산업별-사례.md 작성: 금융·의료·법률·교육 4개 산업 각각 글로벌/한국 사례, 특이 패턴, 규제·거버넌스 정리
- 공통 패턴 + 실패·논란 사례(Mata v. Avianca, Air Canada, Stanford 법률 AI 평가, Epic MyChart, Robin AI 구조조정, Chegg, Mayo Clinic) 추가
- sources.md에 산업별 사례 출처 ~80개 추가 (Bloomberg·Morgan Stanley·JPMorgan·Goldman·Citi, Epic·Microsoft·Abridge·Nabla·Hippocratic·OpenEvidence·Glass·Mayo, Harvey·CoCounsel·LexisNexis·Hebbia·Robin AI, Khanmigo·Duolingo·MagicSchool·NotebookLM·Study Mode·QANDA·Riiid·교육부 AIDT, 규제·거버넌스)

## 2026-06-10 (01 엔터프라이즈 사내지식 + 02 프로덕션 아키텍처 작성)
- 01-엔터프라이즈-사내지식.md 작성: 한국 11(네이버 플레이스·우아한형제들·LY/LINE·카카오엔터프라이즈·SKT·카카오뱅크·포스코·신한·KB국민카드·KT Cloud·포스타입), 글로벌 11(M365·Glean·Rovo·Slack AI·Cisco·Salesforce·Klarna·Morgan Stanley·JPMorgan·Uber·Spotify·LinkedIn·DoorDash·Walmart·Stack Overflow·Anthropic·NotebookLM), 코드베이스 4(Copilot·Cody·Tabnine·Cursor)
- 02-프로덕션-아키텍처.md 작성: 벡터DB·임베딩·청킹(Contextual Retrieval·Late Chunking)·검색·리랭킹·질의 변환·평가·캐싱·신선도·멀티모달(ColPali)·GraphRAG(LazyGraphRAG)·보안·한국 환경 12개 영역
- sources.md에 130+개 출처 추가

## 2026-06-10 (00 종합 요약 작성 — 초기 리서치 완료)
- 00-요약-트렌드.md 작성: 10개 메가 트렌드, 디폴트 스택, 2024→2026 변화 표, 실패 모드 통합, 한국 특이점, 향후 관전 포인트
- 초기 심층 리서치 단계 완료. 다음 단계: /loop 점진적 누적
