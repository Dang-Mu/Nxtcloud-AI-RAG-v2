# 업데이트 로그

## 2026-08-13 (일일 루프 #58)
- **신규 사례 3건** (WebFetch 전면 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **LG CNS × 동아쏘시오그룹 AI 신약개발 플랫폼 (2026-08-12)** [한국 사례]: LG CNS의 제약·바이오 특화 에이전틱 AI 플랫폼 '에이전틱웍스(AgenticWorks) for BIO' 기반으로 동아쏘시오그룹 IT 계열사 DAI와 약 6개월 구축. Knowledge Lake(GraphRAG + 벡터 임베딩 + 지식 그래프 자동 매핑 + RAGAS 평가)로 화합물·유전체 정보·실험 결과·논문·특허를 통합. 단계별 AI 지원: 질병 분석→치료 표적 발굴→후보물질 생성형 AI 설계→가상 검증. snippet-verified (ZDNet Korea + 한국경제 + 파이낸셜뉴스 + 뉴스와이어 + 뉴스웨이 + 이지경제 + 시사저널e + CBC뉴스 9개 이상 독립 출처). → `04-산업별-사례.md` JMIR 연구 다음에 추가
  2. **RAG-TESTER (arXiv:2608.00054, 2026-08)**: Ange Maiztegi, Jon Ayerdi, Miren Illarramendi, Aitor Arrieta (Mondragon University, 스페인). RAG 파이프라인의 다양한 LLM·임베딩·검색 메커니즘·프롬프트 조합별 실패 행태 차이를 4단계 자동화 엔드투엔드 테스팅으로 대응. 테스트 케이스 자동 생성 → 실행 → LLM-as-judge 평가. CI/CD 통합 가능한 회귀 탐지 프레임워크. snippet-verified (arXiv abs + arXiv html + Mondragon University 3개 이상 독립 출처). → `02-프로덕션-아키텍처.md` MEGRAG 다음 신규 연구 섹션에 추가
  3. **Guardian Crawler (arXiv:2608.08994, KDIR 2026)**: Joshua Castillo, Santosh Nukavarapu, Ravi Mukkamala. 노이즈 웹 데이터에서 BM25 + 4단 리랭킹 스택 + 명시적 인용 기반 제한적 RAG 생성을 결합한 검색 우선(retrieval-first) 지식 발굴 테스트베드. 사이버보안·허위정보·리스크 모니터링 도메인 타겟. KDIR 2026 단편 논문 채택. snippet-verified (arXiv abs + arXiv html + cs/pastweek listing 3개 독립 출처). → `02-프로덕션-아키텍처.md` RAG-TESTER 다음에 추가

| 사례 | 도메인 | 검증 방법 | 출처 수 | 한국 여부 |
|------|--------|-----------|---------|----------|
| LG CNS × 동아쏘시오그룹 AI 신약개발 플랫폼 (2026-08-12) | 04-산업별 의약/바이오 | snippet-verified | 9개 이상 | ✅ 한국 |
| RAG-TESTER (arXiv:2608.00054, 2026-08) | 02-프로덕션 자동화 테스팅 | snippet-verified | 3개 이상 | 글로벌 (스페인) |
| Guardian Crawler (arXiv:2608.08994, KDIR 2026) | 02-프로덕션 검색 우선 설계 | snippet-verified | 3개 이상 | 글로벌 |

- `sources.md`에 3개 출처 추가 (## 2026-08-13 일일 누적 추가 출처 섹션 신설)
- `04-산업별-사례.md` 헤더 날짜 2026-08-13 업데이트 + LG CNS × 동아쏘시오그룹 사례 JMIR 다음에 추가
- `02-프로덕션-아키텍처.md` 헤더 날짜 2026-08-13 업데이트 + RAG-TESTER + Guardian Crawler MEGRAG 다음에 추가
- `00-요약-트렌드.md` 업데이트(2026-08-13, 사례 216+건, 출처 322+)
- **검증 결과**: URL 200 OK: 0/3건(전면 WebFetch 차단) · snippet-verified: 3/3건 · 단언 톤다운: 0건 · 중복 폐기: 0건 · 발굴 시도 → 최종 채택: 약 12건 시도 → 3건 채택

## 2026-08-12 (일일 루프 #57)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 연구자 포함 사례 1건)
  1. **CoinRAG (arXiv:2608.07458, 2026-08-07)** [한국 연구자 — Cheoneum Park, 한밭대학교]: Gyuwan Kim(UC Santa Barbara), Cheoneum Park(한밭대학교), Tao Yang(UC Santa Barbara). 장문 RAG에서 기존 청크 수준 KV 캐시 재사용의 정보 중복·노이즈 문제를 너겟(information nugget) 수준 캐시 분해·재사용으로 해소. 오프라인 계산된 너겟 KV 캐시를 온라인에서 컨텍스트화·재조합(compositional reuse). 낮은 프리필 레이턴시 제약 하 정확도-효율 파레토 프런티어 최적화. snippet-verified (arXiv abs + arXiv html + Eye on AI 3개 이상 독립 출처). → `02-프로덕션-아키텍처.md` SAGE 다음에 추가
  2. **RAG 지식 추출 공격·방어 체계적 벤치마크 (arXiv:2602.09319, KDD 2026, 제주 2026-08-09~13 발표)**: Zhisheng Qi, Utkarsh Sahu 외 10인. RAG 지식 추출 공격(knowledge-extraction attack)·방어에 대한 최초 체계적 벤치마크. 다양한 공격·방어 전략, 검색 임베딩 모델, 오픈/클로즈드 소스 생성기를 표준화된 프로토콜로 다국어·복수 데이터셋에 걸쳐 평가. 제로샷 추출도 비무시 성공률. 쿼리 필터링·프롬프트 인젝션 저항성 방어가 위험 완화. IP 도용·프라이버시 유출 우려 있는 RAG 코퍼스 보호 실용 지침 제공. snippet-verified (arXiv abs + arXiv html v3 + Huggingface Papers + liner.com 4개 이상 독립 출처). → `03-에이전트-툴유즈-MCP.md` WARP 다음에 추가
  3. **MEGRAG (arXiv:2608.02195, 2026-08-03)**: Weidong Bao, Yingying Sun, Jun Yang 외 7인. 멀티홉 QA RAG에서 단일 세분도 증거의 노이즈 문제와 중간 홉 오류 누적을 동시에 해소하는 답변-인식 다중 세분도 증거 그래프 프레임워크. 오프라인 교차 세분도 인덱스(패시지→문장→트리플) 구축 후 온라인에서 compact triple부터 순차적으로 컨텍스트 추가. snippet-verified (arXiv abs + arXiv html 2개 독립 출처). → `02-프로덕션-아키텍처.md` 신규 연구 섹션 NeSy-RAG 다음에 추가

| 사례 | 도메인 | 검증 방법 | 출처 수 | 한국 여부 |
|------|--------|-----------|---------|----------|
| CoinRAG (arXiv:2608.07458, 2026-08-07) | 02-프로덕션 KV 캐시 효율화 | snippet-verified | 3개 이상 | ✅ 한국 연구자 (Cheoneum Park, 한밭대학교) |
| RAG 지식 추출 벤치마크 (arXiv:2602.09319, KDD 2026) | 03-에이전트 보안/공격 | snippet-verified | 4개 이상 | 글로벌 (KDD 2026 제주 발표) |
| MEGRAG (arXiv:2608.02195, 2026-08-03) | 02-프로덕션 멀티홉 RAG | snippet-verified | 2개 | 글로벌 |

- `sources.md`에 3개 출처 추가 (## 2026-08-12 일일 누적 추가 출처 섹션 신설)
- `02-프로덕션-아키텍처.md` 헤더 날짜 2026-08-12 업데이트 + CoinRAG(SAGE 다음) + MEGRAG(신규연구 섹션) 추가
- `03-에이전트-툴유즈-MCP.md` WARP 다음에 지식 추출 벤치마크 추가
- `00-요약-트렌드.md` 업데이트(2026-08-12, 사례 213+건, 출처 319+)
- **검증 결과**: URL 200 OK: 0/3건(arXiv 전면 차단) · snippet-verified: 3/3건 · 단언 톤다운: 0건 · 중복 폐기: 0건 · 발굴 시도 → 최종 채택: 약 10건 시도 → 3건 채택

## 2026-08-11 (일일 루프 #56)
- **신규 사례 2건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 0건 — 발굴 시도 후 폐기)
  1. **EvoTrustRAG: Evolution-Aware Conflict Attribution and Evidence Handling for Reliable Retrieval-Augmented Generation (arXiv:2608.07933, 2026-08-08)**: Xi Nie, Hongwei Li, Shenghao Wu, Wenshu Fan, Qiyang Song, Wenbo Jiang. RAG 충돌 해소 연구에서 최초로 "충돌 기원 귀인(Conflict Origin Attribution)"을 독립 서브태스크로 정의 — "어느 사실이 맞는가" 대신 "왜 충돌이 발생했는가"를 식별. 충돌 증거 그래프(스팬 노드 + 시간·보조 관계 엣지) 구성 → 진화·조작 가설 점수화 → 전역 일관성 투영. 훈련 불필요. 귀인 매크로-F1 72.2%→79.1%, 조율 공격 오류율 31.2%→16% 감소. snippet-verified (arXiv abs + arXiv html 2개 이상 독립 출처). → `02-프로덕션-아키텍처.md` DCCD 다음에 추가
  2. **SAGE: SLO-Aware Adaptive Retrieval for Production RAG Systems (arXiv:2608.08237, IEEE CoDIT 2026, 2026-08-08)**: Muhammad Faizan Raza, Shuo (Luna) Yang, Satish Mahadevan Srinivasan. 프로덕션 RAG의 고정 k 검색이 꼬리 지연 SLO와 비용 SLO를 동시에 충족할 수 없는 문제를 오프라인 모방 학습 기반 경량 정책으로 해결. 쿼리별 점수 분포·랭크 간격·어휘 신호만 사용해 추가 LLM 호출 없이 동적 k 결정. P95 5초 SLO 준수율 95%(최강 정적 기준선 30%), P95 지연 36% 감소, 검색 비용 51% 절감. snippet-verified (arXiv abs + arXiv html + Scribd 3개 이상 독립 출처). → `02-프로덕션-아키텍처.md` CA-RAG 다음에 추가

| 사례 | 도메인 | 검증 방법 | 출처 수 | 한국 여부 |
|------|--------|-----------|---------|----------|
| EvoTrustRAG (arXiv:2608.07933, 2026-08-08) | 02-프로덕션 충돌 해소 | snippet-verified | 2개 | 글로벌 |
| SAGE (arXiv:2608.08237, IEEE CoDIT 2026, 2026-08-08) | 02-프로덕션 비용·지연 | snippet-verified | 3개 이상 | 글로벌 |

- **한국 사례 탐색 결과**: 데이터메티카(enetnews.co.kr 2026-08-11 보도, 선박·항만 RAG LLM) 발굴 → 독립 출처 1개(enetnews.co.kr 단독 보도)로 snippet-verified 기준(최소 2개 독립 출처) 미달 → 폐기
- `sources.md`에 2개 출처 추가 (## 2026-08-11 일일 누적 추가 출처 섹션 신설)
- `02-프로덕션-아키텍처.md` 헤더 날짜 2026-08-11 업데이트 + EvoTrustRAG(DCCD 다음) + SAGE(CA-RAG 다음) 추가
- `00-요약-트렌드.md` 업데이트(2026-08-11, 사례 210+건, 출처 316+)

## 2026-08-10 (일일 루프 #55)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 2건 포함)
  1. **Before Reasoning Fails: Pre-Evidence Procedural Failures in Agentic RAG (arXiv:2608.02011, 2026-08-03)** [한국 사례]: Daeyoung Roh(Independent Researcher) × Donghee Han(KAIST). 에이전틱 RAG 실패를 "사전-증거 규율 실패(pre-evidence discipline failure)"와 "사후-골드-읽기 실패(post-gold-read failure)"로 분해. 12,000 paired trajectory(HotpotQA·2WikiMultiHopQA·MuSiQue) 분석. 두 실패 유형은 대체로 비중복(both-trigger 비율 11.2~13.1%). Read-Gate 경량 런타임 정책으로 읽기 건너뛴 궤적에서 LLM-Acc +14.9~19.9 포인트. snippet-verified (arXiv abs + arXiv html + AI 분석 블로그 3개 이상 독립 출처). → `03-에이전트-툴유즈-MCP.md` WARP 다음에 추가
  2. **HALT: Verification-Aware Stopping for Retrieval-Augmented Search Agents (arXiv:2608.02009, 2026-08-03)** [한국 사례]: 동일 저자(KAIST Donghee Han). RAG 검색 에이전트 중단 기준을 생성기 신뢰도에서 **증거 커버리지(evidence coverage)**로 전환하는 HALT 경량 검증-인식 정책. 홉 클레임을 질문에서 생성→누적 증거가 모든 클레임 지지 시 검색 중단. 3개 멀티홉 QA 벤치마크에서 중복 검색 감소 + EM 보존. Before Reasoning Fails(2608.02011)의 동반 논문. snippet-verified (arXiv abs + arXiv html 2개 이상 독립 출처). → `03-에이전트-툴유즈-MCP.md` Before Reasoning Fails 다음에 추가
  3. **TA-RAG: Tone Awareness as a Design Imperative for Retrieval-Augmented Generation (arXiv:2608.06672, 2026-08-07)**: Yong-Bin Kang, Anthony McCosker (Swinburne University of Technology, 호주). 검색된 문서의 커뮤니케이션 스타일이 RAG 출력 어조를 지배해 사용자 톤 지시를 무력화하는 **"컨텍스트 분리(contextual decoupling)"** 현상 규명. 단순 프롬프트로는 해결 불가한 구조적 결함, 톤-인식 검색 레이어 통합 필요. 콜센터·의료·법률 등 수신자 맞춤 어조가 핵심인 도메인에서 설계 원칙으로 확산 가능. snippet-verified (arXiv abs + arXiv html 2개 이상 독립 출처). → `02-프로덕션-아키텍처.md` LLM-Generated Text Harms Retrieval 다음에 추가

| 사례 | 도메인 | 검증 방법 | 출처 수 | 한국 여부 |
|------|--------|-----------|---------|----------|
| Before Reasoning Fails (arXiv:2608.02011, 2026-08-03) | 03-에이전트 실패 모드 | snippet-verified | 3개 이상 | ✅ 한국 (KAIST Donghee Han) |
| HALT (arXiv:2608.02009, 2026-08-03) | 03-에이전트 효율화 | snippet-verified | 2개 이상 | ✅ 한국 (KAIST Donghee Han) |
| TA-RAG (arXiv:2608.06672, 2026-08-07) | 02-프로덕션 설계 원칙 | snippet-verified | 2개 이상 | 글로벌 (Swinburne, 호주) |

- `sources.md`에 3개 출처 추가 (## 2026-08-10 일일 누적 추가 출처 섹션 신설)
- `03-에이전트-툴유즈-MCP.md` WARP 다음에 Before Reasoning Fails + HALT 추가
- `02-프로덕션-아키텍처.md` LLM-Generated Text 다음에 TA-RAG 추가, 헤더 날짜 2026-08-10 업데이트
- `00-요약-트렌드.md` 업데이트(2026-08-10, 사례 208+건, 출처 314+)

## 2026-08-09 (일일 루프 #54)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **법무법인 율촌 × BHSN — 폐쇄형 RAG 리걸 AI '아이율(AI:Yul)' 전사 가동 (2026-01-12)** [한국 사례]: BHSN(법률 특화 AI 스타트업) × 법무법인 율촌(Yulchon LLC, 국내 4대 로펌). BHSN의 법률 특화 멀티 LLM 플랫폼 '앨리비 아스트로(Allibee Astro)' 기반 폐쇄형 RAG 아키텍처. 외부로 데이터 전송 없이 독립된 내부 망 환경에서 AI 작동, 대화 내용 AI 학습 미사용. 기존 사내 KM 시스템과 직접 연동. **국내 대형 로펌 최초 폐쇄형 RAG 도입 사례**. snippet-verified (VentureSquare + 전자신문 + hellot + aitimes + bhsn.ai 보도자료 5개 이상 독립 출처). → `04-산업별-사례.md` 법률 > 한국 섹션 미디어젠 다음에 추가
  2. **WARP: A Word-Level Backdoor Attack Targeting RAG Systems via Retrieval Corpus Poisoning (KDD 2026, ACM DL: 10.1145/3770854.3780227)**: Hui Liu, Yibo Zhou, Liguo Dong, Weidong Li, Shui Yu (Central China Normal University). 단어 수준 트리거를 임베딩 공간에 유사하도록 설계한 적대적 텍스트로 RAG 코퍼스를 오염시키는 최초의 단어 수준 백도어 공격 프레임워크. 기존 문서 단위 오염 대비 탐지 어려움. KDD 2026(2026-08-09~13, 제주, Pages 867-878). snippet-verified (ACM DL DOI + RAG backdoor 연구 포털 2개 이상 독립 출처). → `03-에이전트-툴유즈-MCP.md` SecureCollaRAG 다음에 추가
  3. **"LLM-Generated Text May Harm Your Retrieval! A Robust Detection Strategy for RAG" (ACL 2026 Long, aclanthology:2026.acl-long.1475)**: Zhaoheng Huang, Yutao Zhu, Ji-Rong Wen, Zhicheng Dou (Renmin University of China / Gaoling School of AI). LLM 텍스트 탐지기를 RAG 파이프라인 검색 단계에 통합해 AI 생성 텍스트 필터링하는 강건화 전략. RAD(Retrieval-Aware Detection) 데이터 증강 전략. 4가지 LLM 텍스트 생성 패러다임(완전 생성·부분 생성·패러프레이즈·후편집)별 영향 분석. snippet-verified (ACL Anthology abs + ACL 2026 accepted papers 목록 + PDF 링크 3개 독립 출처). → `02-프로덕션-아키텍처.md` SIRIN 다음에 추가

| 사례 | 도메인 | 검증 방법 | 출처 수 | 한국 여부 |
|------|--------|-----------|---------|----------|
| 법무법인 율촌 × BHSN 아이율 (2026-01-12) | 04-산업별 법률·한국 | snippet-verified | 5개 이상 | ✅ 한국 (BHSN×율촌) |
| WARP (KDD 2026, ACM DL: 10.1145/3770854.3780227) | 03-에이전트 보안/공격 | snippet-verified | 2개 이상 | 글로벌 (Central China Normal Univ.) |
| LLM-Generated Text Harms Retrieval (ACL 2026, aclanthology:1475) | 02-프로덕션 검색 강건성 | snippet-verified | 3개 | 글로벌 (Renmin Univ. of China) |

- `sources.md`에 3개 출처 추가 (## 2026-08-09 일일 누적 추가 출처 섹션 신설)
- `04-산업별-사례.md` 법률 > 한국 섹션에 아이율 추가
- `03-에이전트-툴유즈-MCP.md` SecureCollaRAG 다음에 WARP 추가
- `02-프로덕션-아키텍처.md` SIRIN 다음에 LLM-Generated Text Harms Retrieval 추가
- `00-요약-트렌드.md` 업데이트(2026-08-09, 사례 205+건, 출처 311+)

## 2026-08-08 (일일 루프 #53)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **카카오 Kanana SLM 개발기 (tech.kakao.com/posts/826, 2026-07-28)** [한국 사례]: 카카오 Kanana LLM 조직. 온디바이스용 한국어·영어 경량 SLM Kanana-2 1.3B/3B 4종 Apache-2.0 오픈소스 공개. RAG-Gen Grounding 32.63 → 57.38, 한국어 토크나이저 처리 효율 30% 향상. snippet-verified (6개 이상 독립 출처). → `02-프로덕션-아키텍처.md` 한국 환경 특이점 > 한국 기업·솔루션 섹션에 추가
  2. **SecureCollaRAG (arXiv:2608.04366, ACM WWW 2026, 2026-08-05)**: "Combating Knowledge Corruption in Agent Systems: A Byzantine-Tolerant Secure Collaborative RAG Framework". 멀티에이전트 RAG에서 지식 부패 공격을 GNN 기반 신뢰도 스코어링 + Byzantine-tolerant 집계로 방어. 3 컴포넌트: Distributed Knowledge Graph Construction · GNN Credibility Scoring · Verification-based Aggregation. snippet-verified (arXiv abs + arXiv html + ACM DL DOI 3개). → `03-에이전트-툴유즈-MCP.md` DenialRAG 다음에 추가
  3. **SIRIN (arXiv:2608.00033, 2026-08)**: "SIRIN: A Unified Toolkit for Detecting Contextual Hallucinations in Retrieval-Augmented and Memory-Grounded LLM Systems". Julia Belikova 외. 3가지 탐지 패러다임(representation probing · uncertainty estimation · judge-style verification) 통합 툴킷 + 웹 UI. pre-generation query answerability 모듈·span-level 검사·white-box/black-box 지원. snippet-verified (arXiv abs + arXiv html 2개). → `02-프로덕션-아키텍처.md` GASP 다음에 추가

| 사례 | 도메인 | 검증 방법 | 출처 수 | 한국 여부 |
|------|--------|-----------|---------|----------|
| 카카오 Kanana SLM (tech.kakao.com/posts/826) | 02-프로덕션 한국 기업·솔루션 | snippet-verified | 6개 이상 | ✅ 한국 (카카오) |
| SecureCollaRAG (arXiv:2608.04366) | 03-에이전트 보안/공격 | snippet-verified | 3개 | 글로벌 (ACM WWW 2026) |
| SIRIN (arXiv:2608.00033) | 02-프로덕션 환각 탐지 | snippet-verified | 2개 | 글로벌 |

- `sources.md`에 3개 출처 추가 (## 2026-08-08 일일 누적 추가 출처 섹션 신설)
- `02-프로덕션-아키텍처.md` SIRIN(환각 탐지 섹션 GASP 다음) + Kanana SLM(한국 기업·솔루션 섹션) 추가
- `03-에이전트-툴유즈-MCP.md` SecureCollaRAG(DenialRAG 다음) 추가
- `00-요약-트렌드.md` 업데이트(2026-08-08, 사례 202+건, 출처 308+)

## 2026-08-07 (일일 루프 #52)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **NeSy-RAG: Neuro-Symbolic Retrieval-Augmented Generation (arXiv:2608.06292, 2026-08-06)**: Heidelberg University Data and Web Science Group (Jonas Gann, Michael Gertz). Prolog 모듈 기반 신경-기호 통합 RAG. 검색 패시지에서 1차 논리 사실 추출 → Prolog 적재 → 규칙 기반 추론으로 완전한 추론 추적(trace) 제공. 대화형 QA 벤치마크 ShARC: 61.1% vs. 표준 RAG 42.8%(+18pp). arXiv abs + arXiv html + Heidelberg DS Group + ResearchGate 4개 독립 출처 snippet-verified. → `02-프로덕션-아키텍처.md` 2026년 주목할 신규 연구 섹션에 추가
  2. **RH-RAG: A Multi-Agent RAG Framework for Privacy-Constrained Long-Form Generation (arXiv:2608.01311, 2026-08-02)**: Raj Shekhar Singh (IIT Roorkee). Planner-Writer-Checker 3-에이전트 프레임워크로 기밀 내부 문서(의료·법률·금융) 대상 프라이버시 제약 장문 생성. NLI 기반 Checker가 각 클레임을 소스로 검증. arXiv abs + arXiv html 2개 독립 출처 snippet-verified. → `02-프로덕션-아키텍처.md` 보안·거버넌스 섹션에 추가
  3. **JMIR 연구 — 한국 의료 RAG 평가 (JMIR Formative Research 2026;10:e72604, 2026-04-30)** [한국 사례]: 10.4 GB 한국어 의료 코퍼스, 487,277개 청크(의학 교과서·임상 가이드라인·학술 논문). 5개 LLM 비교 평가 및 메타데이터 필터링 효과 실증. 핵심 발견: 문서 유형 메타데이터 필터링이 한국 의료 RAG 성능의 결정적 요인. 2개 독립 WebSearch 출처 snippet-verified. → `04-산업별-사례.md` 의료 > 한국 섹션 뷰노 다음에 추가

| 사례 | 도메인 | 검증 방법 | 출처 수 | 한국 여부 |
|------|--------|-----------|---------|----------|
| NeSy-RAG (arXiv:2608.06292) | 02-프로덕션 신규 연구 | snippet-verified | 4개 | 글로벌 (Heidelberg Univ.) |
| RH-RAG (arXiv:2608.01311) | 02-프로덕션 보안·거버넌스 | snippet-verified | 2개 | 글로벌 (IIT Roorkee) |
| JMIR 한국 의료 RAG (e72604) | 04-산업별 의료·한국 | snippet-verified | 2개 | ✅ 한국 |

- `sources.md`에 3개 출처 추가 (## 2026-08-07 일일 누적 추가 출처 섹션 신설)
- `02-프로덕션-아키텍처.md` NeSy-RAG(신규 연구 섹션) + RH-RAG(보안·거버넌스 섹션) 추가
- `04-산업별-사례.md` 의료 > 한국 섹션 JMIR 연구 추가
- `00-요약-트렌드.md` 업데이트(2026-08-07, 사례 199+건, 출처 305+)

## 2026-08-06 (일일 루프 #51)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **KoVRE: Training an Efficient Embedding Model for Korean Visual Document Retrieval (arXiv:2608.01389, 2026-08)** [한국 사례]: 경희대학교(Kyung Hee University) + 고려대학교(Korea University) 연구팀. 708,729개 한국어·영어 쿼리-페이지 쌍으로 단일 벡터 검색기(single-vector retriever) 임베딩 모델 학습. 긍정 인식 하드 네거티브 마이닝 + 리랭커 기반 지식 증류 통제 실험으로 최적 학습 레시피 도출. 한국어 시각 문서(PDF·슬라이드·표) 전용 공개 임베딩 모델. arXiv abs + arXiv html 2개 독립 출처 snippet-verified. → `02-프로덕션-아키텍처.md` 검색 섹션 LG Uplus 한국 사례 다음에 추가
  2. **RAGOCR: Optical Compression of Retrieval-Augmented Text via Visual Representation (arXiv:2608.00765, 2026-08-01)**: 北京大学 왕쉬안 연구소. 검색 문서를 이미지로 렌더링 후 쿼리-인식 동적 해상도 메커니즘으로 압축. 나이브 RAG 대비 정확도 +15% 이상, 입력 토큰 1/8 수준으로 절감. 텍스트 대신 시각 표현으로 RAG 컨텍스트를 압축하는 새 패러다임. arXiv abs + arXiv html 2개 독립 출처 snippet-verified. → `02-프로덕션-아키텍처.md` JKO-RAG 다음에 추가
  3. **SciRet: A Compute-Aware Empirical Study of Retrieval and Reranking for Scientific RAG (arXiv:2608.03860, 2026-08-04)**: Laurentian University + North South University. CORD-19 코퍼스 3개 규모(1K·5K·15K) 통제 실험. BM25+BGE-M3+RRF 하이브리드 검색이 전 규모에서 Recall@10=1.000 달성. MS MARCO 학습 교차 인코더 리랭커가 과학 코퍼스에서 정밀도를 오히려 낮춤(도메인 불일치). arXiv abs + arXiv html 2개 독립 출처 snippet-verified. → `04-산업별-사례.md` 신규 `## 과학·학술` 섹션 신설

| 사례 | 도메인 | 검증 방법 | 출처 수 | 한국 여부 |
|------|--------|-----------|---------|----------|
| KoVRE (arXiv:2608.01389) | 02-프로덕션 임베딩 | snippet-verified | 2개 | ✅ 한국 (경희대+고려대) |
| RAGOCR (arXiv:2608.00765) | 02-프로덕션 컨텍스트 압축 | snippet-verified | 2개 | 글로벌 (Peking Univ.) |
| SciRet (arXiv:2608.03860) | 04-산업별 과학·학술 | snippet-verified | 2개 | 글로벌 (Laurentian+NSU) |

- `sources.md`에 3개 출처 추가 (## 2026-08-06 일일 누적 추가 출처 섹션 신설)
- `02-프로덕션-아키텍처.md` 헤더 업데이트(2026-08-06) + KoVRE·RAGOCR 추가
- `04-산업별-사례.md` 헤더 업데이트(2026-08-06) + `## 과학·학술` 섹션 신설(SciRet)
- `00-요약-트렌드.md` 업데이트(2026-08-06, 사례 196+건, 출처 302+)

## 2026-08-05 (일일 루프 #50)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **삼성SDS — KDD 2026 Korea Day: 400+ 시스템·5M 문서 기반 엔터프라이즈 RAG 플랫폼 (2026-08-11 발표)** [한국 사례]: 그룹 전체 400개 이상 이기종 시스템(ERP·HR·업무 포털 등), 50,000+ 테이블, 500만+ 비정형 문서를 통합해 1,000개 이상의 AI 에이전트·LLM 챗봇을 운영하는 엔터프라이즈 AI 지식 기반 플랫폼. 보안 RAG 파이프라인 + 문서 접근 제어 + 셀프서비스 AI 플랫폼(도메인 전문가 노코드 에이전트 생성). KDD 2026 Korea Day 특별 플레너리 세션(2026-08-11, 제주 ICC)에서 Google Jeff Dean 기조연설 다음 발표 슬롯. kdd2026.kdd.org/korea-day/ + beri.net/events/kdd-2026 + samsungsds.com 3개 이상 독립 출처 snippet-verified. → `01-엔터프라이즈-사내지식.md` 한국 사례 섹션에 추가
  2. **DocNavRAG: Document-Structured Graph RAG with Stateful Evidence Construction (arXiv:2608.01565, 2026-08-03)**: 문서 계층 구조와 문서 간 교차 영역 관계를 탐색 가능한 그래프(navigable graph)로 조직. 4가지 그래프 연산(locate·navigate·expand·fetch) + 상태 기반 증거(stateful evidence)로 충분한 증거 확보 시까지 검색 유도. 4개 장문서·멀티 문서 QA 벤치마크에서 답변 품질 +7.8%, 컨텍스트 충분성 +17.7%. Wuhan Univ. + HKUST + CUHK + ETH Zurich. arXiv abs + arXiv html 2개 독립 출처 snippet-verified. → `02-프로덕션-아키텍처.md` GraphRAG 섹션에 추가
  3. **DenialRAG: Single-Document RAG Poisoning via Embedded Parametric Denial (arXiv:2608.02678, 2026-08-02, ACSAC 2026 제출)**: 올바른 답을 명시적으로 언급한 뒤 부정(denial)하고 공격자 제어 오답을 제시하는 단일 문서 중독 공격. 3가지 오픈도메인 QA × 8개 LLM(4개 벤더) × 5개 방어 기법 체계적 벤치마크. 모든 Mistral-7B 데이터셋에서 기존 4개 단일 문서 포이즈닝 공격 대비 최고 ASR 달성. arXiv abs + arXiv html + redteams.ai 3개 독립 출처 snippet-verified. → `03-에이전트-툴유즈-MCP.md` 보안/공격 섹션에 추가

| 사례 | 도메인 | 검증 방법 | 출처 수 | 한국 여부 |
|------|--------|-----------|---------|----------|
| 삼성SDS KDD 2026 Korea Day | 01-엔터프라이즈 | snippet-verified | 3개 이상 | ✅ 한국 |
| DocNavRAG (arXiv:2608.01565) | 02-프로덕션 GraphRAG | snippet-verified | 2개 | 글로벌 |
| DenialRAG (arXiv:2608.02678) | 03-에이전트 보안 | snippet-verified | 3개 | 글로벌 |

- `sources.md`에 3개 출처 추가 (## 2026-08-05 일일 누적 추가 출처 섹션 신설)
- `01-엔터프라이즈-사내지식.md` 헤더 업데이트(2026-08-05, 한국 32→, 총 49건) + 삼성SDS 섹션 추가
- `02-프로덕션-아키텍처.md` GraphRAG 섹션에 DocNavRAG 추가
- `03-에이전트-툴유즈-MCP.md` 와이즈넛 이후 DenialRAG 섹션 추가
- `00-요약-트렌드.md` 업데이트(2026-08-05, 사례 193+건, 출처 299+)

## 2026-08-04 (일일 루프 #49)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **와이즈넛 WISE Agent Labs GS인증 1등급 획득 (2026-08-03)** [한국 사례]: 노코드(no-code) AI 에이전트 빌더로 과기정통부 산하 KTL GS(Good Software) 1등급 인증 취득. 코딩 없이 드래그 앤 드롭으로 AI 에이전트 구성. Multi-LLM 연동 + RAG 파이프라인 내장 + MCP 서버 연결 + 설계→개발→학습→검증→운영→개선 전 생애주기 통합. GS 1등급은 기능성·신뢰성·사용성·성능효율성·보안성 전 항목 최고 수준(ISO/IEC 25023 기반) 요건 충족. ZDNet Korea + VentureSquare + 뉴스웍스 3개 이상 snippet-verified. → `03-에이전트-툴유즈-MCP.md` 한국 사례 섹션에 추가
  2. **RING: Retrieval-Internalized Generation via Mixture-of-Memory Experts (arXiv:2608.01630, 2026-08-03)**: 외부 검색기(external retriever)를 완전히 제거하고 대규모 외부 지식을 Mixture-of-Memory Experts(MoME)에 내재화하는 새로운 패러다임. 3단계 학습: Dual Causal Attention 기반 Knowledge Expert 지속 사전학습 → "search-then-answer" SFT → 계층적 보상 RL 최적화. CAS Institute of Computing Technology + Xiaohongshu Inc. arXiv abs + arXiv html 2개 독립 출처 snippet-verified. → `02-프로덕션-아키텍처.md` 2026년 주목할 신규 연구 섹션에 추가
  3. **ACE-GraphRAG: Agentic Context Engineering for Hierarchical GraphRAG (arXiv:2608.01269, 2026-08-02)**: 계층형 GraphRAG의 표현-추론 간극(representation-inference gap)을 정의하고, 추론 시 초기 컨텍스트를 보완·적응하는 정책 레이어(ACE)로 해소. gap-aware refinement + 검색 브랜치 + 태스크 조건부 적응. HotpotQA, 2WikiMultiHopQA, UltraDomain 4개 서브셋에서 Full-ACE가 RAG·GraphRAG 베이스라인 전체 초과. CUHK + 武汉理工大学 + HKUST + Huawei Noah's Ark Lab. arXiv abs + arXiv html 2개 독립 출처 snippet-verified. → `02-프로덕션-아키텍처.md` GraphRAG 섹션에 추가
- `sources.md`에 3개 출처 추가 (## 2026-08-04 일일 누적 추가 출처 섹션 신설)
- `03-에이전트-툴유즈-MCP.md` 와이즈넛 WISE Agent Labs 섹션 추가 (한국 사례)
- `02-프로덕션-아키텍처.md` GraphRAG 섹션에 ACE-GraphRAG 추가, 2026년 주목할 신규 연구 섹션 신설 후 RING 추가
- `00-요약-트렌드.md` 날짜·사례 수·출처 수 갱신 (187+→190+, 293+→296+)

### 검증 결과 (루프 #49)
| # | 사례 | URL 유효 | 요약-출처 일치 | 단언 완화 | ID/날짜 형식 | 중복 없음 |
|---|------|-----------|----------------|-----------|-------------|-----------|
| 1 | 와이즈넛 WISE Agent Labs GS인증 (2026-08-03) [한국] | snippet-verified (ZDNet Korea + VentureSquare + 뉴스웍스 3개 이상 독립 출처) | ✓ (와이즈넛·WISE Agent Labs·GS 1등급·KTL·노코드·드래그 앤 드롭·Multi-LLM+RAG+MCP 확인) | ✓ | 2026-08-03 | ✓ |
| 2 | RING (arXiv:2608.01630, 2026-08-03) | snippet-verified (arXiv abs + arXiv html 2개 독립 출처) | ✓ (MoME·Dual Causal Attention·CAS·Xiaohongshu·State Key Laboratory of AI Safety 확인) | ✓ | 2608.01630, 2026-08-03 | ✓ |
| 3 | ACE-GraphRAG (arXiv:2608.01269, 2026-08-02) | snippet-verified (arXiv abs + arXiv html 2개 독립 출처) | ✓ (표현-추론 간극·gap-aware refinement·CUHK·Huawei Noah's Ark Lab·HotpotQA·UltraDomain 확인) | ✓ | 2608.01269, 2026-08-02 | ✓ |

- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건
- 단언 톤다운: 0건
- 중복 폐기: 0건
- 한국 사례: 1건 (와이즈넛 WISE Agent Labs, 2026-08-03)

## 2026-08-03 (일일 루프 #48)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **KidnapRAG: 에이전틱 RAG 추론 체인 납치 블랙박스 공격 (arXiv:2607.00422, 2026-07)** [한국 사례]: 고려대학교 Language & Intelligence Lab (Buru Chang 교수) 주도 연구. 블랙박스 위협 모델로 공개 소스에 독소 문서를 게시하는 것만으로 에이전틱 RAG의 다단계 추론 체인 전체를 납치해 공격자 의도 답변을 유도. 단일 검색 단계 포이즈닝과 달리 추론 체인 제어가 핵심 기여. arXiv abs + arXiv 목록 + security 연구 저장소 3개 이상 snippet-verified. → `03-에이전트-툴유즈-MCP.md` 2026년 주목할 신규 연구 섹션에 추가
  2. **Core-based Hierarchies for Efficient GraphRAG (arXiv:2603.05207, KDD 2026)**: Leiden 모듈성 최적화의 비결정성 문제를 이론적으로 증명하고 k-코어 분해로 대체하는 결정론적 GraphRAG. 3개 데이터셋·3개 LLM·5개 판별기 조건에서 포괄성·다양성 향상 + 토큰 사용량 감소 동시 달성. KDD 2026(2026-08-09~13, 제주) 발표. arXiv abs + arXiv html + ResearchGate + alphaXiv + KDD 2026 목록 5개 이상 snippet-verified. → `02-프로덕션-아키텍처.md` GraphRAG 섹션에 추가
  3. **VLD-RAG: 에이전틱 비전-언어 장문서 멀티모달 RAG (arXiv:2607.24748, 2026-07)**: Seonok Kim(Mazelone). 다중 페이지 증거 검색·페이지 간 교차 추론을 위한 에이전틱 멀티모달 RAG. 페이지 보존 멀티모달 인덱스 + 하이브리드 검색 + 반복적 멀티모달 질의. arXiv html 목록 + cs.IR 목록 2개 독립 출처 snippet-verified. → `02-프로덕션-아키텍처.md` 멀티모달 섹션에 추가
- `sources.md`에 3개 출처 추가 (## 2026-08-03 일일 누적 추가 출처 섹션 신설)
- `03-에이전트-툴유즈-MCP.md` 2026년 신규 연구 섹션에 KidnapRAG 추가
- `02-프로덕션-아키텍처.md` 멀티모달 섹션에 VLD-RAG 추가, GraphRAG 섹션에 Core-based Hierarchies 추가
- `00-요약-트렌드.md` 날짜·사례 수·출처 수 갱신 (184+→187+, 290+→293+)

### 검증 결과 (루프 #48)
| # | 사례 | URL 유효 | 요약-출처 일치 | 단언 완화 | ID/날짜 형식 | 중복 없음 |
|---|------|-----------|----------------|-----------|-------------|-----------|
| 1 | KidnapRAG (arXiv:2607.00422, 2026-07) [한국] | snippet-verified (arXiv abs + arXiv 목록 + security 저장소 3개 이상) | ✓ (Buru Chang·고려대·블랙박스·추론 체인 납치 확인) | ✓ | 2607.00422, 2026-07 | ✓ |
| 2 | Core-based Hierarchies GraphRAG (arXiv:2603.05207, KDD 2026) | snippet-verified (arXiv abs + html + ResearchGate + alphaXiv + KDD 2026 목록 5개 이상) | ✓ (Jakir Hossain·Univ. at Buffalo·k-코어 분해·KDD 2026 제주 확인) | ✓ | 2603.05207 | ✓ |
| 3 | VLD-RAG (arXiv:2607.24748, 2026-07) | snippet-verified (arXiv html 목록 + cs.IR 목록 2개 독립 출처) | ✓ (Seonok Kim·Mazelone·페이지 보존 멀티모달 인덱스 확인) | ✓ | 2607.24748, 2026-07 | ✓ |

- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건
- 단언 톤다운: 0건
- 중복 폐기: 0건
- 한국 사례: 1건 (KidnapRAG, 고려대학교 Language & Intelligence Lab)

## 2026-08-02 (일일 루프 #47)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **우리은행 × 삼성SDS — AI 에이전트 뱅킹 구축 (2026-04-07)** [한국 사례]: 삼성SDS 패브릭스(FabriX) 플랫폼 기반 175개 AI 에이전트 구축. 5대 영역(기업여신·자산관리·내부통제·고객상담·업무자동화). RAG 기반 답변체계 + 가드레일 + 베테랑 직원 노하우 비정형 데이터 자산화. 2027년 8월 완료, 업무 처리 속도 ~30% 향상 전망. "국내 금융권 최초 대규모 AI 에이전트 적용". samsungsds.com + ZDNet Korea + 전자신문 + 파이낸셜뉴스 + 데이터넷 + 매일일보 + 디일렉 7개 독립 출처 snippet-verified. → `04-산업별-사례.md` 금융 > 한국 섹션에 추가
  2. **MTGuard: MCP 도구 보안 하이브리드 분석 (arXiv:2607.25297, 2026-07-28)**: MCP 기반 LLM 에이전트 도구 사용의 안전 위협 완화를 위한 라이프사이클 인식 정적-동적 공동 분석(static-dynamic co-analysis). 다양한 유해 도구 사용 카테고리 완화·양성 성능 유지. Ping He, Yuexiang Xie, Yaliang Li, Shouling Ji. arXiv abs 2607.25297v1 + arXiv html 2607.25297v1 2개 독립 출처 snippet-verified. → `03-에이전트-툴유즈-MCP.md` 2026년 주목할 신규 연구 섹션에 추가
  3. **GASP: RAG 환각 그라운딩 민감도 탐지 (arXiv:2607.04223, 2026-07-05)**: 지지 구절 제거 시 로그-우도 하락 + Jensen-Shannon Divergence로 스팬 레벨 환각 탐지. RAGTruth response-level AUC ~0.73·span-level AUC ~0.67. TofuEval 전이 가능. arXiv abs + arXiv html + arXiv pdf 3개 독립 출처 snippet-verified. → `02-프로덕션-아키텍처.md` 환각 탐지 섹션에 추가
- `sources.md`에 3개 출처 추가 (## 2026-08-02 일일 누적 추가 출처 섹션 신설)
- `04-산업별-사례.md` 금융 > 한국 섹션에 우리은행 × 삼성SDS AI 에이전트 뱅킹 추가
- `03-에이전트-툴유즈-MCP.md` 2026년 신규 연구 섹션에 MTGuard 추가
- `02-프로덕션-아키텍처.md` 환각 탐지 섹션에 GASP 추가
- `00-요약-트렌드.md` 날짜·사례 수·출처 수 갱신 (181+→184+, 287+→290+)

### 검증 결과 (루프 #47)
| # | 사례 | URL 유효 | 요약-출처 일치 | 단언 완화 | ID/날짜 형식 | 중복 없음 |
|---|------|-----------|----------------|-----------|-------------|-----------|
| 1 | 우리은행 × 삼성SDS AI 에이전트 뱅킹 (2026-04-07) | snippet-verified (samsungsds.com + ZDNet Korea + 전자신문 + 파이낸셜뉴스 + 데이터넷 + 매일일보 + 디일렉 7개 독립 출처) | ✓ (175개 에이전트·5대 영역·FabriX 플랫폼·~30% 향상 전망 확인) | ✓ | 2026-04-07 | ✓ |
| 2 | MTGuard (arXiv:2607.25297, 2026-07-28) | snippet-verified (arXiv abs 2607.25297v1 + arXiv html 2607.25297v1 2개 독립 출처) | ✓ (Ping He·Yuexiang Xie·lifecycle-aware static-dynamic co-analysis 확인) | ✓ | 2607.25297, 2026-07-28 | ✓ |
| 3 | GASP (arXiv:2607.04223, 2026-07-05) | snippet-verified (arXiv abs + arXiv html + arXiv pdf 3개 독립 출처) | ✓ (log-likelihood·JSD·RAGTruth AUC ~0.73 확인) | ✓ | 2607.04223, 2026-07-05 | ✓ |

- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건
- 단언 톤다운: 0건
- 중복 폐기: 0건
- 한국 사례: 1건 (우리은행 × 삼성SDS AI 에이전트 뱅킹, 2026-04-07)

## 2026-08-01 (일일 루프 #46)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **금융보안원 × 한양대 — 계층적 리랭킹 기반 확장형 금융 RAG (arXiv:2607.27523, 2026-07-29)** [한국 사례]: 금융보안원(Joohyun Lee)·한양대(Sungwoo Hong) 공동 연구. 3대 혁신(Pre-Retrieval Optimization + Hierarchical Reranker Architecture + Long-Context Management)을 결합한 금융 특화 RAG 파이프라인. NDCG@20=0.7918(FinQA·FinanceBench·ConvFinQA 종합), ACM-ICAIF '24 FinanceRAG Challenge 2위. FinLLM @ IJCAI-ECAI 2026 채택. arXiv abs + arXiv html + 독립 검색 스니펫 3개 이상 snippet-verified. → `04-산업별-사례.md` 금융 > 한국 섹션에 추가
  2. **예산-인식 능동 검색 평가 프레임워크 (arXiv:2607.24010, KDD 2026)**: 능동 RAG의 운영 지점 미지정 문제를 해소하기 위해 능동 검색을 효용 추정(marginal correctness change) 문제로 재정의. Pin Qian 외 7명, KDD 2026 Workshop on Evaluation and Trustworthiness of Agentic AI. arXiv abs + arXiv pdf + arXiv html 3개 독립 출처 snippet-verified. → `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션에 추가
  3. **JKO-RAG: Wasserstein-2 자유에너지 경사 흐름 기반 분산 검색 리랭킹 (arXiv:2607.24776)**: 리랭킹을 자유에너지 F(p)=관련성+엔트로피+중복성 최소화로 재정의. JKO 근위 도식으로 Wasserstein-2 경사 흐름을 통해 최적 문서 분포 계산. 기저 계량 C_ij=(1−cos⟨z_i,z_j⟩)²이 시맨틱 기하 인코딩. 선형 응답 이론으로 Wasserstein vs KL 차이 해석. Levi Segal, Murari Ambati. arXiv abs + arXiv pdf + ResearchGate 3개 독립 출처 snippet-verified. → `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션에 추가
- `sources.md`에 3개 출처 추가 (## 2026-08-01 일일 누적 추가 출처 섹션 신설)
- `04-산업별-사례.md` 금융 > 한국 섹션에 금융보안원 × 한양대 계층적 리랭킹 추가
- `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션에 예산-인식 능동 검색 평가 + JKO-RAG 추가
- `00-요약-트렌드.md` 날짜·사례 수·출처 수 갱신 (178+→181+, 284+→287+)

### 검증 결과 (루프 #46)
| # | 사례 | URL 유효 | 요약-출처 일치 | 단언 완화 | ID/날짜 형식 | 중복 없음 |
|---|------|-----------|----------------|-----------|-------------|-----------|
| 1 | 금융보안원 × 한양대 계층적 리랭킹 금융 RAG (arXiv:2607.27523, 2026-07-29) | snippet-verified (arXiv abs + arXiv html + 독립 검색 스니펫 3개 이상 출처) | ✓ (금융보안원·한양대 저자·NDCG@20=0.7918·FinanceRAG Challenge 2위·FinLLM@IJCAI-ECAI 2026 확인) | ✓ | 2607.27523, 2026-07-29 | ✓ |
| 2 | 예산-인식 능동 검색 평가 (arXiv:2607.24010, KDD 2026) | snippet-verified (arXiv abs + arXiv pdf + arXiv html 3개 독립 출처) | ✓ (8명 저자·KDD 2026 Workshop·marginal correctness change 효용 정의 확인) | ✓ | 2607.24010 | ✓ |
| 3 | JKO-RAG (arXiv:2607.24776) | snippet-verified (arXiv abs + arXiv pdf + ResearchGate 3개 독립 출처) | ✓ (JKO proximal scheme·Wasserstein-2·F(p)=관련성+엔트로피+중복성·Levi Segal 확인) | ✓ | 2607.24776 | ✓ |

- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건
- 단언 톤다운: 0건
- 중복 폐기: 0건
- 한국 사례: 1건 (금융보안원 × 한양대 — 계층적 리랭킹 기반 확장형 금융 RAG, arXiv:2607.27523, 2026-07-29)

## 2026-07-31 (일일 루프 #45)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **지미션(JIMISSION) × NC AI — 도면 특화 에이전틱 RAG 플랫폼 개발 착수 (2026-07-31)** [한국 사례]: 지미션이 과기정통부 '모두의 챌린지 AX-LLM 협업과제' 수행기관으로 선정되어 NC AI 파운데이션 모델 기반 도면 특화 에이전틱 RAG 플랫폼 R&D에 착수. 제조·산업 현장의 설계도면·기술 문서를 AI가 직접 이해·검색·분석하는 산업 특화 에이전틱 RAG. ZDNet Korea + BetaNews 2개 독립 출처 snippet-verified. → `04-산업별-사례.md` 제조·자동차 > 한국 섹션에 추가
  2. **LayerRAG-Bench (arXiv:2607.27353, 2026-07-29)**: 에이전틱 RAG의 4개 계층(증거·도구계약·권한·세션상태)에서 발생하는 교차 계층 신뢰성 실패를 8개 엔터프라이즈 도메인·240 태스크·9개 장애 시나리오·38,880 레코드·9개 모델로 체계적 실증. 스키마 정규화는 schema-drift(0.000→0.913)만 해결; stale 증거·권한 거부·wrong-session은 별도 수리 필요. Groundedness-only 평가의 구조적 위양성 실증. arXiv abs + arXiv html + LinkedIn Musa Shams 3개 독립 출처 snippet-verified. → `03-에이전트-툴유즈-MCP.md` 2026년 주목할 신규 연구 섹션에 추가
  3. **GLM-RAG (arXiv:2607.28397, 2026-07-30)**: KG 기반 RAG 검색기로 그래프 언어 모델(GLM)·GNN·벡터 검색 체계적 비교. 파인튜닝된 GLM이 두 멀티홉 벤치마크 SOTA + 도메인 외 일반화에서 우위. Heidelberg Univ. + Aleph Alpha Research. arXiv abs + arXiv html 2개 독립 출처 snippet-verified. → `02-프로덕션-아키텍처.md` GraphRAG / 지식 그래프 결합 섹션에 추가
- `sources.md`에 3개 출처 추가 (## 2026-07-31 일일 누적 추가 출처 섹션 신설)
- `04-산업별-사례.md` 제조·자동차 > 한국 섹션에 지미션 × NC AI 도면 에이전틱 RAG 추가
- `03-에이전트-툴유즈-MCP.md` 신규 연구 섹션에 LayerRAG-Bench 추가
- `02-프로덕션-아키텍처.md` GraphRAG 섹션에 GLM-RAG 추가
- `00-요약-트렌드.md` 날짜·사례 수·출처 수 갱신 (175+→178+, 281+→284+)

### 검증 결과 (루프 #45)
| # | 사례 | URL 유효 | 요약-출처 일치 | 단언 완화 | ID/날짜 형식 | 중복 없음 |
|---|------|-----------|----------------|-----------|-------------|-----------|
| 1 | 지미션 × NC AI 도면 에이전틱 RAG (2026-07-31) | snippet-verified (ZDNet Korea + BetaNews NC AI 국책사업 선정 2개 독립 출처) | ✓ (NC AI 파운데이션 모델·AX-LLM 협업과제·도면 특화·2026-07-18 협약 확인) | ✓ | 2026-07-31 | ✓ |
| 2 | LayerRAG-Bench (arXiv:2607.27353, 2026-07-29) | snippet-verified (arXiv abs + arXiv html + LinkedIn Musa Shams 3개 독립 출처) | ✓ (8개 도메인·240 태스크·9개 장애 시나리오·38,880 레코드·schema-drift 0.000→0.913 확인) | ✓ | 2607.27353, 2026-07-29 | ✓ |
| 3 | GLM-RAG (arXiv:2607.28397, 2026-07-30) | snippet-verified (arXiv abs + arXiv html 2개 독립 출처) | ✓ (저자·Heidelberg+Aleph Alpha·멀티홉 SOTA·도메인 외 일반화 확인) | ✓ | 2607.28397, 2026-07-30 | ✓ |

- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건
- 단언 톤다운: 0건
- 중복 폐기: 0건
- 한국 사례: 1건 (지미션 × NC AI — 도면 특화 에이전틱 RAG 플랫폼 개발, 2026-07-31)
- 발굴 시도 → 최종 채택: 약 10건 시도 → 3건 채택 (arXiv:2607.26497 중복 폐기, TWC 콜봇 7일 경과 폐기, OpenCoder 날짜 불확실 보류)

## 2026-07-30 (일일 루프 #44)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **특허청 IP-AX 추진단 — 3종 IP 행정 AI 에이전트 자체 구축 (2026-07-25)** [한국 사례]: 특허청 IP-AX 추진단이 별도 예산·전문 개발 인력 없이 3종 AI 에이전트를 자체 구축. (1) 지식위키(LLM Wiki): 정책 회의 문서를 LLM이 위키 형식으로 재생성 + RAG 기반 자연어 검색. (2) AI 보관소: 해외 IP기관 보도자료 자동 수집·분류·분석. (3) AI 에이전트: 입법예고·발의법안 모니터링+담당부서 선정+법안검토. 아이피데일리 + 헤럴드경제 + 골든타임즈 + GNN뉴스 + 한국경찰뉴스 5개 독립 출처 snippet-verified. → `04-산업별-사례.md` 공공·행정 > 한국 섹션에 추가
  2. **"Which RAG Paradigm Wins at Scale?" (arXiv:2607.26497, 2026-07-29)**: EnterpriseRAG-Bench(511,959 문서, 500 질문, 28 중첩 티어)로 RAG 패러다임 스케일 의존성 체계 분석. BM25가 모든 티어에서 저비용 Pareto 프런티어 하단을 정의하며 중규모 이상에서 정확도 선도. LLM 기반 구성 없이도 경쟁력 유지. Pengyu Wang 외 6인. arXiv abs + arXiv html 2개 독립 출처 snippet-verified. → `02-프로덕션-아키텍처.md` 평가 > 벤치마크 섹션에 신규 ### 추가
  3. **CMT-RAG (arXiv:2607.26470, 2026-07-29)**: 멀티턴 대화에서 멀티홉 추론과 장거리 의존성을 동시 처리. 원시 대화 이력 대신 서브 질문 수준 추론 추적(CMT)으로 대화 컨텍스트 표현. MuMu-QA 벤치마크(교차-턴 서브 질문 의존성 주석 포함) 신규 구축. Lang Zhou, Yingjian Chen, Shuxuan Li, Kun-Yu Lin, Zhilin Zhao. arXiv abs + arXiv html 2개 독립 출처 snippet-verified. → `03-에이전트-툴유즈-MCP.md` 2026년 주목할 신규 연구 섹션에 추가
- `sources.md`에 3개 출처 추가 (## 2026-07-30 일일 누적 추가 출처 섹션 신설)
- `04-산업별-사례.md` 공공·행정 > 한국에 특허청 IP-AX 추가, 날짜 갱신
- `02-프로덕션-아키텍처.md` 평가 섹션에 arXiv:2607.26497 추가, 날짜 갱신
- `03-에이전트-툴유즈-MCP.md` 신규 연구 섹션에 CMT-RAG 추가
- `00-요약-트렌드.md` 날짜·사례 수·출처 수 갱신 (172+→175+, 278+→281+)

### 검증 결과 (루프 #44)
| # | 사례 | URL 유효 | 요약-출처 일치 | 단언 완화 | ID/날짜 형식 | 중복 없음 |
|---|------|-----------|----------------|-----------|-------------|-----------|
| 1 | 특허청 IP-AX (2026-07-25) | snippet-verified (아이피데일리 + 헤럴드경제 + 골든타임즈 + GNN뉴스 + 한국경찰뉴스 5개 독립 출처) | ✓ (3종 에이전트 구성·별도 예산 없음 확인) | ✓ | 2026-07-25 | ✓ |
| 2 | arXiv:2607.26497 (2026-07-29) | snippet-verified (arXiv abs + arXiv html 2개 독립 출처) | ✓ (BM25·Pareto 프런티어·511,959 문서·28 티어 확인) | ✓ | 2607.26497, 2026-07-29 | ✓ |
| 3 | arXiv:2607.26470 CMT-RAG (2026-07-29) | snippet-verified (arXiv abs + arXiv html 2개 독립 출처) | ✓ (CMT·MuMu-QA 벤치마크·교차-턴 서브 질문 의존성 확인) | ✓ | 2607.26470, 2026-07-29 | ✓ |

- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건
- 단언 톤다운: 0건
- 중복 폐기: 0건
- 한국 사례: 1건 (특허청 IP-AX 추진단)
- 발굴 시도 → 최종 채택: 약 10건 시도 → 3건 채택

## 2026-07-29 (일일 루프 #43)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **LG Uplus — 접합적 교차 페이지 검색 커버리지 실증 연구 (arXiv:2607.24165, 2026-07)** [한국 사례]: Sungguk Cha 외 LG Uplus 연구팀이 현행 RAG 검색기가 다중 페이지에 분산된 증거를 모두 커버하는지 통제 실험으로 실증. 단일 페이지 vs 교차 페이지 증거 요구 조건 분리, "관련성" 외 독립 평가 차원으로서 "접합적 커버리지(conjunctive coverage)"를 제안. arXiv + ZoomInfo(Sungguk Cha @ LG Uplus) + sciprofiles 3개 독립 출처 snippet-verified. → `02-프로덕션-아키텍처.md` 검색 품질·평가 섹션에 추가
  2. **MCP 2026-07-28 신규 스펙 (Anthropic, 2026-07-28)**: Stateless Core(서버리스·엣지 배포 가능), OAuth 2.0/OIDC 엔터프라이즈 인증(Entra·Okta), Versioned Extensions(Apps·Tasks). MCP SDK 월 4억 다운로드(전년 4× 성장). 사내 지식 베이스를 기업 권한 모델 그대로 MCP tool로 노출하는 엔터프라이즈 RAG 패턴 표준화. Anthropic 공식 블로그 + ClaudeDevs X + explainx.ai + stacktr.ee + bovo-digital.tech + vindler.solutions 6개 독립 출처 snippet-verified. → `03-에이전트-툴유즈-MCP.md` MCP 섹션에 추가
  3. **TSGR — 타오바오 생성적 검색 비즈니스 가치 인식 (arXiv:2607.18796, Alibaba/Taobao, 2026-07-21)**: Taobao Search에서 VRM(Value-aware Ranking Module)으로 비즈니스 가치 신호를 SID 구성과 후보 랭킹 양 단계에 내장. 단일 모델이 검색기+사전 랭커 동시 수행. 오프라인 +9.16% HR@1000; 온라인 +0.43% IPV, +1.12% TC, +1.64% GMV. arXiv abs + arXiv html + X/@_reachsumit + Springer link 4개 독립 출처 snippet-verified. → `04-산업별-사례.md` 커머스·고객서비스 > 글로벌 섹션에 추가
- `sources.md`에 3개 출처 추가 (## 2026-07-29 일일 누적 추가 출처 섹션 신설)
- `02-프로덕션-아키텍처.md` 검색 품질·평가 섹션에 LG Uplus arXiv:2607.24165 추가
- `03-에이전트-툴유즈-MCP.md` MCP 섹션에 MCP 2026-07-28 스펙 추가
- `04-산업별-사례.md` 커머스·고객서비스 > 글로벌 섹션에 TSGR 추가

### 검증 결과 (루프 #43)
| # | 사례 | URL 유효 | 요약-출처 일치 | 단언 완화 | ID/날짜 형식 | 중복 없음 |
|---|------|-----------|----------------|-----------|-------------|-----------|
| 1 | LG Uplus Conjunctive Retrieval (arXiv:2607.24165, 2026-07) | snippet-verified (arXiv + ZoomInfo Sungguk Cha @ LG Uplus + sciprofiles 3개 독립 출처) | ✓ (저자·기관·교차 페이지 커버리지 연구 확인) | ✓ | 2607.24165, 2026-07 | ✓ |
| 2 | MCP 2026-07-28 spec (Anthropic, 2026-07-28) | snippet-verified (Anthropic 블로그 + ClaudeDevs X + explainx.ai + stacktr.ee + bovo-digital.tech + vindler.solutions 6개 독립 출처) | ✓ (Stateless Core·OAuth 2.0/OIDC·Versioned Extensions·4억 다운로드 확인) | ✓ | 2026-07-28 | ✓ |
| 3 | TSGR (arXiv:2607.18796, Alibaba/Taobao, 2026-07-21) | snippet-verified (arXiv abs + arXiv html + X/@_reachsumit + Springer link 4개 독립 출처) | ✓ (저자·VRM·SID·+9.16% HR@1000·+1.64% GMV 수치 확인) | ✓ | 2607.18796, 2026-07-21 | ✓ |

- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건
- 단언 톤다운: 0건
- 중복 폐기: 0건
- 한국 사례: 1건 (LG Uplus — arXiv:2607.24165, 접합적 교차 페이지 검색 커버리지)
- 발굴 시도 → 최종 채택: 약 10건 시도 → 3건 채택

## 2026-07-28 (일일 루프 #42)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **ARI — 한국 고문서 복원 RAG (arXiv:2607.21936, ACL 2026 Findings, 2026-07-24)** [한국 사례]: 강원대학교 Gabeen Kim·Kyeongpil Kang 팀이 제안한 ARI(Attention-based Retrieval Integration) 프레임워크. 물리적 훼손으로 판독 불가능한 한국 역사 고문서에서 고유명사·인명·지명 등 외부 지식이 필요한 개체명을 정확히 복원. LLM 암묵적 지식 + RAG 외부 역사 지식을 어텐션 기반으로 이중 결합. 일반 문자·고유명사 복원 모두 베이스라인 대비 유의미한 성능 향상, ACL 2026 Findings 채택. arXiv abs + arXiv html + Scholar profile(Kyeongpil Kang) 3개 이상 독립 출처 snippet-verified. → `04-산업별-사례.md` 과학·연구 > 한국 섹션 신설 후 추가
  2. **VecTree-RAG (arXiv:2607.23006, 2026-07-25)**: 과학 문헌 QA에서 "관련 논문 판별"과 "논문 내 증거 위치 파악"이라는 두 개의 질적으로 다른 문제를 벡터 검색(코퍼스 수준 랭킹)과 트리 순회(문서 내 정밀 위치 파악)로 분리 처리하는 에이전틱 RAG 프레임워크. XJTLU + Suzhou Lab + China Univ. of Petroleum. QASPER LLM-judge 0.800 · LitQA2 0.925 · MOSAIC 0.547 — 세 벤치마크 모두 최고 성능. arXiv abs + arXiv html 2개 독립 출처 snippet-verified. → `03-에이전트-툴유즈-MCP.md` 신규 연구 섹션에 추가
  3. **Optimizing Hypergraph-Based RAG (arXiv:2607.20506, 2026-07)**: 하이퍼그래프 RAG의 두 가지 실용 병목(추출 오류·비효율 검색)을 EXT++(자기일관성 프롬프팅으로 추출 품질 향상) + Personalized PageRank(구조적 연결성 기반 청크 검색)로 동시 해결. Houda Khrouf, Pedro Fillastre, Sebastiao Correia. 소스 코드·평가 데이터 공개. arXiv abs + arXiv html 2개 독립 출처 snippet-verified. → `02-프로덕션-아키텍처.md` GraphRAG 섹션에 추가
- `sources.md`에 3개 출처 추가 (## 2026-07-28 일일 누적 추가 출처 섹션 신설)
- `04-산업별-사례.md` 과학·연구 섹션에 "### 한국" 서브섹션 신설 후 ARI 추가
- `03-에이전트-툴유즈-MCP.md` 신규 연구 섹션에 VecTree-RAG 추가
- `02-프로덕션-아키텍처.md` GraphRAG 섹션에 Optimizing Hypergraph-Based RAG 추가
- `00-요약-트렌드.md` 날짜·사례 수·출처 수 갱신 (166+→169+, 272+→275+)

### 검증 결과 (루프 #42)
| # | 사례 | URL 유효 | 요약-출처 일치 | 단언 완화 | ID/날짜 형식 | 중복 없음 |
|---|------|-----------|----------------|-----------|-------------|-----------|
| 1 | ARI (arXiv:2607.21936, 2026-07-24) | snippet-verified (arXiv abs + arXiv html + Scholar profile 3개 독립 출처) | ✓ (저자·날짜·기관·ARI 프레임워크·ACL 2026 Findings·한국 고문서 실험 확인) | ✓ | 2607.21936, 2026-07-24 | ✓ |
| 2 | VecTree-RAG (arXiv:2607.23006, 2026-07-25) | snippet-verified (arXiv abs + arXiv html 2개 독립 출처) | ✓ (저자·날짜·기관·QASPER 0.800·LitQA2 0.925·MOSAIC 0.547 벤치마크 수치 확인) | ✓ | 2607.23006, 2026-07-25 | ✓ |
| 3 | Optimizing Hypergraph RAG (arXiv:2607.20506, 2026-07) | snippet-verified (arXiv abs + arXiv html 2개 독립 출처) | ✓ (저자·EXT++·PPR 방법론·공개 코드 확인) | ✓ | 2607.20506, 2026-07 (일자 미확인) | ✓ |

- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건
- 단언 톤다운: 0건
- 중복 폐기: 0건
- 한국 사례: 1건 (ARI — 강원대학교, 한국 고문서 RAG, ACL 2026 Findings)
- 발굴 시도 → 최종 채택: 약 12건 시도 → 3건 채택

## 2026-07-27 (일일 루프 #41)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **올거나이즈 × 한국증권금융 — 온프레미스 전사 AI 비서 플랫폼 (2026-07-15)** [한국 사례]: 금융공기업 한국증권금융의 '생성형 AI 활용 플랫폼 내부 구축' 수주. 전사 임직원 대상 AI 플랫폼 + 업무별 AI 비서. 올거나이즈 FDSE 방법론, 온프레미스(외부 전송 금지), DRM·SSO·개인정보 비식별화·내부망 연동. AI 기본법·금감원 RMF·금융보안원 AI 보안 안내서 반영. edaily + zdnet + venturesquare + newstheai + ezyeconomy + digitalchosun 6개 이상 독립 출처 snippet-verified. → `04-산업별-사례.md` 금융 > 한국 섹션에 추가
  2. **GRASP: GRanularity-Aware Search Policy for Agentic RAG (arXiv:2607.10463, 2026-07-11)**: 에이전트 RAG에서 semantic search, keyword search, paragraph reading 세 검색 액션을 RL로 동적 조율. 결합 보상(답변 정확도+근거 읽기+보완적 검색+턴 효율). 세분성 인식 정책으로 쿼리 복잡도·문서 구조에 따라 검색 깊이 자동 전환. UMass Amherst + Adobe Research. → `03-에이전트-툴유즈-MCP.md` 주목할 신규 연구 섹션에 추가
  3. **From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents (arXiv:2607.08028, 2026-07-09)**: 엔터프라이즈 LLM 앱을 추적·감사 가능 아키텍처로 재구성. RAG를 소스-근거 클레임 레이어로 명시 설계. 5가지 계약(소스 근거·엔티티 라우팅·추적·출력 위생·권고 언어). 한국 5개 대기업 그룹(25개 상장사) 검증. 3개 호스팅 모델 교체 실험에서 계약 유지 확인. AI Leadership Research Center(한국인 저자). → `02-프로덕션-아키텍처.md` 보안·거버넌스 섹션에 추가
- `sources.md`에 3개 출처 추가 (## 2026-07-27 일일 누적 추가 출처 섹션 신설)
- `04-산업별-사례.md` 금융 > 한국 섹션에 올거나이즈 × 한국증권금융 추가
- `03-에이전트-툴유즈-MCP.md` 신규 연구 섹션에 GRASP 추가
- `02-프로덕션-아키텍처.md` 보안·거버넌스 섹션에 Harness Engineering 추가
- `00-요약-트렌드.md` 날짜·사례 수·출처 수 갱신 (163+→166+, 269+→272+)

### 검증 결과 (루프 #41)
| # | 사례 | URL 유효 | 요약-출처 일치 | 단언 완화 | ID/날짜 형식 | 중복 없음 |
|---|------|-----------|----------------|-----------|-------------|-----------|
| 1 | 올거나이즈 × 한국증권금융 (2026-07-15) | snippet-verified (edaily + zdnet + venturesquare + newstheai + ezyeconomy + digitalchosun 6개 이상 독립 출처) | ✓ (수주 사실·기술 스택·규제 대응 확인) | ✓ | 2026-07-15 | ✓ |
| 2 | GRASP (arXiv:2607.10463) | snippet-verified (arXiv abs + arXiv html + HuggingFace papers + ResearchGate + X post 5개 독립 출처) | ✓ (저자·제출일·RL 프레임워크·벤치마크 확인) | ✓ | 2607.10463, 2026-07-11 | ✓ |
| 3 | Harness Engineering (arXiv:2607.08028) | snippet-verified (arXiv abs + arXiv html + cs.CL listing + ORCID 4개 독립 출처) | ✓ (저자·날짜·5가지 계약·한국 기업 검증 확인) | ✓ | 2607.08028, 2026-07-09 | ✓ |

- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건
- 단언 톤다운: 0건
- 중복 폐기: 0건
- 한국 사례: 1건 (올거나이즈 × 한국증권금융 — 2026-07-15)
- 발굴 시도 → 최종 채택: 약 10건 시도 → 3건 채택

## 2026-07-26 (일일 루프 #40)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **서울아산병원 — 폐쇄망 기반 프라이빗 AI 지식 검색 시스템 (2026-05-18)** [한국 사례]: 국내 의료기관 최초 완전 폐쇄망 기반 프라이빗 AI 지식 관리 시스템. 벡터 데이터베이스 + RAG로 임상지침·규정 문서 인덱싱, 온프레미스 100%(외부 클라우드 0%). RAG 기반 환각 방지 + 의료 데이터 외부 전송 0의 동시 달성. rapportian.com + etnews.com + docdocdoc.co.kr + khanews.com + thefirstmedi.co.kr + medicalinfo.co.kr 6개 이상 독립 출처 snippet-verified. → `04-산업별-사례.md` 의료 > 한국 섹션에 추가
  2. **IteraSim RAG (arXiv:2607.20346, 2026-07-22)**: OpenFOAM CFD 비전문가 장벽 해소를 위한 멀티스테이지 에이전틱 RAG. LLM 기반 멀티-변형 쿼리 확장(물리·솔버-키워드·트러블슈팅) → RRF → MMR → HNSW 밀집 벡터 검색; 초안·검토 에이전트 분리로 자기 검토 한계 극복. Computer Physics Communications 제출. → `04-산업별-사례.md` 과학·연구 > 글로벌 섹션에 추가
  3. **MetaRAG 재현성 연구 (arXiv:2604.19899, SIGIR 2026)**: 메타인지 RAG의 상대적 개선은 재현 가능하나 절대 점수는 원논문보다 낮음(폐쇄소스 LLM 버전 변경·구현 세부 사항 부재가 원인). PointWise·ListWise 리랭커 + SIM-RAG 비교 확장. DOI: 10.1145/3805712.3808551. GitHub: iai-group/sigir2026-metarag. → `02-프로덕션-아키텍처.md` 평가 섹션에 추가
- `sources.md`에 3개 출처 추가 (## 2026-07-26 일일 누적 추가 출처 섹션 신설)
- `04-산업별-사례.md` 날짜 2026-07-23→2026-07-26, 의료>한국 섹션에 서울아산병원 폐쇄망 AI 추가, 과학·연구>글로벌 섹션에 IteraSim RAG 추가
- `02-프로덕션-아키텍처.md` 날짜 2026-07-25→2026-07-26, 평가 섹션에 MetaRAG 재현성 연구 추가
- `00-요약-트렌드.md` 날짜·사례 수·출처 수 갱신 (160+→163+, 266+→269+)

### 검증 결과 (루프 #40)
| # | 사례 | URL 유효 | 요약-출처 일치 | 단언 완화 | ID/날짜 형식 | 중복 없음 |
|---|------|-----------|----------------|-----------|-------------|-----------|
| 1 | 서울아산병원 폐쇄망 프라이빗 AI (2026-05-18) | snippet-verified (rapportian.com + etnews.com + docdocdoc.co.kr + khanews.com + thefirstmedi.co.kr + medicalinfo.co.kr 6개 이상 독립 출처) | ✓ (공식 발표일·기술 스택·아키텍처 특이점 확인) | ✓ | 2026-05-18 | ✓ (기존 서울아산병원 스마트청킹 항목과 별도 사례) |
| 2 | IteraSim RAG (arXiv:2607.20346) | snippet-verified (arXiv abs + arXiv html + bohrium.com 3개 독립 출처) | ✓ (저자·제출일·CFD 도메인·아키텍처 확인) | ✓ | 2607.20346, 2026-07-22 | ✓ |
| 3 | MetaRAG 재현성 연구 (arXiv:2604.19899) | snippet-verified (arXiv abs + SIGIR 2026 ACM DOI + GitHub iai-group/sigir2026-metarag 3개 독립 출처) | ✓ (SIGIR 2026 발표·DOI·재현성 결과 확인) | ✓ | 2604.19899, SIGIR 2026 2026-07-20~24 | ✓ |

- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건
- 단언 톤다운: 0건
- 중복 폐기: 0건
- 한국 사례: 1건 (서울아산병원 폐쇄망 기반 프라이빗 AI — 2026-05-18, 이전 루프 미수록)
- 발굴 시도 → 최종 채택: 약 15건 시도 → 3건 채택

## 2026-07-25 (일일 루프 #39)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **GraphContainer (arXiv:2607.19362, KAIST, VLDB 2026 Demo)** [한국 사례]: 이종 Graph RAG 프레임워크(Microsoft GraphRAG·LightRAG·MemGraphRAG 등)의 구조적 파편화 문제를 해결하는 통합 비교·디버깅 플랫폼. UGR(Unified Graph Representation) 레이어로 다양한 그래프 포맷을 표준화하고, Graph Recorder로 검색 단계별 시각 재현 가능. VLDB 2026 Demo 채택. KAIST 저자(Seonho An, Chaejeong Hyun, Min-Soo Kim). → `02-프로덕션-아키텍처.md` GraphRAG / 지식 그래프 결합 섹션에 추가
  2. **PAGE-RAG (arXiv:2607.19301, 2026-07-21)**: 자동 구성 그래프가 원문의 불완전한 투영임을 인정하고, 그래프를 독립 지식 소스 대신 의미적 골격으로 취급하는 장문서 QA 프레임워크. 태스크 적응형 검색 라우팅으로 그래프 traversal과 원문 직접 접근을 동적 선택. 증거 근거 설계로 환각 구조적 억제. 오픈소스. → `02-프로덕션-아키텍처.md` GraphRAG / 지식 그래프 결합 섹션에 추가
  3. **GRADRAG (arXiv:2607.21324, 2026-07-23)**: RAG 파이프라인을 계산 그래프로 모델링해 평가자 피드백을 역방향 전파, 검색기·그래프 구성기·생성기 프롬프트를 조율 업데이트하는 멀티에이전트 RAG 크로스-컴포넌트 최적화 프레임워크. 조기 종료 신호로 불필요한 반복 차단. SQUALITY + QMSUM 벤치마크. → `03-에이전트-툴유즈-MCP.md` 주목할 신규 연구 섹션에 추가
- `sources.md`에 3개 출처 추가 (## 2026-07-25 일일 누적 추가 출처 섹션 신설)
- `02-프로덕션-아키텍처.md` 날짜 2026-07-24→2026-07-25, GraphRAG 섹션에 GraphContainer(한국 사례) + PAGE-RAG 추가
- `03-에이전트-툴유즈-MCP.md` 신규 연구 섹션에 GRADRAG 추가
- `00-요약-트렌드.md` 날짜·사례 수·출처 수 갱신 (157+→160+, 263+→266+)

### 검증 결과 (루프 #39)
| # | 사례 | URL 유효 | 요약-출처 일치 | 단언 완화 | ID/날짜 형식 | 중복 없음 |
|---|------|-----------|----------------|-----------|-------------|-----------|
| 1 | GraphContainer (arXiv:2607.19362) | snippet-verified (arXiv abs + arXiv html + VLDB 2026 demonstrations 3개 독립 출처) | ✓ (KAIST 저자·VLDB 2026 Demo 채택·UGR+Graph Recorder 기능 확인) | ✓ | 2607.19362, 2026-07 | ✓ |
| 2 | PAGE-RAG (arXiv:2607.19301) | snippet-verified (arXiv abs + arXiv html + cs.IR listing 3개 독립 출처) | ✓ (저자·날짜·핵심 기여 확인) | ✓ | 2607.19301, 2026-07-21 | ✓ |
| 3 | GRADRAG (arXiv:2607.21324) | snippet-verified (arXiv abs + arXiv html + cs.CL listing + cs.AI listing 4개 독립 출처) | ✓ (저자·날짜·벤치마크·아키텍처 확인) | ✓ | 2607.21324, 2026-07-23 | ✓ |

- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건
- 단언 톤다운: 0건
- 중복 폐기: 0건
- 한국 사례: 1건 (GraphContainer — KAIST, VLDB 2026 Demo)
- 발굴 시도 → 최종 채택: 약 7건 시도 → 3건 채택

## 2026-07-24 (일일 루프 #38)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 0건 — 2026-07-17~24 기간 내 검증 가능한 신규 한국 RAG 사례 미발굴)
  1. **Salience Induction (arXiv:2607.17535, 2026-07-20)**: 멀티홉 RAG 에이전트에서 개별 사실이 모두 참인 상태에서 현저성 채널(사실 위치·강조·프레이밍·의미적 근접성)을 조작해 에이전트 추론을 오염시키는 신규 공격 유형. 6개 Salience-Editing 연산자 정의 + 반복적 제안자-검증자 파이프라인 + SalientWiki-MH 벤치마크 구축. 30% 편집 예산 내 ASR 83.3%; 최강 방어 후 사후 ASR 75.7%. GPT/Claude/Gemini/DeepSeek/Qwen 5개 모델 + ReAct/Reflexion/tool-calling 3가지 아키텍처 실험. National University of Defense Technology(중국). → `03-에이전트-툴유즈-MCP.md` 주목할 신규 연구 섹션에 추가
  2. **SelectBench / RL Selective Evidence (arXiv:2607.20090, 2026-07-22)**: 오염된 RAG 컨텍스트에서 유효 증거와 오해 유발 콘텐츠를 구별하는 선택적 증거 채택 능력을 강화학습(DAPO)으로 학습. SelectBench 벤치마크 + 훈련 세트. Qwen3.5-4B 포스트 트레이닝. strict success 22.46%→25.54%(DAPO-Rule)/26.46%(DAPO-DeepSeek). → `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션에 추가
  3. **TopoGuard (arXiv:2607.20437, 2026-07)**: 분할 지식 공격(각각 무해한 문서가 조합되면 허위 관계 형성, LlamaGuard 등 문서별 필터 우회) 탐지를 위한 검색 문서 의미적 유사도 그래프 위상 분석 방어 프레임워크. 이론적 효과성 증명, 서브밀리초 지연, 적응형 공격자 및 양성 교차 도메인 쿼리 환경 강건성. University of Nevada, Las Vegas. → `02-프로덕션-아키텍처.md` 보안·거버넌스 섹션에 추가
- `sources.md`에 3개 출처 추가 (## 2026-07-24 일일 누적 추가 출처 섹션 신설)
- `03-에이전트-툴유즈-MCP.md`: Salience Induction 항목 추가
- `02-프로덕션-아키텍처.md` 날짜 2026-07-23→2026-07-24, SelectBench 항목 + TopoGuard 항목 추가
- `00-요약-트렌드.md` 날짜·사례 수·출처 수 갱신 (154+→157+, 260+→263+)

### 검증 결과 (루프 #38)
| # | 사례 | URL 유효 | 요약-출처 일치 | 단언 완화 | ID/날짜 형식 | 중복 없음 |
|---|------|-----------|----------------|-----------|-------------|-----------|
| 1 | Salience Induction (arXiv:2607.17535) | snippet-verified (arXiv abs + cs.CR listing 2개 독립 출처) | ✓ | ✓ | 2607.17535, 2026-07-20 | ✓ |
| 2 | SelectBench (arXiv:2607.20090) | snippet-verified (arXiv abs + cs.CL listing 2개 독립 출처) | ✓ | ✓ | 2607.20090, 2026-07-22 | ✓ |
| 3 | TopoGuard (arXiv:2607.20437) | snippet-verified (arXiv abs + cs.CR listing 2개 독립 출처) | ✓ | ✓ (제출일 불확실, 아이디 기준 2026-07 표기) | 2607.20437, 2026-07 | ✓ |

- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건
- 단언 톤다운: 1건 (TopoGuard 제출 정확일 불확실 → "2026-07" 기간 표기)
- 중복 폐기: 0건 (3건 모두 sources.md 미수록 확인)
- 한국 사례: 0건 (2026-07-17~24 기간 내 검증 가능 신규 한국 RAG 사례 미발굴)
- 발굴 시도 → 최종 채택: 약 8건 시도 → 3건 채택 (HG-RAG 날짜 불확실 폐기, VoiceAgentRAG 7일 경과 폐기, KT RAG 이미 sources.md 수록 폐기)

## 2026-07-23 (일일 루프 #37)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **미디어젠 — MIRAGE 에이전틱 RAG + 공정거래위원회 AI 시스템 (2026-07-23)**: 자체 sLLM 기반 에이전틱 RAG 엔진 MIRAGE로 공정거래위원회 불공정 약관 심사 AI 시스템·하도급 계약 AI 지원 시스템 구축. klaw-Contriever 기반 한국어 법규 특화 검색 모델로 법령 검색 성능 최대 33% 향상, 도메인 특화 검색 모델 원천 특허 등록(2026-07-23). → `04-산업별-사례.md` 법률 > 한국 섹션에 추가 [한국 사례]
  2. **RIMS (arXiv:2607.16431, 2026-07-17)**: 소형 LLM(SLM) RAG의 노이즈 검색 증거 민감성을 3단계 프레임워크(자체 rejection sampling 합성 데이터 + differentiable soft aggregation + 멀티 쌍 선호도 최적화)로 해소. Columbia·Rutgers·Purdue·SUNY Albany. → `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션에 추가
  3. **VizRAG (arXiv:2607.19830, 2026-07-22)**: 하이퍼그래프 기반 RAG의 텍스트 단일 모달 한계를 HyperViz 시각화 툴킷으로 극복, MLLM 검색·추론에 하이퍼그래프 시각 신호 주입. SUSTech·HKUST·Huawei Research·Beihang Univ. → `02-프로덕션-아키텍처.md` GraphRAG / 지식 그래프 결합 섹션에 추가
- `sources.md`에 3개 출처 추가 (## 2026-07-23 추가 출처 섹션 신설)
- `04-산업별-사례.md` 날짜 2026-07-22→2026-07-23, 법률 > 한국 섹션에 미디어젠 MIRAGE 추가
- `02-프로덕션-아키텍처.md` 날짜 2026-07-22→2026-07-23, 검색·리랭킹 섹션에 RIMS 추가, GraphRAG 섹션에 VizRAG 추가
- `00-요약-트렌드.md` 날짜·사례 수·출처 수 갱신 (151+→154+, 257+→260+)

### 검증 결과 (루프 #37)
| # | 사례 | URL 유효 | 요약-출처 일치 | 단언 완화 | ID/날짜 형식 | 중복 없음 |
|---|------|-----------|----------------|-----------|-------------|-----------|
| 1 | 미디어젠 MIRAGE (서울신문 2026-07-23) | snippet-verified (서울신문·aisakorea.com·dailyinvest.kr·newspim.com KCC 2026 4개 이상 독립 출처) | ✓ | ✓ (수치는 회사 발표·KCC 논문 기준 명시) | 2026-07-23 | ✓ |
| 2 | RIMS (arXiv:2607.16431) | snippet-verified (arXiv abs + html 2개 독립 출처) | ✓ | ✓ | 2607.16431, 2026-07-17 | ✓ |
| 3 | VizRAG (arXiv:2607.19830) | snippet-verified (arXiv abs + html 2개 독립 출처) | ✓ | ✓ | 2607.19830, 2026-07-22 | ✓ |

- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건
- 단언 톤다운: 0건 (수치는 발표·논문 기준 명시로 처리)
- 중복 폐기: 0건 (3건 모두 sources.md 미수록 확인)
- 한국 사례: 1건 (미디어젠 MIRAGE — 공정거래위원회 법규 특화 에이전틱 RAG)
- 발굴 시도 → 최종 채택: 약 6건 시도 → 3건 채택

## 2026-07-22 (일일 루프 #36)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 0건 — 해당 기간 내 검증 가능 신규 한국 사례 미발굴)
  1. **TurboVec (arXiv:2607.16973, 2026-07-18)**: 코퍼스-독립 4-bit scalar quantizer(TurboQuant)로 멀티테넌트 엔터프라이즈 RAG에서 프라이버시-보존 벡터 압축 실현. FAISS PQ 대비 Recall@5 +8.5–8.9pp(동일 메모리). 커널 얼로우리스트 필터링으로 Recall@10 0.86–0.93 유지(post-filter 대비 5–10×). 멤버십 추론 ~50%(랜덤 수준). Rust 오픈소스. → `02-프로덕션-아키텍처.md` 벡터DB 트렌드 섹션에 추가
  2. **RAGAL (arXiv:2607.18756, 2026-07-21)**: 루마니아 정부기관 AFIR의 단일 소비자용 8GB 노트북 완전 로컬 RAG. 데이터 외부 전송 금지·읽기 전용 제약하에 루마니아어 ~25,000 청크 하이브리드 검색 + 의도 라우팅으로 평가 62%→81%. → `04-산업별-사례.md` 공공·행정 > 글로벌 섹션(신설)에 추가
  3. **FinSAgent (arXiv:2607.18102, 2026-07)**: SEC 10-K 공시 QA 코퍼스-정렬 멀티에이전트 RAG. 역할-특화 병렬 에이전트 + DB-인식 쿼리 분해 + 피처-게이팅 리랭킹으로 사전 코퍼스 미정렬 문제 해결. → `04-산업별-사례.md` 금융 > 글로벌 섹션에 추가
- `sources.md`에 3개 출처 추가 (## 2026-07-22 추가 출처 섹션 신설)
- `02-프로덕션-아키텍처.md` 날짜 2026-07-21→2026-07-22, 벡터DB 트렌드 섹션에 TurboVec 추가
- `04-산업별-사례.md` 날짜 2026-07-21→2026-07-22, 금융 > 글로벌 섹션에 FinSAgent 추가, 공공·행정 > 글로벌 섹션(신설)에 RAGAL 추가
- `00-요약-트렌드.md` 날짜·사례 수·출처 수 갱신 (148+→151+, 254+→257+)

### 검증 결과 (루프 #36)
| # | 사례 | URL 유효 | 요약-출처 일치 | 단언 완화 | ID/날짜 형식 | 중복 없음 |
|---|------|-----------|----------------|-----------|-------------|-----------|
| 1 | TurboVec (arXiv:2607.16973) | snippet-verified (alphamatch.ai + larsroettig.me + knightli.com + medevel.com + Medium 포함 6개 이상 독립 출처) | ✓ | ✓ (수치는 논문 기준 명시) | 2607.16973, 2026-07-18 | ✓ |
| 2 | RAGAL (arXiv:2607.18756) | snippet-verified (arxiv.org abs + html + 연관 검색 결과 3개 이상 독립 출처) | ✓ | ✓ | 2607.18756, 2026-07-21 | ✓ |
| 3 | FinSAgent (arXiv:2607.18102) | snippet-verified (arxiv.org abs + html 2개 이상 독립 출처) | ✓ | ✓ | 2607.18102, 2026-07 | ✓ |

- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건
- 단언 톤다운: 0건 (수치는 논문 기준 명시로 처리)
- 중복 폐기: 0건
- 한국 사례: 0건 (2026-07-15~22 기간 내 네이버·카카오·토스·우아한형제들·LY Corp·SKT·KT·금융·의료·법률·교육 등 10+ 대상 탐색했으나 검증 가능한 신규 사례 미발굴)
- 발굴 시도 → 최종 채택: 약 10건 시도 → 3건 채택

## 2026-07-21 (일일 루프 #35)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **법제처 × 행안부 × 과기정통부 — AI 법령 비서 (2026-07-14)**: 공무원이 직접 약 1개월 만에 구축한 법령 RAG QA 서비스. 대법원 판례 6만 건 + 법령·행정규칙 24만 건 + 자치법규 5만 건 인덱싱. 범정부 AI 공통 인프라 RAG 모듈 활용. 2026-07-14 시범 개시. → `04-산업별-사례.md` 공공·행정 > 한국 섹션에 추가 [한국 사례]
  2. **arXiv:2607.16604 — "When Do Multimodal and Graph-Augmented RAG Help?" (2026-07-18)**: PubLayNet 1,000페이지 4-way 소거 실험. KG 증강은 정확도 향상 미검증, 시각 증강은 픽셀 전용 질의에서만 유효. 이미지 토크나이저별 토큰 수 최대 11배 차이. → `02-프로덕션-아키텍처.md` 멀티모달 섹션에 추가
  3. **arXiv:2607.17538 — D-NOVA: 스토리지 내 RAG 벡터 검색 가속기 (MICRO 2026)**: 3D NAND 메모리 배열 내부에서 직접 IVF 기반 벡터 검색 실행. CPU 대비 41.7배 속도·71배 에너지 효율, 최신 인스토리지 가속기 대비 12.13배 처리량. → `02-프로덕션-아키텍처.md` 비용·지연 엔지니어링 섹션에 추가
- `sources.md`에 3개 출처 추가 (## 2026-07-21 추가 출처 섹션 신설)
- `04-산업별-사례.md` 날짜 2026-07-20→2026-07-21, 공공·행정 > 한국 섹션에 AI 법령 비서 추가
- `02-프로덕션-아키텍처.md` 날짜 2026-07-20→2026-07-21, 멀티모달 섹션에 arXiv:2607.16604 추가, 비용·지연 섹션에 D-NOVA 추가
- `00-요약-트렌드.md` 날짜·사례 수·출처 수 갱신

### 검증 결과 (루프 #35)
| # | 사례 | URL 유효 | 요약-출처 일치 | 단언 완화 | ID/날짜 형식 | 중복 없음 |
|---|------|-----------|----------------|-----------|-------------|-----------|
| 1 | AI 법령 비서 (법제처·행안부·과기정통부) | snippet-verified (뉴스핌·ZDNet Korea·아시아투데이·이데일리·다음뉴스·디지털타임스·헬로디디·네이트뉴스 8개 독립 출처) | ✓ | ✓ | 2026-07-14 | ✓ |
| 2 | arXiv:2607.16604 "When Do Multimodal and Graph-Augmented RAG Help?" | snippet-verified (arXiv abs + arXiv html 2개 독립 출처) | ✓ | ✓ (정확도 수치 논문 기준 명시) | 2607.16604, 2026-07-18 | ✓ |
| 3 | arXiv:2607.17538 D-NOVA (MICRO 2026) | snippet-verified (arXiv abs + arXiv html 2개 독립 출처) | ✓ | ✓ (수치는 논문 발표 기준) | 2607.17538, MICRO 2026 | ✓ |

- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건
- 단언 톤다운: 0건 (수치는 논문·회사 발표 기준 명시로 처리)
- 중복 폐기: 0건
- 한국 사례: 1건 (AI 법령 비서)
- 발굴 시도 → 최종 채택: 약 7건 시도 → 3건 채택

## 2026-07-20 (일일 루프 #34)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **LG전자 파트리버(PartRiever) — 부품 탐색 RAG 에이전트 (2026-07-03)**: 자연어 질의로 2D 도면·3D 형상·기술 문서를 종합 분석하는 R&D 부품 탐색 AI 에이전트. 부품 탐색 소요 시간 수일→30분, 전기레인지 신제품 PoC에서 550개 후보 부품 분석 후 신규 개발 부품 수 25% 절감. PoC 단계, 연내 전사 확대 예정. → `04-산업별-사례.md` 제조·자동차 > 한국 섹션(신설)에 추가 [한국 사례]
  2. **SRAG: Lightweight and Specialized RAG at the Edge (SIGIR 2026, DOI: 10.1145/3805712.3809702, 2026-07-20)**: 엣지 서버별 도메인 인식 특화 지식 베이스 유지 + 버퍼 기반 도메인 외 콘텐츠 마이그레이션. 단일 범용 지식 베이스의 한계(검색 관련성 저하, 저장 비효율)를 극복. retrieval relevance·generation quality·storage efficiency 동시 향상. → `02-프로덕션-아키텍처.md` 보안·거버넌스 섹션에 추가
  3. **GeoRAG (arXiv:2606.29328, ICTIR'26 @ SIGIR 2026, 2026-07-25 멜버른)**: 컨텍스트 선택을 정보 수요 커버리지 최적화 문제로 재정의. 다양성 서브 질의 2단계 생성 + 역방향 검증 품질 가중치 + Sinkhorn-Wasserstein 거리 최소화로 선택. 6개 오픈도메인 QA 벤치마크에서 top-k 대비 EM +6.5~+7.5%p (HotpotQA·ASQA 최대 +9.7%p). → `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션에 추가
- `sources.md`에 3개 출처 추가 (## 2026-07-20 추가 출처 섹션 신설)
- `04-산업별-사례.md` 날짜 2026-07-19→2026-07-20, 제조·자동차 > 한국 섹션 신설 후 LG전자 파트리버 추가
- `02-프로덕션-아키텍처.md` 날짜 2026-07-19→2026-07-20, 검색·리랭킹 섹션에 GeoRAG 추가, 보안·거버넌스 섹션에 SRAG 추가
- `00-요약-트렌드.md` 날짜 2026-07-19→2026-07-20, 사례 수 142+→145+, 출처 수 248+→251+, 섹션 1.2에 GeoRAG 트렌드 노트, 섹션 1.5에 SRAG 엣지 RAG 트렌드 노트 추가

### 검증 결과 (루프 #34)
| # | 사례 | URL 유효 | 요약-출처 일치 | 단언 완화 | ID/날짜 형식 | 중복 없음 |
|---|------|-----------|----------------|-----------|-------------|-----------|
| 1 | LG전자 파트리버 (뉴스웍스) | snippet-verified (뉴스웍스·더퍼블릭·EBN·이데일리·네이트·포인트데일리·시사저널e·소셜밸류 8개 독립 출처) | ✓ | ✓ (회사 발표 기준 명시) | 2026-07-03 | ✓ |
| 2 | SRAG (ACM SIGIR 2026) | snippet-verified (SIGIR 2026 RAG Systems 세션 + ACM DOI 2개 독립 출처) | ✓ | ✓ | 2026-07-20 (SIGIR 2026) | ✓ |
| 3 | GeoRAG (arXiv:2606.29328) | snippet-verified (arXiv abs + arXiv html + ICTIR'26 proceedings 3개 독립 출처) | ✓ | ✓ | 2026-06-28 제출, ICTIR'26 @ SIGIR 2026-07-25 | ✓ |

- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건
- 단언 톤다운: 0건 (회사 발표 기준 표현 명시로 처리)
- 중복 폐기: 0건
- 한국 사례: 1건 (LG전자 파트리버)
- 발굴 시도 → 최종 채택: 약 9건 시도 → 3건 채택

## 2026-07-19 (일일 루프 #33)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **LG AI Research EXAONE Data Foundry × 국민연금공단 (ICML 2026, 2026-07-08)**: 생성형 AI 기반 도메인 전문 데이터 자동 생성 플랫폼. 기존 60명 전문가 3개월 수작업을 EXAONE 장문 컨텍스트 처리(최대 32,768 토큰) 기반 RAG 자동화 파이프라인으로 대체. 국민연금공단 파일럿에서 하루 1만 건+ 전문 데이터 자동 구축, 생산성 1,000배 이상 향상, 데이터 품질 평균 20% 이상 향상(회사 발표 기준). → `04-산업별-사례.md` 공공·행정 > 한국 섹션에 추가 [한국 사례]
  2. **Search for Coverage (arXiv:2605.28522, SIGIR 2026, 2026-07-20~24 멜버른)**: 장문형 RAG에서 관련성 최적화 검색기가 정보 커버리지를 낮추는 구조적 문제를 해결. 질의를 원자적 서브 질문으로 분해하고 응답 가능성을 증강 신호로 활용해 커버리지 직접 최적화. 13개 BEIR + 3개 nugget-based 커버리지 벤치마크에서 유의미한 향상. → `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션에 추가
  3. **AED-RAG (ACL 2026 Findings, arXiv 미공개)**: 비구조화 패시지·구조화 트리플렛·파라메트릭 메모리를 단일 확률 공간으로 투영하고 소프트 토큰 레벨로 동적 퓨전하는 적응형 앙상블 디코딩. 유용성 예측기(대조 퍼플렉시티) 파인튜닝으로 세분화 불일치 사전 제거. → `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션에 추가
- `sources.md`에 3개 출처 추가 (## 2026-07-19 추가 출처 섹션 신설)
- `04-산업별-사례.md` 날짜 2026-07-18→2026-07-19, 공공·행정 > 한국 섹션에 EXAONE Data Foundry 추가
- `02-프로덕션-아키텍처.md` 날짜 2026-07-18→2026-07-19, 검색·리랭킹 섹션에 Search for Coverage + AED-RAG 추가
- `00-요약-트렌드.md` 날짜 2026-07-18→2026-07-19, 사례 수 139+→142+, 출처 수 245+→248+, 섹션 1.2에 Search for Coverage + AED-RAG 트렌드 노트 추가

### 검증 결과 (루프 #33)
| # | 사례 | URL 유효 | 요약-출처 일치 | 단언 완화 | ID/날짜 형식 | 중복 없음 |
|---|------|-----------|----------------|-----------|-------------|-----------|
| 1 | EXAONE Data Foundry × 국민연금공단 (LG AI Research) | snippet-verified (7+ 독립 출처: Korea Times + Herald경제 + 이투데이 + 서울경제 + Businesskorea + Korea Herald + BigGo Finance) | ✓ | ✓ (회사 발표 기준 명시) | 2026-07-08 (ICML 2026) | ✓ |
| 2 | Search for Coverage (arXiv:2605.28522) | snippet-verified (arXiv pdf + SIGIR 2026 공식 proceedings DOI + SIGIR accepted papers 목록) | ✓ | ✓ | SIGIR 2026 (2026-07-20~24) | ✓ |
| 3 | AED-RAG (ACL 2026 Findings) | snippet-verified (ACL Anthology + ACL 2026 Findings 목록) | ✓ | ✓ | ACL 2026 Findings | ✓ |

- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건
- 단언 톤다운: 0건 (회사 발표 기준 표현 명시로 처리)
- 중복 폐기: 0건
- 한국 사례: 1건 (EXAONE Data Foundry × 국민연금공단)
- 발굴 시도 → 최종 채택: 약 8건 시도 → 3건 채택

## 2026-07-18 (일일 루프 #32)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 2건 포함)
  1. **현대차증권 — HAI 1.0: 사내 문서 RAG 기반 AI 에이전트 (2026-07-09)**: Claude Sonnet 4.5 기반 클라우드 플랫폼 + RAG 파이프라인으로 사내 규정·지침·업무 문서 Q&A + 문서 요약 시스템 구축. AX 전략 하에 중소형 증권사 최초 클라우드 AI 에이전트 도입. 연내 HAI 2.0(전사 공통 AI 플랫폼) 구축 예정. → `04-산업별-사례.md` 금융 > 한국 섹션에 추가 [한국 사례]
  2. **과기정통부 "모두의 AI" — 전 국민 무료 AI 챗봇 + 공공서비스 RAG 에이전트 (2026-07-13)**: 전 국민(5,200만명) 무료·무제한 AI 챗봇 + RAG 기반 공공서비스 신청 대행 에이전트. 국내 독자 AI 모델(Solar·A.X K1·EXAONE 등) 50%+ 의무 사용, 정부 B200 GPU 512개 제공. 8월 사업자 선정·9월 베타·12월 정식 출시 예정. → `04-산업별-사례.md` 공공·행정 섹션 신설(한국 최초) [한국 사례]
  3. **FastV-RAG — 비디오 QA용 추측적 디코딩 + RAG 파이프라인 (arXiv:2601.01513, ACL 2026 Main)**: 유사도 기반 필터링으로 개체 인식 오류 완화 + 경량 드래프트 모델→고성능 검증 모델 추측적 디코딩 구조로 약 2배 추론 속도 향상. 저자: Gen Li(UESTC), Peiyu Liu(UIBE). → `02-프로덕션-아키텍처.md` 멀티모달 섹션에 추가
- `sources.md`에 3개 출처 추가 (## 2026-07-18 추가 출처 섹션 신설)
- `04-산업별-사례.md` 날짜 2026-07-16→2026-07-18, 금융 > 한국 섹션에 현대차증권 HAI 1.0 추가, 공공·행정 섹션 신설 후 모두의 AI 추가
- `02-프로덕션-아키텍처.md` 날짜 2026-07-16→2026-07-18, 멀티모달 섹션에 FastV-RAG 추가

### 검증 결과 (루프 #32)
| # | 사례 | URL 유효 | 요약-출처 일치 | 단언 완화 | ID/날짜 형식 | 중복 없음 |
|---|------|-----------|----------------|-----------|-------------|-----------|
| 1 | 현대차증권 HAI 1.0 (서울경제) | snippet-verified (3+ 독립 출처) | ✓ | ✓ | 2026-07-09 | ✓ |
| 2 | 과기정통부 모두의 AI | snippet-verified (5+ 독립 출처) | ✓ | ✓ (G20 최초 → 보도됨) | 2026-07-13 | ✓ |
| 3 | FastV-RAG (arXiv:2601.01513) | snippet-verified (4+ 독립 출처) | ✓ | ✓ | ACL 2026 Main | ✓ |

- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건
- 단언 톤다운: 1건 (모두의 AI "G20 최초" → "G20 최초로 보도됨")
- 중복 폐기: 0건
- 한국 사례: 2건 (현대차증권 HAI 1.0, 모두의 AI)
- 발굴 시도 → 최종 채택: 약 10건 시도 → 3건 채택

## 2026-07-17 (일일 루프 #31)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 2건 포함)
  1. **올거나이즈(Allganize) — RARE: 기업용 RAG 평가의 구조적 한계 실증 (ACL 2026 Main, arXiv:2604.19047)**: 금융 보고서·법률 문서 고중복 코퍼스에서 기존 RAG 검색 정확도가 77.9%→8.5%(금융)→5.0%(법률)로 급락함을 실증. RARE(원자적 사실 분해 + CRRF 랭크 퓨전)로 엔터프라이즈 특화 평가 프레임워크 제안. ACL 2026 Main Conference(2026-07-02, San Diego) 채택. → `01-엔터프라이즈-사내지식.md` 한국 사례 섹션에 추가 [한국 사례]
  2. **바이브컴퍼니(VAIV) × 고려대 × Copenhagen × UC Berkeley — 저정밀 RAG 검색 정확도 회복: HPS + TRM (ACL 2026 Main, arXiv:2508.03306)**: 저정밀 환경의 RAG 검색 동점 문제를 최종 스코어링 레이어만 FP32 업캐스트(HPS)로 해소. Tie-aware Retrieval Metric(TRM)으로 평가 불확실성 정량화. ACL 2026 Main Conference(2026-07-02, San Diego) 채택. → `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션에 추가 [한국 사례]
  3. **CA-RAG — 쿼리별 검색 깊이 적응형 비용 인식 라우팅 (arXiv:2606.02581, 2026-06)**: 쿼리별 최적 검색 깊이를 스칼라 유틸리티 최대화로 동적 선택하는 라우터. 항상-밀집-검색 대비 토큰 비용 26% 절감, 항상-직접-추론 대비 지연 34% 감소하면서 품질 동등 유지. → `02-프로덕션-아키텍처.md` 비용·지연 엔지니어링 섹션에 추가
- `sources.md`에 3개 출처 추가 (## 2026-07-17 추가 출처 섹션 신설)
- `01-엔터프라이즈-사내지식.md` 한국 사례 섹션에 Allganize RARE 추가
- `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션에 VAIV HPS/TRM 추가, 비용·지연 엔지니어링 섹션에 CA-RAG 추가

### 검증 결과 (루프 #31)
| # | 사례 | URL 유효 | 요약-출처 일치 | 단언 완화 | ID/날짜 형식 | 중복 없음 |
|---|------|-----------|----------------|-----------|-------------|-----------|
| 1 | Allganize RARE (arXiv:2604.19047) | snippet-verified (4+ 독립 출처) | ✓ | ✓ | 2026-07-02 (ACL 2026 Main) | ✓ |
| 2 | VAIV HPS/TRM (arXiv:2508.03306) | snippet-verified (3+ 독립 출처) | ✓ | ✓ | 2026-07-02 (ACL 2026 Main) | ✓ |
| 3 | CA-RAG (arXiv:2606.02581) | snippet-verified (4+ 독립 출처) | ✓ | ✓ | 2026-06 | ✓ |

## 2026-07-16 (일일 루프 #30)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 전건; 한국 사례 1건 포함)
  1. **LG AI Research × KOSCOM — EXAONE Business Intelligence 금융 AI 에이전트 (2026-07-07)**: ChatEXAONE RAG 기술 기반 4-에이전트 구조(저널리스트→이코노미스트→애널리스트→의사결정)로 한국·미국 상장사 8,000개 이상을 매일 자동 분석해 예측 점수 + 코멘터리 생성. 2025년 9월 LSEG와 상용 런칭 후 2026년 7월 KOSCOM과 계약 체결해 국내 금융 인프라에 공급. → `04-산업별-사례.md` 금융 > 한국 섹션에 추가 [한국 사례]
  2. **arXiv:2607.11933 — LLM→크로스 인코더 지식 증류 RAG 리랭커 (2026-07-11)**: LLaMA 3 (8B)를 LoRA SFT + 4비트 양자화 2단계로 파인튜닝해 크로스 인코더 드롭인 대체 리랭커 구현. 크로스 인코더 이차 비용 문제 해소하면서 답변 정확도 +21% 향상. → `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션에 추가
  3. **arXiv:2607.11464 — FAIR GraphRAG: FAIR 원칙 기반 과학 데이터 그래프 RAG (2026-07-13)**: FAIR 디지털 오브젝트(FDO)를 그래프 노드로 통합해 과학·의료 데이터의 추적성·재현성·상호운용성을 GraphRAG에서 구조적으로 보장. RWTH Aachen Univ. → `02-프로덕션-아키텍처.md` GraphRAG 섹션에 추가
- `sources.md`에 3개 출처 추가 (## 2026-07-16 추가 출처 섹션 신설)
- `04-산업별-사례.md` 날짜 2026-07-13→2026-07-16, 금융 > 한국 섹션에 EXAONE BI 추가
- `02-프로덕션-아키텍처.md` 날짜 2026-07-15→2026-07-16, 검색·리랭킹 섹션에 arXiv:2607.11933 추가, GraphRAG 섹션에 arXiv:2607.11464 추가

### 검증 결과 (루프 #30)
| # | 사례 | URL 유효 | 요약-출처 일치 | 단언 완화 | ID/날짜 형식 | 중복 없음 |
|---|------|-----------|----------------|-----------|-------------|-----------|
| 1 | EXAONE BI (LG AI × KOSCOM) | snippet-verified (5+ 출처) | ✓ | ✓ | 2026-07-07 | ✓ |
| 2 | arXiv:2607.11933 LLM→크로스인코더 | snippet-verified (2 출처) | ✓ | ✓ | 2026-07-11 | ✓ |
| 3 | arXiv:2607.11464 FAIR GraphRAG | snippet-verified (4 출처) | ✓ | ✓ | 2026-07-13 | ✓ |

## 2026-07-15 (일일 루프 #29)
- **신규 사례 2건** (WebFetch 403 차단 환경, snippet-verified 2건; 한국 사례 2건 포함)
  1. **arXiv:2512.20136 — M³KG-RAG: 고려대·성균관대·NVIDIA·한화시스템 CVPR 2026 멀티홉 멀티모달 KG-RAG (2026-06)**: 기존 MMKG의 멀티홉 연결성 부재 + 공유 임베딩 유사도 검색의 무관·중복 지식 여과 실패 두 가지 한계를 동시에 해소. GRASP(Grounded Retrieval And Selective Pruning): 시각·청각 그라운딩으로 무관 트리플렛 제거하는 경량 선택적 프루닝. 멀티 에이전트 파이프라인으로 멀티홉 M³KG 자동 구축. 오디오·비디오·오디오-비주얼 QA 복수 벤치마크에서 베이스 MLLM 대비 유의미한 성능 향상. 저자: Hyeongcheol Park(고려대), Jiyoung Seo(성균관대), Wonmin Byeon(NVIDIA), JeungSub Lee(한화시스템), Sangpil Kim(고려대). → `02-프로덕션-아키텍처.md` GraphRAG / 지식 그래프 결합 섹션에 추가 [한국 사례]
  2. **arXiv:2509.15577 — R2U: 서울대 Seung-won Hwang 팀 ACL 2026 Findings 관련성→유용성 프로세스 감독 재작성 (2026-07)**: 검색 관련성(topical relevance)과 생성 유용성(generation utility) 간 구조적 간극을 직접 최소화하는 프로세스 감독 재작성 프레임워크. 재작성과 답변 생성을 추론 과정에서 동시에 관찰해 진정한 유용성 근사. 나이브 RAG 대비 평균 F1 +6.8%p, 최고 기존 기준선 대비 +5.6%p. 저자: Jaeyoung Kim, Jongho Kim, Seung-won Hwang(서울대), Seoho Song, Young-In Song. → `02-프로덕션-아키텍처.md` 질의 변환·확장 섹션에 추가 [한국 사례]
- `sources.md`에 2개 출처 추가 (## 2026-07-15 추가 출처 섹션 신설)
- `02-프로덕션-아키텍처.md` 날짜 2026-07-14→2026-07-15, GraphRAG 섹션에 M³KG-RAG 추가, 질의 변환·확장 섹션에 R2U 추가

### 검증 결과
- URL 200 OK: 0/2건 (WebFetch 전체 403 차단)
- snippet-verified: 2/2건 (arXiv:2512.20136: arXiv abs + NVIDIA Research + CVPR OpenAccess PDF + YouTube 발표 영상 4개 독립 출처; arXiv:2509.15577: arXiv abs + ACL 2026 Findings 목록 + Seung-won Hwang SNU 프로필 3개 독립 출처)
- 단언 톤다운: 0건
- 중복 폐기: 2건 (KT K-RAG: 01-엔터프라이즈-사내지식.md 2026-06-17 기수록 확인; LangChain Interrupt 2026 LATAM Airlines: sources.md 기수록 확인)
- 한국 사례: 2건 (M³KG-RAG — 고려대·성균관대·한화시스템 산학협력 CVPR 2026; R2U — 서울대 Seung-won Hwang 팀 ACL 2026 Findings)
- 발굴 시도 → 최종 채택: 약 4건 시도 → 2건 채택

## 2026-07-14 (일일 루프 #28)
- **신규 사례 2건** (WebFetch 403 차단 환경, snippet-verified 2건; 한국 사례 1건 포함)
  1. **arXiv:2607.09092 — AgentKGV: NAVER × 성균관대 에이전틱 LLM-RAG 기반 지식 그래프 팩트 검증 (2026-07-10)**: 자동 구성된 대규모 KG의 사실 오류를 산업 규모에서 검증하는 에이전틱 LLM-RAG 프레임워크. NAVER 엔지니어(Hyeon-gu Lee, Sumin Seo)와 성균관대(Yumin Heo, Youngjoong Ko 교수) 공동 개발. 동적 라우팅(파라메트릭 vs 외부 검색) + 반복 쿼리 재작성으로 표면 표현 불일치 극복. SFT+GRPO 2단계 학습으로 T-REx 및 NAVER 한국 엔터프라이즈 KG 벤치마크 모두 최고 성능. → `03-에이전트-툴유즈-MCP.md` 2026년 주목할 신규 연구 섹션에 추가 [한국 사례]
  2. **arXiv:2607.11683 — RAGU: 컴팩트 도메인 특화 LLM 기반 멀티스텝 GraphRAG 엔진 (2026-07-13)**: 기존 GraphRAG 단일 패스 추출의 노이즈·불안정 검색 문제를 추출-통합 분리 2단계 파이프라인으로 해결한 오픈소스 GraphRAG 엔진. Meno-Lite-0.1(7B)이 Qwen2.5-32B를 KG 구성에서 +12.5% 조화평균 초과. 저자: Mikhail Komarov 외 (ITMO Univ. 등). → `02-프로덕션-아키텍처.md` GraphRAG / 지식 그래프 결합 섹션에 추가
- `sources.md`에 2개 출처 추가
- `02-프로덕션-아키텍처.md` 날짜 2026-07-13→2026-07-14, GraphRAG 섹션에 RAGU 추가
- `03-에이전트-툴유즈-MCP.md` 2026년 주목할 신규 연구 섹션에 AgentKGV 추가

### 검증 결과
- URL 200 OK: 0/2건 (WebFetch 전체 403 차단)
- snippet-verified: 2/2건 (arXiv:2607.09092: arXiv abs + html + cs.CL listing + ResearchGate 저자 소속 3개 이상 독립 출처; arXiv:2607.11683: arXiv abs + html + 검색 스니펫 2개 이상 독립 출처)
- 단언 톤다운: 0건
- 중복 폐기: 0건 (2607.09092·2607.11683 모두 sources.md 미수록 확인)
- 한국 사례: 1건 (AgentKGV — NAVER × 성균관대 산학협력 논문, NAVER 한국 엔터프라이즈 KG 평가)
- 발굴 시도 → 최종 채택: 약 4건 시도 → 2건 채택 (SK하이닉스 AWS 블로그: 2025-02 발행으로 대상 기간 외 → 제외)

## 2026-07-13 (일일 루프 #27)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 3건; 한국 사례 1건 포함)
  1. **LY Corp Tech-Verse 2026 — Semantic Context OS / PathAlign (2026-06-29)**: 코드 인텔리전스 AI 에이전트용 RAG 대체 아키텍처. 벡터 거리 탐색 대신 정적 AST 파싱 기반 PathAlign으로 구문 트리 보존 컨텍스트 수집. LINE Yahoo(LY Corp) 내부 에이전트 운용 사례. → `02-프로덕션-아키텍처.md` 한국 환경 특이점 > 한국 기업·솔루션 섹션에 추가 [한국 사례]
  2. **arXiv:2607.07721 — Context Graphs for Proactive Enterprise Agents (2026-07)**: 반응형 RAG 한계 비판 + 선제형 에이전트 아키텍처 제안. Context Graph(라이브 엔티티·관계·상태 모델) + Delta Detection Engine + Proactivity Scorer + Claude API 기반 Surfacing Layer. Precision@5=0.83, FP=0.11, 컨텍스트 인지→알림 47분→30초 미만. NetworkX + Anthropic Claude API Python 구현. → `03-에이전트-툴유즈-MCP.md` 2026년 주목할 신규 연구 섹션에 추가
  3. **arXiv:2607.08269 — PolyUQuest: Verifiable Structure-Aware Web RAG (2026-07)**: 웹 RAG를 위한 이종 그래프(hyperlink topology + DOM hierarchy + entity-relation) 기반 구조 인식 검색. PolyU 4,240페이지 공식 웹사이트 평가. 기존 RAG 대비 정확성·커버리지·충실성 우위, LLM 토큰 절감. 학생 대상 QA 서비스 배포 준비 중. → `04-산업별-사례.md` 교육 > 글로벌 섹션에 추가
- `sources.md`에 3개 출처 추가
- `02-프로덕션-아키텍처.md` 날짜 2026-07-12→2026-07-13, 한국 기업·솔루션 섹션에 LY Corp 항목 추가
- `03-에이전트-툴유즈-MCP.md` 신규 연구 섹션에 arXiv:2607.07721 추가
- `04-산업별-사례.md` 날짜 2026-07-11→2026-07-13, 교육 > 글로벌 섹션에 arXiv:2607.08269 추가

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (LY Corp Semantic Context OS: techblog.lycorp.co.jp 한/영/일 3개 이상 독립 출처; arXiv:2607.07721: arXiv abs + html + arxiv-sanity 복수 독립 출처; arXiv:2607.08269: arXiv abs + html 2개 독립 출처)
- 단언 톤다운: 0건
- 중복 폐기: 0건 (3건 모두 sources.md 미수록 확인)
- 한국 사례: 1건 (LY Corp Semantic Context OS — LINE Yahoo 엔지니어링 블로그)
- 발굴 시도 → 최종 채택: 약 5건 시도 → 3건 채택

## 2026-07-12 (일일 루프 #26)
- **신규 사례 2건** (WebFetch 403 차단 환경, snippet-verified 2건; 한국 사례 0건 — 7월 7-12일 대상 접근 가능한 1차 출처 발굴 실패)
  1. **arXiv:2604.26649 — ReaLM-Retrieve: 추론 모델 단계별 불확실성 감지 적응형 검색 (SIGIR 2026, 2026-04)**: DeepSeek-R1·o1 계열 대형 추론 모델(LRM)의 확장 CoT 체인과 RAG의 "추론 전 컨텍스트 주입" 간 구조적 불일치를 해소하는 적응형 검색 프레임워크. 단계별 불확실성 감지기 + 검색 개입 정책 + 효율 최적화(나이브 통합 대비 3.2배 오버헤드 감소). SIGIR 2026(2026-07-20~24, 멜버른) 발표 8일 전 타이밍. → `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션에 추가
  2. **arXiv:2606.29645 — Metadata, Structure, or Strategy? RAG 컨텍스트 보강 분해 분석 (ECML-PKDD 2026, 2026-06-29)**: 메타데이터·구조·검색 전략 중 무엇이 RAG 성능을 결정하는지 체계적 분해 분석. 처리 가능성 위계(Processability Hierarchy) 프레임워크 도입: 모델 사전 학습 특성 기반 메타데이터 활용 예측. 정렬된 환경에서 소형 모델이 프론티어 모델을 F1 기준 19점 상회. RAG 설계를 메타데이터 축적→모델-컨텍스트 정렬 관점으로 전환 제안. → `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션에 추가
- `sources.md`에 2개 출처 추가
- `02-프로덕션-아키텍처.md` 날짜 2026-07-11→2026-07-12, 검색·리랭킹 섹션에 2건 추가

### 검증 결과
- URL 200 OK: 0/2건 (WebFetch 전체 403 차단)
- snippet-verified: 2/2건 (arXiv:2604.26649: arXiv abs + SIGIR 2026 프로그램 + ACL Anthology + arXiv pdf 4개 독립 출처; arXiv:2606.29645: arXiv abs + ECML-PKDD 2026 확인 2개 이상 독립 출처)
- 단언 톤다운: 0건
- 중복 폐기: 0건 (2604.26649·2606.29645 모두 sources.md 미수록 확인)
- 한국 사례: 0건 발굴 — 7월 7-12일 대상 접근 가능한 국내 tech blog 1차 출처 없음 (7월 10일 루프와 동일 상황)
- 발굴 시도 → 최종 채택: 약 5건 시도 → 2건 채택

## 2026-07-11 (일일 루프 #25)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 3건; 한국 사례 1건 포함)
  1. **네이버 쇼핑앱 — 쇼핑 AI 에이전트 (Shopping Intelligence, 2026-07-01 출시)**: 커머스 특화 LLM "Shopping Intelligence"(100억 건 쇼핑 기록 학습) + 탐색·비교·추천 3개 서브 에이전트 + 프로액티브 대화 트리거(사용자 쇼핑 맥락 기반 에이전트 선행 발화). 범용 LLM+RAG 대신 도메인 특화 LLM과 멀티 에이전트 분업으로 상품 정보 정확도 확보. → `01-엔터프라이즈-사내지식.md` 한국 사례 추가 (한국 30→31건, 총 47→48건)
  2. **AI21 멀티스케일 청킹 — 쿼리 의존형 최적 청크 크기 (2026-03, AIEWF 2026)**: 단일 고정 청크 크기의 구조적 한계(oracle gap 20–40%+)를 정량화. 100/200/500 토큰 멀티 인덱스 + RRF로 1–37% 리콜 향상. 모델 어그노스틱, 재학습 불필요. AIEWF 2026 "Stop Chunking Like It's 2022" 세션 발표. → `02-프로덕션-아키텍처.md` 청킹 전략 섹션에 추가
  3. **arXiv:2607.03880 — Walmart InvAwr-RAG: 재고 인식 RAG 스폰서드 검색 키워드 생성 (SIGIR eCom'24)**: 의미 검색 + 실시간 재고 필터링 RAG로 스폰서드 검색 키워드 자동 생성. Fill Rate 68% 향상(GPT-4 기준선 대비). 동적 생성 + 히스토리 기반 + RRF 앙상블 구조. SIGIR eCom 2024 원발표, arXiv 2026-07 게시. → `04-산업별-사례.md` 커머스·고객서비스 > 글로벌 섹션 신설 후 추가
- `sources.md`에 3개 출처 추가
- `01-엔터프라이즈-사내지식.md` 날짜 2026-07-09→2026-07-11, 한국 30→31건, 총 47→48건
- `02-프로덕션-아키텍처.md` 날짜 2026-07-10→2026-07-11
- `04-산업별-사례.md` 날짜 2026-07-10→2026-07-11, 커머스·고객서비스에 글로벌 서브섹션 신설

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (네이버 쇼핑 AI 에이전트: navercorp.com 공식 + daum.net + bizwatch.co.kr + etoday.co.kr + designcompass.org 5개 이상 독립 출처; AI21 멀티스케일 청킹: ai21.com blog + GitHub AI21Labs + AIEWF 2026 발표 3개 이상 독립 출처; arXiv:2607.03880: arXiv abs + html + semanticscholar.org + sigir-ecom.github.io 4개 독립 출처)
- 단언 톤다운: 0건
- 중복 폐기: 3건 (arXiv:2607.05438 출처 1개뿐 → 폐기; 삼성 STC 2025 DeepDive 8개월 이상 구형 → 폐기; KAI×네이버 국방 AI MOU RAG 특정성 없음 → 폐기)
- 발굴 시도 → 최종 채택: 약 6건 시도 → 3건 채택

## 2026-07-10 (일일 루프 #24)
- **신규 사례 2건** (WebFetch 403 차단 환경, snippet-verified 2건; 한국 사례 0건 — 대상 기간 접근 가능한 1차 출처 발굴 실패)
  1. **arXiv:2607.06641 — Healthier LLMs: 공중보건 QA를 위한 RAG (2026-07-07)**: 영국 공중보건 지침(PubHealthBench, 7,929개 Q&A)에서 하이브리드 검색이 리콜·랭킹 품질을 일관되게 향상시킴을 실증. 최적 청크 크기가 도메인·주제별로 달라지며, 개방형 응답 평가의 필요성 제기. 영국 기반 연구팀. → `04-산업별-사례.md` 의료 > 글로벌 섹션에 추가
  2. **arXiv:2607.07302 — Evaluating RAG Metrics in Applied Contexts: 자동 RAG 지표 vs 인간 평가 괴리 실무 검증 (2026-07-08)**: Ragas·DeepEval·RAGChecker·Opik 4개 라이브러리의 자동 지표를 실제 비즈니스 QA 데이터셋에 적용, 인간 평가·recall과의 상관관계 체계 분석. 자동 지표가 실무 맥락에서 인간 평가와 항상 일치하지 않음을 실증. Quentin Brabant, Orange Research. EvalLLM 2026 영문 번역. → `02-프로덕션-아키텍처.md` RAG 평가 섹션에 추가
- `sources.md`에 2개 출처 추가
- `02-프로덕션-아키텍처.md` 날짜 2026-07-09→2026-07-10, 자동 RAG 지표 vs 인간 평가 괴리 섹션 추가
- `04-산업별-사례.md` 날짜 2026-07-09→2026-07-10, arXiv:2607.06641 공중보건 QA RAG 항목 추가

### 검증 결과
- URL 200 OK: 0/2건 (WebFetch 전체 403 차단)
- snippet-verified: 2/2건 (arXiv:2607.06641: abs + html 2개 arXiv 출처; arXiv:2607.07302: abs + html 2개 arXiv 출처)
- 단언 톤다운: 0건
- 중복 폐기: 0건 (2607.06641·2607.07302 모두 sources.md 미수록 확인)
- 한국 사례: 0건 발굴 — 7월 7-10일 대상 접근 가능한 국내 tech blog 1차 출처 없음 (삼성 Tech Blog 기사 검토 → 1월 29일 발행으로 대상 기간 외; 카카오페이증권 AI 어닝콜은 RAG 전용 사례 아님)
- 발굴 시도 → 최종 채택: 약 5건 시도 → 2건 채택

## 2026-07-09 (일일 루프 #23)
- **업데이트 1건 + 신규 사례 2건** (WebFetch 403 차단 환경, snippet-verified 3건)
  1. **[업데이트] 네이버 — AI탭 하네스 엔지니어링 + Clarify RL (2026-07-02 Tech Deep Talk)**: 기존 네이버 AI탭 정식 출시 항목에 2026-07-02 AI 검색 Tech Deep Talk에서 공개된 기술 아키텍처 추가. 하네스 엔지니어링 4단계 파이프라인(안전 필터→의도·맥락 관리→서비스 연계 추론→출처·액션 실행), Clarify RL(불확실 시 추가 질문으로 의도 확인), 분업형 SLM 구조(역할별 특화 SLM 조합). 공개 수치: HCX 대비 환각 30%p 감소·응답 속도 2배·운영 비용 1/3 → `01-엔터프라이즈-사내지식.md` 기존 네이버 AI탭 항목 업데이트
  2. **arXiv:2607.00013 — GRACE-RAG: 기관 특화 폐쇄 도메인 그래프 증강 거버넌스 검색 (2026-07)**: 엔티티 밀도가 높은 기관 도메인에서 벡터 단독 검색의 구조적 한계를 극복하는 그래프 증강 검색 레이어 제안. 구조적 추론을 생성 단계 대신 오프라인 검색 사전 처리로 외재화. Mistral 24B·GPT OSS 120B·Gemini 2.5 Flash 3모델에서 일관 향상, 중간 규모 모델 기준 최대 20% 품질 향상. National Payments Corporation of India. COLM 2026 → `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션에 추가
  3. **arXiv:2607.06964 — 항공 자율 비행 계획 LLM+RAG+멀티모달 코치 에이전트 (ICML 2026 LM4Plan Workshop)**: 항공기 비행 계획 엔드투엔드 자동화를 위한 LLM+RAG 기반 메모리+멀티모달 코치 에이전트 파이프라인. RAG가 비행 규정·공역·절차 지식 제공, 코치 에이전트가 멀티모달 검증·재시도 지시. 안전 임계적 도메인에 LLM+RAG를 적용한 ICML 2026 Workshop 사례 → `04-산업별-사례.md` 과학·연구 섹션에 추가
- `sources.md`에 3개 출처 추가
- `01-엔터프라이즈-사내지식.md` 날짜 2026-07-08→2026-07-09, 기존 네이버 AI탭 항목 업데이트 (기술 아키텍처 상세 추가)
- `02-프로덕션-아키텍처.md` 날짜 2026-07-08→2026-07-09
- `04-산업별-사례.md` 날짜 2026-07-08→2026-07-09

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (네이버 Tech Deep Talk: digitaltoday + asiae + edaily + etoday + theguru + sedaily.en + koreatimes 7개 이상 독립 출처; arXiv:2607.00013: abs + html 2개 arXiv 출처; arXiv:2607.06964: arXiv robotics list + LM4Plan ICML26 workshop 2개 독립 출처)
- 단언 톤다운: 0건
- 중복 폐기: 0건 (네이버 Tech Deep Talk URL 신규, 2607.00013·2607.06964 모두 sources.md 미수록 확인)
- 발굴 시도 → 최종 채택: 약 6건 시도 → 3건 채택 (1건 업데이트 + 2건 신규)

## 2026-07-08 (일일 루프 #22)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 3건)
  1. **업스테이지 × 다음 — Solar RAG 기반 포털 AI 요약 베타 서비스 (2026-07-01)**: 업스테이지 인수 후 다음 포털에 자체 LLM Solar 기반 AI 요약 베타 서비스 출시. 36년 치 뉴스 PGC 데이터·사전·버티컬 DB를 Solar RAG 엔진과 실시간 연동. 이슈·금융·엔터·건강·사전·일상 6개 영역 우선 적용. AI 오버뷰→RAG→서치 에이전트→액션 에이전트 4단계 진화 로드맵 공개 → `01-엔터프라이즈-사내지식.md` 한국 사례 추가 (한국 29→30건, 총 46→47건)
  2. **arXiv:2607.04391 — MOSS: Memory-Orchestrated Semantic System (2026-07-05)**: 임베딩 유사도 기반 RAG의 불투명성·감사 불가능성을 비판하며 에이전트가 관계형 DB에 직접 질의하는 감사 가능한 메모리 아키텍처 제안. 검색 실행이 기호적·재현 가능(LLM 미참여). 1년간 실프로덕션 운영(44M 토큰, 11만 세그먼트, 16만 문서) → `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션에 추가
  3. **arXiv:2607.05055 — CareConnect: 의료 물류 안전 우선 대화 에이전트 (2026-07-06)**: 의료 물류(예약·변경·취소·시설 정보) 자동화를 위한 RAG + LLM 함수 호출 + 계층적 결정론적 안전 가드레일 3중 구조. 8개 도메인 특화 도구 오케스트레이션. 의료 진단·조언 범위 외 엄격 제한 → `04-산업별-사례.md` 의료 > 글로벌 섹션에 추가
- `sources.md`에 3개 출처 추가
- `01-엔터프라이즈-사내지식.md` 헤더 수정: 한국 29→30건, 총 46→47건, 날짜 2026-07-07→2026-07-08
- `02-프로덕션-아키텍처.md` 날짜 2026-07-07→2026-07-08
- `04-산업별-사례.md` 날짜 2026-07-06→2026-07-08

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (업스테이지×다음: v.daum.net + aitimes + hankyung + ebn 4개 이상 독립 출처; arXiv:2607.04391: abs + html 2개 arXiv 출처; arXiv:2607.05055: abs + html 2개 arXiv 출처)
- 단언 톤다운: 0건
- 중복 폐기: 3건 (arXiv:2607.05217 출처 1개 부족, arXiv:2507.05714 연도 오류 2025, LY Corp Tech-Verse 5단계 AX 이미 수록)
- 발굴 시도 → 최종 채택: 약 7건 시도 → 3건 채택

## 2026-07-07 (일일 루프 #21)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 3건)
  1. **LY Corporation — AX 로드맵: 레거시에서 AI 주도 프로젝트로 (2026-07-06)**: 레거시 소프트웨어를 AI 주도(AI-driven) 개발로 전환하는 4단계 AX 로드맵 공개. RAG 시스템을 지식 레이어로 활용해 AI가 스펙·히스토리를 참조하고, CI 이벤트 트리거를 통해 스펙→PR 워크플로를 자동화하는 Agentic 개발 파이프라인 구현 → `01-엔터프라이즈-사내지식.md` 한국 사례 추가 (한국 28→29건, 총 45→46건)
  2. **arXiv:2607.01852 — 학술 문서 RAG 청킹 전략 평가: 시맨틱 청킹이 항상 우위가 아니다 (2026-07-02)**: 스위스 대학원 논문 대상 RAGAs 기반 평가. 클러스터 기반 시맨틱 청킹이 고정 크기·재귀 청킹 대비 일관된 우위를 보이지 않음을 실증. RAGAs faithfulness 지표의 신뢰도 한계도 함께 확인 → `02-프로덕션-아키텍처.md` 청킹 전략 섹션에 추가
  3. **arXiv:2607.02966 — TR-RAG: 교차언어 RAG 언어 표류 문제 해결을 위한 교사 정규화 강화학습 (2026-07)**: 비영어권 질의 + 영어 증거 문서 RAG에서 언어 표류(language drift) 현상을 Teacher-Regularized RL로 억제. 언어 일관성 붕괴율 약 27pp 감소. BioASQ-ENKB5·HotPot-ENKB5·MKQA 벤치마크 → `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션에 추가
- `sources.md`에 3개 출처 추가
- `01-엔터프라이즈-사내지식.md` 헤더 수정: 한국 28→29건, 총 45→46건, 날짜 2026-07-06→2026-07-07
- `02-프로덕션-아키텍처.md` 날짜 2026-07-06→2026-07-07

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (LY Corp AX 로드맵: techblog.lycorp.co.jp 영문·일문 버전 2개 이상 독립 출처; arXiv:2607.01852: abs + html 2개 arXiv 출처; arXiv:2607.02966: arxiv.org 복수 독립 출처)
- 단언 톤다운: 0건
- 중복 폐기: 0건 (LY Corp AX 로드맵 URL sources.md 미수록 확인; 2607.01852·2607.02966 모두 기존 수록 범위 2607.01659 이후 신규 ID)
- 발굴 시도 → 최종 채택: 약 7건 시도 → 3건 채택

## 2026-07-06 (일일 루프 #20)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 3건)
  1. **KT Cloud × 카카오 — RAG Suite 2.0 + Kanana Safeguard 공공 AI 안전 파트너십 (2026-06-23/26)**: KT Cloud가 공공기관 고객용 RAG Suite 2.0(PII 마스킹·가드레일·한국어 파서·리랭킹 탑재)을 출시하고, 카카오와 MOU 체결해 Kanana Safeguard(국내 기업 최초 오픈소스 공개된 한국어 AI 가드레일 모델)를 통합. 망분리 환경 공공·금융 기관 대상 안전 RAG 아키텍처 구현 → `01-엔터프라이즈-사내지식.md` 한국 사례 추가 (한국 27→28건, 총 44→45건)
  2. **arXiv:2607.00012 — PRA-RAG: 검색 오염 공격 대응 이론적 강건성 RAG (2026-07)**: 임베딩 공간의 기하학적 구조로 독성 문서를 탐지하고 안정적 집합 표현을 도출하는 RAG 방어 기법. 이론적 강건성 상한(theoretical bound) 수학적 증명. Fudan University·WPI → `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션에 추가
  3. **arXiv:2606.01613 — TechRAG: Goodyear 타이어·차량 동역학 기술 문서 에이전틱 멀티모달 RAG (2026-06)**: FAISS+BM25+cross-encoder + Neo4j 지식 그래프 + ColSmol+MUVERA 시각 검색 + evidence-gated 재시도 구조로 40,000+ 기술 논문 페이지 처리. 제조 분야 첫 에이전틱 멀티모달 RAG 사례 → `04-산업별-사례.md` 신규 "## 제조·자동차" 섹션 생성
- `sources.md`에 3개 출처 추가
- `01-엔터프라이즈-사내지식.md` 헤더 수정: 한국 27→28건, 총 44→45건, 날짜 2026-07-05→2026-07-06
- `02-프로덕션-아키텍처.md` 날짜 2026-07-02→2026-07-06
- `04-산업별-사례.md` 날짜 2026-07-04→2026-07-06, 신규 "제조·자동차" 섹션 생성

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (KT Cloud×카카오: kakaocorp.com + ajunews + etoday + insightkorea + thelec + digitaltoday 6개 이상 독립 출처; arXiv:2607.00012: abs + html 2개 arXiv 출처; arXiv:2606.01613: abs + html + pdf 3개 arXiv 출처)
- 단언 톤다운: 0건
- 중복 폐기: 0건
- 발굴 시도 → 최종 채택: 약 7건 시도 → 3건 채택

## 2026-07-05 (일일 루프 #19)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 3건)
  1. **카카오페이증권 — 춘시리(ChoonSiri) RAG 업무도우미 봇 (2026-06-12)**: Confluence 사내 문서를 Amazon Bedrock + PGVector 스택으로 RAG화. 보안 정책상 외부 AI 사용 불가 환경에서의 내부 RAG 실증. RAG 모드/일반 LLM 모드 자동 분기 → `01-엔터프라이즈-사내지식.md` 한국 사례 추가 (한국 26→27건, 총 43→44건)
  2. **arXiv:2607.00725 — Budget-Constrained Multi-Hop RAG 진단 (2026-07-01)**: 예산 제약 RAG에서 문서 리콜 대신 answer-in-context 지표 제안. HotpotQA F1 예측 상관관계 향상. 서브모듈러 증거 패킹 방법 제시 → `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션에 추가
  3. **arXiv:2607.00798 — ClinRAG-GRAPH 유방암 pCR 예측 (2026-07-01)**: RAG+그래프 결합으로 멀티센터 MRI 이질성 극복. 내부 AUC 0.815, 외부 2센터 AUC 0.774/0.712 → `04-산업별-사례.md` 의료 > 글로벌 섹션에 추가
- `sources.md`에 3개 출처 추가
- `01-엔터프라이즈-사내지식.md` 헤더 수정: 한국 26→27건, 총 43→44건, 날짜 2026-07-04→2026-07-05

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (카카오페이 기술 블로그 검색 스니펫 2개 이상 독립 출처; arXiv:2607.00725 abs+html 2개 출처; arXiv:2607.00798 abs+html 2개 출처)
- 단언 톤다운: 0건
- 중복 폐기: 2건 (LY Corp PJ One Piece techverse2026-105: 이미 수록, SK하이닉스 AWS 블로그: 이미 수록)
- 발굴 시도 → 최종 채택: 약 8건 시도 → 3건 채택

## 2026-07-04 (일일 루프 #18)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 3건)
  1. **삼성리서치 — Agentic Search: LangGraph 기반 에이전트 RAG 프레임워크 (2026년 상반기)**: LangGraph 상태 그래프로 반복 검색(Iterative Retrieval) 구현. 에이전트가 검색 시점·질의 재구성·검색 결과 검증을 자율 결정. 복잡 질의(멀티 홉·비교·종합 추론)에서 단순 RAG 대비 정확도 향상 실증 → `01-엔터프라이즈-사내지식.md` 한국 사례 추가 (한국 25→26건, 총 42→43건)
  2. **대학 강의 멀티모달 RAG — 환각률 31.7%→6.6% 감소** (arXiv:2607.01115, 2026-07): VLM 기반 멀티모달 RAG로 강의 슬라이드의 다이어그램·수식을 직접 처리. 텍스트 전용 RAG 대비 환각률 31.7%→6.6%로 대폭 감소 → `04-산업별-사례.md` 교육 > 글로벌 섹션 추가
  3. **Rubin Observatory LSST — 천문 프로젝트 기술 문서 RAG** (arXiv:2607.01659, 2026-07): Weaviate+LangChain+GPT 오픈소스 스택으로 LSST 레거시 기술 문서를 자연어 검색 가능한 지식 베이스로 변환 → `04-산업별-사례.md` 신규 "## 과학·연구" 섹션 생성 (실패·논란 사례 앞)
- `sources.md`에 3개 출처 추가
- `01-엔터프라이즈-사내지식.md` 헤더 수정: 한국 25→26건, 총 42→43건, 날짜 2026-07-02→2026-07-04
- `04-산업별-사례.md` 헤더 날짜 2026-07-03→2026-07-04, 신규 "과학·연구" 섹션 생성

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (Samsung article/82: techblog.samsung.com 검색 결과 + 삼성 AI 블로그 참조 2개 이상; arXiv:2607.01115: arxiv.org/abs 검색 결과; arXiv:2607.01659: arxiv.org/abs 검색 결과 교차확인)
- 단언 톤다운: 1건 (Samsung date "2026-01-29" → "2026년 상반기"로 조정, 간접 출처 날짜 불확실)
- 중복 폐기: 없음 (sources.md 및 domain 파일 grep 확인, article/82·2607.01115·2607.01659 모두 미수록 확인)
- 발굴 시도 → 최종 채택: 약 10건 시도 → 3건 채택

## 2026-07-03 (일일 루프 #17)
- **신규 사례 3건** (WebFetch 403 차단 환경, snippet-verified 3건)
  1. **채널코퍼레이션(채널톡) — RAG 기반 B2B AI 상담 에이전트 ALF + AI 상담 시뮬레이션 출시 (2026-05-27)**: RAG 지식 베이스 + 노코드 워크플로우 이중 구조로 반복 문의 80% 자동 응답. 23만+ 기업 고객사, 누적 상담 650만 건. B2C 고객 대면 B2B SaaS에서 RAG 기반 CS 에이전트의 한국 대표 상용 사례 → `04-산업별-사례.md` 신규 "커머스·고객서비스 > 한국" 섹션 추가
  2. **DCCD — 이중 신뢰도 대조 디코딩** (arXiv:2607.00570, 2026-07-01): 멀티문서 RAG 내 충돌 정보 해소를 위한 training-free 디코딩 방법(DCCD). 문서 레벨 + 토큰 레벨 신뢰도 신호 결합. DRQA 벤치마크(엔터프라이즈 심층 리서치 시나리오) 제안 → `02-프로덕션-아키텍처.md` 검색·리랭킹 섹션 추가
  3. **Bayesian Uncertainty Propagation for Agentic RAG** (arXiv:2607.00972, 2026-07-01): 에이전틱 RAG 플래너·평가자·생성자 단계별 불확실성을 베이즈 네트워크로 전파·집계해 시스템 레벨 신뢰도 추정. HotpotQA 멀티홉 시나리오에서 효과 확인 (proof-of-concept) → `03-에이전트-툴유즈-MCP.md` 신규 연구 섹션 추가
- `sources.md`에 3개 출처 추가
- `04-산업별-사례.md` 헤더 날짜 2026-06-30→2026-07-03 업데이트, 신규 "커머스·고객서비스" 섹션 생성

### 검증 결과
- URL 200 OK: 0/3건 (WebFetch 전체 403 차단)
- snippet-verified: 3/3건 (채널코퍼레이션: ET News·ZDNet·byline.network·sisajournal·AI Times·platum.kr 6개 이상 독립 출처; arXiv:2607.00570: arxiv.org/abs + 복수 검색 결과 출처; arXiv:2607.00972: arxiv.org/abs + arxiv.org/html 2개 arXiv 출처 교차확인)
- 단언 톤다운: 1건 (채널코퍼레이션 "한국 No.1" 마케팅 문구 → "한국 대표 상용 사례"로 조정)
- 중복 폐기: 없음 (sources.md 및 domain 파일 grep 확인, 채널코퍼레이션·2607.00570·2607.00972 모두 미수록 확인)
- 발굴 시도 → 최종 채택: 약 12건 시도 → 3건 채택

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
