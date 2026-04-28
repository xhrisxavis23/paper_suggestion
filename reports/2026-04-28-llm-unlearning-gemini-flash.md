# Research Topic Suggestion — "llm unlearning"

생성: 2026-04-28T08:57:14.517493+00:00
DB 윈도우: 2026-01-18 ~ 2026-04-28 (100d)
모델: gemini-2.5-flash
매칭 논문: 100건
확장 키워드: ['llm unlearning', 'large language model unlearning', 'machine unlearning', 'neural network unlearning', 'model unlearning', 'knowledge unlearning', 'data deletion in llms', 'forgetting mechanism llm', 'model editing for unlearning', 'privacy-preserving unlearning', 'undesired knowledge removal', 'selective knowledge removal']

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — 고급 학습 제거 기법 및 아키텍처
- **설명**: LoRA, 어댑터, 프롬프트 기반, 뉴턴 방식 등 새로운 모델 아키텍처나 효율적인 매개변수 조정을 활용한 고급 학습 제거 방법론에 초점을 맞춥니다. 확산 모델 및 LLM과 같은 특정 모델 유형에 대한 혁신적인 접근법을 포함합니다.
- **빈도**: 29건
- **월별 (≈25d씩, 오래된→최근)**: 11 → 6 → 5 → 7
- **대표 논문**:
  - [P-2604.21571] Separable Expert Architecture: Toward Privacy-Preserving LLM Personalization via Composable Adapters and Deletable User Proxies — Chris Schneider, Philipp Schoenegger, Ben Bariach, arXiv 2026
  - [P-2604.17396] Representation-Guided Parameter-Efficient LLM Unlearning — Zeguan Xiao, Lang Mo, Yun Chen et al., arXiv 2026
  - [P-2604.13438] WIN-U: Woodbury-Informed Newton-Unlearning as a retain-free Machine Unlearning Framework — Xingjian Zhao, Mohammad Mohammadi Amiri, Malik Magdon-Ismail, arXiv 2026

### 클러스터 2 — 학습 제거 평가 및 강건성
- **설명**: 학습 제거의 효과와 강건성을 측정하고, 재학습 및 내부 표현 분석과 같은 취약점을 식별하며, 공격에 대한 모델의 보안을 보장하는 방법에 대한 연구를 다룹니다.
- **빈도**: 23건
- **월별 (≈25d씩, 오래된→최근)**: 8 → 7 → 4 → 4
- **대표 논문**:
  - [P-2604.22076] PrivUn: Unveiling Latent Ripple Effects and Shallow Forgetting in Privacy Unlearning — Xiaoyi Chen, Haoyuan Wang, Siyuan Tang et al., arXiv 2026
  - [P-2603.11266] The Unlearning Mirage: A Dynamic Framework for Evaluating LLM Unlearning — Raj Sanjay Shah, Jing Huang, Keerthiram Murugesan et al., arXiv 2026
  - [P-2602.18505] Suppression or Deletion: A Restoration-Based Representation-Level Analysis of Machine Unlearning — Yurim Jang, Jaeung Lee, Dohyun Kim et al., arXiv 2026

### 클러스터 3 — 기본 개념, 연속 및 법적 학습 제거
- **설명**: 연속 학습 제거의 과제, '잊혀질 권리'와 같은 법적 및 윤리적 고려 사항, 그리고 학습 제거의 통계적 또는 이론적 기초를 탐구하는 연구를 포함합니다.
- **빈도**: 27건
- **월별 (≈25d씩, 오래된→최근)**: 8 → 6 → 5 → 8
- **대표 논문**:
  - [P-2604.18649] Position: No Retroactive Cure for Infringement during Training — Satoru Utsunomiya, Masaru Isonuma, Junichiro Mori et al., arXiv 2026
  - [P-2604.07962] Is your algorithm unlearning or untraining? — Eleni Triantafillou, Ahmed Imtiaz Humayun, Monica Ribero et al., arXiv 2026
  - [P-2604.19108] Robust Continual Unlearning against Knowledge Erosion and Forgetting Reversal — Eun-Ju Park, Youjin Shin, Simon S. Woo, arXiv 2026

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap gap_1 — 대부분의 학습 제거 연구에서 유틸리티 보존과 망각 효율성 간의 근본적인 상충관계와 높은 연산 비용 문제가 지속적으로 제기됩니다. 특히 폐쇄형 대
- **타입**: recurring-limitation
- **설명**: 대부분의 학습 제거 연구에서 유틸리티 보존과 망각 효율성 간의 근본적인 상충관계와 높은 연산 비용 문제가 지속적으로 제기됩니다. 특히 폐쇄형 대규모 모델이나 복잡한 데이터 구조에서 이러한 한계가 두드러집니다.
- **근거 논문**: P-2604.21251, P-2602.23400, P-2602.01703, P-2602.02824
- **Skeptic 검토**: ✓ 통과 — 이것은 학습 제거의 근본적이고 지속적인 도전 과제로, 어떤 클러스터에서도 완전히 해결되었다고 제시되지 않습니다.

### Gap gap_5 — 대부분의 학습 제거 연구가 특정 사실, 개인 정보, 유해 콘텐츠 제거에 집중하는 반면, LLM의 '기초적인 추론 능력'이나 '알고리즘적 지식' 
- **타입**: between-clusters
- **설명**: 대부분의 학습 제거 연구가 특정 사실, 개인 정보, 유해 콘텐츠 제거에 집중하는 반면, LLM의 '기초적인 추론 능력'이나 '알고리즘적 지식' 자체를 학습 제거하고 이를 재발명하는 것과 같은 고차원적 지식 제거에 대한 탐구는 제한적입니다.
- **근거 논문**: P-2604.05716, P-2604.15847, P-2604.03571
- **Skeptic 검토**: ✓ 통과 — 이 갭은 LLM의 추론 및 알고리즘 지식이라는 새로운 유형의 정보 제거를 다루며, 이는 기존 클러스터에서 다루는 일반적인 정보 제거와는 구별되는 고차원적이고 미개척된 영역입니다.

### Gap gap_6 — 일반적인 LLM이나 확산 모델에 대한 학습 제거 연구는 활발하나, 멀티모달 추천 시스템, 임상 언어 모델, 연합 학습, 제로샷 TTS, 전력 설
- **타입**: between-clusters
- **설명**: 일반적인 LLM이나 확산 모델에 대한 학습 제거 연구는 활발하나, 멀티모달 추천 시스템, 임상 언어 모델, 연합 학습, 제로샷 TTS, 전력 설비 진단 등 특정 도메인의 고유한 특성(데이터 구조, 윤리적 민감성, 실시간 요구사항)을 고려한 맞춤형 학습 제거 방법론은 아직 부족합니다.
- **근거 논문**: P-2604.02183, P-2603.19302, P-2603.19101, P-2603.07551, P-2603.06962
- **Skeptic 검토**: ✓ 통과 — 이 갭은 특정 도메인/애플리케이션에 특화된 학습 제거의 필요성을 제기하며, 이는 기존 클러스터가 일반적인 방법론이나 평가에 집중하는 것과 달리 새로운 적용 범위를 제시합니다.

### Gap gap_7 — 데이터 보유에 대한 경제적 인센티브와 사용자 개인 정보 보호 권리 사이의 균형을 맞추기 위해, 서버가 사용자 선호도에 대한 사전 지식 없이 데이
- **타입**: single-shot
- **설명**: 데이터 보유에 대한 경제적 인센티브와 사용자 개인 정보 보호 권리 사이의 균형을 맞추기 위해, 서버가 사용자 선호도에 대한 사전 지식 없이 데이터 보유 가격을 책정하는 '정보 없는 인용 메커니즘'을 제안하는 연구는 본 클러스터에서 단발성으로 나타납니다.
- **근거 논문**: P-2604.11511
- **Skeptic 검토**: ✓ 통과 — 이 갭은 학습 제거 문제를 경제학적/게임 이론적 관점에서 접근하는 독특한 시도로, 다른 클러스터에서 체계적으로 다루어지지 않는 학제 간 연구 방향을 제시합니다.

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap gap_2** — 현재 학습 제거 방법론과 평가 지표가 모델의 출력 수준에서 '얕은 망각'만을 달성하며, 실제 민감 정보가 내부 표현 수준에 여전히 남아있을 수 있다는 문제가 반복적으로 지적됩니다. 이는 재학습 공격이나 선형 프로빙에 취약할 수 있습니다. · 거부 사유: 다른 클러스터에서 이미 다룸. 이 갭에서 제시된 '얕은 망각' 및 '내부 표현' 문제는 클러스터 2('학습 제거 평가 및 강건성')의 핵심 연구 주제이며, 관련 논문들(arxiv:2604.22076, arxiv:2604.08271, arxiv:2602.18505, arxiv:2602.05375)이 해당 클러스터에 포함되어 있습니다.
- **Gap gap_3** — 실제 세계에서 학습 제거 요청은 단발성이 아닌 연속적/반복적으로 발생하며, 기존 방법론은 이러한 연속적인 요청에 대해 '지식 침식'이나 '망각 역전'과 같은 현상으로 인해 모델의 유틸리티가 점진적으로 저하되거나 이전에 잊었던 정보가 다시 인식될 위험이 있습니다. · 거부 사유: 다른 클러스터에서 이미 다룸. 이 갭에서 설명된 '연속적 학습 제거'의 도전 과제는 클러스터 3('기본 개념, 연속 및 법적 학습 제거')의 핵심 주제이며, 관련 논문들(arxiv:2604.19108, arxiv:2604.12686, arxiv:2604.12526, arxiv:2601.21682)이 해당 클러스터에 포함되어 있습니다.
- **Gap gap_4** — 학습 제거 기술은 '잊혀질 권리'와 같은 법적/윤리적 요구사항을 충족시키기 위해 개발되지만, 법적 준수를 위한 '검증 가능한' 기술적 보장을 제공하는 데는 여전히 간극이 존재합니다. 특히 데이터 lineage와 같은 근본적인 법적 책임을 사후 완화로 해결하기 어렵다는 주장이 있습니다. · 거부 사유: 다른 클러스터에서 이미 다룸. 이 갭에서 제시된 학습 제거의 법적/윤리적 준수 및 검증 가능성 문제는 클러스터 3('기본 개념, 연속 및 법적 학습 제거')의 핵심 주제이며, 관련 논문들(arxiv:2604.18649, arxiv:2602.14553)이 해당 클러스터에 포함되어 있습니다.

</details>

## 3. 연구 제안 (Proposer)

### 제안 1 — PARA-OPT
**가설**: LLM 학습 제거 시, 전역적인 매개변수 수정 대신 중요한 매개변수를 효율적으로 식별하고 국소적으로 업데이트함으로써 유틸리티 손실을 최소화하고 계산 비용을 절감하며 망각 효율성을 유지할 수 있다.
**메우는 갭**: gap_1
**접근**: 기존 연구들이 지적하는 'polysemy dilemma' (arxiv:2602.23400)나 'gradient conflicts' (arxiv:2602.01703) 문제를 해결하기 위해, 우리는 LLM의 매개변수 공간에서 망각과 보존에 대한 각 매개변수의 비대칭적 중요도를 학습하고 이를 기반으로 업데이트의 강도를 동적으로 조절하는 프레임워크를 제안한다. 특히, 희소성(sparsity)을 고려하여 (arxiv:2602.00577) 특정 레이어 또는 어댑터 내에서만 가중치를 수정하되, 중요도 재분배 메커니즘을 도입하여 pruned된 매개변수의 영향을 보상한다. 이를 통해 필요한 정보만 선택적으로 제거하고 나머지 지식의 손상을 최소화한다.
**Baselines**: LoRA, Gradient Ascent (GA), Negative Preference Alignment, U-CAN, AGT$^{AO}$, SAU, PerTA. (Models: Llama-2-7B, Phi-3.5-mini, Llama-3.1-8B, GPT-2, DistilGPT-2)
**예상 기여**: 이 연구는 LLM 학습 제거의 고질적인 유틸리티-망각 상충관계를 완화하고, 특히 자원 제약이 있는 환경에서의 실용적인 배포 가능성을 높인다. 또한, 폐쇄형 모델에서도 적용 가능한 프레임워크를 제시하여 학습 제거 기술의 접근성을 확장한다.
**참고**: P-2604.21251, P-2602.23400, P-2602.01703, P-2602.02824, P-2602.00577, P-2601.22030

### 제안 2 — ALGO-ERASE
**가설**: LLM의 사슬형 추론(CoT) 과정에서 특정 알고리즘적 지식의 흔적을 효과적으로 제거하고, 제거된 알고리즘의 핵심 원리를 바탕으로 모델이 새로운 방식으로 해당 알고리즘을 '재발명'하도록 유도할 수 있다.
**메우는 갭**: gap_5
**접근**: 이 연구는 CoT 추론 과정에서 특정 알고리즘(예: Dijkstra's, Euclid's)의 적용 패턴을 식별하고, 해당 패턴과 관련된 내부 표현(internal representations)을 깊이 있는 레이어에서부터 제거하는 '다층적 개입' 방법론을 제안한다. 이를 위해, 먼저 '알고리즘 연관성 그래프'를 구성하여 핵심 추론 경로를 매핑하고, 이 경로에 대한 그라디언트 기반 억제와 함께 (arxiv:2604.03571), 제거된 지식의 '재발명'을 위한 구조화된 제약 조건을 부여하는 생성적 검증기(generative verifier)를 활용한다 (arxiv:2604.05716). 재발명 단계에서는 반사실적 추론 트레이스 (arxiv:2604.15847)와 같은 기법을 통해 모델이 논리적으로 타당한 대안적 해결책을 탐색하도록 유도한다.
**Baselines**: GRPO-based unlearning, CiPO, Selective Forgetting, GONE. (Models: Llama-3-8B, Mistral-7B, Qwen3-4B-Thinking-2507, Phi-3.5-mini)
**예상 기여**: LLM의 기초적인 추론 및 알고리즘 지식을 제거하고 재구축하는 새로운 방법론을 제시하여, 모델의 지식 구조에 대한 심도 깊은 이해를 제공한다. 이는 LLM의 편향 제거, 특정 기능의 재설계, 그리고 진정한 '잊혀질 권리' 구현을 위한 새로운 차원의 가능성을 열어줄 것이다.
**참고**: P-2604.05716, P-2604.15847, P-2604.03571, P-2604.04255, P-2603.12275, P-2603.09980

### 제안 3 — CROSS-DOMAIN-MU
**가설**: 다양한 특수 도메인(예: 멀티모달 추천 시스템, 임상 언어 모델)에서 데이터 구조와 윤리적 민감성을 고려한 맞춤형 학습 제거 프레임워크를 개발함으로써, 일반적인 학습 제거 방법론의 한계를 극복하고 도메인별 최적의 망각 및 유틸리티 보존을 달성할 수 있다.
**메우는 갭**: gap_6
**접근**: 우리는 도메인별 특성을 반영하는 '적응형 세분화' (adaptive granularity) 기법을 활용하여 학습 제거의 깊이와 범위를 조절한다. 예를 들어, 멀티모달 추천 시스템에서는 사용자-아이템 상호작용 그래프와 풍부한 아이템 콘텐츠 간의 결합에서 발생하는 비균일한 영향 (arxiv:2604.02183)을, 임상 언어 모델에서는 PMI(점별 상호 정보량)를 활용한 토큰 임베딩 수정 (arxiv:2603.19302)을 통해 민감한 정보의 노출 경로를 정밀하게 식별한다. 이후, 각 도메인에 특화된 '가중치 재분배' 및 '표현 공간 투영' (arxiv:2604.13127) 전략을 적용하여, 해당 도메인의 핵심 기능(예: 추천 정확도, 진단 정확도)을 유지하면서 민감 정보를 효율적으로 제거한다.
**Baselines**: TRU, STEU, FedTrident, SGSP, SISA. (Models: BioClinicalBERT, BERT-base, DistilBERT, Llama2-7B. Datasets: MIMIC-IV, MIMIC-III, eICU, CIFAR-100)
**예상 기여**: 이 연구는 기계 학습 제거의 적용 범위를 확장하여, 고도로 전문화된 AI 시스템의 규제 준수 및 윤리적 책임성을 강화한다. 각 도메인의 고유한 제약을 해결하는 맞춤형 방법론은 실제 산업 및 의료 분야에서의 AI 신뢰성을 높이는 데 기여할 것이다.
**참고**: P-2604.02183, P-2603.19302, P-2603.19101, P-2603.07551, P-2603.06962, P-2604.13127

## 4. 참고문헌 (메타DB 기반)

### 클러스터 1 — 고급 학습 제거 기법 및 아키텍처 (29)
- [P-2604.21571] Separable Expert Architecture: Toward Privacy-Preserving LLM Personalization via Composable Adapters and Deletable User Proxies, Chris Schneider, Philipp Schoenegger, Ben Bariach, arXiv 2026 · http://arxiv.org/abs/2604.21571v1
- [P-2604.21251] CAP: Controllable Alignment Prompting for Unlearning in LLMs, Zhaokun Wang, Jinyu Guo, Jingwen Pu et al., arXiv 2026 · http://arxiv.org/abs/2604.21251v1
- [P-2604.21041] Projected Gradient Unlearning for Text-to-Image Diffusion Models: Defending Against Concept Revival Attacks, Aljalila Aladawi, Mohammed Talha Alam, Fakhri Karray, arXiv 2026 · http://arxiv.org/abs/2604.21041v1
- [P-2604.17396] Representation-Guided Parameter-Efficient LLM Unlearning, Zeguan Xiao, Lang Mo, Yun Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.17396v1
- [P-2604.15847] CiPO: Counterfactual Unlearning for Large Reasoning Models through Iterative Preference Optimization, Junyi Li, Yongqiang Chen, Ningning Ding, arXiv 2026 · http://arxiv.org/abs/2604.15847v1
- [P-2604.14808] Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem, Zeguan Xiao, Siqing Li, Yong Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.14808v1
- [P-2604.13777] From Anchors to Supervision: Memory-Graph Guided Corpus-Free Unlearning for Large Language Models, Wenxuan Li, Zhenfei Zhang, Mi Zhang et al., arXiv 2026 · http://arxiv.org/abs/2604.13777v1
- [P-2604.13438] WIN-U: Woodbury-Informed Newton-Unlearning as a retain-free Machine Unlearning Framework, Xingjian Zhao, Mohammad Mohammadi Amiri, Malik Magdon-Ismail, arXiv 2026 · http://arxiv.org/abs/2604.13438v1
- [P-2604.12820] RePAIR: Interactive Machine Unlearning through Prompt-Aware Model Repair, Jagadeesh Rachapudi, Pranav Singh, Ritali Vatsi et al., arXiv 2026 · http://arxiv.org/abs/2604.12820v1
- [P-2604.10636] Mitigating Privacy Risk via Forget Set-Free Unlearning, Aviraj Newatia, Michael Cooper, Viet Nguyen et al., arXiv 2026 · http://arxiv.org/abs/2604.10636v1
- [P-2604.05634] PECKER: A Precisely Efficient Critical Knowledge Erasure Recipe For Machine Unlearning in Diffusion Models, Zhiyong Ma, Zhitao Deng, Huan Tang et al., arXiv 2026 · http://arxiv.org/abs/2604.05634v1
- [P-2604.04231] Subspace Control: Turning Constrained Model Steering into Controllable Spectral Optimization, Yancheng Huang, Changsheng Wang, Chongyu Fan et al., arXiv 2026 · http://arxiv.org/abs/2604.04231v1
- [P-2603.22870] Designing to Forget: Deep Semi-parametric Models for Unlearning, Amber Yijia Zheng, Yu-Shan Tai, Raymond A. Yeh, arXiv 2026 · http://arxiv.org/abs/2603.22870v1
- [P-2603.16489] Unlearning for One-Step Generative Models via Unbalanced Optimal Transport, Hyundo Choi, Junhyeong An, Jinseong Park et al., arXiv 2026 · http://arxiv.org/abs/2603.16489v1
- [P-2603.15033] Rethinking Machine Unlearning: Models Designed to Forget via Key Deletion, Sonia Laguna, Jorge da Silva Goncalves, Moritz Vandenhirtz et al., arXiv 2026 · http://arxiv.org/abs/2603.15033v3
- [P-2603.10445] Unlearning the Unpromptable: Prompt-free Instance Unlearning in Diffusion Models, Kyungryeol Lee, Kyeonghyun Lee, Seongmin Hong et al., arXiv 2026 · http://arxiv.org/abs/2603.10445v2
- [P-2603.00992] Compensation-free Machine Unlearning in Text-to-Image Diffusion Models by Eliminating the Mutual Information, Xinwen Cheng, Jingyuan Zhang, Zhehao Huang et al., arXiv 2026 · http://arxiv.org/abs/2603.00992v1
- [P-2602.23400] U-CAN: Utility-Aware Contrastive Attenuation for Efficient Unlearning in Generative Recommendation, Zezheng Wu, Rui Wang, Xinghe Cheng et al., arXiv 2026 · http://arxiv.org/abs/2602.23400v1
- [P-2602.13151] Quantization-Robust LLM Unlearning via Low-Rank Adaptation, João Vitor Boer Abitante, Joana Meneguzzo Pasquali, Luan Fonseca Garcia et al., arXiv 2026 · http://arxiv.org/abs/2602.13151v3
- [P-2602.10568] Gauss-Newton Unlearning for the LLM Era, Lev McKinney, Anvith Thudi, Juhan Bae et al., arXiv 2026 · http://arxiv.org/abs/2602.10568v1
- [P-2602.10217] Temper-Then-Tilt: Principled Unlearning for Generative Models through Tempering and Classifier Guidance, Jacob L. Block, Mehryar Mohri, Aryan Mokhtari et al., arXiv 2026 · http://arxiv.org/abs/2602.10217v1
- [P-2602.06441] Is Gradient Ascent Really Necessary? Memorize to Forget for Machine Unlearning, Zhuo Huang, Qizhou Wang, Ziming Hong et al., arXiv 2026 · http://arxiv.org/abs/2602.06441v1
- [P-2602.07058] SPARE: Self-distillation for PARameter-Efficient Removal, Natnael Mola, Leonardo S. B. Pereira, Carolina R. Kelsch et al., arXiv 2026 · http://arxiv.org/abs/2602.07058v2
- [P-2602.03410] UnHype: CLIP-Guided Hypernetworks for Dynamic LoRA Unlearning, Piotr Wójcik, Maksym Petrenko, Wojciech Gromski et al., arXiv 2026 · http://arxiv.org/abs/2602.03410v1
- [P-2602.01703] $\textbf{AGT$^{AO}$}$: Robust and Stabilized LLM Unlearning via Adversarial Gating Training with Adaptive Orthogonality, Pengyu Li, Lingling Zhang, Zhitao Gao et al., arXiv 2026 · http://arxiv.org/abs/2602.01703v1
- [P-2602.02824] CATNIP: LLM Unlearning via Calibrated and Tokenized Negative Preference Alignment, Zhengbang Yang, Yisheng Zhong, Junyuan Hong et al., arXiv 2026 · http://arxiv.org/abs/2602.02824v1
- [P-2601.22456] Machine Unlearning in Low-Dimensional Feature Subspace, Kun Fang, Qinghua Tao, Junxu Liu et al., arXiv 2026 · http://arxiv.org/abs/2601.22456v1
- [P-2601.22030] Per-parameter Task Arithmetic for Unlearning in Large Language Models, Chengyi Cai, Zesheng Ye, Jiangchao Yao et al., arXiv 2026 · http://arxiv.org/abs/2601.22030v1
- [P-2602.00350] ReLAPSe: Reinforcement-Learning-trained Adversarial Prompt Search for Erased concepts in unlearned diffusion models, Ignacy Kolton, Kacper Marzol, Paweł Batorski et al., arXiv 2026 · http://arxiv.org/abs/2602.00350v1

### 클러스터 2 — 학습 제거 평가 및 강건성 (23)
- [P-2604.22076] PrivUn: Unveiling Latent Ripple Effects and Shallow Forgetting in Privacy Unlearning, Xiaoyi Chen, Haoyuan Wang, Siyuan Tang et al., arXiv 2026 · http://arxiv.org/abs/2604.22076v1
- [P-2604.16536] Towards Reliable Testing of Machine Unlearning, Anna Mazhar, Sainyam Galhotra, arXiv 2026 · http://arxiv.org/abs/2604.16536v1
- [P-2603.26316] SALMUBench: A Benchmark for Sensitive Association-Level Multimodal Unlearning, Cai Selvas-Sala, Lei Kang, Lluis Gomez, arXiv 2026 · http://arxiv.org/abs/2603.26316v1
- [P-2603.16576] REFORGE: Multi-modal Attacks Reveal Vulnerable Concept Unlearning in Image Generation Models, Yong Zou, Haoran Li, Fanxiao Li et al., arXiv 2026 · http://arxiv.org/abs/2603.16576v1
- [P-2603.11266] The Unlearning Mirage: A Dynamic Framework for Evaluating LLM Unlearning, Raj Sanjay Shah, Jing Huang, Keerthiram Murugesan et al., arXiv 2026 · http://arxiv.org/abs/2603.11266v1
- [P-2604.04255] Towards Unveiling Vulnerabilities of Large Reasoning Models in Machine Unlearning, Aobo Chen, Chenxu Zhao, Chenglin Miao et al., arXiv 2026 · http://arxiv.org/abs/2604.04255v1
- [P-2603.00823] A Comprehensive Evaluation of LLM Unlearning Robustness under Multi-Turn Interaction, Ruihao Pan, Suhang Wang, arXiv 2026 · http://arxiv.org/abs/2603.00823v2
- [P-2603.00436] ROKA: Robust Knowledge Unlearning against Adversaries, Jinmyeong Shin, Joshua Tapia, Nicholas Ferreira et al., arXiv 2026 · http://arxiv.org/abs/2603.00436v1
- [P-2603.00587] Unlearning Evaluation through Subset Statistical Independence, Chenhao Zhang, Muxing Li, Feng Liu et al., arXiv 2026 · http://arxiv.org/abs/2603.00587v1
- [P-2602.23798] MPU: Towards Secure and Privacy-Preserving Knowledge Unlearning for Large Language Models, Tiantong Wang, Xinyu Yan, Tiantong Wu et al., arXiv 2026 · http://arxiv.org/abs/2602.23798v1
- [P-2602.21773] Easy to Learn, Yet Hard to Forget: Towards Robust Unlearning Under Bias, JuneHyoung Kwon, MiHyeon Kim, Eunju Lee et al., arXiv 2026 · http://arxiv.org/abs/2602.21773v1 · also_in: hf
- [P-2602.20114] Benchmarking Unlearning for Vision Transformers, Kairan Zhao, Iurie Luca, Peter Triantafillou, arXiv 2026 · http://arxiv.org/abs/2602.20114v1
- [P-2602.19612] Anatomy of Unlearning: The Dual Impact of Fact Salience and Model Fine-Tuning, Borisiuk Anna, Andrey Savchenko, Alexander Panchenko et al., arXiv 2026 · http://arxiv.org/abs/2602.19612v2
- [P-2602.18505] Suppression or Deletion: A Restoration-Based Representation-Level Analysis of Machine Unlearning, Yurim Jang, Jaeung Lee, Dohyun Kim et al., arXiv 2026 · http://arxiv.org/abs/2602.18505v1
- [P-2602.16400] Easy Data Unlearning Bench, Roy Rinberg, Pol Puigdemont, Martin Pawelczyk et al., arXiv 2026 · http://arxiv.org/abs/2602.16400v1
- [P-2602.06248] REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop, Patryk Rybak, Paweł Batorski, Paul Swoboda et al., arXiv 2026 · http://arxiv.org/abs/2602.06248v1
- [P-2602.05375] Erase at the Core: Representation Unlearning for Machine Unlearning, Jaewon Lee, Yongwoo Kim, Donghyun Kim, arXiv 2026 · http://arxiv.org/abs/2602.05375v2
- [P-2602.03567] EVE: Efficient Verification of Data Erasure through Customized Perturbation in Approximate Unlearning, Weiqi Wang, Zhiyi Tian, Chenhan Zhang et al., arXiv 2026 · http://arxiv.org/abs/2602.03567v1
- [P-2602.03379] Rethinking Benign Relearning: Syntax as the Hidden Driver of Unlearning Failures, Sangyeon Yoon, Hyesoo Hong, Wonje Jeung et al., arXiv 2026 · http://arxiv.org/abs/2602.03379v1
- [P-2602.03787] Inference-time Unlearning Using Conformal Prediction, Somnath Basu Roy Chowdhury, Rahul Kidambi, Avinava Dubey et al., arXiv 2026 · http://arxiv.org/abs/2602.03787v1
- [P-2601.22359] The Unseen Threat: Residual Knowledge in Machine Unlearning under Perturbed Samples, Hsiang Hsu, Pradeep Niroula, Zichang He et al., arXiv 2026 · http://arxiv.org/abs/2601.22359v1
- [P-2602.01150] Statistical MIA: Rethinking Membership Inference Attack for Reliable Unlearning Auditing, Jialong Sun, Zeming Wei, Jiaxuan Zou et al., arXiv 2026 · http://arxiv.org/abs/2602.01150v1
- [P-2603.09980] Explainable LLM Unlearning Through Reasoning, Junfeng Liao, Qizhou Wang, Shanshan Ye et al., arXiv 2026 · http://arxiv.org/abs/2603.09980v1

### 클러스터 3 — 기본 개념, 연속 및 법적 학습 제거 (27)
- [P-2604.19108] Robust Continual Unlearning against Knowledge Erosion and Forgetting Reversal, Eun-Ju Park, Youjin Shin, Simon S. Woo, arXiv 2026 · http://arxiv.org/abs/2604.19108v1
- [P-2604.18649] Position: No Retroactive Cure for Infringement during Training, Satoru Utsunomiya, Masaru Isonuma, Junichiro Mori et al., arXiv 2026 · http://arxiv.org/abs/2604.18649v1
- [P-2604.15482] Harmonizing Multi-Objective LLM Unlearning via Unified Domain Representation and Bidirectional Logit Distillation, Yisheng Zhong, Sijia Liu, Zhuangdi Zhu, arXiv 2026 · http://arxiv.org/abs/2604.15482v1
- [P-2604.12686] BID-LoRA: A Parameter-Efficient Framework for Continual Learning and Unlearning, Jagadeesh Rachapudi, Ritali Vatsi, Praful Hambarde et al., arXiv 2026 · http://arxiv.org/abs/2604.12686v1
- [P-2604.12526] Orthogonal Subspace Projection for Continual Machine Unlearning via SVD-Based LoRA, Yogachandran Rahulamathavan, Nasir Iqbal, Juncheng Hu et al., arXiv 2026 · http://arxiv.org/abs/2604.12526v1
- [P-2604.12459] Operationalising the Right to be Forgotten in LLMs: A Lightweight Sequential Unlearning Framework for Privacy-Aligned Deployment in Politically Sensitive Environments, Esen Kurt, Haithem Afli, arXiv 2026 · http://arxiv.org/abs/2604.12459v1
- [P-2604.11511] The Price of Ignorance: Information-Free Quotation for Data Retention in Machine Unlearning, Bin Han, Di Feng, Zexin Fang et al., arXiv 2026 · http://arxiv.org/abs/2604.11511v1
- [P-2604.08111] Bias Redistribution in Visual Machine Unlearning: Does Forgetting One Group Harm Another?, Yunusa Haruna, Adamu Lawan, Ibrahim Haruna Abdulhamid et al., arXiv 2026 · http://arxiv.org/abs/2604.08111v1
- [P-2604.07962] Is your algorithm unlearning or untraining?, Eleni Triantafillou, Ahmed Imtiaz Humayun, Monica Ribero et al., arXiv 2026 · http://arxiv.org/abs/2604.07962v1
- [P-2604.08238] $\oslash$ Source Models Leak What They Shouldn't $\nrightarrow$: Unlearning Zero-Shot Transfer in Domain Adaptation Through Adversarial Optimization, Arnav Devalapally, Poornima Jain, Kartik Srinivas et al., arXiv 2026 · http://arxiv.org/abs/2604.08238v1
- [P-2604.05716] Can Large Language Models Reinvent Foundational Algorithms?, Jian Zhao, Haoren Luo, Yu Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.05716v1 · also_in: hf
- [P-2604.06154] Exclusive Unlearning, Mutsumi Sasaki, Kouta Nakayama, Yusuke Miyao et al., arXiv 2026 · http://arxiv.org/abs/2604.06154v1
- [P-2604.03571] Selective Forgetting for Large Reasoning Models, Tuan Le, Wei Qian, Mengdi Huai, arXiv 2026 · http://arxiv.org/abs/2604.03571v1
- [P-2603.26569] Machine Unlearning under Retain-Forget Entanglement, Jingpu Cheng, Ping Liu, Qianxiao Li et al., arXiv 2026 · http://arxiv.org/abs/2603.26569v1
- [P-2603.14484] Unlearning-based sliding window for continual learning under concept drift, Michal Wozniak, Marek Klonowski, Maciej Maczynski et al., arXiv 2026 · http://arxiv.org/abs/2603.14484v1
- [P-2603.12915] Stake the Points: Structure-Faithful Instance Unlearning, Kiseong Hong, JungKyoo Shin, Eunwoo Kim, arXiv 2026 · http://arxiv.org/abs/2603.12915v1
- [P-2603.12468] Adaptation of Weakly Supervised Localization in Histopathology by Debiasing Predictions, Alexis Guichemerre, Banafsheh Karimian, Soufiane Belharbi et al., arXiv 2026 · http://arxiv.org/abs/2603.12468v1
- [P-2603.11210] Reference-Guided Machine Unlearning, Jonas Mirlach, Sonia Laguna, Julia E. Vogt, arXiv 2026 · http://arxiv.org/abs/2603.11210v1
- [P-2603.03172] Less Noise, Same Certificate: Retain Sensitivity for Unlearning, Carolin Heinzler, Kasra Malihi, Amartya Sanyal, arXiv 2026 · http://arxiv.org/abs/2603.03172v1
- [P-2602.17692] Agentic Unlearning: When LLM Agent Meets Machine Unlearning, Bin Wang, Fan Wang, Pingping Wang et al., arXiv 2026 · http://arxiv.org/abs/2602.17692v2
- [P-2602.16697] Protecting the Undeleted in Machine Unlearning, Aloni Cohen, Refael Kohen, Kobbi Nissim et al., arXiv 2026 · http://arxiv.org/abs/2602.16697v1
- [P-2602.14553] Governing AI Forgetting: Auditing for Machine Unlearning Compliance, Qinqi Lin, Ningning Ding, Lingjie Duan et al., arXiv 2026 · http://arxiv.org/abs/2602.14553v1
- [P-2602.15602] Certified Per-Instance Unlearning Using Individual Sensitivity Bounds, Hanna Benarroch, Jamal Atif, Olivier Cappé, arXiv 2026 · http://arxiv.org/abs/2602.15602v1
- [P-2602.14938] Variance-Reduced $(\varepsilon,δ)-$Unlearning using Forget Set Gradients, Martin Van Waerebeke, Marco Lorenzi, Kevin Scaman et al., arXiv 2026 · http://arxiv.org/abs/2602.14938v1
- [P-2602.06331] Don't Break the Boundary: Continual Unlearning for OOD Detection Based on Free Energy Repulsion, Ningkang Peng, Kun Shao, Jingyang Mao et al., arXiv 2026 · http://arxiv.org/abs/2602.06331v1
- [P-2602.02986] Why Some Models Resist Unlearning: A Linear Stability Perspective, Wei-Kai Chang, Rajiv Khanna, arXiv 2026 · http://arxiv.org/abs/2602.02986v1
- [P-2603.12275] GONE: Structural Knowledge Unlearning via Neighborhood-Expanded Distribution Shaping, Chahana Dahal, Ashutosh Balasubramaniam, Zuobin Xiong, arXiv 2026 · http://arxiv.org/abs/2603.12275v1

### 기타 (클러스터 미분류) (21)
- [P-2604.16591] Randomized Antipodal Search Done Right for Data Pareto Improvement of LLM Unlearning, Ziwen Liu, Huawei Lin, Yide Ran et al., arXiv 2026 · http://arxiv.org/abs/2604.16591v1
- [P-2604.15166] Class Unlearning via Depth-Aware Removal of Forget-Specific Directions, Arman Hatami, Romina Aalishah, Ilya E. Monosov, arXiv 2026 · http://arxiv.org/abs/2604.15166v1
- [P-2604.13127] Graph Propagated Projection Unlearning: A Unified Framework for Vision and Audio Discriminative Models, Shreyansh Pathak, Jyotishman Das, arXiv 2026 · http://arxiv.org/abs/2604.13127v1
- [P-2604.09391] Efficient Unlearning through Maximizing Relearning Convergence Delay, Khoa Tran, Simon S. Woo, arXiv 2026 · http://arxiv.org/abs/2604.09391v1
- [P-2604.08271] An Illusion of Unlearning? Assessing Machine Unlearning Through Internal Representations, Yichen Gao, Altay Unal, Akshay Rangamani et al., arXiv 2026 · http://arxiv.org/abs/2604.08271v1
- [P-2604.05669] Efficient machine unlearning with minimax optimality, Jingyi Xie, Linjun Zhang, Sai Li, arXiv 2026 · http://arxiv.org/abs/2604.05669v1
- [P-2604.02183] TRU: Targeted Reverse Update for Efficient Multimodal Recommendation Unlearning, Zhanting Zhou, KaHou Tam, Ziqiang Zheng et al., arXiv 2026 · http://arxiv.org/abs/2604.02183v2
- [P-2603.19101] FedTrident: Resilient Road Condition Classification Against Poisoning Attacks in Federated Learning, Sheng Liu, Panos Papadimitratos, arXiv 2026 · http://arxiv.org/abs/2603.19101v1
- [P-2603.19302] Parameter-Efficient Token Embedding Editing for Clinical Class-Level Unlearning, Iyad Ait Hou, Shrenik Borad, Harsh Sharma et al., arXiv 2026 · http://arxiv.org/abs/2603.19302v1
- [P-2603.07551] Targeted Speaker Poisoning Framework in Zero-Shot Text-to-Speech, Thanapat Trachu, Thanathai Lertpetchpun, Sai Praneeth Karimireddy et al., arXiv 2026 · http://arxiv.org/abs/2603.07551v1
- [P-2603.06962] A SISA-based Machine Unlearning Framework for Power Transformer Inter-Turn Short-Circuit Fault Localization, Nanhong Liu, Jingyi Yan, Mucun Sun et al., arXiv 2026 · http://arxiv.org/abs/2603.06962v1
- [P-2603.07166] ACD-U: Asymmetric co-teaching with machine unlearning for robust learning with noisy labels, Reo Fukunaga, Soh Yoshida, Mitsuji Muneyasu, arXiv 2026 · http://arxiv.org/abs/2603.07166v1
- [P-2602.19967] Unlearning Noise in PINNs: A Selective Pruning Framework for PDE Inverse Problems, Yongsheng Chen, Yong Chen, Wei Guo et al., arXiv 2026 · http://arxiv.org/abs/2602.19967v3
- [P-2602.17088] MeGU: Machine-Guided Unlearning with Target Feature Disentanglement, Haoyu Wang, Zhuo Huang, Xiaolong Wang et al., arXiv 2026 · http://arxiv.org/abs/2602.17088v1
- [P-2602.09304] Statistical Roughness-Informed Machine Unlearning, Mohammad Partohaghighi, Roummel Marcia, Bruce J. West et al., arXiv 2026 · http://arxiv.org/abs/2602.09304v1
- [P-2602.02139] EvoMU: Evolutionary Machine Unlearning, Pawel Batorski, Paul Swoboda, arXiv 2026 · http://arxiv.org/abs/2602.02139v2
- [P-2602.00577] SAU: Sparsity-Aware Unlearning for LLMs via Gradient Masking and Importance Redistribution, Yuze Wang, Yujia Tong, Xuan Liu et al., arXiv 2026 · http://arxiv.org/abs/2602.00577v3
- [P-2602.00567] Forget by Uncertainty: Orthogonal Entropy Unlearning for Quantized Neural Networks, Tian Zhang, Yujia Tong, Junhao Dong et al., arXiv 2026 · http://arxiv.org/abs/2602.00567v1
- [P-2601.22651] GUDA: Counterfactual Group-wise Training Data Attribution for Diffusion Models via Unlearning, Naoki Murata, Yuhta Takida, Chieh-Hsin Lai et al., arXiv 2026 · http://arxiv.org/abs/2601.22651v1
- [P-2601.21682] FIT: Defying Catastrophic Forgetting in Continual LLM Unlearning, Xiaoyu Xu, Minxin Du, Kun Fang et al., arXiv 2026 · http://arxiv.org/abs/2601.21682v1
- [P-2601.21283] DUET: Distilled LLM Unlearning from an Efficiently Contextualized Teacher, Yisheng Zhong, Zhengbang Yang, Zhuangdi Zhu, arXiv 2026 · http://arxiv.org/abs/2601.21283v2

---

## 메타 / 디버그
- model: gemini-2.5-flash
- backend: gemini-flash-sdk
- matched_n: 100
- matched_total_before_cap: 116
- window_days: 100
- tokens_in_uncached: 9220
- tokens_in_cached_read: 118720
- tokens_out: 6800
- usd_estimate: $0.0287
