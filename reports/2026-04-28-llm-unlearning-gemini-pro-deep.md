# Research Topic Suggestion — "llm unlearning"

생성: 2026-04-28T07:54:12.904288+00:00
DB 윈도우: 2026-01-18 ~ 2026-04-28 (100d)
모델: gemini-2.5-pro
매칭 논문: 21건
확장 키워드: ['llm unlearning', 'large language model unlearning', 'machine unlearning for llms', 'model editing in language models', 'knowledge erasure in llms', 'concept erasure from llms', 'selective forgetting in llms', 'data deletion for language models', 'erasing information from llms', 'unlearning harmful knowledge', 'privacy-preserving model editing']

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — Unlearning 알고리즘 고도화
- **설명**: Unlearning의 핵심 목표인 '잊기'와 '기억하기' 간의 균형을 맞추기 위한 새로운 최적화 기법이나 모델 아키텍처를 제안하는 연구 클러스터입니다. 강화학습, 지식 증류, 표현 공간 제어, 그래디언트 충돌 완화 등 다양한 수학적 접근법을 활용합니다.
- **빈도**: 11건
- **월별 (≈25d씩, 오래된→최근)**: 8 → 0 → 0 → 3
- **대표 논문**:
  - [P-2601.20568] Reinforcement Unlearning via Group Relative Policy Optimization — Efstratios Zaradoukas, Bardh Prenkaj, Gjergji Kasneci, arXiv 2026
  - [P-2602.10568] Gauss-Newton Unlearning for the LLM Era — Lev McKinney, Anvith Thudi, Juhan Bae et al., arXiv 2026
  - [P-2604.14808] Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem — Zeguan Xiao, Siqing Li, Yong Wang et al., arXiv 2026

### 클러스터 2 — Unlearning 효과성 및 견고성 검증
- **설명**: 기존 Unlearning 방법론들이 표면적인 정보 억제에 그칠 수 있다는 문제의식에서 출발하여, Unlearning의 실제 효과를 다각도로 검증하는 연구 클러스터입니다. 대화형 질의, 다단계 추론, 적대적 프롬프트 생성 등 정교한 평가 프레임워크와 벤치마크를 제안합니다.
- **빈도**: 4건
- **월별 (≈25d씩, 오래된→최근)**: 1 → 1 → 1 → 1
- **대표 논문**:
  - [P-2603.11266] The Unlearning Mirage: A Dynamic Framework for Evaluating LLM Unlearning — Raj Sanjay Shah, Jing Huang, Keerthiram Murugesan et al., arXiv 2026
  - [P-2602.06248] REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop — Patryk Rybak, Paweł Batorski, Paul Swoboda et al., arXiv 2026
  - [P-2603.00823] A Comprehensive Evaluation of LLM Unlearning Robustness under Multi-Turn Interaction — Ruihao Pan, Suhang Wang, arXiv 2026

### 클러스터 3 — 실용적 제약조건 하의 Unlearning
- **설명**: 실제 모델 배포 및 운영 환경에서 발생하는 특수한 문제들을 해결하기 위한 Unlearning 연구입니다. 대규모 삭제 요청을 순차적으로 처리하거나, 양자화된 모델, 멀티모달 모델에 적용하는 등 특정 도메인 및 제약 조건에 초점을 맞춥니다.
- **빈도**: 6건
- **월별 (≈25d씩, 오래된→최근)**: 4 → 0 → 0 → 2
- **대표 논문**:
  - [P-2601.21682] FIT: Defying Catastrophic Forgetting in Continual LLM Unlearning — Xiaoyu Xu, Minxin Du, Kun Fang et al., arXiv 2026
  - [P-2602.13151] Quantization-Robust LLM Unlearning via Low-Rank Adaptation — João Vitor Boer Abitante, Joana Meneguzzo Pasquali, Luan Fonseca Garcia et al., arXiv 2026
  - [P-2604.12459] Operationalising the Right to be Forgotten in LLMs: A Lightweight Sequential Unlearning Framework for Privacy-Aligned Deployment in Politically Sensitive Environments — Esen Kurt, Haithem Afli, arXiv 2026

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap B — 다수의 Unlearning 연구들이 '잊어야 할 지식(forget set)'과 '보존해야 할 지식(retain set)' 사이의 균형을 맞추는 
- **타입**: recurring-limitation
- **설명**: 다수의 Unlearning 연구들이 '잊어야 할 지식(forget set)'과 '보존해야 할 지식(retain set)' 사이의 균형을 맞추는 것을 목표로 합니다. 그러나 이는 현실적으로 확보하기 어렵거나, 정의하기 모호한 대규모 '보존 데이터셋'에 의존하는 한계를 내포합니다. 일부 연구는 이러한 데이터 의존성을 비실용적이거나 계산 비용이 많이 드는 문제로 명시적으로 지적하며, 이를 해결하려는 시도를 보이고 있습니다.
- **근거 논문**: P-2602.02824, P-2604.16591, P-2602.10568
- **Skeptic 검토**: ✓ 통과 — 보존 데이터셋에 대한 의존성은 여러 논문에서 반복적으로 지적되는 실제적 한계입니다. 일부 논문(예: arxiv:2602.02824)이 이 문제 해결을 시도하고 있지만, 이는 문제가 완전히 해결되었다기보다 현재 활발히 연구가 진행 중인 유효한 갭임을 보여줍니다.

### Gap C — 대부분의 연구가 Unlearning을 유해하거나 민감한 정보를 '제거'하는 수단으로 접근하는 반면, 한 논문은 이를 모델의 잠재 표현을 조작하여
- **타입**: single-shot
- **설명**: 대부분의 연구가 Unlearning을 유해하거나 민감한 정보를 '제거'하는 수단으로 접근하는 반면, 한 논문은 이를 모델의 잠재 표현을 조작하여 특정 행동(예: 진실성, 거절)을 유도하거나 특정 능력(예: 인과관계 추론)을 강화하는 '제어 기술'로 활용할 수 있다는 새로운 관점을 제시합니다. 이 연구는 Unlearning을 소극적 삭제가 아닌 적극적 모델 편집(model editing)의 도구로 재해석했습니다. 하지만 매칭된 다른 논문들에서는 이러한 관점을 채택하거나 후속 연구로 발전시킨 사례가 보이지 않습니다.
- **근거 논문**: P-2601.21702
- **Skeptic 검토**: ✓ 통과 — 제시된 논문 모음 내에서 Unlearning을 단순한 정보 '삭제'가 아닌, 모델의 행동을 적극적으로 '제어'하고 특정 능력을 '강화'하는 수단으로 재해석한 접근은 arxiv:2601.21702에서만 유일하게 나타나는 독창적인 관점으로, 아직 탐구되지 않은 연구 방향입니다.

### Gap D — 핵심 Unlearning 알고리즘(클러스터 1)은 주로 텍스트 기반의 full-precision 모델을 가정하고 개발되지만, 실제 배포 환경에서
- **타입**: between-clusters
- **설명**: 핵심 Unlearning 알고리즘(클러스터 1)은 주로 텍스트 기반의 full-precision 모델을 가정하고 개발되지만, 실제 배포 환경에서는 양자화, 멀티모달리티 등 다양한 제약조건(클러스터 3)이 발생합니다. 관련 연구는 표준적인 Unlearning 기법이 양자화된 모델에서는 효과가 없거나('revert to pre-unlearning behavior'), 멀티모달 모델에 직접 적용하기 어렵다고 보고합니다. 이는 알고리즘의 이론적 성능과 실제 적용 가능성 사이에 괴리가 있음을 의미합니다.
- **근거 논문**: P-2602.13151, P-2601.22020
- **Skeptic 검토**: ✓ 통과 — 클러스터 3의 논문들이 양자화(arxiv:2602.13151)나 멀티모달(arxiv:2601.22020) 같은 특정 제약 조건에 대한 개별적 해결책을 제시하는 반면, 클러스터 1의 핵심 알고리즘 연구들은 이러한 실용적 제약 조건을 고려하지 않아 두 연구 흐름 간의 단절이 명확히 보입니다.

### Gap E — 한 연구는 Unlearning을 특정 알고리즘(예: 다익스트라)에 대한 지식을 모델에서 제거한 뒤, 모델이 해당 알고리즘을 스스로 '재창조'할 
- **타입**: single-shot
- **설명**: 한 연구는 Unlearning을 특정 알고리즘(예: 다익스트라)에 대한 지식을 모델에서 제거한 뒤, 모델이 해당 알고리즘을 스스로 '재창조'할 수 있는지 시험하는 독특한 실험 도구로 활용했습니다. 이는 Unlearning을 LLM의 안전성이나 프라이버시 문제가 아닌, LLM의 근본적인 추론 및 혁신 능력을 탐구하기 위한 수단으로 사용한 유일한 사례입니다. 이러한 접근법은 다른 연구들에서는 전혀 시도되지 않았습니다.
- **근거 논문**: P-2604.05716
- **Skeptic 검토**: ✓ 통과 — Unlearning 기술을 모델의 안전성 개선이 아닌, 모델의 내재된 추론 및 지식 재구성 능력을 탐구하는 과학적 탐침(scientific probe)으로 활용한 arxiv:2604.05716의 접근법은 주어진 논문군 전체에서 유일하며, 이는 매우 독창적이고 미개척된 연구 방향입니다.

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap A** — Unlearning 알고리즘의 발전(클러스터 1)과 평가 방법론의 고도화(클러스터 2)가 별개의 트랙으로 진행되고 있습니다. 평가 연구들은 기존 알고리즘들이 대화형 질의나 적대적 프롬프트 같은 복잡한 상호작용 하에서 쉽게 우회되어 잊었던 정보를 다시 복원해낼 수 있음을 지적합니다. 이는 현재 개발되는 알고리즘들이 정적 벤치마크에 과적합될 수 있으며, 실제 환경에서의 견고성이 부족할 수 있음을 시사합니다. · 거부 사유: (a) 다른 클러스터에서 이미 다룸. 알고리즘 개발 단계(클러스터 1)에서 이미 적대적 견고성을 통합하려는 연구가 존재합니다. 예를 들어, AGTᴬᴼ [arxiv:2602.01703]는 '내부 복구 시도를 시뮬레이션하고 대응'하기 위한 적대적 훈련 메커니즘을 제안하여, 설계부터 견고성 문제를 직접적으로 다루고 있습니다.

</details>

## 3. 연구 제안 (Proposer)

### 제안 1 — SURE
**가설**: 명시적인 보존 데이터셋 없이, 레이블이 없는 일반 말뭉치에 대한 모델의 내부 표현 변화를 최소화하는 정규화 항을 통해 치명적 망각을 방지하고 효과적인 언러닝을 달성할 수 있다.
**메우는 갭**: B
**접근**: 기존의 많은 언러닝 방법론이 보존 데이터셋(Dr)에 의존하여 유틸리티 보존 손실(L_retain)을 계산하는 한계를 극복하고자 한다. 본 연구는 특정 보존 쌍 대신 레이블이 없는 대규모 범용 말뭉치를 활용한다. 언러닝 업데이트 전후, 이 말뭉치에 대한 모델의 핵심 레이어 활성화(activations) 분포 변화를 측정하고, 이 변화를 최소화하는 '자기-표현 보존(self-representation preservation)' 정규화 항을 언러닝 목적 함수에 추가한다. 이 메커니즘은 특정 보존 데이터에 대한 의존성을 제거하여 데이터 수집 비용과 프라이버시 문제를 해결하고 언러닝의 실용성을 높인다.
**Baselines**: Gradient Ascent (GA), PerTA, CATNIP, RWKU benchmark, WMDP benchmark, MUSE benchmark
**예상 기여**: 보존 데이터셋 확보의 어려움이라는 실용적 병목 현상을 해결하는 새로운 언러닝 패러다임을 제시한다. 이는 데이터에 의존하지 않는 정규화 기법을 통해 모델의 일반 성능 저하를 최소화함으로써, 언러닝 기술의 실제 적용 범위를 크게 확장할 것으로 기대된다.
**참고**: P-2602.02824, P-2604.16591, P-2601.22030, P-2602.10568

### 제안 2 — QUAKE
**가설**: 언러닝 최적화 과정에 양자화 연산을 직접 통합함으로써, 양자화 이후에도 언러닝 효과가 안정적으로 유지되는 모델을 만들 수 있다.
**메우는 갭**: D
**접근**: 기존 연구(arxiv:2602.13151)는 LoRA 어댑터에 언러닝을 집중시켜 양자화 후 성능 저하를 완화하지만, 언러닝 알고리즘 자체를 양자화에 강건하게 만들지는 못한다. 본 연구는 언러닝의 그래디언트 업데이트 단계에 '가상 양자화(simulated quantization)'를 직접 통합하는 QUAKE(QUantization-Aware Knowledge Erasure)를 제안한다. 최적화 과정에서 계산된 그래디언트를 모델 파라미터에 적용할 때, 해당 업데이트가 양자화 이후에도 살아남을지 실시간으로 시뮬레이션하고, 양자화 임계값을 넘어서는 의미 있는 변화를 유도하도록 그래디언트를 조정한다. 이 양자화 인식 최적화는 저-비트 환경에서도 정보 삭제 효과의 지속성을 보장한다.
**Baselines**: LoRA-based unlearning, Post-Training Quantization (PTQ), GA+GDR, MLLMU benchmark, MUSE dataset
**예상 기여**: Full-precision 모델에서만 유효했던 기존 언러닝 기법들의 한계를 극복하고, 실제 배포 환경의 필수 제약 조건인 저-비트 양자화 모델에서도 견고하게 작동하는 프레임워크를 제공한다. 이는 언러닝 연구의 이론과 실제 배포 간의 괴리를 해소하는 데 중요한 기여를 할 것이다.
**참고**: P-2602.13151, P-2601.22020, P-2601.21682

### 제안 3 — MARS
**가설**: 언러닝의 표현 공간 조작 기법을 다축(multi-axis) 제어로 확장하여, 단일 최적화 과정에서 상충될 수 있는 여러 목표 행동(예: 진실성 강화 및 유해성 억제)을 동시에 제어할 수 있다.
**메우는 갭**: C
**접근**: Representation misdirection(arxiv:2601.21702)이 단일 목표 벡터로 표현을 유도한 것에서 영감을 얻어, 이를 다차원적 행동 제어로 확장하는 MARS(Multi-Axis Representation Steering)를 제안한다. 먼저 대조적 프롬프팅을 통해 모델의 잠재 공간 내에서 '진실성', '거절', '창의성' 등 서로 직교에 가까운 행동 축(behavioral axes)들을 식별한다. 그 후, 언러닝 과정에서 특정 입력에 대한 잠재 표현을 이 다중 축에 투영(projection)하고, 각 축 방향으로 개별적인 조향력(steering force)을 가하여 모델의 행동을 복합적으로 편집한다. 이는 단일 목표의 정보 삭제를 넘어선 정교하고 다차원적인 모델 행동 제어를 가능하게 한다.
**Baselines**: Representation misdirection, MMLU, CommonsenseQA, GSM8K
**예상 기여**: 언러닝을 정보 삭제라는 수동적 관점에서 벗어나, 모델의 행동과 능력을 정교하게 조각하는 능동적 엔지니어링 도구로 재정의한다. 이는 안전성, 윤리성, 유용성 등 여러 가치를 동시에 만족시키는 모델을 개발하는 새로운 방향을 제시하며, 언러닝의 활용 범위를 모델 편집 및 제어 영역으로 확장한다.
**참고**: P-2601.21702, P-2604.15482, P-2604.14808

## 4. 참고문헌 (메타DB 기반)

### 클러스터 1 — Unlearning 알고리즘 고도화 (11)
- [P-2601.20568] Reinforcement Unlearning via Group Relative Policy Optimization, Efstratios Zaradoukas, Bardh Prenkaj, Gjergji Kasneci, arXiv 2026 · http://arxiv.org/abs/2601.20568v3
- [P-2601.21283] DUET: Distilled LLM Unlearning from an Efficiently Contextualized Teacher, Yisheng Zhong, Zhengbang Yang, Zhuangdi Zhu, arXiv 2026 · http://arxiv.org/abs/2601.21283v2
- [P-2601.22030] Per-parameter Task Arithmetic for Unlearning in Large Language Models, Chengyi Cai, Zesheng Ye, Jiangchao Yao et al., arXiv 2026 · http://arxiv.org/abs/2601.22030v1
- [P-2601.22028] From Logits to Latents: Contrastive Representation Shaping for LLM Unlearning, Haoran Tang, Rajiv Khanna, arXiv 2026 · http://arxiv.org/abs/2601.22028v1
- [P-2602.01703] $\textbf{AGT$^{AO}$}$: Robust and Stabilized LLM Unlearning via Adversarial Gating Training with Adaptive Orthogonality, Pengyu Li, Lingling Zhang, Zhitao Gao et al., arXiv 2026 · http://arxiv.org/abs/2602.01703v1
- [P-2602.02824] CATNIP: LLM Unlearning via Calibrated and Tokenized Negative Preference Alignment, Zhengbang Yang, Yisheng Zhong, Junyuan Hong et al., arXiv 2026 · http://arxiv.org/abs/2602.02824v1
- [P-2603.09980] Explainable LLM Unlearning Through Reasoning, Junfeng Liao, Qizhou Wang, Shanshan Ye et al., arXiv 2026 · http://arxiv.org/abs/2603.09980v1
- [P-2602.10568] Gauss-Newton Unlearning for the LLM Era, Lev McKinney, Anvith Thudi, Juhan Bae et al., arXiv 2026 · http://arxiv.org/abs/2602.10568v1
- [P-2604.17396] Representation-Guided Parameter-Efficient LLM Unlearning, Zeguan Xiao, Lang Mo, Yun Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.17396v1
- [P-2604.15482] Harmonizing Multi-Objective LLM Unlearning via Unified Domain Representation and Bidirectional Logit Distillation, Yisheng Zhong, Sijia Liu, Zhuangdi Zhu, arXiv 2026 · http://arxiv.org/abs/2604.15482v1
- [P-2604.14808] Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem, Zeguan Xiao, Siqing Li, Yong Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.14808v1

### 클러스터 2 — Unlearning 효과성 및 견고성 검증 (4)
- [P-2603.00823] A Comprehensive Evaluation of LLM Unlearning Robustness under Multi-Turn Interaction, Ruihao Pan, Suhang Wang, arXiv 2026 · http://arxiv.org/abs/2603.00823v2
- [P-2602.06248] REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop, Patryk Rybak, Paweł Batorski, Paul Swoboda et al., arXiv 2026 · http://arxiv.org/abs/2602.06248v1
- [P-2603.11266] The Unlearning Mirage: A Dynamic Framework for Evaluating LLM Unlearning, Raj Sanjay Shah, Jing Huang, Keerthiram Murugesan et al., arXiv 2026 · http://arxiv.org/abs/2603.11266v1
- [P-2604.05716] Can Large Language Models Reinvent Foundational Algorithms?, Jian Zhao, Haoren Luo, Yu Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.05716v1 · also_in: hf

### 클러스터 3 — 실용적 제약조건 하의 Unlearning (6)
- [P-2601.21682] FIT: Defying Catastrophic Forgetting in Continual LLM Unlearning, Xiaoyu Xu, Minxin Du, Kun Fang et al., arXiv 2026 · http://arxiv.org/abs/2601.21682v1
- [P-2601.22020] Visual-Guided Key-Token Regularization for Multimodal Large Language Model Unlearning, Chengyi Cai, Zesheng Ye, Peike Li et al., arXiv 2026 · http://arxiv.org/abs/2601.22020v1
- [P-2601.21702] Beyond Forgetting: Machine Unlearning Elicits Controllable Side Behaviors and Capabilities, Tien Dang, The-Hai Nguyen, Dinh Mai Phuong et al., arXiv 2026 · http://arxiv.org/abs/2601.21702v2
- [P-2602.13151] Quantization-Robust LLM Unlearning via Low-Rank Adaptation, João Vitor Boer Abitante, Joana Meneguzzo Pasquali, Luan Fonseca Garcia et al., arXiv 2026 · http://arxiv.org/abs/2602.13151v3
- [P-2604.16591] Randomized Antipodal Search Done Right for Data Pareto Improvement of LLM Unlearning, Ziwen Liu, Huawei Lin, Yide Ran et al., arXiv 2026 · http://arxiv.org/abs/2604.16591v1
- [P-2604.12459] Operationalising the Right to be Forgotten in LLMs: A Lightweight Sequential Unlearning Framework for Privacy-Aligned Deployment in Politically Sensitive Environments, Esen Kurt, Haithem Afli, arXiv 2026 · http://arxiv.org/abs/2604.12459v1

---

## 메타 / 디버그
- model: gemini-2.5-pro
- backend: gemini-pro-sdk
- matched_n: 21
- matched_total_before_cap: 21
- window_days: 100
- tokens_in_uncached: 21784
- tokens_in_cached_read: 25772
- tokens_out: 5093
- usd_estimate: $0.0861
- deep: True
- deep_k: 10
- deep_pdfs_ok: 10
- deep_pdfs_failed: 0
