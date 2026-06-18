# 업데이트 로그

## 2026-06-17 (일일 루프 #1)
- **신규 사례 3건** 추가 (GitHub HTTP 200 검증 완료)
  1. **EnterpriseRAG-Bench** (Onyx팀, arXiv 2605.05253, 2026-05): 엔터프라이즈 특화 RAG 벤치마크. 50만+ 문서·500 질문·10카테고리·공개 리더보드 → `02-프로덕션-아키텍처.md` 벤치마크 섹션 추가
  2. **Tencent WeKnora v0.6.2** (2026-06-10 릴리즈): 오픈소스 엔터프라이즈 RAG 플랫폼. RAG Q&A + ReAct Agent + Wiki Mode 3-in-1, 16.4k stars → `01-엔터프라이즈-사내지식.md` 글로벌 섹션 추가 (글로벌 11→12)
  3. **AutoRAG** (Marker-Inc-Korea / Markr.AI, 한국): RAG AutoML 파이프라인 자동 최적화 도구. 4.8k stars, Apache-2.0 → `02-프로덕션-아키텍처.md` 한국 기업·솔루션 추가
- `sources.md`에 3개 출처 추가
- `00-요약-트렌드.md` 마지막 업데이트 날짜 및 평가 섹션 보강
- 자가검증 5개 항목 전부 통과 (arXiv 403으로 직접 확인 불가, GitHub 레포 참조로 대체)

## 2026-06-15 (일일 누적 — 사례 9건 합산)

### 추가된 사례
- **[01-엔터프라이즈-사내지식.md]** SK하이닉스 GaiA — 반도체 특화 사내 생성형 AI 플랫폼. Native RAG+LLM → 에이전트 → Agentic AI → A2A 오케스트레이션 4단계 로드맵 공개. Biz 특화 에이전트(장비보전·글로벌정책분석·HR·회의) 2025-07 베타.
- **[02-프로덕션-아키텍처.md]** Databricks Instructed Retriever — 메타데이터 인식 멀티스텝 검색 플랜 생성. InstructedRetriever-4B (TAO + Offline RL), StaRK-Instruct recall 35-50% ↑·답변 정확도 70% ↑. Instructed-Retriever-1(2026-06-04)은 MoE + 병렬 처리로 검색 3배 빠름.
- **[02-프로덕션-아키텍처.md]** Google Gemini Embedding 2 (2026-03-11) — 텍스트·이미지·비디오·오디오·PDF 통합 멀티모달 임베딩, MRL 3072d, ColPali 수준 시각 문서 검색 API화; 트렌드 요약 갱신
- **[03-에이전트-툴유즈-MCP.md]** 카카오페이 결제 MCP Agent Toolkit (2025-08) — MCP 표준으로 결제 API 8개를 AI 에이전트 도구로 노출, LangChain·Vercel·OpenAI SDK 멀티프레임워크 지원. 핀테크 MCP 최초 공개 사례.
- **[03-에이전트-툴유즈-MCP.md]** 삼성리서치 DeepDive — Planner/Supervisor/Researcher 3계층 멀티에이전트가 사내 문서를 리서치·보고서 자동화, Samsung AI Forum 2025 발표
- **[03-에이전트-툴유즈-MCP.md]** LY Corp ODW #5 (2026-05-07) — Flava 벡터 DB + 에이전트 스킬(MCP 툴 래퍼)로 RAG 구현하는 워크숍 실습; tool-discovery 비용 절감 패턴 소개
- **[03-에이전트-툴유즈-MCP.md]** arXiv 2603.07379 SoK: Agentic RAG (2026-03) — Agentic RAG를 POMDP로 형식화, 에이전트 위상·계획·메모리·툴 조정 5축 분류, 평가 방법론 부재·신뢰성 리스크 지적.
- **[03-에이전트-툴유즈-MCP.md]** arXiv 2606.04435 CHARM — Agentic RAG 멀티스텝 파이프라인의 cascading hallucination 감지·차단 프레임워크. 89.4% 감지율·82.1% 에러 전파 감소.
- **[04-산업별-사례.md]** 올거나이즈 한국어 RAG 리더보드(금융·공공·의료·법률·커머스) — 실제 업무 문서(표·이미지 포함) 기반 5개 도메인 한국어 RAG 공개 벤치마크. 테스트 데이터 전체 공개.

### 파일 업데이트 요약
- 01-엔터프라이즈-사내지식.md: 한국 사례 11→12건 (SK하이닉스 GaiA 추가)
- 02-프로덕션-아키텍처.md: Instructed Retrieval 신기술 섹션 신설 + Gemini Embedding 2 추가 + 트렌드 요약 갱신
- 03-에이전트-툴유즈-MCP.md: 카카오페이 MCP·SoK 논문·삼성리서치 DeepDive·LY Corp ODW #5 추가, "2026년 주목할 신규 연구" 섹션 신설 (CHARM 논문)
- 04-산업별-사례.md: 올거나이즈 한국어 RAG 리더보드 추가
- 00-요약-트렌드.md: 한국 사례 목록 업데이트 + 멀티모달 임베딩 트렌드(1.3항) 갱신
- sources.md: 출처 11건 추가

### 검증 메모
- URL 살아있음 검증: 이 실행 환경에서 WebFetch가 HTTP 403(봇 차단)을 반환. 죽은 링크(404)가 아닌 접근 차단이며, 동일 URL에 대해 복수의 독립 검색 결과가 페이지 존재·내용을 확인함.
- 단언 톤다운: 0건
- 중복 폐기: 0건 (Kanana-2 기존 문서 중복 확인 후 폐기)
- 발굴 시도 → 최종 채택: 약 20건 시도 → 9건 채택 (두 에이전트 합산)

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
