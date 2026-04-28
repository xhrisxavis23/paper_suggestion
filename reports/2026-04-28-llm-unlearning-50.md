# Research Topic Suggestion — "llm unlearning"

생성: 2026-04-28T06:33:58.257951+00:00
DB 윈도우: 2026-02-27 ~ 2026-04-28 (60d)
모델: claude-sonnet-4-6
매칭 논문: 50건
확장 키워드: ['llm unlearning', 'machine unlearning', 'language model unlearning', 'knowledge unlearning', 'model unlearning', 'concept erasure', 'selective forgetting', 'targeted forgetting', 'knowledge removal', 'right to be forgotten', 'data forgetting', 'model forgetting']

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — LLM 지식·프라이버시 망각
- **설명**: LLM에서 특정 지식·민감정보를 선택적으로 제거하는 핵심 unlearning 기법군. 파라미터 효율(LoRA), retain-set 의존 제거, 다목적(망각/유지/강건성) 동시 최적화, LRM의 chain-of-thought 망각 등이 주된 흐름이다.
- **빈도**: 19건
- **월별 (≈15d씩, 오래된→최근)**: 0 → 6 → 7 → 6
- **대표 논문**:
  - [P-2604.14808] Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem — Zeguan Xiao, Siqing Li, Yong Wang et al., arXiv 2026
  - [P-2604.17396] Representation-Guided Parameter-Efficient LLM Unlearning — Zeguan Xiao, Lang Mo, Yun Chen et al., arXiv 2026
  - [P-2604.13438] WIN-U: Woodbury-Informed Newton-Unlearning as a retain-free Machine Unlearning Framework — Xingjian Zhao, Mohammad Mohammadi Amiri, Malik Magdon-Ismail, arXiv 2026

### 클러스터 2 — T2I·멀티모달 개념 삭제
- **설명**: Text-to-Image 디퓨전, VLM, VLA, 멀티모달 추천 등 비-텍스트 모달리티에서 특정 개념·표현·소속관계를 제거하는 연구군. 직교 부공간 투영, 폐쇄형 해, training-free 추론시 제어, 인접 개념 보존 등이 주요 축이다.
- **빈도**: 16건
- **월별 (≈15d씩, 오래된→최근)**: 3 → 6 → 5 → 2
- **대표 논문**:
  - [P-2604.16481] Erasing Thousands of Concepts: Towards Scalable and Practical Concept Erasure for Text-to-Image Diffusion Models — Hoigi Seo, Byung Hyun Lee, Jaehyun Cho et al., arXiv 2026
  - [P-2604.10032] Closed-Form Concept Erasure via Double Projections — Chi Zhang, Jingpu Cheng, Zhixian Wang et al., arXiv 2026
  - [P-2604.03114] Can VLMs Truly Forget? Benchmarking Training-Free Visual Concept Unlearning — Zhangyun Tan, Zeliang Zhang, Susan Liang et al., arXiv 2026

### 클러스터 3 — 신뢰성·연속화·규제
- **설명**: Unlearning의 진짜 작동 여부를 평가·감사하고, 반복적 삭제 요청·연합학습·규제 준수 시나리오로 확장하는 메타-층위 연구. 표면적 망각(illusion) 진단, relearning delay 메트릭, 연속 unlearning 간섭, GDPR/저작권 입장 등을 다룬다.
- **빈도**: 15건
- **월별 (≈15d씩, 오래된→최근)**: 2 → 2 → 8 → 3
- **대표 논문**:
  - [P-2604.16536] Towards Reliable Testing of Machine Unlearning — Anna Mazhar, Sainyam Galhotra, arXiv 2026
  - [P-2604.07962] Is your algorithm unlearning or untraining? — Eleni Triantafillou, Ahmed Imtiaz Humayun, Monica Ribero et al., arXiv 2026
  - [P-2604.08271] An Illusion of Unlearning? Assessing Machine Unlearning Through Internal Representations — Yichen Gao, Altay Unal, Akshay Rangamani et al., arXiv 2026

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap A — C1(LLM 핵심 언러닝)의 대부분 방법은 단발성(single-shot) 삭제를 가정하지만, C3(신뢰성·연속화)는 retain-forget 얽
- **타입**: between-clusters
- **설명**: C1(LLM 핵심 언러닝)의 대부분 방법은 단발성(single-shot) 삭제를 가정하지만, C3(신뢰성·연속화)는 retain-forget 얽힘과 반복 unlearning에서의 누적 erosion·forgetting reversal을 별도로 다룬다. LLM에 특화된 연속·반복 unlearning에서 'retain-forget 얽힘 + 반복 erosion + reversal 강건성'을 동시에 만족하는 방법이 비어 있다.
- **근거 논문**: P-2604.12459, P-2604.12686, P-2604.12526, P-2604.19108, P-2603.26569
- **Skeptic 검토**: ✓ 통과 — BID-LoRA(2604.12686), Orthogonal SVD-LoRA(2604.12526), 2604.19108은 각각 한 축씩만 다룸. 셋을 LLM 차원에서 통합한 사례는 메타DB에 없음.

### Gap B — 여러 논문이 "표면적 망각" / "fine-tuning 한 번이면 부활" / "내부 표현에 잔재" 라는 동일 한계를 반복 명시한다. PrivUn
- **타입**: recurring-limitation
- **설명**: 여러 논문이 "표면적 망각" / "fine-tuning 한 번이면 부활" / "내부 표현에 잔재" 라는 동일 한계를 반복 명시한다. PrivUn은 3-tier 공격으로, Illusion of Unlearning은 internal representation 분석으로, Untraining 논문은 정의 모호성으로 같은 결론에 도달한다. 진단은 풍부하나, 적대적 fine-tuning 하에서도 깊은 망각을 *guarantee*하는 방법은 부재.
- **근거 논문**: P-2604.22076, P-2604.08271, P-2604.07962, P-2604.21041, P-2604.09391, P-2604.15166
- **Skeptic 검토**: ✓ 통과 — 방어 시도(2604.21041 PGU)가 존재하나 T2I 한정. LLM에서 PrivUn-급 3-tier 공격을 동시 통과하는 방법은 메타DB에서 미발견. 통과.

### Gap D — Unlearning이 의미적으로 인접한 그룹의 정확도·표현을 비대칭적으로 흔드는 'bias redistribution' 현상은 비주얼 unlea
- **타입**: between-clusters
- **설명**: Unlearning이 의미적으로 인접한 그룹의 정확도·표현을 비대칭적으로 흔드는 'bias redistribution' 현상은 비주얼 unlearning(2604.08111)과 인접 개념 약화(2603.25994, 2604.15482의 over-refusal)에서 각각 부분적으로 관찰됐지만, LLM 엔티티/지식 unlearning에서 인접 인구통계·하위그룹·관련 개념의 측정·완화는 비어 있다.
- **근거 논문**: P-2604.08111, P-2603.25994, P-2604.15482, P-2603.26316
- **Skeptic 검토**: ✓ 통과 — 비주얼 1편(2604.08111) + 인접 보존 시도(2603.25994, 2604.15482)는 효용/안전 축, fairness 축은 LLM에서 미관측. SALMUBench(2603.26316)가 association-level 평가지반 제공. 통과.

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap C** — C1 LLM unlearning 방법 논문이 C3가 제안한 testing 프레임워크(2604.16536)를 채택하지 않는다. · 거부 사유: (c) trivial — 신규 방법론에 새 평가 프레임워크 적용은 자체 연구 갭이 아니라 적용 권고 수준.
- **Gap E** — LRM(Large Reasoning Model)의 CoT-trace 단위 unlearning과 적대적 reasoning 공격이 결합되지 않았다. · 거부 사유: (a) 이미 다룸 — CiPO(2604.15847), Vulnerabilities of LRM(2604.04255), Selective Forgetting LRM(2604.03571) 세 편이 LRM 망각·취약성을 직접 다루고 있어 single-shot이 아님.

</details>

## 3. 연구 제안 (Proposer)

### 제안 1 — CONTANGLE
**가설**: LoRA 기반 LLM에 'retain-forget 얽힘 페널티 + 직교 부공간 투영'을 결합한 연속 unlearning 스케줄을 적용하면, 10회 이상의 순차 삭제 요청에서도 단일 단계 망각 효율을 유지하면서 retain 성능 누적 erosion과 forgetting reversal을 동시에 줄일 수 있다.
**메우는 갭**: A
**접근**: (1) BID-LoRA의 continual 어댑터 분리와 Orthogonal SVD-LoRA의 SVD 기반 부공간 분리를 LLM 베이스라인으로 사용한다. (2) Retain-Forget Entanglement(2603.26569)의 augmented Lagrangian + gradient projection을 시퀀셜 스텝마다 삽입해 'forget 인접 retain'을 보호한다. (3) Robust Continual Unlearning(2604.19108)이 정의한 knowledge erosion / forgetting reversal 두 지표를 LLM 도메인으로 이식해 매 스텝 평가한다. (4) 평가는 Sequential framework(2604.12459)의 정치적 민감 데이터 시나리오와 PrivUn(2604.22076) 3-tier 공격을 결합해 누적 강건성을 측정.
**Baselines**: BID-LoRA(2604.12686), Orthogonal SVD-LoRA(2604.12526), Sequential framework(2604.12459), Retain-Forget Entanglement(2603.26569), Robust Continual Unlearning(2604.19108).
**예상 기여**: LLM 연속 unlearning에서 'retain 성능–forget 견고성–누적 erosion' 3축을 동시에 다룬 첫 통합 프레임워크 제시. retain-forget 얽힘 페널티의 LLM-스케일 효과를 수치화하고, 반복 삭제 환경에서의 견고성 새 벤치마크를 제공.
**참고**: P-2604.12686, P-2604.12526, P-2604.12459, P-2603.26569, P-2604.19108, P-2604.22076

### 제안 2 — DEEPSCAR
**가설**: 표현공간에서 forget 방향의 깊이 인지 제거(depth-aware direction removal)와 retain 활성공간 직교 보충부 투영을 결합하고, relearning convergence delay를 학습 신호로 직접 최적화하면, fine-tuning 기반 relearning 공격 하에서도 PrivUn 3-tier 공격을 모두 통과하는 깊은 망각을 달성한다.
**메우는 갭**: B
**접근**: (1) Class Unlearning Depth-Aware(2604.15166)의 forget-specific direction 제거를 LLM 토큰 임베딩·레이어별 활성공간으로 확장. (2) Projected Gradient Unlearning(2604.21041)의 Core Gradient Space orthogonal 투영을 LLM gradient step에 이식해 downstream fine-tuning에서도 forget 방향이 복귀하지 못하도록 한다. (3) Relearning Convergence Delay(2604.09391)를 미분 가능 surrogate로 설계해 학습 손실에 직접 포함시킨다. (4) 평가는 PrivUn 3-tier 공격(2604.22076), Illusion-of-Unlearning 내부표현 분석(2604.08271), Untraining 정의 검증(2604.07962)을 모두 통과해야 한다.
**Baselines**: Representation-Guided PE Unlearning(2604.17396), Asymmetric Two-Task SAGO(2604.14808), CAP(2604.21251), Harmonizing Multi-Objective(2604.15482); 평가지표는 PrivUn(2604.22076), Illusion(2604.08271), Untraining(2604.07962), Relearning Convergence Delay(2604.09391).
**예상 기여**: LLM 도메인에서 'fine-tune-revival에 강건한' 첫 방법-수준 솔루션을 제시. depth-aware 방향제거+직교투영+relearning 지연을 한 손실로 통합한 'deep forgetting guarantee' 학습 절차를 정의하고, 진단 메트릭이 학습 신호로 직접 사용 가능함을 입증.
**참고**: P-2604.15166, P-2604.21041, P-2604.09391, P-2604.22076, P-2604.08271, P-2604.07962, P-2604.17396, P-2604.14808

### 제안 3 — EQUIFORGET
**가설**: LLM에서 특정 엔티티/개념을 unlearning할 때, 의미적으로 인접한 인구통계·관계·연관 엔티티의 association-level 정확도가 비대칭적으로 변화하며, fairness-aware regularizer로 이 redistribution을 명시적으로 제약하면 효용·견고성을 유지하면서 인접 그룹 격차를 통계적으로 유의하게 줄일 수 있다.
**메우는 갭**: D
**접근**: (1) Bias Redistribution(2604.08111) 측정 프로토콜을 SALMUBench(2603.26316)의 60K persona-attribute association 위에 LLM 형태로 이식해 'association-level 비대칭 변화'를 정량화한다. (2) 인접 보존 동기를 가진 두 방법론(Neighbor-Aware Localized(2603.25994)의 인접 직교화, Harmonizing Multi-Objective(2604.15482)의 over-refusal 억제)을 LLM unlearning 스텝에 결합해 baseline 대비 redistribution을 측정한다. (3) 인접 그룹 disparity를 직접 페널티로 두는 fairness-aware loss를 추가하고 trade-off 곡선을 그린다. (4) 동일 셋업에서 CAP(2604.21251)과 Asymmetric Two-Task(2604.14808)에도 적용해 일반성 입증.
**Baselines**: CAP(2604.21251), Harmonizing Multi-Objective(2604.15482), Asymmetric Two-Task(2604.14808); 평가는 SALMUBench(2603.26316), Bias Redistribution 프로토콜(2604.08111), Neighbor-Aware Localized(2603.25994)의 인접 보존 지표.
**예상 기여**: LLM unlearning의 fairness 영향을 association 수준으로 측정 가능한 첫 평가-방법 통합 프레임워크. 'forget 1개 → 인접 N개 약화' 현상을 LLM 도메인에서 처음 정량화하고, fairness-aware unlearning regularizer가 효용 손실을 작게 유지하면서 그룹 disparity를 줄이는 정도를 수치화한다.
**참고**: P-2604.08111, P-2603.26316, P-2603.25994, P-2604.15482, P-2604.21251, P-2604.14808

## 4. 참고문헌 (메타DB 기반)

### 클러스터 1 — LLM 지식·프라이버시 망각 (19)
- [P-2604.21571] Separable Expert Architecture: Toward Privacy-Preserving LLM Personalization via Composable Adapters and Deletable User Proxies, Chris Schneider, Philipp Schoenegger, Ben Bariach, arXiv 2026 · http://arxiv.org/abs/2604.21571v1
- [P-2604.21251] CAP: Controllable Alignment Prompting for Unlearning in LLMs, Zhaokun Wang, Jinyu Guo, Jingwen Pu et al., arXiv 2026 · http://arxiv.org/abs/2604.21251v1
- [P-2604.22076] PrivUn: Unveiling Latent Ripple Effects and Shallow Forgetting in Privacy Unlearning, Xiaoyi Chen, Haoyuan Wang, Siyuan Tang et al., arXiv 2026 · http://arxiv.org/abs/2604.22076v1
- [P-2604.17396] Representation-Guided Parameter-Efficient LLM Unlearning, Zeguan Xiao, Lang Mo, Yun Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.17396v1
- [P-2604.16591] Randomized Antipodal Search Done Right for Data Pareto Improvement of LLM Unlearning, Ziwen Liu, Huawei Lin, Yide Ran et al., arXiv 2026 · http://arxiv.org/abs/2604.16591v1
- [P-2604.15482] Harmonizing Multi-Objective LLM Unlearning via Unified Domain Representation and Bidirectional Logit Distillation, Yisheng Zhong, Sijia Liu, Zhuangdi Zhu, arXiv 2026 · http://arxiv.org/abs/2604.15482v1
- [P-2604.15847] CiPO: Counterfactual Unlearning for Large Reasoning Models through Iterative Preference Optimization, Junyi Li, Yongqiang Chen, Ningning Ding, arXiv 2026 · http://arxiv.org/abs/2604.15847v1
- [P-2604.14808] Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem, Zeguan Xiao, Siqing Li, Yong Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.14808v1
- [P-2604.13777] From Anchors to Supervision: Memory-Graph Guided Corpus-Free Unlearning for Large Language Models, Wenxuan Li, Zhenfei Zhang, Mi Zhang et al., arXiv 2026 · http://arxiv.org/abs/2604.13777v1
- [P-2604.13438] WIN-U: Woodbury-Informed Newton-Unlearning as a retain-free Machine Unlearning Framework, Xingjian Zhao, Mohammad Mohammadi Amiri, Malik Magdon-Ismail, arXiv 2026 · http://arxiv.org/abs/2604.13438v1
- [P-2604.12820] RePAIR: Interactive Machine Unlearning through Prompt-Aware Model Repair, Jagadeesh Rachapudi, Pranav Singh, Ritali Vatsi et al., arXiv 2026 · http://arxiv.org/abs/2604.12820v1
- [P-2604.12459] Operationalising the Right to be Forgotten in LLMs: A Lightweight Sequential Unlearning Framework for Privacy-Aligned Deployment in Politically Sensitive Environments, Esen Kurt, Haithem Afli, arXiv 2026 · http://arxiv.org/abs/2604.12459v1
- [P-2604.10636] Mitigating Privacy Risk via Forget Set-Free Unlearning, Aviraj Newatia, Michael Cooper, Viet Nguyen et al., arXiv 2026 · http://arxiv.org/abs/2604.10636v1
- [P-2604.06154] Exclusive Unlearning, Mutsumi Sasaki, Kouta Nakayama, Yusuke Miyao et al., arXiv 2026 · http://arxiv.org/abs/2604.06154v1
- [P-2604.05716] Can Large Language Models Reinvent Foundational Algorithms?, Jian Zhao, Haoren Luo, Yu Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.05716v1 · also_in: hf
- [P-2604.05669] Efficient machine unlearning with minimax optimality, Jingyi Xie, Linjun Zhang, Sai Li, arXiv 2026 · http://arxiv.org/abs/2604.05669v1
- [P-2604.04255] Towards Unveiling Vulnerabilities of Large Reasoning Models in Machine Unlearning, Aobo Chen, Chenxu Zhao, Chenglin Miao et al., arXiv 2026 · http://arxiv.org/abs/2604.04255v1
- [P-2604.04231] Subspace Control: Turning Constrained Model Steering into Controllable Spectral Optimization, Yancheng Huang, Changsheng Wang, Chongyu Fan et al., arXiv 2026 · http://arxiv.org/abs/2604.04231v1
- [P-2604.03571] Selective Forgetting for Large Reasoning Models, Tuan Le, Wei Qian, Mengdi Huai, arXiv 2026 · http://arxiv.org/abs/2604.03571v1

### 클러스터 2 — T2I·멀티모달 개념 삭제 (16)
- [P-2604.21041] Projected Gradient Unlearning for Text-to-Image Diffusion Models: Defending Against Concept Revival Attacks, Aljalila Aladawi, Mohammed Talha Alam, Fakhri Karray, arXiv 2026 · http://arxiv.org/abs/2604.21041v1
- [P-2604.15829] Beyond Text Prompts: Precise Concept Erasure through Text-Image Collaboration, Jun Li, Lizhi Xiong, Ziqiang Li et al., arXiv 2026 · http://arxiv.org/abs/2604.15829v1
- [P-2604.16483] Dynamic Eraser for Guided Concept Erasure in Diffusion Models, Qinghui Gong, arXiv 2026 · http://arxiv.org/abs/2604.16483v1
- [P-2604.16481] Erasing Thousands of Concepts: Towards Scalable and Practical Concept Erasure for Text-to-Image Diffusion Models, Hoigi Seo, Byung Hyun Lee, Jaehyun Cho et al., arXiv 2026 · http://arxiv.org/abs/2604.16481v1
- [P-2604.10032] Closed-Form Concept Erasure via Double Projections, Chi Zhang, Jingpu Cheng, Zhixian Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.10032v1
- [P-2604.09405] EGLOCE: Training-Free Energy-Guided Latent Optimization for Concept Erasure, Junyeong Ahn, Seojin Yoon, Sungyong Baik, arXiv 2026 · http://arxiv.org/abs/2604.09405v1
- [P-2603.25994] Neighbor-Aware Localized Concept Erasure in Text-to-Image Diffusion Models, Zhuan Shi, Alireza Dehghanpour Farashah, Rik de Vries et al., arXiv 2026 · http://arxiv.org/abs/2603.25994v1
- [P-2604.03941] SafeCtrl: Region-Aware Safety Control for Text-to-Image Diffusion via Detect-Then-Suppress, Lingyun Zhang, Yu Xie, Zhongli Fang et al., arXiv 2026 · http://arxiv.org/abs/2604.03941v1
- [P-2604.03114] Can VLMs Truly Forget? Benchmarking Training-Free Visual Concept Unlearning, Zhangyun Tan, Zeliang Zhang, Susan Liang et al., arXiv 2026 · http://arxiv.org/abs/2604.03114v1
- [P-2604.03956] VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models, Ravi Ranjan, Agoritsa Polyzou, arXiv 2026 · http://arxiv.org/abs/2604.03956v2
- [P-2604.05634] PECKER: A Precisely Efficient Critical Knowledge Erasure Recipe For Machine Unlearning in Diffusion Models, Zhiyong Ma, Zhitao Deng, Huan Tang et al., arXiv 2026 · http://arxiv.org/abs/2604.05634v1
- [P-2604.13127] Graph Propagated Projection Unlearning: A Unified Framework for Vision and Audio Discriminative Models, Shreyansh Pathak, Jyotishman Das, arXiv 2026 · http://arxiv.org/abs/2604.13127v1
- [P-2604.08111] Bias Redistribution in Visual Machine Unlearning: Does Forgetting One Group Harm Another?, Yunusa Haruna, Adamu Lawan, Ibrahim Haruna Abdulhamid et al., arXiv 2026 · http://arxiv.org/abs/2604.08111v1
- [P-2604.08238] $\oslash$ Source Models Leak What They Shouldn't $\nrightarrow$: Unlearning Zero-Shot Transfer in Domain Adaptation Through Adversarial Optimization, Arnav Devalapally, Poornima Jain, Kartik Srinivas et al., arXiv 2026 · http://arxiv.org/abs/2604.08238v1
- [P-2604.02183] TRU: Targeted Reverse Update for Efficient Multimodal Recommendation Unlearning, Zhanting Zhou, KaHou Tam, Ziqiang Zheng et al., arXiv 2026 · http://arxiv.org/abs/2604.02183v2
- [P-2603.26316] SALMUBench: A Benchmark for Sensitive Association-Level Multimodal Unlearning, Cai Selvas-Sala, Lei Kang, Lluis Gomez, arXiv 2026 · http://arxiv.org/abs/2603.26316v1

### 클러스터 3 — 신뢰성·연속화·규제 (15)
- [P-2604.20300] FSFM: A Biologically-Inspired Framework for Selective Forgetting of Agent Memory, Yingjie Gu, Wenjian Xiong, Liqiang Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.20300v2
- [P-2604.19108] Robust Continual Unlearning against Knowledge Erosion and Forgetting Reversal, Eun-Ju Park, Youjin Shin, Simon S. Woo, arXiv 2026 · http://arxiv.org/abs/2604.19108v1
- [P-2604.18649] Position: No Retroactive Cure for Infringement during Training, Satoru Utsunomiya, Masaru Isonuma, Junichiro Mori et al., arXiv 2026 · http://arxiv.org/abs/2604.18649v1
- [P-2604.16536] Towards Reliable Testing of Machine Unlearning, Anna Mazhar, Sainyam Galhotra, arXiv 2026 · http://arxiv.org/abs/2604.16536v1
- [P-2604.15166] Class Unlearning via Depth-Aware Removal of Forget-Specific Directions, Arman Hatami, Romina Aalishah, Ilya E. Monosov, arXiv 2026 · http://arxiv.org/abs/2604.15166v1
- [P-2604.12686] BID-LoRA: A Parameter-Efficient Framework for Continual Learning and Unlearning, Jagadeesh Rachapudi, Ritali Vatsi, Praful Hambarde et al., arXiv 2026 · http://arxiv.org/abs/2604.12686v1
- [P-2604.12526] Orthogonal Subspace Projection for Continual Machine Unlearning via SVD-Based LoRA, Yogachandran Rahulamathavan, Nasir Iqbal, Juncheng Hu et al., arXiv 2026 · http://arxiv.org/abs/2604.12526v1
- [P-2604.12348] PrivEraserVerify: Efficient, Private, and Verifiable Federated Unlearning, Parthaw Goswami, Md Khairul Islam, Ashfak Yeafi, arXiv 2026 · http://arxiv.org/abs/2604.12348v1
- [P-2604.11511] The Price of Ignorance: Information-Free Quotation for Data Retention in Machine Unlearning, Bin Han, Di Feng, Zexin Fang et al., arXiv 2026 · http://arxiv.org/abs/2604.11511v1
- [P-2604.11306] Learning to Forget -- Hierarchical Episodic Memory for Lifelong Robot Deployment, Leonard Bärmann, Joana Plewnia, Alex Waibel et al., arXiv 2026 · http://arxiv.org/abs/2604.11306v1
- [P-2604.09391] Efficient Unlearning through Maximizing Relearning Convergence Delay, Khoa Tran, Simon S. Woo, arXiv 2026 · http://arxiv.org/abs/2604.09391v1
- [P-2604.08271] An Illusion of Unlearning? Assessing Machine Unlearning Through Internal Representations, Yichen Gao, Altay Unal, Akshay Rangamani et al., arXiv 2026 · http://arxiv.org/abs/2604.08271v1
- [P-2604.07962] Is your algorithm unlearning or untraining?, Eleni Triantafillou, Ahmed Imtiaz Humayun, Monica Ribero et al., arXiv 2026 · http://arxiv.org/abs/2604.07962v1
- [P-2604.00131] Oblivion: Self-Adaptive Agentic Memory Control through Decay-Driven Activation, Ashish Rana, Chia-Chien Hung, Qumeng Sun et al., arXiv 2026 · http://arxiv.org/abs/2604.00131v2
- [P-2603.26569] Machine Unlearning under Retain-Forget Entanglement, Jingpu Cheng, Ping Liu, Qianxiao Li et al., arXiv 2026 · http://arxiv.org/abs/2603.26569v1

---

## 메타 / 디버그
- model: claude-sonnet-4-6
