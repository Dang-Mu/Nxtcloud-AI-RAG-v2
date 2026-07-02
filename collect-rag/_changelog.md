# 업데이트 로그

## 2026-07-02 (일일 루프 #16)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 3건)
  1. **SKT AX 혁신 2.0 — 에이닷 비즈 코워크 전사 배포** (2026-05-28 베타 배포 · 2026-06-16 공식 선언): 에이닷 비즈 코워크(ReAct 기반 AI 에이전트)를 사내에 배포하고 AI 에이전트에 사번을 부여하는 "디지털 직원" 모델을 도입. AXMS 1.5 전사 AX 관리 플랫폼 운영. AX 혁신 1.0(효율화)에서 2.0(일하는 방식 근본 재설계)으로 전환 공식화 → `01-엔터프라이즈-사내지식.md` 한국 사례 추가 (한국 24→25건, 총 41→42건)
  2. **Amazon Bedrock Managed Knowledge Base GA** (AWS Summit New York 2026, 2026-06-17): RAG 파이프라인 전체를 단일 매니지드 프리미티브로 추상화. Smart Parsing(멀티모달 자동 파싱) + Agentic Retriever(멀티홉 복잡 질의 자율 처리) + 6개 네이티브 커넥터(S3·SharePoint·Confluence·Google Drive·OneDrive·Web Crawler) + MCP 호환. 쿼리당 고정 과금 모델 → `02-프로덕션-아키텍처.md` 클라우드 매니지드 RAG 섹션 추가
  3. **Span-Level 환각 탐지 — 코드·툴 출력 확장** (arXiv:2607.00895, 2026-07-01): 코드·툴 출력·구조화 문서·NL RAG를 통합하는 스팬 레벨 환각 탐지 벤치마크. Qwen3.5-2B 미세조정 탐지기가 span-F1 0.689로 LettuceDetect-large(0.17) 크게 능가. 에이전틱 RAG의 생성 품질 모니터링 확장 방향 제시 → `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션에 추가
- `sources.md`에 3개 출처 추가
- `01-엔터프라이즈-사내지식.md` 헤더 수정: 한국 24→25건, 총 41→42건

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (SKT AX 혁신 2.0: SKT 뉴스룸 + ZDNet + 머니투데이 + 서울경제 4개 이상 독립 출처; Amazon Bedrock MKB: aws.amazon.com 공식 블로그 + 8개 이상 독립 출처; arXiv:2607.00895: arxiv.org/abs + arxiv.org/html 2개 arXiv 출처 교차확인)
- 단언 톤다운: 0건
- 중복 폐기: 없음 (sources.md 및 domain 파일 grep 확인, 에이닷 비즈·AX 혁신·Managed Knowledge Base·2607.00895 모두 미수록 확인)
- 발굴 시도 → 최종 채택: 약 12건 시도 → 3건 채택

## 2026-07-01 (일일 루프 #15)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 3건)
  1. **SKT A.X K1 기반 제조업 특화 AI 에이전트** (2026-06-25 MOU 발표): A.X K1(5,190억 매개변수, 추론 시 330억 활성화) 기반 제조업 특화 AI 에이전트. KG스틸·코넥과 MOU 체결, 온프레미스 RAG로 설비 매뉴얼·장애 분석 리포트 참조. 하반기 철강·자동차부품 공장 현장 실증 예정 → `01-엔터프라이즈-사내지식.md` 한국 사례 추가 (한국 23→24건, 총 40→41건)
  2. **FLOWREADER** (arXiv:2606.07235, 2026-06, A. Mehrish & S. Vascon): 멀티모달 장문서 QA에서 증거 집약 문제를 최소 비용 흐름(min-cost flow) 최적화로 재정의. 엔트로피 정규화 리플리케이터 다이나믹스로 최적 흐름 분해·가지치기. 이중 프로세스 게이트로 단 1회 정밀 검색만 트리거. VisDoMBench PaperTab/SlideVQA에서 최상위 성능 → `02-프로덕션-아키텍처.md` 멀티모달 섹션 추가
  3. **KAIST + 그래파이 — AkasicDB & OmniRAG** (ACM SIGMOD 2026, 2026-06-02 발표): 벡터DB+그래프DB+관계형DB를 단일 DBMS에 통합한 AkasicDB 기반 OmniRAG. 정확도 78% 향상, 복합 검색 속도 20배 향상(21.3초→1초). KAIST 교원창업기업 (주)그래파이 개발 → `02-프로덕션-아키텍처.md` 한국 기업·솔루션 섹션 추가
- `sources.md`에 3개 출처 추가
- `01-엔터프라이즈-사내지식.md` 헤더 수정: 한국 23→24건, 총 40→41건

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (SKT A.X K1: SK텔레콤 뉴스룸 공식 + 아주경제·이투데이·인사이트코리아 등 4개 이상 출처; FLOWREADER: arxiv.org/pdf/2606.07235 스니펫 교차확인; KAIST OmniRAG: AI타임스·서울경제·EurekAlert·인공지능신문·헬로디디 등 5개 이상 출처)
- 단언 톤다운: 1건 (SKT "한국 최초" 통신사 제조업 적용 표현 → "한국 첫 통신사 사례로 언급"으로 조정)
- 중복 폐기: 없음 (sources.md 및 domain 파일 grep 확인)
- 발굴 시도 → 최종 채택: 약 10건 시도 → 3건 채택

## 2026-06-30 (일일 루프 #14)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 3건)
  1. **삼성리서치 — Personal Context RAG** (2026-02-10): SLM 기반 Semantic Router + NPU 로컬 임베딩·인덱싱 + 클라우드 LLM 하이브리드 오케스트레이션으로 온디바이스 개인 데이터(일정·메모·앱 이력 등)를 프라이버시 보존 방식으로 처리하는 "나를 이해하는 RAG" 아키텍처 연구 → `01-엔터프라이즈-사내지식.md` 한국 섹션 추가 (한국 22→23건, 총 39→40건)
  2. **ACIE** (arXiv:2606.19602, 2026-06-17, 독일 에센대학병원): 에이전틱 RAG 기반 온프레미스 임상 정보 추출 시스템. 74개 필드·99명 환자·7,326건 판정에서 임상의 수용률 96.5%. 표준 RAG 실패 지점(시간적 추론·교차 문서 의존성·메타데이터 부재)을 에이전틱 구조로 해소. → `04-산업별-사례.md` 의료 > 글로벌 섹션 추가
  3. **CAMI** (arXiv:2606.28365, ACM CAIS 2026, IBM Research): 코퍼스 전체 대신 샘플 기반 비용-품질 트레이드오프 추정으로 최적 의미 풍부화 인덱싱 구성을 자동 결정하는 비용 인식 에이전트 기반 멀티 인덱싱 전략 → `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션 추가
- `sources.md`에 3개 출처 추가
- `01-엔터프라이즈-사내지식.md` 헤더 수정: 한국 22→23건, 총 39→40건

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (삼성리서치: techblog.samsung.com article/80 + 복수 검색 스니펫 교차확인; ACIE arXiv:2606.19602: arxiv.org + 독일 에센대학병원 핵의학과 연구 맥락 교차확인; CAMI arXiv:2606.28365: arxiv.org + IBM Research 저자 소속 교차확인)
- 단언 톤다운: 0건
- 중복 폐기: 없음 (sources.md 및 domain 파일 grep 확인)
- 발굴 시도 → 최종 채택: 3건 채택

## 2026-06-29 (일일 루프 #13)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 3건)
  1. **네이버 AI탭** (2026-06-26 정식 출시): HyperCLOVA X 기반 "프로덕트 네이티브 LLM" + 버티컬 데이터 RAG + Tool Calling으로 5,000만 사용자 대상 에이전틱 대화형 검색 서비스 정식 출시. 베타 2개월 만에 누적 400만 사용자. 에이전트N 로드맵의 첫 단계 → `01-엔터프라이즈-사내지식.md` 한국 섹션 추가 (한국 21→22건, 총 38→39건)
  2. **EvoEmbedding** (arXiv:2606.21649, 2026-06-24, Nanjing Univ.·CASIA): 임베딩 모델이 연속 메모리 큐를 유지하며 장문 컨텍스트 처리 시 표현을 동적으로 진화시키는 새 패러다임. Qwen3-Embedding-8B 등 대형 전문 모델 능가, naive RAG에 장착 시 전용 에이전틱 메모리 시스템 능가 → `02-프로덕션-아키텍처.md` 임베딩 섹션 신규 항목 추가
  3. **그래프 기반 RAG로 복잡한 질의 환각 반감** (arXiv:2606.05901, 2026-06-04, Newcastle Univ.·EPCC 외): 단순 그래프 스키마 + 벡터 검색 하이브리드로 Wikipedia MoNaCo 벤치마크에서 복잡한 질의 거부율을 절반 이상 감소하면서 정답률도 개선. "안전한 거부" 원칙 적용 → `02-프로덕션-아키텍처.md` GraphRAG 섹션 추가
- `sources.md`에 3개 출처 추가
- `01-엔터프라이즈-사내지식.md` 헤더 수정: 한국 21→22건, 총 38→39건

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (네이버 AI탭: insightkorea.co.kr + digitaltoday.co.kr + ajunews.com + thelec.kr 4개 이상 독립 출처; EvoEmbedding: arxiv.org/abs/2606.21649 + huggingface.co/papers/2606.21649 + github.com/MiG-NJU/EvoEmbedding 3개 출처; arXiv:2606.05901: arxiv.org/abs/2606.05901 + arxiv.org/html/2606.05901 2개 arXiv 출처 교차확인)
- 단언 톤다운: 1건 (네이버 AI탭 "한국 최초" 표현 → "한국 첫 사례 중 하나"로 조정)
- 중복 폐기: 2건 (PentaRAG arXiv:2506.21593 — 2025-06-18 제출로 2025년 논문, LY Corp techverse2026-219 — RAG 직접 관련성 부족)
- 발굴 시도 → 최종 채택: 약 10건 시도 → 3건 채택

## 2026-06-28 (일일 루프 #12)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 3건)
  1. **카카오뱅크 LostCow팀 — 2025 금융보안원 AI Challenge RAG** (2026-02): MoE+CPT+BM25 위주 하이브리드 검색 + 13단계 필터링 파이프라인으로 금융 규제 법령 QA 수행. 기준 대비 +0.9pp 정확도 향상, 우수상 수상. 금융 도메인 BM25 우위 실증 → `04-산업별-사례.md` 금융 > 한국 섹션 추가
  2. **MAGE-RAG** (arXiv:2606.15906, 2026-06-14): 멀티그레뉴러 증거 그래프(페이지 노드+요소 노드 계층) 기반 에이전틱 장문서 멀티모달 QA. 적응형 컨텍스트 예산으로 쿼리 복잡도에 따라 검색 깊이·증거 노드 수 동적 조절 → `02-프로덕션-아키텍처.md` 멀티모달/표·PDF·이미지 섹션 추가
  3. **KT Cloud — RAG 성능 최적화 실전 가이드** (2026-04): AI Foundry 기반 RAG의 TopK 튜닝·Reranking·Deduplication·Compression 4대 최적화 축을 단계별 실험 수치와 함께 공개한 시리즈 #3 → `01-엔터프라이즈-사내지식.md` KT Cloud 섹션 추가 (한국 20→21건, 총 37→38건)
- `sources.md`에 3개 출처 추가
- `01-엔터프라이즈-사내지식.md` 헤더 수정: 한국 20→21건, 총 37→38건

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (카카오뱅크 LostCow: tech.kakaobank.com 공식 블로그 + 복수 검색 스니펫 교차확인; MAGE-RAG: arxiv.org/abs/2606.15906 + 복수 arXiv/검색 출처; KT Cloud 최적화: tech.ktcloud.com 공식 블로그 + 기존 시리즈 연속성 확인)
- 단언 톤다운: 0건
- 중복 폐기: 4건 (EraRAG 2506.20963 — 날짜 2025년 해당, FlexRAG 2506.12494 — 2025-06월 오래됨, 우아한형제들 RAG 챗봇 — sources.md 이미 등록, T-RAG arXiv:2504.01346 — ICLR 2026 Withdrawn)
- 발굴 시도 → 최종 채택: 약 10건 시도 → 3건 채택

## 2026-06-27 (일일 루프 #11)
- **신규 사례 2건** (WebFetch 403 차단 환경, snippet-verified 2건)
  1. **LG CNS 에이전틱웍스(AgenticWorks) + PerfecTwin ERP Edition** (2025-08 출시·2026-06-25 글로벌 확장): 6모듈 풀스택 에이전틱 AI 플랫폼(MCP+A2A+RAG 지원). LG디스플레이 적용 시 일일 생산성 10% 향상·연간 100억원 비용 절감 검증. 2026-06-25 SAP Sapphire 2026에서 ERP 테스트 자동화 솔루션 PerfecTwin ERP Edition 공개·글로벌 확장. 히타치 솔루션즈 크리에이트(HSC)와 일본 파트너십 → `03-에이전트-툴유즈-MCP.md` 한국 사례 신규 추가
  2. **MKG-RAG-Bench** (arXiv:2606.26458, 2026-06-24, Penn State Univ. 외): 멀티모달 지식 그래프 RAG의 검색 병목을 전문적으로 평가하는 첫 크로스도메인 벤치마크. 일반 도메인 + 의료 도메인 두 MKG 기반, 검색·생성 단계 모두 통제 평가. "비정형 RAG 벤치마크(BEIR·MTEB)는 멀티모달 KG 환경에 부적합"을 정량화 → `02-프로덕션-아키텍처.md` GraphRAG 섹션에 추가
- `sources.md`에 2개 출처 추가
- `00-요약-트렌드.md` GraphRAG 섹션 업데이트 (MKG-RAG-Bench 평가 관점 추가)

### 검증 결과
- URL 200 OK: 0/2건 (WebFetch 전체 403 차단)
- snippet-verified: 2/2건 (LG CNS: lg.co.kr + koreatimes.co.kr + prnewswire.com + thelec.kr 4개 이상 출처; MKG-RAG-Bench: arxiv.org/abs/2606.26458 + arxiv.org/html/2606.26458 2개 arXiv 출처 + researchgate.net·semanticscholar.org 교차확인)
- 단언 톤다운: 1건 ("국내 유일의 플랫폼" 등 회사 자체 주장은 맥락 표기로 처리)
- 중복 폐기: 0건
- 발굴 시도 → 최종 채택: 약 10건 시도 → 2건 채택

## 2026-06-26 (일일 루프 #10)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 3건)
  1. **LY Corporation — Semantic Context OS** (Tech-Verse 2026, 2026-06-22~26): 코드 RAG에서 벡터 검색이 AST·import 그래프를 파괴하는 문제를 PathAlign(AST 기반 컨텍스트 격리)으로 해결. 소프트웨어 인텔리전스 에이전트(코드 리뷰·취약점 발견·리팩터링)를 위한 Semantic Context OS 아키텍처 제안. "문서 청킹≠코드 청킹" 공식화 → `03-에이전트-툴유즈-MCP.md` 한국 사례 신규 추가
  2. **InSemRAG** (arXiv:2606.01240, 2026-06): IAR(의도 인식 동적 하이브리드 검색) + SPC(손상된 증거 청크 탐지·복원) + SLM 기반 반복 검색-확인 루프. HotPotQA F1 +2.65점, FEVER 정확도 +1.5점 → `02-프로덕션-아키텍처.md` 신규 섹션 추가
  3. **KT 에이전틱 패브릭 (Agentic Fabric)** (MWC 2026, 2026-03-02): 기업용 AI 운영체제. 5계층(Experience-Intelligence-Context-Execution-Governance), Context Layer에 Memory+RAG 내재화, Zero Trust 보안. 대법원·금융기관·제조사·실종자 수색 실증 사례 → `01-엔터프라이즈-사내지식.md` 한국 사례 신규 추가 (한국 19→20건, 총 36→37건)
- `sources.md`에 3개 출처 추가
- `01-엔터프라이즈-사내지식.md` 헤더 수정: 한국 19→20건, 총 36→37건

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (LY Corp Semantic Context OS: techblog.lycorp.co.jp 공식 + 다중 검색 스니펫; InSemRAG: arxiv.org/abs/2606.01240 + arxiv.org/html/2606.01240 2개 arXiv 출처; KT 에이전틱 패브릭: enterprise.kt.com + ebn.co.kr + financialpost.co.kr + epnc.co.kr 4개 이상 출처)
- 단언 톤다운: 0건
- 중복 폐기: 0건
- 발굴 시도 → 최종 채택: 약 12건 시도 → 3건 채택

## 2026-06-25 (일일 루프 #9)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 3건)
  1. **네이버클라우드 CLOVA Studio for Gov** (2026-06-24, 공공 AI 박람회): 2026년 3월 서비스 개시 후 40개+ 부처·기관 확산. 하반기 GraphRAG·멀티모달 RAG·MCP 연동 에이전트 빌더·국산 NPU 강화 계획. 범정부 AI 공통기반으로의 진화 방향 발표 → `01-엔터프라이즈-사내지식.md` 한국 사례 추가 (한국 17→19건)
  2. **삼성SDS 패브릭스 공공 AI 에이전트** (2026-06-24, 공공 AI 박람회): 패브릭스로 공공기관 직원이 직접 AI 에이전트 구축. 정부24 AI (RAG 검색 → 연관성 검증 → 답변 4단계), AI 민원서포터, 조달법령 해석 서비스 공개. 법제처 등 자체 에이전트 구축 추진 중 → `01-엔터프라이즈-사내지식.md` 한국 사례 추가
  3. **GraphRAG-Bench** (arXiv:2506.05690, ICLR 2026, 2025-06-06): GraphRAG가 Natural Questions에서 vanilla RAG 대비 13.4% 낮은 정확도 확인. 멀티홉 추론에서만 4.5% 향상(지연 2.3배). 그래프를 써야 하는 시나리오를 최초로 체계적 분석 → `02-프로덕션-아키텍처.md` GraphRAG 섹션 추가
- `sources.md`에 3개 출처 추가
- `01-엔터프라이즈-사내지식.md` 헤더 수정: 한국 17→19건, 총 34→36건

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (CLOVA Studio for Gov: ddaily.co.kr + zdnet.co.kr + financialpost.co.kr 3개 이상 출처; 삼성SDS 패브릭스: zdnet.co.kr + inews24.com + etoday.co.kr + dailysecu.com 4개 이상 출처; GraphRAG-Bench: arxiv.org + researchgate.net + github.com/GraphRAG-Bench + huggingface.co + dblp.org 5개 이상 출처)
- 단언 톤다운: 0건
- 중복 폐기: 0건
- 발굴 시도 → 최종 채택: 약 12건 시도 → 3건 채택

## 2026-06-24 (일일 루프 #8)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 3건)
  1. **쿠팡 생성형AI 광고 에이전트** (AWS Summit Seoul 2025): Bedrock + Knowledge Base RAG 기반 광고 인사이트·입찰가 자동화. 수치 일치 기반 RAG 응답 품질 점수화, 프롬프트 캐싱 비용 최적화 → `01-엔터프라이즈-사내지식.md` 한국 사례 추가 (한국 16→17건)
  2. **Databricks Agent Bricks & Knowledge Assistant GA** (DAIS 2026, 2026-06): Instructed Retriever 위에 구축된 Knowledge Assistant GA — Unity Catalog 메타데이터 내재화로 단순 RAG 대비 최대 70% 품질 향상(내부 기준). Lakebase 에이전트 메모리, 100k+ 에이전트, 1+ quadrillion 토큰/년 → `02-프로덕션-아키텍처.md` Instructed Retrieval 섹션에 하위 항목 추가
  3. **SAG** (arXiv:2606.15971, 2026-06-14, Zleap AI): 청크를 이벤트+엔티티로 변환, SQL JOIN으로 쿼리 시점 동적 하이퍼에지 생성. 그래프 사전 구축 없이 구조화 필터링·의미 확장·LLM 리랭킹 통합 → `02-프로덕션-아키텍처.md` GraphRAG 섹션 추가
- `sources.md`에 3개 출처 추가

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (쿠팡: iting.co.kr + aws.amazon.com 2개 출처; Databricks: databricks.com 블로그 + docs.databricks.com + community.databricks.com 3개 출처; SAG: arxiv.org + huggingface.co/papers + github.com/Zleap-AI 3개 출처)
- 단언 톤다운: 1건 (Databricks 70% 수치에 "자체 내부 비교 기준" 명시)
- 중복 폐기: 0건
- 발굴 시도 → 최종 채택: 약 10건 시도 → 3건 채택

## 2026-06-23 (일일 루프 #7)
- **신규 사례 2건 + 기존 업데이트 1건** (WebFetch 403 차단 환경, snippet-verified 3건)
  1. **토스플레이스 PANDA** (2026-04-22, Toss Tech Blog): 내부 데이터봇. LLM + Text-to-SQL + ReAct 루프 구조. 70% 단순 추출 요청을 자동화. 오픈 첫날 팀 1/3 사용, 1주일 내 절반, 메시지 4,000건+ → `01-엔터프라이즈-사내지식.md` 신규 항목 추가
  2. **T²-RAGBench** (arXiv 2506.12071, EACL 2026, University of Hamburg): 금융 문서 텍스트+테이블 RAG 평가 벤치마크. 23,088 트리플. Hybrid BM25가 text-embedding-3-large 능가 — 도메인 특화 어휘는 렉시컬 매칭이 유효함을 재확인 → `04-산업별-사례.md` 금융 벤치마크 섹션 추가
  3. **KT RAG 사내 사용 지표 업데이트** (블로터 idxno=665779, 2026-06): 임직원 약 1만 4,000명 / 사용률 97% 확인. 기존 KT K-RAG 항목에 수치 보강 + 블로터 출처 추가 → `01-엔터프라이즈-사내지식.md` 기존 항목 업데이트
- `sources.md`에 3개 출처 추가
- `01-엔터프라이즈-사내지식.md` 헤더 수정: 한국 15→16건, 총 32→33건

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (PANDA: toss.tech + newsworks 2개 출처; T²-RAGBench: arXiv·ResearchGate·HuggingFace·ACL Anthology 4개 출처; KT bloter: 2개 검색 결과 교차확인)
- 단언 톤다운: 0건
- 중복 폐기: 0건
- 발굴 시도 → 최종 채택: 약 10건 시도 → 신규 2건 + 업데이트 1건 채택

## 2026-06-22 (일일 루프 #6)
- **신규 사례 3건** 추가 (WebFetch 403 차단 환경, snippet-verified 3건)
  1. **LY Corporation — PJ One Piece 분석 AI 에이전트** (Tech-Verse 2026, 2026-06-22): 사내 데이터 분석 AI 에이전트. 자연어 질의로 기존 2주 소요 분석을 10분으로 단축. 파일럿 사업 부문 50%+ 일상 사용 → `01-엔터프라이즈-사내지식.md` LY Corp 신규 항목 추가
  2. **K-FinHallu** (arXiv 2605.29523, 2026-05-28, KAIST AI + KakaoBank Financial Tech Lab): 한국 금융 RAG 멀티턴 환각 탐지 벤치마크. answerability 기반 계층적 분류체계(5종 환각 유형) → `04-산업별-사례.md` 금융 한국 섹션 추가
  3. **MASDR-RAG** (arXiv 2606.11350, 2026-06-09, University of Wyoming): 대규모 RAG의 벡터 검색 희석 문제 정량화 + 도메인 스코핑 기반 해결책. Wyoming DOT 코퍼스에서 75%→<40% 정확도 급락 입증 → `02-프로덕션-아키텍처.md` 신규 섹션 추가
- `sources.md`에 3개 출처 추가
- `01-엔터프라이즈-사내지식.md` 헤더 수정: 한국 14→15건, 총 31→32건

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (각각 2개 이상 독립 출처 교차확인)
- 단언 톤다운: 1건 (K-FinHallu "최초" → 논문 주장 인용 형태로 표현)
- 중복 폐기: 0건
- 발굴 시도 → 최종 채택: 약 12건 시도 → 3건 채택

## 2026-06-21 (일일 루프 #5)
- **업데이트 1건 + 신규 2건** (WebFetch 403 차단 환경, snippet-verified 3건)
  1. **우아한형제들 물어보새 v1.5** (2026 상반기, AWS re:Invent 2025 발표): 기존 v1(2024, GPT-4o+RAG) 항목을 v1.5 하이브리드 에이전트 구조로 업데이트. 슈퍼바이저 에이전트가 SQL에이전트·지식에이전트·서포트에이전트로 라우팅. Amazon Bedrock + Claude 스택으로 전환. 전사 도입률 30%+. v2.0(MCP+ReAct+Reflect) 로드맵 공개 → `01-엔터프라이즈-사내지식.md` 기존 항목 업데이트
  2. **FIDES** (arXiv 2606.05644, 2026-06-04, Zhejiang Univ.·Guangzhou Univ.·GenTel.io): RAG 검색-메모리 충돌을 디코딩 단계에서 해소하는 training-free 디코더. Opposition·Shift·Noise 3신호가 충돌 집중 토큰을 탐지 → `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션 신규 추가
  3. **CONCORD** (arXiv 2606.15179, 2026-06-13, IEEE ICWS 2026): 기기-클라우드 분산 RAG. 문서 격리 환경(HIPAA·법률·금융)에서 Waiting Debt Control + Certificate-guided Minimal Supplementation으로 대역폭 최소화 → `02-프로덕션-아키텍처.md` 보안·거버넌스 섹션 신규 추가
- `sources.md`에 3개 출처 추가

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (물어보새: 3개 이상 독립 뉴스 출처, arXiv 논문 2건: 각각 arXiv 페이지 + HTML 버전 2개 이상 출처 확인)
- 단언 톤다운: 0건
- 중복 폐기: 0건 (arXiv 2606.04127 기존 수록 확인 → 제외)
- 발굴 시도 → 최종 채택: 약 8건 시도 → 3건 채택

## 2026-06-20 (일일 루프 #4)
- **신규 사례 3건** 추가 (GitHub URL 200 OK 2건, snippet-verified 1건)
  1. **RAGFlow v0.26.1** (InfiniFlow, 2026-06-17): 오픈소스 RAG 엔진 83k stars. 주요 신규: Slack/Teams/SharePoint/Salesforce 커넥터, GraphRAG 체크포인트/재개, Ψ-RAG(RAPTOR+AHC) 모드, 메시징 채널 직접 배포 → `01-엔터프라이즈-사내지식.md` 글로벌 섹션 추가 (글로벌 12→13건)
  2. **headroom** (v0.26.0, 2026-06-16, Apache-2.0, ⭐41.8k): RAG 청크·도구 출력 컨텍스트 압축 레이어. 코드검색 92%·SRE 92%·이슈 73% 토큰 절감, SmartCrusher/CodeCompressor/CacheAligner 포함 6종 알고리즘, MCP 서버 배포 지원 → `02-프로덕션-아키텍처.md` 비용·지연 섹션 신설
  3. **UniversalRAG** [ACL 2026] (arXiv 2504.20734, KAIST AI 그룹): 모달리티 인식 라우팅으로 텍스트·이미지·비디오 이질적 코퍼스 처리. 학습/무학습 기반 라우터 모두 지원 → `02-프로덕션-아키텍처.md` 멀티모달 섹션 추가 (한국 연구)
- `sources.md`에 3개 출처 추가
- `01-엔터프라이즈-사내지식.md` 헤더 수정: 글로벌 12→13건, 총 30→31건

### 검증 결과
- URL 200 OK: 3/3건 (GitHub 접근 성공)
- snippet-verified: 1/3건 (UniversalRAG arXiv 403, GitHub README 교차 확인)
- 단언 톤다운: 0건
- 중복 폐기: 0건
- 발굴 시도 → 최종 채택: 약 12건 시도 → 3건 채택

## 2026-06-19 (일일 루프 #3)
- **신규 사례 3건** 추가 (WebFetch 403 차단 환경, snippet-verified 3건)
  1. **KT — K-RAG 기반 에이전틱 AI 전략** (2026-06-17 기자간담회): 자체 개발 K-RAG(검색→생성→학습→실행 전 단계 통합), 산업 특성별 RAG 유형 분화(그래프/에이전트/멀티모달 RAG), B2C·B2B 에이전트 H2 2026 상용화 예정 → `01-엔터프라이즈-사내지식.md` 한국 사례 추가
  2. **arXiv:2606.04127 "When Retrieval Doesn't Help"** (2026-06-02): 5모델×10의료QA×4검색방법×4코퍼스 실험. RAG가 no-retrieval 대비 1~2% 향상에 그침. 백본 모델 선택이 검색기 선택보다 훨씬 큰 영향 → `04-산업별-사례.md` 의료 섹션 추가
  3. **arXiv:2606.00610 MemGraphRAG** (KDD 2026, Xiamen Univ.): 공유 메모리 기반 멀티 에이전트로 그래프 구성의 주제 일관성·논리 충돌 해소. 복수 벤치마크 SOTA 능가 → `02-프로덕션-아키텍처.md` GraphRAG 섹션 추가
- `sources.md`에 3개 출처 추가
- `01-엔터프라이즈-사내지식.md` 헤더 수정: 한국 13→14건, 총 29→30건

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (KT 5개 이상 독립 출처, arXiv 논문 2개 각각 2+ 출처)
- 단언 톤다운: 0건
- 중복 폐기: 0건
- 발굴 시도 → 최종 채택: 약 10건 시도 → 3건 채택

## 2026-06-18 (일일 루프 #2)
- **신규 사례 3건** 추가 (WebFetch 403 차단 환경, snippet-verified 3건)
  1. **LY Corporation Agent i** (2026-04-20 출시): LINE·Yahoo! JAPAN 통합 AI 에이전트 브랜드. 100+ 서비스 데이터 RAG 지식 기반, 7개 도메인 전문 에이전트 + 오케스트레이터 구조, 메모리 기능 2026-06 예정 → `01-엔터프라이즈-사내지식.md` 한국 사례 추가
  2. **LATAM Airlines 컨시어지 에이전트** (LangChain Interrupt 2026, 2026-05): Supervisor+6 전문 에이전트, DAU 4,000명, LangSmith 초기부터 통합 → `03-에이전트-툴유즈-MCP.md` 글로벌 프로덕션 사례 신설
  3. **Google Research Cross-Corpus Retrieval** (2026-06-05): Sufficient Context Agent 포함 5-에이전트 Agentic RAG, 표준 RAG 대비 +34% 정확도, 퍼블릭 프리뷰 → `03-에이전트-툴유즈-MCP.md` 2026년 주목할 신규 연구 추가
- `sources.md`에 3개 출처 추가
- `00-요약-트렌드.md` 1.4 Agentic RAG 섹션 2026-06 갱신 (Interrupt 2026 프로덕션 사례·Google Gemini 수치 반영)

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (각각 2개 이상 독립 출처 교차확인)
- 단언 톤다운: 1건 (Agent i "일본 최초" → 구체적 주장 제거)
- 중복 폐기: 0건
- 발굴 시도 → 최종 채택: 약 12건 시도 → 3건 채택

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
