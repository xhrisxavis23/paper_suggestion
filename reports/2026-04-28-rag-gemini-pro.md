# Research Topic Suggestion — "rag"

생성: 2026-04-28T07:30:14.717983+00:00
DB 윈도우: 2026-02-27 ~ 2026-04-28 (60d)
모델: gemini-2.5-pro
매칭 논문: 200건
확장 키워드: ['Retrieval-Augmented Generation', 'RAG model', 'retrieval augmented language model', 'retrieval based generation', 'knowledge grounding for LLMs', 'external knowledge retrieval', 'vector search for generation', 'dense passage retrieval', 'generative question answering']

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — 지식그래프 및 구조적 검색
- **설명**: 단순 텍스트 검색을 넘어 지식그래프(KG), 하이퍼그래프 등 구조화된 데이터를 활용하여 다중 홉(multi-hop) 추론 및 의미 관계에 기반한 검색 정확도를 높이는 연구 클러스터입니다.
- **빈도**: 13건
- **월별 (≈15d씩, 오래된→최근)**: 1 → 3 → 4 → 5
- **대표 논문**:
  - [P-2604.22282] STEM: Structure-Tracing Evidence Mining for Knowledge Graphs-Driven Retrieval-Augmented Generation — Peng Yu, En Xu, Bin Chen et al., arXiv 2026
  - [P-2604.12185] Knowledge Is Not Static: Order-Aware Hypergraph RAG for Language Models — Keshu Wu, Chenchen Kuai, Zihao Li et al., arXiv 2026
  - [P-2506.17001] PersonalAI: A Systematic Comparison of Knowledge Graph Storage and Retrieval Approaches for Personalized LLM agents — Mikhail Menschikov, Dmitry Evseev, Victoria Dochkina et al., HF 2026

### 클러스터 2 — RAG 에이전트 및 멀티에이전트
- **설명**: LLM을 도구 사용, 동적 계획, 자가 교정이 가능한 '에이전트'로 활용하여 복잡한 질문을 해결하는 연구입니다. 여러 전문 에이전트가 협력하거나 토론하는 멀티에이전트 시스템을 통해 문제 해결 능력을 극대화합니다.
- **빈도**: 10건
- **월별 (≈15d씩, 오래된→최근)**: 3 → 2 → 1 → 4
- **대표 논문**:
  - [P-2604.17405] STRIDE: Strategic Iterative Decision-Making for Retrieval-Augmented Multi-Hop Question Answering — Wei Chen, Lili Zhao, Zhi Zheng et al., arXiv 2026
  - [P-2603.28488] Courtroom-Style Multi-Agent Debate with Progressive RAG and Role-Switching for Controversial Claim Verification — Masnun Nuha Chowdhury, Nusrat Jahan Beg, Umme Hunny Khan et al., arXiv 2026
  - [P-2604.00901] Experience as a Compass: Multi-agent RAG with Evolving Orchestration and Agent Prompts — Sha Li, Naren Ramakrishnan, arXiv 2026

### 클러스터 3 — RAG 평가, 강건성, 보안
- **설명**: RAG 시스템의 성능을 체계적으로 측정하기 위한 벤치마크를 구축하고, 환각(hallucination) 현상을 탐지 및 완화하며, 데이터 포이즈닝이나 정보 유출과 같은 적대적 공격에 대한 방어 기술을 연구합니다.
- **빈도**: 17건
- **월별 (≈15d씩, 오래된→최근)**: 4 → 3 → 4 → 6
- **대표 논문**:
  - [P-2604.18663] Beyond Explicit Refusals: Soft-Failure Attacks on Retrieval-Augmented Generation — Wentao Zhang, Yan Zhuang, ZhuHang Zheng et al., arXiv 2026
  - [P-2604.18584] MathNet: a Global Multimodal Benchmark for Mathematical Reasoning and Retrieval — Shaden Alshammari, Kevin Wen, Abrar Zainal et al., arXiv 2026
  - [P-2604.08304] Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions — Yuming Xu, Mingtao Zhang, Zhuohan Ge et al., arXiv 2026

### 클러스터 4 — 도메인 특화 RAG 응용
- **설명**: 의료, 법률, 금융, 사이버 보안, 통신 등 특정 전문 분야의 데이터를 활용하여 RAG 시스템을 구축하는 연구입니다. 해당 분야의 고유한 데이터 형식과 추론 방식을 처리하는 데 중점을 둡니다.
- **빈도**: 14건
- **월별 (≈15d씩, 오래된→최근)**: 5 → 2 → 4 → 3
- **대표 논문**:
  - [P-2604.22061] Lightweight Retrieval-Augmented Generation and Large Language Model-Based Modeling for Scalable Patient-Trial Matching — Xiaodi Li, Yang Xiao, Munhwan Lee et al., arXiv 2026
  - [P-2604.11419] Beyond RAG for Cyber Threat Intelligence: A Systematic Evaluation of Graph-Based and Agentic Retrieval — Dzenan Hamzic, Florian Skopik, Max Landauer et al., arXiv 2026
  - [P-2604.14222] Adaptive Query Routing: A Tier-Based Framework for Hybrid Retrieval Across Financial, Legal, and Medical Documents — Afshan Hashmi, arXiv 2026

### 클러스터 5 — RAG 파이프라인 요소 최적화
- **설명**: RAG 시스템을 구성하는 개별 요소 기술을 심도 있게 연구합니다. 문서 분할(chunking), 검색 결과 재순위화(reranking), 사용자 질의 변환 및 라우팅(query transformation/routing) 등을 최적화하여 효율과 성능을 높입니다.
- **빈도**: 10건
- **월별 (≈15d씩, 오래된→최근)**: 2 → 3 → 2 → 3
- **대표 논문**:
  - [P-2603.25333] Adaptive Chunking: Optimizing Chunking-Method Selection for RAG — Paulo Roberto de Moura Júnior, Jean Lelong, Annabelle Blangero, arXiv 2026
  - [P-2604.22661] Can QPP Choose the Right Query Variant? Evaluating Query Variant Selection for RAG Pipelines — Negar Arabzadeh, Andrew Drozdov, Michael Bendersky et al., arXiv 2026
  - [P-2604.02091] Optimizing RAG Rerankers with LLM Feedback via Reinforcement Learning — Yuhang Wu, Xiangqing Shen, Fanfan Wang et al., arXiv 2026

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap B — 다수의 RAG 연구들이 공통적으로 높은 계산 비용과 지연 시간(latency)을 한계로 지적하고 있습니다. 특히 에이전트 기반의 다단계 추론, 
- **타입**: recurring-limitation
- **설명**: 다수의 RAG 연구들이 공통적으로 높은 계산 비용과 지연 시간(latency)을 한계로 지적하고 있습니다. 특히 에이전트 기반의 다단계 추론, 복잡한 쿼리 재구성, 대규모 문서 처리 파이프라인은 상당한 계산 자원을 소모합니다. 이는 RAG 시스템의 실용성과 확장성을 저해하는 핵심적인 병목 현상으로, 여러 논문에서 이를 완화하려는 시도가 이루어지고 있으나 여전히 근본적인 문제로 남아있습니다.
- **근거 논문**: P-2604.22661, P-2604.22061, P-2604.20452, P-2604.17337
- **Skeptic 검토**: ✓ 통과 — 여러 클러스터의 증거 논문들이 공통적으로 계산 비용을 핵심 한계로 명시하고 있으며, 제안된 해결책들은 부분적인 완화에 그쳐 효율성이 RAG 시스템의 실용화를 막는 근본적인 문제로 남아있음을 인정합니다.

### Gap D — 대부분의 RAG 시스템은 LLM이 비정형 텍스트를 처리하는 능력에 의존하지만, 일부 연구에서는 신경망-기호(Neuro-Symbolic) 접근법을
- **타입**: between-clusters
- **설명**: 대부분의 RAG 시스템은 LLM이 비정형 텍스트를 처리하는 능력에 의존하지만, 일부 연구에서는 신경망-기호(Neuro-Symbolic) 접근법을 통해 LLM의 한계를 보완하려 시도합니다. 이는 비정형적인 임상 가이드라인의 논리적 모순을 기호 논리로 변환하여 검증한 후 RAG를 적용하는 것과 같은 방식입니다. 그러나 이러한 접근법은 아직 소수의 논문에서만 탐색되고 있으며, 기호적 추론을 RAG 파이프라인에 체계적으로 통합하는 연구는 주류를 이루지 못하고 있습니다.
- **근거 논문**: P-2604.17340, P-2604.10114
- **Skeptic 검토**: ✓ 통과 — 제시된 증거들은 표준 RAG의 한계를 지적하며 기호 논리 기반 검증을 새로운 패러다임으로 제시합니다. 데이터베이스 내 압도적인 다수의 논문이 순수 신경망 기반 접근법을 따르는 것을 볼 때, 신경-기호 통합이 아직 비주류이며 체계적으로 연구되지 않은 영역이라는 주장은 타당합니다.

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap A** — RAG 시스템의 성능 평가는 주로 일반적인 QA 벤치마크에 의존하고 있어, 법률, 금융, 특허 등 현실 세계의 전문 분야에서 나타나는 고유한 문제를 제대로 반영하지 못합니다. 이들 분야의 문서는 정보가 중복되고 문서 간 유사성이 매우 높아, 기존 평가 방식으로는 검색기의 성능을 올바르게 측정하기 어렵습니다. 특정 도메인에 특화된, 현실적인 평가 프레임워크 구축에 대한 연구가 부족한 상황입니다. · 거부 사유: (a) 다른 클러스터에서 이미 다룸
- **Gap C** — RAG 시스템에 대한 보안 연구는 주로 데이터 파이프라인(검색, 생성 단계)의 취약점에 집중되어 있습니다. 반면, 도구 사용, 동적 계획, 장기 기억을 가진 '에이전트' 시스템이 노출하는 새로운 공격 표면에 대한 연구는 상대적으로 미흡합니다. 에이전트의 의사결정 과정을 조작하거나, 도구 사용을 오염시키거나, 다중 에이전트 간의 통신을 공격하는 등 에이전트 고유의 취약점을 다루는 보안 프레임워크가 부재합니다. · 거부 사유: (a) 다른 클러스터에서 이미 다룸

</details>

## 3. 연구 제안 (Proposer)

### 제안 1 — PRE-FLIGHT
**가설**: 쿼리의 복잡도를 사전에 예측하여 정적 파이프라인(단순 검색)과 동적 에이전트 파이프라인(다단계 추론) 중 가장 비용 효율적인 실행 경로를 동적으로 선택하면, 전체 시스템의 평균 지연 시간과 비용을 크게 줄일 수 있다.
**메우는 갭**: B
**접근**: 사용자 쿼리를 입력받아 '단순 사실 확인', '비교 분석', '다단계 추론' 등의 유형으로 분류하는 경량 라우터 모델을 학습시킵니다. 각 쿼리 유형에 미리 정의된 최적의 RAG 파이프라인(예: 단순 Vector RAG, 또는 STRIDE와 같은 에이전트 시스템)을 매핑하여 실행합니다. 이를 통해 모든 쿼리에 고비용 에이전트 시스템을 적용하는 비효율을 제거하고, 계산 리소스를 차등적으로 할당합니다.
**Baselines**: AutoSearch, STRIDE, Vector RAG, Tree Reasoning
**예상 기여**: 모든 쿼리에 일률적으로 고비용 파이프라인을 적용하는 대신, 쿼리 유형에 따라 계산 리소스를 적응적으로 할당하는 프레임워크를 제안합니다. 이는 시스템 전체의 처리량과 비용 효율성을 극대화하여, 복잡한 RAG 시스템의 실용성을 높이는 데 기여할 것입니다.
**참고**: P-2604.17337, P-2604.17405, P-2604.22661, P-2604.03455, P-2604.14222

### 제안 2 — LOGIC-RAG
**가설**: 검색된 비정형 텍스트를 LLM을 이용해 정형화된 논리적 주장(atomic claims)으로 변환하고, 기호적 추론기(symbolic reasoner)를 통해 이들의 일관성을 검증하며 새로운 사실을 추론한 후 생성 모델에 전달하면, 환각을 줄이고 사실적 일관성이 높은 응답을 생성할 수 있다.
**메우는 갭**: D
**접근**: 먼저 표준 RAG로 관련 문서를 검색한 후, LLM을 이용해 검색된 내용에서 논리적 주장들을 추출합니다. 이 주장들을 기호 논리(symbolic logic) 형식으로 변환하여 지식베이스를 구축하고, SAT 솔버나 논리 프로그래밍 엔진으로 모순을 탐지하고 새로운 사실을 추론합니다. 최종적으로, 검증되고 확장된 이 지식베이스를 생성 모델의 컨텍스트로 사용하여 답변을 생성합니다.
**Baselines**: ArbGraph, Neuro-Symbolic Resolution, CircuitSynth
**예상 기여**: 검색과 생성 단계 사이에 명시적인 '기호적 검증 및 추론' 단계를 도입합니다. 이는 LLM의 유연한 자연어 처리 능력과 기호 시스템의 엄밀한 논리적 추론 능력을 결합하여, 특히 상충되거나 복잡한 정보를 다룰 때 RAG 시스템의 신뢰성을 획기적으로 향상시킬 것입니다.
**참고**: P-2604.17340, P-2604.18362, P-2604.10114

### 제안 3 — PRO-FETCH
**가설**: 다단계 추론 과정에서 현재 단계의 검색 결과를 바탕으로 다음 단계에 필요할 가능성이 높은 정보를 예측하여 미리 검색(prefetching)하면, 추론과 검색을 병렬화하여 전체 지연 시간을 단축시킬 수 있다.
**메우는 갭**: B
**접근**: 다단계 에이전트 RAG 프레임워크 내에서, 에이전트가 첫 검색 결과를 처리하고 다음 쿼리를 생성하는 동안, 별도의 '프리페처(Prefetcher)' 모듈이 첫 검색 결과에 포함된 주요 엔티티들을 기반으로 연관 문서를 미리 검색합니다. 에이전트가 다음 쿼리를 확정하면, 프리페칭된 문서 풀에서 즉시 결과를 제공받거나, 없다면 그때 정식 검색을 수행합니다. 이 방식은 HaS의 투기적 검색 아이디어를 다단계 추론 파이프라인에 적용한 것입니다.
**Baselines**: HaS, STRIDE, ReAct
**예상 기여**: 순차적으로 수행되던 검색-추론 사이의 유휴 시간을 활용하여, 복잡한 다단계 질의응답 시스템의 응답 속도를 개선합니다. 이는 지연 시간이 중요한 대화형 에이전트나 실시간 분석 시스템의 실용성을 높이는 데 기여할 것입니다.
**참고**: P-2604.20452, P-2604.17405, P-2604.01413

### 제안 4 — SYMPLAN-RAG
**가설**: LLM 에이전트가 자유로운 자연어 대신 'RETRIEVE(entity)', 'FILTER(criteria)', 'SYNTHESIZE(doc1, doc2)'와 같은 사전 정의된 기호적 연산자(symbolic operators)로 구성된 실행 계획을 생성하도록 제어하면, 추론 과정의 투명성과 재현성을 높이고 치명적인 논리적 오류를 줄일 수 있다.
**메우는 갭**: D
**접근**: STRIDE 프레임워크에서 영감을 받아, Meta-Planner가 자연어 추론 경로 대신 기호적 연산자로 구성된 계획 트리를 생성하도록 합니다. 생성된 계획은 Supervisor에 의해 해석되고, 각 연산자는 벡터 검색기나 키워드 필터와 같은 결정론적 도구 호출에 매핑됩니다. LLM은 계획 생성에만 관여하고 실행은 도구에 의해 수행되어 전체 프로세스의 신뢰성을 확보합니다.
**Baselines**: STRIDE, GraphWalk, ReAct, Tri-RAG
**예상 기여**: 에이전트의 추론 과정을 비결정적인 자연어 생성에서 검증 가능한 기호적 계획 실행으로 전환합니다. 이는 RAG 에이전트의 '환각' 문제를 계획 단계에서부터 원천적으로 억제하고, 전체 추론 과정을 감사 및 디버깅하기 쉽게 만들어 고신뢰성 도메인에서의 적용 가능성을 높입니다.
**참고**: P-2604.17405, P-2604.01610, P-2604.12610, P-2604.17340

### 제안 5 — RAG-DISTILL
**가설**: 복잡하고 여러 단계로 구성된 고성능 RAG 파이프라인(교사)의 최종 출력을 사용하여 단일 경량 모델(학생)을 미세 조정(fine-tuning)하면, 계산 비용과 지연 시간을 크게 줄이면서도 교사 모델의 성능에 근접할 수 있다.
**메우는 갭**: B
**접근**: 먼저, 다단계 쿼리 확장 및 재순위화를 포함하는 복잡한 '교사' RAG 파이프라인을 구축합니다. 대규모 질문 데이터셋을 이 교사 파이프라인에 통과시켜 고품질의 (검색된 증거, 최종 답변) 쌍으로 구성된 학습 데이터를 생성합니다. 마지막으로, 이 데이터를 사용하여 검색된 증거를 컨텍스트로 받아 답변을 생성하는 단일 '학생' LLM을 미세 조정합니다.
**Baselines**: AdaRankLLM, HotpotQA, MuSiQue, LLaMA-3, GPT-4o
**예상 기여**: 다단계 RAG 파이프라인의 높은 추론 비용 문제를 해결하기 위한 실용적인 지식 증류 프레임워크를 제안합니다. 이를 통해 고성능 RAG 시스템의 능력을 계산 자원이 제한된 환경에서도 배포 가능한 경량 모델로 효과적으로 이전하는 경로를 제시합니다.
**참고**: P-2604.15621, P-2604.22661, P-2604.22061, P-2604.22095

## 4. 참고문헌 (메타DB 기반)

### 클러스터 1 — 지식그래프 및 구조적 검색 (13)
- [P-2604.22282] STEM: Structure-Tracing Evidence Mining for Knowledge Graphs-Driven Retrieval-Augmented Generation, Peng Yu, En Xu, Bin Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.22282v1
- [P-2506.17001] PersonalAI: A Systematic Comparison of Knowledge Graph Storage and Retrieval Approaches for Personalized LLM agents, Mikhail Menschikov, Dmitry Evseev, Victoria Dochkina et al., HF 2026 · https://huggingface.co/papers/2506.17001 · also_in: arxiv
- [P-2604.17458] EHRAG: Bridging Semantic Gaps in Lightweight GraphRAG via Hybrid Hypergraph Construction and Retrieval, Yifan Song, Xingjian Tao, Zhicheng Yang et al., arXiv 2026 · http://arxiv.org/abs/2604.17458v2
- [P-2604.12610] Transforming External Knowledge into Triplets for Enhanced Retrieval in RAG of LLMs, Xudong Wang, Chaoning Zhang, Qigan Sun et al., arXiv 2026 · http://arxiv.org/abs/2604.12610v1
- [P-2604.12185] Knowledge Is Not Static: Order-Aware Hypergraph RAG for Language Models, Keshu Wu, Chenchen Kuai, Zihao Li et al., arXiv 2026 · http://arxiv.org/abs/2604.12185v1
- [P-2604.04359] GROUNDEDKG-RAG: Grounded Knowledge Graph Index for Long-document Question Answering, Tianyi Zhang, Andreas Marfurt, arXiv 2026 · http://arxiv.org/abs/2604.04359v1
- [P-2604.18362] ArbGraph: Conflict-Aware Evidence Arbitration for Reliable Long-Form Retrieval-Augmented Generation, Qingying Niu, Yuhao Wang, Ruiyang Ren et al., arXiv 2026 · http://arxiv.org/abs/2604.18362v1
- [P-2604.12766] NaviRAG: Towards Active Knowledge Navigation for Retrieval-Augmented Generation, Jihao Dai, Dingjun Wu, Yuxuan Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.12766v1
- [P-2604.08256] HyperMem: Hypergraph Memory for Long-Term Conversations, Juwei Yue, Chuanrui Hu, Jiawei Sheng et al., arXiv 2026 · http://arxiv.org/abs/2604.08256v2
- [P-2604.10426] CodaRAG: Connecting the Dots with Associativity Inspired by Complementary Learning, Cheng-Yen Li, Xuanjun Chen, Claire Lin et al., arXiv 2026 · http://arxiv.org/abs/2604.10426v1
- [P-2604.04969] MG$^2$-RAG: Multi-Granularity Graph for Multimodal Retrieval-Augmented Generation, Sijun Dai, Qiang Huang, Xiaoxing You et al., arXiv 2026 · http://arxiv.org/abs/2604.04969v1
- [P-2603.25152] UniAI-GraphRAG: Synergizing Ontology-Guided Extraction, Multi-Dimensional Clustering, and Dual-Channel Fusion for Robust Multi-Hop Reasoning, Jie Wang, Honghua Huang, Xi Ge et al., arXiv 2026 · http://arxiv.org/abs/2603.25152v2
- [P-2604.18478] WorldDB: A Vector Graph-of-Worlds Memory Engine with Ontology-Aware Write-Time Reconciliation, Harish Santhanalakshmi Ganesan, arXiv 2026 · http://arxiv.org/abs/2604.18478v1

### 클러스터 2 — RAG 에이전트 및 멀티에이전트 (10)
- [P-2604.17405] STRIDE: Strategic Iterative Decision-Making for Retrieval-Augmented Multi-Hop Question Answering, Wei Chen, Lili Zhao, Zhi Zheng et al., arXiv 2026 · http://arxiv.org/abs/2604.17405v1
- [P-2604.17337] AutoSearch: Adaptive Search Depth for Efficient Agentic RAG via Reinforcement Learning, Jingbo Sun, Wenyue Chong, Songjun Tu et al., arXiv 2026 · http://arxiv.org/abs/2604.17337v1
- [P-2604.18509] MASS-RAG: Multi-Agent Synthesis Retrieval-Augmented Generation, Xingchen Xiao, Heyan Huang, Runheng Liu et al., arXiv 2026 · http://arxiv.org/abs/2604.18509v2
- [P-2603.28488] Courtroom-Style Multi-Agent Debate with Progressive RAG and Role-Switching for Controversial Claim Verification, Masnun Nuha Chowdhury, Nusrat Jahan Beg, Umme Hunny Khan et al., arXiv 2026 · http://arxiv.org/abs/2603.28488v1
- [P-2604.09508] VISOR: Agentic Visual Retrieval-Augmented Generation via Iterative Search and Over-horizon Reasoning, Yucheng Shen, Jiulong Wu, Jizhou Huang et al., arXiv 2026 · http://arxiv.org/abs/2604.09508v1
- [P-2603.27910] GAAMA: Graph Augmented Associative Memory for Agents, Swarna Kamal Paul, Shubhendu Sharma, Nitin Sareen, arXiv 2026 · http://arxiv.org/abs/2603.27910v1
- [P-2604.00901] Experience as a Compass: Multi-agent RAG with Evolving Orchestration and Agent Prompts, Sha Li, Naren Ramakrishnan, arXiv 2026 · http://arxiv.org/abs/2604.00901v2
- [P-2604.07645] PRIME: Training Free Proactive Reasoning via Iterative Memory Evolution for User-Centric Agent, Prince Zizhuang Wang, Shuli Jiang, arXiv 2026 · http://arxiv.org/abs/2604.07645v1
- [P-2604.07146] Learning to Search: A Decision-Based Agent for Knowledge-Based Visual Question Answering, Zhuohong Chen, Zhenxian Wu, Yunyao Yu et al., arXiv 2026 · http://arxiv.org/abs/2604.07146v2
- [P-2604.14572] Don't Retrieve, Navigate: Distilling Enterprise Knowledge into Navigable Agent Skills for QA and RAG, Yiqun Sun, Pengfei Wei, Lawrence B. Hsieh, arXiv 2026 · http://arxiv.org/abs/2604.14572v1 · also_in: hf

### 클러스터 3 — RAG 평가, 강건성, 보안 (17)
- [P-2604.20932] Adaptive Defense Orchestration for RAG: A Sentinel-Strategist Architecture against Multi-Vector Attacks, Pranav Pallerla, Wilson Naik Bhukya, Bharath Vemula et al., arXiv 2026 · http://arxiv.org/abs/2604.20932v1
- [P-2604.18584] MathNet: a Global Multimodal Benchmark for Mathematical Reasoning and Retrieval, Shaden Alshammari, Kevin Wen, Abrar Zainal et al., arXiv 2026 · http://arxiv.org/abs/2604.18584v1 · also_in: hf
- [P-2604.18234] Evaluating Multi-Hop Reasoning in RAG Systems: A Comparison of LLM-Based Retriever Evaluation Strategies, Lorenz Brehme, Thomas Ströhle, Ruth Breu, arXiv 2026 · http://arxiv.org/abs/2604.18234v1
- [P-2604.18663] Beyond Explicit Refusals: Soft-Failure Attacks on Retrieval-Augmented Generation, Wentao Zhang, Yan Zhuang, ZhuHang Zheng et al., arXiv 2026 · http://arxiv.org/abs/2604.18663v1
- [P-2604.09174] Facet-Level Tracing of Evidence Uncertainty and Hallucination in RAG, Passant Elchafei, Monorama Swain, Shahed Masoudian et al., arXiv 2026 · http://arxiv.org/abs/2604.09174v1
- [P-2604.08304] Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions, Yuming Xu, Mingtao Zhang, Zhuohan Ge et al., arXiv 2026 · http://arxiv.org/abs/2604.08304v1
- [P-2604.10717] Detecting RAG Extraction Attack via Dual-Path Runtime Integrity Game, Yuanbo Xie, Yingjie Zhang, Yulin Li et al., arXiv 2026 · http://arxiv.org/abs/2604.10717v1
- [P-2604.02954] LogicPoison: Logical Attacks on Graph Retrieval-Augmented Generation, Yilin Xiao, Jin Chen, Qinggang Zhang et al., arXiv 2026 · http://arxiv.org/abs/2604.02954v1
- [P-2603.25164] PIDP-Attack: Combining Prompt Injection with Database Poisoning Attacks on Retrieval-Augmented Generation Systems, Haozhen Wang, Haoyue Liu, Jionghao Zhu et al., arXiv 2026 · http://arxiv.org/abs/2603.25164v1
- [P-2604.09666] Do We Still Need GraphRAG? Benchmarking RAG and GraphRAG for Agentic Search Systems, Dongzhe Fan, Zheyi Xue, Siyuan Liu et al., arXiv 2026 · http://arxiv.org/abs/2604.09666v1
- [P-2604.00387] RAGShield: Detecting Numerical Claim Manipulation in Government RAG Systems, KrishnaSaiReddy Patil, arXiv 2026 · http://arxiv.org/abs/2604.00387v2
- [P-2604.10745] How You Ask Matters! Adaptive RAG Robustness to Query Variations, Yunah Jang, Megha Sundriyal, Kyomin Jung et al., arXiv 2026 · http://arxiv.org/abs/2604.10745v1
- [P-2604.19047] RARE: Redundancy-Aware Retrieval Evaluation Framework for High-Similarity Corpora, Hanjun Cho, Jay-Yoon Lee, arXiv 2026 · http://arxiv.org/abs/2604.19047v1
- [P-2604.20763] Coverage, Not Averages: Semantic Stratification for Trustworthy Retrieval Evaluation, Andrew Klearman, Radu Revutchi, Rohin Garg et al., arXiv 2026 · http://arxiv.org/abs/2604.20763v1
- [P-2604.15945] RAGognizer: Hallucination-Aware Fine-Tuning via Detection Head Integration, Fabian Ridder, Laurin Lessel, Malte Schilling, arXiv 2026 · http://arxiv.org/abs/2604.15945v1
- [P-2603.27752] Retromorphic Testing with Hierarchical Verification for Hallucination Detection in RAG, Boxi Yu, Yuzhong Zhang, Liting Lin et al., arXiv 2026 · http://arxiv.org/abs/2603.27752v1
- [P-2604.13417] The Cognitive Circuit Breaker: A Systems Engineering Framework for Intrinsic AI Reliability, Jonathan Pan, arXiv 2026 · http://arxiv.org/abs/2604.13417v1

### 클러스터 4 — 도메인 특화 RAG 응용 (14)
- [P-2604.22061] Lightweight Retrieval-Augmented Generation and Large Language Model-Based Modeling for Scalable Patient-Trial Matching, Xiaodi Li, Yang Xiao, Munhwan Lee et al., arXiv 2026 · http://arxiv.org/abs/2604.22061v1
- [P-2604.11419] Beyond RAG for Cyber Threat Intelligence: A Systematic Evaluation of Graph-Based and Agentic Retrieval, Dzenan Hamzic, Florian Skopik, Max Landauer et al., arXiv 2026 · http://arxiv.org/abs/2604.11419v1
- [P-2604.17340] Neuro-Symbolic Resolution of Recommendation Conflicts in Multimorbidity Clinical Guidelines, Shiyao Xie, Jian Du, arXiv 2026 · http://arxiv.org/abs/2604.17340v1
- [P-2604.10389] BLUEmed: Retrieval-Augmented Multi-Agent Debate for Clinical Error Detection, Saukun Thika You, Nguyen Anh Khoa Tran, Wesley K. Marizane et al., arXiv 2026 · http://arxiv.org/abs/2604.10389v1
- [P-2604.07274] A Systematic Study of Retrieval Pipeline Design for Retrieval-Augmented Medical Question Answering, Nusrat Sultana, Abdullah Muhammad Moosa, Kazi Afzalur Rahman et al., arXiv 2026 · http://arxiv.org/abs/2604.07274v1
- [P-2604.16422] Injecting Structured Biomedical Knowledge into Language Models: Continual Pretraining vs. GraphRAG, Jaafer Klila, Sondes Bannour Souihi, Rahma Boujelben et al., arXiv 2026 · http://arxiv.org/abs/2604.16422v1
- [P-2604.14222] Adaptive Query Routing: A Tier-Based Framework for Hybrid Retrieval Across Financial, Legal, and Medical Documents, Afshan Hashmi, arXiv 2026 · http://arxiv.org/abs/2604.14222v1
- [P-2604.10420] CARE-ECG: Causal Agent-based Reasoning for Explainable and Counterfactual ECG Interpretation, Elahe Khatibi, Ziyu Wang, Ankita Sharma et al., arXiv 2026 · http://arxiv.org/abs/2604.10420v1
- [P-2603.24580] Retrieval Improvements Do Not Guarantee Better Answers: A Study of RAG for AI Policy QA, Saahil Mathur, Ryan David Rittner, Vedant Ajit Thakur et al., arXiv 2026 · http://arxiv.org/abs/2603.24580v1
- [P-2604.14172] Tug-of-War within A Decade: Conflict Resolution in Vulnerability Analysis via Teacher-Guided Retrieval-Augmented Generations, Ziyin Zhou, Jianyi Zhang, Xu ji et al., arXiv 2026 · http://arxiv.org/abs/2604.14172v1
- [P-2604.20869] Clinical Reasoning AI for Oncology Treatment Planning: A Multi-Specialty Case-Based Evaluation, Philippe E. Spiess, Md Muntasir Zitu, Alison Walker et al., arXiv 2026 · http://arxiv.org/abs/2604.20869v1
- [P-2604.19776] Development and Preliminary Evaluation of a Domain-Specific Large Language Model for Tuberculosis Care in South Africa, Thokozile Khosa, Olawande Daramola, arXiv 2026 · http://arxiv.org/abs/2604.19776v1
- [P-2603.24012] CVPD at QIAS 2026: RAG-Guided LLM Reasoning for Al-Mawarith Share Computation and Heir Allocation, Wassim Swaileh, Mohammed-En-Nadhir Zighem, Hichem Telli et al., arXiv 2026 · http://arxiv.org/abs/2603.24012v2
- [P-2604.19522] GenerativeMPC: VLM-RAG-guided Whole-Body MPC with Virtual Impedance for Bimanual Mobile Manipulation, Marcelino Julio Fernando, Miguel Altamirano Cabrera, Jeffrin Sam et al., arXiv 2026 · http://arxiv.org/abs/2604.19522v1

### 클러스터 5 — RAG 파이프라인 요소 최적화 (10)
- [P-2604.22661] Can QPP Choose the Right Query Variant? Evaluating Query Variant Selection for RAG Pipelines, Negar Arabzadeh, Andrew Drozdov, Michael Bendersky et al., arXiv 2026 · http://arxiv.org/abs/2604.22661v1
- [P-2604.12047] Empirical Evaluation of PDF Parsing and Chunking for Financial Question Answering with RAG, Omar El Bachyr, Yewei Song, Saad Ezzini et al., arXiv 2026 · http://arxiv.org/abs/2604.12047v1
- [P-2604.04948] From PDF to RAG-Ready: Evaluating Document Conversion Frameworks for Domain-Specific Question Answering, José Guilherme Marques dos Santos, Ricardo Yang, Rui Humberto Pereira et al., arXiv 2026 · http://arxiv.org/abs/2604.04948v1
- [P-2603.25333] Adaptive Chunking: Optimizing Chunking-Method Selection for RAG, Paulo Roberto de Moura Júnior, Jean Lelong, Annabelle Blangero, arXiv 2026 · http://arxiv.org/abs/2603.25333v1
- [P-2604.02091] Optimizing RAG Rerankers with LLM Feedback via Reinforcement Learning, Yuhang Wu, Xiangqing Shen, Fanfan Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.02091v1
- [P-2604.17325] Align Documents to Questions: Question-Oriented Document Rewriting for Retrieval-Augmented Generation, Jiaang Li, Zhendong Mao, Quan Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.17325v1
- [P-2604.15802] CHOP: Chunkwise Context-Preserving Framework for RAG on Multi Documents, Hyunseok Park, Jihyeon Kim, Jongeun Kim et al., arXiv 2026 · http://arxiv.org/abs/2604.15802v1
- [P-2604.03455] Lightweight Query Routing for Adaptive RAG: A Baseline Study on RAGRouter-Bench, Prakhar Bansal, Shivangi Agarwal, arXiv 2026 · http://arxiv.org/abs/2604.03455v1
- [P-2604.01733] From BM25 to Corrective RAG: Benchmarking Retrieval Strategies for Text-and-Table Documents, Meftun Akarsu, Recep Kaan Karaman, Christopher Mierbach, arXiv 2026 · http://arxiv.org/abs/2604.01733v1
- [P-2604.22678] BERAG: Bayesian Ensemble Retrieval-Augmented Generation for Knowledge-based Visual Question Answering, Jinghong Chen, Jingbiao Mei, Guangyu Yang et al., arXiv 2026 · http://arxiv.org/abs/2604.22678v1

### 기타 (클러스터 미분류) (136)
- [P-2604.22207] Evaluating LLM-Based Goal Extraction in Requirements Engineering: Prompting Strategies and Their Limitations, Anna Arnaudo, Riccardo Coppola, Maurizio Morisio et al., arXiv 2026 · http://arxiv.org/abs/2604.22207v1
- [P-2604.22261] Bridging the Long-Tail Gap: Robust Retrieval-Augmented Relation Completion via Multi-Stage Paraphrase Infusion, Fahmida Alam, Mihai Surdeanu, Ellen Riloff, arXiv 2026 · http://arxiv.org/abs/2604.22261v1
- [P-2604.22095] An End-to-End Ukrainian RAG for Local Deployment. Optimized Hybrid Search and Lightweight Generation, Mykola Trokhymovych, Yana Oliinyk, Nazarii Nyzhnyk, arXiv 2026 · http://arxiv.org/abs/2604.22095v1
- [P-2604.20666] ORPHEAS: A Cross-Lingual Greek-English Embedding Model for Retrieval-Augmented Generation, Ioannis E. Livieris, Athanasios Koursaris, Alexandra Apostolopoulou et al., arXiv 2026 · http://arxiv.org/abs/2604.20666v1
- [P-2604.20487] Knowledge Capsules: Structured Nonparametric Memory Units for LLMs, Bin Ju, Shenfeng Weng, Danying Zhou et al., arXiv 2026 · http://arxiv.org/abs/2604.20487v2
- [P-2604.20598] Self-Aware Vector Embeddings for Retrieval-Augmented Generation: A Neuroscience-Inspired Framework for Temporal, Confidence-Weighted, and Relational Knowledge, Naizhong Xu, arXiv 2026 · http://arxiv.org/abs/2604.20598v1
- [P-2604.20452] HaS: Accelerating RAG through Homology-Aware Speculative Retrieval, Peng Peng, Weiwei Lin, Wentai Wu et al., arXiv 2026 · http://arxiv.org/abs/2604.20452v1
- [P-2604.20199] All Languages Matter: Understanding and Mitigating Language Bias in Multilingual RAG, Dan Wang, Guozhao Mo, Yafei Shi et al., arXiv 2026 · http://arxiv.org/abs/2604.20199v1
- [P-2604.19834] KD-Judge: A Knowledge-Driven Automated Judge Framework for Functional Fitness Movements on Edge Devices, Shaibal Saha, Fan Li, Yunge Li et al., arXiv 2026 · http://arxiv.org/abs/2604.19834v1
- [P-2604.18257] DocQAC: Adaptive Trie-Guided Decoding for Effective In-Document Query Auto-Completion, Rahul Mehta, Kavin R, Indrajit Pal et al., arXiv 2026 · http://arxiv.org/abs/2604.18257v1
- [P-2604.17906] Bayesian Active Learning with Gaussian Processes Guided by LLM Relevance Scoring for Dense Passage Retrieval, Junyoung Kim, Anton Korikov, Jiazhou Liang et al., arXiv 2026 · http://arxiv.org/abs/2604.17906v1
- [P-2604.17866] Latent Abstraction for Retrieval-Augmented Generation, Ha Lan N. T, Minh-Anh Nguyen, Dung D. Le, arXiv 2026 · http://arxiv.org/abs/2604.17866v1
- [P-2604.17677] Semantic Entanglement in Vector-Based Retrieval: A Formal Framework and Context-Conditioned Disentanglement Pipeline for Agentic RAG Systems, Nick Loghmani, arXiv 2026 · http://arxiv.org/abs/2604.17677v1
- [P-2604.17778] TeleEmbedBench: A Multi-Corpus Embedding Benchmark for RAG in Telecommunications, Pranshav Gajjar, Vijay K Shah, arXiv 2026 · http://arxiv.org/abs/2604.17778v1
- [P-2604.18105] NIM4-ASR: Towards Efficient, Robust, and Customizable Real-Time LLM-Based ASR, Yuan Xie, Jiaqi Song, Guang Qiu et al., arXiv 2026 · http://arxiv.org/abs/2604.18105v1
- [P-2604.17889] AeroRAG: Structured Multimodal Retrieval-Augmented LLM for Fine-Grained Aerial Visual Reasoning, Junxiao Xue, Quan Deng, Tingqi Hu et al., arXiv 2026 · http://arxiv.org/abs/2604.17889v1
- [P-2604.04936] Web Retrieval-Aware Chunking (W-RAC) for Efficient and Cost-Effective Retrieval-Augmented Generation Systems, Uday Allu, Sonu Kedia, Tanmay Odapally et al., HF 2026 · https://huggingface.co/papers/2604.04936 · also_in: arxiv
- [P-2604.17301] RoTRAG: Rule of Thumb Reasoning for Conversation Harm Detection with Retrieval-Augmented Generation, Juhyeon Lee, Wonduk Seo, Junseo Koh et al., arXiv 2026 · http://arxiv.org/abs/2604.17301v1
- [P-2604.15958] A Case Study on the Impact of Anonymization Along the RAG Pipeline, Andreea-Elena Bodea, Stephen Meisenbacher, Florian Matthes, arXiv 2026 · http://arxiv.org/abs/2604.15958v1
- [P-2604.15771] Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing, Kai Wei, Raymond Li, Xi Zhu et al., arXiv 2026 · http://arxiv.org/abs/2604.15771v1
- [P-2604.15621] Rethinking the Necessity of Adaptive Retrieval-Augmented Generation through the Lens of Adaptive Listwise Ranking, Jun Feng, Jiahui Tang, Zhicheng He et al., arXiv 2026 · http://arxiv.org/abs/2604.15621v1
- [P-2604.15663] CodeMMR: Bridging Natural Language, Code, and Image for Unified Retrieval, Jiahui Geng, Qing Li, Fengyu Cai et al., arXiv 2026 · http://arxiv.org/abs/2604.15663v1
- [P-2604.14967] UniDoc-RL: Coarse-to-Fine Visual RAG with Hierarchical Actions and Dense Rewards, Jun Wang, Shuo Tan, Zelong Sun et al., arXiv 2026 · http://arxiv.org/abs/2604.14967v2 · also_in: hf
- [P-2604.14896] Toward Agentic RAG for Ukrainian, Marta Sumyk, Oleksandr Kosovan, arXiv 2026 · http://arxiv.org/abs/2604.14896v1
- [P-2604.15385] Prompt-Driven Code Summarization: A Systematic Literature Review, Afia Farjana, Zaiyu Cheng, Antonio Mastropaolo, arXiv 2026 · http://arxiv.org/abs/2604.15385v1
- [P-2604.14576] Enhancing Mental Health Counseling Support in Bangladesh using Culturally-Grounded Knowledge, Md Arid Hasan, Azhagu Meena SP, Aditya Khan et al., arXiv 2026 · http://arxiv.org/abs/2604.14576v1
- [P-2604.14034] Large Language Models to Enhance Business Process Modeling: Past, Present, and Future Trends, João Bettencourt, Sérgio Guerreiro, arXiv 2026 · http://arxiv.org/abs/2604.14034v1
- [P-2604.13705] Beyond Arrow's Impossibility: Fairness as an Emergent Property of Multi-Agent Collaboration, Sayan Kumar Chaki, Antoine Gourru, Julien Velcin, arXiv 2026 · http://arxiv.org/abs/2604.13705v1
- [P-2604.13666] Automatically Inferring Teachers' Geometric Content Knowledge: A Skills Based Approach, Ziv Fenigstein, Kobi Gal, Avi Segal et al., arXiv 2026 · http://arxiv.org/abs/2604.13666v1
- [P-2604.14339] Shuffle the Context: RoPE-Perturbed Self-Distillation for Long-Context Adaptation, Zichong Li, Chen Liang, Liliang Ren et al., arXiv 2026 · http://arxiv.org/abs/2604.14339v1
- [P-2604.13579] MM-Doc-R1: Training Agents for Long Document Visual Question Answering through Multi-turn Reinforcement Learning, Jiahang Lin, Kai Hu, Binghai Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.13579v1
- [P-2604.14147] ROSE: Retrieval-Oriented Segmentation Enhancement, Song Tang, Guangquan Jie, Henghui Ding et al., arXiv 2026 · http://arxiv.org/abs/2604.14147v1 · also_in: hf
- [P-2604.13660] VRAG-DFD: Verifiable Retrieval-Augmentation for MLLM-based Deepfake Detection, Hui Han, Shunli Wang, Yandan Zhao et al., arXiv 2026 · http://arxiv.org/abs/2604.13660v3
- [P-2604.13021] Representation geometry shapes task performance in vision-language modeling for CT enterography, Cristian Minoccheri, Emily Wittrup, Kayvan Najarian et al., arXiv 2026 · http://arxiv.org/abs/2604.13021v1
- [P-2604.14227] FRESCO: Benchmarking and Optimizing Re-rankers for Evolving Semantic Conflict in Retrieval-Augmented Generation, Sohyun An, Hayeon Lee, Shuibenyang Yuan et al., arXiv 2026 · http://arxiv.org/abs/2604.14227v1
- [P-2604.12812] DocSeeker: Structured Visual Reasoning with Evidence Grounding for Long Document Understanding, Hao Yan, Yuliang Liu, Xingchen Liu et al., arXiv 2026 · http://arxiv.org/abs/2604.12812v4
- [P-2604.12735] AffectAgent: Collaborative Multi-Agent Reasoning for Retrieval-Augmented Multimodal Emotion Recognition, Zeheng Wang, Zitong Yu, Yijie Zhu et al., arXiv 2026 · http://arxiv.org/abs/2604.12735v1
- [P-2604.12138] Beyond Factual Grounding: The Case for Opinion-Aware Retrieval-Augmented Generation, Aditya Agrawal, Alwarappan Nakkiran, Darshan Fofadiya et al., arXiv 2026 · http://arxiv.org/abs/2604.12138v1
- [P-2604.12034] Memory as Metabolism: A Design for Companion Knowledge Systems, Stefan Miteski, arXiv 2026 · http://arxiv.org/abs/2604.12034v1
- [P-2604.11699] Legal2LogicICL: Improving Generalization in Transforming Legal Cases to Logical Formulas via Diverse Few-Shot Learning, Jieying Xue, Phuong Minh Nguyen, Ha Thanh Nguyen et al., arXiv 2026 · http://arxiv.org/abs/2604.11699v1
- [P-2604.11407] Retrieval as Generation: A Unified Framework with Self-Triggered Information Planning, Bo Li, Mingda Wang, Gexiang Fang et al., arXiv 2026 · http://arxiv.org/abs/2604.11407v2
- [P-2604.11209] Exploring Knowledge Conflicts for Faithful LLM Reasoning: Benchmark and Method, Tianzhe Zhao, Jiaoyan Chen, Shuxiu Zhang et al., arXiv 2026 · http://arxiv.org/abs/2604.11209v1
- [P-2604.10874] AOP-Smart: A RAG-Enhanced Large Language Model Framework for Adverse Outcome Pathway Analysis, Qinjiang Niu, Lu Yan, arXiv 2026 · http://arxiv.org/abs/2604.10874v1
- [P-2604.10504] CARO: Chain-of-Analogy Reasoning Optimization for Robust Content Moderation, Bingzhe Wu, Haotian Lu, Yuchen Mou, arXiv 2026 · http://arxiv.org/abs/2604.10504v1
- [P-2604.10734] Self-Correcting RAG: Enhancing Faithfulness via MMKP Context Selection and NLI-Guided MCTS, Shijia Xu, Zhou Wu, Xiaolong Jia et al., arXiv 2026 · http://arxiv.org/abs/2604.10734v1
- [P-2604.10772] HOG-Layout: Hierarchical 3D Scene Generation, Optimization and Editing via Vision-Language Models, Haiyan Jiang, Deyu Zhang, Dongdong Weng et al., arXiv 2026 · http://arxiv.org/abs/2604.10772v1
- [P-2604.10114] CircuitSynth: Reliable Synthetic Data Generation, Zehua Cheng, Wei Dai, Jiahao Sun et al., arXiv 2026 · http://arxiv.org/abs/2604.10114v1
- [P-2604.20878] AITP: Traffic Accident Responsibility Allocation via Multimodal Large Language Models, Zijin Zhou, Songan Zhang, arXiv 2026 · http://arxiv.org/abs/2604.20878v1
- [P-2604.09430] On the Representational Limits of Quantum-Inspired 1024-D Document Embeddings: An Experimental Evaluation Framework, Dario Maio, arXiv 2026 · http://arxiv.org/abs/2604.09430v1
- [P-2604.08920] Beyond Relevance: Utility-Centric Retrieval in the LLM Era, Hengran Zhang, Minghao Tang, Keping Bi et al., arXiv 2026 · http://arxiv.org/abs/2604.08920v1
- [P-2604.08952] MAB-DQA: Addressing Query Aspect Importance in Document Question Answering with Multi-Armed Bandits, Yixin Xiang, Yunshan Ma, Xiaoyu Du et al., arXiv 2026 · http://arxiv.org/abs/2604.08952v2
- [P-2604.13101] Building Trust in the Skies: A Knowledge-Grounded LLM-based Framework for Aviation Safety, Anirudh Iyengar, Alisa Tiselska, Dumindu Samaraweera et al., arXiv 2026 · http://arxiv.org/abs/2604.13101v1
- [P-2604.09747] ADAM: A Systematic Data Extraction Attack on Agent Memory via Adaptive Querying, Xingyu Lyu, Jianfeng He, Ning Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.09747v1
- [P-2604.14215] PriHA: A RAG-Enhanced LLM Framework for Primary Healthcare Assistant in Hong Kong, Richard Wai Cheung Chan, Shanru Lin, Ya-nan Ma et al., arXiv 2026 · http://arxiv.org/abs/2604.14215v1
- [P-2604.08046] Guaranteeing Knowledge Integration with Joint Decoding for Retrieval-Augmented Generation, Zhengyi Zhao, Shubo Zhang, Zezhong Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.08046v2
- [P-2604.07590] DCD: Domain-Oriented Design for Controlled Retrieval-Augmented Generation, Valeriy Kovalskiy, Nikita Belov, Nikita Miteyko et al., arXiv 2026 · http://arxiv.org/abs/2604.07590v1
- [P-2604.06737] WisdomInterrogatory (LuWen): An Open-Source Legal Large Language Model Technical Report, Yiquan Wu, Yuhang Liu, Yifei Liu et al., arXiv 2026 · http://arxiv.org/abs/2604.06737v2
- [P-2604.06666] A Graph-Enhanced Defense Framework for Explainable Fake News Detection with LLM, Bo Wang, Jing Ma, Hongzhan Lin et al., arXiv 2026 · http://arxiv.org/abs/2604.06666v1
- [P-2604.06616] CubeGraph: Efficient Retrieval-Augmented Generation for Spatial and Temporal Data, Mingyu Yang, Wentao Li, Wei Wang, arXiv 2026 · http://arxiv.org/abs/2604.06616v1
- [P-2604.07285] Why teaching resists automation in an AI-inundated era: Human judgment, non-modular work, and the limits of delegation, Songhee Han, arXiv 2026 · http://arxiv.org/abs/2604.07285v1
- [P-2604.07012] DTCRS: Dynamic Tree Construction for Recursive Summarization, Guanran Luo, Zhongquan Jian, Wentao Qiu et al., arXiv 2026 · http://arxiv.org/abs/2604.07012v1
- [P-2604.06997] ChunQiuTR: Time-Keyed Temporal Retrieval in Classical Chinese Annals, Yihao Wang, Zijian He, Jie Ren et al., arXiv 2026 · http://arxiv.org/abs/2604.06997v1
- [P-2604.06647] Feedback Adaptation for Retrieval-Augmented Generation, Jihwan Bang, Seunghan Yang, Kyuhong Shim et al., arXiv 2026 · http://arxiv.org/abs/2604.06647v2
- [P-2604.06633] Argus: Reorchestrating Static Analysis via a Multi-Agent Ensemble for Full-Chain Security Vulnerability Detection, Zi Liang, Qipeng Xie, Jun He et al., arXiv 2026 · http://arxiv.org/abs/2604.06633v1
- [P-2604.06279] Plasma GraphRAG: Physics-Grounded Parameter Selection for Gyrokinetic Simulations, Ruichen Zhang, Feda AlMuhisen, Chenguang Wan et al., arXiv 2026 · http://arxiv.org/abs/2604.06279v1
- [P-2604.05587] ResearchEVO: An End-to-End Framework for Automated Scientific Discovery and Documentation, Zhe Zhao, Haibin Wen, Jiaming Ma et al., arXiv 2026 · http://arxiv.org/abs/2604.05587v1
- [P-2604.06269] MAT-Cell: A Multi-Agent Tree-Structured Reasoning Framework for Batch-Level Single-Cell Annotation, Yehui Yang, Zelin Zang, Changxi Chi et al., arXiv 2026 · http://arxiv.org/abs/2604.06269v1
- [P-2604.05418] VideoStir: Understanding Long Videos via Spatio-Temporally Structured and Intent-Aware RAG, Honghao Fu, Miao Xu, Yiwei Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.05418v3
- [P-2604.05358] LatentAudit: Real-Time White-Box Faithfulness Monitoring for Retrieval-Augmented Generation with Verifiable Deployment, Zhe Yu, Wenpeng Xing, Meng Han, arXiv 2026 · http://arxiv.org/abs/2604.05358v1
- [P-2604.05350] DQA: Diagnostic Question Answering for IT Support, Vishaal Kapoor, Mariam Dundua, Sarthak Ahuja et al., arXiv 2026 · http://arxiv.org/abs/2604.05350v2
- [P-2604.06262] From Exposure to Internalization: Dual-Stream Calibration for In-context Clinical Reasoning, Chuang Zhao, Hongke Zhao, Xiaofang Zhou et al., arXiv 2026 · http://arxiv.org/abs/2604.06262v1
- [P-2604.05268] Region-R1: Reinforcing Query-Side Region Cropping for Multi-Modal Re-Ranking, Chan-Wei Hu, Zhengzhong Tu, arXiv 2026 · http://arxiv.org/abs/2604.05268v2
- [P-2604.05467] CUE-R: Beyond the Final Answer in Retrieval-Augmented Generation, Siddharth Jain, Venkat Narayan Vedam, arXiv 2026 · http://arxiv.org/abs/2604.05467v1 · also_in: hf
- [P-2604.05818] WikiSeeker: Rethinking the Role of Vision-Language Models in Knowledge-Based Visual Question Answering, Yingjian Zhu, Xinming Wang, Kun Ding et al., arXiv 2026 · http://arxiv.org/abs/2604.05818v2
- [P-2604.05540] Learning to Edit Knowledge via Instruction-based Chain-of-Thought Prompting, Jinhu Fu, Yan Bai, Longzhu He et al., arXiv 2026 · http://arxiv.org/abs/2604.05540v1
- [P-2604.05051] This Treatment Works, Right? Evaluating LLM Sensitivity to Patient Question Framing in Medical QA, Hye Sun Yun, Geetika Kapoor, Michael Mackert et al., arXiv 2026 · http://arxiv.org/abs/2604.05051v1
- [P-2604.04853] MemMachine: A Ground-Truth-Preserving Memory System for Personalized AI Agents, Shu Wang, Edwin Yu, Oscar Love et al., arXiv 2026 · http://arxiv.org/abs/2604.04853v1
- [P-2604.04749] AI Trust OS -- A Continuous Governance Framework for Autonomous AI Observability and Zero-Trust Compliance in Enterprise Environments, Eranga Bandara, Asanga Gunaratna, Ross Gore et al., arXiv 2026 · http://arxiv.org/abs/2604.04749v1
- [P-2604.04593] Ruling Out to Rule In: Contrastive Hypothesis Retrieval for Medical Question Answering, Byeolhee Kim, Min-Kyung Kim, Young-Hak Kim et al., arXiv 2026 · http://arxiv.org/abs/2604.04593v1
- [P-2604.04565] PassiveQA: A Three-Action Framework for Epistemically Calibrated Question Answering via Supervised Finetuning, Madhav S Baidya, arXiv 2026 · http://arxiv.org/abs/2604.04565v1
- [P-2604.04869] Optimizing LLM Prompt Engineering with DSPy Based Declarative Learning, Shiek Ruksana, Sailesh Kiran Kurra, Thipparthi Sanjay Baradwaj, arXiv 2026 · http://arxiv.org/abs/2604.04869v1
- [P-2604.05096] RAG or Learning? Understanding the Limits of LLM Adaptation under Continuous Knowledge Drift in the Real World, Hanbing Liu, Lang Cao, Yang Li, arXiv 2026 · http://arxiv.org/abs/2604.05096v2
- [P-2604.04103] Compliance-by-Construction Argument Graphs: Using Generative AI to Produce Evidence-Linked Formal Arguments for Certification-Grade Accountability, Mahyar T. Moghaddam, arXiv 2026 · http://arxiv.org/abs/2604.04103v1
- [P-2604.03926] CODE-GEN: A Human-in-the-Loop RAG-Based Agentic AI System for Multiple-Choice Question Generation, Xiaojing Duan, Frederick Nwanganga, Chaoli Wang, arXiv 2026 · http://arxiv.org/abs/2604.03926v1
- [P-2604.04020] Unmasking Hallucinations: A Causal Graph-Attention Perspective on Factual Reliability in Large Language Models, Sailesh kiran kurra, Shiek Ruksana, Vishal Borusu, arXiv 2026 · http://arxiv.org/abs/2604.04020v1
- [P-2604.04036] MisEdu-RAG: A Misconception-Aware Dual-Hypergraph RAG for Novice Math Teachers, Zhihan Guo, Rundong Xue, Yuting Lu et al., arXiv 2026 · http://arxiv.org/abs/2604.04036v1
- [P-2604.03656] Beyond Retrieval: Modeling Confidence Decay and Deterministic Agentic Platforms in Generative Engine Optimization, XinYu Zhao, ChengYou Li, XiangBao Meng et al., arXiv 2026 · http://arxiv.org/abs/2604.03656v1
- [P-2604.03571] Selective Forgetting for Large Reasoning Models, Tuan Le, Wei Qian, Mengdi Huai, arXiv 2026 · http://arxiv.org/abs/2604.03571v1
- [P-2604.03664] Document-Level Numerical Reasoning across Single and Multiple Tables in Financial Reports, Yi-Cheng Wang, Wei-An Wang, Chu-Song Chen, arXiv 2026 · http://arxiv.org/abs/2604.03664v1
- [P-2604.03448] ExpressEdit: Fast Editing of Stylized Facial Expressions with Diffusion Models in Photoshop, Kenan Tang, Jiasheng Guo, Jeffrey Lin et al., arXiv 2026 · http://arxiv.org/abs/2604.03448v1
- [P-2604.03174] Beyond the Parameters: A Technical Survey of Contextual Enrichment in Large Language Models: From In-Context Prompting to Causal Retrieval-Augmented Generation, Prakhar Bansal, Shivangi Agarwal, arXiv 2026 · http://arxiv.org/abs/2604.03174v1
- [P-2604.03043] Analyzing Healthcare Interoperability Vulnerabilities: Formal Modeling and Graph-Theoretic Approach, Jawad Mohammed, Gahangir Hossain, arXiv 2026 · http://arxiv.org/abs/2604.03043v1
- [P-2604.03330] AICCE: AI Driven Compliance Checker Engine, Mohammad Wali Ur Rahman, Martin Manuel Lopez, Lamia Tasnim Mim et al., arXiv 2026 · http://arxiv.org/abs/2604.03330v1
- [P-2604.02640] Overcoming the "Impracticality" of RAG: Proposing a Real-World Benchmark and Multi-Dimensional Diagnostic Framework, Kenichirou Narita, Siqi Peng, Taku Fukui et al., arXiv 2026 · http://arxiv.org/abs/2604.02640v1
- [P-2604.02545] Competency Questions as Executable Plans: a Controlled RAG Architecture for Cultural Heritage Storytelling, Naga Sowjanya Barla, Jacopo de Berardinis, arXiv 2026 · http://arxiv.org/abs/2604.02545v1
- [P-2604.02409] LumiVideo: An Intelligent Agentic System for Video Color Grading, Yuchen Guo, Junli Gong, Hongmin Cai et al., arXiv 2026 · http://arxiv.org/abs/2604.02409v1
- [P-2604.02238] Generative AI Spotlights the Human Core of Data Science: Implications for Education, Nathan Taback, arXiv 2026 · http://arxiv.org/abs/2604.02238v1
- [P-2604.01610] GraphWalk: Enabling Reasoning in Large Language Models through Tool-Based Graph Navigation, Taraneh Ghandi, Hamidreza Mahyar, Shachar Klaiman, arXiv 2026 · http://arxiv.org/abs/2604.01610v1
- [P-2604.02554] Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming, Qiheng Lu, Nicholas D. Sidiropoulos, arXiv 2026 · http://arxiv.org/abs/2604.02554v1
- [P-2604.01413] Adaptive Stopping for Multi-Turn LLM Reasoning, Xiaofan Zhou, Huy Nguyen, Bo Yu et al., arXiv 2026 · http://arxiv.org/abs/2604.01413v2
- [P-2604.00715] To Memorize or to Retrieve: Scaling Laws for RAG-Considerate Pretraining, Karan Singh, Michael Yu, Varun Gangal et al., arXiv 2026 · http://arxiv.org/abs/2604.00715v1
- [P-2604.00550] BloClaw: An Omniscient, Multi-Modal Agentic Workspace for Next-Generation Scientific Discovery, Yao Qin, Yangyang Yan, Jinhua Pang et al., arXiv 2026 · http://arxiv.org/abs/2604.00550v1
- [P-2604.01348] Procedural Knowledge at Scale Improves Reasoning, Di Wu, Devendra Singh Sachan, Wen-tau Yih et al., arXiv 2026 · http://arxiv.org/abs/2604.01348v2
- [P-2604.16401] GraphRAG-Router: Learning Cost-Efficient Routing over GraphRAGs and LLMs with Reinforcement Learning, Dongzhe Fan, Chuanhao Ji, Zimu Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.16401v1
- [P-2603.29159] Kwame 2.0: Human-in-the-Loop Generative AI Teaching Assistant for Large Scale Online Coding Education in Africa, George Boateng, Samuel Boateng, Victor Kumbol, arXiv 2026 · http://arxiv.org/abs/2603.29159v2
- [P-2603.29002] Understand and Accelerate Memory Processing Pipeline for Disaggregated LLM Inference, Zifan He, Rui Ma, Yizhou Sun et al., arXiv 2026 · http://arxiv.org/abs/2603.29002v1 · also_in: hf
- [P-2603.28474] CiQi-Agent: Aligning Vision, Tools and Aesthetics in Multimodal Agent for Cultural Reasoning on Chinese Porcelains, Wenhan Wang, Zhixiang Zhou, Zhongtian Ma et al., arXiv 2026 · http://arxiv.org/abs/2603.28474v1
- [P-2603.28444] Entropic Claim Resolution: Uncertainty-Driven Evidence Selection for RAG, Davide Di Gioia, arXiv 2026 · http://arxiv.org/abs/2603.28444v1
- [P-2603.28108] Quid est VERITAS? A Modular Framework for Archival Document Analysis, Leonardo Bassanini, Ludovico Biancardi, Alfio Ferrara et al., arXiv 2026 · http://arxiv.org/abs/2603.28108v1
- [P-2603.28128] ORACAL: A Robust and Explainable Multimodal Framework for Smart Contract Vulnerability Detection with Causal Graph Enrichment, Tran Duong Minh Dai, Triet Huynh Minh Le, M. Ali Babar et al., arXiv 2026 · http://arxiv.org/abs/2603.28128v1
- [P-2604.20874] The Root Theorem of Context Engineering, Borja Odriozola Schick, arXiv 2026 · http://arxiv.org/abs/2604.20874v1
- [P-2603.27768] TailNLG: A Multilingual Benchmark Addressing Verbalization of Long-Tail Entities, Lia Draetta, Michael Oliverio, Virginia Ramón-Ferrer et al., arXiv 2026 · http://arxiv.org/abs/2603.27768v1
- [P-2604.19779] ESGLens: An LLM-Based RAG Framework for Interactive ESG Report Analysis and Score Prediction, Tsung-Yu Yang, Meng-Chi Chen, arXiv 2026 · http://arxiv.org/abs/2604.19779v1
- [P-2603.27423] AstraAI: LLMs, Retrieval, and AST-Guided Assistance for HPC Codebases, Mahesh Natarajan, Xiaoye Li, Weiqun Zhang, arXiv 2026 · http://arxiv.org/abs/2603.27423v1
- [P-2603.27404] Heterogeneous Debate Engine: Identity-Grounded Cognitive Architecture for Resilient LLM-Based Ethical Tutoring, Jakub Masłowski, Jarosław A. Chudziak, arXiv 2026 · http://arxiv.org/abs/2603.27404v1
- [P-2604.19777] Self-Describing Structured Data with Dual-Layer Guidance: A Lightweight Alternative to RAG for Precision Retrieval in Large-Scale LLM Knowledge Navigation, Hung Ming Liu, arXiv 2026 · http://arxiv.org/abs/2604.19777v1
- [P-2603.27253] Mitigating Hallucination on Hallucination in RAG via Ensemble Voting, Zequn Xie, Zhengyang Sun, arXiv 2026 · http://arxiv.org/abs/2603.27253v2
- [P-2603.27259] Seeing the Scene Matters: Revealing Forgetting in Video Understanding Models with a Scene-Aware Long-Video Benchmark, Seng Nam Chen, Hao Chen, Chenglam Ho et al., arXiv 2026 · http://arxiv.org/abs/2603.27259v1
- [P-2603.26567] Beyond Code Snippets: Benchmarking LLMs on Repository-Level Question Answering, Yoseph Berhanu Alebachew, Hunter Leary, Swanand Vaishampayan et al., arXiv 2026 · http://arxiv.org/abs/2603.26567v2
- [P-2603.28651] Not Search, But Scan: Benchmarking MLLMs on Scan-Oriented Academic Paper Reasoning, Rongjin Li, Zichen Tang, Xianghe Wang et al., arXiv 2026 · http://arxiv.org/abs/2603.28651v1
- [P-2603.26512] CADSmith: Multi-Agent CAD Generation with Programmatic Geometric Validation, Jesse Barkley, Rumi Loghmani, Amir Barati Farimani, arXiv 2026 · http://arxiv.org/abs/2603.26512v1
- [P-2604.19772] CoAuthorAI: A Human in the Loop System For Scientific Book Writing, Yangjie Tian, Xungang Gu, Yun Zhao et al., arXiv 2026 · http://arxiv.org/abs/2604.19772v1
- [P-2604.19766] OThink-SRR1: Search, Refine and Reasoning with Reinforced Learning for Large Language Models, Haijian Liang, Zenghao Niu, Junjie Wu et al., arXiv 2026 · http://arxiv.org/abs/2604.19766v1
- [P-2603.26557] MemBoost: A Memory-Boosted Framework for Cost-Aware LLM Inference, Joris Köster, Zixuan Liu, Siavash Khajavi et al., arXiv 2026 · http://arxiv.org/abs/2603.26557v1
- [P-2603.26046] Retrieval-Augmented Generation Based Nurse Observation Extraction, Kyomin Hwang, Nojun Kwak, arXiv 2026 · http://arxiv.org/abs/2603.26046v1
- [P-2603.26815] Resolving the Robustness-Precision Trade-off in Financial RAG through Hybrid Document-Routed Retrieval, Zhiyuan Cheng, Longying Lai, Yue Liu, arXiv 2026 · http://arxiv.org/abs/2603.26815v2
- [P-2603.25737] Training the Knowledge Base through Evidence Distillation and Write-Back Enrichment, Yuxing Lu, Xukai Zhao, Wei Wu et al., arXiv 2026 · http://arxiv.org/abs/2603.25737v1
- [P-2603.26807] GroupRAG: Cognitively Inspired Group-Aware Retrieval and Reasoning via Knowledge-Driven Problem Structuring, Xinyi Duan, Yuanrong Tang, Jiangtao Gong, arXiv 2026 · http://arxiv.org/abs/2603.26807v1
- [P-2603.24940] Evaluating adaptive and generative AI-based feedback and recommendations in a knowledge-graph-integrated programming learning system, Lalita Na Nongkhai, Jingyun Wang, Adam Wynn et al., arXiv 2026 · http://arxiv.org/abs/2603.24940v1
- [P-2603.25186] Knowledge-Guided Retrieval-Augmented Generation for Zero-Shot Psychiatric Data: Privacy Preserving Synthetic Data Generation, Adam Jakobsen, Sushant Gautam, Hugo Lewi Hammer et al., arXiv 2026 · http://arxiv.org/abs/2603.25186v1
- [P-2603.24925] GraphER: An Efficient Graph-Based Enrichment and Reranking Method for Retrieval-Augmented Generation, Ruizhong Miao, Yuying Wang, Rongguang Wang et al., arXiv 2026 · http://arxiv.org/abs/2603.24925v1
- [P-2603.24736] AutoSAM: an Agentic Framework for Automating Input File Generation for the SAM Code with Multi-Modal Retrieval-Augmented Generation, Zaid Abulawi, Zavier Ndum Ndum, Eric Cervi et al., arXiv 2026 · http://arxiv.org/abs/2603.24736v1
- [P-2603.24556] Evaluating Chunking Strategies For Retrieval-Augmented Generation in Oil and Gas Enterprise Documents, Samuel Taiwo, Mohd Amaluddin Yusoff, arXiv 2026 · http://arxiv.org/abs/2603.24556v1
- [P-2603.24218] Who Benefits from RAG? The Role of Exposure, Utility and Attribution Bias, Mahdi Dehghan, Graham McDonald, arXiv 2026 · http://arxiv.org/abs/2603.24218v1
- [P-2604.14170] Stateful Evidence-Driven Retrieval-Augmented Generation with Iterative Reasoning, Qi Dong, Ziheng Lin, Ning Ding, arXiv 2026 · http://arxiv.org/abs/2604.14170v1
- [P-2603.24579] MARCH: Multi-Agent Reinforced Self-Check for LLM Hallucination, Zhuo Li, Yupeng Zhang, Pengyu Cheng et al., arXiv 2026 · http://arxiv.org/abs/2603.24579v1

---

## 메타 / 디버그
- model: gemini-2.5-pro
- backend: gemini-pro-sdk
- matched_n: 200
- matched_total_before_cap: 356
- window_days: 60
- tokens_in_uncached: 8665
- tokens_in_cached_read: 249680
- tokens_out: 6288
- usd_estimate: $0.1511
