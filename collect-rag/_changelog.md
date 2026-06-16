# 업데이트 로그

## 2026-06-16 (일일 누적 — 사례 3건)

### 추가 내용
- **[01-엔터프라이즈-사내지식.md]** 삼성리서치 — DeepDive Agentic RAG 보고서 생성 서비스 (2026-06-01 Samsung Tech Blog, 작성자 정윤환). Planner/Supervisor/Researcher 멀티에이전트, PPTX·HTML·팟캐스트 등 다형식 출력.
- **[01-엔터프라이즈-사내지식.md]** SK하이닉스 — GaiA 반도체 업무 특화 생성형 AI 플랫폼 (2025-08-14 공식 뉴스룸). RAG+LLM → Agentic AI → A2A 단계적 로드맵, 장비보전·글로벌 정책·HR·회의 4종 에이전트.
- **[03-에이전트-툴유즈-MCP.md]** Google Research — Gemini Enterprise Agent Platform의 Sufficient Context Agent (2026-06 Google Research Blog). multi-hop 쿼리를 스스로 판단하고 재검색, 표준 RAG 대비 factuality +34%.
- **[sources.md]** 위 3건 출처 추가 (Samsung Tech Blog, SK하이닉스 뉴스룸, Google Research Blog)
- **[01-엔터프라이즈-사내지식.md]** 개요·카운트 업데이트 (한국 11→13, 총 26→28)

### 검증 메모
- URL 검증: WebFetch가 이 실행 환경에서 모든 외부 URL에 HTTP 403 반환 (네트워크 봇 차단). 대신 복수의 독립 검색 결과(5건 이상)로 URL 생존 및 내용 일치를 교차 확인.
- 단언 톤다운: 0건 (단언 표현 미사용)
- 중복 폐기: 0건
- 발굴 시도 → 최종 채택: 6건 시도 → 3건 채택 (SK하이닉스 AWS 블로그 2025-02는 기존 AWS 출처 중복 인접, arXiv 2506.00054는 2025-06 논문으로 실무 사례 아님으로 폐기)

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
