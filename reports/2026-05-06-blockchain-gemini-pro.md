# Research Topic Suggestion — "blockchain"

생성: 2026-05-06T04:02:59.511309+00:00
DB 윈도우: 1998-12-20 ~ 2026-05-06 (9999d)
모델: gemini-2.5-pro
매칭 논문: 100건
확장 키워드: ['blockchain technology', 'distributed ledger technology', 'DLT', 'smart contract', 'decentralized application', 'dApp', 'cryptocurrency', 'decentralized finance', 'DeFi', 'consensus algorithm']

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — LLM 추론 능력 분석 및 평가
- **설명**: LLM의 복잡한 추론 및 문제 해결 능력을 체계적으로 측정하고 분석하기 위한 새로운 벤치마크와 평가 프레임워크를 제안하는 연구 클러스터입니다. 모델의 강점과 약점을 파악하고 신뢰성을 높이는 데 중점을 둡니다.
- **빈도**: 20건
- **구간별 (≈2499d씩, 오래된→최근)**: 9 → 0 → 11 → 0
- **대표 논문**:
  - [P-ICLR-ebcd4e] Not Search, But Scan: Benchmarking MLLMs on Scan-Oriented Academic Paper Reasoning — Rongjin Li, Zichen Tang, Xianghe Wang et al., ICLR 2025
  - [P-ICLR-6a2da5] RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models — Yunseok Han, Yejoon Lee, Jaeyoung Do, ICLR 2025
  - [P-ICLR-09e44f] HardcoreLogic: Challenging Large Reasoning Models with Long-tail Logic Puzzle Games — Jingcong Liang, Shijun Wan, Xuehai Wu et al., ICLR 2025

### 클러스터 2 — LLM 정렬, 안전성 및 공정성
- **설명**: LLM이 인간의 가치에 부합하고, 편향되지 않으며, 잠재적 위험으로부터 안전하게 작동하도록 보장하는 기술을 다룹니다. 탈옥 공격 방어, 개인정보보호, 공정성 확보, 유해 콘텐츠 생성 방지 등의 연구가 포함됩니다.
- **빈도**: 14건
- **구간별 (≈2499d씩, 오래된→최근)**: 8 → 0 → 6 → 0
- **대표 논문**:
  - [P-ICLR-90befe] SoSBench: Benchmarking Safety Alignment on Six Scientific Domains — Fengqing Jiang, Fengbo Ma, Zhangchen Xu et al., ICLR 2025
  - [P-ICLR-cd9091] Fairness via Independence: A General Regularization Framework for Machine Learning — Yezi Liu, Hanning Chen, Wenjun Huang et al., ICLR 2025

### 클러스터 3 — 강화학습 및 의사결정 에이전트
- **설명**: 복잡한 환경에서 장기적인 목표를 달성하기 위해 스스로 학습하고 행동하는 지능형 에이전트를 개발하는 연구입니다. 효율적인 탐색, 계층적 계획, 멀티 에이전트 협력, 메모리 활용 등이 핵심 주제입니다.
- **빈도**: 14건
- **구간별 (≈2499d씩, 오래된→최근)**: 8 → 0 → 6 → 0
- **대표 논문**:
  - [P-ICLR-6786ce] SLAP: Shortcut Learning for Abstract Planning — Y. Isabel Liu, Bowen Li, Benjamin Eysenbach et al., ICLR 2025
  - [P-ICLR-cb0185] Unraveling the Complexity of Memory in RL Agents: an Approach for Classification and Evaluation — Egor Cherepanov, Nikita Kachaev, Artem Zholus et al., ICLR 2025
  - [P-ICLR-d5a6a5] Task Tokens: A Flexible Approach to Adapting Behavior Foundation Models — Ron Vainshtein, Zohar Rimon, Shie Mannor et al., ICLR 2025

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap A — LLM의 텍스트 기반 안전성을 다루는 연구(클러스터 2)와 환경 내에서 행동하는 자율 에이전트 개발 연구(클러스터 3) 사이에 명확한 단절이 존
- **타입**: between-clusters
- **설명**: LLM의 텍스트 기반 안전성을 다루는 연구(클러스터 2)와 환경 내에서 행동하는 자율 에이전트 개발 연구(클러스터 3) 사이에 명확한 단절이 존재합니다. 현재 안전성 연구는 주로 유해한 텍스트 생성을 방지하는 데 초점을 맞추는 반면, 에이전트 연구는 안전이나 가치 정렬을 명시적으로 고려하지 않고 능력(계획, 탐색, 기억 등) 향상에 집중하고 있습니다. 이로 인해 물리적 또는 디지털 환경과 상호작용할 수 있는 에이전트의 안전성을 보장하고 평가하는 방법론이 부족한 연구 갭이 발생합니다.
- **근거 논문**: P-ICLR-90befe, P-X-e69c06, P-ICLR-6786ce, P-ICLR-e29753
- **Skeptic 검토**: ✓ 통과 — 텍스트 생성 모델의 정적 안전성(클러스터 2)과 동적 환경에서 행동하는 에이전트의 안전성(클러스터 3) 사이의 간극은 명확하며, 이는 매우 중요한 연구 공백입니다.

### Gap B — LLM 추론 능력 평가 클러스터(클러스터 1) 내의 여러 논문들이 기존 벤치마크의 한계를 반복적으로 지적하고 있습니다. 이들은 현재 벤치마크가 
- **타입**: recurring-limitation
- **설명**: LLM 추론 능력 평가 클러스터(클러스터 1) 내의 여러 논문들이 기존 벤치마크의 한계를 반복적으로 지적하고 있습니다. 이들은 현재 벤치마크가 특정 형식에 대한 과적합이나 암기된 패턴에 의존하는 경향이 있으며, 모델의 실제 추론 과정의 충실도를 측정하지 못한다고 비판합니다. 이는 모델이 표면적으로는 정답을 맞히더라도, 그 과정이 논리적으로 타당한지, 아니면 그럴듯하게 보이는 착각에 불과한지를 구별하기 어렵다는 근본적인 문제를 드러냅니다.
- **근거 논문**: P-ICLR-09e44f, P-ICLR-ebcd4e, P-ICLR-6a2da5
- **Skeptic 검토**: ✓ 통과 — 클러스터 1의 핵심 논문들 스스로가 기존 벤치마크의 암기/충실도 문제를 지적하고 있으므로, 이는 명백하고 반복적으로 나타나는 한계점입니다.

### Gap C — 논문 'A Fano-Style Accuracy Upper Bound...'는 정보이론적 접근을 통해 특정 조건(단일 패스, 다중 홉 QA)에서 
- **타입**: single-shot
- **설명**: 논문 'A Fano-Style Accuracy Upper Bound...'는 정보이론적 접근을 통해 특정 조건(단일 패스, 다중 홉 QA)에서 LLM 추론 능력의 이론적 상한선을 규명합니다. 이는 대부분의 연구가 경험적 벤치마크를 구축하는 클러스터 1 내에서 유일하게 모델의 근본적인 용량 한계를 수학적으로 분석한 연구입니다. 다른 논문들이 이러한 이론적 분석을 확장하거나 다른 종류의 추론 작업에 적용하려는 시도가 없어, 이 중요한 이론적 접근법이 단발성으로 남아 있습니다.
- **근거 논문**: P-ICLR-03e7ca
- **Skeptic 검토**: ✓ 통과 — 경험적 벤치마크 구축이 대다수인 클러스터 1 내에서, Fano-style의 정보이론적 상한선 분석은 독보적인 이론적 접근이며, 이 방향의 후속 연구 부재는 설득력 있는 갭입니다.

### Gap E — LLM 안전성 및 정렬 클러스터(클러스터 2)의 여러 논문들은 현재의 방어 기제가 새롭거나 더 정교한 공격에 취약하다는 공통된 한계를 보고합니다
- **타입**: recurring-limitation
- **설명**: LLM 안전성 및 정렬 클러스터(클러스터 2)의 여러 논문들은 현재의 방어 기제가 새롭거나 더 정교한 공격에 취약하다는 공통된 한계를 보고합니다. 적대적 훈련은 새로운 탈옥 기법에 실패하는 경우가 많고, 안전성 벤치마크는 이미 알려진 단순한 위험 시나리오에 국한되는 경향이 있습니다. 이는 현재의 안전 대책이 알려진 취약점에 대한 사후 대응에 그치며, 미지의 위협에 대해 일반화되는 강건한 방어 체계를 구축하는 데에는 어려움을 겪고 있음을 시사합니다.
- **근거 논문**: P-X-e69c06, P-ICLR-90befe, P-ICLR-6139d3
- **Skeptic 검토**: ✓ 통과 — 제시된 증거 논문들 자체가 현재 안전 방어 기제가 새로운 공격에 취약하다는 점을 명시적으로 인정하고 있어, 이는 분야 내에서 널리 인식되는 시급한 문제입니다.

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap D** — 강화학습 에이전트 연구(클러스터 3)에서는 장기 기억(long-term memory)의 중요성을 강조하지만, LLM 평가 연구(클러스터 1)는 대부분 단발성 질의응답이나 정적인 문제 해결 능력을 측정하는 데 머물러 있습니다. 이로 인해 동적인 환경에서 장시간에 걸쳐 정보를 축적하고, 학습하며, 적응하는 에이전트의 능력을 체계적으로 평가할 수 있는 표준화된 벤치마크가 부재한 상황입니다. · 거부 사유: (a) 다른 클러스터에서 이미 다룸. 클러스터 1의 'AstaBench'나 'WebDevJudge'와 같은 논문들이 장기적이고 상호작용이 필요한 에이전트 태스크를 평가하는 벤치마크를 이미 제안하고 있어, 해당 영역이 부재하다는 주장은 사실과 다릅니다. [title:astabench: rigorous benchmarking of ai agents with a scientific research suite], [title:webdevjudge: evaluating (m)llms as critiques for web development quality]

</details>

## 3. 연구 제안 (Proposer)

### 제안 1 — SAFEGUARD-RL
**가설**: 행동의 예상 결과를 평가하는 동적 안전 보상 함수를 강화학습에 통합하면, 정적 텍스트 분석만으로는 방지할 수 없는 자율 에이전트의 위험한 행동을 효과적으로 억제할 수 있다.
**메우는 갭**: A
**접근**: 본 연구는 '행동 에이전트'와 '안전 평가자'로 구성된 이중 모델 프레임워크를 제안한다. 행동 에이전트가 환경 내에서 행동 계획을 생성하면, 안전 평가자는 계획의 첫 단계를 가상으로 실행하고 그 결과 상태의 위험도를 평가한다. 이 평가 결과는 즉각적인 음의 보상 신호로 변환되어 에이전트의 정책을 실시간으로 수정하는 데 사용되며, 이를 통해 에이전트는 잠재적으로 위험한 행동 경로를 회피하도록 학습한다.
**Baselines**: SLAP (계층적 계획 에이전트), CitySeeker (실행 환경), SoSBench (안전 위반 정의), HERO (보상 모델 결합 방식)
**예상 기여**: 본 연구는 기존의 텍스트 기반 LLM 안전성 연구와 동적 환경에서의 에이전트 행동 연구 사이의 간극을 메우는 새로운 패러다임을 제시한다. 이는 물리적 또는 디지털 환경과 상호작용하는 에이전트의 안전성을 훈련 단계에서부터 보장하는 실용적인 프레임워크를 제공할 것이다. 또한, 에이전트의 동적 안전성을 정량적으로 평가하는 방법론을 확립하는 데 기여할 것으로 기대된다.
**참고**: P-ICLR-90befe, P-ICLR-6786ce, P-ICLR-e29753, P-ICLR-9eeb17

### 제안 2 — PROC-EVAL
**가설**: 모델에게 정답을 도출하는 대신 그럴듯하지만 결함이 있는 추론 과정의 논리적 오류를 명시적으로 식별하고 수정하도록 요구하는 평가는, 정답 일치율만으로는 측정할 수 없는 모델의 실제 추론 충실도를 더 정확하게 측정할 수 있다.
**메우는 갭**: B
**접근**: 기존 추론 벤치마크(예: GSM8K)를 기반으로 새로운 평가 데이터셋을 구축한다. 각 문제에 대해, 정답으로 이어지지만 논리적 비약이 있거나 중간 단계에 오류가 있는 '그럴듯한 오답' 추론 과정을 생성한다. 평가 대상 모델은 주어진 추론 과정의 타당성을 판단하고, 오류가 있다면 어느 단계에서 어떤 종류의 오류가 발생했는지 지적해야 한다. 이 방식은 결과가 아닌 과정의 타당성을 직접 평가함으로써 암기나 우연에 의한 정답을 걸러내고 모델의 실제 논리적 이해도를 측정한다.
**Baselines**: RFEval, HardcoreLogic, ScholScan (기존 벤치마크), Chain-of-Thought (CoT) prompting, self-consistency (추론 전략)
**예상 기여**: 본 연구는 LLM 추론 평가를 '결과 중심'에서 '과정 중심'으로 전환하는 최초의 벤치마크를 제안한다. 이는 모델이 '왜' 정답인지를 실제로 이해하는지, 아니면 정답 패턴을 암기한 것인지를 구별하는 강력한 도구를 제공한다. 결과적으로 더 신뢰성 있고 충실한 추론 능력을 갖춘 모델 개발을 촉진할 것이다.
**참고**: P-ICLR-09e44f, P-ICLR-ebcd4e, P-ICLR-6a2da5, P-ICLR-fbcad2

### 제안 3 — FANO-ITER
**가설**: 다단계(multi-step) 및 도구 사용(tool-use) 추론 과정을 정보 채널의 연속으로 모델링함으로써, 각 단계의 유한한 용량이 전체 문제 해결 능력에 미치는 누적적 제약을 Fano-style 부등식을 통해 정량화할 수 있다.
**메우는 갭**: C
**접근**: 단일 패스 추론에 적용되었던 Fano-style 정보이론적 분석을 여러 단계에 걸쳐 정보를 처리하는 에이전트 시나리오로 확장한다. 각 추론 단계(예: 내부 독백, API 호출, 결과 파싱)를 용량이 제한된 별개의 정보 채널로 정의한다. 이를 통해 전체 추론 과정에서 정보 손실과 오류가 어떻게 누적되는지를 수학적으로 모델링하고, 문제 복잡도와 추론 단계 수에 따른 성공 확률의 이론적 상한선을 유도한다. 이 이론적 모델은 실제 에이전트 시스템의 성능과 비교하여 검증될 것이다.
**Baselines**: InfoQA (Fano-style upper bound), Aria (반복적 자동 형식화 에이전트), RePro (최적화 관점의 추론 과정 분석)
**예상 기여**: 이 연구는 LLM의 추론 능력에 대한 경험적 평가를 넘어, 그 근본적인 정보이론적 한계를 이해하는 이론적 토대를 확장한다. 이는 단일 패스를 넘어 에이전트와 같은 복잡한 다단계 추론 시스템의 성능 한계를 예측하고, 정보 병목 현상을 완화하는 새로운 아키텍처 설계에 대한 원칙적 지침을 제공할 것이다.
**참고**: P-ICLR-03e7ca, P-ICLR-f7385f, P-ICLR-fbcad2

## 4. 참고문헌 (메타DB 기반)

### 클러스터 1 — LLM 추론 능력 분석 및 평가 (20)
- [P-ICLR-ebcd4e] Not Search, But Scan: Benchmarking MLLMs on Scan-Oriented Academic Paper Reasoning, Rongjin Li, Zichen Tang, Xianghe Wang et al., ICLR 2025 · https://openreview.net/forum?id=GDA1yB6yDP
- [P-ICLR-09e44f] HardcoreLogic: Challenging Large Reasoning Models with Long-tail Logic Puzzle Games, Jingcong Liang, Shijun Wan, Xuehai Wu et al., ICLR 2025 · https://openreview.net/forum?id=8USxc43D3I
- [P-ICLR-6a2da5] RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models, Yunseok Han, Yejoon Lee, Jaeyoung Do, ICLR 2025 · https://openreview.net/forum?id=2Gc8aj0afg
- [P-ICLR-03e7ca] A Fano-Style Accuracy Upper Bound for LLM Single-Pass Reasoning in Multi-Hop QA, Kaiyang Wan, Lang Gao, Honglin Mu et al., ICLR 2025 · https://openreview.net/forum?id=dPAcHrG4rl
- [P-ICLR-fbcad2] Rectifying LLM Thought from Lens of Optimization, Junnan Liu, Hongwei Liu, Songyang Zhang et al., ICLR 2025 · https://openreview.net/forum?id=bOMQmyR492
- [P-ICLR-ecee7e] AstaBench: Rigorous Benchmarking of AI Agents with a Scientific Research Suite, Jonathan Bragg, Mike D'Arcy, Nishant Balepur et al., ICLR 2025 · https://openreview.net/forum?id=M7TNf5J26u
- [P-ICLR-1019a3] WebDevJudge: Evaluating (M)LLMs as Critiques for Web Development Quality, Chunyang Li, Yilun Zheng, Xinting Huang et al., ICLR 2025 · https://openreview.net/forum?id=CCSPm6V5EF
- [P-ICLR-f7385f] Aria: an Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph, Hanyu Wang, Ruohan Xie, Yutong Wang et al., ICLR 2025 · https://openreview.net/forum?id=CPxZClPMiy
- [P-ICLR-e94992] Complementing Self-Consistency with Cross-Model Disagreement for Uncertainty Quantification, Kimia Hamidieh, Veronika Thost, Walter Gerych et al., ICLR 2025 · https://openreview.net/forum?id=lOoRJo8xWy
- [P-ICLR-75cedc] GuidedSampling: Steering LLMs Towards Diverse Candidate Solutions at Inference-Time, Divij Handa, Mihir Parmar, Aswin RRV et al., ICLR 2025 · https://openreview.net/forum?id=TD9jC48sts
- [P-ICLR-6475f0] Culture In a Frame: C$^3$B as a Comic-Based Benchmark for Multimodal Culturally Awareness, Yuchen Song, Andong Chen, Wenxin Zhu et al., ICLR 2025 · https://openreview.net/forum?id=jvPdTOSTVl
- [P-ICLR-fe003f] PrefDisco: Benchmarking Proactive Personalized Reasoning, Shuyue Stella Li, Avinandan Bose, Faeze Brahman et al., ICLR 2025 · https://openreview.net/forum?id=O1hfVE0UxG
- [P-ICLR-d79039] OpenEstimate: Evaluating LLMs on Reasoning Under Uncertainty with Real-World Data, Alana Marzoev, Jillian Ross, Jacob Andreas, ICLR 2025 · https://openreview.net/forum?id=sAzUQkP47r
- [P-ICLR-db612c] Multiple Token Divergence: Measuring and Steering In-Context Computation Density, Vincent Herrmann, Eric Alcaide, Michael Wand et al., ICLR 2025 · https://openreview.net/forum?id=Ch0MxMvNHz
- [P-ICLR-140055] Is Your Paper Being Reviewed by an LLM? Benchmarking AI Text Detection in Peer Review, Sungduk Yu, Man Luo, Avinash Madasu et al., ICLR 2025 · https://openreview.net/forum?id=HyZwf1rt4s
- [P-ICLR-9e4492] Characterizing Deep Research: A Benchmark and Formal Definition, Abhinav Java, Ashmit Khandelwal, Sukruta Prakash Midigeshi et al., ICLR 2025 · https://openreview.net/forum?id=5EmpOCq1Ql
- [P-ICLR-10e1ac] MSCR: Exploring the Vulnerability of LLMs’ Mathematical Reasoning Abilities Using Multi-Source Candidate Replacement, Zhishen Sun, Guang Dai, Haishan Ye, ICLR 2025 · https://openreview.net/forum?id=ijOAhcHI7S
- [P-ICLR-6afcf2] SC-Arena: A Natural Language Benchmark for Single-Cell Reasoning with Knowledge-Augmented Evaluation, Jiahao Zhao, Feng Jiang, Shaowei Qin et al., ICLR 2025 · https://openreview.net/forum?id=5RcoUe1tA1
- [P-ICLR-559897] UIS-Digger: Towards Comprehensive Research Agent Systems for Real-world Unindexed Information Seeking, Chang Liu, Chuqiao Kuang, Tianyi Zhuang et al., ICLR 2025 · https://openreview.net/forum?id=aykkGh9TIy
- [P-ICLR-8797e8] Diagnosing and Remedying Knowledge Deficiencies in LLMs via Label-free Curricular Meaningful Learning, Kai Xiong, Xiao Ding, Yixin Cao et al., ICLR 2025 · https://openreview.net/forum?id=qVadFFSfrI

### 클러스터 2 — LLM 정렬, 안전성 및 공정성 (13)
- [P-ICLR-cd9091] Fairness via Independence: A General Regularization Framework for Machine Learning, Yezi Liu, Hanning Chen, Wenjun Huang et al., ICLR 2025 · https://openreview.net/forum?id=sbEb0Ld6MK
- [P-ICLR-7af5d3] Fair Conformal Classification via Learning Representation-Based Groups, Senrong Xu, Yanke Zhou, Yuhao Tan et al., ICLR 2025 · https://openreview.net/forum?id=aa91WoBZeg
- [P-ICLR-90befe] SoSBench: Benchmarking Safety Alignment on Six Scientific Domains, Fengqing Jiang, Fengbo Ma, Zhangchen Xu et al., ICLR 2025 · https://openreview.net/forum?id=2Td8r7KYK2
- [P-ICLR-a5f13f] Generative Value Conflicts Reveal LLM Priorities, Andy Liu, Kshitish Ghate, Mona T. Diab et al., ICLR 2025 · https://openreview.net/forum?id=RXCRKAcv3B
- [P-ICLR-6f8db6] Operationalizing Data Minimization for Privacy-Preserving LLM Prompting, Jijie Zhou, Niloofar Mireshghallah, Tianshi Li, ICLR 2025 · https://openreview.net/forum?id=rpcnvW33EG
- [P-ICLR-5ceddb] Exponential-Wrapped Mechanisms: Differential Privacy on Hadamard Manifolds Made Practical, Yangdi Jiang, Xiaotian Chang, Lei Ding et al., ICLR 2025 · https://openreview.net/forum?id=ulCVfMOo30
- [P-ICLR-acbf80] How Catastrophic is Your LLM? Certifying Risks in Conversation, Chengxiao Wang, Isha Chaudhary, Qian Hu et al., ICLR 2025 · https://openreview.net/forum?id=yt9TW2WtpG
- [P-ICLR-6139d3] BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge Evaluation, Peng Lai, Zhihao Ou, Yong Wang et al., ICLR 2025 · https://openreview.net/forum?id=QGOw6AU8Lp
- [P-ICLR-ff3c8f] Downgrade to Upgrade: Optimizer Simplification Enhances Robustness in LLM Unlearning, Yicheng Lang, Yihua Zhang, Chongyu Fan et al., ICLR 2025 · https://openreview.net/forum?id=Sswng2ToR4
- [P-ICLR-01b319] LLM Fingerprinting via Semantically Conditioned Watermarks, Thibaud Gloaguen, Robin Staab, Nikola Jovanović et al., ICLR 2025 · https://openreview.net/forum?id=t38nZqqi3Z
- [P-ICLR-d7b6b3] Fingerprinting Deep Neural Networks for Ownership Protection: An Analytical Approach, Guang Yang, Ziye Geng, Yihang Chen et al., ICLR 2025 · https://openreview.net/forum?id=sg3UNWKVFt
- [P-ICLR-c8ddff] A Fair Bayesian Inference through Matched Gibbs Posterior, Jihu Lee, Kunwoong Kim, Sehyun Park et al., ICLR 2025 · https://openreview.net/forum?id=sIjFXzEOOH
- [P-ICLR-9142f6] Test-Time Alignment for Large Language Models via Textual Model Predictive Control, Kuang-Da Wang, Teng-Ruei Chen, Yu Heng Hung et al., ICLR 2025 · https://openreview.net/forum?id=DsS3xRPSs5

### 클러스터 3 — 강화학습 및 의사결정 에이전트 (14)
- [P-ICLR-d5a6a5] Task Tokens: A Flexible Approach to Adapting Behavior Foundation Models, Ron Vainshtein, Zohar Rimon, Shie Mannor et al., ICLR 2025 · https://openreview.net/forum?id=6T3wJQhvc3
- [P-ICLR-39b81e] EMFuse: Energy-based Model Fusion for Decision Making, Kejie He, Yi-Chen Li, Yang Yu, ICLR 2025 · https://openreview.net/forum?id=6wDp8XRmNI
- [P-ICLR-cb0185] Unraveling the Complexity of Memory in RL Agents: an Approach for Classification and Evaluation, Egor Cherepanov, Nikita Kachaev, Artem Zholus et al., ICLR 2025 · https://openreview.net/forum?id=lJKdOYFF5W
- [P-ICLR-7e7f3d] Online Decision-Focused Learning, Aymeric Capitaine, Maxime Haddouche, Eric Moulines et al., ICLR 2025 · https://openreview.net/forum?id=FJhtHBphCt
- [P-ICLR-02afb4] Flow Matching with Injected Noise for Offline-to-Online Reinforcement Learning, Yongjae Shin, Jongseong Chae, Jongeui Park et al., ICLR 2025 · https://openreview.net/forum?id=6wd38R8L0Z
- [P-ICLR-01bff2] ReIn: Conversational Error Recovery with Reasoning Inception, Takyoung Kim, Jinseok Nam, Chandrayee Basu et al., ICLR 2025 · https://openreview.net/forum?id=4J3kkHI6m5
- [P-ICLR-6786ce] SLAP: Shortcut Learning for Abstract Planning, Y. Isabel Liu, Bowen Li, Benjamin Eysenbach et al., ICLR 2025 · https://openreview.net/forum?id=enprG5H9aD
- [P-ICLR-aa6674] AutoQD: Automatic Discovery of Diverse Behaviors with Quality-Diversity Optimization, Saeed Hedayatian, Stefanos Nikolaidis, ICLR 2025 · https://openreview.net/forum?id=FNnJIf4ymV
- [P-ICLR-399b2f] Distributions as Actions: A Unified Framework for Diverse Action Spaces, Jiamin He, A. Rupam Mahmood, Martha White, ICLR 2025 · https://openreview.net/forum?id=4ol71wMPY8
- [P-ICLR-77e2d6] Inter-Agent Relative Representations for Multi-Agent Option Discovery, Raul D. Steleac, Mohan Sridharan, David Abel, ICLR 2025 · https://openreview.net/forum?id=Fte7TOqnQp
- [P-ICLR-9eeb17] Hybrid Reinforcement: when reward is sparse, better to be dense, Leitian Tao, Ilia Kulikov, Swarnadeep Saha et al., ICLR 2025 · https://openreview.net/forum?id=0CajQNVKyB
- [P-ICLR-e5f949] KL-Regularized Reinforcement Learning for Generative Modelling is Designed to Mode Collapse, Anthony GX-Chen, Jatin Prakash, Jeff Guo et al., ICLR 2025 · https://openreview.net/forum?id=flBRtdIihA
- [P-ICLR-b345cb] AutoLibra: Agent Metric Induction from Open-Ended Human Feedback, Hao Zhu, Phil Cuvin, Xinkai Yu et al., ICLR 2025 · https://openreview.net/forum?id=4BjGVZ7Bxn
- [P-ICLR-e29753] CitySeeker: How Do VLMs Explore Embodied Urban Navigation with Implicit Human Needs?, Siqi Wang, Chao Liang, Yunfan Gao et al., ICLR 2025 · https://openreview.net/forum?id=hzf23XSDcs

### 기타 (클러스터 미분류) (53)
- [P-ICLR-98404b] The Price of Robustness:  Stable Classifiers Need Overparameterization, Jonas von Berg, Adalbert Fono, Massimiliano Datres et al., ICLR 2025 · https://openreview.net/forum?id=63VXjOFiit
- [P-ICLR-032d95] Leveraging Discrete Function Decomposability for Scientific Design, James C Bowden, Sergey Levine, Jennifer Listgarten, ICLR 2025 · https://openreview.net/forum?id=lndDn7i8W6
- [P-ICLR-2f7093] Beyond Ensembles: Simulating All-Atom Protein Dynamics in a Learned Latent Space, Aditya Sengar, Jiying Zhang, Pierre Vandergheynst et al., ICLR 2025 · https://openreview.net/forum?id=AwowReRWXI
- [P-ICLR-05b434] Bi-Criteria Metric Distortion, Kiarash Banihashem, Diptarka Chakraborty, Shayan Chashm Jahan et al., ICLR 2025 · https://openreview.net/forum?id=QBgHVmvN5S
- [P-ICLR-09dc5c] Price of Quality: Sufficient Conditions for Sparse Recovery using Mixed-Quality Data, Youssef Chaabouni, David Gamarnik, ICLR 2025 · https://openreview.net/forum?id=1PIfB5w05x
- [P-ICLR-acc4d3] Multimodal Prompt Optimization: Why Not Leverage Multiple Modalities for MLLMs, Yumin Choi, Dongki Kim, Jinheon Baek et al., ICLR 2025 · https://openreview.net/forum?id=M5MfDi4gJO
- [P-ICLR-0155a8] Critical attention scaling in long-context transformers, Shi Chen, Zhengjiang Lin, Yury Polyanskiy et al., ICLR 2025 · https://openreview.net/forum?id=7SLtElfqCW
- [P-ICLR-7e8b20] Graph homophily booster: Reimagining the role of discrete features in heterophilic graph learning, Ruizhong Qiu, Ting-Wei Li, Gaotang Li et al., ICLR 2025 · https://openreview.net/forum?id=owZ6KNAtYU
- [P-ICLR-69d4e7] Trion: FFT-based Dynamic Subspace Selection for Low-Rank Adaptive Optimization of LLMs, Ionut-Vlad Modoranu, Mher Safaryan, Erik Schultheis et al., ICLR 2025 · https://openreview.net/forum?id=TkHjRwbMNl
- [P-ICLR-b986f0] An Efficient SE(p)-Invariant Transport Metric Driven by Polar Transport Discrepancy-based Representation, Junyi Lin, Dunyao Xue, Jun Yu et al., ICLR 2025 · https://openreview.net/forum?id=oyxExc7TEl
- [P-ICLR-2b1d71] Learning Escorted Protocols For Multistate Free-Energy Estimation, Lars Holdijk, Nithishwer Mouroug Anand, Michael M. Bronstein et al., ICLR 2025 · https://openreview.net/forum?id=Da8PJXp0js
- [P-ICLR-6f4ab9] Unified 3D Scene Understanding Through Physical World Modeling, Wanhee Lee, Klemen Kotar, Rahul Mysore Venkatesh et al., ICLR 2025 · https://openreview.net/forum?id=NQq9JLMfNN
- [P-ICLR-9cc020] Adversarial Déjà Vu: Jailbreak Dictionary Learning for Stronger Generalization to Unseen Attacks, Mahavir Dabas, Tran Huynh, Nikhil Reddy Billa et al., ICLR 2025 · https://openreview.net/forum?id=WFo8P1gQBh
- [P-ICLR-01438c] A Scalable Constant-Factor Approximation Algorithm for $W_p$ Optimal Transport, Pankaj K Agarwal, Oliver Chubet, Sharath Raghvendra et al., ICLR 2025 · https://openreview.net/forum?id=RPQKJxrEPs
- [P-ICLR-b7af9b] Sharp asymptotic theory for Q-learning with \texttt{LD2Z} learning rate and its generalization, Soham Bonnerjee, Zhipeng Lou, Wei Biao Wu, ICLR 2025 · https://openreview.net/forum?id=WjEAMyLDoh
- [P-ICLR-a226bf] Learnable Fractional Superlets with a Spectro-Temporal Emotion Encoder for Speech Emotion Recognition, Alaa Nfissi, Wassim Bouachir, Nizar Bouguila et al., ICLR 2025 · https://openreview.net/forum?id=uZGEEL20mU
- [P-ICLR-38fd33] A Representer Theorem for Hawkes Processes via Penalized Least Squares Minimization, Hideaki Kim, Tomoharu Iwata, ICLR 2025 · https://openreview.net/forum?id=gJjRdLG5MY
- [P-ICLR-f0501c] Simulation to Rules: A Dual-VLM Framework for Formal Visual Planning, Yilun Hao, Yongchao Chen, Chuchu Fan et al., ICLR 2025 · https://openreview.net/forum?id=7tlLpQpGlx
- [P-ICLR-41821e] Efficient Testing for Correlation Clustering: Improved Algorithms and Optimal Bounds, Chengyuan Deng, Jie Gao, Songhua He et al., ICLR 2025 · https://openreview.net/forum?id=3AFchYEwRQ
- [P-ICLR-6d1aa9] Poly-attention: a general scheme for higher-order self-attention, Sayak Chakrabarti, Toniann Pitassi, Josh Alman, ICLR 2025 · https://openreview.net/forum?id=amivrmQyvQ
- [P-ICLR-598482] MATHMO: Automated Mathematical Modeling Through Adaptive Search, Tennison Liu, Mihaela van der Schaar, ICLR 2025 · https://openreview.net/forum?id=t2fZ2GOwAT
- [P-ICLR-1c74c2] Two (narrow) heads are better than (an arbitrarily wide) one, Amanuel Tesfaye, Zeno Kujawa, Rajmohan Rajaraman et al., ICLR 2025 · https://openreview.net/forum?id=RRmPbbZsvl
- [P-ICLR-7f4c4d] Decoupling Positional and Symbolic Attention in Transformers, Felipe Urrutia, Jorge Salas, Alexander Kozachinskiy et al., ICLR 2025 · https://openreview.net/forum?id=V38yAoqddQ
- [P-ICLR-ad3787] Mode-conditioning unlocks superior test-time compute scaling, Chen Henry Wu, Sachin Goyal, Aditi Raghunathan, ICLR 2025 · https://openreview.net/forum?id=JzkdJQzPw1
- [P-ICLR-46428d] Learning Concept Bottleneck Models from Mechanistic Explanations, Antonio De Santis, Schrasing Tong, Marco Brambilla et al., ICLR 2025 · https://openreview.net/forum?id=gdEWoxhb70
- [P-ICLR-8a7715] LVTINO: LAtent Video consisTency INverse sOlver for High Definition Video Restoration, Alessio Spagnoletti, Andres Almansa, Marcelo Pereyra, ICLR 2025 · https://openreview.net/forum?id=8SyEcWVe10
- [P-ICLR-51a7aa] DiffBED: Scaling Bayesian Experimental Design to High-Dimensions, Adhi Saravanan, Rik Knowles, Gavin Kerrigan et al., ICLR 2025 · https://openreview.net/forum?id=pNO7VqKAcY
- [P-ICLR-b830a5] Scaling Laws Revisited: Modeling the Role of Data Quality in Language Model Pretraining, Anirudh Subramanyam, Yuxin Chen, Robert L. Grossman, ICLR 2025 · https://openreview.net/forum?id=x54wwB6QvL
- [P-ICLR-4efbe0] Learn to Guide Your Diffusion Model, Alexandre Galashov, Ashwini Pokle, Arnaud Doucet et al., ICLR 2025 · https://openreview.net/forum?id=l8XOk4ylBH
- [P-ICLR-37cf73] Lipschitz Bandits with Stochastic Delayed Feedback, Zhongxuan Liu, Yue Kang, Thomas Lee, ICLR 2025 · https://openreview.net/forum?id=dfoN64vP4Q
- [P-ICLR-5912ae] SPIKE-RL: Video-LLMs meet Bayesian Surprise, Sahithya Ravi, Aditya Chinchure, Raymond T. Ng et al., ICLR 2025 · https://openreview.net/forum?id=QLiXtWEAkq
- [P-ICLR-04394f] BAH Dataset for Ambivalence/Hesitancy Recognition in Videos for  Digital  Behavioural Change, Manuela González-González, Soufiane Belharbi, Muhammad Osama Zeeshan et al., ICLR 2025 · https://openreview.net/forum?id=jYDHVscRO3
- [P-ICLR-cb05a4] Forward-Learned Discrete Diffusion: Learning how to noise to denoise faster, Grigory Bartosh, Teodora Pandeva, Sushrut Karmalkar et al., ICLR 2025 · https://openreview.net/forum?id=45EtKUdgbJ
- [P-ICLR-065c81] Graph Diffusion Transformers are In-Context Molecular Designers, Gang Liu, Jie Chen, Yihan Zhu et al., ICLR 2025 · https://openreview.net/forum?id=lJ87GN5zJc
- [P-ICLR-2eeee0] Shortcut Diffusion Training with Cumulative Consistency Loss: An Optimal Control View, Paribesh Regmi, Sandesh Ghimire, Rui Li, ICLR 2025 · https://openreview.net/forum?id=cZqAk87Lu4
- [P-ICLR-93085b] Decentralized Nonconvex Optimization under Heavy-Tailed Noise: Normalization and Optimal Convergence, Shuhua Yu, Dusan Jakovetic, Soummya Kar, ICLR 2025 · https://openreview.net/forum?id=B0qUqxBOT6
- [P-ICLR-c9ca66] Latent Stochastic Interpolants, Saurabh Singh, Dmitry Lagun, ICLR 2025 · https://openreview.net/forum?id=txiGUfI4yF
- [P-ICLR-fc5565] Understanding the Learning Phases in Self-Supervised Learning via Critical Periods, JangHyeon Lee, Philipe Ambrozio Dias, Yao-Yi Chiang et al., ICLR 2025 · https://openreview.net/forum?id=UxIRc97ecL
- [P-ICLR-34362c] Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching, Ren Kishimoto, Rikiya Takehi, Koichi Tanaka et al., ICLR 2025 · https://openreview.net/forum?id=g2cZaKmRrc
- [P-ICLR-367a98] MCbiF: Measuring Topological Autocorrelation in Multiscale Clusterings via 2-Parameter Persistent Homology, Juni Schindler, Mauricio Barahona, ICLR 2025 · https://openreview.net/forum?id=E7D6uybODJ
- [P-ICLR-ac2eed] Can You Hear Me Now? A Benchmark for Long-Range Graph Propagation, Luca Miglior, Matteo Tolloso, Alessio Gravina et al., ICLR 2025 · https://openreview.net/forum?id=DgkWFPZMPp
- [P-ICLR-2bea2f] Conditional Independent Component Analysis for Estimating Causal Structure with Latent Variables, Yewei Xia, Zhengming Chen, Haoyue Dai et al., ICLR 2025 · https://openreview.net/forum?id=TAOpnCPnjg
- [P-ICLR-877fd4] DreamOn: Diffusion Language Models For Code Infilling Beyond Fixed-size Canvas, Zirui Wu, Lin Zheng, Zhihui Xie et al., ICLR 2025 · https://openreview.net/forum?id=EQTPmqukiU
- [P-ICLR-2ad840] Tracking Equivalent Mechanistic Interpretations Across Neural Networks, Alan Sun, Mariya Toneva, ICLR 2025 · https://openreview.net/forum?id=9lycwRxAOI
- [P-ICLR-4a73e0] Conformal Robustness Control: A New Strategy for Robust Decision, Yang Hu, Jieren Tan, Changliang Zou et al., ICLR 2025 · https://openreview.net/forum?id=bt4Ahpemmi
- [P-ICLR-5aac51] It's All Just Vectorization: einx, a Universal Notation for Tensor Operations, Florian Fervers, Sebastian Bullinger, Christoph Bodensteiner et al., ICLR 2025 · https://openreview.net/forum?id=QqvQ3iAdpC
- [P-ICLR-3606ae] From Large to Small: Transferring CUDA Optimization Expertise via Reasoning Graph, Junfeng Gong, Zhiyi Wei, Junying Chen et al., ICLR 2025 · https://openreview.net/forum?id=vqESUhcSOG
- [P-ICLR-872f15] Mitigating the Curse of Detail: Scaling Arguments for Feature Learning and Sample Complexity, Noa Rubin, Orit Davidovich, Zohar Ringel, ICLR 2025 · https://openreview.net/forum?id=Lexn2TAw59
- [P-ICLR-a9b1c5] MarS-FM: Generative Modeling of Molecular Dynamics via Markov State Models, Kacper Kapuśniak, Cristian Gabellini, Michael M. Bronstein et al., ICLR 2025 · https://openreview.net/forum?id=jP3HnYXoIp
- [P-ICLR-b51591] An Optimal Diffusion Approach to Quadratic Rate-Distortion Problems: New Solution and Approximation Methods, Dror Freirich, Nir Weinberger, ICLR 2025 · https://openreview.net/forum?id=upReXsENIl
- [P-ICLR-ef3c07] To Infinity and Beyond: Tool-Use Unlocks Length Generalization in State Space Models, Eran Malach, Omid Saremi, Sinead Williamson et al., ICLR 2025 · https://openreview.net/forum?id=sSfep4udCb
- [P-ICLR-b69896] Neural Multi-Objective Combinatorial Optimization for Flexible Job Shop Scheduling Problems, Igor G. Smit, Yaoxin Wu, Pavel Troubil et al., ICLR 2025 · https://openreview.net/forum?id=YAgOaYedLQ
- [P-ICLR-9f32b6] Navigating the Latent Space Dynamics of Neural Models, Marco Fumero, Luca Moschella, Emanuele Rodolà et al., ICLR 2025 · https://openreview.net/forum?id=Zunww3FHPU

---

## 메타 / 디버그
- model: gemini-2.5-pro
- backend: gemini-pro-sdk
- matched_n: 100
- matched_total_before_cap: 16541
- window_days: 9999
- tokens_in_uncached: 8791
- tokens_in_cached_read: 125592
- tokens_out: 5975
- usd_estimate: $0.1097
