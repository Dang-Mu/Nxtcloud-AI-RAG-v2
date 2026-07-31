# 03. Agentic RAG / 툴유즈 / MCP 통합

## 개요

2024년까지의 RAG는 대부분 **단방향 파이프라인**이었다 — 사용자 질문이 들어오면 임베딩하고, top-k 검색하고, 컨텍스트에 붙이고, 생성한다. 2025~2026년 들어 이 그림은 두 방향에서 동시에 무너지고 있다.

첫째, **모델이 검색을 도구로 호출**하기 시작했다. OpenAI Responses API의 file_search, Anthropic Claude의 web_search·MCP 툴, Google Gemini grounding이 모두 "retrieval = function call" 모델로 수렴했다. 사용자가 질문하면 모델이 스스로 "이건 검색해야겠다"고 판단하고, 쿼리를 재작성하고, 결과를 보고 부족하면 다시 검색한다. 이게 좁은 의미의 *Agentic RAG*다.

둘째, **MCP(Model Context Protocol)** 가 사실상의 표준이 됐다. 2024년 11월 Anthropic이 발표한 뒤 1년 만에 SDK 다운로드 월 9,700만 회, 활성 서버 1만 개를 넘었고, 2025년 12월 Anthropic은 MCP를 Linux Foundation 산하 AAIF에 기부했다. 같은 시기 Atlassian Rovo MCP, Salesforce Hosted MCP가 GA로 풀렸고, "사내 지식 = MCP 서버"라는 패턴이 엔터프라이즈에 자리잡았다. RAG가 죽는 게 아니라, **"검색"이라는 행위가 더 이상 별도 시스템이 아니라 도구 카탈로그의 한 항목**으로 흡수되는 중이다.

세 번째 축은 **컨텍스트 윈도우의 확장**이다. Claude Opus 4.6 / Sonnet 4.6 / Gemini 3.1 Pro 모두 1M 토큰, Llama 4 Scout은 10M 토큰까지 갔다. 이 때문에 한쪽에선 "RAG is dead"라는 주장이 반복되지만, 실제로는 long context가 noisy하고 비싸다는 점이 명확해졌다 — 비용 8~82배, latency 큼. 그래서 2026년 시점의 정답은 "long context 기반 + 필요시 retrieval tool 호출"이라는 하이브리드다.

## "Agentic RAG"란 무엇인가 (정의의 분화)

"Agentic RAG"는 단일 정의가 없고, 적어도 세 갈래로 쪼개진다.

1. **Retrieval-as-tool** — 가장 약한 정의. LLM이 function calling으로 vector search 함수를 호출하는 패턴. OpenAI file_search, Claude의 MCP search tool이 여기 해당. RAG 파이프라인이 LLM에 외부 함수로 노출됐을 뿐, 제어 흐름은 여전히 단순하다.
2. **Self-correcting RAG** — Self-RAG, CRAG(Corrective RAG), Adaptive RAG. 검색 결과의 품질을 모델 자신이 평가하고, 부족하면 재검색하거나 web fallback을 트리거한다.
3. **Multi-step / planning RAG** — 질문을 sub-query로 분해, 각각 검색·답변 후 합성. ReAct over documents, Plan*RAG, multi-hop decomposition이 여기 속한다.

humanloop.com의 비용·지연 차트는 이 분화를 잘 보여준다 — Adaptive RAG가 1.5~2배 비용·1.2~2배 지연으로 가장 싸고, Self-RAG는 2~3배·1.5~2배, CRAG는 3~5배·2~3배, ReAct-over-docs는 4~8배·3~5배, multi-hop decomposition은 5~10배·3~6배. **agentic으로 갈수록 정확도는 올라가지만 비용·지연은 기하급수적으로 늘어난다**는 게 2025년의 일반적 합의다.

futureagi.com의 한 줄 요약: "Documented error rate reductions of approximately 78% compared to traditional RAG implementations have been observed." — 단, 이건 multi-hop·복잡 쿼리 비율이 높은 워크로드에서만 성립한다. 단순 lookup이 80%인 워크로드에 agentic을 쓰면 비용만 늘어난다.

## 주요 패턴

### Self-RAG / CRAG / Adaptive RAG

**Self-RAG**는 모델이 생성 중에 "지금 retrieve가 필요한가?"를 self-token으로 판단하고, 필요할 때만 검색을 트리거한다. 긴 답변을 쓸 때 필요한 정보가 동적으로 바뀌는 경우(연구 보고서, 백서 작성)에 유리.

**CRAG(Corrective RAG)** — Yan et al. (ICLR 2024). 핵심은 **lightweight retrieval evaluator**가 각 검색 결과에 confidence score를 매기고, 임계치 미달이면 **web search로 fallback**하거나 **decompose-then-recompose**로 노이즈를 걸러낸다. 2025년 들어 LangGraph 공식 튜토리얼이 CRAG를 reference 구현으로 채택하면서 가장 널리 쓰이는 패턴이 됐다.

**Adaptive RAG** — 쿼리 복잡도에 따라 라우팅. "오늘 날씨"는 zero-shot, "이 보고서 요약"은 single retrieval, "A·B·C를 비교"는 multi-hop. 라우터 자체가 작은 분류기거나 LLM 판단.

### Multi-hop / 분해형 RAG

HotpotQA 스타일의 "엔티티 A는 문서 X에, 엔티티 B는 문서 Y에" 패턴. 2025년 production에서 본 패턴:

- **KRAGEN** — graph-of-thoughts로 복잡 쿼리를 sub-problem으로 분해, 각 sub-problem에 대해 sub-graph를 retrieve.
- **Plan*RAG** — 같은 depth의 독립적 노드들을 병렬 실행. 순차 ReAct 대비 지연을 크게 줄임.
- **LQR (Layered Query Retrieval)** — 계층적 plan, 각 layer가 이전 답을 기반으로 다음 검색 쿼리 생성.

운영상 합의: **per-turn retrieval cap (4~6회)** + **"I have enough" confidence signal**이 없으면 retrieval thrash로 무한루프에 빠진다. 실제로 LangGraph 공식 agentic RAG 튜토리얼이 무한루프 버그를 가지고 있어서 `rewrite_count` cap을 도입했다.

### Retrieval as a tool (function calling)

가장 광범위하게 쓰이는 패턴. function calling으로 vector search·SQL·web search·내부 API를 모두 도구로 노출하고, LLM이 골라 호출.

- **OpenAI Responses API** — file_search, web_search, computer_use를 1급 도구로. 2025년 3월 발표. Vector store 파일 한도가 2025년 11월부터 10K → 100M으로 확장. file_search는 1K쿼리당 $2.50, 스토리지 $0.10/GB/day. Assistants API는 2026년 중반 deprecation 예정.
- **Anthropic** — web_search tool, MCP search 서버, 그리고 **memory tool**(2025년 9월 베타). `/memory` 디렉토리에 파일을 만들고/읽고/수정해서 세션 간 지식을 누적하는 file-based memory.
- **Google Vertex AI Search** — RAG Engine GA, "Check grounding API"로 RAG 출력과 retrieved facts를 자동 비교해서 grounding 검증. high-fidelity mode는 Gemini 1.5 Flash를 fine-tuning해서 customer-provided context에만 답하도록.

## MCP와 RAG

MCP의 RAG 관련 의미는 두 가지다.

**(1) "검색"을 MCP 서버로 표준화** — 사내 지식이든 외부 SaaS든, 검색은 MCP 서버의 한 tool로 노출된다. 클라이언트(Claude Desktop, Claude Code, Cursor, ChatGPT Desktop)는 MCP만 알면 어떤 retrieval 시스템도 즉시 쓸 수 있다.

주요 GA 사례:
- **Atlassian Rovo MCP** — Jira·Confluence 검색·생성·수정. semantic search, issue/page create·update, UI extension 지원.
- **Salesforce Hosted MCP** — 특정 Salesforce API/데이터를 코드 없이 MCP tool로 노출. 2025년 6월 Agentforce에 native MCP client 탑재, 10월 hosted MCP servers beta.
- **Stack Overflow Stack Internal** — Confluence·Teams 콘텐츠를 atomic Q&A로 정제해서 enterprise knowledge base로 통합.

**(2) "Code Execution with MCP" — 토큰 절감의 새 패턴**

2025년 11월 Anthropic이 발표한 code execution with MCP는 MCP 사용 방식을 뒤집었다. 문제 의식:

- 에이전트가 수백~수천 개 MCP tool에 연결되면, tool 정의를 컨텍스트에 전부 로드하는 것만으로 토큰이 폭발.
- 중간 결과(예: Google Drive 파일 전체 내용)도 모델 컨텍스트를 거쳐야 하니 추가 폭발.

해결책: 에이전트가 **filesystem-like API**로 MCP tool을 탐색하게 한다. `./servers/google-drive/`, `./servers/salesforce/` 같은 디렉토리를 listing해서 필요한 tool 파일만 읽고, 복잡한 로직은 코드로 한 번에 실행해서 중간 데이터를 컨텍스트에 안 거치게 한다.

결과: 동일 워크플로우가 **150K 토큰 → 2K 토큰 (98.7% 감소)**. 이 패턴은 동시에 발표된 Advanced tool use와 한 묶음이다 — Claude가 tool을 동적으로 discover·learn·execute.

**(3) 사내 MCP 서버 구축 사례 — 네이버 플레이스**

가장 구체적인 한국 사례. 네이버 플레이스 Backoffice AI Agent는 사내 백오피스 지식 검색에 Agentic RAG + MCP 구조를 도입:

- 구성: RAG + MCP + Semantic Search + Hybrid Retrieval + RRF + LLM Reranker + Milvus + OpenSearch.
- 두 MCP 서버 비교: Lexical Search MCP(키워드 기반) vs Backoffice AI MCP(의미 기반 Agentic RAG). 신규 입사자 온보딩 시나리오로 A/B 테스트.
- **결과: 응답 만족도 2배, 응답 속도 1.4배, 토큰 사용 66% 감소, 툴 호출 49% 감소.**
- 핵심 메시지: "질의 해석부터 최종 답변까지 검색 프로세스 전반을 스스로 판단하고 제어하는 Agentic RAG 구조."

**(4) MCP 2026-07-28 신규 스펙 — Stateless Core·OAuth 2.0/OIDC·Versioned Extensions**

- **발표**: Anthropic 공식 블로그 (2026-07-28). Claude 제품군 및 MCP SDK 전반에 적용.
- **핵심 변경사항**:
  1. **Stateless Core**: 기존 양방향 상태 유지(bidirectional stateful) 연결에서 **요청-응답(request/response) 무상태 코어**로 전환. 서버리스·엣지 환경에 MCP 서버를 배포할 수 있어 진입 장벽이 크게 낮아짐.
  2. **OAuth 2.0 + OIDC 엔터프라이즈 인증**: Microsoft Entra, Okta 등 기업 ID 제공자와 직접 통합. 엔터프라이즈 배포 시 별도 인증 레이어 없이 기존 SSO 인프라 활용 가능.
  3. **버전화된 확장 프레임워크 (Versioned Extensions)**: Apps 확장(UI·권한 제어)과 Tasks 확장(비동기 장기 작업)을 명시적 버전으로 관리. 하위 호환성 보장.
- **규모**: MCP SDK 월간 다운로드 **4억 회** (전년 대비 4× 성장), 2026-07-28 현재.
- **RAG 관련 의미**: Stateless 전환으로 서버리스 RAG 검색 서버(Lambda, Cloudflare Workers 등)가 MCP 서버로 직접 노출 가능. OAuth/OIDC 통합으로 사내 지식 베이스를 기업 권한 모델 그대로 MCP tool로 안전하게 노출하는 엔터프라이즈 RAG 패턴이 표준화.
- **출처**: [Anthropic — Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude) (snippet-verified: Anthropic 공식 블로그 + ClaudeDevs X 공식 계정 + explainx.ai + stacktr.ee + bovo-digital.tech + vindler.solutions 6개 독립 출처)

## 멀티에이전트 + 검색

multi-agent + retrieval은 2025년에 가장 hype도 높고 동시에 가장 회의론도 강한 영역이다. 주요 프레임워크:

### LangGraph

가장 많이 쓰이는 production multi-agent RAG framework. 상태머신 기반이라 retrieval loop·branch·human-in-the-loop를 명시적으로 모델링하기 좋다. LangSmith observability를 묶어 쓰는 게 사실상 기본.

- 패턴: orchestrator agent + retriever sub-agents (dense·BM25·SQL·web 각각). orchestrator가 쿼리 분해 → 적절한 retriever로 라우팅 → 결과 합성.
- alphabold.com이 정리한 production 교훈: well-defined workflow + 명확한 use case boundary + LangSmith observability + human-in-the-loop checkpoint. naive하게 만들면 의미없는 chunk를 retrieve하고 hallucination이 폭발.

### CrewAI

role-playing + 순차 task delegation에 강함. sequential workflow에서 토큰 15~20% 절감. PyPI 월 130만+ 다운로드, GitHub 35K+ stars로 빠르게 production 채택. content pipeline·RAG assistant에 잘 맞음.

### AutoGen

Microsoft 발. conversation-pattern agent (agent들이 자유 대화). 복잡 reasoning에서 토큰 25~30% 절감. code execution sub-agent에 강점.

### OpenAI Agents SDK (구 Swarm)

2025년 3월 발표. Swarm의 후속. agent = system prompt + tools, **handoff = 다른 agent를 반환하는 function**이라는 미니멀한 primitive. guardrails, tracing, TypeScript 지원 추가. retrieval·persistent memory는 외부 레이어로 두는 게 명시적 설계 선택.

### 하이브리드 추천

여러 비교 글의 합의: **LangGraph가 outer orchestration, CrewAI가 structured sub-task crew, AutoGen이 code-execution sub-agent**. 그리고 retrieval은 어디서 일어나든 별도 reusable layer로.

## 메모리 시스템

agent의 "기억"은 이제 별도 산업이다. agentmarketcap.ai 추산: 2025년 agent memory 시장 $6.3B → 2030년 $28.5B(CAGR 35%). 4대 벤더:

### Letta (구 MemGPT)

운영체제의 가상메모리 비유. context window = RAM, 외부 store = disk·cold storage. 3-tier:
- **Core Memory** — context window 내 small block (RAM).
- **Recall Memory** — 대화 이력, 외부 store에서 검색 (disk cache).
- **Archival Memory** — tool call로 쿼리하는 장기 저장 (cold storage).

agent 자체가 Letta runtime 안에서 동작 (agent loop·tool execution·state persistence·memory가 통합). **30일 연속 실행에서 500+ interaction에 걸쳐 task context 유지** — typical RAG baseline은 50회 후 fragment.

### Mem0

memory layer "라이브러리". 기존 프레임워크에 bolted on. arxiv 2504.19413에서 **p95 latency 91% 감소, 토큰 비용 90%+ 절감** 보고. GitHub 48K+ stars, $24M Series A. 우선 도입에 가장 편함.

### Zep / Graphiti

temporal knowledge graph 엔진. "누가 언제 무엇을 했다"의 시간축 그래프. 시계열 의존이 큰 task(고객 히스토리, 일정·관계 추적)에 적합.

### LangChain LangMem

LangChain native. langgraph store + 메모리 retrieval 추상화.

### Anthropic Memory Tool

2025년 9월 베타. `/memory` 디렉토리에 파일 단위로 read/write/delete. file-based이라서 디버깅·인스펙션이 쉬움. **Netflix가 세션 간 context 유지에, Rakuten의 장시간 task agent가 과거 실수 재발 방지에 사용 — first-pass error 97% 감소**.

10월에 Pro/Max 사용자까지, Claude Managed Agents에도 persistent memory 공개 베타. VentureBeat의 비판: Anthropic이 memory·evals·orchestration까지 직접 소유하려는 움직임이 엔터프라이즈 lock-in 우려를 키운다.

### 실무 가이드라인

- validation phase에는 **Mem0**부터.
- 패턴 검증 후 long-horizon이 가치 있으면 **Letta**.
- Anthropic stack 고정이면 **Claude memory tool** (file-based이라 transparency 좋음).

## 코딩 에이전트의 RAG·컨텍스트 관리

이 영역에서 **가장 격렬한 정답 논쟁**이 벌어지는 중이다. 두 진영이 명확히 갈린다.

### "Agentic search" 진영 — Claude Code, Aider, Devin

vadim.blog와 milvus.io의 논쟁이 대표적. Claude Code는 **Glob + Grep + Read만 쓴다.** 임베딩도, 벡터DB도, 인덱스도 없다.

이유:
- **Security** — 인덱스는 공격 대상. 임베딩에서 코드 정보가 일정 부분 복원됨.
- **Privacy** — 사내 코드 임베딩을 어디 두느냐는 정책 문제.
- **Staleness** — 세션 시작 시 만든 인덱스는 첫 파일 수정 시점에 stale.
- **Reliability** — 시스템 하나당 실패점 하나. grep은 30년 검증됨.
- **Predictability** — 같은 쿼리에 같은 결과.

비판: grep-only는 동의어·의미 매칭이 안 돼서 결국 더 많은 round trip이 필요. 토큰을 더 태운다. — 그래서 zilliztech가 claude-context MCP server를 만듦. Milvus/Zilliz Cloud에 인덱싱, BM25 + dense vector hybrid. **동일 검색 품질 대비 토큰 40% 감소** 주장.

### "Embedding RAG" 진영 — Cursor

towardsdatascience.com에 따르면 Cursor는 **Turbopuffer 벡터DB**에 임베딩 저장. `@Codebase`나 ⌘Enter 시 의미 기반 검색. 파일경로는 client-side에서 secret key + nonce로 obfuscate해서 privacy 완화. digitalapplied.com은 "semantic search로 code agent 정확도 12.5% 향상" 수치 인용.

### Cline / Continue

- **Cline** — VS Code extension. `@problems`로 IDE diagnostic API에서 type error·lint 가져옴. `FileContextTracker`가 외부 수정 감지해서 stale context 방지. **Plan mode**(read-only exploration) + **Act mode**(편집) 분리. MCP server로 외부 DB·docs 연결.
- **Continue** — context retrieval이 architecture pattern 질문에서 Cline 대비 25% 더 정확하다는 측정.
- **Aider** — git-integrated, 터미널 native. repo map(코드 구조 요약)을 만들어 컨텍스트에 주입.

### 정리

smartscope.blog: Claude Code가 vector DB-based RAG를 버린 건 "코드 검색은 단어와 구조의 매칭이 의미 매칭보다 더 자주 정답이기 때문." Anthropic 권장도 같은 결: agentic search부터 시작하고, 속도가 부족할 때만 semantic 추가.

## RAG vs Long Context (2026 시점 정리)

2026년 6월 현재의 합의는 "**both, but mostly RAG**."

핵심 데이터:
- Claude Opus/Sonnet 4.6, Gemini 3.1 Pro: 1M tokens. Llama 4 Scout: 10M.
- akitaonrails.com / lighton.ai 종합:
  - long context가 **stable Wikipedia-style QA**에선 RAG보다 정확.
  - 하지만 **비용 8~82배**, latency 큼.
  - 모델은 long context에서도 정확도가 떨어진다는 측정이 누적 (lost-in-the-middle, needle-in-haystack 한계).
- Anthropic effective context engineering의 공식 입장: "Larger context windows help but do not replace structured retrieval, filtering, and memory management."

대신 떠오른 패턴: **just-in-time context**. 파일경로·쿼리·URL 같은 lightweight identifier만 유지하고, 필요할 때 tool로 dynamic load. 이는 정확히 Claude Code agentic search와 같은 철학이다.

## RAG vs Fine-tuning (2026 시점 정리)

이 논쟁은 사실상 끝났다. 답은 "**둘 다, 다른 용도로**."

elastic.co, glean.com, dust.tt 종합:

| 상황 | 선택 |
|---|---|
| 지식이 자주 바뀜 | RAG |
| 도메인 어휘·문체·포맷 학습 | Fine-tune |
| 정확한 출처 표시·인용 필요 | RAG |
| 다중 도메인 — 데이터 소스만 바꿔서 운영 | RAG |
| 매우 협소·반복적 task, 쿼리 볼륨 큼 | 작은 모델 fine-tune이 비용 우위 |
| 추론·tool use 능력 자체 강화 | RLHF/RLAIF (별도) |

하이브리드가 표준: **moderate fine-tune (도메인·tone) + RAG (live knowledge)**. 2024년에 많았던 "fine-tune이면 RAG 필요 없다" 주장은 거의 사라졌다.

## 한국 사례

자료가 가장 단단한 두 곳:

### 네이버 플레이스 — Backoffice AI Agent (Agentic RAG + MCP)

위에서 다룬 사례. 한국에서 가장 구체적인 Agentic RAG production write-up. 핵심 지표: 만족도 2배, 속도 1.4배, **토큰 66%·툴 호출 49% 감소**. RRF + LLM Reranker + Milvus + OpenSearch의 hybrid 구성. MCP server를 두 종류(Lexical·Semantic)로 나눠 A/B 테스트한 점이 특히 좋음.

### LY Corporation (LINE) — Flava AI Assistant (FAA)

LY 사내 클라우드 플랫폼 Flava의 AI 어시스턴트. 두 편짜리 시리즈 (techblog.lycorp.co.jp의 컨텍스트 엔지니어링·에이전트 엔지니어링).

교훈이 매우 직설적:
- "복잡한 워크플로 없이도 모델은 논리적 순서를 만들어낸다."
- **컨텍스트 엔지니어링 + 검색 후 잘 자르기 + 모델 신뢰**로 ReAct가 충분.
- 운영 결과: Flava 관련 문의의 **96.1%에 답변 제공**.
- 즉, 작은 회사가 LangGraph 같은 복잡 그래프부터 시작하지 말고 ReAct + 좋은 도구·context부터 시작하라는 메시지.

### LY Corporation — ODW #5: 벡터 DB + 에이전트 스킬로 RAG 시스템 만들기 (2026-05-07)

FAA 시리즈에서 한 발짝 더 나아간 워크숍(Open Dev Workshop) 아티클. Flava 사내 클라우드 위에서 벡터 DB와 **에이전트 스킬**을 결합해 RAG를 구현하는 실습 내용을 담았다.

- **에이전트 스킬**은 "AI 에이전트에게 어떤 컬렉션과 메타데이터를 사용해야 하는지 지식을 제공하는 MCP 툴 래퍼". 매 호출마다 에이전트가 툴 스키마 전체를 처리하는 대신, 스킬이 올바른 컬렉션 및 필터 힌트를 내장해 토큰과 추론 비용을 줄인다.
- 참가자들이 Flava 벡터 DB에 마크다운 문서를 로드하고, 에이전트 스킬로 검색 인터페이스를 만드는 핸즈온 형식. Claude Code 서브에이전트 구조도 연계.
- **핵심 메시지**: 에이전트 스킬은 MCP 툴 사용을 단순화해 RAG 파이프라인의 tool-discovery 비용을 낮추는 abstraction layer.

출처: [ODW #5: 벡터 DB와 에이전트 스킬로 RAG 시스템 만들기](https://techblog.lycorp.co.jp/ko/building-rag-system-with-vector-db-and-agent-skills) — 2026-05-07 · LY Corp Tech Blog

### 삼성리서치 — DeepDive: 사내 문서 대상 멀티에이전트 Agentic RAG 서비스

삼성리서치가 Samsung AI Forum 2025에서 발표하고 이후 기술 블로그로 공개한 내부 서비스. 방대한 사내 문서를 대상으로 정보 탐색·보고서 작성을 자동화하는 Agentic RAG 기반 플랫폼.

- **구성 요소**: Planner → Supervisor → Researcher(복수) 3계층 멀티에이전트 구조.
  - Planner: "차세대 배터리 기술 트렌드 보고서 작성"처럼 사용자 쿼리가 오면 점진적 문제 해결 전략을 수립.
  - Supervisor: 계획을 실행 단계로 변환·조율.
  - Researcher 에이전트들: 사내 문서, 웹 검색, 학술 논문, 데이터베이스에서 순차 또는 병렬로 정보 추출.
- **출력 형식**: 텍스트 보고서, 이미지 포함 PPTX, HTML, 오디오 팟캐스트 — 쿼리 성격에 따라 자동 선택.
- **데이터 소스**: 사내 문서(1차) + 웹 검색(fallback) + 학술 논문 DB. "사용자가 첨부한 문서 → 최신 논문 검색 → 웹 → 종합 보고서" 방식의 분리된 리서치 루프.
- **교훈**: 단일 QA가 아닌 "깊이 있는 멀티문서 리서치"가 목표인 워크로드에서는 Planner-based multi-step agentic이 비용을 감수할 가치가 있음.

출처: [업무 생산성 향상을 위한 Agentic RAG 기반 서비스](https://techblog.samsung.com/blog/article/76) — 2025 (Samsung AI Forum 2025 발표) · Samsung Research Tech Blog

### 카카오 PlayMCP & Kanana

- PlayMCP — 카카오가 만든 개방형 MCP 플랫폼. MCP 서버·tool 등록, 자체 Kanana 모델로 에이전트 구현.
- Kanana-2 — 카카오 첫 추론 모델, Hugging Face 오픈소스. "에이전트 최적화" 명시.
- Kanana 웹 버전 — 그룹 AI '카나' + 개인 AI '나나'.

### 카카오페이 — 결제 MCP Agent Toolkit (2025-08)

- **회사/팀**: 카카오페이 개발팀
- **목적**: AI 에이전트가 카카오페이 결제 API를 자연어 대화로 직접 호출할 수 있도록 MCP 기반 표준 연동 레이어 구축. "대화로 결제하는 시대"를 목표로 핀테크 도메인에 MCP를 최초로 공개 적용.
- **데이터 소스**: 카카오페이 결제 오픈 API (결제 준비·승인·취소·상태조회·구독 등 8개 엔드포인트)
- **스택**: MCP(Model Context Protocol) 기반, LangChain·Vercel AI SDK·OpenAI SDK 멀티 프레임워크 지원. 결제·구독 관련 8개 툴 설계.
- **아키텍처 특이점**: 기존 OpenAI function calling·LangChain tool의 한계(단일 프레임워크 종속, 비표준 인터페이스)를 MCP 표준 채택으로 극복. 에이전트가 "결제 링크 생성해줘" → 자동으로 MCP 툴 선택 → 결제 준비 → 링크 반환하는 end-to-end 대화형 결제 플로우 시연. RAG 검색이 아닌 **외부 트랜잭션 API를 도구로 노출**하는 패턴을 핀테크에 공식화.
- **결과·교훈**: AI 에이전트가 상태 조회·취소까지 실시간 처리 가능 확인. **"사내 문서 검색 MCP"를 넘어 외부 API를 에이전트 도구로 개방하는 생태계 확장** 패턴 제시. 한국 핀테크 최초의 MCP 공개 구현 사례.
- **출처**: [카카오페이 기술 블로그 — AI 에이전트와 카카오페이 결제 오픈 API 연동하기: MCP Agent Toolkit 개발기](https://tech.kakaopay.com/post/kakaopay-mcp-agent-toolkit/) (2025-08-07)

### LY Corporation — Semantic Context OS: 코드 에이전트를 위한 AST 기반 컨텍스트 검색 (Tech-Verse 2026, 2026-06)

- **회사/팀**: LY Corporation (LINE + Yahoo Japan 통합법인)
- **목적**: 자동화된 코드 리뷰·취약점 발견·리팩터링 같은 소프트웨어 인텔리전스 태스크에 LLM 에이전트를 투입할 때, 표준 벡터 RAG가 코드베이스에 실패하는 근본 원인을 해결.
- **데이터 소스**: 사내 소스코드 저장소.
- **스택**: Semantic Context OS(자체 프레임워크) + PathAlign(AST 기반 컨텍스트 분리 단계). POSIX 유사 가상 파일시스템으로 AI 커널이 상태 토폴로지를 관리, 비동기 톱니파형 메모리 모델로 인플라이트 토큰 최적화.
- **아키텍처 특이점**: 표준 벡터 RAG의 한계를 정면으로 지적한다 — 고정 글자 수 기준으로 코드베이스를 청킹하면 AST(추상 구문 트리)와 import 그래프·부모-자식 의존성이 파괴되어, 의미 있는 코드 컨텍스트 검색 자체가 불가능해진다. **PathAlign** 단계가 이를 해결한다: 타겟 소스 파일을 메모리에 계층적 구문 트리로 컴파일 → 클래스 정의·인터페이스 구현·함수 호출·변수를 식별 → 벡터 거리 탐색 대신 AST 기반 격리로 관련 컨텍스트를 정밀 추출. 이 접근은 "Large Context Window = 지능 향상"이라는 "실리콘 오류(Silicon Fallacy)"를 반박한다.
- **결과·교훈**: Tech-Verse 2026(2026-06-29 개최, 사전 기사 2026-06-22~26 공개)에서 발표. **"코드 RAG에서는 청킹 단위가 토큰이 아니라 AST 노드여야 한다"** — 문서 RAG와 코드 RAG의 청킹 전략이 근본적으로 달라야 한다는 것을 공식화한 사례. 에이전틱 소프트웨어 인텔리전스 워크플로에서 LLM 컨텍스트 관리를 운영체제(OS) 개념으로 추상화하는 방향을 제시.
- **출처**: [LY Corp Tech Blog — Architecting Semantic Context OS: Beyond token stuffing in agentic systems](https://techblog.lycorp.co.jp/en/techverse2026-59) (Tech-Verse 2026, 2026-06-22~26 공개, snippet-verified)

### LG CNS — 에이전틱웍스(AgenticWorks) + PerfecTwin ERP Edition (2025-08 출시 · 2026-06-25 글로벌 확장)

- **회사/팀**: LG CNS (LG 그룹 IT 서비스 계열사)
- **목적**: 기업이 에이전틱 AI 서비스를 설계·구축·운영·관리하는 전 주기를 지원하는 풀스택 플랫폼 제공. 내부 업무 혁신(보고서 생성·데이터 분석)과 외부 ERP 테스트 자동화를 동일 플랫폼으로 처리.
- **데이터 소스**: 사내 문서(ERP 거래 데이터·기업 지식 베이스·정책 문서) + 외부 SaaS(ERP·CRM 시스템 연동).
- **스택**: 에이전틱웍스 6개 모듈 — △**널리지 레이크**(Knowledge Lake, 데이터 전처리) △**리파이너**(모델 학습·미세조정) △**빌더**(에이전트 개발도구) △**허브**(에이전트 운영환경) △**스튜디오**(최적화·배포, RAG 체계 구축 지원) △**라우터**(모델 자동 매칭 엔진). MCP(Model Context Protocol) + A2A(Agent to Agent) 통신 지원으로 ERP·CRM 등 기업 시스템을 코드 수정 없이 에이전트에 연결.
- **아키텍처 특이점**: 스튜디오 모듈이 사전제작(Pre-Built) 에이전트에 RAG 체계를 구축하는 고도화 작업을 지원하며, MCP 표준을 통해 기존 시스템과 에이전트 간 연동 코드를 별도 개발하지 않아도 되는 점이 핵심. **PerfecTwin ERP Edition**(SAP 전용 ERP 테스트 자동화): 실거래 데이터 기반으로 테스트 시나리오를 자동 생성해 SAP S/4HANA 전환·ERP 신규 오픈 전 잠재 결함을 사전 탐지. 시나리오 설계 시간을 수 시간으로 단축. 하반기 중 **Agent Orchestration 프레임워크** 도입 예정 — 여러 AI 에이전트가 시나리오 생성→실행→오류 분석→수정→검증 전 주기를 협업 처리.
- **결과·교훈**: LG디스플레이 적용에서 일일 업무 생산성 **10% 향상**, 외부 유사 서비스 대비 **연간 100억원 이상 비용 절감** 검증. 출시 한 달 만에 10여 개 고객사와 PoC 진행 중. 2026년 6월 SAP Sapphire 2026(올랜도) 및 Japan IT Week 참가로 글로벌 전개. 히타치 솔루션즈 크리에이트(HSC)와 일본 리셀러 파트너십 체결. **교훈**: MCP + A2A 표준을 채택하면 기업 시스템 연동 커스텀 코드 개발 부담이 대폭 감소하며, 모듈형 판매(필요 기능만 선택)가 기업 도입 장벽을 낮추는 핵심 요소.
- **출처**: [LG 공식 보도자료 — 에이전틱웍스 발표](https://www.lg.co.kr/media/release/29289) (2025-08-25, snippet-verified) · [Korea Times — LG CNS debuts agentic AI testing tool in push for global ERP market](https://www.koreatimes.co.kr/amp/business/companies/20260625/lg-cns-debuts-agentic-ai-testing-tool-in-push-for-global-erp-market) (2026-06-25, snippet-verified) · [PRNewswire — LG CNS Expands Global Footprint with Latest ERP Testing Solution Powered by Agentic AI](https://www.prnewswire.com/news-releases/lg-cns-expands-global-footprint-with-latest-erp-testing-solution-powered-by-agentic-ai-302807074.html) (2026-06-25, snippet-verified)

### 그 외

- **KT Cloud** — RAG 시스템 구조 해설 시리즈 (사례 자체보단 교육 자료에 가까움).
- **CLOVA Studio** — function calling으로 외부 함수·API 호출, RAG 결합.
- **SK Devocean** — RAG 기반 Multi-Agent 구현 사례 (개인 학습 톤이지만 한국어 자료로 유용).

## 글로벌 프로덕션 사례

### LATAM Airlines — B2C 컨시어지 에이전트 (LangChain Interrupt 2026)

- **회사/팀**: LATAM Airlines (라틴아메리카 최대 항공사), Nico Venegas·Claudio Urbina
- **목적**: 항공사 B2C 웹사이트에서 여행객의 복합 질의(항공편·예약·운임·규정·FAQ·일정)를 단일 컨시어지 에이전트로 처리. 다양한 도메인 질문을 한 창구에서 자연어로 해결.
- **데이터 소스**: 항공편·예약·요금·운항 정책·여행 규정 등 항공사 내부 지식 베이스.
- **스택**: LangChain LangGraph(멀티에이전트 오케스트레이션) + LangSmith(트레이싱·관측). Supervisor 에이전트 1개 + 도메인 전문 에이전트 6개 구성.
- **아키텍처 특이점**: Supervisor 에이전트가 인텐트 분류 후 6개 전문 에이전트(항공편 검색·예약·운임·규정·FAQ·일정 도메인별)에 위임하는 계층형 패턴. **LangSmith를 설계 초기부터 관측 레이어로 통합**하여 트레이스 데이터를 기반으로 아키텍처를 지속 개선 — "시스템이 실제 어디서 깨졌는지 추적 데이터가 알려줘서 구조 변경이 가능했다"는 교훈이 핵심. 론칭 이후 아키텍처는 트레이싱 인사이트 기반으로 상당 부분 바뀌었음.
- **결과·교훈**: 일 활성 사용자(DAU) **4,000명** 규모 운영 중. LangChain Interrupt 2026(2026-05-13/14, 샌프란시스코)에서 발표.
- **출처**: [LangChain Interrupt 2026 세션 녹화](https://interrupt.langchain.com/recordings) (2026-05-13/14, snippet-verified) · [Interrupt 2026 사전 소개 블로그](https://www.langchain.com/blog/previewing-interrupt-2026-agents-at-enterprise-scale)

## 2026년 주목할 신규 연구

### Cascading Hallucination in Agentic RAG — CHARM 프레임워크 (arXiv 2606.04435)

Saroj Mishra가 2026-06-03 arXiv에 제출한 논문. Agentic RAG 멀티스텝 파이프라인에서 초기 단계의 오류가 후속 단계를 거쳐 증폭되는 **"cascading hallucination"**을 독립적인 실패 모드로 정의하고, 이를 감지·차단하는 CHARM(Cascading Hallucination Aware Resolution and Mitigation) 아키텍처 프레임워크를 제안.

**핵심 아이디어**: 기존 agentic RAG 파이프라인을 교체하지 않고 4개 컴포넌트를 병렬로 붙이는 방식.
1. **Stage-level fact verification** — 각 단계 출력에서 사실 오류를 즉시 감지.
2. **Cross-stage consistency tracking** — 단계 간 발화 일관성 추적.
3. **Confidence propagation monitoring** — confidence score가 단계를 거치며 낮아지면 조기 차단.
4. **Cascade resolution triggering** — 오류 전파 감지 시 워크플로 중단 및 재시도 트리거.

**성능 수치** (HotpotQA, MuSiQue, 2WikiMultiHopQA + 맞춤형 적대 데이터셋, LangChain agentic pipeline):
- 캐스케이드 감지율: **89.4%**
- FP율: **5.3%**
- 오류 전파 감소: **82.1%**
- 평균 추가 지연: **215ms** (단계당)

**의의**: "단계별 hallucination 누적"이 multi-hop agentic RAG의 가장 대표적 실패 모드임을 수치로 입증. per-turn cap·confidence stop과 함께, 파이프라인 레벨의 hallucination cascade 차단이 2026년 agentic RAG 운영의 새 요구사항으로 부상 중.

- **출처**: [arXiv 2606.04435 — Cascading Hallucination in Agentic RAG: The CHARM Framework](https://arxiv.org/abs/2606.04435) (2026-06-03 제출)

### Google Research — Cross-Corpus Retrieval: Gemini Enterprise Agent Platform Agentic RAG (2026-06-05)

Google Research와 Google Cloud가 2026년 6월 5일 발표. Gemini Enterprise Agent Platform에 Cross-Corpus Retrieval이 퍼블릭 프리뷰로 탑재됨.

**핵심 문제의식**: 표준 RAG는 단일 코퍼스 내 top-k 검색에 최적화되어 있어, 여러 데이터베이스에 분산된 정보를 멀티홉으로 조합해야 하는 복합 질의(cross-corpus retrieval)에서 성능이 낮다. "현재 수집된 컨텍스트가 충분한가"를 자체 평가하는 컴포넌트가 없기 때문이다.

**5개 전문 에이전트 구조**:
1. **Orchestrator** — 전체 에이전트 흐름 조율
2. **Planner** — 복잡한 쿼리를 서브 쿼리로 분해·계획 수립
3. **Query Rewriter** — 각 코퍼스에 최적화된 검색어 생성
4. **RAG Agent** — 지정된 코퍼스에서 실제 검색 수행
5. **Sufficient Context Agent** — 수집된 컨텍스트의 충분성 판단, 부족 시 재검색 트리거 (이 컴포넌트가 핵심 혁신)

**성능 수치**:
- 표준 RAG 대비 사실성 데이터셋 정확도 **+34%** 향상
- 4개 코퍼스 중 올바른 코퍼스 선택 정확도 **90.1%**

**적용 도메인 예시**: 의료팀(처방·식이·알레르기 세 DB 병합), 엔지니어링팀(서버 ID → 다른 DB의 사양서 추적), 금융팀(예산 데이터 + 일정 로그 조합).

**의의**: "검색한 정보가 충분한가"를 독립 에이전트로 분리한 설계 패턴이 핵심. 신뢰성 있는 Agentic RAG를 위해 "Sufficient Context"를 LLM 판단에 위임하지 않고 별도 컴포넌트로 제도화한 첫 상용 구현. Gemini Enterprise Agent Platform의 매니지드 서비스로 제공되어 직접 구축 없이 사용 가능.

- **출처**: [Google Research Blog — Unlocking dependable responses with Gemini Enterprise Agent Platform's Agentic RAG](https://research.google/blog/unlocking-dependable-responses-with-gemini-enterprise-agent-platforms-agentic-rag/) (2026-06-05, snippet-verified) · [MarkTechPost 커버리지](https://www.marktechpost.com/2026/06/08/google-research-adds-agentic-rag-to-gemini-enterprise-agent-platform-with-a-sufficient-context-agent-for-multi-hop-queries/)

### Bayesian Uncertainty Propagation for Agentic RAG — 베이즈 불확실성 전파 (arXiv:2607.00972, 2026-07-01)

멀티홉 질의 응답을 중심으로 에이전틱 RAG 파이프라인 전체의 불확실성을 추적·전파하는 proof-of-concept 프레임워크.

**핵심 문제의식**: 에이전틱 RAG 파이프라인에서 플래너(planner)·평가자(evaluator)·생성자(generator) 각 단계는 독립적으로 오류를 일으킬 수 있고, 이 오류가 다음 단계로 누적될 때 최종 출력의 신뢰도를 추정하기 어렵다. 기존 단순 confidence score는 단계 간 전파 메커니즘이 없어 시스템 레벨 품질 보증이 불가능하다.

**핵심 아이디어**:
1. 각 단계에서 **의미 발산(semantic divergence)** + **생성자 자기 평가(generator self-evaluation)**로 불확실성 신호를 생성
2. **베이즈 네트워크(Bayesian Network)**를 통해 단계별 불확실성을 시스템 레벨로 전파·집계
3. 최종적으로 전체 파이프라인의 시스템 레벨 불확실성 추정치 + 노드별 잠재 실패 지점 지표 도출

**실험 설정**: GPT-3.5-Turbo·GPT-4.1-Nano로 StrategyQA·HotpotQA 평가. 지표: AUROC, AUARC, ECE, Brier Score(판별력·선택적 예측·보정 전반).

**주요 결과**: HotpotQA(멀티홉)에서 베이즈 전파가 효과적 — 불확실성이 단계를 거치며 누적되는 패턴에서 강점 발휘. StrategyQA에서는 상류 신호의 오보정(miscalibration)이 한계로 작용. 연구진은 "promising but preliminary"로 규정, 오프쇼어 풍력(OSW) 등 산업 도메인 검증이 추가로 필요하다고 명시.

**의의**: 단계별 신뢰도 추적은 엔터프라이즈 에이전틱 RAG의 **관측성(observability) + 안전 게이팅** 강화의 다음 단계로 주목받는 연구 방향. CHARM 프레임워크(2606.04435)의 cascade hallucination 감지와 상호 보완적인 접근이다.

- **출처**: [arXiv:2607.00972 — Bayesian Uncertainty Propagation for Agentic RAG Pipelines: A Proof-of-Concept Study on Multi-Hop Question Answering](https://arxiv.org/abs/2607.00972) (2026-07-01, snippet-verified, arxiv abs + html 2개 출처)

### Context Graphs for Proactive Enterprise Agents — 반응형→선제형 RAG 아키텍처 전환 (arXiv:2607.07721, 2026-07)

표준 RAG·에이전틱 프레임워크가 본질적으로 **반응형(reactive)**—인간의 질의를 기다린 후 검색·응답—인 한계를 정면으로 비판하고, 엔터프라이즈 에이전트가 **선제적으로(proactively)** 컨텍스트를 인지하고 행동을 제안하는 아키텍처를 제안한다.

**핵심 구성 요소**:
1. **Context Graph**: 엔터프라이즈 엔티티(계약·인시던트·영업 기회 등), 관계, 상태 전이를 실시간으로 모델링하는 라이브 관계형 데이터 구조. NetworkX 기반 Python 구현.
2. **Delta Detection Engine**: 컨텍스트 그래프의 상태 변화를 모니터링하고 의미 있는 델타를 식별.
3. **Proactivity Scorer**: 발견된 변화를 긴급도·관련성·페르소나 적합성(urgency, relevance, persona-fit) 기준으로 순위화.
4. **Surfacing Layer**: LLM(Anthropic Claude API) 기반 랭킹 알림 생성 및 전달.

**성과**:
- Precision@5 = **0.83**, False Positive 비율 = **0.11**
- 컨텍스트 인지부터 알림까지 평균 시간: **47분 → 30초 미만**
- 평가 시나리오 3건: 계약 라이프사이클 관리, 엔지니어링 인시던트 대응, 영업 파이프라인 위생

**의의**: "RAG = 질의 응답"이라는 기존 프레임을 벗어나, 에이전트가 스스로 엔터프라이즈 상태 변화를 감지하고 관련 페르소나에게 선제적으로 알리는 패턴을 제시. MCP 서버가 엔터프라이즈 시스템 연결 표준으로 자리잡는 흐름과 결합하면, "MCP로 상태를 읽고 → Context Graph로 변화 감지 → 선제 알림"의 파이프라인이 현실적인 구현 경로가 된다.

- **저자**: Avinash Kumar
- **출처**: [arXiv:2607.07721 — Context Graphs for Proactive Enterprise Agents](https://arxiv.org/abs/2607.07721) (2026-07, cs.AI, cs.LG, snippet-verified, 복수 독립 출처)

### AgentKGV — 에이전틱 LLM-RAG 기반 지식 그래프 팩트 검증 (NAVER × 성균관대, arXiv:2607.09092, 2026-07-10) [한국 사례]

자동 구성된 대규모 지식 그래프(KG)에 포함된 사실 오류를 산업 규모에서 검증하는 에이전틱 LLM-RAG 프레임워크. NAVER(Hyeon-gu Lee, Sumin Seo)와 성균관대 NLP 연구실(Yumin Heo, Youngjoong Ko 교수)이 공동 개발했으며, NAVER 내부 한국 엔터프라이즈 KG 데이터셋으로 평가한 한국 산학협력 사례다.

**핵심 문제**: KG 트리플(엔티티-관계-엔티티)의 표면 표현이 검색 대상 문서 코퍼스의 자연어 표현과 불일치하는 **표면 표현 불일치(surface-form mismatch)** 문제. 단순 검색 기반 접근은 KG 표현과 문서 언어 사이의 간극을 처리하지 못해 정확한 팩트 검증이 불가능하다.

**두 가지 핵심 메커니즘**:
1. **Dynamic Routing**: 에이전트가 입력 트리플을 보고 파라메트릭 지식(내부 지식)으로 처리 가능한지, 외부 문서 검색이 필요한지를 먼저 판단해 불필요한 검색 호출을 차단.
2. **Iterative Query Rewriting**: 외부 검색이 필요하다고 판단되면 KG 트리플을 문서 수준 검색에 적합한 자연어 쿼리로 반복 변환하여 표현 불일치 극복.

**2단계 학습 전략**:
- **SFT (Turn-level Distillation)**: 대형 교사 모델의 추론 능력을 소형 모델로 지식 증류 — 안정적인 쿼리 재작성·추론 능력 확보.
- **GRPO (Trajectory-level RL)**: 검색 정책을 최적화해 불필요한 검색 호출 횟수를 줄이면서 F1을 향상시키는 효율 중심 강화학습.

**성과**: T-REx 표준 벤치마크(seen/unseen 두 분할)에서 모든 베이스라인 초과. **NAVER 한국 엔터프라이즈 KG**(언어·도메인·검색기가 다른 환경)에서도 가장 높은 Pos-F1·Macro-F1을 기록하여, 2단계 학습이 언어·도메인 무관하게 일반화됨을 실증.

**의의**: 동적 라우팅으로 불필요한 검색을 줄이고 반복 재작성으로 표현 간극을 극복하는 이 패턴은, 사내 지식 그래프·온톨로지를 운영하는 기업의 KG 품질 보증 자동화에 직접 적용 가능한 아키텍처. KG 팩트 검증이 단순 QA와 구별되는 고유 에이전틱 RAG 태스크임을 NAVER 산업 사례로 뒷받침한다.

- **저자**: Yumin Heo (성균관대), Hyeon-gu Lee (NAVER), Sumin Seo (NAVER), Youngjoong Ko (성균관대)
- **출처**: [arXiv:2607.09092 — AgentKGV: Agentic LLM-RAG Framework with Two-Stage Training for the Fact Verification of Knowledge Graphs](https://arxiv.org/abs/2607.09092) (2026-07-10, snippet-verified, arXiv abs + html + cs.CL listing 3개 독립 출처; NAVER 저자 소속 ResearchGate 확인)

### Salience Induction — 멀티홉 RAG 에이전트 대상 현저성 채널 공격과 방어 (arXiv:2607.17535, 2026-07-20)

멀티홉 RAG 에이전트에서 개별 사실이 모두 참인 상태에서도 **사실의 위치·강조·표현 방식(현저성 채널, salience channel)**을 조작해 에이전트 추론을 원하는 방향으로 유도하는 신규 공격 유형. 국방과학기술대학교(중국) Xingfu Zhou, Pengfei Wang, Yuan Zhou, Wei Xie, Xu Zhou 연구팀이 제안.

**문제**: 기존 RAG 보안 연구는 검색 오염(독성 문서 주입)이나 프롬프트 인젝션 두 가지 공격 면(attack surface)에 집중했다. Salience Induction은 **제3의 공격 면**을 정의한다 — 검색된 문서의 모든 주장이 사실이지만, 어떤 사실이 얼마나 두드러지는지(현저성)를 조절해 에이전트 추론 경로를 오염시킨다.

**핵심 기여**:
1. **6가지 Salience-Editing 연산자 클래스 정의**: 사실 위치(position), 강조(emphasis), 프레이밍(framing), 의미적 근접성(semantic proximity) 등 현저성 조작 방식을 체계적으로 분류.
2. **반복적 제안자-검증자 파이프라인(Iterative Proposer-Verifier Pipeline)**: 사실성(factual accuracy)과 스텔스(stealth) 제약 하에서 편집 예산(edit budget) 내 공격 시퀀스를 탐색.
3. **SalientWiki-MH 벤치마크**: 기만 주석(decoy annotation)이 포함된 멀티홉 평가 데이터셋 신규 구축.

**실험 결과**: 30% 편집 예산 내 **공격 성공률(ASR) 83.3%**; 가장 강한 방어 적용 후에도 **사후 방어 ASR 75.7%** — 현재 방어 기법으로 충분히 막기 어려움을 실증. GPT, Claude, Gemini, DeepSeek, Qwen 5개 프론티어 모델군 + ReAct, Reflexion, tool-calling 3가지 에이전트 아키텍처에서 일관되게 확인.

**의의**: "검색 결과가 사실이면 안전하다"는 전제를 무너뜨림. 멀티홉 RAG 에이전트 설계 시 현저성 조작에 대한 별도 방어 계층(사실 위치 무관 추론, 적대적 현저성 정규화 등)이 필요함을 시사. 에이전트 RAG의 신뢰성 평가 기준을 확장하는 연구.

- **저자**: Xingfu Zhou, Pengfei Wang, Yuan Zhou, Wei Xie, Xu Zhou (National University of Defense Technology, China)
- **출처**: [arXiv:2607.17535 — Salience Induction against Multi-Hop RAG Agents: Threat and Defense](https://arxiv.org/abs/2607.17535) (2026-07-20, snippet-verified, arXiv abs + cs.CR listing 2개 독립 출처)

### GRADRAG — 멀티에이전트 RAG 파이프라인 크로스-컴포넌트 프롬프트 적응 (arXiv:2607.21324, 2026-07-23)

멀티 에이전트 RAG 시스템에서 각 컴포넌트(검색기·그래프 구성기·답변 생성기)를 **격리해 최적화하는 기존 접근법**은 파이프라인 전체의 조율된 성능 향상을 이끌어내지 못한다는 문제를 해결하는 프레임워크. RAG 파이프라인을 **계산 그래프(computational graph)**로 모델링하고, 하류 평가 피드백을 역방향으로 전파해 상류 에이전트 프롬프트를 업데이트한다.

**핵심 아키텍처**:
1. **평가자(Evaluator)**: 하류 답변과 지지 증거를 비판적으로 검토하고, 구체적인 실행 가능 피드백(actionable feedback)을 생성.
2. **프롬프트 최적화기(Prompt Optimizer)**: 평가자의 피드백을 받아 검색기·그래프 구성기·답변 생성기 등 업스트림 적응형 에이전트(adaptive agents)의 프롬프트를 반복적으로 업데이트. 출력이 만족스러우면 조기 종료(early stopping) 신호를 발생시켜 불필요한 반복을 차단.
3. **계산 그래프 기반 역전파**: 컴포넌트 간 의존성을 그래프로 표현해 피드백이 어느 컴포넌트까지 전파되어야 하는지를 구조적으로 결정.

**평가**: SQUALITY(긴 문서 요약·QA) + QMSUM(회의 요약·QA) 두 벤치마크에서 **두 가지 검색 패러다임** 하에 평가.
  - 플랫 청크 기반 검색: IRCoT 스타일 쿼리 정제 방식.
  - 그래프 기반 검색: 엔티티-관계 그래프를 문서에서 구성하고 반복적으로 풍부화하는 방식.

**의의**: 기존 RAG 컴포넌트 최적화 연구가 개별 컴포넌트의 독립 튜닝에 집중한 것과 달리, GRADRAG는 파이프라인 전체를 하나의 계산 그래프로 보고 **컴포넌트 간 조율(cross-component coordination)**을 명시적으로 모델링한다. "평가자가 상류 컴포넌트 프롬프트를 직접 수정"하는 설계는 컴파일러 최적화의 데이터 흐름 분석과 유사한 발상으로, 멀티에이전트 RAG 자동 최적화의 새 방향을 제시한다.

- **저자**: Paolo Pedinotti, Enrico Santus
- **출처**: [arXiv:2607.21324 — GRADRAG: Cross-Component Prompt Adaptation for Coordinated Multi-Agent RAG](https://arxiv.org/abs/2607.21324) (2026-07-23, snippet-verified: arXiv abs + arXiv html + cs.CL listing + cs.AI listing 4개 독립 출처)

#### GRASP: GRanularity-Aware Search Policy for Agentic RAG (arXiv:2607.10463, 2026-07-11)
- **핵심 아이디어**: 에이전트 RAG에서 검색 액션의 **세분성(granularity)**을 동적으로 조절하는 강화학습(RL) 프레임워크. 에이전트가 semantic search, keyword search, paragraph reading 세 가지 검색 액션을 상황에 맞게 조율하도록 학습.
- **설계**:
  - 결합 보상(joint reward): 답변 정확도 + 근거 있는 읽기(grounded reading) + 보완적 검색(complementary search) + 턴 효율(turn efficiency).
  - 세분성 인식 정책(granularity-aware policy): 쿼리 복잡도·문서 구조에 따라 넓은 semantic search에서 좁은 paragraph-level reading으로 자동 전환.
  - 해석 가능한 스키밍/스캐닝 행동 학습 — 사람의 정보 검색 전략과 유사.
- **평가**: 단일 스텝·프롬프팅·RL 베이스라인 대비 멀티홉 QA 벤치마크에서 우위. 검색 효율과 답변 정확도 동시 개선.
- **의의**: 기존 에이전트 RAG 연구가 검색 횟수·도구 선택에 집중한 데 비해, GRASP는 각 검색 액션 내부의 세분성 레벨 자체를 정책의 결정 변수로 삼는다. "얼마나 깊이 읽을 것인가"를 RL로 학습하는 방향은 비용-정확도 트레이드오프 최적화에 새 차원을 추가한다.
- **저자**: Varun Gandhi, Jaewook Lee, Shantanu Todmal, Franck Dernoncourt, Ryan Rossi, Zichao Wang, Andrew Lan (UMass Amherst + Adobe Research)
- **출처**: [arXiv:2607.10463 — GRASP: GRanularity-Aware Search Policy for Agentic RAG](https://arxiv.org/abs/2607.10463) (2026-07-11, snippet-verified: arXiv abs + arXiv html + HuggingFace papers + ResearchGate + X post 5개 독립 출처)

### VecTree-RAG — 벡터+트리 이중 검색 기반 에이전틱 과학 문헌 QA (arXiv:2607.23006, 2026-07-25)

과학 문헌 QA에서 기존 RAG가 고정 길이 패시지로 문서 구조를 평탄화(flatten)해 "어떤 논문이 관련 있는가"와 "논문 내 어디에 증거가 있는가"를 모두 유사도 검색으로 처리하는 한계를 해결하는 에이전틱 RAG 프레임워크. **두 가지 질적으로 다른 검색 문제를 두 가지 상보적 메커니즘으로 분리 처리**하는 것이 핵심 설계 원칙.

**핵심 아키텍처**:
1. **벡터 검색(Vector Search)**: 문서 전체 표현과 섹션 수준 표현을 압축 벡터로 색인해 **코퍼스 전체에서 관련 논문을 랭킹**. raw 패시지를 임베딩하지 않아 인덱스 크기를 문서 구조 엔트리 수에만 비례하게 제어.
2. **트리 순회(Tree Traversal)**: 소스 검증된 섹션 트리를 **추론 기반으로 순회해 단축리스트된 논문 내부에서 증거를 정밀 위치 파악**. 전체 원문은 페이지 스토어에 보존, 구조적 위치 파악 이후 점진적으로만 노출.

**평가 결과**: 기존 Dense RAG·RAPTOR·Search-o1 등 베이스라인 대비 3개 벤치마크 최고 성능:
- QASPER(300개 질의): LLM-judge 정답률 **0.800** (Dense RAG 대비 증거 페이지 정밀도 0.274 vs 0.046~0.071)
- LitQA2(54개 질의, 오픈 액세스): 정확도 **0.925**
- MOSAIC(49개 멀티문서 질의): 복합 점수 **0.547**

**효율성**: LitQA2 절제 실험에서 트리 탐색 또는 코퍼스 수준 벡터 라우팅 없이는 더 많은 추론 토큰 필요 — 두 메커니즘이 상호 보완적임을 확인.

**의의**: "문서 관련성 판별"과 "문서 내 증거 위치 파악"을 단일 유사도 검색으로 처리하는 기존 패러다임 한계를 명시하고, 각각에 맞는 전문 메커니즘을 조합하는 설계를 제안. 계층적 구조(섹션·챕터)를 가진 긴 문서 코퍼스 전반에 일반화 가능.

- **저자**: Xinyan Zhong, Yuwei Shi, Yuqi Wei, Chen Shen, Tianhang Zhou, Zhenghao Wu (Xi'an Jiaotong-Liverpool University [XJTLU] · Suzhou Lab · China University of Petroleum)
- **출처**: [arXiv:2607.23006 — VecTree-RAG: An Agentic Retrieval-Augmented Generation Framework Combining Vector and Tree Retrieval for Efficiency and Accuracy](https://arxiv.org/abs/2607.23006) (2026-07-25, snippet-verified: arXiv abs + arXiv html 2개 독립 출처)

### CMT-RAG — 멀티턴 멀티홉 RAG의 상호보완적 메모리 추적 (arXiv:2607.26470, 2026-07-29)

멀티턴 대화에서 **멀티홉 추론**과 **장거리 의존성 추적**이 동시에 필요한 시나리오에서, 기존 RAG가 원시 대화 이력(raw dialogue history)에 의존해 교차-턴 서브 질문 의존성을 처리하지 못하는 한계를 해결하는 프레임워크.

**핵심 아이디어**: 대화 컨텍스트를 원시 이력 대신 **서브 질문 수준의 추론 추적(sub-question-level reasoning traces)**으로 표현하는 "상호보완적 메모리 추적(Complementary Memory Traces, CMT)"을 도입.

**핵심 기여**:
1. **CMT**: 각 대화 턴의 멀티홉 추론 과정을 서브 질문 단위로 분해·추적하여 컨텍스트로 활용. 원시 대화 이력이 아닌 구조화된 추론 경로를 메모리로 유지.
2. **MuMu-QA 벤치마크**: 교차-턴 서브 질문 의존성 주석(explicit cross-turn sub-question dependency annotations)을 포함한 신규 멀티턴 멀티홉 QA 벤치마크. 기존 멀티턴 QA 벤치마크의 교차-턴 의존성 평가 공백을 메움.

**저자**: Lang Zhou, Yingjian Chen, Shuxuan Li, Kun-Yu Lin, Zhilin Zhao

**의의**: 멀티턴 대화 RAG에서 "대화 이력을 어떻게 표현·압축할 것인가"가 핵심 병목임을 정면으로 다루는 연구. 교차-턴 서브 질문 의존성을 명시적으로 모델링하는 방향은 장기 대화 RAG 에이전트의 컨텍스트 관리 설계에 직접 영향을 준다.

- **출처**: [arXiv:2607.26470 — CMT-RAG: Complementary Memory Traces for Multi-turn Multi-hop RAG](https://arxiv.org/abs/2607.26470) (2026-07-29, snippet-verified: arXiv abs + arXiv html 2개 독립 출처)

### LayerRAG-Bench — 에이전틱 RAG 계층별 신뢰성 벤치마크 (arXiv:2607.27353, 2026-07-29)

에이전틱 RAG 시스템이 **증거 계층(evidence layer)·도구 계약 계층(tool-contract layer)·권한 계층(authorization layer)·세션 상태 계층(session-state layer)** 각각에서 별도로 실패할 수 있음을 체계적으로 정의하고, 계층 교차 신뢰성 벤치마크로 실증한 논문.

**핵심 문제의식**: 에이전틱 RAG가 표면적으로는 근거(grounded) 답변처럼 보이면서도 아래 계층에서 조용히 실패하는 "은폐된 실패 모드"를 기존 평가 방법이 탐지하지 못한다. 특히 groundedness-only 평가(출력에 인용이 있는가)는 stale 증거나 wrong-session 컨텍스트 조건에서 **상당한 위양성(false positive)**을 생성한다.

**벤치마크 설계**:
- 8개 엔터프라이즈 도메인, 240개 태스크, **9개 장애 시나리오(fault scenarios)**
- 2가지 계약 모드(contract modes)
- **38,880개의 실시간 태스크 레벨 레코드**
- OpenAI·Anthropic·Gemini 9개 모델 평가

**핵심 발견**:
1. **스키마 정규화(schema normalization)**: schema-drift 성공률 0.000 → **0.913**으로 극적 개선. 그러나 이 수정은 오직 schema-drift 장애에만 효과적.
2. **스키마 정규화로 회복 불가능한 장애**: stale 증거, 도구 출력 누락(missing tool output), 권한 거부(denied permissions), wrong-session 컨텍스트 — 이 4가지는 스키마 수정으로 해결되지 않음.
3. **계층별 평가 원칙**: 신뢰성 개입(reliability intervention)은 자신이 수리하는 목표 계층에 대해서만 공로를 인정받아야 하며, 범용 수정처럼 취급해서는 안 된다.

**저자**: Musa Shams (Independent Researcher; LinkedIn: EY Data Engineer, Applied AI/RAG 전문가)

**의의**: 에이전틱 RAG에서 "그라운딩(grounding)이 있으면 신뢰할 수 있다"는 단순 가정이 시스템 수준에서 틀릴 수 있음을 8개 도메인·38,880 레코드 규모로 실증. 엔터프라이즈 에이전틱 RAG 배포 시 **계층별 독립 평가**를 신뢰성 검증의 표준 단계로 편입해야 한다는 실무 원칙을 1차 자료로 뒷받침. 코드·데이터: GitHub [MusaShams/layerrag-bench](https://github.com/MusaShams/layerrag-bench).

- **출처**: [arXiv:2607.27353 — LayerRAG-Bench: A Cross-Layer Reliability Benchmark for Agentic Retrieval-Augmented Generation](https://arxiv.org/abs/2607.27353) (2026-07-29, snippet-verified: arXiv abs + arXiv html + LinkedIn Musa Shams(EY) 3개 독립 출처)

---

## 이 도메인의 공통 패턴

1. **"Retrieval = tool"의 일반화**. vector search든 SQL이든 web이든, LLM이 호출할 수 있는 함수로 노출하는 게 표준. MCP가 이 표준의 wire format.
2. **하이브리드가 default**. dense + BM25 + reranker + (필요시) graph. 어느 한 retrieval만 쓰는 production은 거의 없다.
3. **MCP 서버화**가 사내 지식 통합의 기본 단위. Atlassian Rovo, Salesforce Hosted MCP가 GA. 사내에서도 "이 시스템에 MCP server를 만들자"가 첫 질문.
4. **메모리는 별도 인프라 컴포넌트**. Mem0·Letta·Anthropic memory tool 중 하나. 이걸 안 쓰고 conversation history만 쓰면 long-horizon task에서 무조건 무너진다.
5. **agentic search vs embedding search**는 use case 따라 선택. 코드는 agentic(grep) 우위, 문서는 embedding 우위.
6. **per-turn retrieval cap + confidence-based stopping**이 production 안정성의 분기점.
7. **Long context는 fallback, RAG는 default**. 비용·정확도 모두 RAG가 우위인 워크로드가 다수.

## 자주 보이는 실패 모드

towardsdatascience agentic RAG failure modes, tensoria.fr, promptql.io 종합:

- **Retrieval thrash** — 답을 못 찾고 비슷한 쿼리를 반복. 토큰 폭발. 해결: hard cap + duplicate query 감지 + confidence stop.
- **Tool storm** — 한 턴에 수십 개 tool을 부르는 폭주. 해결: per-turn tool call cap + budget.
- **Context bloat** — 중간 결과를 전부 컨텍스트에 쌓아 모델이 길을 잃음. 해결: filesystem-based MCP (Anthropic 패턴), observation summarization.
- **Semantic drift** — 반복 reformulation 중 원래 의도와 멀어짐. 해결: 매 iteration마다 원본 쿼리를 함께 보존.
- **Non-determinism** — 같은 입력에 다른 결과. evaluation·debugging이 매우 어려움. 해결: tracing(LangSmith·Helicone·Phoenix) + replay.
- **Multi-hop 가정 오류** — 사실 90%는 single lookup이면 충분한데 agentic을 깔아둔 경우. 해결: workload 분석 먼저, agentic은 multi-hop 비율 15%+ 일 때만.
- **Memory leak / unbounded** — Letta·Mem0 사용 시 archival memory가 무한히 누적. 해결: TTL·retention policy.
- **MCP 보안** — 잘못된 MCP server가 prompt injection 벡터. 해결: server allow-list, OAuth/identity 기반 접근 통제, Salesforce처럼 enterprise MCP registry로 정책 강제.
- **"agentic 만능주의"** — 비용 5~10배 들여서 정확도 5%p 개선하는 경우가 흔함. 해결: hybrid search + reranker로 먼저 baseline 끌어올린 뒤, 남는 hard query에만 agentic 적용.

## 참조 논문 (2026년 누적)

### arXiv 2603.07379 — SoK: Agentic RAG (2026-03)

- **논문**: *SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions* (arXiv 2603.07379, 제출 2026-03-07)
- **핵심 기여**: Agentic RAG를 **유한 수평 부분 관측 마르코프 결정 과정(finite-horizon POMDP)**으로 형식화한 최초의 체계적 지식(SoK) 논문. 제어 정책과 상태 전이를 명시적으로 모델링.
- **분류 체계**: 에이전트 위상(단일 에이전트 RAG / 플래너-실행자 아키텍처 / 멀티 에이전트 RAG 시스템), 계획 전략, 검색 오케스트레이션, 메모리 패러다임, 툴 조정 메커니즘의 5축 분류.
- **주요 지적**: 빠른 산업 채택에도 불구하고 (1) 일관된 평가 방법론 부재, (2) 아키텍처 파편화, (3) 신뢰성 리스크 미해결이 세 가지 핵심 공백으로 남아 있음.
- **실무 시사점**: 이 도메인에서 이미 관찰되는 실패 모드(retrieval thrash·context bloat·multi-hop 가정 오류)를 POMDP 제어 문제로 재구성하면, per-turn cap·confidence-based stopping이 결국 정책 제약(policy constraint)임을 체계적으로 설명할 수 있다.
- **출처**: [arXiv 2603.07379](https://arxiv.org/abs/2603.07379)
