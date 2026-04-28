# Research Topic Suggestion — "llm unlearning"

생성: 2026-04-28T07:22:51.047560+00:00
DB 윈도우: 2026-02-27 ~ 2026-04-28 (60d)
모델: gemini-2.5-pro
매칭 논문: 17건
확장 키워드: ['llm unlearning', 'large language model unlearning', 'machine unlearning for llms', 'model forgetting', 'data deletion in llms', 'erasing information from llms', 'concept erasure in language models', 'knowledge unlearning', 'selective model editing', 'right to be forgotten']

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — 언러닝 견고성 및 평가
- **설명**: 기존 언러닝 기법의 취약점을 지적하고, 보다 현실적인 대화형 환경이나 적대적 공격 상황에서의 견고성을 평가하는 새로운 프레임워크와 문제점을 정의하는 연구 그룹입니다.
- **빈도**: 4건
- **월별 (≈15d씩, 오래된→최근)**: 3 → 0 → 1 → 0
- **대표 논문**:
  - [P-2603.11266] The Unlearning Mirage: A Dynamic Framework for Evaluating LLM Unlearning — Raj Sanjay Shah, Jing Huang, Keerthiram Murugesan et al., arXiv 2026
  - [P-2603.00823] A Comprehensive Evaluation of LLM Unlearning Robustness under Multi-Turn Interaction — Ruihao Pan, Suhang Wang, arXiv 2026
  - [P-2603.00436] ROKA: Robust Knowledge Unlearning against Adversaries — Jinmyeong Shin, Joshua Tapia, Nicholas Ferreira et al., arXiv 2026

### 클러스터 2 — 차세대 언러닝 알고리즘
- **설명**: 파라미터 수정, 그래디언트 합성, 프롬프트 기반 제어 등 기존의 단순 미세조정을 넘어서는 새로운 언러닝 핵심 방법론을 제안하는 연구 그룹입니다. 효율성, 정확성, 데이터 접근성 등 다양한 제약을 고려합니다.
- **빈도**: 7건
- **월별 (≈15d씩, 오래된→최근)**: 1 → 0 → 0 → 6
- **대표 논문**:
  - [P-2604.14808] Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem — Zeguan Xiao, Siqing Li, Yong Wang et al., arXiv 2026
  - [P-2604.13438] WIN-U: Woodbury-Informed Newton-Unlearning as a retain-free Machine Unlearning Framework — Xingjian Zhao, Mohammad Mohammadi Amiri, Malik Magdon-Ismail, arXiv 2026
  - [P-2604.21251] CAP: Controllable Alignment Prompting for Unlearning in LLMs — Zhaokun Wang, Jinyu Guo, Jingwen Pu et al., arXiv 2026

### 클러스터 3 — 연속 및 연합 언러닝
- **설명**: 일회성 요청이 아닌, 연속적인 삭제 요청이 들어오거나 분산된 데이터 환경에서 언러닝을 수행하는 실용적인 시나리오에 초점을 맞춘 연구 그룹입니다.
- **빈도**: 3건
- **월별 (≈15d씩, 오래된→최근)**: 0 → 1 → 0 → 2
- **대표 논문**:
  - [P-2604.19108] Robust Continual Unlearning against Knowledge Erosion and Forgetting Reversal — Eun-Ju Park, Youjin Shin, Simon S. Woo, arXiv 2026
  - [P-2603.12977] Exact Federated Continual Unlearning for Ridge Heads on Frozen Foundation Models — Yijun Quan, Wentai Wu, Giovanni Montana, arXiv 2026
  - [P-2604.12348] PrivEraserVerify: Efficient, Private, and Verifiable Federated Unlearning — Parthaw Goswami, Md Khairul Islam, Ashfak Yeafi, arXiv 2026

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap A — 클러스터 1('견고성 및 평가')에서는 정적(static)이고 단발성(single-turn)인 기존 평가 방식의 한계를 지적하며 대화형, 다단계
- **타입**: between-clusters
- **설명**: 클러스터 1('견고성 및 평가')에서는 정적(static)이고 단발성(single-turn)인 기존 평가 방식의 한계를 지적하며 대화형, 다단계 추론(multi-hop) 등 더 현실적인 평가 프레임워크를 제안합니다. 하지만 클러스터 2('차세대 언러닝 알고리즘')에서 제안된 새로운 알고리즘들은 대부분 이러한 발전된 평가 프레임워크가 아닌, 기존의 정적 벤치마크를 사용하여 성능을 검증하고 있습니다. 이로 인해 최신 알고리즘들이 실제 환경에서도 견고할지에 대한 검증이 이루어지지 않는 간극이 존재합니다.
- **근거 논문**: P-2603.00823, P-2603.11266
- **Skeptic 검토**: ✓ 통과 — 새로운 알고리즘(클러스터 2)들이 발전된 평가 방법론(클러스터 1)을 채택했다는 증거가 없어, 두 연구 흐름 간의 명백한 단절이 관찰됩니다. 타당한 갭입니다.

### Gap C — 클러스터 2는 그래디언트 합성, 표현 공간 제어 등 정교한 차세대 언러닝 알고리즘을 제안하는 반면, 클러스터 3은 연속적인 삭제 요청이나 연합 
- **타입**: between-clusters
- **설명**: 클러스터 2는 그래디언트 합성, 표현 공간 제어 등 정교한 차세대 언러닝 알고리즘을 제안하는 반면, 클러스터 3은 연속적인 삭제 요청이나 연합 학습 같은 실용적인 시나리오에 초점을 맞춥니다. 그러나 클러스터 2의 발전된 알고리즘들이 클러스터 3의 복잡한 환경(예: 연속적인 요청으로 인한 성능 저하, 분산 환경의 통신 제약)에서 어떻게 작동하고 적용될 수 있는지에 대한 연구는 거의 없습니다.
- **근거 논문**: P-2604.14808, P-2604.19108, P-2603.12977
- **Skeptic 검토**: ✓ 통과 — 클러스터 3의 논문들은 특정 시나리오를 위한 자체적인 기법을 제안할 뿐, 클러스터 2의 범용 고급 알고리즘을 해당 시나리오에 적용 및 검증하는 연구는 보이지 않아 타당한 통합 연구 갭으로 판단됩니다.

### Gap D — 대부분의 언러닝 연구는 LLM을 일반적인 텍스트 생성 모델로 다루지만, 특정 아키텍처나 능력에 초점을 맞춘 연구는 드뭅니다. 'arxiv:260
- **타입**: single-shot
- **설명**: 대부분의 언러닝 연구는 LLM을 일반적인 텍스트 생성 모델로 다루지만, 특정 아키텍처나 능력에 초점을 맞춘 연구는 드뭅니다. 'arxiv:2604.04255' 논문은 유일하게 대규모 추론 모델(LRM)의 언러닝 취약점을 다루며, 언러닝 과정에서 "설득력 있지만 오해의 소지가 있는 추론 과정"을 생성하도록 공격할 수 있음을 보였습니다. 이는 모델의 특정 능력(예: 추론, 멀티모달)과 언러닝의 상호작용이라는 새로운 연구 방향을 제시하지만, 후속 연구가 아직 없습니다.
- **근거 논문**: P-2604.04255
- **Skeptic 검토**: ✓ 통과 — 제시된 논문 외에 모델의 특정 능력(추론 등)과 언러닝의 상호작용을 다룬 연구가 없어, 해당 분야가 아직 미개척 상태라는 주장은 유효합니다.

### Gap E — 실용적인 언러닝을 수행할 때, 개인정보 보호나 비용 문제로 인해 삭제할 데이터를 제외한 나머지 '유지(retain)' 데이터셋 전체에 접근하는 
- **타입**: recurring-limitation
- **설명**: 실용적인 언러닝을 수행할 때, 개인정보 보호나 비용 문제로 인해 삭제할 데이터를 제외한 나머지 '유지(retain)' 데이터셋 전체에 접근하는 것이 불가능할 수 있습니다. 일부 연구('arxiv:2604.13438')는 이러한 '유지 데이터셋 없는(retain-free)' 언러닝을 명시적으로 제안하며 이 문제를 해결하고자 합니다. 하지만 다수의 다른 고급 언러닝 기법들은 여전히 모델의 일반 성능 유지를 위해 유지 데이터셋에 접근할 수 있다고 암묵적으로 가정하고 있어, 현실 적용에 한계를 보입니다.
- **근거 논문**: P-2604.13438, P-2602.23798
- **Skeptic 검토**: ✓ 통과 — 다수의 차세대 알고리즘들(예: arxiv:2604.17396, arxiv:2604.14808)이 명시적으로 유지 데이터셋을 요구하는 반면, 이를 문제로 제기하는 논문(arxiv:2604.13438)도 존재하여 현실적 제약과 연구 방향 간의 괴리가 명확합니다.

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap B** — 다수의 논문이 언러닝의 핵심 과제로 '잊기(forget)'와 '유지하기(retain)' 사이의 균형을 다루지만, 이는 실용적인 언러닝이 만족해야 할 다중 목표 중 일부에 불과합니다. 한 논문은 기존 연구들이 "견고성 및 경계 행동(robustness and boundary behaviors)"과 같은 중요한 목표를 간과하고 있다고 명시적으로 지적합니다. 따라서 망각 효용성, 일반 성능 보존, 관련 개념에 대한 과잉 거부 방지, 적대적 공격에 대한 강건함 등 여러 목표를 동시에 조화롭게 최적화하는 연구는 아직 부족한 상태입니다. · 거부 사유: (a) 다른 클러스터에서 이미 다룸: '견고성(robustness)'과 같은 추가 목표가 간과되고 있다는 주장은 사실과 다릅니다. 클러스터 1('언러닝 견고성 및 평가') 자체가 이 주제를 핵심으로 다루고 있으며, ROKA [arxiv:2603.00436]는 적대적 공격에 대한 견고한 언러닝을 명시적으로 제안합니다.

</details>

## 3. 연구 제안 (Proposer)

### 제안 1 — DYNAMO-BENCH
**가설**: 최신 언러닝 알고리즘들은 정적 평가에서는 높은 성능을 보이지만, 다단계 추론 및 대화형 질의로 구성된 동적 평가 환경에서는 망각했던 지식이 쉽게 복구되어 견고성이 현저히 저하될 것이다.
**메우는 갭**: A
**접근**: 클러스터 2의 대표적인 알고리즘들(SAGO, REGLU 등)을 선별하여, 클러스터 1에서 제안된 동적 평가 프레임워크(다단계 질의 생성, 대화 기반 탐침)를 적용한다. 이를 통해 언러닝 후 모델의 지식 복구율을 측정하고, 정적 벤치마크 결과와의 비교 분석을 통해 성능 저하의 원인을 규명한다. 특히, 활성화 분석을 통해 단일 홉과 다중 홉 질의에 대한 모델의 내부 연산 경로 변화를 추적하여 취약점의 근본 원인을 탐색한다.
**Baselines**: SAGO, REGLU, TOFU, WMDP
**예상 기여**: 최신 언러닝 알고리즘의 현실적인 취약점을 최초로 정량적으로 평가하고, 향후 알고리즘 개발이 지향해야 할 견고성 기준을 제시한다. 이는 정적 벤치마크의 한계를 넘어 실제 환경에서의 안정적인 언러닝 기술 개발을 촉진하는 중요한 근거가 될 것이다.
**참고**: P-2603.00823, P-2603.11266, P-2604.14808, P-2604.17396

### 제안 2 — CASC-RFU
**가설**: 모델의 표현 공간에서 유지(retain) 데이터의 핵심적인 통계적 분포를 소수의 파라미터로 근사하여 저장하면, 전체 유지 데이터셋에 접근하지 않고도 연속적인 언러닝 요청에 대해 지식 침식(Knowledge Erosion)과 망각 역전(Forgetting Reversal)을 효과적으로 방지할 수 있다.
**메우는 갭**: C
**접근**: 초기 모델 학습 시, 유지 데이터의 표현 공간 분포를 저차원 통계적 대리(low-dimensional statistical proxy)로 추출하여 보관한다. 연속적인 언러닝 요청이 들어올 때마다, 이 통계적 대리를 정규화 항으로 사용하여 삭제 대상 데이터의 영향력은 제거하면서도 기존 지식 구조는 보존하도록 최적화한다. 이는 전체 유지 데이터셋에 접근하지 않고도 고급 언러닝 알고리즘의 안정성을 확보하는 방법이다.
**Baselines**: SAFER, WIN-U
**예상 기여**: 실용적인 연속 언러닝 시나리오와 데이터 접근성 제약(retain-free)을 동시에 해결하는 최초의 프레임워크를 제안한다. 이는 고급 언러닝 알고리즘을 현실 세계의 복잡한 요구사항에 맞게 확장하는 중요한 교두보 역할을 할 것이다.
**참고**: P-2604.19108, P-2604.13438, P-2604.17396

### 제안 3 — REASON-GUARD
**가설**: 언러닝 과정에서 모델의 추론 경로(reasoning pathways)를 명시적으로 보존하는 제약 조건을 추가하면, 특정 지식을 삭제하면서도 논리적 일관성을 유지하고 설득력 있는 허위 추론을 생성하는 취약점을 방지할 수 있다.
**메우는 갭**: D
**접근**: 먼저, 삭제 대상 지식과 관련된 추론 경로와 일반적인 논리적 추론에 사용되는 핵심 경로를 활성화 분석을 통해 식별한다. 언러닝 최적화 시, 삭제 대상 경로의 활성화는 억제하면서 핵심 추론 경로의 표현은 원래 상태를 유지하도록 하는 정규화(regularization) 손실을 도입한다. 이를 통해 목표 지식만 정밀하게 제거하고 부수적인 추론 능력 손상을 최소화하여 언러닝 공격에 대한 방어 능력을 확보한다.
**Baselines**: LRM
**예상 기여**: 추론 모델(LRM)을 위한 최초의 방어적 언러닝 기법을 제안하여, 언러닝이 야기하는 새로운 공격 벡터에 대한 해결책을 제시한다. 이는 언러닝 연구의 범위를 일반 텍스트 모델에서 특정 능력을 갖춘 전문화된 모델로 확장하는 계기가 될 것이다.
**참고**: P-2604.04255, P-2603.11266

## 4. 참고문헌 (메타DB 기반)

### 클러스터 1 — 언러닝 견고성 및 평가 (4)
- [P-2603.00823] A Comprehensive Evaluation of LLM Unlearning Robustness under Multi-Turn Interaction, Ruihao Pan, Suhang Wang, arXiv 2026 · http://arxiv.org/abs/2603.00823v2
- [P-2603.00436] ROKA: Robust Knowledge Unlearning against Adversaries, Jinmyeong Shin, Joshua Tapia, Nicholas Ferreira et al., arXiv 2026 · http://arxiv.org/abs/2603.00436v1
- [P-2603.11266] The Unlearning Mirage: A Dynamic Framework for Evaluating LLM Unlearning, Raj Sanjay Shah, Jing Huang, Keerthiram Murugesan et al., arXiv 2026 · http://arxiv.org/abs/2603.11266v1
- [P-2604.04255] Towards Unveiling Vulnerabilities of Large Reasoning Models in Machine Unlearning, Aobo Chen, Chenxu Zhao, Chenglin Miao et al., arXiv 2026 · http://arxiv.org/abs/2604.04255v1

### 클러스터 2 — 차세대 언러닝 알고리즘 (7)
- [P-2602.23798] MPU: Towards Secure and Privacy-Preserving Knowledge Unlearning for Large Language Models, Tiantong Wang, Xinyu Yan, Tiantong Wu et al., arXiv 2026 · http://arxiv.org/abs/2602.23798v1
- [P-2604.21251] CAP: Controllable Alignment Prompting for Unlearning in LLMs, Zhaokun Wang, Jinyu Guo, Jingwen Pu et al., arXiv 2026 · http://arxiv.org/abs/2604.21251v1
- [P-2604.16591] Randomized Antipodal Search Done Right for Data Pareto Improvement of LLM Unlearning, Ziwen Liu, Huawei Lin, Yide Ran et al., arXiv 2026 · http://arxiv.org/abs/2604.16591v1
- [P-2604.17396] Representation-Guided Parameter-Efficient LLM Unlearning, Zeguan Xiao, Lang Mo, Yun Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.17396v1
- [P-2604.15482] Harmonizing Multi-Objective LLM Unlearning via Unified Domain Representation and Bidirectional Logit Distillation, Yisheng Zhong, Sijia Liu, Zhuangdi Zhu, arXiv 2026 · http://arxiv.org/abs/2604.15482v1
- [P-2604.14808] Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem, Zeguan Xiao, Siqing Li, Yong Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.14808v1
- [P-2604.13438] WIN-U: Woodbury-Informed Newton-Unlearning as a retain-free Machine Unlearning Framework, Xingjian Zhao, Mohammad Mohammadi Amiri, Malik Magdon-Ismail, arXiv 2026 · http://arxiv.org/abs/2604.13438v1

### 클러스터 3 — 연속 및 연합 언러닝 (3)
- [P-2603.12977] Exact Federated Continual Unlearning for Ridge Heads on Frozen Foundation Models, Yijun Quan, Wentai Wu, Giovanni Montana, arXiv 2026 · http://arxiv.org/abs/2603.12977v2
- [P-2604.19108] Robust Continual Unlearning against Knowledge Erosion and Forgetting Reversal, Eun-Ju Park, Youjin Shin, Simon S. Woo, arXiv 2026 · http://arxiv.org/abs/2604.19108v1
- [P-2604.12348] PrivEraserVerify: Efficient, Private, and Verifiable Federated Unlearning, Parthaw Goswami, Md Khairul Islam, Ashfak Yeafi, arXiv 2026 · http://arxiv.org/abs/2604.12348v1

### 기타 (클러스터 미분류) (3)
- [P-2603.20292] HSI Image Enhancement Classification Based on Knowledge Distillation: A Study on Forgetting, Songfeng Zhu, arXiv 2026 · http://arxiv.org/abs/2603.20292v1
- [P-2604.12459] Operationalising the Right to be Forgotten in LLMs: A Lightweight Sequential Unlearning Framework for Privacy-Aligned Deployment in Politically Sensitive Environments, Esen Kurt, Haithem Afli, arXiv 2026 · http://arxiv.org/abs/2604.12459v1
- [P-2604.05716] Can Large Language Models Reinvent Foundational Algorithms?, Jian Zhao, Haoren Luo, Yu Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.05716v1 · also_in: hf

---

## 메타 / 디버그
- model: gemini-2.5-pro
- backend: gemini-pro-sdk
- matched_n: 17
- matched_total_before_cap: 17
- window_days: 60
- tokens_in_uncached: 6150
- tokens_in_cached_read: 20096
- tokens_out: 4775
- usd_estimate: $0.0617
