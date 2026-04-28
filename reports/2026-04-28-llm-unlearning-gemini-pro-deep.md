# Research Topic Suggestion — "llm unlearning"

생성: 2026-04-28T08:21:24.785345+00:00
DB 윈도우: 2026-01-18 ~ 2026-04-28 (100d)
모델: gemini-2.5-pro
매칭 논문: 100건
확장 키워드: ['llm unlearning', 'large language model unlearning', 'machine unlearning', 'model editing', 'concept erasure', 'knowledge unlearning', 'selective model forgetting', 'data deletion from models', 'fine-tuning for unlearning', 'right to be forgotten']

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — 생성 모델 개념 제거
- **설명**: 텍스트-이미지 변환 등 생성 모델에서 특정 객체, 스타일, 저작권 등 원치 않는 개념을 제거하는 방법론에 초점을 맞춘 연구 그룹입니다. 모델의 생성 품질 저하를 최소화하면서 특정 개념만 정교하게 삭제하는 기술을 다룹니다.
- **빈도**: 17건
- **월별 (≈25d씩, 오래된→최근)**: 3 → 6 → 2 → 6
- **대표 논문**:
  - [P-2604.16481] Erasing Thousands of Concepts: Towards Scalable and Practical Concept Erasure for Text-to-Image Diffusion Models — Hoigi Seo, Byung Hyun Lee, Jaehyun Cho et al., arXiv 2026
  - [P-2604.21041] Projected Gradient Unlearning for Text-to-Image Diffusion Models: Defending Against Concept Revival Attacks — Aljalila Aladawi, Mohammed Talha Alam, Fakhri Karray, arXiv 2026
  - [P-2603.00978] EraseAnything++: Enabling Concept Erasure in Rectified Flow Transformers Leveraging Multi-Object Optimization — Zhaoxin Fan, Nanxiang Jiang, Daiheng Gao et al., arXiv 2026

### 클러스터 2 — 언러닝 알고리즘 및 프레임워크
- **설명**: 특정 데이터를 잊도록 모델 파라미터를 수정하는 새로운 알고리즘과 최적화 프레임워크를 제안하는 연구 그룹입니다. 성능 저하를 최소화하면서 효율적이고 정교하게 지식을 제거하는 방법론에 중점을 둡니다.
- **빈도**: 21건
- **월별 (≈25d씩, 오래된→최근)**: 2 → 3 → 2 → 14
- **대표 논문**:
  - [P-2604.21571] Separable Expert Architecture: Toward Privacy-Preserving LLM Personalization via Composable Adapters and Deletable User Proxies — Chris Schneider, Philipp Schoenegger, Ben Bariach, arXiv 2026
  - [P-2604.21251] CAP: Controllable Alignment Prompting for Unlearning in LLMs — Zhaokun Wang, Jinyu Guo, Jingwen Pu et al., arXiv 2026
  - [P-2604.14808] Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem — Zeguan Xiao, Siqing Li, Yong Wang et al., arXiv 2026

### 클러스터 3 — 언러닝의 한계와 평가
- **설명**: 언러닝 기술의 실효성과 취약점을 분석하고, 보다 신뢰성 있는 평가 방법론을 제안하는 연구 그룹입니다. 언러닝 후에도 정보가 잔존하는 현상이나 의도치 않은 부작용(ripple effects) 등을 탐구합니다.
- **빈도**: 15건
- **월별 (≈25d씩, 오래된→최근)**: 5 → 1 → 5 → 4
- **대표 논문**:
  - [P-2604.22076] PrivUn: Unveiling Latent Ripple Effects and Shallow Forgetting in Privacy Unlearning — Xiaoyi Chen, Haoyuan Wang, Siyuan Tang et al., arXiv 2026
  - [P-2604.08271] An Illusion of Unlearning? Assessing Machine Unlearning Through Internal Representations — Yichen Gao, Altay Unal, Akshay Rangamani et al., arXiv 2026
  - [P-2604.07962] Is your algorithm unlearning or untraining? — Eleni Triantafillou, Ahmed Imtiaz Humayun, Monica Ribero et al., arXiv 2026

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap A — 생성 모델(Cluster 1)의 개념 제거 기술은 빠르게 발전하고 있으나, 그것을 검증할 평가 및 공격 프레임워크(Cluster 3)는 아직 초
- **타입**: between-clusters
- **설명**: 생성 모델(Cluster 1)의 개념 제거 기술은 빠르게 발전하고 있으나, 그것을 검증할 평가 및 공격 프레임워크(Cluster 3)는 아직 초기 단계에 머물러 있습니다. 특히 LLM을 대상으로 개발된 정교한 평가 방법론(예: 다중 턴 상호작용, 구조적 쿼리를 통한 복원 시도)이 생성 모델의 시각적 콘텐츠 제거 효과를 검증하는 데에는 거의 적용되지 않고 있습니다. T2V 모델의 '시간적 재발현' 현상(arxiv:2603.21547)이나 텍스트 중심 방어의 맹점을 파고드는 공격(arxiv:2603.17828) 등은 생성 모델에 특화된 평가의 필요성을 보여줍니다.
- **근거 논문**: P-2603.21547, P-2603.17828, P-2603.00823, P-2603.11266
- **Skeptic 검토**: ✓ 통과 — 클러스터 3이 언러닝 평가를 다루지만, 증거 논문들은 생성 모델(특히 비디오)의 시간적 특성이나 시각적 공격 벡터 등 LLM 중심 평가론으로 해결되지 않는 고유한 문제가 있음을 명확히 보여주므로, 특화된 평가 프레임워크의 부재는 유효한 갭입니다.

### Gap B — 다수의 논문들이 특정 정보를 제거할 때 의도치 않게 관련 있는 다른 지식까지 손상시키는 '리플 효과(ripple effects)' 또는 '부수적
- **타입**: recurring-limitation
- **설명**: 다수의 논문들이 특정 정보를 제거할 때 의도치 않게 관련 있는 다른 지식까지 손상시키는 '리플 효과(ripple effects)' 또는 '부수적 피해(collateral damage)'를 공통적인 한계로 지적합니다. 이는 모델 내에서 지식 표현들이 서로 '얽혀(entangled)' 있기 때문에 발생하는 근본적인 문제입니다. 예를 들어, 한 인종 그룹을 잊게 학습시켰더니 편향이 다른 그룹으로 전이(arxiv:2604.08111)되거나, 특정 개념을 억제하니 의미적으로 유사한 이웃 개념까지 약화(arxiv:2603.25994)되는 현상이 보고되었습니다.
- **근거 논문**: P-2604.22076, P-2603.26569, P-2604.08111, P-2603.25994
- **Skeptic 검토**: ✓ 통과 — 일부 연구가 리플 효과를 '완화'하려 시도하지만, 언러닝 수행 '전'에 어떤 관련 지식이 영향을 받을지 그 범위를 '예측'하고 통제하는 방법론은 여전히 부재합니다. 이는 사후 대응을 넘어선 근본적인 문제이므로 갭으로 인정됩니다.

### Gap C — 대부분의 기술 논문들이 언러닝을 데이터 프라이버시 및 저작권 문제의 실용적인 해결책으로 가정하고 접근하는 반면, 'arxiv:2604.18649
- **타입**: single-shot
- **설명**: 대부분의 기술 논문들이 언러닝을 데이터 프라이버시 및 저작권 문제의 실용적인 해결책으로 가정하고 접근하는 반면, 'arxiv:2604.18649' 논문은 법적 관점에서 근본적인 이의를 제기합니다. 이 논문은 불법적으로 수집된 데이터로 학습한 행위 자체가 이미 완료된 침해이며, 사후적인 언러닝으로는 법적 책임을 소급하여 '치유'할 수 없다고 주장합니다. 이는 언러닝의 기술적 효용성과 별개로, 그 법적-철학적 전제를 문제 삼는 독자적인 시각입니다.
- **근거 논문**: P-2604.18649
- **Skeptic 검토**: ✓ 통과 — 이 갭은 기술적 해결책이 아닌, 언러닝이라는 접근법 자체의 법적-철학적 전제에 대한 근본적인 도전입니다. 다른 클러스터에서 다루는 기술적 방법론들과는 차원이 다른 문제 제기이므로 명백한 갭입니다.

### Gap E — 추론 과정을 단계별로 생성하는 대규모 추론 모델(LRM)에서의 언러닝은 특별한 과제를 제시합니다. 일반적인 언러닝 알고리즘(Cluster 2)은
- **타입**: between-clusters
- **설명**: 추론 과정을 단계별로 생성하는 대규모 추론 모델(LRM)에서의 언러닝은 특별한 과제를 제시합니다. 일반적인 언러닝 알고리즘(Cluster 2)은 주로 최종 결과물에 초점을 맞추지만, LRM에서는 중간 추론 과정(chain-of-thought)에 남은 정보를 제거하면서도 전체적인 논리 흐름을 깨뜨리지 않아야 합니다. 여러 논문(arxiv:2604.15847, arxiv:2604.03571)은 기존 방법들이 추론 능력을 저하시키거나 CoT에서 정보를 완전히 제거하지 못하는 딜레마에 빠진다고 지적합니다.
- **근거 논문**: P-2604.15847, P-2604.04255, P-2604.03571
- **Skeptic 검토**: ✓ 통과 — LRM의 Chain-of-Thought 구조는 표준 언러닝 알고리즘이 고려하지 않는 새로운 제약(논리적 일관성 유지)을 부과합니다. 증거 논문들이 이 문제를 해결하기 시작했지만, 이는 해당 분야가 이제 막 형성되고 있음을 보여주며, 견고한 방법론의 부재는 여전히 중요한 갭입니다.

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap D** — 많은 언러닝 알고리즘들이 실제 배포 환경에서는 충족하기 어려운 비현실적인 가정을 전제로 합니다. 예를 들어, 잊어야 할 'forget set' 데이터(arxiv:2604.10636), 보존해야 할 'retain set' 데이터(arxiv:2604.13438), 또는 모델의 모든 가중치에 대한 접근(arxiv:2604.21251)을 요구하는 경우가 많습니다. 이는 API 형태로 제공되는 비공개 모델이나, 엄격한 데이터 보관 규정이 있는 상황에서는 적용이 불가능합니다. · 거부 사유: 이미 클러스터 2에서 다룸. 이 갭은 '연구가 부족하다'고 주장하지만, 제시된 증거 논문들(arxiv:2604.21251, arxiv:2604.13438, arxiv:2604.10636) 자체가 바로 그 문제에 대한 해결책들입니다. 이는 갭이 아니라 이미 활발히 연구되고 있는 하위 분야입니다.

</details>

## 3. 연구 제안 (Proposer)

### 제안 1 — PRE-MAP
**가설**: 언러닝 수행 전 잊을 대상과 관련된 '그래디언트 영향 그래프'를 구축하면, 리플 효과를 예측하고 제어하여 관련 지식의 손실 없이 목표 지식만 정교하게 제거할 수 있다.
**메우는 갭**: B
**접근**: 본 프레임워크는 먼저 잊을 데이터셋과 유지할 데이터셋 샘플 간의 그래디언트 유사도를 계산하여 '잠재적 리플 효과 그래프'를 생성한다. 이 그래프에서 잊을 노드와 강하게 연결된 '취약 이웃' 노드들을 식별한다. 이후, 기존 언러닝 알고리즘에 이 취약 이웃 노드들의 표현을 보존하는 제약 조건을 추가하여, 언러닝의 영향이 목표 개념에만 국한되도록 최적화를 유도한다.
**Baselines**: Methods: PGU, GA, NPO; Evaluation: PrivUn framework; Datasets: CelebA, Waterbirds
**예상 기여**: 기존의 사후 대응 방식에서 벗어나, 언러닝으로 인한 부수적 피해를 사전에 예측하고 통제하는 최초의 프레임워크를 제안한다. 이를 통해 모델의 안정성을 해치지 않으면서도 안전하고 정밀한 지식 제거가 가능해진다.
**참고**: P-2604.22076, P-2604.08111, P-2603.26569, P-2602.21773

### 제안 2 — LOGI-REDACT
**가설**: 대규모 추론 모델(LRM)의 연쇄적 사고(CoT)에서 민감 정보를 포함하는 최소한의 논리적 단계만 식별하여 중립적인 자리표시자로 '편집'하는 방식은, 전체 추론 과정을 대체하는 것보다 추론 능력을 더 잘 보존하면서 효과적으로 정보를 제거할 수 있다.
**메우는 갭**: E
**접근**: 먼저 인과관계 추적(causal tracing) 기법을 활용하여 CoT 내에서 잊고자 하는 정보 생성에 결정적인 기여를 하는 토큰 및 추론 단계를 식별한다. 그 다음, 식별된 단계를 완전한 반사실적 추론으로 대체하는 대신, 논리적 흐름을 유지하는 중립적 구문(예: '이전 단계에 따라')으로 대체하는 '논리 보존 편집'을 수행한다. 이 편집된 CoT를 정답으로 삼아 모델을 소폭 미세조정하여, 민감 정보의 발현 경로를 차단하면서도 기존 추론 구조의 손상을 최소화한다.
**Baselines**: Methods: CiPO; Models: LLaMA-3, Mistral
**예상 기여**: LRM 언러닝을 위한 새로운 '최소 편집' 패러다임을 제시하여, 추론 능력 저하라는 기존 방법들의 핵심적인 한계를 극복한다. 이는 복잡한 추론 과정에서도 정밀한 정보 통제를 가능하게 하는 실용적인 해결책이 될 것이다.
**참고**: P-2604.15847, P-2604.03571, P-2604.04255

### 제안 3 — DREAM
**가설**: 미세조정을 통한 개념 부활, 시계열 데이터에서의 점진적 재발현, 텍스트와 무관한 시각적 역공격 등 다양한 공격 벡터를 통합한 동적 평가 프레임워크는, 정적 결과물 분석만으로는 발견할 수 없는 생성 모델 언러닝의 치명적인 취약점을 드러낼 것이다.
**메우는 갭**: A
**접근**: 본 '동적 재구성 및 회피 감사 프레임워크(DREAM)'는 세 가지 모듈을 통합한다. 첫째, '개념 부활 모듈'은 관련 없는 데이터로 미세조정을 수행하여 제거된 개념이 복원되는지 자동으로 탐지한다. 둘째, '시간적 재발현 모듈'은 비디오 생성 모델의 프레임 전반에 걸쳐 제거된 개념이 점진적으로 다시 나타나는 현상을 정량화한다. 마지막으로, '교차 모달 역공격 모듈'은 제거된 개념과 무관한 텍스트 프롬프트를 사용하여 모델 내에 잔존하는 시각적 지식을 강제로 활성화시키려 시도한다.
**Baselines**: Methods: PGU, ESD, UCE, Receler; Models: Stable Diffusion, T2V models; Attacks: TINA
**예상 기여**: 생성 모델의 개념 제거 기술에 대한 최초의 통합적이고 자동화된 스트레스 테스트 프레임워크를 제공한다. 이는 단순히 개념이 '보이지 않는가'를 넘어 '어떤 조건에서도 복원될 수 없는가'를 검증하는 새로운 평가 표준을 제시하여, 보다 견고하고 안전한 생성 AI 개발을 촉진할 것이다.
**참고**: P-2603.21547, P-2603.17828, P-2604.21041, P-2603.00823

## 4. 참고문헌 (메타DB 기반)

### 클러스터 1 — 생성 모델 개념 제거 (17)
- [P-2604.21041] Projected Gradient Unlearning for Text-to-Image Diffusion Models: Defending Against Concept Revival Attacks, Aljalila Aladawi, Mohammed Talha Alam, Fakhri Karray, arXiv 2026 · http://arxiv.org/abs/2604.21041v1
- [P-2604.15829] Beyond Text Prompts: Precise Concept Erasure through Text-Image Collaboration, Jun Li, Lizhi Xiong, Ziqiang Li et al., arXiv 2026 · http://arxiv.org/abs/2604.15829v1
- [P-2604.16483] Dynamic Eraser for Guided Concept Erasure in Diffusion Models, Qinghui Gong, arXiv 2026 · http://arxiv.org/abs/2604.16483v1
- [P-2604.16481] Erasing Thousands of Concepts: Towards Scalable and Practical Concept Erasure for Text-to-Image Diffusion Models, Hoigi Seo, Byung Hyun Lee, Jaehyun Cho et al., arXiv 2026 · http://arxiv.org/abs/2604.16481v1
- [P-2604.10032] Closed-Form Concept Erasure via Double Projections, Chi Zhang, Jingpu Cheng, Zhixian Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.10032v1
- [P-2604.09405] EGLOCE: Training-Free Energy-Guided Latent Optimization for Concept Erasure, Junyeong Ahn, Seojin Yoon, Sungyong Baik, arXiv 2026 · http://arxiv.org/abs/2604.09405v1
- [P-2603.25994] Neighbor-Aware Localized Concept Erasure in Text-to-Image Diffusion Models, Zhuan Shi, Alireza Dehghanpour Farashah, Rik de Vries et al., arXiv 2026 · http://arxiv.org/abs/2603.25994v1
- [P-2603.25074] Z-Erase: Enabling Concept Erasure in Single-Stream Diffusion Transformers, Nanxiang Jiang, Zhaoxin Fan, Baisen Wang et al., arXiv 2026 · http://arxiv.org/abs/2603.25074v1
- [P-2603.21547] PROBE: Diagnosing Residual Concept Capacity in Erased Text-to-Video Diffusion Models, Yiwei Xie, Zheng Zhang, Ping Liu, arXiv 2026 · http://arxiv.org/abs/2603.21547v1
- [P-2603.17828] TINA: Text-Free Inversion Attack for Unlearned Text-to-Image Diffusion Models, Qianlong Xiang, Miao Zhang, Haoyu Zhang et al., arXiv 2026 · http://arxiv.org/abs/2603.17828v1
- [P-2603.16489] Unlearning for One-Step Generative Models via Unbalanced Optimal Transport, Hyundo Choi, Junhyeong An, Jinseong Park et al., arXiv 2026 · http://arxiv.org/abs/2603.16489v1
- [P-2603.11493] OrthoEraser: Coupled-Neuron Orthogonal Projection for Concept Erasure, Chuancheng Shi, Wenhua Wu, Fei Shen et al., arXiv 2026 · http://arxiv.org/abs/2603.11493v1
- [P-2603.10445] Unlearning the Unpromptable: Prompt-free Instance Unlearning in Diffusion Models, Kyungryeol Lee, Kyeonghyun Lee, Seongmin Hong et al., arXiv 2026 · http://arxiv.org/abs/2603.10445v2
- [P-2603.08271] Prototype-Guided Concept Erasure in Diffusion Models, Yuze Cai, Jiahao Lu, Hongxiang Shi et al., arXiv 2026 · http://arxiv.org/abs/2603.08271v1
- [P-2603.00992] Compensation-free Machine Unlearning in Text-to-Image Diffusion Models by Eliminating the Mutual Information, Xinwen Cheng, Jingyuan Zhang, Zhehao Huang et al., arXiv 2026 · http://arxiv.org/abs/2603.00992v1
- [P-2603.00978] EraseAnything++: Enabling Concept Erasure in Rectified Flow Transformers Leveraging Multi-Object Optimization, Zhaoxin Fan, Nanxiang Jiang, Daiheng Gao et al., arXiv 2026 · http://arxiv.org/abs/2603.00978v1
- [P-2602.19631] Localized Concept Erasure in Text-to-Image Diffusion Models via High-Level Representation Misdirection, Uichan Lee, Jeonghyeon Kim, Sangheum Hwang, arXiv 2026 · http://arxiv.org/abs/2602.19631v1

### 클러스터 2 — 언러닝 알고리즘 및 프레임워크 (21)
- [P-2604.21571] Separable Expert Architecture: Toward Privacy-Preserving LLM Personalization via Composable Adapters and Deletable User Proxies, Chris Schneider, Philipp Schoenegger, Ben Bariach, arXiv 2026 · http://arxiv.org/abs/2604.21571v1
- [P-2604.21251] CAP: Controllable Alignment Prompting for Unlearning in LLMs, Zhaokun Wang, Jinyu Guo, Jingwen Pu et al., arXiv 2026 · http://arxiv.org/abs/2604.21251v1
- [P-2604.17396] Representation-Guided Parameter-Efficient LLM Unlearning, Zeguan Xiao, Lang Mo, Yun Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.17396v1
- [P-2604.16591] Randomized Antipodal Search Done Right for Data Pareto Improvement of LLM Unlearning, Ziwen Liu, Huawei Lin, Yide Ran et al., arXiv 2026 · http://arxiv.org/abs/2604.16591v1
- [P-2604.15847] CiPO: Counterfactual Unlearning for Large Reasoning Models through Iterative Preference Optimization, Junyi Li, Yongqiang Chen, Ningning Ding, arXiv 2026 · http://arxiv.org/abs/2604.15847v1
- [P-2604.15482] Harmonizing Multi-Objective LLM Unlearning via Unified Domain Representation and Bidirectional Logit Distillation, Yisheng Zhong, Sijia Liu, Zhuangdi Zhu, arXiv 2026 · http://arxiv.org/abs/2604.15482v1
- [P-2604.15166] Class Unlearning via Depth-Aware Removal of Forget-Specific Directions, Arman Hatami, Romina Aalishah, Ilya E. Monosov, arXiv 2026 · http://arxiv.org/abs/2604.15166v1
- [P-2604.14808] Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem, Zeguan Xiao, Siqing Li, Yong Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.14808v1
- [P-2604.13777] From Anchors to Supervision: Memory-Graph Guided Corpus-Free Unlearning for Large Language Models, Wenxuan Li, Zhenfei Zhang, Mi Zhang et al., arXiv 2026 · http://arxiv.org/abs/2604.13777v1
- [P-2604.13438] WIN-U: Woodbury-Informed Newton-Unlearning as a retain-free Machine Unlearning Framework, Xingjian Zhao, Mohammad Mohammadi Amiri, Malik Magdon-Ismail, arXiv 2026 · http://arxiv.org/abs/2604.13438v1
- [P-2604.12820] RePAIR: Interactive Machine Unlearning through Prompt-Aware Model Repair, Jagadeesh Rachapudi, Pranav Singh, Ritali Vatsi et al., arXiv 2026 · http://arxiv.org/abs/2604.12820v1
- [P-2604.12686] BID-LoRA: A Parameter-Efficient Framework for Continual Learning and Unlearning, Jagadeesh Rachapudi, Ritali Vatsi, Praful Hambarde et al., arXiv 2026 · http://arxiv.org/abs/2604.12686v1
- [P-2604.12526] Orthogonal Subspace Projection for Continual Machine Unlearning via SVD-Based LoRA, Yogachandran Rahulamathavan, Nasir Iqbal, Juncheng Hu et al., arXiv 2026 · http://arxiv.org/abs/2604.12526v1
- [P-2604.10636] Mitigating Privacy Risk via Forget Set-Free Unlearning, Aviraj Newatia, Michael Cooper, Viet Nguyen et al., arXiv 2026 · http://arxiv.org/abs/2604.10636v1
- [P-2604.04231] Subspace Control: Turning Constrained Model Steering into Controllable Spectral Optimization, Yancheng Huang, Changsheng Wang, Chongyu Fan et al., arXiv 2026 · http://arxiv.org/abs/2604.04231v1
- [P-2603.26569] Machine Unlearning under Retain-Forget Entanglement, Jingpu Cheng, Ping Liu, Qianxiao Li et al., arXiv 2026 · http://arxiv.org/abs/2603.26569v1
- [P-2603.15033] Rethinking Machine Unlearning: Models Designed to Forget via Key Deletion, Sonia Laguna, Jorge da Silva Goncalves, Moritz Vandenhirtz et al., arXiv 2026 · http://arxiv.org/abs/2603.15033v3
- [P-2603.12915] Stake the Points: Structure-Faithful Instance Unlearning, Kiseong Hong, JungKyoo Shin, Eunwoo Kim, arXiv 2026 · http://arxiv.org/abs/2603.12915v1
- [P-2603.11210] Reference-Guided Machine Unlearning, Jonas Mirlach, Sonia Laguna, Julia E. Vogt, arXiv 2026 · http://arxiv.org/abs/2603.11210v1
- [P-2602.23798] MPU: Towards Secure and Privacy-Preserving Knowledge Unlearning for Large Language Models, Tiantong Wang, Xinyu Yan, Tiantong Wu et al., arXiv 2026 · http://arxiv.org/abs/2602.23798v1
- [P-2602.23400] U-CAN: Utility-Aware Contrastive Attenuation for Efficient Unlearning in Generative Recommendation, Zezheng Wu, Rui Wang, Xinghe Cheng et al., arXiv 2026 · http://arxiv.org/abs/2602.23400v1

### 클러스터 3 — 언러닝의 한계와 평가 (15)
- [P-2604.22076] PrivUn: Unveiling Latent Ripple Effects and Shallow Forgetting in Privacy Unlearning, Xiaoyi Chen, Haoyuan Wang, Siyuan Tang et al., arXiv 2026 · http://arxiv.org/abs/2604.22076v1
- [P-2604.19108] Robust Continual Unlearning against Knowledge Erosion and Forgetting Reversal, Eun-Ju Park, Youjin Shin, Simon S. Woo, arXiv 2026 · http://arxiv.org/abs/2604.19108v1
- [P-2604.18649] Position: No Retroactive Cure for Infringement during Training, Satoru Utsunomiya, Masaru Isonuma, Junichiro Mori et al., arXiv 2026 · http://arxiv.org/abs/2604.18649v1
- [P-2604.16536] Towards Reliable Testing of Machine Unlearning, Anna Mazhar, Sainyam Galhotra, arXiv 2026 · http://arxiv.org/abs/2604.16536v1
- [P-2604.08271] An Illusion of Unlearning? Assessing Machine Unlearning Through Internal Representations, Yichen Gao, Altay Unal, Akshay Rangamani et al., arXiv 2026 · http://arxiv.org/abs/2604.08271v1
- [P-2604.08111] Bias Redistribution in Visual Machine Unlearning: Does Forgetting One Group Harm Another?, Yunusa Haruna, Adamu Lawan, Ibrahim Haruna Abdulhamid et al., arXiv 2026 · http://arxiv.org/abs/2604.08111v1
- [P-2604.07962] Is your algorithm unlearning or untraining?, Eleni Triantafillou, Ahmed Imtiaz Humayun, Monica Ribero et al., arXiv 2026 · http://arxiv.org/abs/2604.07962v1
- [P-2604.04255] Towards Unveiling Vulnerabilities of Large Reasoning Models in Machine Unlearning, Aobo Chen, Chenxu Zhao, Chenglin Miao et al., arXiv 2026 · http://arxiv.org/abs/2604.04255v1
- [P-2604.03114] Can VLMs Truly Forget? Benchmarking Training-Free Visual Concept Unlearning, Zhangyun Tan, Zeliang Zhang, Susan Liang et al., arXiv 2026 · http://arxiv.org/abs/2604.03114v1
- [P-2603.11266] The Unlearning Mirage: A Dynamic Framework for Evaluating LLM Unlearning, Raj Sanjay Shah, Jing Huang, Keerthiram Murugesan et al., arXiv 2026 · http://arxiv.org/abs/2603.11266v1
- [P-2603.00823] A Comprehensive Evaluation of LLM Unlearning Robustness under Multi-Turn Interaction, Ruihao Pan, Suhang Wang, arXiv 2026 · http://arxiv.org/abs/2603.00823v2
- [P-2603.00587] Unlearning Evaluation through Subset Statistical Independence, Chenhao Zhang, Muxing Li, Feng Liu et al., arXiv 2026 · http://arxiv.org/abs/2603.00587v1
- [P-2603.00436] ROKA: Robust Knowledge Unlearning against Adversaries, Jinmyeong Shin, Joshua Tapia, Nicholas Ferreira et al., arXiv 2026 · http://arxiv.org/abs/2603.00436v1
- [P-2602.21773] Easy to Learn, Yet Hard to Forget: Towards Robust Unlearning Under Bias, JuneHyoung Kwon, MiHyeon Kim, Eunju Lee et al., arXiv 2026 · http://arxiv.org/abs/2602.21773v1 · also_in: hf
- [P-2602.19612] Anatomy of Unlearning: The Dual Impact of Fact Salience and Model Fine-Tuning, Borisiuk Anna, Andrey Savchenko, Alexander Panchenko et al., arXiv 2026 · http://arxiv.org/abs/2602.19612v2

### 기타 (클러스터 미분류) (47)
- [P-2604.21640] Task-specific Subnetwork Discovery in Reinforcement Learning for Autonomous Underwater Navigation, Yi-Ling Liu, Melvin Laux, Mariela De Lucas Alvarez et al., arXiv 2026 · http://arxiv.org/abs/2604.21640v1
- [P-2604.16170] neuralCAD-Edit: An Expert Benchmark for Multimodal-Instructed 3D CAD Model Editing, Toby Perrett, Matthew Bouchard, William McCarthy, arXiv 2026 · http://arxiv.org/abs/2604.16170v1
- [P-2604.12459] Operationalising the Right to be Forgotten in LLMs: A Lightweight Sequential Unlearning Framework for Privacy-Aligned Deployment in Politically Sensitive Environments, Esen Kurt, Haithem Afli, arXiv 2026 · http://arxiv.org/abs/2604.12459v1
- [P-2604.12348] PrivEraserVerify: Efficient, Private, and Verifiable Federated Unlearning, Parthaw Goswami, Md Khairul Islam, Ashfak Yeafi, arXiv 2026 · http://arxiv.org/abs/2604.12348v1
- [P-2604.12559] FABLE: Fine-grained Fact Anchoring for Unstructured Model Editing, Peng Wang, Biyu Zhou, Xuehai Tang et al., arXiv 2026 · http://arxiv.org/abs/2604.12559v1
- [P-2604.13127] Graph Propagated Projection Unlearning: A Unified Framework for Vision and Audio Discriminative Models, Shreyansh Pathak, Jyotishman Das, arXiv 2026 · http://arxiv.org/abs/2604.13127v1
- [P-2604.11511] The Price of Ignorance: Information-Free Quotation for Data Retention in Machine Unlearning, Bin Han, Di Feng, Zexin Fang et al., arXiv 2026 · http://arxiv.org/abs/2604.11511v1
- [P-2604.11214] HiEdit: Lifelong Model Editing with Hierarchical Reinforcement Learning, Yangfan Wang, Tianyang Sun, Chen Tang et al., arXiv 2026 · http://arxiv.org/abs/2604.11214v1
- [P-2604.09391] Efficient Unlearning through Maximizing Relearning Convergence Delay, Khoa Tran, Simon S. Woo, arXiv 2026 · http://arxiv.org/abs/2604.09391v1
- [P-2604.08284] Distributed Multi-Layer Editing for Rule-Level Knowledge in Large Language Models, Yating Wang, Wenting Zhao, Yaqi Zhao et al., arXiv 2026 · http://arxiv.org/abs/2604.08284v1
- [P-2604.07965] DSCA: Dynamic Subspace Concept Alignment for Lifelong VLM Editing, Gyanendra Das, Sai Satyam Jena, arXiv 2026 · http://arxiv.org/abs/2604.07965v1
- [P-2604.08238] $\oslash$ Source Models Leak What They Shouldn't $\nrightarrow$: Unlearning Zero-Shot Transfer in Domain Adaptation Through Adversarial Optimization, Arnav Devalapally, Poornima Jain, Kartik Srinivas et al., arXiv 2026 · http://arxiv.org/abs/2604.08238v1
- [P-2604.05716] Can Large Language Models Reinvent Foundational Algorithms?, Jian Zhao, Haoren Luo, Yu Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.05716v1 · also_in: hf
- [P-2604.05634] PECKER: A Precisely Efficient Critical Knowledge Erasure Recipe For Machine Unlearning in Diffusion Models, Zhiyong Ma, Zhitao Deng, Huan Tang et al., arXiv 2026 · http://arxiv.org/abs/2604.05634v1
- [P-2604.05669] Efficient machine unlearning with minimax optimality, Jingyi Xie, Linjun Zhang, Sai Li, arXiv 2026 · http://arxiv.org/abs/2604.05669v1
- [P-2604.06154] Exclusive Unlearning, Mutsumi Sasaki, Kouta Nakayama, Yusuke Miyao et al., arXiv 2026 · http://arxiv.org/abs/2604.06154v1
- [P-2604.03941] SafeCtrl: Region-Aware Safety Control for Text-to-Image Diffusion via Detect-Then-Suppress, Lingyun Zhang, Yu Xie, Zhongli Fang et al., arXiv 2026 · http://arxiv.org/abs/2604.03941v1
- [P-2604.03571] Selective Forgetting for Large Reasoning Models, Tuan Le, Wei Qian, Mengdi Huai, arXiv 2026 · http://arxiv.org/abs/2604.03571v1
- [P-2604.02183] TRU: Targeted Reverse Update for Efficient Multimodal Recommendation Unlearning, Zhanting Zhou, KaHou Tam, Ziqiang Zheng et al., arXiv 2026 · http://arxiv.org/abs/2604.02183v2
- [P-2603.27338] CounterMoral: Editing Morals in Language Models, Michael Ripa, Jim Davies, arXiv 2026 · http://arxiv.org/abs/2603.27338v1
- [P-2603.26316] SALMUBench: A Benchmark for Sensitive Association-Level Multimodal Unlearning, Cai Selvas-Sala, Lei Kang, Lluis Gomez, arXiv 2026 · http://arxiv.org/abs/2603.26316v1
- [P-2603.22870] Designing to Forget: Deep Semi-parametric Models for Unlearning, Amber Yijia Zheng, Yu-Shan Tai, Raymond A. Yeh, arXiv 2026 · http://arxiv.org/abs/2603.22870v1
- [P-2603.21317] Stream separation improves Bregman conditioning in transformers, James Clayton Kerce, arXiv 2026 · http://arxiv.org/abs/2603.21317v1
- [P-2603.19101] FedTrident: Resilient Road Condition Classification Against Poisoning Attacks in Federated Learning, Sheng Liu, Panos Papadimitratos, arXiv 2026 · http://arxiv.org/abs/2603.19101v1
- [P-2603.14259] Bringing Model Editing to Generative Recommendation in Cold-Start Scenarios, Chenglei Shen, Teng Shi, Weijie Yu et al., arXiv 2026 · http://arxiv.org/abs/2603.14259v1
- [P-2603.14484] Unlearning-based sliding window for continual learning under concept drift, Michal Wozniak, Marek Klonowski, Maciej Maczynski et al., arXiv 2026 · http://arxiv.org/abs/2603.14484v1
- [P-2603.14343] Localizing and Editing Knowledge in Large Audio-Language Models, Sung Kyun Chung, Jiaheng Dong, Qiuchi Hu et al., arXiv 2026 · http://arxiv.org/abs/2603.14343v1
- [P-2603.12743] MoKus: Leveraging Cross-Modal Knowledge Transfer for Knowledge-Aware Concept Customization, Chenyang Zhu, Hongxiang Li, Xiu Li et al., arXiv 2026 · http://arxiv.org/abs/2603.12743v1 · also_in: hf
- [P-2603.12977] Exact Federated Continual Unlearning for Ridge Heads on Frozen Foundation Models, Yijun Quan, Wentai Wu, Giovanni Montana, arXiv 2026 · http://arxiv.org/abs/2603.12977v2
- [P-2603.12598] Neural Gate: Mitigating Privacy Risks in LVLMs via Neuron-Level Gradient Gating, Xiangkui Cao, Jie Zhang, Meina Kan et al., arXiv 2026 · http://arxiv.org/abs/2603.12598v1
- [P-2603.12468] Adaptation of Weakly Supervised Localization in Histopathology by Debiasing Predictions, Alexis Guichemerre, Banafsheh Karimian, Soufiane Belharbi et al., arXiv 2026 · http://arxiv.org/abs/2603.12468v1
- [P-2603.11239] Reversible Lifelong Model Editing via Semantic Routing-Based LoRA, Haihua Luo, Xuming Ran, Tommi Kärkkäinen et al., arXiv 2026 · http://arxiv.org/abs/2603.11239v2
- [P-2603.19302] Parameter-Efficient Token Embedding Editing for Clinical Class-Level Unlearning, Iyad Ait Hou, Shrenik Borad, Harsh Sharma et al., arXiv 2026 · http://arxiv.org/abs/2603.19302v1
- [P-2603.19297] CLaRE-ty Amid Chaos: Quantifying Representational Entanglement to Predict Ripple Effects in LLM Editing, Manit Baser, Alperen Yildiz, Dinil Mon Divakaran et al., arXiv 2026 · http://arxiv.org/abs/2603.19297v2
- [P-2603.07551] Targeted Speaker Poisoning Framework in Zero-Shot Text-to-Speech, Thanapat Trachu, Thanathai Lertpetchpun, Sai Praneeth Karimireddy et al., arXiv 2026 · http://arxiv.org/abs/2603.07551v1
- [P-2603.15656] Attribution-Guided Model Rectification of Unreliable Neural Network Behaviors, Peiyu Yang, Naveed Akhtar, Jiantong Jiang et al., arXiv 2026 · http://arxiv.org/abs/2603.15656v1
- [P-2603.07529] Obliviator Reveals the Cost of Nonlinear Guardedness in Concept Erasure, Ramin Akbari, Milad Afshari, Vishnu Naresh Boddeti, arXiv 2026 · http://arxiv.org/abs/2603.07529v1
- [P-2603.06962] A SISA-based Machine Unlearning Framework for Power Transformer Inter-Turn Short-Circuit Fault Localization, Nanhong Liu, Jingyi Yan, Mucun Sun et al., arXiv 2026 · http://arxiv.org/abs/2603.06962v1
- [P-2603.07166] ACD-U: Asymmetric co-teaching with machine unlearning for robust learning with noisy labels, Reo Fukunaga, Soh Yoshida, Mitsuji Muneyasu, arXiv 2026 · http://arxiv.org/abs/2603.07166v1
- [P-2603.03172] Less Noise, Same Certificate: Retain Sensitivity for Unlearning, Carolin Heinzler, Kasra Malihi, Amartya Sanyal, arXiv 2026 · http://arxiv.org/abs/2603.03172v1
- [P-2603.01756] NeuroSymb-MRG: Differentiable Abductive Reasoning with Active Uncertainty Minimization for Radiology Report Generation, Rong Fu, Yiqing Lyu, Chunlei Meng et al., arXiv 2026 · http://arxiv.org/abs/2603.01756v2
- [P-2602.21499] Easy3E: Feed-Forward 3D Asset Editing via Rectified Voxel Flow, Shimin Hu, Yuanyi Wei, Fei Zha et al., arXiv 2026 · http://arxiv.org/abs/2602.21499v2
- [P-2602.20114] Benchmarking Unlearning for Vision Transformers, Kairan Zhao, Iurie Luca, Peter Triantafillou, arXiv 2026 · http://arxiv.org/abs/2602.20114v1
- [P-2602.19967] Unlearning Noise in PINNs: A Selective Pruning Framework for PDE Inverse Problems, Yongsheng Chen, Yong Chen, Wei Guo et al., arXiv 2026 · http://arxiv.org/abs/2602.19967v3
- [P-2603.12275] GONE: Structural Knowledge Unlearning via Neighborhood-Expanded Distribution Shaping, Chahana Dahal, Ashutosh Balasubramaniam, Zuobin Xiong, arXiv 2026 · http://arxiv.org/abs/2603.12275v1
- [P-2602.18711] HIME: Mitigating Object Hallucinations in LVLMs via Hallucination Insensitivity Model Editing, Ahmed Akl, Abdelwahed Khamis, Ali Cheraghian et al., arXiv 2026 · http://arxiv.org/abs/2602.18711v1
- [P-2602.17088] MeGU: Machine-Guided Unlearning with Target Feature Disentanglement, Haoyu Wang, Zhuo Huang, Xiaolong Wang et al., arXiv 2026 · http://arxiv.org/abs/2602.17088v1

---

## 메타 / 디버그
- model: gemini-2.5-pro
- backend: gemini-pro-sdk
- matched_n: 100
- matched_total_before_cap: 171
- window_days: 100
- tokens_in_uncached: 21015
- tokens_in_cached_read: 118316
- tokens_out: 5877
- usd_estimate: $0.1217
- deep: True
- deep_k: 5
- deep_pdfs_ok: 5
- deep_pdfs_failed: 0
- pdf_archive: reports/2026-04-28-llm-unlearning-gemini-pro-deep/
- pdf_archive_linked: 5
- pdf_archive_copied: 0
- pdf_archive_missing: 0
