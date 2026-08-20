# 출처 목록

## 2026-08-20 일일 누적 추가 출처 (3건, 루프 #65)

### 한국 — 금융
- [ZDNet Korea — 신한투자증권, 구글 클라우드와 AI 에이전트 플랫폼 개발](https://zdnet.co.kr/view/?no=20260818151045) — 2026-08-18 · [korea][finance][agent-platform][gemini][rag][hybrid-orchestrator] · 신한투자증권 × 구글클라우드. Gemini Enterprise Agent Platform + 하이브리드 오케스트레이터 + BigQuery 데이터 플라이휠(내부 RAG). 500개+ 에이전트, 1년→3개월 단축. (snippet-verified: ZDNet Korea + 전자신문 + 서울경제 + VentureSquare + SentV 5개 이상 독립 출처)

### 글로벌 — 산업별 (항공·제조)
- [arXiv:2608.18465 — Reducing Technician Search Burden: A Multimodal RAG for Cessna 172 Maintenance Manual](https://arxiv.org/abs/2608.18465) — 2026-08 · [aviation][manufacturing][multimodal][mmr][maintenance-manual] · Seongjun Ha, Md Rashedul Islam, Gaurav Nanda, Damon Lercel (Purdue). MMR 93.37% recall@5, MRAG 87.20% 의미 유사도. 텍스트+도면 통합 검색. (snippet-verified: arXiv abs + HCI listing + 독립 검색 스니펫 3개 이상 출처)

### 글로벌 — 아키텍처 (적응적 검색)
- [arXiv:2608.13237 — When Should Multi-Round RAG Stop? Structured Stopping Judgments and Retrieval Reduction in Search-R1](https://arxiv.org/abs/2608.13237) — 2026-08-13 · [architecture][adaptive-retrieval][stopping][search-r1][multi-round] · Weimeng Luo. S2G-RAG 충분성-갭 판단을 frozen Search-R1에 적용, Qwen3.5-2B judge 학습(HotpotQA 3,009 상태). 불필요한 검색 라운드 감소. (snippet-verified: arXiv cs.CL/IR listing + 독립 검색 스니펫 2개 이상 출처)

## 2026-08-19 일일 누적 추가 출처 (3건, 루프 #64)

### 한국 — 엔터프라이즈 사내지식
- [rebellions.ai — vLLM Korea Meetup 2026 Wrap-Up](https://rebellions.ai/vllm-korea-meetup-2026-wrap-up/) — 2026-04 · [korea][enterprise][air-gapped][private-llm][access-control][vllm] · 삼성전자 Sungsu Kim 발표: 에어갭 환경 4,000명+ 임직원 대상 사내 LLM + 업무 분리 RAG 에이전트. (snippet-verified: rebellions.ai + vllm.ai/blog + blog.squeezebits.com 3개 이상 독립 출처)

### 글로벌 — 아키텍처 (멀티모달·표)
- [arXiv:2504.09554 — Mixture-of-RAG: Integrating Text and Tables with Large Language Models](https://arxiv.org/abs/2504.09554) — KDD 2026 (2026-08-09~13, 제주) · [architecture][multimodal][table][heterogeneous][kdd2026] · Chi Zhang, Qiyang Chen, Mengqi Zhang. DocRAGLib(2,000개 문서 벤치마크) + MixRAG(top-1 +46%). 이기종 문서 RAG. (snippet-verified: arXiv abs + pdf + html v3 3개 독립 출처)

### 글로벌 — 산업별 (법률)
- [arXiv:2608.14210 — Evaluating Hallucinations in Legal RAG Systems](https://arxiv.org/abs/2608.14210) — 2026-08-14 · [legal][hallucination][evaluation][safety] · 법률 RAG 전용 환각 평가 방법론 4축. 일반 지표로는 법률 환각 ~60% 미검출. (snippet-verified: arXiv abs + arXiv html + WebSearch 스니펫)

## 2026-08-18 일일 누적 추가 출처 (3건, 루프 #63)

### 한국 — 공공·행정
- [디지털데일리 — 네이버클라우드, 행정망 내 AI 기능 확대…'NAVER WORKS AI' 3종 발표](https://www.ddaily.co.kr/page/view/2026081317502210787) — 2026-08-13 · [korea][public][agentic][hybrid-rag][admin-network] · 네이버클라우드 NAVER WORKS AI. Naver AI Tab API 행정망 연동(외부 검색+내부 문서 이중 소스 RAG) + Page(지식관리) + EASY(에이전틱 빌더) + CLOVA Studio for Gov 발표. (snippet-verified: 디지털데일리 + betanews + 이데일리 + 네이트뉴스 4개 이상 독립 출처)
- [ZDNet Korea — NIA, 66억 규모 '범정부 AI 공통기반 고도화' 사업 발주…에이전트·RAG 통합](https://zdnet.co.kr/view/?no=20260810101425) — 2026-08-10 · [korea][public][agentic][mcp][common-rag-platform] · NIA 발주, 예산 66억원, 기간 180일. 챗봇→에이전트, 기관별 분산 RAG→공통 RAG 표준화+MCP 연동, 규정 기반 검토 에이전트, AI 게이트웨이 신설. (snippet-verified: ZDNet Korea)

### 글로벌 — 아키텍처
- [arXiv:2604.11407 — GRIP: Grounding Retrieval Integration with Planning](https://arxiv.org/abs/2604.11407) — ACL 2026 Main (2026.acl-long.196) · [architecture][self-triggering][adaptive-retrieval][control-tokens][acl2026] · Bo Li, Mingda Wang, Gexiang Fang, Shikun Zhang, Wei Ye (WisdomShell). 제어 토큰([RETRIEVE]·[INTERMEDIARY]·[ANSWER]·[SOLVED])으로 검색 트리거를 모델 디코딩에 내재화. 외부 검색 컨트롤러 없는 자기 트리거 정보 계획. 5개 QA 벤치마크에서 Self-RAG·FLARE·IRCoT 초과. GitHub: WisdomShell/GRIP. (snippet-verified: arXiv abs + ACL Anthology 2026.acl-long.196 + GitHub 3개 이상 독립 출처)

## 2026-08-17 일일 누적 추가 출처 (3건, 루프 #62)

- [AWS 기술블로그 — LINE Games의 AI Agent를 통한 게임 퍼블리싱 가속화 여정](https://aws.amazon.com/ko/blogs/tech/linegames-ai-agent-for-accelerating-game-publishing/) — 2026-03-02 · [korea][agentic][enterprise][gametech] · LINE Games(한국, LY Corporation 계열). Amazon Bedrock Knowledge Base + Bedrock Agents 기반 "Nexus AI" 게임 퍼블리싱 지원 플랫폼. Confluence 자동 수집 + 품질 필터링 + 2단계 청킹 + 메타데이터 기반 검색. (snippet-verified)

- [arXiv:2608.13010 — RAGSieve: Self-Referenced Local Contrast for Knowledge-Poison Detection in Retrieval-Augmented Generation](https://arxiv.org/abs/2608.13010) — 2026-08-13 · [architecture][security][poison-detection] · Xinlong Xu, Yoshua Y. Li. RAG 지식 오염(knowledge poisoning) 탐지용 자가 참조 로컬 대비 프레임워크. RSQ(쿼리-로컬 대비) + RSG(코퍼스-로컬 대비). 3 QA 데이터셋 × 6 오염 구성에서 RSQ AUROC 95.2%. (snippet-verified)

- [arXiv:2608.00585 — Verification Without Sufficiency: Per-Chunk Filtering Fails on Multi-Hop RAG, and Decomposition Repairs It](https://arxiv.org/abs/2608.00585) — 2026-08 · [architecture][multi-hop][verification] · Randhir Kumar. 멀티홉 RAG에서 청크별 검증이 실패하는 이유: 청크 하나로 충분한 근거가 될 수 없는 구조. 서브쿼리 분해 기반 검증으로 수리. MuSiQue: 수반성 0.546 → 0.840. (snippet-verified)

## 2026-08-15 일일 누적 추가 출처 (2건, 루프 #60)

- [arXiv:2608.11030 — Self-Knowledge Based Retrieval-Augmented Generation for Patent Matching](https://arxiv.org/abs/2608.11030) — 2026-08-11 · [architecture] [ip] [patent] [ontology] [query-expansion] · Jian Zhang, Songlin Lei, Zhuohao Yang, Bangli Liu, Ziwei Wang, Xufeng Weng, Gehan Amaratunga, Yu Lin, Hongwei Wang (절강대학교 ZJU 컴퓨터학부 + ZJU-UIUC 연구소 × 소흥 K3i Technology Co. Ltd.). LLM이 특허 명세서에서 핵심 기술 엔티티를 자율 추출 → 계층적 온톨로지 구조 생성 → 쿼리 확장·정밀 검색. 도메인 사전학습·명령 튜닝 없이 치명적 망각 없이 IP 전문 검색 가능. 특허 선행기술조사 자동화. (snippet-verified: arXiv abs + arXiv HTML + 2개 이상 독립 WebSearch 스니펫)
- [arXiv:2606.04231 — MM-BizRAG: Enhancing Multimodal Business Document RAG with Document Structure-aware Split](https://arxiv.org/abs/2606.04231) — 2026-06-02 preprint / ACL 2026 Industry Track · [enterprise] [multimodal] [document-structure] [financial] [jpmorgan] · Hanoz Bhathena, Parin Rajesh Jhaveri, Rohan Mittal, Prateek Singh, Aymen Kallala, Rachneet Kaur, Yiqiao Jin, Zhen Zeng, Adwait Ratnaparkhi, Denis Kochedykov (JPMorgan Chase & Co. + Georgia Institute of Technology). 문서 방향별 동적 라우팅(세로형 레이아웃 인식 파싱 / 가로형 페이지 레벨 처리) + LLM 아티팩트 변환 + 추론 시 멀티모달 조립(검색 표현 ≠ 생성 표현 분리). 금융 엔터프라이즈 복잡 문서 멀티모달 RAG. (snippet-verified: arXiv abs + ACL 2026 Industry Track 프로그램 + LinkedIn 3개 이상 독립 출처)

## 2026-08-14 일일 누적 추가 출처 (3건, 루프 #59)

- [아이티데일리 — '에이전틱 AI 프로덕션 전환 해법 모색'…MCP 데브 서밋](https://www.itdaily.kr/news/articleView.html?idxno=241017) — 2026-08-14 · [korea] [conference] [mcp] [agentic] [enterprise] · Linux Foundation + AAIF 공동 주최 MCP Dev Summit Seoul 2026 (오픈소스 서밋 코리아 2026 연계, 2026-08-13~14). 삼성전자·SK텔레콤·LG전자·현대자동차·현대오토에버·SK하이닉스·KT클라우드·네이버클라우드·카카오뱅크·라인플러스·ETRI + 글로벌 기업. MCP 프로토콜 개발·멀티에이전트 설계·엔터프라이즈 시스템 연결·보안·성능 SLO 관리 세션. MCPA 실무 인증 발표. (snippet-verified: itdaily.kr + LF Events + byline.network + venturesquare.net 4개 이상 독립 출처)
- [arXiv:2608.07994 — VDGR-RAG: Vectors, Directories, Graphs, and Reflection Are All You Need for Unified Reasoning over Hierarchical Enterprise Knowledge](https://arxiv.org/abs/2608.07994) — 2026-08-08 · [architecture] [enterprise] [knowledge-graph] [multi-route-retrieval] [reflection] · Wenqi Chen, Haofei Yang, Rui Yang, Fangming Li (Huawei Technologies, 상하이). 엔터프라이즈 계층적 제품 문서 QA 특화 프레임워크. H²KG(Hierarchical Heterogeneous Knowledge Graph) 구축 + 벡터·TOC 에이전틱·엔티티 강화 그래프 3경로 멀티-루트 검색 + 디렉토리 백트래킹 + 리플렉션 도구. 통신 도메인 4개 데이터셋에서 벡터 RAG·GraphRAG 베이스라인 대비 우위. (snippet-verified: arXiv abs + arXiv html + arXiv pdf 3개 독립 출처)
- [arXiv:2608.06223 — TS-RAG: Retrieval Augmented Generation for Time Series Forecasting](https://arxiv.org/abs/2608.06223) — 2026-08-06 · [architecture] [time-series] [forecasting] [retrieval] · Yixiong Xiao, Congxi Xiao, Shuangli Li, Jingbo Zhou (Baidu, Inc.). 시계열 예측에 RAG 참조 검색 적용 — 유사 패턴 검색으로 LLM 시계열 예측 품질 향상. 시간적 분해 표현 + 계층적 이종 코퍼스 인덱스 + 컨텍스트 보강 생성. TS-RAG(arXiv:2503.07649, NeurIPS 2025, UConn DSIS)와 별개의 동명 논문. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)

## 2026-08-13 일일 누적 추가 출처 (3건, 루프 #58)

- [ZDNet Korea — LG CNS, 동아쏘시오그룹 AI 신약개발 플랫폼 구축](https://zdnet.co.kr/view/?no=20260812091506) — 2026-08-12 · [korea] [industry:제약바이오] [graphrag] [enterprise] [agentic] · LG CNS × 동아쏘시오그룹 DAI. AgenticWorks for BIO 기반 신약 연구 데이터(화합물·유전체·논문·특허) 통합 Knowledge Lake + GraphRAG. 질병 분석·후보물질 생성형 AI 설계·가상 검증 전 주기 지원. 약 6개월 구축. (snippet-verified: ZDNet Korea + 한국경제 + 파이낸셜뉴스 + 뉴스와이어 + 뉴스웨이 + 이지경제 + 시사저널e + CBC뉴스 9개 이상 독립 출처)
- [arXiv:2608.00054 — RAG-Tester: Automated End-to-End Testing of Retrieval-Augmented Large Language Models](https://arxiv.org/abs/2608.00054) — 2026-08 · [architecture] [evaluation] [testing] [production] · Ange Maiztegi, Jon Ayerdi, Miren Illarramendi, Aitor Arrieta (Mondragon University, 스페인). RAG 파이프라인의 LLM·임베딩·검색 조합별 실패 행태를 4단계 자동화 테스팅으로 대응. 테스트 케이스 자동 생성 → 다양한 조합 실행 → LLM-as-judge 평가. CI/CD 통합 가능 회귀 탐지 프레임워크. cs.AI + cs.SE. (snippet-verified: arXiv abs + arXiv html + Mondragon University 3개 이상 독립 출처)
- [arXiv:2608.08994 — Guardian Crawler: Retrieval-First Knowledge Discovery with Bounded LLM Augmentation for Noisy Web Intelligence](https://arxiv.org/abs/2608.08994) — 2026-08 · [architecture] [retrieval] [reranking] [security] [noisy-web] · Joshua Castillo, Santosh Nukavarapu, Ravi Mukkamala. KDIR 2026 Short Paper. 노이즈 웹 데이터 대상 BM25 1차 검색 + 리스크-인식·임베딩-증강·하이브리드 4단 리랭킹 스택 + 명시적 인용 기반 제한적 RAG 생성. 검색 우선(retrieval-first) 설계 원칙 통제 실험 실증. (snippet-verified: arXiv abs + arXiv html + cs/pastweek listing 3개 독립 출처)

## 2026-08-12 일일 누적 추가 출처 (3건, 루프 #57)

- [arXiv:2608.07458 — CoinRAG: Contextualized Information Nugget KV Cache Reuse for Long-Context RAG](https://arxiv.org/abs/2608.07458) — 2026-08-07 · [korea] [architecture] [inference-efficiency] [kv-cache] [long-context] · Gyuwan Kim (UC Santa Barbara), Cheoneum Park (한밭대학교 Hanbat National University, 한국), Tao Yang (UC Santa Barbara). 청크 수준 KV 캐시 재사용의 정보 중복·노이즈 한계를 너겟(information nugget) 수준 캐시 분해·재조합으로 해소. 낮은 프리필 레이턴시 제약 하 정확도-효율 파레토 프런티어 최적화. (snippet-verified: arXiv abs + arXiv html + Eye on AI 3개 이상 독립 출처)
- [arXiv:2602.09319 — Benchmarking Knowledge-Extraction Attack and Defense on Retrieval-Augmented Generation](https://arxiv.org/abs/2602.09319) — KDD 2026 (2026-08-09~13, 제주) · [security] [attack] [benchmark] [privacy] [knowledge-extraction] · Zhisheng Qi, Utkarsh Sahu, Li Ma, Haoyu Han, Ryan Rossi, Franck Dernoncourt 외. RAG 지식 추출 공격·방어 최초 체계적 벤치마크. 다양한 공격·방어 전략, 검색 임베딩 모델, 오픈/클로즈드 소스 생성기를 표준화된 프로토콜로 다국어·복수 데이터셋 평가. IP 도용·프라이버시 유출 위험 정량화. (snippet-verified: arXiv abs + arXiv html v3 + Huggingface Papers + liner.com 4개 이상 독립 출처)
- [arXiv:2608.02195 — MEGRAG: Multi-Granular Evidence Graphs for Answer-Aware Multi-Hop RAG](https://arxiv.org/abs/2608.02195) — 2026-08-03 · [architecture] [multi-hop] [evidence-graph] [retrieval] · Weidong Bao, Yingying Sun, Jun Yang, Yilin Wang, Zili Wei, Yubin Bao, Fangling Leng, Minghe Yu, Tiancheng Zhang, Ge Yu. 멀티홉 QA RAG에서 단일 세분도 증거 문제와 오류 누적을 교차 세분도 인덱스(패시지→문장→트리플)와 답변 인식 동적 증거 선택으로 해소. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)

## 2026-08-11 일일 누적 추가 출처 (2건, 루프 #56)

- [arXiv:2608.07933 — EvoTrustRAG: Evolution-Aware Conflict Attribution and Evidence Handling for Reliable Retrieval-Augmented Generation](https://arxiv.org/abs/2608.07933) — 2026-08-08 · [architecture] [conflict-resolution] [reliability] [trust] · Xi Nie, Hongwei Li, Shenghao Wu, Wenshu Fan, Qiyang Song, Wenbo Jiang. RAG 충돌을 진화·조작·불확실성으로 기원 분류하는 새 서브태스크 정의. 충돌 증거 그래프 + 가설 점수화로 훈련 불필요. 귀인 매크로-F1 72.2%→79.1%, 조율 공격 오류 31.2%→16%. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)
- [arXiv:2608.08237 — SAGE: SLO-Aware Adaptive Retrieval for Production RAG Systems](https://arxiv.org/abs/2608.08237) — 2026-08-08 · [production] [latency] [slo] [adaptive-retrieval] [cost] · Muhammad Faizan Raza, Shuo (Luna) Yang, Satish Mahadevan Srinivasan (IEEE CoDIT 2026, 바리, 이탈리아, pp. 169-175). 고정 k 대신 쿼리별 SLO 인식 동적 k 선택. 모방 학습 기반 경량 정책. P95 5초 SLO 준수율 95%(vs. 정적 30%), P95 지연 -36%, 검색 비용 -51%. (snippet-verified: arXiv abs + arXiv html + Scribd 3개 이상 독립 출처)

## 2026-08-10 일일 누적 추가 출처 (3건, 루프 #55)

- [arXiv:2608.02011 — Before Reasoning Fails: Pre-Evidence Procedural Failures in Agentic RAG](https://arxiv.org/abs/2608.02011) — 2026-08-03 · [korea] [agentic] [evaluation] [failure-mode] · Daeyoung Roh (Independent Researcher), Donghee Han (KAIST, 한국). 에이전틱 RAG 실패를 "사전-증거 규율 실패"와 "사후-골드-읽기 실패"로 분해. 12,000 paired trajectory 분석. Read-Gate 경량 런타임 정책으로 LLM-Acc +14.9~19.9 포인트. (snippet-verified: arXiv abs + arXiv html + AI 분석 블로그 3개 이상 독립 출처)
- [arXiv:2608.02009 — HALT: Verification-Aware Stopping for Retrieval-Augmented Search Agents](https://arxiv.org/abs/2608.02009) — 2026-08-03 · [korea] [agentic] [efficiency] [stopping-criterion] · Daeyoung Roh (Independent Researcher), Donghee Han (KAIST, 한국). RAG 검색 중단 기준을 생성기 신뢰도에서 증거 커버리지로 전환. 3개 멀티홉 QA 벤치마크에서 중복 검색 감소 + EM 보존. Before Reasoning Fails(2608.02011)의 동반 논문. (snippet-verified: arXiv abs + arXiv html 2개 이상 독립 출처)
- [arXiv:2608.06672 — TA-RAG: Tone Awareness as a Design Imperative for Retrieval-Augmented Generation](https://arxiv.org/abs/2608.06672) — 2026-08-07 · [architecture] [design] [tone] [user-experience] · Yong-Bin Kang, Anthony McCosker (Swinburne University of Technology, 호주). 검색 문서의 커뮤니케이션 스타일이 RAG 출력 어조를 지배해 사용자 톤 지시를 무력화하는 "컨텍스트 분리(contextual decoupling)" 현상 규명. 톤-인식 검색 레이어 설계 원칙 제안. (snippet-verified: arXiv abs + arXiv html 2개 이상 독립 출처)

## 2026-08-09 일일 누적 추가 출처 (3건, 루프 #54)

- [VentureSquare — BHSN-법무법인 율촌, 리걸 AI '아이율(AI:Yul)' 본격 가동](https://www.venturesquare.net/1032198) — 2026-01-12 · [korea] [industry:법률] [closed-rag] [enterprise] · BHSN(법률 특화 AI 스타트업) × 법무법인 율촌(Yulchon LLC). 법률 특화 멀티 LLM 플랫폼 '앨리비 아스트로(Allibee Astro)' 기반 폐쇄형 RAG 아키텍처. 외부로 데이터 전송 없이 독립된 내부 망 환경에서 AI 작동. 국내 대형 로펌 최초 폐쇄형 RAG 도입 사례. (snippet-verified: VentureSquare + 전자신문 + hellot + aitimes + bhsn.ai 보도자료 5개 이상 독립 출처)
- [ACM DL — WARP: A Word-Level Backdoor Attack Targeting RAG Systems via Retrieval Corpus Poisoning](https://dl.acm.org/doi/10.1145/3770854.3780227) — KDD 2026 (2026-08-09~13, 제주) · [security] [poisoning] [adversarial] [backdoor] · Hui Liu, Yibo Zhou, Liguo Dong, Weidong Li, Shui Yu (Central China Normal University). 단어 수준 트리거를 임베딩 공간에 유사하도록 설계한 적대적 텍스트로 RAG 코퍼스를 오염시키는 최초의 단어 수준 백도어 공격 프레임워크. Pages 867-878. (snippet-verified: ACM DL DOI + RAG backdoor 연구 포털 2개 이상 독립 출처)
- [ACL Anthology — LLM-Generated Text May Harm Your Retrieval! A Robust Detection Strategy for RAG](https://aclanthology.org/2026.acl-long.1475/) — ACL 2026 Long Paper (2026-07-02~07, San Diego) · [architecture] [retrieval-robustness] [hallucination-detection] [detection] · Zhaoheng Huang, Yutao Zhu, Ji-Rong Wen, Zhicheng Dou (Renmin University of China / Gaoling School of AI). LLM 텍스트 탐지기를 RAG 검색 단계에 통합해 AI 생성 텍스트 필터링. RAD(Retrieval-Aware Detection) 데이터 증강 전략. 4가지 LLM 텍스트 생성 패러다임별 영향 분석. (snippet-verified: ACL Anthology abs + ACL 2026 accepted papers 목록 + PDF 링크 3개 독립 출처)

## 2026-08-08 일일 누적 추가 출처 (3건, 루프 #53)

- [카카오 기술 블로그 — 더 작고 강해진 Kanana SLM 개발](https://tech.kakao.com/posts/826) — 2026-07-28 · [korea][architecture][embedding] · 카카오 Kanana LLM 조직. Kanana-2 SLM (1.3B/3B) 4종 Apache-2.0 오픈소스 공개. RAG-Gen Grounding 32.63→57.38, 한국어 토크나이저 30% 효율 개선, coding/math/FC 1.5× 향상. 온디바이스 한국어·영어 경량 SLM의 RAG 그라운딩 개선 레퍼런스 사례. (snippet-verified: 6개 이상 독립 출처)
- [arXiv:2608.04366 — SecureCollaRAG: Combating Knowledge Corruption in Agent Systems: A Byzantine-Tolerant Secure Collaborative RAG Framework](https://arxiv.org/abs/2608.04366) — 2026-08-05 · [architecture][agentic][security][multi-agent][graph] · ACM Web Conference 2026 (DOI: 10.1145/3774904.3792200). 멀티에이전트 RAG 지식 부패 공격 방어. Distributed Knowledge Graph Construction + GNN-based Credibility Scoring(그래프 위상 기반 Byzantine 에이전트 탐지) + Verification-based Aggregation(신뢰도 가중 집계). (snippet-verified: arXiv abs + arXiv html + ACM DL DOI 3개 독립 출처)
- [arXiv:2608.00033 — SIRIN: A Unified Toolkit for Detecting Contextual Hallucinations in Retrieval-Augmented and Memory-Grounded LLM Systems](https://arxiv.org/abs/2608.00033) — 2026-08 · [architecture][hallucination-detection][evaluation][toolkit] · Julia Belikova, Rauf Parchiev, Mikhail Filimonov, Konstantin Polev, Andrey Savchenko, Maksim Makarenko. 3가지 탐지 패러다임 통합(representation probing · uncertainty estimation · judge-style verification) + 웹 UI + pre-generation query answerability 모듈 + span-level 검사. white-box/black-box 모두 지원. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)

## 2026-08-07 일일 누적 추가 출처 (3건, 루프 #52)

- [arXiv:2608.06292 — NeSy-RAG: Neuro-Symbolic Retrieval-Augmented Generation](https://arxiv.org/abs/2608.06292) — 2026-08-06 · [architecture] [explainability] [symbolic-reasoning] [qa] · Jonas Gann, Michael Gertz (Heidelberg University, Data and Web Science Group). Prolog 모듈 기반 신경-기호 통합 RAG. 검색 패시지에서 1차 논리 사실 추출 → Prolog 적재 → 규칙 기반 추론. 대화형 QA ShARC: 61.1% vs. 표준 RAG 42.8%. 감사 추적·설명 책임이 필요한 금융·의료·법률 도메인 적용 가능. (snippet-verified: arXiv abs + arXiv html + Heidelberg DS Group + ResearchGate 4개 독립 출처)
- [arXiv:2608.01311 — RH-RAG: A Multi-Agent RAG Framework for Privacy-Constrained Long-Form Generation from Confidential Reports](https://arxiv.org/abs/2608.01311) — 2026-08-02 · [architecture] [agentic] [privacy] [long-form] [multi-agent] · Raj Shekhar Singh (IIT Roorkee). Planner-Writer-Checker 3-에이전트 프레임워크. NLI 기반 Checker가 각 클레임을 소스로 검증해 PII 누출·사실 오류 동시 완화. 기밀 내부 문서(의료·법률·금융) 대상 장문 생성 워크플로우. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)
- [JMIR Formative Research 2026;10:e72604 — Evaluation of Retrieval-Augmented Generation for Korean Medical Question Answering](https://formative.jmir.org/2026/1/e72604) — 2026-04-30 · [korea] [industry:의료] [evaluation] [metadata-filtering] · 10.4 GB 한국어 의료 코퍼스(487,277개 청크), 5개 LLM 비교 평가. 문서 유형 메타데이터 필터링이 한국 의료 RAG 성능 결정적 요인. 단순 의미 유사도 검색만으로는 한국어 의료 용어 다형성 처리 불충분. (snippet-verified: 2개 독립 WebSearch 출처)

## 2026-08-06 일일 누적 추가 출처 (3건, 루프 #51)

- [arXiv:2608.01389 — KoVRE: Training an Efficient Embedding Model for Korean Visual Document Retrieval](https://arxiv.org/abs/2608.01389) — 2026-08 · [korea] [architecture] [embedding] [visual-document] [multimodal] · Yongbin Choi (경희대학교 Kyung Hee University), Gyuho Shim, Youngjoon Jang (고려대학교 Korea University). 708,729개 한국어·영어 쿼리-페이지 쌍으로 한국어 시각 문서(PDF·슬라이드·표) 전용 단일 벡터 검색기 임베딩 모델 학습. 긍정 인식 하드 네거티브 마이닝 + 리랭커 기반 지식 증류 통제 실험으로 최적 학습 레시피 도출. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)
- [arXiv:2608.00765 — RAGOCR: Optical Compression of Retrieval-Augmented Text via Visual Representation](https://arxiv.org/abs/2608.00765) — 2026-08-01 · [architecture] [context-compression] [multimodal] [visual] · Jiayang Yu, Jialun Zhong, Lei Zou (北京大学 Wangxuan Institute of Computer Technology). 검색 문서를 이미지로 렌더링 후 쿼리-인식 동적 해상도(query-aware dynamic resolution) 메커니즘으로 압축. 나이브 RAG 대비 정확도 +15% 이상, 입력 토큰 1/8 수준으로 절감. 하드/소프트 압축 트레이드오프를 동시에 해소하는 시각 표현 기반 컨텍스트 압축 새 패러다임. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)
- [arXiv:2608.03860 — SciRet: A Compute-Aware Empirical Study of Retrieval and Reranking for Scientific RAG](https://arxiv.org/abs/2608.03860) — 2026-08-04 · [architecture] [retrieval] [reranking] [evaluation] [scientific] · Kaysarul Anas Apurba (Laurentian University, 캐나다) + 공동 연구진 (North South University). CORD-19 코퍼스 3개 규모(1K·5K·15K 논문) 통제 실험. BM25+BGE-M3+RRF 하이브리드 검색 전 규모 Recall@10=1.000. MS MARCO 학습 교차 인코더 리랭커가 과학 코퍼스에서 정밀도 낮춤(도메인 불일치 역효과 실증). 코퍼스 규모 증가 시 RAGAS 충실도 향상. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)

## 2026-08-05 일일 누적 추가 출처 (3건, 루프 #50)

- [KDD 2026 Korea Day](https://kdd2026.kdd.org/korea-day/) — 2026-08-11 (제주 ICC) · [korea] [enterprise] [agentic] [knowledge-platform] · 삼성SDS(Samsung DS) AI 플랫폼 사업부. 그룹 전체 400개 이상 이기종 시스템(ERP·HR·업무 포털 등), 50,000+ 테이블, 500만+ 비정형 문서를 통합해 1,000개 이상의 AI 에이전트·LLM 챗봇 운영. 보안 RAG 파이프라인 + 문서 접근 제어 + 셀프서비스 AI 플랫폼. KDD 2026 Korea Day 특별 플레너리 세션(Google Jeff Dean 기조연설 다음 슬롯). (snippet-verified: kdd2026.kdd.org/korea-day/ + beri.net/events/kdd-2026 + samsungsds.com 3개 이상 독립 출처)
- [arXiv:2608.01565 — DocNavRAG: Document-Structured Graph RAG with Stateful Evidence Construction for Complex Document Question Answering](https://arxiv.org/abs/2608.01565) — 2026-08-03 · [architecture] [graphrag] [agentic] [long-document] · 武汉大学(Wuhan University) + HKUST + CUHK + ETH Zurich 공동 연구. 문서 계층 구조와 문서 간 교차 영역 관계를 탐색 가능한 그래프(navigable graph)로 조직. 4가지 그래프 연산(locate·navigate·expand·fetch) + 상태 기반 증거(stateful evidence). 4개 벤치마크에서 답변 품질 +7.8%, 컨텍스트 충분성 +17.7%. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)
- [arXiv:2608.02678 — DenialRAG: Single-Document RAG Poisoning via Embedded Parametric Denial](https://arxiv.org/abs/2608.02678) — 2026-08-02 · [security] [poisoning] [adversarial] · Abay Zhurekbay, Tao Liu, Fan Li. ACSAC 2026 제출. 올바른 답을 명시적으로 언급 후 부정(denial)하고 공격자 제어 오답 제시하는 단일 문서 중독 공격. 3가지 QA 데이터셋 × 8개 LLM × 5개 방어 기법 체계적 벤치마크. Mistral-7B 전 데이터셋에서 기존 단일 문서 포이즈닝 공격 대비 최고 ASR. (snippet-verified: arXiv abs + arXiv html + redteams.ai 3개 독립 출처)

## 2026-08-04 일일 누적 추가 출처 (3건, 루프 #49)

- [ZDNet Korea — 와이즈넛 'WISE Agent Labs', 최상위 GS인증 1등급 획득](https://zdnet.co.kr/view/?no=20260803172254) — 2026-08-03 · [korea] [agentic] [mcp] [no-code] [gs-certification] · 와이즈넛. 노코드 AI 에이전트 빌더 WISE Agent Labs로 KTL GS 1등급 인증 취득. 코딩 없이 드래그 앤 드롭으로 AI 에이전트 구성. Multi-LLM + RAG 내장 + MCP 연동 + 전 생애주기 통합. 공공기관 우선 구매 요건 충족. (snippet-verified: ZDNet Korea + VentureSquare + 뉴스웍스 3개 이상 독립 출처)
- [arXiv:2608.01630 — RING: Retrieval-Internalized Generation via Mixture-of-Memory Experts](https://arxiv.org/abs/2608.01630) — 2026-08-03 · [architecture] [internalization] [mixture-of-experts] [rl] · CAS Institute of Computing Technology + Xiaohongshu Inc. (State Key Laboratory of AI Safety). 외부 검색기 완전 제거, 대규모 지식을 MoME에 내재화. 3단계 학습: Dual Causal Attention 지속 사전학습 → SFT → 계층적 보상 RL. 서빙 지연·엔지니어링 오버헤드 제거 목표. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)
- [arXiv:2608.01269 — ACE-GraphRAG: Agentic Context Engineering for Hierarchical GraphRAG](https://arxiv.org/abs/2608.01269) — 2026-08-02 · [architecture] [graphrag] [context-engineering] [inference-time] · Yongfeng Huang, Yuren Lai, Ruiying Chen, Haoyu Huang, Mingming Zhao, James Cheng (CUHK · 武汉理工 · HKUST · Huawei Noah's Ark Lab). 계층형 GraphRAG의 표현-추론 간극(representation-inference gap)을 정의. gap-aware refinement + 검색 브랜치 + 태스크 조건부 적응 정책 레이어. HotpotQA·2WikiMultiHopQA·UltraDomain에서 Full-ACE가 RAG·GraphRAG 베이스라인 전체 초과. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)

## 2026-08-03 일일 누적 추가 출처 (3건, 루프 #48)

- [arXiv:2607.00422 — KidnapRAG: Black-box Adversarial Attacks on Agentic RAG](https://arxiv.org/abs/2607.00422) — 2026-07 · [korea] [agentic] [security] [adversarial] · Chanwoo Choi, Euntae Kim, Kyuho Lee, Youngsam Chun, Jinhee Jeong, Eunmi Kim, Myunggyo Oh, Junseo Jang, Buru Chang (고려대학교 Language & Intelligence Lab). 블랙박스 위협 모델 기반 에이전틱 RAG 공격. 공개 소스에 독소 문서 게시만으로 다단계 추론 체인 전체를 납치해 공격자 의도 답변 유도. 단일 검색 단계 포이즈닝과 달리 추론 체인 제어가 핵심. (snippet-verified: arXiv abs + arXiv 목록 + security 연구 저장소 3개 이상 독립 출처)
- [arXiv:2603.05207 — Core-based Hierarchies for Efficient GraphRAG](https://arxiv.org/abs/2603.05207) — 2026-03 제출·2026-06 개정·KDD 2026 채택 · [architecture] [graph] [graphrag] [evaluation] · Jakir Hossain, Ahmet Erdem Sarıyüce (University at Buffalo). Leiden 모듈성 최적화의 비결정성을 이론 증명하고 k-코어 분해로 대체. 선형 시간 결정론적·밀도 인식 계층 생성 + 토큰 예산 인식 샘플링. 3개 데이터셋·3개 생성기·5개 판별기에서 포괄성·다양성 향상 + 토큰 감소 동시 달성. KDD 2026 (2026-08-09~13, 제주). GitHub: jakir-sust/Kcore-GraphRAG. (snippet-verified: arXiv abs + arXiv html + ResearchGate + alphaXiv + KDD 2026 목록 5개 이상 독립 출처)
- [arXiv:2607.24748 — VLD-RAG: An Agentic Vision-Language Long-Document RAG Framework](https://arxiv.org/abs/2607.24748) — 2026-07 · [architecture] [multimodal] [agentic] [long-document] · Seonok Kim (Mazelone). 시각적으로 풍부한 장문서(보고서·슬라이드·매뉴얼) 대상 에이전틱 멀티모달 RAG. 페이지 보존 멀티모달 인덱스(파싱 텍스트 + 페이지 메타데이터 + 밀집 시각 표현) + 하이브리드 검색 + 반복적 멀티모달 질의로 다중 페이지 증거 검색 실현. (snippet-verified: arXiv html 목록 + cs.IR Information Retrieval 목록 2개 독립 출처)

## 2026-08-02 일일 누적 추가 출처 (3건, 루프 #47)

- [삼성SDS 보도자료: 우리은행 AI 에이전트 뱅킹 구축](https://www.samsungsds.com/kr/news/wr-260407.html) — 2026-04-07 · [korea] [industry:금융] [agentic] [architecture] · 우리은행 × 삼성SDS. 삼성SDS 패브릭스(FabriX) 플랫폼 기반 175개 AI 에이전트 구축. 5대 영역(기업여신·자산관리·내부통제·고객상담·업무자동화). RAG 기반 답변체계 + 가드레일 + 베테랑 직원 노하우 비정형 데이터 자산화. 2026년 12월 90개 선공개 → 2027년 8월 175개 완료. 업무 처리 속도 ~30% 향상 전망. "국내 금융권 최초 대규모 AI 에이전트 적용". (snippet-verified: samsungsds.com + ZDNet Korea + 전자신문 + 파이낸셜뉴스 + 데이터넷 + 매일일보 + 디일렉 7개 독립 출처)
- [arXiv:2607.25297 — MTGuard: Towards Safe Tool Use for MCP-Based LLM Agents via Lifecycle-Aware Static-Dynamic Co-Analysis](https://arxiv.org/abs/2607.25297) — 2026-07-28 · [agentic] [security] [mcp] [tool-use] · Ping He, Yuexiang Xie, Yaliang Li, Shouling Ji. MCP 기반 LLM 에이전트 도구 사용의 안전 위협 완화. 라이프사이클 인식 정적-동적 공동 분석(lifecycle-aware static-dynamic co-analysis). 다양한 유해 도구 사용 카테고리 완화·양성 작업 성능 유지. (snippet-verified: arXiv abs 2607.25297v1 + arXiv html 2607.25297v1 2개 독립 출처)
- [arXiv:2607.04223 — GASP: Grounding-Aware Sensitivity Probing for RAG Hallucination Detection](https://arxiv.org/abs/2607.04223) — 2026-07-05 · [architecture] [hallucination] [evaluation] · (저자 정보 snippet 미확인). 지지 구절 제거 시 로그-우도 하락 + Jensen-Shannon Divergence로 스팬 레벨 환각 탐지. RAGTruth response-level AUC ~0.73·span-level AUC ~0.67. TofuEval 전이 가능. RAGBench 단답형 QA에서 한계. 3개 벤치마크, 3개 스코어러, 신뢰구간·유의성 검정·소거 연구 포함. 23페이지, 9그림, 15표. (snippet-verified: arXiv abs + arXiv html + arXiv pdf 3개 독립 출처)

## 2026-08-01 일일 누적 추가 출처 (3건, 루프 #46)

- [arXiv:2607.27523 — Hierarchical Reranking for Scalable Financial RAG](https://arxiv.org/abs/2607.27523) — 2026-07-29 · [korea] [industry:금융] [retrieval] [reranking] · Joohyun Lee (금융보안원 Financial Security Institute), Sungwoo Hong (한양대 Hanyang University). 계층적 리랭킹 기반 확장형 금융 RAG. Pre-Retrieval Optimization + Hierarchical Reranker Architecture + Long-Context Management 3대 혁신. NDCG@20=0.7918(FinQA·FinanceBench·ConvFinQA), ACM-ICAIF '24 FinanceRAG Challenge 2위. FinLLM @ IJCAI-ECAI 2026 채택. (snippet-verified: arXiv abs + arXiv html + 독립 검색 스니펫 3개 이상 출처)
- [arXiv:2607.24010 — Budget-Aware Evaluation of Active Retrieval in RAG](https://arxiv.org/abs/2607.24010) — 2026-07 · [evaluation] [retrieval] [active-rag] · Pin Qian, Su Wang, Chong Peng, Junxian You, Lifei Liu, Haoran Yu, Yihang Chen, Xiaochong Jiang (8명). 능동 RAG 평가의 운영 지점 미지정 문제를 효용 추정(marginal correctness change over 비검색 베이스라인)으로 재정의. 예산 제약 하 검색 결정을 비교 가능한 단위로 측정. KDD 2026 Workshop on Evaluation and Trustworthiness of Agentic AI. (snippet-verified: arXiv abs + arXiv pdf + arXiv html 3개 독립 출처)
- [arXiv:2607.24776 — JKO-RAG: Distributional Retrieval as Wasserstein Free-Energy Gradient Flow](https://arxiv.org/abs/2607.24776) — 2026-07 · [architecture] [retrieval] [reranking] [optimal-transport] · Levi Segal, Murari Ambati. 리랭킹을 자유에너지 F(p)=관련성+엔트로피+중복성 최소화로 재정의. JKO(Jordan–Kinderlehrer–Otto) 근위 도식으로 Wasserstein-2 경사 흐름을 통해 최적 문서 분포 계산. 기저 계량 C_ij=(1−cos⟨z_i,z_j⟩)²이 시맨틱 기하 인코딩. 선형 응답 이론으로 Wasserstein vs KL 차이 해석. cs.IR + cs.LG. (snippet-verified: arXiv abs + arXiv pdf + ResearchGate 3개 독립 출처)

## 2026-07-31 일일 누적 추가 출처 (3건, 루프 #45)

- [ZDNet Korea — 지미션, 도면 특화 '에이전틱 RAG 플랫폼' 개발 나선다](https://zdnet.co.kr/view/?no=20260731151945) — 2026-07-31 · [korea] [industry:제조] [agentic] [architecture] · 지미션(JIMISSION) × NC AI. NC AI 파운데이션 모델 기반 제조·산업 현장 도면 특화 에이전틱 RAG 플랫폼 R&D 착수. 과기정통부 '모두의 챌린지 AX-LLM 협업과제' 수행기관 선정(2026-07-18 협약). 설계도면·기술 문서 이해·검색·분석 특화. (snippet-verified: ZDNet Korea + BetaNews NC AI 에이전틱 AI 국책사업 선정 2개 독립 출처)
- [arXiv:2607.27353 — LayerRAG-Bench: A Cross-Layer Reliability Benchmark for Agentic Retrieval-Augmented Generation](https://arxiv.org/abs/2607.27353) — 2026-07-29 · [agentic] [evaluation] [benchmark] [security] · Musa Shams (Independent Researcher; EY). 에이전틱 RAG의 4개 계층(증거·도구계약·권한·세션상태) 교차 신뢰성 벤치마크. 8개 엔터프라이즈 도메인·240 태스크·9개 장애 시나리오·38,880 레코드·9개 모델. 스키마 정규화는 schema-drift 해소(0.000→0.913)에만 효과적; stale 증거·권한 거부·wrong-session은 미해결. Groundedness-only 평가가 상당한 위양성 생성 실증. (snippet-verified: arXiv abs + arXiv html + LinkedIn Musa Shams 3개 독립 출처)
- [arXiv:2607.28397 — GLM-RAG: Graph Language Models for Graph-Based Retrieval-Augmented Generation](https://arxiv.org/abs/2607.28397) — 2026-07-30 · [architecture] [graph] [knowledge-graph] · Maya Arseven, Anette Frank, Beni Egressy, Johann Higl, Moritz Plenz (Heidelberg Univ. + Aleph Alpha Research). KG 기반 RAG 검색기로 GLM·GNN·벡터 검색 체계적 비교. 파인튜닝된 GLM이 두 멀티홉 벤치마크 SOTA, 도메인 외 일반화에서 우위. 파라미터·서브그래프 커버리지 스케일링 효과 확인. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)

## 2026-07-30 일일 누적 추가 출처 (3건, 루프 #44)

- [아이피데일리 — 특허청, 예산 없이 AI 에이전트 3종 자체 구축](https://www.ipdaily.co.kr/news/articleView.html?idxno=49591) — 2026-07-25 · [korea] [industry:공공] [agentic] [architecture] · 특허청 IP-AX 추진단. 별도 예산·전문 개발 인력 없이 3종 AI 에이전트 자체 구축: 지식위키(정책 회의 문서 → LLM Wiki + RAG 검색), AI 보관소(해외 IP기관 보도자료 자동 수집·분류·분석), AI 에이전트(입법예고·발의법안 모니터링+담당부서 선정+법안검토). (snippet-verified: 아이피데일리 + 헤럴드경제 + 골든타임즈 + GNN뉴스 + 한국경찰뉴스 5개 독립 출처)
- [arXiv:2607.26497 — Which RAG Paradigm Wins at Scale?](https://arxiv.org/abs/2607.26497) — 2026-07-29 · [evaluation] [architecture] [benchmark] · Pengyu Wang, Benfeng Xu, Shaohan Wang, Xin Zeng, Huarui Wu, Lei Zhang, Licheng Zhang. EnterpriseRAG-Bench(511,959 문서, 500 질문, 28 중첩 티어)로 RAG 패러다임 스케일 의존성 분석. BM25가 모든 티어에서 저비용 Pareto 프런티어 하단 정의 + 중규모 이상 정확도 선도. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)
- [arXiv:2607.26470 — CMT-RAG: Complementary Memory Traces for Multi-turn Multi-hop RAG](https://arxiv.org/abs/2607.26470) — 2026-07-29 · [agentic] [architecture] [multi-turn] · Lang Zhou, Yingjian Chen, Shuxuan Li, Kun-Yu Lin, Zhilin Zhao. 멀티턴 대화 RAG에서 원시 대화 이력 대신 서브 질문 수준 추론 추적(CMT)으로 대화 컨텍스트 표현. MuMu-QA 벤치마크(교차-턴 서브 질문 의존성 주석 포함) 신규 구축. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)

## 2026-07-29 일일 누적 추가 출처 (3건, 루프 #43)

- [arXiv:2607.24165 — Do Current Retrievers Cover All the Evidence? A Controlled Study of Conjunctive Cross-Page Retrieval](https://arxiv.org/abs/2607.24165) — 2026-07 · [korea] [evaluation] [retrieval] · Sungguk Cha, DongWook Kim, Mintae Kim, Youngsub Han, Byoung-Ki Jeon, Sangyeob Lee (LG Uplus, 한국). 현행 RAG 검색기의 접합적 교차 페이지 커버리지 통제 실험. 단일 페이지 vs 다중 페이지 증거 요구 조건 분리. "관련성" 외 "접합적 커버리지"를 독립 평가 차원으로 제안. (snippet-verified: arXiv + ZoomInfo Sungguk Cha @ LG Uplus + sciprofiles 3개 독립 출처)
- [Anthropic — Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude) — 2026-07-28 · [architecture] [agentic] [mcp] [enterprise] · Anthropic. MCP 신규 스펙: Stateless Core(서버리스·엣지 배포), OAuth 2.0/OIDC(Entra·Okta 통합), Versioned Extensions(Apps·Tasks). MCP SDK 월 4억 다운로드(전년 4× 성장). 엔터프라이즈 RAG 사내 지식 베이스의 MCP tool 노출 패턴 표준화. (snippet-verified: Anthropic 공식 블로그 + ClaudeDevs X 공식 계정 + explainx.ai + stacktr.ee + bovo-digital.tech + vindler.solutions 6개 독립 출처)
- [arXiv:2607.18796 — TSGR: Taobao Search Generative Retrieval](https://arxiv.org/abs/2607.18796) — 2026-07-21 · [industry:커머스] [architecture] [generative-retrieval] · Tianyu Zhan, Gui Ling, Tong Xiong 등 (Alibaba/Taobao 검색팀). VRM(Value-aware Ranking Module)으로 비즈니스 가치를 SID 구성+랭킹 단계 양쪽에 내장. 단일 모델이 검색기+사전 랭커 동시 수행. 오프라인 +9.16% HR@1000; 온라인 +0.43% IPV, +1.12% TC, +1.64% GMV 프로덕션 A/B 결과. (snippet-verified: arXiv abs + arXiv html + X/@_reachsumit + Springer link 4개 독립 출처)

## 2026-07-28 일일 누적 추가 출처 (3건, 루프 #42)

- [arXiv:2607.21936 — Leveraging External Knowledge for Historical Document Restoration via Retrieval-Augmented Large Language Models](https://arxiv.org/abs/2607.21936) — 2026-07-24 · [korea] [architecture] [humanities] [nlp] · Gabeen Kim, Kyeongpil Kang (강원대학교 Kangwon National University). 한국 역사 고문서 복원에 RAG 적용. ARI 프레임워크로 LLM 내재 지식 + 외부 검색 지식 결합. 일반 문자·고유명사 복원 모두 베이스라인 대비 유의미한 향상. ACL 2026 Findings 채택. (snippet-verified: arXiv abs + arXiv html + Google Scholar/ResearchGate profile(Kyeongpil Kang) 3개 독립 출처)
- [arXiv:2607.23006 — VecTree-RAG: An Agentic Retrieval-Augmented Generation Framework Combining Vector and Tree Retrieval for Efficiency and Accuracy](https://arxiv.org/abs/2607.23006) — 2026-07-25 · [architecture] [agentic] [scientific-computing] · Xinyan Zhong, Yuwei Shi, Yuqi Wei, Chen Shen, Tianhang Zhou, Zhenghao Wu (XJTLU · Suzhou Lab · China Univ. of Petroleum). 과학 문헌 QA를 위한 벡터+트리 이중 검색 에이전틱 RAG. 코퍼스 수준 벡터 랭킹 + 섹션 트리 추론 순회. QASPER 0.800 · LitQA2 0.925 · MOSAIC 0.547. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)
- [arXiv:2607.20506 — Optimizing Hypergraph-Based RAG: Toward Better Fact Extraction and Chunk Retrieval](https://arxiv.org/abs/2607.20506) — 2026-07 · [architecture] [graph] · Houda Khrouf, Pedro Fillastre, Sebastiao Correia. 하이퍼그래프 RAG의 추출(EXT++ 자기일관성 프롬프팅) + 검색(Personalized PageRank 구조적 연결성) 최적화. 소스 코드·평가 데이터 공개. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)

## 2026-07-27 일일 누적 추가 출처 (3건, 루프 #41)

- [edaily — 올거나이즈, 한국증권금융 '생성형 AI 활용 플랫폼 구축' 수주](https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=03457126645514848) — 2026-07-15 · [korea] [industry:금융] [architecture] [privacy] · 올거나이즈(Allganize). 한국증권금융 전사 임직원 대상 생성형 AI 플랫폼 + 업무별 AI 비서. FDSE 방법론. 온프레미스(외부 전송 금지). DRM·SSO·개인정보 비식별화·내부망 연동. AI 기본법·금감원 RMF·금융보안원 AI 보안 안내서 반영. (snippet-verified: edaily + zdnet + venturesquare + newstheai + ezyeconomy + digitalchosun 6개 이상 독립 출처)
- [arXiv:2607.10463 — GRASP: GRanularity-Aware Search Policy for Agentic RAG](https://arxiv.org/abs/2607.10463) — 2026-07-11 · [agentic] [architecture] [reinforcement-learning] · Varun Gandhi, Jaewook Lee, Shantanu Todmal, Franck Dernoncourt, Ryan Rossi, Zichao Wang, Andrew Lan (UMass Amherst + Adobe Research). 에이전트 RAG 검색 세분성 RL 최적화. semantic search·keyword search·paragraph reading 3가지 액션. 결합 보상(답변 정확도+근거 읽기+보완적 검색+턴 효율). 멀티홉 QA 벤치마크 우위. (snippet-verified: arXiv abs + arXiv html + HuggingFace papers + ResearchGate + X post 5개 독립 출처)
- [arXiv:2607.08028 — From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents](https://arxiv.org/abs/2607.08028) — 2026-07-09 · [architecture] [enterprise] [governance] [security] · Joongho Ahn, Moonsoo Kim (AI Leadership Research Center). 엔터프라이즈 LLM 앱을 추적·감사 가능 아키텍처로 재구성. RAG = 소스-근거 클레임 레이어. 5가지 계약(소스 근거·엔티티 라우팅·추적·출력 위생·권고 언어). 한국 5개 대기업 그룹(25개 상장사) 검증. 3개 모델 교체 실험에서 계약 유지. 참조 구현 공개. (snippet-verified: arXiv abs + arXiv html + cs.CL listing + ORCID 4개 독립 출처)

## 2026-07-26 일일 누적 추가 출처 (3건, 루프 #40)

- [Rapportian — 서울아산병원, 국내 의료기관 최초 폐쇄망 기반 프라이빗 AI 도입](https://www.rapportian.com/news/articleView.html?idxno=236096) — 2026-05-18 · [korea] [industry:의료] [architecture] [privacy] · 서울아산병원(Asan Medical Center). 벡터 데이터베이스 + RAG 기반 임상지침·규정 지식 검색 시스템. 온프레미스 100%(외부 클라우드 0%), 완전 폐쇄망. 국내 의료기관 최초 프라이빗 AI 지식 관리. RAG 기반 환각 방지 + 의료 데이터 외부 전송 0. (snippet-verified: rapportian.com + etnews.com + docdocdoc.co.kr + khanews.com + thefirstmedi.co.kr + medicalinfo.co.kr 6개 이상 독립 출처)
- [arXiv:2607.20346 — IteraSim RAG: A Multi-Stage Retrieval-Augmented Agentic Back-End for OpenFOAM-Based Computational Fluid Dynamics](https://arxiv.org/abs/2607.20346) — 2026-07-22 · [architecture] [agentic] [scientific-computing] · Pratyush Kumar. OpenFOAM CFD 비전문가 장벽 해소. LLM 기반 멀티-변형 쿼리 확장(물리·솔버-키워드·트러블슈팅 변형) → RRF → MMR → HNSW 밀집 벡터 검색. 초안 에이전트 + 검토 에이전트 분리. Computer Physics Communications 제출. (snippet-verified: arXiv abs + arXiv html + bohrium.com 3개 독립 출처)
- [arXiv:2604.19899 — A Reproducibility Study of Metacognitive Retrieval-Augmented Generation](https://arxiv.org/abs/2604.19899) — 2026-07-20~24 · [evaluation] [reproducibility] [reranking] · iai-group (SIGIR 2026, DOI: 10.1145/3805712.3808551). MetaRAG 상대적 개선은 재현 가능, 절대 점수는 원논문보다 낮음(LLM 버전 변경 + 구현 세부 사항 부재). PointWise·ListWise 리랭커 + SIM-RAG 비교 확장. GitHub: iai-group/sigir2026-metarag. (snippet-verified: arXiv abs + SIGIR 2026 ACM DOI + GitHub repo 3개 독립 출처)

## 2026-07-25 일일 누적 추가 출처 (3건, 루프 #39)

- [arXiv:2607.19362 — GraphContainer: A Unified Platform for Comparing and Debugging Graph RAG Methods](https://arxiv.org/abs/2607.19362) — 2026-07 · [korea] [architecture] [graph] [tooling] · Seonho An, Chaejeong Hyun, Min-Soo Kim (KAIST). VLDB 2026 Demo 채택. UGR(Unified Graph Representation) 레이어로 이종 그래프 포맷 표준화 + Graph Recorder로 검색 단계별 시각 재현. 이종 Graph RAG 프레임워크 비교·디버깅 최초 통합 플랫폼. (snippet-verified: arXiv abs + arXiv html + VLDB 2026 demonstrations 프로그램 3개 독립 출처)
- [arXiv:2607.19301 — PAGE-RAG: Evidence-Grounded Adaptive Graph Retrieval for Long-Document Question Answering](https://arxiv.org/abs/2607.19301) — 2026-07-21 · [architecture] [graph] [long-doc] · Xingyu Chen, Junxiu An, Jun Guo, Li Wang. 자동 구성 그래프를 독립 지식 소스 대신 의미적 골격(semantic skeleton)으로 취급. 태스크 적응형 검색 라우팅으로 그래프 traversal과 원문 접근을 동적 선택. 장문서 QA 신뢰성 향상. 오픈소스. (snippet-verified: arXiv abs + arXiv html + cs.IR listing 3개 독립 출처)
- [arXiv:2607.21324 — GRADRAG: Cross-Component Prompt Adaptation for Coordinated Multi-Agent RAG](https://arxiv.org/abs/2607.21324) — 2026-07-23 · [agentic] [architecture] · Paolo Pedinotti, Enrico Santus. RAG 파이프라인을 계산 그래프로 모델링, 평가자 피드백을 역방향 전파해 검색기·그래프 구성기·생성기 프롬프트를 조율 업데이트. 조기 종료 신호로 비효율 반복 차단. SQUALITY + QMSUM 벤치마크 평가. (snippet-verified: arXiv abs + arXiv html + cs.CL listing + cs.AI listing 4개 독립 출처)

## 2026-07-24 일일 누적 추가 출처 (3건, 루프 #38)

- [arXiv:2607.17535 — Salience Induction against Multi-Hop RAG Agents: Threat and Defense](https://arxiv.org/abs/2607.17535) — 2026-07-20 · [agentic] [security] · Xingfu Zhou, Pengfei Wang, Yuan Zhou, Wei Xie, Xu Zhou (National University of Defense Technology, China). 멀티홉 RAG 에이전트의 현저성 채널(사실 위치·강조·프레이밍) 공격 — 모든 사실이 참인 상태에서 추론을 오염. 6개 Salience-Editing 연산자 + 반복적 제안자-검증자 파이프라인 + SalientWiki-MH 벤치마크. 30% 편집 예산 내 ASR 83.3%; 최강 방어 후 사후 ASR 75.7%. GPT/Claude/Gemini/DeepSeek/Qwen 5개 프론티어 모델 + ReAct/Reflexion/tool-calling 3가지 아키텍처에서 실험. (snippet-verified: arXiv abs + cs.CR listing 2개 독립 출처)
- [arXiv:2607.20090 — Reinforcement Learning for Large Language Model Selective Evidence Adoption from Contaminated Retrieval Results](https://arxiv.org/abs/2607.20090) — 2026-07-22 · [architecture] [retrieval] [security] · Yanyu Chen, Yue Li, Yongyi Cui, Dongsheng Shi, Lichang Dai. 오염된 RAG 컨텍스트에서 유효 증거와 오해 유발 콘텐츠를 구별하는 선택적 증거 채택 강화학습. SelectBench 통제 벤치마크 + 훈련 세트. Qwen3.5-4B를 DAPO로 포스트 트레이닝(Rule/DeepSeek 보상). strict success 22.46%→25.54%/26.46% 향상. (snippet-verified: arXiv abs + cs.CL listing 2개 독립 출처)
- [arXiv:2607.20437 — TopoGuard: Graph Theory Based Defenses Against Split-Knowledge Attacks on RAG](https://arxiv.org/abs/2607.20437) — 2026-07 · [architecture] [security] · Chahana Dahal, Zuobin Xiong (University of Nevada, Las Vegas). 분할 지식 공격(각각 무해하나 조합 시 허위 관계 형성) 탐지를 위한 검색 문서 의미적 유사도 그래프 위상 분석 방어 프레임워크. 이론적 효과성 증명, 서브밀리초 지연, 적응형 공격자 및 양성 교차 도메인 쿼리 환경에서 강건성 유지. (snippet-verified: arXiv abs + cs.CR listing 2개 독립 출처)

## 2026-07-23 추가 출처

- [서울신문 — 미디어젠, 생성형 AI 검색 정확도 향상 특허 등록…에이전틱 RAG 기술 확보로 AI 에이전트·리걸 AI 사업 확대](https://www.seoul.co.kr/news/economy/2026/07/23/20260723500054) — 2026-07-23 · [korea] [industry:법률] [architecture] [agentic] · 미디어젠 MIRAGE(MediaZen Intelligent Retrieval And Generative Engine) — 자체 sLLM 기반 에이전틱 RAG 엔진. klaw-Contriever 기반 한국어 법규 특화 검색(법령 검색 최대 33% 향상). 공정거래위원회 불공정 약관 심사·하도급 계약 AI 시스템 적용. 도메인 특화 검색 모델 원천 특허 등록. (snippet-verified: 서울신문 + aisakorea.com + dailyinvest.kr + newspim.com KCC 2026 4개 이상 독립 출처)
- [arXiv:2607.16431 — RIMS: Preference Optimization via Smoothed Multi-pair Aggregation for Small-Scale LLM Retrieval-Augmented Generation](https://arxiv.org/abs/2607.16431) — 2026-07-17 · [architecture] [retrieval] [small-model] · Columbia Univ., Rutgers Univ., Purdue Univ., SUNY Albany. SLM의 노이즈 검색 증거 민감성 해소. 3단계: 자체 SLM rejection sampling 합성 데이터 생성 + differentiable soft aggregation(그래디언트 신호 보존) + 멀티 쌍 선호도 최적화. hard argmin/argmax 기반 단일 쌍 선호도 학습의 신호 낭비 문제 극복. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)
- [arXiv:2607.19830 — VizRAG: Enhancing Retrieval-Augmented Generation with Hypergraph Visualization](https://arxiv.org/abs/2607.19830) — 2026-07-22 · [architecture] [graph] [multimodal] · Yanbin Wei, Yang Chen 외 (SUSTech·HKUST·Huawei Research·Beihang Univ.). 하이퍼그래프 기반 RAG의 텍스트 단일 모달 한계 극복. HyperViz 툴킷으로 n원 원자 사실 하이퍼에지를 시각 표현으로 변환해 MLLM 검색·추론에 주입. 시각 과부하·렌더링 편향 해결. 강력한 기준선 대비 유의미한 성능 향상. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)

## 2026-07-22 추가 출처

- [arXiv:2607.16973 — TurboVec: Cost-Efficient Private Retrieval for Enterprise RAG via Codebook-Oblivious Scalar Quantization](https://arxiv.org/abs/2607.16973) — 2026-07-18 · [architecture] [enterprise] [privacy] [vector-index] · TurboQuant 4-bit scalar quantizer(코퍼스 학습 불필요, per-vector min/max 정규화). FAISS PQ 대비 Recall@5 +8.5–8.9pp, 동일 메모리. 멀티테넌트 커널 얼로우리스트 필터링으로 Recall@10 0.86–0.93 유지(post-filter 대비 5–10×). 멤버십 추론 ~50%(랜덤 수준) vs PQ 코드북 57.3%. Rust 오픈소스. (snippet-verified: alphamatch.ai + larsroettig.me + knightli.com + medevel.com + Medium 포함 6개 이상 독립 출처)
- [arXiv:2607.18756 — RAGAL: Frugal, Fully Local RAG for a Romanian Government Agency](https://arxiv.org/abs/2607.18756) — 2026-07-21 · [industry] [public-sector] [architecture] [edge] · 루마니아 농업 지원 기관 AFIR. 제약: 데이터 외부 전송 금지·읽기 전용·단일 8GB 소비자 노트북. 루마니아어 코퍼스 ~25,000 청크(실제 티켓 15,073건 + 규범 문서). 하이브리드 dense-sparse + 의도 라우팅. 평가 62%→81%. bge-m3 파인튜닝으로 recall@10 0.663. (snippet-verified: arxiv.org abs + html 3개 이상 독립 출처)
- [arXiv:2607.18102 — FinSAgent: Corpus-Aligned Multi-Agent RAG for SEC Financial Filings QA](https://arxiv.org/abs/2607.18102) — 2026-07 · [industry] [finance] [agentic] [architecture] · SEC 10-K 공시 QA. 사전 코퍼스 미정렬(prior-corpus misalignment) 문제 해결: 역할-특화 병렬 에이전트(10-K 아이템 구조 앵커) + DB-인식 쿼리 분해(공시 DB 요약 뷰 조건화) + 멀티패스 검색 + 피처-게이팅 리랭킹. (snippet-verified: arxiv.org abs + html 2개 이상 독립 출처)

## 2026-07-21 추가 출처

- [뉴스핌 — 공무원이 만든 'AI 법령 비서' 14일 시범 개시…법령 검토 시간 단축 기대](https://www.newspim.com/news/view/20260713000229) — 2026-07-13 · [korea] [industry:공공] [architecture] · 법제처·행정안전부·과기정통부 합동. RAG 기반 법령·판례 QA 시스템. 대법원 판례 6만 건 + 법령 24만 건 + 자치법규 5만 건. 공무원 직접 개발(약 1개월), 범정부 AI 공통 인프라 활용. 2026-07-14 시범 개시. (snippet-verified: 뉴스핌+ZDNet Korea+아시아투데이+이데일리+다음뉴스+디지털타임스+헬로디디+네이트뉴스 8개 이상 독립 출처)
- [arXiv:2607.16604 — When Do Multimodal and Graph-Augmented RAG Help? A Controlled Evaluation for Document Question Answering](https://arxiv.org/abs/2607.16604) — 2026-07-18 · [architecture] [multimodal] [graph] [evaluation] · Sokipriala Jonah. PubLayNet 1,000페이지 4-way 소거 실험. KG 증강 효과 미검증, 시각 증강은 픽셀 전용 질의에서만 유효, 이미지 토크나이저별 토큰 수 최대 11배 차이. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)
- [arXiv:2607.17538 — D-NOVA: In-Storage Retrieval Accelerator via Dual-Bound 3D NAND-Optimized Similarity Search with Vector Adaptation](https://arxiv.org/abs/2607.17538) — MICRO 2026(아테네) · [architecture] [hardware] [retrieval] · Chang Eun Song 외 UC San Diego. 3D NAND 스토리지 내 IVF 벡터 검색 내재화. CPU 대비 41.7배 속도·71배 에너지 효율, 최신 인스토리지 가속기 대비 12.13배 처리량. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)

## 2026-07-20 추가 출처

- [뉴스웍스 — LG전자, AI로 부품탐색 시간 수일→30분 단축…신규 개발 부품 25% 절감](https://www.newsworks.co.kr/news/articleView.html?idxno=845553) — 2026-07-03 · [industry] [manufacturing] [agentic] [multimodal] [korea] · LG전자. 부품(Part) + 되찾다(Retrieve)를 결합한 파트리버(PartRiever) RAG 에이전트. 자연어 질의로 2D 도면·3D 형상·기술 문서 종합 분석. 부품 탐색 수일→30분, 신규 개발 부품 수 25% 절감. PoC 단계, 연내 전사 확대 예정. (snippet-verified: 뉴스웍스·더퍼블릭·EBN·이데일리·네이트·포인트데일리·시사저널e·소셜밸류 8개 독립 출처)
- [ACM DL — SRAG: Lightweight and Specialized RAG at the Edge](https://dl.acm.org/doi/10.1145/3805712.3809702) — 49th ACM SIGIR 2026, 2026-07-20 · [architecture] [edge] [distributed] · 엣지 서버별 도메인 인식 특화 지식 베이스 유지 + 버퍼 기반 지식 마이그레이션. 단일 범용 지식 베이스의 한계(이질적 쿼리·자원 제약 엣지 환경)를 극복. retrieval relevance·generation quality·storage efficiency 향상, end-to-end 지연 감소. (snippet-verified: SIGIR 2026 RAG Systems 세션 + ACM DOI 2개 독립 출처)
- [arXiv:2606.29328 — GeoRAG: Optimizing Information Demand Coverage in Retrieval-Augmented Generation](https://arxiv.org/abs/2606.29328) — ICTIR'26 @ SIGIR 2026 (2026-07-25, Melbourne) · [architecture] [retrieval] [coverage] [context-selection] · Bingxue Zhang, Jianying Jia (USST), Feida Zhu (SMU). 컨텍스트 선택을 정보 수요 커버리지 최적화로 재정의. 다양성 서브 질의 + 역방향 검증 품질 가중치 + Sinkhorn-Wasserstein 거리 최소화. 6개 오픈도메인 QA 벤치마크 top-k 대비 EM +6.5~+7.5%p. (snippet-verified: arXiv abs + arXiv html + ICTIR'26 proceedings 3개 독립 출처)

## 2026-07-19 추가 출처

- [LG AI Research — LG Showcases EXAONE's Real-World Industry Impact at ICML 2026](https://www.lgresearch.ai/news/view?seq=664) — 2026-07-08 · [industry] [public-sector] [data-generation] [korea] · LG AI Research × 국민연금공단. EXAONE Data Foundry: 생성형 AI + 장문 컨텍스트 처리(최대 32,768 토큰) 기반 도메인 전문 데이터 자동 생성 플랫폼. 국민연금공단 파일럿에서 하루 1만 건+ 전문 데이터 자동 구축, 생산성 1,000배 이상 향상, 데이터 품질 평균 20% 이상 향상(회사 발표 기준). ICML 2026(서울, 2026-07-06~11) 발표. (snippet-verified: Korea Times + Herald경제 + 이투데이 + 서울경제 + Businesskorea + Korea Herald + BigGo Finance 7개 이상 독립 출처)
- [arXiv:2605.28522 — Search for Coverage: Sub-Question Answerability Augmentation for Long-Form RAG](https://arxiv.org/abs/2605.28522) — SIGIR 2026 (DOI: 10.1145/3805712.3809752, 2026-07-20~24 멜버른) · [architecture] [retrieval] [long-form] · Tzu-Wen Yeh 외. 장문형 RAG에서 관련성 최적화 검색기의 커버리지 저하 문제를 원자적 서브 질문 분해 + 응답 가능성 증강으로 직접 해결. 13개 BEIR + 3개 nugget-based 커버리지 벤치마크에서 유의미한 향상. (snippet-verified: arXiv pdf + SIGIR 2026 공식 proceedings DOI + SIGIR accepted papers 목록 3개 이상 독립 출처)
- [ACL Anthology — AED-RAG: Adaptive Ensemble Decoding for Multi-Granular RAG Context Fusion](https://aclanthology.org/2026.findings-acl.1148/) — ACL 2026 Findings · [architecture] [retrieval] [decoding] · Junzhe Zhou, Fulin Lin, Tairan Cheng, Shaowen Chen, Hongwei Wang. 비구조화 패시지·구조화 트리플렛·파라메트릭 메모리를 단일 확률 공간으로 투영, 소프트 토큰 레벨 퓨전으로 정보 이득 동적 최적화. 유용성 예측기(대조 퍼플렉시티) 파인튜닝으로 세분화 불일치 사전 제거. (snippet-verified: ACL Anthology + ACL 2026 Findings 목록 2개 이상 독립 출처)

## 2026-07-18 추가 출처

- [서울경제 — 현대차증권, AI 에이전트 HAI 도입](https://m.sedaily.com/amparticle/20065936) — 2026-07-09 · [industry] [finance] [korea] · 현대차증권. Claude Sonnet 4.5 기반 클라우드 플랫폼 + RAG 파이프라인으로 사내 규정·지침·업무 문서 Q&A + 문서 요약 시스템 HAI 1.0 구축. AX 전략 하에 중소형 증권사 최초 클라우드 AI 에이전트 도입. 연내 HAI 2.0 구축 예정. (snippet-verified: 서울경제 한국어 + en.sedaily.com 영문 + 추가 미디어 3건 이상)
- [AI타임스 — 과기정통부, '모두의 AI' 사업 공모 시작](https://www.aitimes.com/news/articleView.html?idxno=212718) — 2026-07-13 · [industry] [public-sector] [agentic] [korea] · 과학기술정보통신부. 전 국민(5,200만명) 무료·무제한 AI 챗봇 + RAG 기반 공공서비스 신청 대행 에이전트. 국내 독자 AI 모델 50%+ 의무 사용, 정부 B200 GPU 512개 제공. 8월 사업자 선정·9월 베타·12월 정식 출시 예정. (snippet-verified: AI타임스 + ZDNet Korea + 전자신문 + 파이낸셜뉴스 + 추가 미디어 5건 이상 독립 출처)
- [arXiv:2601.01513 — FastV-RAG: Enhancing Video Question Answering RAG with Speculative Decoding](https://arxiv.org/abs/2601.01513) — ACL 2026 Main Conference · [architecture] [multimodal] [video] · Gen Li (UESTC), Peiyu Liu (UIBE). 유사도 기반 필터링으로 개체 인식 오류 완화 + 경량 드래프트 모델→고성능 검증 모델 추측적 디코딩 구조로 약 2배 추론 속도 향상. VideoQA 도메인 RAG 최초 추측적 디코딩 결합 ACL 2026 Main 채택 사례. (snippet-verified: arXiv abs + arXiv html + ACL Anthology + ACL 2026 수락 논문 목록 4개 이상 독립 출처)

## 2026-07-17 추가 출처

- [arXiv:2604.19047 — RARE: Redundancy-Aware Retrieval Evaluation Framework for High-Similarity Corpora](https://arxiv.org/abs/2604.19047) — 2026-07-02 (ACL 2026 Main Conference) · [enterprise] [evaluation] [korea] · Hanjun Cho(Allganize), Jay-Yoon Lee(SNU). 기업 코퍼스(금융·법률)의 고중복 문서 환경에서 RAG 검색 정확도가 77.9%→8.5%(금융)→5.0%(법률)로 급락함을 실증. RARE 프레임워크(원자적 사실 분해 + CRRF)로 엔터프라이즈 특화 평가 설계 제안. (snippet-verified: arXiv abs + arXiv html + platum.kr + venturesquare.net 4개 이상 독립 출처)
- [arXiv:2508.03306 — Reliable Evaluation Protocol for Low-Precision Retrieval](https://arxiv.org/abs/2508.03306) — 2026-07-02 (ACL 2026 Main Conference) · [architecture] [retrieval] [korea] · Kisu Yang, Yoonna Jang, Hwanseok Jang, Kenneth Choi, Isabelle Augenstein, Heuiseok Lim (VAIV Company, Korea University, Univ. of Copenhagen, UC Berkeley). 저정밀 환경의 RAG 검색 동점 문제를 최종 레이어만 FP32 업캐스트(HPS)로 해소. Tie-aware Retrieval Metric(TRM)으로 평가 불확실성 정량화. (snippet-verified: arXiv abs + businesskorea.co.kr + newsprime.co.kr 3개 이상 독립 출처)
- [arXiv:2606.02581 — Cost-Aware Query Routing in RAG: Empirical Analysis of Retrieval Depth Tradeoffs](https://arxiv.org/abs/2606.02581) — 2026-06 · [architecture] [cost] [retrieval] · Sanjay Mishra. 쿼리별 검색 깊이를 동적 선택하는 CA-RAG 라우터로 항상-밀집-검색 대비 토큰 비용 26% 절감, 항상-직접-추론 대비 지연 34% 감소하면서 품질 동등 유지. (snippet-verified: arXiv abs + arXiv html + ResearchGate + preprints.org 4개 이상 독립 출처)

## 2026-07-16 추가 출처

- [LG AI Research × KOSCOM — EXAONE Business Intelligence 금융 AI 에이전트](https://www.koreatimes.co.kr/www/tech/2026/07/129_exaone-koscom.html) — 2026-07-07 · [industry] [finance] [agentic] [korea] · LG AI Research × KOSCOM. ChatEXAONE RAG 기반 4-에이전트 구조(저널리스트→이코노미스트→애널리스트→의사결정)로 한국·미국 상장사 8,000개 이상 매일 자동 분석, 예측 점수 + 코멘터리 생성. 2026-07-07 KOSCOM 계약 체결. (snippet-verified: Korea Times + Asia Business Daily + Seoul Economic Daily + Korea Herald + BigGo Finance 5개 이상 독립 출처)
- [arXiv:2607.11933 — Knowledge Distillation from LLM to Cross-Encoder for RAG Reranking](https://arxiv.org/abs/2607.11933) — 2026-07-11 · [architecture] [retrieval] [reranking] · Shreeya Dasa Lakshminath, Shubhan S. LLaMA 3 (8B)를 LoRA SFT + 4비트 양자화로 파인튜닝해 크로스 인코더 드롭인 대체 리랭커 구현. 답변 정확도 +21%, 크로스 인코더 이차 비용 해소. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)
- [arXiv:2607.11464 — FAIR GraphRAG: Integrating FAIR Digital Objects in Graph Retrieval-Augmented Generation](https://arxiv.org/abs/2607.11464) — 2026-07-13 · [architecture] [graph] [scientific] · Marlena Flüh, Soo-Yon Kim, Carolin Victoria Schneider, Sandra Geisler (RWTH Aachen Univ.). FAIR 디지털 오브젝트(FDO)를 그래프 노드로 통합해 과학·의료 RAG의 추적성·재현성·상호운용성 구조적 보장. (snippet-verified: arXiv abs + arXiv html + IEEE Xplore + RWTH Publications 4개 독립 출처)

## 2026-07-15 추가 출처

- [arXiv:2512.20136 — M³KG-RAG: Multi-hop Multimodal Knowledge Graph-enhanced Retrieval-Augmented Generation](https://arxiv.org/abs/2512.20136) — 2026-06 · [architecture] [graph] [multimodal] [korea] · Hyeongcheol Park(고려대), Jiyoung Seo(성균관대), Wonmin Byeon(NVIDIA), JeungSub Lee(한화시스템), Sangpil Kim(고려대) 외. 멀티홉 멀티모달 지식 그래프(M³KG) + GRASP 선택적 프루닝으로 오디오-비주얼 QA에서 유의미한 성능 향상. CVPR 2026 발표. (snippet-verified: arXiv abs + NVIDIA Research + CVPR OpenAccess + YouTube 발표 영상 4개 독립 출처)
- [arXiv:2509.15577 — Relevance to Utility: Process-Supervised Rewrite for RAG](https://arxiv.org/abs/2509.15577) — 2026-07 · [architecture] [retrieval] [korea] · Jaeyoung Kim, Jongho Kim, Seung-won Hwang(서울대), Seoho Song, Young-In Song. 검색 관련성→생성 유용성 간극을 재작성으로 해소. R2U: 나이브 RAG 대비 F1 +6.8%p, 최고 기존 기준선 대비 +5.6%p. ACL 2026 Findings 채택. (snippet-verified: arXiv abs + ACL 2026 Findings 목록 + SNU 교수 프로필 3개 독립 출처)

## 2026-07-14 추가 출처

- [arXiv:2607.09092 — AgentKGV: Agentic LLM-RAG Framework with Two-Stage Training for the Fact Verification of Knowledge Graphs](https://arxiv.org/abs/2607.09092) — 2026-07-10 · [agentic] [knowledge-graph] [korea] · Yumin Heo, Hyeon-gu Lee (NAVER), Sumin Seo (NAVER), Youngjoong Ko (성균관대). 에이전틱 LLM-RAG 기반 지식 그래프 팩트 검증. 동적 라우팅(파라메트릭 vs 외부 검색)·반복 쿼리 재작성 + SFT+GRPO 2단계 학습. T-REx 및 NAVER 한국 엔터프라이즈 KG 벤치마크에서 최고 성능. (snippet-verified, arXiv abs + html + cs.CL listing 3개 독립 출처; NAVER·SKKU 저자 소속 확인)
- [arXiv:2607.11683 — RAGU: A Multi-Step GraphRAG Engine with a Compact Domain-Adapted LLM](https://arxiv.org/abs/2607.11683) — 2026-07-13 · [architecture] [graph] [open-source] · Mikhail Komarov, Ivan Bondarenko, Stanislav Shtuka 외 (ITMO Univ., Novosibirsk State Univ., Far Eastern Federal Univ.). 추출-통합 분리 2단계 유형 추출 + DBSCAN 중복 제거 + Leiden 커뮤니티 탐지. Meno-Lite-0.1(7B)이 Qwen2.5-32B를 KG 구성에서 +12.5% 조화평균 초과. 오픈소스 모듈형 GraphRAG 엔진. (snippet-verified, arXiv abs + html 2개 독립 출처)

## 2026-07-13 추가 출처

- [LY Corp Tech-Verse 2026 — Semantic Context OS](https://techblog.lycorp.co.jp/ko/techverse2026-59) — 2026-06-29 · [architecture] [code-intelligence] [korea] · LY Corp(LINE Yahoo). 코드 인텔리전스 AI 에이전트용 RAG 대체 아키텍처. PathAlign 스테이지: 벡터 거리 탐색 대신 정적 AST 파싱으로 구문 트리 보존 계층적 컨텍스트 수집. Tech-Verse 2026 컨퍼런스 발표(2026-06-29). (snippet-verified, 한/영/일 3개 이상 독립 출처)
- [arXiv:2607.07721 — Context Graphs for Proactive Enterprise Agents](https://arxiv.org/abs/2607.07721) — 2026-07 · [agentic] [enterprise] [proactive] · Avinash Kumar. cs.AI, cs.LG. Context Graph + Delta Detection Engine + Proactivity Scorer + Claude API Surfacing Layer. Precision@5=0.83, FP=0.11, 알림 시간 47분→30초 미만. 계약·인시던트·영업 파이프라인 3건 평가. (snippet-verified, 복수 독립 출처)
- [arXiv:2607.08269 — PolyUQuest: Verifiable Structure-Aware Web Retrieval-Augmented Generation](https://arxiv.org/abs/2607.08269) — 2026-07 · [education] [graph] [web-rag] · Ying Liu, Yi Ye, Quanyu Feng et al. (홍콩폴리텍대). 이종 그래프(hyperlink topology + DOM hierarchy + entity-relation) 기반 대학 웹사이트 RAG. 4,240페이지·31,086 DOM 블록·29,119 엔티티·37,680 관계. 기존 RAG 대비 정확성·커버리지·충실성 우위. (snippet-verified, 2개 독립 출처)

## 2026-07-12 추가 출처

- [arXiv:2604.26649 — When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models](https://arxiv.org/abs/2604.26649) — 2026-04 · [architecture] [retrieval] [reasoning] · Dongxin Guo, Jikun Wu, Siu Ming Yiu. SIGIR 2026. 대형 추론 모델(DeepSeek-R1·o1)의 확장 CoT 체인과 RAG 컨텍스트 주입 간 구조적 불일치 해소. 단계별 불확실성 감지기·검색 개입 정책으로 추론 중 선택적 검색 개입. 나이브 통합 대비 3.2배 오버헤드 감소. (snippet-verified, 4개 독립 출처: arXiv abs + SIGIR 2026 프로그램 + ACL Anthology + arXiv pdf)
- [arXiv:2606.29645 — Metadata, Structure, or Strategy? A Decomposition of RAG Context Enrichment](https://arxiv.org/abs/2606.29645) — 2026-06-29 · [architecture] [retrieval] [chunking] · Saber Zerhoudi, Michael Granitzer, Jelena Mitrovic. ECML-PKDD 2026. 처리 가능성 위계(Processability Hierarchy): 사전 학습 특성 기반 메타데이터 활용 예측. 정렬된 환경에서 소형 모델이 프론티어 모델을 F1 19점 상회. RAG 설계를 메타데이터 축적→모델-컨텍스트 정렬으로 전환 제안. (snippet-verified, 2개 이상 독립 출처)

## 2026-07-11 추가 출처

- [bizwatch.co.kr — 네이버, 쇼핑앱에 AI 에이전트 출시](https://www.bizwatch.co.kr/) — 2026-07-01 · [enterprise] [korea] [commerce] · 네이버 쇼핑앱 쇼핑 AI 에이전트 공식 출시. 커머스 특화 LLM "Shopping Intelligence"(100억 건 쇼핑 기록 학습) + 탐색·비교·추천 멀티 에이전트 + 사용자 쇼핑 맥락 기반 프로액티브 대화 트리거. (snippet-verified, 5개 이상 독립 출처: navercorp.com + daum.net + bizwatch.co.kr + etoday.co.kr + designcompass.org)
- [AI21 Blog — Query-Dependent Chunking](https://www.ai21.com/blog/query-dependent-chunking/) — 2026-03 · [architecture] [chunking] · 최적 청크 크기가 쿼리 의존적임을 실증(oracle gap 20–40%+). 100/200/500 토큰 멀티 인덱스 + RRF로 1–37% 리콜 향상. AIEWF 2026 "Stop Chunking Like It's 2022" 발표. GitHub: AI21Labs/multi-window-chunk-size. (snippet-verified, 3개 이상 독립 출처)
- [arXiv:2607.03880 — Next-Gen Sponsored Search: Crafting the Perfect Query with Inventory-Aware RAG (InvAwr-RAG) Based GenAI](https://arxiv.org/abs/2607.03880) — 2024-07-18 원발표(SIGIR eCom 2024), 2026-07 arXiv 게시 · [commerce] [architecture] [retrieval] · Walmart AdTech. 의미 검색 + 실시간 재고 필터링 RAG로 스폰서드 검색 키워드 자동 생성. Fill Rate 68% 향상(GPT-4 기준선 대비). 동적 생성 + 히스토리 기반 + RRF 앙상블. (snippet-verified, 4개 독립 출처: arXiv abs + html + semanticscholar.org + sigir-ecom.github.io)

## 2026-07-10 추가 출처

- [arXiv:2607.06641 — Healthier LLMs: Retrieval-Augmented Generation for Public Health Question Answering](https://arxiv.org/abs/2607.06641) — 2026-07-07 · [medical] [architecture] [retrieval] · 영국 기반 연구팀. PubHealthBench(UK 공중보건 지침 7,929개 Q&A)를 RAG 설정으로 확장. 하이브리드 검색이 리콜·랭킹 품질 일관 향상. 최적 청크 크기가 도메인·주제별로 달라짐을 실증. 개방형 응답 평가의 필요성 제기. (snippet-verified, 2개 arXiv 출처: abs + html)
- [arXiv:2607.07302 — Evaluating RAG Metrics in Applied Contexts: An Experiment, Its Findings and Its Limitations](https://arxiv.org/abs/2607.07302) — 2026-07-08 · [architecture] [evaluation] · Quentin Brabant, Orange Research. EvalLLM 2026 프랑스어 워크숍 발표 영문 번역. Ragas·DeepEval·RAGChecker·Opik 4개 라이브러리의 자동 지표를 실제 비즈니스 QA 데이터셋에 적용, 인간 평가·recall과의 상관관계 체계 분석. 자동 지표가 실무 맥락에서 인간 평가와 항상 일치하지 않음을 실증. (snippet-verified, 2개 arXiv 출처: abs + html)

## 2026-07-09 추가 출처

- [Digital Today — Naver unveils core technology behind AI Tab](https://www.digitaltoday.co.kr/en/view/78099/naver-unveils-core-technology-behind-ai-tab) — 2026-07-02 · [enterprise] [korea] [architecture] · 네이버 AI탭 아키텍처 공식 공개: 하네스 엔지니어링 4단계 파이프라인, Clarify RL(모호 시 추가 질문), 분업형 SLM 구조. 기존 HCX 대비 환각 30%p 감소·속도 2배·비용 1/3. (snippet-verified, 7개 이상 독립 출처: digitaltoday + asiae + edaily + etoday + theguru + sedaily.en + koreatimes)
- [arXiv:2607.00013 — GRACE-RAG: Governed Retrieval Architecture for Canonical Evidence Synthesis, Enabling Lightweight Deployment in Closed-Domain Institutional Settings](https://arxiv.org/abs/2607.00013) — 2026-07 · [architecture] [graph] · Asit Desai, Aman Kumar, Prashant Devadiga (National Payments Corporation of India). 그래프 증강 검색 레이어로 구조적 추론을 오프라인 사전 처리. 중간 규모 모델에서 최대 20% 품질 향상. 폐쇄 도메인 기관 특화 경량 배포 지원. (snippet-verified, arXiv abs + html 2개 독립 출처)
- [arXiv:2607.06964 — End-to-End LLM Flight Planning with RAG-based Memory and Multi-modal Coach Agent](https://arxiv.org/abs/2607.06964) — 2026-07 · [agentic] [multimodal] [industry:과학·항공] · Tabrizian et al. ICML 2026 LM4Plan Workshop. 항공기 비행 계획 LLM+RAG 메모리+멀티모달 코치 에이전트 엔드투엔드 파이프라인. (snippet-verified, arXiv robotics list + LM4Plan ICML26 workshop 2개 독립 출처)

## 2026-07-07 추가 출처

- [LY Corp Tech Blog — From legacy to AI-driven: An AX transformation roadmap](https://techblog.lycorp.co.jp/en/legacy-to-ai-driven-project-ax-roadmap) — 2026-07-06 · [enterprise] [korea] [agentic] · 레거시 소프트웨어를 AI 주도 개발로 전환하는 4단계 AX 로드맵. RAG를 지식 레이어로 활용해 스펙→PR 워크플로를 CI 이벤트 트리거로 자동화하는 Agentic 개발 파이프라인 구현. (snippet-verified, 2개 이상 독립 출처: 영문·일문 버전)
- [arXiv:2607.01852 — Evaluating Chunking Strategies for Retrieval-Augmented Generation on Academic Texts](https://arxiv.org/abs/2607.01852) — 2026-07-02 · [architecture] [chunking] · 스위스 대학원 논문 대상 RAGAs 기반 청킹 전략 비교. 클러스터 기반 시맨틱 청킹이 고정 크기·재귀 청킹 대비 일관된 우위를 보이지 않음. RAGAs faithfulness 신뢰도 한계도 확인. (snippet-verified, 2개 arXiv 출처: abs + html)
- [arXiv:2607.02966 — Distill Where the Student Goes: Teacher-Regularized RL for English-Evidence Cross-Lingual RAG](https://arxiv.org/abs/2607.02966) — 2026-07 · [architecture] [retrieval] [multilingual] · 교차언어 RAG에서 언어 표류(language drift) 억제를 위한 Teacher-Regularized RL(TR-RAG). 언어 일관성 붕괴율 약 27pp 감소. BioASQ-ENKB5·HotPot-ENKB5·MKQA 벤치마크. (snippet-verified, 복수 독립 출처)

## 2026-07-06 추가 출처

- [카카오 뉴스룸 — 카카오·kt cloud, 안전한 AI 생태계 구축을 위한 MOU 체결](https://www.kakaocorp.com/page/detail/12072) — 2026-06-26 · [enterprise] [korea] [security] · KT Cloud가 RAG Suite 2.0(PII 마스킹·가드레일·한국어 파서·리랭킹)을 출시하고 카카오 Kanana Safeguard를 통합. 공공·금융 기관 대상 AI 안전 RAG 서비스 제공. 국내 최초 공공 RAG Safety 통합 사례. (snippet-verified, 6개 이상 독립 출처)
- [arXiv:2607.00012 — PRA-RAG: Provably Robust Aggregation in Retrieval-Augmented Generation against Retrieval Corruption](https://arxiv.org/abs/2607.00012) — 2026-07 · [architecture] [security] · 검색 오염 공격에 대한 이론적 강건성 보장 RAG. 임베딩 기하학적 구조로 독성 문서 탐지, 안정적 집합 표현 도출. 이론적 상한 증명. Fudan University·WPI. (snippet-verified, 2개 arXiv 출처: abs + html)
- [arXiv:2606.01613 — TechRAG: Evidence-Gated Multimodal Agentic RAG for Technical Literature Reasoning](https://arxiv.org/abs/2606.01613) — 2026-06 · [agentic] [multimodal] [industry:제조] · Goodyear의 타이어·차량 동역학 기술 문서 40,000+ 페이지 RAG. FAISS+BM25+cross-encoder, Neo4j 지식 그래프, ColSmol+MUVERA 시각 검색, evidence-gated 재시도 구조. (snippet-verified, 3개 arXiv 출처: abs + html + pdf)

## 2026-07-05 추가 출처

- [카카오페이 기술 블로그 — 페이증권의 업무도우미 AI봇을 소개합니다! 근데 이제 춘식이를 곁들인](https://tech.kakaopay.com/post/choonsiri/) — 2026-06-12 · [enterprise] [korea] [finance] · 카카오페이증권이 Confluence 사내 문서 RAG 기반으로 구축한 업무도우미 AI봇 춘시리. Amazon Bedrock + PGVector 스택. 보안 규정상 외부 AI 사용 불가 환경의 내부 RAG 대체 사례. (snippet-verified, 2개 이상 독립 출처)
- [arXiv:2607.00725 — What Survives Into Context: A Diagnostic for Budget-Constrained Multi-Hop RAG and When Submodular Evidence Packing Improves It](https://arxiv.org/abs/2607.00725) — 2026-07-01 · [architecture] [retrieval] · 예산 제약 멀티홉 RAG에서 문서 리콜 대신 answer-in-context 진단 지표 제안. HotpotQA F1 예측 상관관계 0.39~0.55로 리콜의 ~0.31 능가. 서브모듈러 증거 패킹으로 답변 품질 향상. (snippet-verified, 2개 arXiv 출처)
- [arXiv:2607.00798 — ClinRAG-GRAPH: Clinical-prior Retrieval-Augmented Graph Model with Domain Adversarial Learning for Breast pCR Prediction](https://arxiv.org/abs/2607.00798) — 2026-07-01 · [medical] [graph] · 유방암 pCR 예측 RAG 그래프 모델. 내부 AUC 0.815, 외부 2센터 AUC 0.774/0.712. RAG를 임상 사례 기반 사전 지식 검색에 활용하는 새 패턴. (snippet-verified, 2개 arXiv 출처)

## 2026-07-04 추가 출처

- [Samsung Tech Blog — Agentic Search: 에이전트가 스스로 검색하는 방법](https://techblog.samsung.com/blog/article/82) — 2026년 상반기 · [enterprise] [korea] [agentic] · 삼성리서치가 LangGraph 기반 에이전트 런타임으로 구현한 Agentic Search 프레임워크. 반복 검색(Iterative Retrieval)으로 멀티 홉 복잡 질의에서 단순 RAG 대비 정확도 향상 실증. (snippet-verified)
- [arXiv:2607.01115](https://arxiv.org/abs/2607.01115) — 2026-07 · [education] [multimodal] · 대학 강의 슬라이드(텍스트·다이어그램·수식) 대상 VLM 기반 멀티모달 RAG. 텍스트 전용 RAG 대비 환각률 31.7%→6.6% 감소. 시각 정보 직접 처리가 핵심. (snippet-verified)
- [arXiv:2607.01659](https://arxiv.org/abs/2607.01659) — 2026-07 · [science] [architecture] · Rubin Observatory LSST 프로젝트 기술 문서 RAG 시스템. Weaviate+LangChain+GPT 오픈소스 스택으로 천문 레거시 문서 지식화. 연구자 자연어 질의 즉시 응답 실현. (snippet-verified)

## 2026-07-03 추가 출처

- [ET News — 채널코퍼레이션, 'AI 상담 시뮬레이션' 기능 출시](https://www.etnews.com/20260527000164) — 2026-05-27 · [industry:커머스] [korea] · 채널톡 ALF 도입 기업이 자사 홈페이지 URL만으로 가상 AI 상담 체험. RAG 기반 웹 크롤링 + 자연어 의도 파악 + 워크플로우 실행. 23만+ B2B 고객사, 반복 문의 80% 자동화. (snippet-verified, 6개 이상 독립 출처)
- [arXiv:2607.00570 — Dual-Confidence Contrastive Decoding for Retrieval-Augmented Generation](https://arxiv.org/abs/2607.00570) — 2026-07-01 · [architecture] · 멀티문서 RAG 내 충돌 정보 해소 training-free 디코딩(DCCD). 문서 레벨 + 토큰 레벨 신뢰도 결합. DRQA 엔터프라이즈 심층 리서치 벤치마크 제안. (snippet-verified, 복수 독립 출처)
- [arXiv:2607.00972 — Bayesian Uncertainty Propagation for Agentic RAG Pipelines: A Proof-of-Concept Study on Multi-Hop Question Answering](https://arxiv.org/abs/2607.00972) — 2026-07-01 · [agentic] [architecture] · 에이전틱 RAG 플래너·평가자·생성자 단계 불확실성을 베이즈 네트워크로 전파. HotpotQA 멀티홉에서 효과 확인, StrategyQA에서 한계 노출. (snippet-verified, arxiv abs + html 2개 출처)

## 2026-07-02 추가 출처

- [SKT 뉴스룸 — "사람과 AI가 원팀" SKT, AX 혁신 2.0 드라이브](https://news.sktelecom.com/226646) — 2026-06-16 · [enterprise] [korea] [agentic] · SKT AX 혁신 2.0 공식 선언. 에이닷 비즈 코워크 사내 배포, AI 에이전트에 사번 부여·디지털 직원 편입, CEO 직속 AI 보드 신설, AXMS 1.5 전사 AX 관리. (snippet-verified, 4개 이상 독립 출처)
- [AWS News Blog — Introducing Amazon Bedrock Managed Knowledge Base for faster, more accurate enterprise AI applications](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-managed-knowledge-base-for-faster-more-accurate-enterprise-ai-applications/) — 2026-06-17 · [architecture] · AWS Summit New York 2026 발표, GA. RAG 파이프라인 전체 매니지드화. Smart Parsing(멀티모달 자동 파싱) + Agentic Retriever(멀티홉 복잡 질의) + 6개 네이티브 커넥터 + MCP 호환. (snippet-verified, 8개 이상 독립 출처)
- [arXiv:2607.00895 — Beyond Document Grounding: Span-Level Hallucination Detection over Code, Tool Output, and Documents](https://arxiv.org/abs/2607.00895) — 2026-07-01 · [architecture] · Ádám Kovács 외. 코드·툴 출력·구조화 문서를 포함하는 스팬 레벨 환각 탐지 통합 벤치마크. Qwen3.5-2B span-F1 0.689 달성, LettuceDetect-large(0.17) 대비 큰 향상. (snippet-verified, 2개 arXiv 출처)

## 2026-07-01 추가 출처

- [SK텔레콤 뉴스룸 — SKT 독자 AI 모델, 철강·자동차 부품 공장 들어간다](https://news.sktelecom.com/227025) — 2026-06-25 · [enterprise] [korea] [industry:제조] · SKT A.X K1 기반 제조업 특화 AI 에이전트. KG스틸·코넥과 MOU. 온프레미스 RAG(보안 문서 참조)로 제조 현장 오답 차단, 하반기 당진공장·주조 공정 실증 예정. (snippet-verified)
- [arXiv:2606.07235 — FLOWREADER: Min-Cost Flow Optimization for Multi-Modal Long Document Q&A](https://arxiv.org/abs/2606.07235) — 2026-06 · [architecture] · A. Mehrish, S. Vascon. 멀티모달 장문서 QA를 최소 비용 흐름 최적화로 재정의. 엔트로피 정규화 리플리케이터 다이나믹스로 증거 압축, 이중 프로세스 게이트로 불필요 재검색 방지. VisDoMBench PaperTab/SlideVQA 최상위 성능. (snippet-verified)
- [AI타임스 — KAIST, AI 환각 줄이고 속도 20배 높인 차세대 '옴니 RAG' 기술 개발](https://www.aitimes.com/news/articleView.html?idxno=211929) — 2026-06-19 보도 (ACM SIGMOD 2026 발표 2026-06-02) · [architecture] [korea] · KAIST 김민수 교수팀 + 그래파이. AkasicDB(벡터+그래프+관계형 통합 DBMS) + OmniRAG. 정확도 78% 향상, 속도 20배 향상. (snippet-verified, 5개 이상 독립 출처)

## 2026-06-30 추가 출처

- [Samsung Tech Blog — RAG의 진화: 검색을 넘어, 나를 이해하는 'Personal Context'의 시대로](https://techblog.samsung.com/blog/article/80) — 2026-02-10 · [enterprise] [korea] · 삼성리서치 데이터 분석 연구실(이철준). SLM 기반 온디바이스 Semantic Router + NPU 로컬 임베딩·인덱싱 + 클라우드 LLM 하이브리드. 온디바이스 개인 데이터(일정·메모·앱 이력) 프라이버시 보존 처리. (snippet-verified)
- [arXiv:2606.19602 — Configurable Clinical Information Extraction with Agentic RAG: What Works, What Breaks, and Why](https://arxiv.org/abs/2606.19602) — 2026-06-17 · [industry:의료] · 독일 에센대학병원 핵의학과. 에이전틱 RAG 기반 온프레미스 임상 정보 추출. 74개 필드·99명 환자·7,326건 판정, 임상의 수용률 96.5%. HIPAA/GDPR 온프레미스 준수. (snippet-verified)
- [arXiv:2606.28365 — CAMI: Cost-Aware Agent-Guided Multi-Indexing for Semantic Retrieval](https://arxiv.org/abs/2606.28365) — 2026-06-28 · [architecture] · Adnan Qidwai, Anand Eswaran, Sonam Mishra, Jaydeep Sen, Sachindra Joshi (IBM Research). 샘플 기반 비용-품질 트레이드오프 추정으로 최적 의미 풍부화 인덱싱 구성 자동 결정. ACM CAIS 2026 채택. (snippet-verified)

## 2026-06-29 추가 출처

- [인사이트코리아 — 네이버, 대화형 검색 서비스 'AI탭' 정식 출시](https://www.insightkorea.co.kr/news/articleView.html?idxno=248924) — 2026-06-26 · [enterprise] [korea] [agentic] · 네이버 AI탭 5,000만 사용자 대상 정식 출시. HyperCLOVA X 기반 프로덕트 네이티브 LLM + 버티컬 RAG + Tool Calling. 베타 2개월 만에 400만 사용자. 에이전트N 로드맵 시작점. (snippet-verified)
- [arXiv:2606.21649 — EvoEmbedding: Evolvable Representations for Long-Context Retrieval and Agentic Memory](https://arxiv.org/abs/2606.21649) — 2026-06-24 · [architecture] · Chang Nie, Chaoyou Fu 외. 연속 메모리 큐 기반 진화 가능 임베딩. Qwen3-Embedding-8B 등 대형 모델 능가, naive RAG에 장착 시 전용 에이전틱 메모리 시스템 능가. GitHub: MiG-NJU/EvoEmbedding (0.8B·4B). (snippet-verified)
- [arXiv:2606.05901 — Reducing Hallucinations in Complex Question Answering using Simple Graph-based RAG (long version)](https://arxiv.org/abs/2606.05901) — 2026-06-04 · [architecture] · Wedge, Stutter, Dixon, Cała (Newcastle Univ.·EPCC 외). 단순 그래프 스키마 + 벡터 검색 하이브리드로 MoNaCo 벤치마크에서 복잡한 질의 거부율 절반 이상 감소, 정답률 향상. "안전한 거부" 원칙 적용. (snippet-verified)

## 2026-06-28 추가 출처

- [카카오뱅크 테크 블로그 — 2025 금융 AI Challenge 후기: LostCow팀의 RAG 챌린지 도전기](https://tech.kakaobank.com/posts/2602-financial-security-ai-challenge-review/) — 2026-02 · [industry:금융] [korea] · MoE+CPT+BM25 하이브리드 검색 + 13단계 필터링 파이프라인. 금융 규제 법령 QA, 기준 대비 +0.9pp, 우수상. 금융 도메인 BM25 우위 실증. (snippet-verified)
- [arXiv:2606.15906 — MAGE-RAG: Multigranular Adaptive Graph Evidence for Agentic Multimodal Long-Document QA](https://arxiv.org/abs/2606.15906) — 2026-06-14 · [architecture] · 멀티그레뉴러 증거 그래프(페이지+요소 노드 계층), 적응형 컨텍스트 예산, 에이전틱 검색-생성-재검색 루프. 장문서 멀티모달 QA 특화. (snippet-verified)
- [KT Cloud 기술 블로그 — RAG 성능 최적화 가이드 (TopK·Rerank·Dedup·Compression)](https://tech.ktcloud.com/entry/2026-04-ktcloud-ai-rag-성능-최적화) — 2026-04 · [enterprise] [korea] · AI Foundry 기반 RAG 4대 최적화 축(TopK 튜닝·Reranking·Deduplication·Compression) 실험 수치 포함. KT Cloud 시리즈 #3. (snippet-verified)

## 2026-06-27 추가 출처

- [LG 공식 보도자료 — LG CNS, 기업용 에이전틱 AI 플랫폼 '에이전틱웍스'와 업무혁신 서비스 '에이엑스씽크' 공개](https://www.lg.co.kr/media/release/29289) — 2025-08-25 · [enterprise] [agentic] [korea] · LG CNS 에이전틱웍스 6모듈 플랫폼(MCP+A2A+RAG) 발표. LG디스플레이 일일 생산성 10% 향상·연간 100억원 비용 절감 검증. (snippet-verified)
- [PRNewswire — LG CNS Expands Global Footprint with Latest ERP Testing Solution Powered by Agentic AI](https://www.prnewswire.com/news-releases/lg-cns-expands-global-footprint-with-latest-erp-testing-solution-powered-by-agentic-ai-302807074.html) — 2026-06-25 · [enterprise] [agentic] [korea] · PerfecTwin ERP Edition 공개. SAP Sapphire 2026, 실거래 데이터 기반 ERP 테스트 시나리오 자동 생성, 히타치 솔루션즈 크리에이트(HSC) 일본 파트너십. (snippet-verified)
- [arXiv:2606.26458 — MKG-RAG-Bench: Benchmarking Retrieval in Multimodal Knowledge Graph-Augmented Generation](https://arxiv.org/abs/2606.26458) — 2026-06-24 · [architecture] · Penn State Univ. 외. 멀티모달 지식 그래프 RAG 검색 전문 크로스도메인 벤치마크(일반+의료 도메인). 검색이 MKG-RAG의 결정적 병목임을 정량화. 기존 BEIR·MTEB의 한계 실증. (snippet-verified)

## 2026-06-26 추가 출처

- [LY Corp Tech Blog — Architecting Semantic Context OS: Beyond token stuffing in agentic systems](https://techblog.lycorp.co.jp/en/techverse2026-59) — 2026-06-22~26 · [agentic] [architecture] [korea] · LY Corp Tech-Verse 2026 세션 59. 코드 RAG에서 벡터 검색이 AST를 파괴하는 문제를 PathAlign(AST 기반 컨텍스트 격리)으로 해결. 소프트웨어 인텔리전스 에이전트용 Semantic Context OS 아키텍처 제안. (snippet-verified)
- [arXiv:2606.01240 — Efficient RAG with Intent-Aware Retrieval and Semantics-Preserving Chunking](https://arxiv.org/abs/2606.01240) — 2026-06 · [architecture] · InSemRAG: IAR(쿼리 의도 기반 동적 하이브리드 검색) + SPC(손상된 증거 청크 탐지·복원) + SLM 기반 반복 검색-확인 루프. HotPotQA F1 +2.65, FEVER 정확도 +1.5. (snippet-verified)
- [KT Enterprise — MWC26, KT가 세계에 선보인 AI 인프라 혁신](https://enterprise.kt.com/bt/dxstory/3782.do) — 2026-03-02 · [enterprise] [korea] [agentic] · KT 에이전틱 패브릭: 기업용 AI 운영체제. 5계층(Experience-Intelligence-Context-Execution-Governance), Context Layer에 Memory+RAG 내재화, Zero Trust 보안, 대법원·금융기관·제조사 사례. (snippet-verified)

## 2026-06-25 추가 출처

- [디지털데일리 — 클로바 스튜디오 포 거브, 개발 도구서 공통기반으로 진화](https://www.ddaily.co.kr/page/view/2026062416435873544) — 2026-06-24 · [enterprise] [korea] · 네이버클라우드 CLOVA Studio for Gov: 행안부·과기부 등 40개+ 부처·기관 확산, 하반기 GraphRAG·멀티모달 RAG·MCP 연동 에이전트 빌더 강화 계획. '2026 공공 AI 박람회' 발표. (snippet-verified)
- [ZDNet Korea — 삼성SDS 패브릭스로 행정 혁신 가속](https://zdnet.co.kr/view/?no=20260624173649) — 2026-06-24 · [enterprise] [agentic] [korea] · 삼성SDS 패브릭스: 공공기관 직원이 직접 AI 에이전트 개발. 정부24 AI(RAG 4단계 구조), AI 민원서포터, AI 조달법령 해석 등 공개. '2026 공공 AI 박람회' 참가. (snippet-verified)
- [arXiv:2506.05690 — When to use Graphs in RAG: A Comprehensive Analysis for Graph Retrieval-Augmented Generation](https://arxiv.org/abs/2506.05690) — 2025-06-06 (ICLR 2026) · [architecture] · GraphRAG-Bench 제안. GraphRAG가 Natural Questions에서 vanilla RAG 대비 13.4% 정확도 하락, 멀티홉 추론에서만 4.5% 향상(지연 2.3배). 그래프를 써야 하는 시나리오를 체계적 분석. (snippet-verified)

> 형식: `- [제목](URL) — 발행일 · 도메인 태그 · 한 줄 요약`
>
> 도메인 태그: `[enterprise]` `[architecture]` `[agentic]` `[industry:금융]` `[industry:의료]` `[industry:법률]` `[industry:교육]` `[korea]`

## 2026-06-24 추가 출처

- [ITing — [AWS SUMMIT 2025] 쿠팡의 생성형AI기반 광고플랫폼 혁신](https://iting.co.kr/aws-summit-seoul-2025-techblog-7/) — 2025 · [enterprise] [korea] · 쿠팡 광고 에이전트: Bedrock + Knowledge Base RAG, 수치 일치 기반 응답 품질 점수화, 프롬프트 캐싱 비용 최적화. AWS Summit Seoul 2025 발표. (snippet-verified)
- [Databricks Blog — Agent Bricks: Data + AI Summit 2026](https://www.databricks.com/blog/agent-bricks-dais-2026) — 2026-06 · [architecture] · DAIS 2026 Agent Bricks 확장 발표. Knowledge Assistant GA(단순 RAG 대비 최대 70% 품질 향상), Lakebase 에이전트 메모리, 100k+ 에이전트 빌드, Unity Catalog 메타데이터 + 검색 통합. (snippet-verified)
- [arXiv:2606.15971 — SAG: SQL-Retrieval Augmented Generation with Query-Time Dynamic Hyperedges](https://arxiv.org/abs/2606.15971) — 2026-06-14 · [architecture] · Zleap AI. 청크를 이벤트+엔티티로 변환, SQL JOIN으로 쿼리 시점에 동적 하이퍼에지 생성. 그래프 사전 구축 없이 구조화 필터링·의미 확장·LLM 리랭킹 통합. 증분 업데이트 자연 지원. (snippet-verified)

## 2026-06-23 추가 출처

- [Toss Tech Blog — 토스플레이스 데이터봇 '판다(PANDA)'를 소개합니다](https://toss.tech/article/da-assistant-panda) — 2026-04-22 · [enterprise] [korea] · 토스플레이스 내부 데이터 추출 에이전트. LLM + Text-to-SQL + ReAct 루프. 오픈 첫날 팀원 1/3, 1주일 내 1/2 사용. 메시지 4,000건+. (snippet-verified)
- [arXiv:2506.12071 — T²-RAGBench: Text-and-Table Benchmark for Evaluating Retrieval-Augmented Generation](https://arxiv.org/abs/2506.12071) — EACL 2026 · [industry:금융] [architecture] · University of Hamburg. 금융 문서 텍스트+테이블 혼합 RAG 벤치마크. 23,088 트리플. Hybrid BM25가 text-embedding-3-large 능가. (snippet-verified)
- [블로터 — KT RAG, 산업 최적화·데이터 선순환 '강점'](https://www.bloter.net/news/articleView.html?idxno=665779) — 2026-06 · [enterprise] [korea] · KT 사내 AI 에이전트: 임직원 약 1만 4,000명 사용, 사용률 97%. 모듈형 아키텍처로 산업별 RAG 유형(그래프·멀티모달·에이전트) 조합. (snippet-verified)

## 2026-06-22 추가 출처

- [LY Corp Tech Blog — Uniting analytics with AI agents as work and roles shift in the GenAI era](https://techblog.lycorp.co.jp/en/techverse2026-105) — 2026-06-22 · [enterprise] [agentic] [korea] · PJ One Piece: 사내 데이터 분석 AI 에이전트. 자연어 → 기존 2주 소요 분석을 10분으로 단축. 파일럿 사업 부문 50%+ 일상 사용. Application+Agents+Tools+Knowledge+Measurement 5계층 아키텍처. (snippet-verified)
- [arXiv:2605.29523 — K-FinHallu: A Hallucination Detection Benchmark for Multi-Turn RAG in Korean Finance](https://arxiv.org/abs/2605.29523) — 2026-05-28 · [korea] [industry:금융] [architecture] · KAIST AI + KakaoBank Financial Tech Lab. 한국 금융 RAG 멀티턴 환각 탐지 벤치마크. answerability 기반 계층적 분류체계(5종 환각 유형). (snippet-verified)
- [arXiv:2606.11350 — When More Documents Hurt RAG: Mitigating Vector Search Dilution with Domain-Scoped, Model-Agnostic Retrieval](https://arxiv.org/abs/2606.11350) — 2026-06-09 · [architecture] · University of Wyoming. 문서 수 증가 시 RAG 정확도 급락(75%→<40%) 원인을 Vector Search Dilution으로 명명. MASDR-RAG(도메인 스코핑+멀티에이전트)로 해결. 200 전문가 검증 질의, 5 LLM, 6 코퍼스 평가. (snippet-verified)

## 2026-06-21 추가 출처

- [블로터 — AWS re:Invent 2025 우아한형제들, AI 에이전트로 업무 혁신...전사 30% 도입해 효율성 향상](https://www.bloter.net/news/articleView.html?idxno=649250) — 2025-12 · [enterprise] [agentic] [korea] · 물어보새 v1.5 하이브리드 에이전트 구조(슈퍼바이저 → SQL에이전트·지식에이전트 라우팅), 전사 30% 도입, AWS Bedrock + Claude 스택. v2.0 MCP+ReAct 로드맵. (snippet-verified)
- [arXiv:2606.05644 — FIDES: Faithful Inference via Deep Evidence Signals for Retrieval-Memory Conflict in RAG](https://arxiv.org/abs/2606.05644) — 2026-06-04 · [architecture] · 검색-메모리 충돌 집중 디코딩 단계를 Opposition·Shift·Noise 3신호로 탐지하는 training-free 디코더. Zhejiang Univ.·Guangzhou Univ.·GenTel.io. (snippet-verified)
- [arXiv:2606.15179 — CONCORD: Asynchronous Sparse Aggregation for Device-Cloud RAG under Document Isolation](https://arxiv.org/abs/2606.15179) — 2026-06-13 · [architecture] · 문서 격리 환경(기기-클라우드 분산 RAG). Waiting Debt Control + Certificate-guided Minimal Supplementation으로 대역폭 최소화. IEEE ICWS 2026. (snippet-verified)

## 2026-06-20 추가 출처

- [GitHub — infiniflow/ragflow](https://github.com/infiniflow/ragflow) — 2026-06-17 (v0.26.1) · [enterprise] [architecture] · 오픈소스 RAG+에이전트 엔진. 83k stars. 최신 업데이트: Slack/Teams/Salesforce/SharePoint 커넥터, Ψ-RAG(RAPTOR+AHC) 모드, GraphRAG 체크포인트, 메시징 채널 직접 배포.
- [GitHub — chopratejas/headroom](https://github.com/chopratejas/headroom) — 2026-06-16 (v0.26.0) · [architecture] · RAG 청크·도구 출력 컨텍스트 압축 레이어. Python/Rust/TypeScript, Apache-2.0, 41.8k stars. 6종 압축 알고리즘으로 60-95% 토큰 절감. MCP 서버 배포 지원. 품질 보존(GSM8K 87% 동일).
- [arXiv:2504.20734 — UniversalRAG: Retrieval-Augmented Generation over Corpora of Diverse Modalities and Granularities](https://arxiv.org/abs/2504.20734) — 2025-04 (ACL 2026) · [architecture] [korea] · KAIST AI 그룹. 모달리티 인식 라우팅으로 텍스트·이미지·비디오 이질적 코퍼스 RAG. 학습/무학습 기반 라우터 지원. GitHub: wgcyeo/UniversalRAG. (snippet-verified)

## 2026-06-19 추가 출처

- [ZDNet Korea — KT, 연내 초개인화 AI 에이전트 상용화 (품질·안정성 차별화)](https://zdnet.co.kr/view/?no=20260617130027) — 2026-06-17 · [enterprise] [korea] · KT 자체 개발 K-RAG 기반 에이전틱 AI 전략 발표. 산업별 RAG 유형 분화(그래프/에이전트/멀티모달), MY K·지니TV·사장이지 등 B2C 서비스 H2 2026 상용화 예정. (snippet-verified)
- [arXiv:2606.04127 — When Retrieval Doesn't Help: A Large-Scale Study of Biomedical RAG](https://arxiv.org/abs/2606.04127) — 2026-06-02 · [industry:의료] [architecture] · 5모델×10의료QA×4검색방법×4코퍼스 대규모 실험. RAG가 no-retrieval 대비 1~2% 향상에 그침. 백본 모델 선택이 검색기 선택보다 훨씬 큰 영향. 주요 병목은 검색 품질이 아닌 모델의 증거 활용 능력. (snippet-verified)
- [arXiv:2606.00610 — MemGraphRAG: Memory-based Multi-Agent System for Graph Retrieval-Augmented Generation](https://arxiv.org/abs/2606.00610) — 2026-06 (KDD 2026) · [architecture] [agentic] · 공유 메모리 기반 멀티 에이전트로 그래프 구성의 주제 일관성·논리 충돌 해소. 메모리 인식 계층적 검색 알고리즘 제안. 복수 벤치마크 SOTA 능가. GitHub: XMUDeepLIT/MemGraphRAG. (snippet-verified)

## 2026-06-18 추가 출처

- [LY Corporation 공식 발표 — LY Corporation Launches New AI Agent Brand "Agent i"](https://www.lycorp.co.jp/en/news/release/020398/) — 2026-04-20 · [enterprise] [korea] · LINE·Yahoo! JAPAN 통합 AI 에이전트 브랜드 출시. 7개 도메인 전문 에이전트, 100+ LY Corp 서비스 데이터 RAG 기반, 메모리·태스크 위임 기능 2026-06 예정. (snippet-verified)
- [LangChain Interrupt 2026 세션 녹화 — LATAM Airlines B2C 컨시어지 에이전트](https://interrupt.langchain.com/recordings) — 2026-05-13/14 · [agentic] · LATAM Airlines Supervisor+6 전문 에이전트로 DAU 4,000명 B2C 컨시어지 운영. LangSmith 관측으로 아키텍처 개선. (snippet-verified)
- [Google Research Blog — Unlocking dependable responses with Gemini Enterprise Agent Platform's Agentic RAG](https://research.google/blog/unlocking-dependable-responses-with-gemini-enterprise-agent-platforms-agentic-rag/) — 2026-06-05 · [agentic] [architecture] · Cross-Corpus Retrieval: 5개 전문 에이전트(Sufficient Context Agent 포함), 표준 RAG 대비 +34% 정확도, 퍼블릭 프리뷰. (snippet-verified)

## 2026-06-17 추가 출처

- [GitHub — onyx-dot-app/EnterpriseRAG-Bench](https://github.com/onyx-dot-app/EnterpriseRAG-Bench) — 2026-05 · [architecture] · 엔터프라이즈 특화 RAG 벤치마크. Slack 275K·Gmail 120K 등 9개 소스 50만+ 문서, 500 질문 10카테고리, MIT 라이선스, 공개 리더보드. arXiv 2605.05253.
- [GitHub — Tencent/WeKnora](https://github.com/Tencent/WeKnora) — 2026-06-10 (v0.6.2) · [enterprise] · 텐센트 오픈소스 엔터프라이즈 RAG 플랫폼. RAG Q&A + ReAct Agent(MCP+웹) + Wiki Mode 3-in-1, Go+Vue+TS, 20+ LLM 지원, Langfuse, 4단계 RBAC. 16.4k stars, MIT.
- [GitHub — Marker-Inc-Korea/AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG) — 2026-04 (v0.3.22) · [architecture] [korea] · 한국 Markr.AI의 RAG AutoML 프레임워크. 파싱→청킹→임베딩→검색→리랭킹→생성 전 단계 자동 최적화, 골든셋 기반 스윕, Apache-2.0, 4.8k stars.

## 1차 자료 (엔지니어링 블로그·사례 연구·컨퍼런스)

### 한국 (엔터프라이즈 사내 지식)
- [네이버 플레이스 개발 블로그 — Backoffice AI Agent 구축기 RAG+MCP](https://medium.com/naver-place-dev/backoffice-ai-agent-%EA%B5%AC%EC%B6%95%EA%B8%B0-rag-mcp-%EA%B8%B0%EB%B0%98-%ED%94%8C%EB%A0%88%EC%9D%B4%EC%8A%A4ai-%ED%8A%B9%ED%99%94-%EC%A7%80%EC%8B%9D-%EA%B2%80%EC%83%89-%EC%8B%9C%EC%8A%A4%ED%85%9C-9a66b4afa1aa) — 2025 · [enterprise] [korea] · 플레이스 백오피스 RAG+MCP 에이전트, 토큰 -66% 툴호출 -49%
- [우아한형제들 — AI 데이터 분석가 '물어보새' 등장 1부](https://techblog.woowahan.com/18144/) — 2024 · [enterprise] [korea] · GPT-4o+RAG+Text-To-SQL 사내 Slackbot
- [우아한형제들 기술블로그](https://techblog.woowahan.com/) — 상시 · [enterprise] [korea] · 우아한공방 Bedrock KB 기반 디자인시스템 RAG 챗봇 등
- [LY Corp Tech Blog — 엔터프라이즈 LLM 서비스 구축기 1 컨텍스트 엔지니어링](https://techblog.lycorp.co.jp/ko/building-an-llm-service-for-enterprise-1-context-engineering) — 2025 · [enterprise] [korea] · Flava AI Assistant 사내 LLM
- [LY Corp Tech Blog — 2 에이전트 엔지니어링](https://techblog.lycorp.co.jp/ko/building-an-llm-service-for-enterprise-2-agent-engineering) — 2025 · [enterprise] [korea] · plan-and-execute vs ReAct 패턴
- [LY Corp Tech Blog — Tech-Verse 2025 AI 회고](https://techblog.lycorp.co.jp/en/tech-verse-2025-recap-current-state-of-ly-ai-tech) — 2025 · [enterprise] [korea] · LY AI 기술 현황
- [바이라인네트워크 — if(kakaoAI)2024 카카오엔터프라이즈의 RAG '청크'가 핵심](https://byline.network/2024/10/241022_kakaorag_3/) — 2024-10 · [enterprise] [korea] · Koworker 사내 챗봇 + 청크 전략
- [if(kakaoAI)2024](https://if.kakao.com/2024) — 2024-10 · [enterprise] [korea] · 카카오 컨퍼런스
- [딜사이트 — SKT 자체 LLM A.X 4.0 한국어 1위](https://dealsite.co.kr/articles/143106/068020) — 2025 · [enterprise] [korea] · A.X 4.0 + RAG 운영비 -65%
- [SK Planet — 멀티 LLM 플레이그라운드](https://techtopic.skplanet.com/skp-prompthon24/) — 2024 · [enterprise] [korea] · 사내 LLM 실험 환경
- [카카오뱅크 — 2300만 고객 AI](https://ai.kakaobank.com/b0f79cf9-a280-4ff5-af94-c9c38ef54956) — 2025 · [enterprise] [korea] · AI 플레이그라운드 + 가드레일 + RAG
- [카카오뱅크 기술블로그](https://tech.kakaobank.com/) — 상시 · [enterprise] [korea] · 카카오뱅크 엔지니어링
- [네이트뉴스 — 카카오뱅크 코드러너 2025](https://news.nate.com/view/20250922n12626) — 2025-09 · [enterprise] [korea] · 비기술 직군 참여 사내 컨퍼런스
- [CIO Korea — 포스코홀딩스 Gemini 1.5 기반 뉴스·지식 검색 포털](https://www.cio.com/article/3538228/) — 2024 · [enterprise] [korea] · 포스코그룹 사내 RAG, 설비/전기 3만+ 페이지
- [POSCO DX 뉴스룸](https://www.poscodx.com/kor/pr/newsRoom.do) — 상시 · [enterprise] [korea] · 포스코 DX 뉴스
- [PRESS9 — 신한은행 '실행하는 AI'](http://www.press9.kr/news/articleView.html?idxno=64316) — 2025 · [enterprise] [korea] · AI ONE + LG CNS 협력 RAG
- [삼성SDS 인사이트 — 2025 국내 은행 AI 전망](https://www.samsungsds.com/kr/insights/ai-in-banking-in-2025.html) — 2025 · [enterprise] [korea] · 국내 은행 AI 도입 분석
- [THE AI — 스켈터랩스 벨라 큐나 LLM 연동 강화](https://www.newstheai.com/news/articleView.html?idxno=5199) — 2024 · [enterprise] [korea] · BELLA QNA RAG + 하이브리드 검색
- [AI타임스 — 국민카드 이벤트 Q&AI 베타](https://www.aitimes.com/news/articleView.html?idxno=154625) — 2024 · [enterprise] [korea] · KB국민카드 LLM 챗봇 출시
- [스켈터랩스 — 금융업 LLM 활용 사례](https://www.skelterlabs.com/blog/llm-usecase) — 2024 · [enterprise] [korea] · KB국민카드 RAG 도입 상세
- [KT Cloud 기술 블로그 — Opensource Summit 2025 AI Foundry 챗봇 구축기](https://tech.ktcloud.com/entry/2025-11-ktcloud-ai-chatbot-%EC%B1%97%EB%B4%87%ED%99%98%EA%B2%BD-%EA%B5%AC%EC%B6%95) — 2025-11 · [enterprise] [korea] · AI Foundry RAG Suite
- [KT Cloud — Tech Series RAG #1 시스템 구조](https://tech.ktcloud.com/entry/2025-08-ktcloud-ai-rag-%EC%8B%9C%EC%8A%A4%ED%85%9C%EA%B5%AC%EC%A1%B0-%EC%9D%B4%ED%95%B4) — 2025-08 · [enterprise] [korea] · RAG 핵심 개념과 시스템 구조
- [KT Cloud — Tech Series RAG #2 데이터 파싱·전처리](https://tech.ktcloud.com/entry/2025-09-ktcloud-ai-rag-parsing-%EC%A0%84%EC%B2%98%EB%A6%AC-%EC%B5%9C%EC%A0%81%ED%99%94) — 2025-09 · [enterprise] [korea] · RAG 전처리 최적화
- [포스타입 팀 블로그 — 사내 AI 챗봇 도입기 1부](https://www.postype.com/@team/post/21465430) — 2025 · [enterprise] [korea] · 백엔드 스펙 RAG 챗봇
- [포스타입 팀 블로그 — 2부 RAG부터 에이전트까지](https://www.postype.com/@team/post/21464482) — 2025 · [enterprise] [korea] · Bedrock KB 기반 사내 어시스턴트
- [SK하이닉스 뉴스룸 — 생성형 AI 로드맵 공개 플랫폼 GaiA](https://news.skhynix.co.kr/ai-platform-gaia-launching-2025/) — 2025-08 · [enterprise] [korea] · 반도체 특화 RAG→Agentic AI 4단계 로드맵, Biz 에이전트(장비보전·HR·글로벌정책·회의) 베타
- [AWS 기술 블로그 — SK하이닉스 RAG 플랫폼 구축 및 성능 평가/분석](https://aws.amazon.com/ko/blogs/tech/sk-hynix-rag-platfrom-analysis-evaluation/) — 2025 · [enterprise] [korea] · AWS Cloud 기반 SK하이닉스 RAG 플랫폼 구축 연구 사례

### 글로벌 (엔터프라이즈 사내 지식)
- [How Copilot Uses Microsoft Graph](https://www.m365.fm/blog/how-copilot-uses-microsoft-graph-behind-the-scenes/) — 2025 · [enterprise] · M365 Copilot Semantic Index + Graph 동작 원리
- [Microsoft — Knowledge in Microsoft Copilot Studio](https://www.microsoft.com/en-us/power-platform/blog/2025/03/27/knowledge-in-microsoft-copilot-studio/) — 2025-03 · [enterprise] · Copilot Studio 지식 연결
- [Glean — Definitive Guide to AI Enterprise Search 2025](https://www.glean.com/blog/the-definitive-guide-to-ai-based-enterprise-search-for-2025) — 2025 · [enterprise] · 통합 인덱스 + 지식 그래프
- [Fine-Tuning Embedding Models for Enterprise RAG (Jason Liu, Glean lessons)](https://jxnl.co/writing/2025/03/06/fine-tuning-embedding-models-for-enterprise-rag-lessons-from-glean/) — 2025-03 · [enterprise] · Glean 임베딩 fine-tune 교훈
- [ZenML LLMOps DB — Glean Custom Embeddings](https://www.zenml.io/llmops-database/fine-tuning-custom-embedding-models-for-enterprise-search) — 2025 · [enterprise] · Glean LLMOps 요약
- [AgentMarketCap — Glean $7.2B 분석](https://agentmarketcap.ai/blog/2026/04/07/glean-7b-enterprise-knowledge-search-agentic-category) — 2026-04 · [enterprise] · Glean 카테고리 분석
- [Atlassian — Rovo](https://www.atlassian.com/software/rovo) — 상시 · [enterprise] · Rovo 제품 소개
- [NetEye Blog — Atlassian Rovo Today: Architecture and Trust](https://www.neteye-blog.com/2025/12/atlassian-rovo-today-architecture-technologies-and-enterprise-trust/) — 2025-12 · [enterprise] · BM25+kNN OpenSearch + Knowledge Graph
- [MindStudio — Rovo 지식 그래프 vs RAG](https://www.mindstudio.ai/blog/atlassian-rovo-knowledge-graph-vs-rag-arr-growth) — 2025 · [enterprise] · Rovo ARR 2배 성장
- [Slack Engineering — How we built enterprise search to be secure and private](https://slack.engineering/how-we-built-enterprise-search-to-be-secure-and-private/) — 2025 · [enterprise] · Federated Search + 권한 보존 RAG
- [Salesforce — Slack as Agentic Surface](https://www.salesforce.com/blog/slack-agentic-enterprise-architecture/) — 2025 · [enterprise] · Slack agentic 아키텍처
- [Salesforce Slack Native AI](https://www.salesforce.com/slack/native-ai/) — 상시 · [enterprise] · Slack 네이티브 AI
- [Cisco Blog — Transforming work with internal AI assistant](https://blogs.cisco.com/cisco-on-cisco/cisco-secure-internal-ai-assistant) — 2025 · [enterprise] · 45M+ 인터랙션 사내 어시스턴트
- [Cisco — AI in the Workplace 케이스](https://www.cisco.com/site/us/en/solutions/cisco-on-cisco/ai-in-the-workplace.html) — 2025 · [enterprise] · 사내 AI 어시스턴트 성과
- [Salesforce — Agentforce](https://www.salesforce.com/agentforce/) — 상시 · [enterprise] · Agentforce 플랫폼
- [Gruve — Agentforce 내부 영업 지원 파일럿](https://gruve.ai/blog/boosting-sales-team-efficiency-with-agentforce-a-pilot-implementation-for-internal-sales-enablement-assistant/) — 2025 · [enterprise] · 사내 영업 어시스턴트
- [Klarna 공식 — AI Assistant 1개월 성과](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/) — 2024-02 · [enterprise] · 67% 자동화
- [LangChain Blog — Klarna 사례](https://blog.langchain.com/customers-klarna/) — 2024 · [enterprise] · Klarna AI 아키텍처
- [Sequoia — Klarna CEO 인터뷰](https://sequoiacap.com/podcast/training-data-sebastian-siemiatkowski/) — 2024 · [enterprise] · Klarna AI 전략 회고
- [Twig — Klarna 30일 무엇이 망가졌나](https://www.twig.so/blog/how-klarna-is-revolutionizing-customer-support-with-ai) — 2025 · [enterprise] · Klarna 실패 분석
- [Morgan Stanley — Key Milestone with OpenAI](https://www.morganstanley.com/press-releases/key-milestone-in-innovation-journey-with-openai) — 2024 · [enterprise] · GPT-4 사내 어시스턴트
- [Morgan Stanley — AskResearchGPT](https://www.morganstanley.com/press-releases/morgan-stanley-research-announces-askresearchgpt) — 2024 · [enterprise] · 35만+ 리서치 문서 RAG
- [OpenAI — Morgan Stanley evals](https://openai.com/index/morgan-stanley/) — 2024 · [enterprise] · AI evals + HITL
- [ZenML — Morgan Stanley GPT-4 LLMOps](https://www.zenml.io/llmops-database/enterprise-knowledge-management-with-llms-morgan-stanley-s-gpt-4-implementation) — 2024 · [enterprise] · Morgan Stanley 구현 상세
- [VentureBeat — JP Morgan 50% AI adoption](https://venturebeat.com/orchestration/jp-morgans-ai-adoption-hit-50-of-employees-the-secret-a-connectivity-first) — 2025 · [enterprise] · 60K 직원 어시스턴트
- [JPMorgan Dev Blog — Virtual Assistant for Commerce Center](https://developer.payments.jpmorgan.com/blog/product/virtual-assistant-ai-reporting) — 2025 · [enterprise] · EVEE QA 시스템
- [Uber Blog — Enhanced Agentic-RAG](https://www.uber.com/blog/enhanced-agentic-rag/) — 2025 · [enterprise] · EAg-RAG +27% 정확도
- [Uber Blog — Genie On-Call Copilot](https://www.uber.com/en-GB/blog/genie-ubers-gen-ai-on-call-copilot/) — 2024 · [enterprise] · Slack on-call copilot
- [ZenML — Enhanced Agentic RAG case](https://www.zenml.io/llmops-database/enhanced-agentic-rag-for-on-call-engineering-support) — 2025 · [enterprise] · Uber Genie LLMOps 사례
- [The New Stack — Introducing AiKA](https://thenewstack.io/introducing-aika-backstage-portal-ai-knowledge-assistant/) — 2025 · [enterprise] · Spotify AiKA Backstage
- [Backstage Blog — AiKA Data Plugins](https://backstage.spotify.com/discover/blog/aika-data-plugins-coming-to-portal) — 2025 · [enterprise] · AiKA 데이터 플러그인
- [NerdOut@Spotify Ep.30 — Building AiKA](https://creators.spotify.com/pod/profile/engineeringatspotify/episodes/30-Building-AiKA-Spotifys-AI-Knowledge-Assistant-e36rlbd) — 2025 · [enterprise] · AiKA 빌딩 팟캐스트
- [Class Central — Leveraging Internal Knowledge at Spotify (CNCF)](https://www.classcentral.com/course/youtube-leveraging-internal-knowledge-building-aika-at-spotify-majd-salman-jofre-mateu-matesanz-444896) — 2025 · [enterprise] · AiKA CNCF 토크
- [DoorDash — Path to High-Quality LLM-Based Dasher Support](https://careersatdoordash.com/blog/large-language-modules-based-dasher-support-automation/) — 2025 · [enterprise] · Dasher 지원 RAG + Guardrail + Judge
- [DoorDash — Summer 2025 Intern Projects (Chatbot-as-a-Service)](https://careersatdoordash.com/blog/part-1-doordash-2025-summer-intern-projects/) — 2025 · [enterprise] · KB Management + Chatbot-as-a-Service
- [AWS Case Study — DoorDash + Bedrock + Claude](https://aws.amazon.com/solutions/case-studies/doordash-bedrock-case-study/) — 2025 · [enterprise] · 컨택센터 + Claude
- [Walmart Corporate — Expanding GenAI Tool to 11 Countries](https://corporate.walmart.com/news/2024/01/09/walmarts-expanding-one-of-a-kind-associate-genai-tool-to-11-countries-in-2024) — 2024-01 · [enterprise] · My Assistant 글로벌 확장
- [Walmart Corporate — 1.5M Associates AI Tools](https://corporate.walmart.com/news/2025/06/24/walmart-unveils-new-ai-powered-tools-to-empower-1-5-million-associates) — 2025-06 · [enterprise] · 매장 직원 AI 도구
- [CIO Dive — Walmart 50K rollout](https://www.ciodive.com/news/Walmart-generative-AI-tool-My-Assistant/692385/) — 2024 · [enterprise] · My Assistant 5만 직원 배포
- [Stack Overflow Blog — Enterprise AI needs more than foundation models](https://stackoverflow.blog/2026/03/12/enterprise-ai-needs-more-than-foundation-models/) — 2026-03 · [enterprise] · Stack Internal 컨텍스트 전략
- [Stack Overflow — RAG topic](https://stackoverflow.blog/retrieval-augmented-generation/) — 상시 · [enterprise] · Stack Overflow RAG 토픽
- [Anthropic — How AI is Transforming Work at Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic) — 2025 · [enterprise] · 사내 Claude Enterprise 49% 활용
- [Anthropic — Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) — 2024-09 · [enterprise] · 실패 검색 -49%/-67%
- [Anthropic — Claude Customer Stories](https://claude.com/customers) — 상시 · [enterprise] · Lyft 등 고객 사례
- [AWS — Contextual Retrieval with Bedrock KB](https://aws.amazon.com/blogs/machine-learning/contextual-retrieval-in-anthropic-using-amazon-bedrock-knowledge-bases/) — 2024 · [enterprise] · Anthropic 기법 Bedrock 통합
- [Google Cloud — NotebookLM for Enterprise](https://cloud.google.com/resources/notebooklm-enterprise) — 2025 · [enterprise] · 엔터프라이즈 티어
- [Google Blog — NotebookLM Plus business tips](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-business-tips/) — 2025 · [enterprise] · 비즈니스 활용 사례

### 코드베이스 RAG
- [GitHub Next — Copilot for Your Codebase](https://githubnext.com/projects/copilot-view/) — 상시 · [enterprise] · Copilot 코드베이스 컨텍스트
- [Quastor — How GitHub Copilot Works](https://blog.quastor.org/p/github-copilot-works) — 2025 · [enterprise] · Copilot RAG 동작 원리
- [Markaicode — GitHub Copilot RAG Architecture 2026](https://markaicode.com/architecture/github-copilot-rag-architecture/) — 2026 · [enterprise] · production 인시던트 분석
- [Sourcegraph Blog — How Cody Understands Your Codebase](https://sourcegraph.com/blog/how-cody-understands-your-codebase) — 2025 · [enterprise] · search-first RAG
- [Augment Code — Cursor vs Tabnine](https://www.augmentcode.com/tools/cursor-vs-tabnine) — 2026 · [enterprise] · Global RAG 멀티레포 비교
- [Augment Code — Sourcegraph Cody vs Cursor vs Augment](https://www.augmentcode.com/tools/sourcegraph-cody-vs-cursor-vs-augment-code-for-enterprise-development) — 2026 · [enterprise] · 엔터프라이즈 코드 도구 비교
- [Augment Code — Cursor freezes on large codebases](https://www.augmentcode.com/tools/why-cursor-freezes-on-large-codebases-5-alternatives) — 2026 · [enterprise] · 모노레포 성능 분석

## 논문·기술 리포트
- [arXiv 2404.17723 — Retrieval-Augmented Generation with KG for Customer Service (LinkedIn, SIGIR 2024)](https://arxiv.org/abs/2404.17723) — 2024-04 · [enterprise] · LinkedIn 이슈 KG RAG, -28.6% 해결시간
- [arXiv 2408.04870 — ConfusedPilot: Confused Deputy Risks in RAG-based LLMs](https://arxiv.org/pdf/2408.04870) — 2024-08 · [enterprise] · M365 Copilot류 권한 우회 리스크
- [arXiv 2606.04435 — Cascading Hallucination in Agentic RAG: The CHARM Framework](https://arxiv.org/abs/2606.04435) — 2026-06-03 · [agentic] · 멀티스텝 agentic RAG의 cascading hallucination 감지·차단, 89.4% 감지율·82.1% 에러 전파 감소

## 벤더·플랫폼 공식 문서
- [Atlassian — Rovo](https://www.atlassian.com/software/rovo) — 상시 · [enterprise] · Atlassian Rovo 공식
- [Salesforce — Agentforce 플랫폼](https://www.salesforce.com/agentforce/) — 상시 · [enterprise] · Agentforce 공식
- [Salesforce — Agentforce Workshop: Ground Agent with Einstein Search](https://developer.salesforce.com/workshops/agentforce-workshop/employee-agents/2-unstructured-search) — 2025 · [enterprise] · Employee Agent 실습
- [Google Cloud — NotebookLM for Enterprise](https://cloud.google.com/resources/notebooklm-enterprise) — 상시 · [enterprise] · NotebookLM Enterprise
- [Anthropic — Claude Customer Stories](https://claude.com/customers) — 상시 · [enterprise] · 고객 사례 허브

---

## 02. 프로덕션 아키텍처 도메인 출처 (2026-06-10 추가)

### 청킹·검색 기법 1차 자료
- [Introducing Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) — 2024-09-19 · [architecture] · Anthropic 공식. Contextual Embeddings + BM25로 retrieval failure 49% 감소, 리랭커 결합 시 67% 감소.
- [Enhancing RAG with contextual retrieval (Claude Cookbook)](https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide) — 2024 · [architecture] · Anthropic 공식 구현 가이드.
- [Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models (arXiv 2409.04701)](https://arxiv.org/pdf/2409.04701) — 2024-09 (EMNLP 2024) · [architecture] · Jina AI. long-context 모델로 전체 문서 임베딩 후 청크 풀링.
- [Jina AI: Late Chunking 소개](https://www.marktechpost.com/2024/08/27/jina-ai-introduced-late-chunking-a-simple-ai-approach-to-embed-short-chunks-by-leveraging-the-power-of-long-context-embedding-models/) — 2024-08-27 · [architecture] · MarkTechPost 정리.
- [Late chunking in Elasticsearch with Jina Embeddings v2](https://www.elastic.co/search-labs/blog/late-chunking-elasticsearch-jina-embeddings) — 2024 · [architecture] · Elastic Search Labs.
- [The Chunking Paradigm: Recursive Semantic for RAG Optimization (ICNLSP 2025)](https://aclanthology.org/2025.icnlsp-1.15.pdf) — 2025 · [architecture] · 의미 vs 재귀 청킹 비교.
- [Best Chunking Strategies for RAG (Firecrawl)](https://www.firecrawl.dev/blog/best-chunking-strategies-rag) — 2026 · [architecture] · 청킹 전략 벤치마크 정리.

### 하이브리드 검색 / RRF
- [Introducing reciprocal rank fusion for hybrid search (OpenSearch Blog)](https://opensearch.org/blog/introducing-reciprocal-rank-fusion-hybrid-search/) — 2024 · [architecture] · OpenSearch 2.12+ RRF 정식 지원.
- [Hybrid Text Search Tutorial (Vespa)](https://docs.vespa.ai/en/learn/tutorials/hybrid-search.html) — 2024 · [architecture] · Vespa hybrid-rrf / hybrid-linear-normalize 옵션.
- [What is hybrid search? (Elastic)](https://www.elastic.co/what-is/hybrid-search) — 2025 · [architecture] · Elasticsearch retriever API 8.14+ RRF.
- [Hybrid Search Scoring (RRF) - Azure AI Search](https://learn.microsoft.com/en-us/azure/search/hybrid-search-ranking) — 2025 · [architecture] · Azure AI Search RRF 공식 문서.
- [Reciprocal Rank Fusion: the one-line algorithm behind hybrid search](https://blog.serghei.pl/posts/reciprocal-rank-fusion-explained/) — 2025 · [architecture] · RRF 알고리즘 분석.
- [BM42: New Baseline for Hybrid Search (Qdrant)](https://qdrant.tech/articles/bm42/) — 2024 · [architecture] · BM25 + self-attention 가중.
- [SPLATE: Sparse Late Interaction Retrieval (arXiv 2404.13950)](https://www.emergentmind.com/papers/2404.13950) — 2024 · [architecture] · ColBERTv2 + sparse adapter.

### 멀티벡터·비전 검색
- [ColPali: Efficient Document Retrieval with Vision Language Models (arXiv 2407.01449)](https://arxiv.org/abs/2407.01449) — 2024-07 (ICLR 2025 accepted) · [architecture] · PaliGemma + ColBERT, ViDoRe SOTA.
- [ColPali (HuggingFace blog)](https://huggingface.co/blog/manu/colpali) — 2024 · [architecture] · ColPali 저자 소개 글.
- [Multimodal Document RAG with Llama 3.2 Vision and ColQwen2 (Together AI)](https://www.together.ai/blog/multimodal-document-rag-with-llama-3-2-vision-and-colqwen2) — 2024 · [architecture] · ColQwen2 + Llama Vision 멀티모달 RAG 가이드.
- [multi-modal-rag-with-colpali (Microsoft)](https://github.com/microsoft/multi-modal-rag-with-colpali) — 2024 · [architecture] · Microsoft 공식 ColPali 멀티모달 RAG 샘플.

### 벡터DB·매니지드 RAG
- [Introducing Pinecone Serverless](https://www.pinecone.io/blog/serverless/) — 2024-01 · [architecture] · storage/compute 분리, 10~100배 비용 절감 주장.
- [Reimagining the vector database (Pinecone)](https://www.pinecone.io/blog/serverless-architecture/) — 2024 · [architecture] · slab/log-structured 인덱싱.
- [Pgvector vs. Qdrant (Tiger Data)](https://www.tigerdata.com/blog/pgvector-vs-qdrant) — 2025 · [architecture] · pgvectorscale로 Qdrant와 경쟁.
- [pgvector vs Pinecone vs Qdrant vs Weaviate (Kalvium Labs)](https://www.kalviumlabs.ai/blog/vector-databases-compared-pgvector-pinecone-qdrant-weaviate/) — 2026 · [architecture] · 5M 벡터에서의 지연/비용 비교.
- [Foundation Models for RAG - Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/) — 2025 · [architecture] · AWS 매니지드 RAG, vector store 옵션 정리.
- [Amazon Bedrock Knowledge Bases supports OpenSearch Service managed cluster](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-knowledge-bases-now-supports-amazon-opensearch-service-managed-cluster-as-vector-store/) — 2025 · [architecture] · OpenSearch 매니지드 vector store 지원.
- [Semantic Ranking Overview - Azure AI Search](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview) — 2025 · [architecture] · Azure transformer cross-encoder 리랭커.
- [Vertex AI RAG Engine: Build & deploy RAG implementations](https://cloud.google.com/blog/products/ai-machine-learning/introducing-vertex-ai-rag-engine) — 2025 · [architecture] · Google Cloud RAG Engine GA.
- [Search from Vertex AI | Google Cloud](https://cloud.google.com/enterprise-search) — 2025 · [architecture] · 엔터프라이즈 RAG용 매니지드 검색.
- [Snowflake Cortex Search: Unmatched Search Quality and Simplicity](https://www.snowflake.com/en/engineering-blog/cortex-search-unmatched-quality-simplicity/) — 2024-2025 · [architecture] · TREC 규모 1시간 내 서비스 생성.
- [Cortex Search Documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview) — 2025 · [architecture] · Snowflake Cortex Search 공식.

### 임베딩·리랭커
- [voyage-3 & voyage-3-lite (Voyage AI Blog)](https://blog.voyageai.com/2024/09/18/voyage-3/) — 2024-09-18 · [architecture] · OpenAI v3-large 대비 7.55% 우위.
- [voyage-3-large (Voyage AI Blog)](https://blog.voyageai.com/2025/01/07/voyage-3-large/) — 2025-01-07 · [architecture] · 신규 SOTA 범용 임베딩.
- [voyage-finance-2 (Voyage AI Blog)](https://blog.voyageai.com/2024/06/03/domain-specific-embeddings-finance-edition-voyage-finance-2/) — 2024-06-03 · [architecture] · 금융 특화, OpenAI 대비 +7%.
- [voyage-code-3 (Voyage AI Blog)](https://blog.voyageai.com/2024/12/04/voyage-code-3/) — 2024-12-04 · [architecture] · 코드 검색 +13.8~16.8%.
- [voyage-multimodal-3 (Voyage AI Blog)](https://blog.voyageai.com/2024/11/12/voyage-multimodal-3/) — 2024-11-12 · [architecture] · 텍스트·이미지·스크린샷 통합 임베딩.
- [Nomic Embed paper (arXiv 2402.01613)](https://arxiv.org/pdf/2402.01613) — 2024-02 · [architecture] · 첫 완전 오픈 8K context 임베딩.
- [BAAI/BGE Reranker v2 M3 vs Cohere Rerank (Agentset)](https://agentset.ai/rerankers/compare/baaibge-reranker-v2-m3-vs-cohere-rerank-35) — 2025 · [architecture] · CPU 350ms / GPU 80ms.
- [Best Reranker Models for RAG 2026 (BSWEN)](https://docs.bswen.com/blog/2026-02-25-best-reranker-models/) — 2026 · [architecture] · 리랭커 선택 가이드.

### PDF·멀티모달 파싱
- [Docling vs LlamaParse vs Unstructured vs Reducto (Reducto)](https://llms.reducto.ai/document-parser-comparison) — 2025 · [architecture] · 파서 비교.
- [Best PDF Parsers for AI and RAG Workflows (Firecrawl)](https://www.firecrawl.dev/blog/best-pdf-parsers) — 2026 · [architecture] · 파서 카테고리 정리.
- [PDF Data Extraction Benchmark 2025 (Procycons)](https://procycons.com/en/blogs/pdf-data-extraction-benchmark/) — 2025 · [architecture] · Docling/Unstructured/LlamaParse 비교.

### GraphRAG
- [Project GraphRAG (Microsoft Research)](https://www.microsoft.com/en-us/research/project/graphrag/) — 2024-2025 · [architecture] · Microsoft GraphRAG 공식.
- [microsoft/graphrag (GitHub)](https://github.com/microsoft/graphrag) — 2024 · [architecture] · 오픈소스 구현.
- [LazyGraphRAG sets a new standard for quality and cost](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/) — 2024-11 · [architecture] · 인덱싱 비용 1/1000.

### 평가·관측
- [LangSmith - Ragas integration](https://docs.ragas.io/en/stable/howtos/integrations/langsmith/) — 2025 · [architecture] · RAGAS+LangSmith 워크플로.
- [Arize Phoenix (GitHub)](https://github.com/arize-ai/phoenix) — 2024-2025 · [architecture] · OTel 기반 오픈소스 LLM 관측.
- [Choosing the Right LLM Evaluation Framework in 2025](https://medium.com/@mahernaija/choosing-the-right-llm-evaluation-framework-in-2025-deepeval-ragas-giskard-langsmith-and-c7133520770c) — 2025 · [architecture] · DeepEval/RAGAS/LangSmith/TruLens 비교.

### 비용·캐싱
- [Prompt caching with Claude (Anthropic)](https://www.anthropic.com/news/prompt-caching) — 2024-08 · [architecture] · 비용 -90%, 지연 -85%.
- [Prompt caching - Claude API Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) — 2024-2025 · [architecture] · cache write 1.25~2×, cache read 0.1× pricing.

### 질의 변환
- [Develop a RAG Solution—Information-Retrieval Phase (Azure)](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-information-retrieval) — 2025 · [architecture] · HyDE·multi-query·decomposition 가이드.
- [Advanced RAG: Query Decomposition and Reasoning (Haystack)](https://haystack.deepset.ai/cookbook/query_decomposition) — 2024-2025 · [architecture] · 질의 분해 패턴.

### 프레임워크
- [LangChain vs LlamaIndex 2025 (Latenode)](https://latenode.com/blog/platform-comparisons-alternatives/automation-platform-comparisons/langchain-vs-llamaindex-2025-complete-rag-framework-comparison) — 2025 · [architecture] · LlamaIndex 92% retrieval 정확도, LangGraph 도입.
- [RAFT: Adapting Language Model to Domain Specific RAG (arXiv 2403.10131)](https://arxiv.org/abs/2403.10131) — 2024-03 · [architecture] · UC Berkeley, retrieval-augmented fine-tuning.

### 신선도·파이프라인
- [How to Build a RAG Pipeline from Scratch in 2026 (kapa.ai)](https://www.kapa.ai/blog/how-to-build-a-rag-pipeline-from-scratch-in-2026) — 2026 · [architecture] · 인덱싱·신선도.
- [The Knowledge Decay Problem (Generation RAG)](https://ragaboutit.com/the-knowledge-decay-problem-how-to-build-rag-systems-that-stay-fresh-at-scale/) — 2025 · [architecture] · 60% 실패가 freshness에서.

### Instructed Retrieval (2026 신기술)
- [Databricks Blog — Instructed Retriever: Unlocking System-Level Reasoning in Search Agents](https://www.databricks.com/blog/instructed-retriever-unlocking-system-level-reasoning-search-agents) — 2026-01-06 · [architecture] · InstructedRetriever-4B, 메타데이터 인식 멀티스텝 검색 플랜, recall 35-50% ↑·답변 정확도 70% ↑
- [Databricks Blog — 3x Faster Search: Parallel Test-Time Scaling with Instructed-Retriever-1](https://www.databricks.com/blog/3x-faster-search-parallel-test-time-scaling-instructed-retriever-1) — 2026-06-04 · [architecture] · MoE + 병렬 query gen + reranking, 검색 3배 빠름·TTFT ~2초

### 보안·거버넌스
- [The Complete Guide to Enterprise AI Security: RAG, Agents & Compliance in 2025 (Ragwalla)](https://ragwalla.com/docs/guides/the-complete-guide-to-enterprise-ai-security-rag-agents-compliance-in-2025) — 2025 · [architecture] · NIST/IETF 동향.
- [Governed RAG (Infiligence)](https://www.infiligence.com/post/governed-rag-secure-policy-driven-ai-retrieval-for-enterprises) — 2025 · [architecture] · ACL·콘텐츠 마스킹·감사 로그.

### 한국 환경
- [nlpai-lab/KURE (GitHub)](https://github.com/nlpai-lab/KURE) — 2024-12 · [korea][architecture] · 고려대 한국어 검색 특화 임베딩.
- [KURE: Embedding Model for Korean-Specific Retrieval (HCLT 학술대회)](https://koreascience.kr/article/CFKO202533761230731.page) — 2025 · [korea][architecture] · KURE 논문.
- [upskyy/kf-deberta-multitask (GitHub)](https://github.com/upskyy/kf-deberta-multitask) — 2024 · [korea][architecture][industry:금융] · 카카오뱅크 KF-DeBERTa 금융 특화.
- [ddobokki/KoSimCSE (GitHub)](https://github.com/ddobokki/KoSimCSE) — 2024 · [korea][architecture] · 한국어 SimCSE 임베딩.
- [KomuRet: Korean Community-style Retrieval Benchmark](https://www.koreascience.kr/article/CFKO202533757619425.view) — 2025 · [korea][architecture] · 나무위키 기반 한국어 검색 벤치.
- [ssisOneTeam/Korean-Embedding-Model-Performance-Benchmark-for-Retriever](https://github.com/ssisOneTeam/Korean-Embedding-Model-Performance-Benchmark-for-Retriever) — 2024-2025 · [korea][architecture] · 한국어 임베딩 RAG 벤치.
- [allganize/RAG-Evaluation-Dataset-KO (HuggingFace)](https://huggingface.co/datasets/allganize/RAG-Evaluation-Dataset-KO) — 2024 · [korea][architecture] · 한국 RAG 평가 표준 데이터셋.
- [Upstage Solar Mini Now Available on AWS](https://www.upstage.ai/news/solarmini-aws) — 2024-03 · [korea][architecture] · 한국어 특화 SLM 클라우드 출시.
- [The Upstage AI Consortium Taps Allganize (KoreaTechDesk)](https://koreatechdesk.com/allganize-upstage-ai-consortium-korea) — 2025 · [korea][architecture] · Solar + Allganize RAG 파트너십.

## 산업별 사례 (04-산업별-사례.md)

### 금융 — 글로벌
- [BloombergGPT: A Large Language Model for Finance (arXiv 2303.17564)](https://arxiv.org/abs/2303.17564) — 2023-03 · [industry:금융] · 50B 파라미터 금융 LLM.
- [Bloomberg AI Powered Document Insights](https://www.bloomberg.com/professional/insights/data/bloomberg-launches-ai-powered-document-insights/) — 2024 · [industry:금융] · 금융 문서 QA.
- [Morgan Stanley & OpenAI](https://openai.com/index/morgan-stanley/) — 2023-2024 · [industry:금융] · GPT-4 기반 사내 지식 어시스턴트.
- [Morgan Stanley AI @ Work](https://www.morganstanley.com/articles/ai-work-financial-advisors) — 2024 · [industry:금융] · FA 자료 검색 채택.
- [JPMorgan IndexGPT/LLM Suite](https://www.cnbc.com/2024/08/09/jpmorgan-launches-in-house-chatbot-as-ai-based-research-analyst.html) — 2024 · [industry:금융] · 60K+ 직원 사내 LLM.
- [Goldman Sachs GS AI Assistant](https://www.reuters.com/technology/artificial-intelligence/goldman-sachs-rolls-out-ai-assistant-firmwide-2025-06-23/) — 2025-06 · [industry:금융] · 전사 배포.
- [Citi AI Tools 140K Employees](https://www.reuters.com/technology/artificial-intelligence/citi-deploys-ai-tools-thousands-employees-eight-countries-2024-06-12/) — 2024-06 · [industry:금융] · Citi Assist + Stylus.

### 금융 — 한국
- [신한투자증권 RAG 사례 (AWS Industry Week 2024)](https://www.itworld.co.kr/news/364486) — 2024 · [korea][industry:금융] · 사내 RAG 자료 검색.
- [Hana Bank LLM 도입 사례 (Megazone Cloud)](https://www.megazone.com/kr/customers/hana-bank/) — 2024 · [korea][industry:금융] · 사내 RAG·콜센터.
- [KB Financial Group: KB-GPT](https://www.kbfg.com/) — 2024-2025 · [korea][industry:금융] · KB-GPT·KB-RAG 폐쇄망 구축.
- [Kakao Bank KF-DeBERTa](https://github.com/upskyy/kf-deberta-multitask) — 2024 · [korea][industry:금융] · 한국어 금융 임베딩 오픈소스.
- [Toss Tech Blog: AI](https://toss.tech/) — 2024-2025 · [korea][industry:금융] · Toss AI 챗봇·LLM 활용.

### 의료 — 글로벌
- [Epic Cosmos & AI](https://www.epic.com/about/cosmos) — 2024-2025 · [industry:의료] · EHR + LLM 통합.
- [Microsoft Dragon Copilot](https://blogs.microsoft.com/blog/2025/03/03/empowering-clinicians-with-dragon-copilot-microsofts-new-voice-first-ai-assistant-for-healthcare/) — 2025-03 · [industry:의료] · Nuance DAX + GPT 통합.
- [Abridge AI](https://www.abridge.com/) — 2024-2025 · [industry:의료] · ambient scribe + RAG.
- [Nabla Copilot](https://www.nabla.com/) — 2024-2025 · [industry:의료] · 의사용 ambient scribe.
- [Hippocratic AI Polaris 3.0](https://hippocraticai.com/polaris-3/) — 2025 · [industry:의료] · constellation 안전 모델.
- [Hippocratic AI Constellation](https://hippocraticai.com/constellation/) — 2025 · [industry:의료] · 안전 모델 군집 아키텍처.
- [OpenEvidence Funding Round](https://www.openevidence.com/announcements/openevidence-the-fastest-growing-application-for-physicians-in-history-announces-dollar210-million-round-at-dollar35-billion-valuation) — 2025 · [industry:의료] · peer-reviewed RAG.
- [medRxiv: OpenEvidence pilot](https://www.medrxiv.org/content/10.64898/2025.11.29.25341091v1.full) — 2025 · [industry:의료] · 임상 평가.
- [NBC News: OpenEvidence](https://www.nbcnews.com/tech/tech-news/openevidence-ai-doctor-medical-physician-login-app-what-npi-uptodate-rcna341064) — 2025 · [industry:의료] · NPI 인증 의사 채택.
- [Glass Health: AI for Doctors](https://glass.health/resources/ai-for-doctors) — 2024-2025 · [industry:의료] · purpose-built clinical AI.
- [Mayo Clinic Library AI Guide](https://libraryguides.mayo.edu/AI) — 2024-2025 · [industry:의료] · 임상 RAG 권고.
- [MDPI: RAG variants for CDS](https://www.mdpi.com/2079-9292/14/21/4227) — 2025 · [industry:의료] · RAG 환각 70-90% 감소.
- [Mayo Innovation Exchange GenAI](https://innovationexchange.mayoclinic.org/accelerating-generative-ai-from-concept-to-care/) — 2024 · [industry:의료] · 임상 GenAI 도입.

### 의료 — 한국
- [서울대병원](https://www.snuh.org/) — 2024-2025 · [korea][industry:의료] · 한국형 의료 LLM·지식그래프 RAG.
- [J Korean Med Sci: Medical LLM](https://jkms.org/) — 2024-2025 · [korea][industry:의료] · 한국어 의료 LLM 연구.
- [서울아산병원 빅데이터센터](https://www.amc.seoul.kr/asan/depts/bigdata/K/main.do) — 2024-2025 · [korea][industry:의료] · 임상 RAG.
- [Lunit Newsroom](https://www.lunit.io/en/company/news) — 2024-2025 · [korea][industry:의료] · 영상 + LLM 보고서.
- [VUNO Med](https://www.vuno.co/en/vunomed) — 2024-2025 · [korea][industry:의료] · SaMD + RAG.

### 법률 — 글로벌
- [Harvey: Product](https://www.harvey.ai/products) — 2024-2025 · [industry:법률] · 600+ 로펌 도입.
- [Harvey BigLaw Bench](https://www.harvey.ai/blog/biglaw-bench) — 2024 · [industry:법률] · 공개 평가.
- [A&O Shearman ContractMatrix](https://www.aoshearman.com/en/news/a-and-o-shearman-makes-contractmatrix-available-to-clients) — 2024 · [industry:법률] · 로펌 + Harvey 공동.
- [Thomson Reuters CoCounsel](https://www.thomsonreuters.com/en/products/cocounsel) — 2024-2025 · [industry:법률] · Westlaw RAG.
- [Stanford RegLab: Legal AI Hallucinations](https://dho.stanford.edu/wp-content/uploads/Legal_RAG_Hallucinations.pdf) — 2024 · [industry:법률] · 17-33% 환각률 측정.
- [LexisNexis Protégé](https://www.lexisnexis.com/en-us/products/protege.page) — 2025 · [industry:법률] · agentic 법률 AI.
- [Hebbia](https://www.hebbia.com/) — 2024-2025 · [industry:법률] · Matrix 대규모 문서 분석.
- [Robin AI](https://www.robinai.com/) — 2024-2025 · [industry:법률] · 계약 검토 + 인간 리뷰.

### 법률 — 한국
- [인텔리콘 메타연구소](https://www.intellicon.co.kr/) — 2024-2025 · [korea][industry:법률] · 법률 AI 플랫폼.
- [LBox](https://lbox.kr/) — 2024-2025 · [korea][industry:법률] · 200만+ 판례 검색.
- [로톡](https://www.lawtalk.co.kr/) — 2024-2025 · [korea][industry:법률] · 법률 상담 매칭.
- [Thomson Reuters Korea](https://www.thomsonreuters.co.kr/) — 2024-2025 · [korea][industry:법률] · 로펌 RAG 도입.

### 교육 — 글로벌
- [Khanmigo](https://www.khanmigo.ai/) — 2024-2025 · [industry:교육] · Socratic 튜터.
- [Khan Academy + Microsoft Partnership](https://blog.khanacademy.org/khan-academy-and-microsoft-partner/) — 2024 · [industry:교육] · 교사용 무료 확대.
- [Duolingo Max](https://blog.duolingo.com/duolingo-max/) — 2024-2025 · [industry:교육] · Explain My Answer + Roleplay.
- [MagicSchool](https://www.magicschool.ai/) — 2024-2025 · [industry:교육] · 5M+ 교사 K-12.
- [MagicSchool Trust Center](https://www.magicschool.ai/trust) — 2024 · [industry:교육] · FERPA·COPPA 준수.
- [Google NotebookLM](https://notebooklm.google/) — 2024-2025 · [industry:교육] · 사용자 업로드 RAG.
- [Google Cloud NotebookLM](https://cloud.google.com/products/notebooklm) — 2025 · [industry:교육] · 엔터프라이즈 RAG.
- [OpenAI Study Mode](https://openai.com/index/chatgpt-study-mode/) — 2025 · [industry:교육] · Socratic 학습 모드.
- [Quizlet](https://quizlet.com/) — 2024-2025 · [industry:교육] · UGC + RAG 학습.

### 교육 — 한국
- [QANDA](https://qanda.ai/) — 2024-2025 · [korea][industry:교육] · 60억 풀이 RAG.
- [Riiid SANTA](https://www.riiid.com/) — 2024-2025 · [korea][industry:교육] · 적응형 외국어 학습.
- [클래스팅 AI](https://www.classting.com/) — 2024-2025 · [korea][industry:교육] · K-12 플랫폼.
- [Classum](https://www.classum.com/) — 2024-2025 · [korea][industry:교육] · 대학 강의 RAG.
- [교육부 AI 디지털교과서](https://aidt.keris.or.kr/) — 2025 · [korea][industry:교육] · AIDT 도입.

### 실패·논란 사례
- [Reuters: Mata v. Avianca](https://www.reuters.com/legal/transactional/lawyers-blame-ai-fake-citations-avianca-case-2023-06-22/) — 2023-06 · [industry:법률] · 환각 판례 인용 사건.
- [Court Order: Mata v. Avianca](https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/gov.uscourts.nysd.575368.54.0_2.pdf) — 2023 · [industry:법률] · 변호사 제재 명령.
- [BBC: Air Canada chatbot](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know) — 2024-02 · · 챗봇 환불 분쟁 판결.
- [CRT Decision: Moffatt v. Air Canada](https://canlii.ca/t/k2spq) — 2024 · · 캐나다 민사재판소 판결.
- [JAMA Network Open: AI-generated patient messages](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2823978) — 2024 · [industry:의료] · Epic MyChart AI 환각 연구.
- [Stat News: Epic AI messages](https://www.statnews.com/2024/07/15/health-care-ai-epic-patient-messages-hallucinations/) — 2024-07 · [industry:의료] · 자동화 편향 우려.
- [The Lawyer: Robin AI](https://www.thelawyer.com/) — 2025 · [industry:법률] · Robin AI 구조조정 보도.
- [Reuters: Chegg AI impact](https://www.reuters.com/technology/chegg-shares-tumble-chatgpt-threat-2023-05-02/) — 2023-05 · [industry:교육] · 시가총액 급락.

### 규제·거버넌스
- [ABA Formal Opinion 512: Generative AI Tools](https://www.americanbar.org/) — 2024 · [industry:법률] · 변호사 GenAI 사용 가이드.
- [EU AI Act](https://artificialintelligenceact.eu/) — 2024 · · 고위험 AI 규제(2026 전면).
- [HHS Health AI Strategy](https://www.hhs.gov/) — 2024-2025 · [industry:의료] · 미국 헬스케어 AI 정책.
- [한국 인공지능기본법](https://www.law.go.kr/) — 2025 통과 / 2026 시행 · [korea] · 고영향 AI 영향평가.
- [식약처 의료기기 SW 가이드라인](https://www.mfds.go.kr/) — 2024 · [korea][industry:의료] · SaMD 인허가.
- [교육부 생성형 AI 교육 활용 가이드라인](https://www.moe.go.kr/) — 2024 · [korea][industry:교육] · 초·중등 활용 가이드.
- [금감원 AI 가이드라인](https://www.fss.or.kr/) — 2024-2025 · [korea][industry:금융] · 금융 AI 운영 가이드.

---

## 2026-06-15 일일 누적 추가 출처 (합산 11건)

### 한국
- [카카오페이 기술 블로그 — AI 에이전트와 카카오페이 결제 오픈 API 연동하기: MCP Agent Toolkit 개발기](https://tech.kakaopay.com/post/kakaopay-mcp-agent-toolkit/) — 2025-08-07 · [agentic] [korea] · MCP 기반 결제 API 에이전트 툴킷 개발기. 8개 결제·구독 툴, LangChain·Vercel·OpenAI SDK 지원. 핀테크 MCP 최초 공개 사례.
- [Samsung Research Tech Blog — 업무 생산성 향상을 위한 Agentic RAG 기반 서비스](https://techblog.samsung.com/blog/article/76) — 2025 (Samsung AI Forum 2025) · [agentic] [korea] [enterprise] · 삼성리서치 DeepDive: Planner/Supervisor/Researcher 3계층 멀티에이전트가 사내 문서 → 텍스트·PPTX·HTML·팟캐스트 보고서 자동 생성
- [LY Corp Tech Blog — ODW #5: 벡터 DB와 에이전트 스킬로 RAG 시스템 만들기](https://techblog.lycorp.co.jp/ko/building-rag-system-with-vector-db-and-agent-skills) — 2026-05-07 · [agentic] [korea] [architecture] · Flava 내부 클라우드에서 에이전트 스킬(MCP 툴 래퍼)로 벡터 DB RAG 구현, tool-discovery 비용 절감 패턴
- [올거나이즈 — RAG 리더보드 공개(금융·공공·의료·법률·커머스 한국어 RAG 성능 평가)](https://www.allganize.ai/ko/blog-posts-ko/rag-leaderboard) — 2024-2025 · [korea] [industry:금융] [industry:의료] [industry:법률] · 5개 한국어 도메인 RAG 벤치마크. 실제 업무 문서(표·이미지 포함) 기반, 테스트 데이터 전체 공개.

### 글로벌 — 아키텍처
- [Google Blog — Gemini Embedding 2: Our first natively multimodal embedding model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/) — 2026-03-11 · [architecture] · 텍스트·이미지·비디오·오디오·PDF를 단일 호출로 동일 벡터 공간 매핑, 3072d MRL, ColPali 수준 시각 문서 검색 API화
- [arXiv 2603.07379 — SoK: Agentic Retrieval-Augmented Generation: Taxonomy, Architectures, Evaluation, and Research Directions](https://arxiv.org/abs/2603.07379) — 2026-03-07 · [agentic] [architecture] · Agentic RAG를 POMDP로 형식화. 에이전트 위상·계획·메모리·툴 조정 5축 분류. 평가 방법론 부재·신뢰성 리스크 지적.

---

## 2026-07-08 일일 누적 추가 출처 (3건, 루프 #22)

### 한국
- [다음뉴스 — 다음, AI 요약 서비스 베타 출시…36년 뉴스 데이터 활용](https://v.daum.net/v/20260701170435278) — 2026-07-01 · [korea] [enterprise] · 업스테이지×다음 Solar RAG 기반 포털 AI 요약 베타. 36년 치 뉴스 PGC·사전·버티컬 DB 연동.

### 글로벌 — 아키텍처·의료
- [arXiv:2607.04391 — MOSS: Memory-Orchestrated Semantic System](https://arxiv.org/abs/2607.04391) — 2026-07-05 · [architecture] · 관계형 DB 기반 감사 가능한 에이전트 메모리 아키텍처. 임베딩 RAG 불투명성 비판. 1년 실프로덕션 운영(44M 토큰, 11만 세그먼트, 16만 문서).
- [arXiv:2607.05055 — Toward Trustworthy Large Language Model Agents in Healthcare: A CareConnect Case Study](https://arxiv.org/abs/2607.05055) — 2026-07-06 · [industry:의료] · 의료 물류 안전 우선 대화 에이전트. RAG + LLM 함수 호출 + 계층적 결정론적 안전 가드레일 3중 구조.


## 2026-08-16 일일 누적 추가 출처 (3건, 루프 #61)

### 글로벌 — 의료
- [arXiv:2608.12138 — A corpus-specific clinical RAG system matches or outperforms newer frontier LLMs on HealthBench](https://arxiv.org/abs/2608.12138) — 2026-08-12 · [industry:의료] [production] [benchmark] [lmic] · Praveen Reddy, Charuta Mandke, Suvrankar Datta, Sarah Khan, Siddharth Reddy Anthireddy, Shitij Arora, Vishal Singh. VITA: 인도·LMIC 특화 코퍼스 RAG 시스템. 질환별 임상 가이드라인 + 인도 AMR 데이터 + 국가 처방집 + 자원 제한 프로토콜 코퍼스. HealthBench 4,023 영어 질문에서 VITA 51.9% vs GPT-5.4 46.1%, o4-mini 44.3% — 코퍼스 특화 RAG가 프론티어 LLM 초과. (snippet-verified: arXiv abs v1 + arXiv abs + 독립 WebSearch 스니펫)

### 글로벌 — 엔터프라이즈 (LinkedIn)
- [arXiv:2608.10224 — Self-evolving Agentic Customer Support System at LinkedIn](https://arxiv.org/abs/2608.10224) — 2026-08-10 · [enterprise] [agentic] [production] [auto-prompting] · Chih Hui Wang, Mengdie Tu, Qianyun Zhang, Wei Wu, Lili Zhou, Mingqi Shen, Changshuai Wei (LinkedIn). RAG + 진화적 자동 프롬프팅 + 모듈형 평가 폐루프. 2주 A/B 테스트: QA 셀프서브 +9.0pp, 취소 셀프서브 +4.8pp, 라우팅 정확도 +30.6pp. (snippet-verified: arXiv abs + arXiv html + Academus 3개 독립 출처)

### 글로벌 — 금융
- [arXiv:2608.12335 — HC-RAG: Evidence-Centric Retrieval-Augmented Generation over Heterogeneous Financial Filings](https://arxiv.org/abs/2608.12335) — 2026-08 · [industry:금융] [architecture] [graph] [heterogeneous] [evidence-centric] · Siyuan Chen, Huaye Tan, You Li, Jiajun Liang (cs.CL · cs.MM). 금융 연간 보고서 특화 계층적 교차-모달 RAG. 유형화 금융 증거 그래프(문서·섹션·텍스트·표 단위·메타데이터 노드) + 문서-섹션-단위 경로 증거 검색 + 공유 검색 공간 텍스트-표 정렬. (snippet-verified: arXiv abs + arXiv html 2개 독립 출처)
