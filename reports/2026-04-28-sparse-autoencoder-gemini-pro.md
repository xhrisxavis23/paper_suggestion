# Research Topic Suggestion — "sparse autoencoder"

생성: 2026-04-28T07:33:00.894678+00:00
DB 윈도우: 2026-02-27 ~ 2026-04-28 (60d)
모델: gemini-2.5-pro
매칭 논문: 92건
확장 키워드: ['sparse autoencoder', 'SAE', 'sparse representation learning', 'sparse feature learning', 'autoencoder with sparsity constraint', 'k-sparse autoencoder', 'stacked sparse autoencoder', 'denoising sparse autoencoder', 'learning sparse representations', 'unsupervised sparse coding']

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — 기계론적 해석 가능성
- **설명**: 희소 오토인코더(SAE)를 사용해 언어 모델, 비전 모델 등 다양한 인공지능 모델의 내부 작동 방식을 분해하고, 인간이 이해할 수 있는 '피처(feature)' 단위로 해석하려는 연구 흐름입니다.
- **빈도**: 19건
- **월별 (≈15d씩, 오래된→최근)**: 6 → 4 → 4 → 5
- **대표 논문**:
  - [P-2603.03031] Step-Level Sparse Autoencoder for Reasoning Process Interpretation — Xuan Yang, Jiayu Liu, Yuhang Lai et al., arXiv 2026
  - [P-2603.23524] Navigating the Concept Space of Language Models — Wilson E. Marcílio-Jr, Danilo M. Eler, arXiv 2026
  - [P-2603.06557] Causal Interpretation of Neural Network Computations with Contribution Decomposition — Joshua Brendan Melander, Zaki Alaoui, Shenghua Liu et al., arXiv 2026

### 클러스터 2 — 모델 제어 및 편향 제거
- **설명**: SAE로 식별한 내부 피처에 직접 개입하여 모델의 행동을 원하는 방향으로 유도(steering)하거나, 사회적 편향 및 유해한 행동을 제거하는 등 모델의 안전성과 정렬(alignment)을 확보하는 연구입니다.
- **빈도**: 13건
- **월별 (≈15d씩, 오래된→최근)**: 2 → 6 → 1 → 4
- **대표 논문**:
  - [P-2602.24014] Interpretable Debiasing of Vision-Language Models for Social Fairness — Na Min An, Yoonna Jang, Yusuke Hirota et al., arXiv 2026
  - [P-2603.12795] SteerRM: Debiasing Reward Models via Sparse Autoencoders — Mengyuan Sun, Zhuohao Yu, Weizheng Gu et al., arXiv 2026
  - [P-2603.16335] Behavioral Steering in a 35B MoE Language Model via SAE-Decoded Probe Vectors: One Agency Axis, Not Five Traits — Jia Qing Yap, arXiv 2026

### 클러스터 3 — SAE 방법론 및 이론
- **설명**: 희소 오토인코더 자체의 안정성, 견고성, 학습 효율을 개선하거나, 희소성의 근본적인 한계와 같은 이론적 기반을 탐구하는 연구 클러스터입니다.
- **빈도**: 7건
- **월별 (≈15d씩, 오래된→최근)**: 1 → 1 → 4 → 1
- **대표 논문**:
  - [P-2603.04198] Stable and Steerable Sparse Autoencoders with Weight Regularization — Piotr Jedryszek, Oliver M. Crook, arXiv 2026
  - [P-2603.28744] Stop Probing, Start Coding: Why Linear Probes and Sparse Autoencoders Fail at Compositional Generalisation — Vitória Barin Pacela, Shruti Joshi, Isabela Camacho et al., arXiv 2026
  - [P-2604.03436] MetaSAEs: Joint Training with a Decomposability Penalty Produces More Atomic Sparse Autoencoder Latents — Matthew Levinson, arXiv 2026

### 클러스터 4 — 희소 표현 기반 응용
- **설명**: SAE를 활용하여 의미론적 개념 공간을 구축하고, 이를 정보 검색(IR), 이미지 검색, 모델 압축, 데이터 선택 등 다양한 다운스트림 태스크의 성능을 높이는 데 직접 적용하는 연구입니다.
- **빈도**: 6건
- **월별 (≈15d씩, 오래된→최근)**: 4 → 1 → 0 → 1
- **대표 논문**:
  - [P-2603.13277] Learning Retrieval Models with Sparse Autoencoders — Thibault Formal, Maxime Louis, Hervé Dejean et al., arXiv 2026
  - [P-2603.05781] Visual Words Meet BM25: Sparse Auto-Encoder Visual Word Scoring for Image Retrieval — Donghoon Han, Eunhwan Park, Seunghyeon Seo, arXiv 2026

### 클러스터 5 — 과학 도메인 모델 분석
- **설명**: 생물학(단일세포), 시계열(기후), 의학(의료영상), 물리(유체역학), 게임(체스) 등 특정 과학 및 전문 분야의 파운데이션 모델을 SAE로 분석하여 해당 도메인의 지식이 어떻게 표현되고 처리되는지 밝히는 연구입니다.
- **빈도**: 10건
- **월별 (≈15d씩, 오래된→최근)**: 3 → 3 → 3 → 1
- **대표 논문**:
  - [P-2603.01752] Causal Circuit Tracing Reveals Distinct Computational Architectures in Single-Cell Foundation Models: Inhibitory Dominance, Biological Coherence, and Cross-Model Convergence — Ihor Kendiukhov, arXiv 2026
  - [P-2603.10071] Dissecting Chronos: Sparse Autoencoders Reveal Causal Feature Hierarchies in Time Series Foundation Models — Anurag Mishra, arXiv 2026
  - [P-2604.10158] Tracing the Thought of a Grandmaster-level Chess-Playing Transformer — Rui Lin, Zhenyu Jin, Guancheng Zhou et al., arXiv 2026

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap B — 여러 연구에서 모델 내부의 지식과 실제 출력 사이의 괴리를 지적하며, 해석 가능성이 반드시 제어 가능성으로 이어지지 않는다는 한계를 반복적으로 
- **타입**: recurring-limitation
- **설명**: 여러 연구에서 모델 내부의 지식과 실제 출력 사이의 괴리를 지적하며, 해석 가능성이 반드시 제어 가능성으로 이어지지 않는다는 한계를 반복적으로 드러냅니다. 특정 개념을 담당하는 피처를 성공적으로 찾아내더라도, 이를 직접 수정하는 개입(intervention)이 의도치 않은 부작용(예: "output drift")을 낳거나 거의 효과가 없는 경우가 많습니다. 이는 '해석'에서 '안전한 교정'으로 나아가는 데 있어 핵심적인 난관임을 시사합니다.
- **근거 논문**: P-2603.18353, P-2603.25075
- **Skeptic 검토**: ✓ 통과 — 제시된 논문들이 '해석 가능성이 행동 가능성을 보장하지 않는다'는 근본적인 문제를 명시적으로 제기하므로, 이는 중요한 현재의 한계점으로 인정됩니다.

### Gap C — `arxiv:2604.10158` 논문은 체스 AI의 의사결정 과정을 해석하기 위해 희소 분해 프레임워크를 적용했습니다. 이는 '과학 도메인 모
- **타입**: single-shot
- **설명**: `arxiv:2604.10158` 논문은 체스 AI의 의사결정 과정을 해석하기 위해 희소 분해 프레임워크를 적용했습니다. 이는 '과학 도메인 모델 분석' 클러스터 내에서 유일하게 생물학이나 물리학 같은 자연과학이 아닌, 게임 이론과 기호 추론이라는 독특한 영역을 다룹니다. 하지만 후속 연구에서 이 방법론을 다른 복잡한 게임(예: 바둑)이나 정리 증명, 프로그램 합성 같은 다른 형식적 추론(formal reasoning) 문제로 확장한 사례가 보이지 않아 단발성 탐구에 그치고 있습니다.
- **근거 논문**: P-2604.10158
- **Skeptic 검토**: ✓ 통과 — 형식적 추론이라는 독특한 도메인에 대한 연구가 현재 메타DB 내에서 단 한 건에 그치고 있어, 해당 방향성의 일반화 가능성이 아직 탐색되지 않은 초기 단계의 갭으로 볼 수 있습니다.

### Gap D — SAE의 핵심 가정인 '희소성(sparsity)'이 오히려 해석 가능성을 해치거나 다른 문제를 야기할 수 있다는 우려가 제기되고 있습니다. 극단
- **타입**: recurring-limitation
- **설명**: SAE의 핵심 가정인 '희소성(sparsity)'이 오히려 해석 가능성을 해치거나 다른 문제를 야기할 수 있다는 우려가 제기되고 있습니다. 극단적인 희소성은 "치명적인 해석 가능성 붕괴(catastrophic interpretability collapse)"를 유발할 수 있으며(`arxiv:2603.18056`), 현재의 SAE 학습 방식은 "분포 외(OOD) 데이터에서의 합성적 일반화(compositional generalisation)"에 실패하는 근본적 한계를 가집니다(`arxiv:2603.28744`). 이는 희소성이라는 단일 목표만으로는 안정적이고 유용한 피처를 학습하기에 불충분함을 시사합니다.
- **근거 논문**: P-2603.18056, P-2603.28744
- **Skeptic 검토**: ✓ 통과 — SAE 방법론의 근간이 되는 '희소성' 제약 자체의 이론적, 실증적 한계를 직접적으로 지적하는 논문들이 존재하므로, 이는 방법론 자체의 발전을 위해 반드시 다루어져야 할 핵심적인 갭입니다.

### Gap E — 'SAE 방법론 및 이론' 클러스터에서는 모델의 안정성(stability), 견고성(robustness), 원자성(atomicity)을 높이기 
- **타입**: between-clusters
- **설명**: 'SAE 방법론 및 이론' 클러스터에서는 모델의 안정성(stability), 견고성(robustness), 원자성(atomicity)을 높이기 위한 연구가 진행되고 있습니다. 반면, '희소 표현 기반 응용' 클러스터의 연구들은 주로 정보 검색이나 모델 압축 같은 다운스트림 태스크 성능 자체에 집중합니다. 응용 연구에서 방법론 클러스터의 최신 성과(예: OOD 견고성을 높인 SAE)를 적극적으로 도입하여, 응용 성능의 안정성과 신뢰성을 높이는 시도는 아직 부족해 보입니다.
- **근거 논문**: P-2604.06495, P-2603.13277, P-2604.03436
- **Skeptic 검토**: ✓ 통과 — 이론/방법론 클러스터에서 제안된 개선 사항(견고성, 원자성 등)이 응용 클러스터의 논문들에서 적극적으로 채택되고 있지 않다는 점은 타당한 지적이며, 이론과 실제 적용 사이의 간극을 보여줍니다.

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap A** — 현재 '모델 제어 및 편향 제거' 클러스터의 연구는 주로 일반 언어 모델의 행동을 유도하는 데 집중하고 있습니다. 반면 '과학 도메인 모델 분석' 클러스터는 생물학, 기후, 유체 역학 등 전문 분야 모델의 내부 작동을 '해석'하는 데 그치고 있습니다. 이 두 영역을 결합하여, 과학 도메인 모델에서 발견된 해석 가능한 피처에 직접 개입함으로써 특정 예측(예: 세포 상태 변화 유도, 특정 기후 시나리오 시뮬레이션)을 제어하거나 편향을 교정하는 연구는 아직 본격적으로 시도되지 않은 연구 갭으로 보입니다. · 거부 사유: (a) 다른 클러스터에서 이미 다룸. '과학 도메인 모델 분석' 클러스터 내에서 이미 과학 모델의 피처를 직접 제어(steering)하는 연구가 수행되었습니다. [arxiv:2603.11940, arxiv:2604.04946]

</details>

## 3. 연구 제안 (Proposer)

### 제안 1 — C-SAFE
**가설**: 모델의 행동은 개별 피처가 아닌 피처 간의 상호작용 회로(circuit)에 의해 결정되므로, 회로 구조를 고려한 개입은 부작용을 줄이면서 더 정밀한 제어를 가능하게 할 것이다.
**메우는 갭**: B
**접근**: Causal Concept Graphs(CCG) 방법론을 사용하여 특정 작업과 관련된 희소 피처들의 상호작용 그래프를 먼저 추출합니다. 단일 피처를 직접 조작하는 대신, 그래프 상의 인과 관계를 고려하여 여러 피처에 걸친 조향 벡터(steering vector)를 계산하고 적용합니다. 이 접근법의 효과를 측정하기 위해 목표 작업의 정확도 향상과 함께, 관련 없는 개념에 대한 예측 변화율(output drift)을 정량화하여 기존 방식과 비교합니다.
**Baselines**: Concept bottleneck steering, sparse autoencoder feature steering, logit lens with activation patching, ARC-Challenge, StrategyQA
**예상 기여**: 단일 피처 개입의 한계인 '지식-행동 격차'와 '출력 표류' 문제를 정면으로 다룹니다. 해석 가능성 연구를 개별 피처 분석에서 피처 간 상호작용 분석으로 확장하고, 더 안정적이고 신뢰할 수 있는 모델 제어 기술의 기반을 마련할 수 있습니다.
**참고**: P-2603.18353, P-2603.25075, P-2603.10377

### 제안 2 — FORMAL-DECOMP
**가설**: 희소 오토인코더는 체스뿐만 아니라 정리 증명이나 프로그램 합성 같은 다양한 형식적 추론 과제에서도 모델의 계산 과정을 인간이 해석 가능한 기호적 하위 연산(sub-operations)으로 분해할 수 있다.
**메우는 갭**: C
**접근**: 정리 증명 데이터셋(예: miniF2F)으로 학습된 트랜스포머 모델의 중간 레이어 활성화 값에 희소 분해 프레임워크를 적용합니다. 학습된 SAE 피처들이 '전제 분리', '가설 적용' 등과 같은 특정 논리적 연산에 선택적으로 반응하는지 분석합니다. 또한, 특정 피처를 활성화했을 때 모델이 특정 증명 전략을 따르도록 유도할 수 있는지 개입 실험을 통해 검증합니다.
**Baselines**: Leela Chess Zero (LC0) sparse decomposition framework
**예상 기여**: 기계론적 해석 가능성 방법론이 게임 이론을 넘어 더 넓은 기호 추론 영역에서도 유효함을 보입니다. 이는 신경망 모델이 어떻게 추상적이고 형식적인 추론을 수행하는지에 대한 근본적인 이해를 높이고, 신경-기호(neuro-symbolic) AI 연구에 새로운 방향을 제시할 수 있습니다.
**참고**: P-2604.10158

### 제안 3 — ADAPT-SAE
**가설**: 고정된 인코더 대신, 추론 시점에 입력 데이터에 맞춰 희소 코드를 반복적으로 최적화하는 절차를 도입하면 SAE의 분포 외(OOD) 합성 일반화 실패 문제를 완화할 수 있다.
**메우는 갭**: D
**접근**: 기존 SAE의 고정된 피드포워드 인코더를 고전적인 희소 코딩의 반복적 추론 알고리즘(예: FISTA)으로 대체하는 새로운 아키텍처를 제안합니다. 이 모델은 학습된 사전을 공유하지만, 각 입력에 대한 희소 표현은 추론 시간에 동적으로 계산됩니다. 제안된 모델의 성능을 통제된 합성 데이터셋을 사용하여 기존 SAE와 비교하며, 특히 이전에 보지 못한 개념 조합에 대한 재구성 오류 및 강건성을 집중적으로 평가합니다.
**Baselines**: Top-k SAE, L1 sparsification, FISTA
**예상 기여**: SAE의 '상각 격차(amortisation gap)'라는 근본적인 한계를 직접적으로 해결하는 새로운 학습 패러다임을 제시합니다. 이는 더 신뢰성 있고 강건한 피처를 학습하여, 해석 가능성 도구가 실제 배포 환경에서 마주칠 수 있는 다양한 입력에 대해 안정적으로 작동하도록 보장합니다.
**참고**: P-2603.28744, P-2603.18056

### 제안 4 — ROBUST-SPLARE
**가설**: 견고성 향상 기법으로 학습된 SAE를 학습된 희소 검색(LSR) 모델에 통합하면, 도메인 외 데이터셋에서의 검색 성능 저하를 크게 완화할 수 있다.
**메우는 갭**: E
**접근**: SPLARE 모델의 SAE 컴포넌트를 학습할 때, 마스킹 기반 정규화(masking-based regularization)와 같은 최신 강건성 향상 기법을 적용합니다. 이렇게 학습된 모델(ROBUST-SPLARE)의 검색 성능을 원래 SPLARE 모델과 비교합니다. 평가는 다국어 및 도메인 외 벤치마크인 MMTEB를 사용하여, 특히 도메인이 바뀌었을 때의 성능 하락 폭을 핵심 지표로 삼아 분석합니다.
**Baselines**: SPLARE, BM25-V, MMTEB
**예상 기여**: SAE 방법론의 이론적 발전이 실제 응용 시스템의 신뢰성 향상으로 이어진다는 구체적인 증거를 제시합니다. 이는 이론 연구와 응용 연구 사이의 간극을 좁히고, 더 강건한 AI 시스템을 구축하기 위한 연구 방향을 제시하는 중요한 사례가 될 것입니다.
**참고**: P-2603.13277, P-2604.06495, P-2603.05781

### 제안 5 — CODEC-STEER
**가설**: 신경망의 최종 출력에 대한 각 뉴런의 인과적 기여도(contribution)를 분해하여 얻은 피처를 조작하는 것이, 활성화(activation) 자체를 기반으로 한 피처를 조작하는 것보다 더 직접적이고 부작용이 적은 모델 제어를 가능하게 한다.
**메우는 갭**: B
**접근**: 먼저 CODEC 방법론을 사용하여 언어 모델의 각 뉴런이 특정 출력에 미치는 긍정적/부정적 기여도를 계산하고, 이를 SAE로 분해하여 '기여도 피처'를 추출합니다. 이후, 모델의 오류를 교정하기 위해 이 기여도 피처를 직접 조향(steering)합니다. 이 방법의 효과를 기존의 활성화 기반 조향 방법과 비교하며, 오류 교정 성공률과 의도치 않은 출력 변화율을 함께 측정하여 성능을 평가합니다.
**Baselines**: CODEC, SAE feature steering, linear probing with truthfulness separator vector
**예상 기여**: 모델 제어의 대상을 '무엇이 표현되는가(활성화)'에서 '무엇이 계산에 기여하는가(기여도)'로 전환하는 새로운 관점을 제시합니다. 이는 모델 내부 지식과 실제 행동 사이의 괴리를 줄일 수 있는 더 강력한 인과적 제어 방법을 제공하여, AI 안전성 및 오류 교정 분야의 중요한 진전을 이룰 수 있습니다.
**참고**: P-2603.06557, P-2603.18353

## 4. 참고문헌 (메타DB 기반)

### 클러스터 1 — 기계론적 해석 가능성 (19)
- [P-2603.03031] Step-Level Sparse Autoencoder for Reasoning Process Interpretation, Xuan Yang, Jiayu Liu, Yuhang Lai et al., arXiv 2026 · http://arxiv.org/abs/2603.03031v1
- [P-2603.23524] Navigating the Concept Space of Language Models, Wilson E. Marcílio-Jr, Danilo M. Eler, arXiv 2026 · http://arxiv.org/abs/2603.23524v1
- [P-2603.06557] Causal Interpretation of Neural Network Computations with Contribution Decomposition, Joshua Brendan Melander, Zaki Alaoui, Shenghua Liu et al., arXiv 2026 · http://arxiv.org/abs/2603.06557v1
- [P-2603.05805] Sparse Crosscoders for diffing MoEs and Dense models, Marmik Chaudhari, Nishkal Hundia, Idhant Gulati, arXiv 2026 · http://arxiv.org/abs/2603.05805v1
- [P-2603.09972] From Data Statistics to Feature Geometry: How Correlations Shape Superposition, Lucas Prieto, Edward Stevinson, Melih Barsbey et al., arXiv 2026 · http://arxiv.org/abs/2603.09972v1
- [P-2603.10377] Causal Concept Graphs in LLM Latent Space for Stepwise Reasoning, Md Muntaqim Meherab, Noor Islam S. Mohammad, Faiza Feroz, arXiv 2026 · http://arxiv.org/abs/2603.10377v2 · also_in: hf
- [P-2603.15615] Mechanistic Origin of Moral Indifference in Language Models, Lingyu Li, Yan Teng, Yingchun Wang, arXiv 2026 · http://arxiv.org/abs/2603.15615v1
- [P-2603.15919] Sparse but not Simpler: A Multi-Level Interpretability Analysis of Vision Transformers, Siyu Zhang, arXiv 2026 · http://arxiv.org/abs/2603.15919v2
- [P-2603.17624] Do Language Models Encode Semantic Relations? Probing and Sparse Feature Analysis, Andor Diera, Ansgar Scherp, arXiv 2026 · http://arxiv.org/abs/2603.17624v2
- [P-2603.18353] Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations, Sanjay Basu, Sadiq Y. Patel, Parth Sheth et al., arXiv 2026 · http://arxiv.org/abs/2603.18353v1
- [P-2603.25075] Sparse Visual Thought Circuits in Vision-Language Models, Yunpeng Zhou, arXiv 2026 · http://arxiv.org/abs/2603.25075v1
- [P-2603.26323] From Human Cognition to Neural Activations: Probing the Computational Primitives of Spatial Reasoning in LLMs, Jiyuan An, Liner Yang, Mengyan Wang et al., arXiv 2026 · http://arxiv.org/abs/2603.26323v1
- [P-2604.11061] Pando: Do Interpretability Methods Work When Models Won't Explain Themselves?, Ziqian Zhong, Aashiq Muhamed, Mona T. Diab et al., arXiv 2026 · http://arxiv.org/abs/2604.11061v1
- [P-2604.11962] The Linear Centroids Hypothesis: How Deep Network Features Represent Data, Thomas Walker, Ahmed Imtiaz Humayun, Randall Balestriero et al., arXiv 2026 · http://arxiv.org/abs/2604.11962v1
- [P-2604.13304] Can Cross-Layer Transcoders Replace Vision Transformer Activations? An Interpretable Perspective on Vision, Gerasimos Chatzoudis, Konstantinos D. Polyzos, Zhuowei Li et al., arXiv 2026 · http://arxiv.org/abs/2604.13304v1
- [P-2604.19974] Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders, Het Patel, Tiejin Chen, Hua Wei et al., arXiv 2026 · http://arxiv.org/abs/2604.19974v1
- [P-2604.05090] Multilingual Language Models Encode Script Over Linguistic Structure, Aastha A K Verma, Anwoy Chatterjee, Mehak Gupta et al., arXiv 2026 · http://arxiv.org/abs/2604.05090v2
- [P-2604.00443] Polysemanticity or Polysemy? Lexical Identity Confounds Superposition Metrics, Iyad Ait Hou, Rebecca Hwa, arXiv 2026 · http://arxiv.org/abs/2604.00443v1
- [P-2604.02685] Finding Belief Geometries with Sparse Autoencoders, Matthew Levinson, arXiv 2026 · http://arxiv.org/abs/2604.02685v1

### 클러스터 2 — 모델 제어 및 편향 제거 (13)
- [P-2602.24014] Interpretable Debiasing of Vision-Language Models for Social Fairness, Na Min An, Yoonna Jang, Yusuke Hirota et al., arXiv 2026 · http://arxiv.org/abs/2602.24014v1
- [P-2603.04069] Monitoring Emergent Reward Hacking During Generation via Internal Activations, Patrick Wilhelm, Thorsten Wittkopp, Odej Kao, arXiv 2026 · http://arxiv.org/abs/2603.04069v1
- [P-2603.12795] SteerRM: Debiasing Reward Models via Sparse Autoencoders, Mengyuan Sun, Zhuohao Yu, Weizheng Gu et al., arXiv 2026 · http://arxiv.org/abs/2603.12795v1
- [P-2603.11493] OrthoEraser: Coupled-Neuron Orthogonal Projection for Concept Erasure, Chuancheng Shi, Wenhua Wu, Fei Shen et al., arXiv 2026 · http://arxiv.org/abs/2603.11493v1
- [P-2603.16335] Behavioral Steering in a 35B MoE Language Model via SAE-Decoded Probe Vectors: One Agency Axis, Not Five Traits, Jia Qing Yap, arXiv 2026 · http://arxiv.org/abs/2603.16335v1
- [P-2603.19028] SEM: Sparse Embedding Modulation for Post-Hoc Debiasing of Vision-Language Models, Quentin Guimard, Federico Bartsch, Simone Caldarella et al., arXiv 2026 · http://arxiv.org/abs/2603.19028v1 · also_in: hf
- [P-2603.22593] Language Models Can Explain Visual Features via Steering, Javier Ferrando, Enrique Lopez-Cuena, Pablo Agustin Martin-Torres et al., arXiv 2026 · http://arxiv.org/abs/2603.22593v2
- [P-2603.21461] DSPA: Dynamic SAE Steering for Data-Efficient Preference Alignment, James Wedgwood, Aashiq Muhamed, Mona T. Diab et al., arXiv 2026 · http://arxiv.org/abs/2603.21461v1
- [P-2603.23301] Steering LLMs for Culturally Localized Generation, Simran Khanuja, Hongbin Liu, Shujian Zhang et al., arXiv 2026 · http://arxiv.org/abs/2603.23301v1
- [P-2604.12384] Preventing Safety Drift in Large Language Models via Coupled Weight and Activation Constraints, Songping Peng, Zhiheng Zhang, Daojian Zeng et al., arXiv 2026 · http://arxiv.org/abs/2604.12384v1
- [P-2604.18756] Towards Understanding the Robustness of Sparse Autoencoders, Ahson Saiyed, Sabrina Sadiekh, Chirag Agarwal, arXiv 2026 · http://arxiv.org/abs/2604.18756v1
- [P-2604.11467] From Attribution to Action: A Human-Centered Application of Activation Steering, Tobias Labarta, Maximilian Dreyer, Katharina Weitz et al., arXiv 2026 · http://arxiv.org/abs/2604.11467v1
- [P-2604.03532] LangFIR: Discovering Sparse Language-Specific Features from Monolingual Data for Language Steering, Sing Hieng Wong, Hassan Sajjad, A. B. Siddique, arXiv 2026 · http://arxiv.org/abs/2604.03532v1

### 클러스터 3 — SAE 방법론 및 이론 (7)
- [P-2603.04198] Stable and Steerable Sparse Autoencoders with Weight Regularization, Piotr Jedryszek, Oliver M. Crook, arXiv 2026 · http://arxiv.org/abs/2603.04198v1
- [P-2603.18056] Fundamental Limits of Neural Network Sparsification: Evidence from Catastrophic Interpretability Collapse, Dip Roy, Rajiv Misra, Sanjay Kumar Singh, arXiv 2026 · http://arxiv.org/abs/2603.18056v1
- [P-2603.28744] Stop Probing, Start Coding: Why Linear Probes and Sparse Autoencoders Fail at Compositional Generalisation, Vitória Barin Pacela, Shruti Joshi, Isabela Camacho et al., arXiv 2026 · http://arxiv.org/abs/2603.28744v1
- [P-2604.14925] Improving Sparse Autoencoder with Dynamic Attention, Dongsheng Wang, Jinsen Zhang, Dawei Su et al., arXiv 2026 · http://arxiv.org/abs/2604.14925v1
- [P-2604.06495] Improving Robustness In Sparse Autoencoders via Masked Regularization, Vivek Narayanaswamy, Kowshik Thopalli, Bhavya Kailkhura et al., arXiv 2026 · http://arxiv.org/abs/2604.06495v1
- [P-2604.04037] Geometric Limits of Knowledge Distillation: A Minimum-Width Theorem via Superposition Theory, Nilesh Sarkar, Dawar Jyoti Deka, arXiv 2026 · http://arxiv.org/abs/2604.04037v2
- [P-2604.03436] MetaSAEs: Joint Training with a Decomposability Penalty Produces More Atomic Sparse Autoencoder Latents, Matthew Levinson, arXiv 2026 · http://arxiv.org/abs/2604.03436v1

### 클러스터 4 — 희소 표현 기반 응용 (5)
- [P-2603.13277] Learning Retrieval Models with Sparse Autoencoders, Thibault Formal, Maxime Louis, Hervé Dejean et al., arXiv 2026 · http://arxiv.org/abs/2603.13277v1
- [P-2603.05781] Visual Words Meet BM25: Sparse Auto-Encoder Visual Word Scoring for Image Retrieval, Donghoon Han, Eunhwan Park, Seunghyeon Seo, arXiv 2026 · http://arxiv.org/abs/2603.05781v1
- [P-2603.02908] SAE as a Crystal Ball: Interpretable Features Predict Cross-domain Transferability of LLMs without Training, Qi Zhang, Yifei Wang, Xiaohan Wang et al., arXiv 2026 · http://arxiv.org/abs/2603.02908v1
- [P-2603.04981] Rethinking Representativeness and Diversity in Dynamic Data Selection, Yuzhe Zhou, Zhenglin Hua, Haiyun Guo et al., arXiv 2026 · http://arxiv.org/abs/2603.04981v1
- [P-2604.21511] From Tokens to Concepts: Leveraging SAE for SPLADE, Yuxuan Zong, Mathias Vast, Basile Van Cooten et al., arXiv 2026 · http://arxiv.org/abs/2604.21511v1

### 클러스터 5 — 과학 도메인 모델 분석 (10)
- [P-2603.01752] Causal Circuit Tracing Reveals Distinct Computational Architectures in Single-Cell Foundation Models: Inhibitory Dominance, Biological Coherence, and Cross-Model Convergence, Ihor Kendiukhov, arXiv 2026 · http://arxiv.org/abs/2603.01752v2
- [P-2603.02952] Sparse autoencoders reveal organized biological knowledge but minimal regulatory logic in single-cell foundation models: a comparative atlas of Geneformer and scGPT, Ihor Kendiukhov, arXiv 2026 · http://arxiv.org/abs/2603.02952v1
- [P-2603.11940] Exhaustive Circuit Mapping of a Single-Cell Foundation Model Reveals Massive Redundancy, Heavy-Tailed Hub Architecture, and Layer-Dependent Differentiation Control, Ihor Kendiukhov, arXiv 2026 · http://arxiv.org/abs/2603.11940v1
- [P-2603.10071] Dissecting Chronos: Sparse Autoencoders Reveal Causal Feature Hierarchies in Time Series Foundation Models, Anurag Mishra, arXiv 2026 · http://arxiv.org/abs/2603.10071v1
- [P-2603.19325] Target Concept Tuning Improves Extreme Weather Forecasting, Shijie Ren, Xinyue Gu, Ziheng Peng et al., arXiv 2026 · http://arxiv.org/abs/2603.19325v1
- [P-2603.23794] Sparse Autoencoders for Interpretable Medical Image Representation Learning, Philipp Wesp, Robbie Holland, Vasiliki Sideri-Lampretsa et al., arXiv 2026 · http://arxiv.org/abs/2603.23794v1
- [P-2604.10158] Tracing the Thought of a Grandmaster-level Chess-Playing Transformer, Rui Lin, Zhenyu Jin, Guancheng Zhou et al., arXiv 2026 · http://arxiv.org/abs/2604.10158v1
- [P-2604.06256] Spectral Edge Dynamics Reveal Functional Modes of Learning, Yongzhong Xu, arXiv 2026 · http://arxiv.org/abs/2604.06256v1
- [P-2604.01619] Automatic Image-Level Morphological Trait Annotation for Organismal Images, Vardaan Pahuja, Samuel Stevens, Alyson East et al., arXiv 2026 · http://arxiv.org/abs/2604.01619v2 · also_in: hf
- [P-2604.04946] Sparse Autoencoders as a Steering Basis for Phase Synchronization in Graph-Based CFD Surrogates, Yeping Hu, Ruben Glatt, Shusen Liu, arXiv 2026 · http://arxiv.org/abs/2604.04946v1

### 기타 (클러스터 미분류) (38)
- [P-2603.05708] Interpretable Perception and Reasoning for Audiovisual Geolocation, Yiyang Su, Xiaoming Liu, arXiv 2026 · http://arxiv.org/abs/2603.05708v1
- [P-2603.05716] Introducing the transitional autonomous vehicle lane-changing dataset: Empirical Experiments, Abhinav Sharma, Zijun He, Danjue Chen, arXiv 2026 · http://arxiv.org/abs/2603.05716v1
- [P-2603.07343] Learning Concept Bottleneck Models from Mechanistic Explanations, Antonio De Santis, Schrasing Tong, Marco Brambilla et al., arXiv 2026 · http://arxiv.org/abs/2603.07343v1
- [P-2603.07335] VisualScratchpad: Inference-time Visual Concepts Analysis in Vision Language Models, Hyesu Lim, Jinho Choi, Taekyung Kim et al., arXiv 2026 · http://arxiv.org/abs/2603.07335v1
- [P-2603.07566] GRD-Net: Generative-Reconstructive-Discriminative Anomaly Detection with Region of Interest Attention Module, Niccolò Ferrari, Michele Fraccaroli, Evelina Lamma, arXiv 2026 · http://arxiv.org/abs/2603.07566v1
- [P-2603.07454] SLNet: A Super-Lightweight Geometry-Adaptive Network for 3D Point Cloud Recognition, Mohammad Saeid, Amir Salarpour, Pedram MohajerAnsari et al., arXiv 2026 · http://arxiv.org/abs/2603.07454v1
- [P-2603.08869] One Language, Two Scripts: Probing Script-Invariance in LLM Concept Representations, Sripad Karne, arXiv 2026 · http://arxiv.org/abs/2603.08869v1
- [P-2603.10092] Execution Is the New Attack Surface: Survivability-Aware Agentic Crypto Trading with OpenClaw-Style Local Executors, Ailiya Borjigin, Igor Stadnyk, Ben Bilski et al., arXiv 2026 · http://arxiv.org/abs/2603.10092v1
- [P-2603.12564] Sell Me This Stock: Unsafe Recommendation Drift in LLM Agents, Zekun Wu, Adriano Koshiyama, Sahan Bulathwela et al., arXiv 2026 · http://arxiv.org/abs/2603.12564v7
- [P-2603.13895] MO-SAE:Multi-Objective Stacked Autoencoders Optimization for Edge Anomaly Detection, Lizhao Zhang, Shengsong Kong, Tao Guo et al., arXiv 2026 · http://arxiv.org/abs/2603.13895v1
- [P-2603.16440] Capability-Guided Compression: Toward Interpretability-Aware Budget Allocation for Large Language Models, Rishaank Gupta, arXiv 2026 · http://arxiv.org/abs/2603.16440v1
- [P-2603.16558] Segmentation-Based Attention Entropy: Detecting and Mitigating Object Hallucinations in Large Vision-Language Models, Jiale Song, Jiaxin Luo, Xue-song Tang et al., arXiv 2026 · http://arxiv.org/abs/2603.16558v1
- [P-2603.18729] Analysis Of Linguistic Stereotypes in Single and Multi-Agent Generative AI Architectures, Martina Ullasci, Marco Rondina, Riccardo Coppola et al., arXiv 2026 · http://arxiv.org/abs/2603.18729v1
- [P-2603.19233] Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models, Bryce Grant, Xijia Zhao, Peng Wang, arXiv 2026 · http://arxiv.org/abs/2603.19233v1
- [P-2603.19183] Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models, Aiden Swann, Lachlain McGranahan, Hugo Buurmeijer et al., arXiv 2026 · http://arxiv.org/abs/2603.19183v1
- [P-2603.26743] Steering Sparse Autoencoder Latents to Control Dynamic Head Pruning in Vision Transformers (Student Abstract), Yousung Lee, Dongsoo Har, arXiv 2026 · http://arxiv.org/abs/2603.26743v1
- [P-2603.24045] LGEST: Dynamic Spatial-Spectral Expert Routing for Hyperspectral Image Classification, Jiawen Wen, Suixuan Qiu, Zihang Luo et al., arXiv 2026 · http://arxiv.org/abs/2603.24045v1
- [P-2603.25325] How Pruning Reshapes Features: Sparse Autoencoder Analysis of Weight-Pruned Language Models, Hector Borobia, Elies Seguí-Mas, Guillermina Tormo-Carbó, arXiv 2026 · http://arxiv.org/abs/2603.25325v1
- [P-2603.26236] A Universal Vibe? Finding and Controlling Language-Agnostic Informal Register with SAEs, Uri Z. Kialy, Avi Shtarkberg, Ayal Klein, arXiv 2026 · http://arxiv.org/abs/2603.26236v1
- [P-2603.27195] AutoMS: Multi-Agent Evolutionary Search for Cross-Physics Inverse Microstructure Design, Zhenyuan Zhao, Yu Xing, Tianyang Xue et al., arXiv 2026 · http://arxiv.org/abs/2603.27195v2
- [P-2604.20895] Towards a Systematic Risk Assessment of Deep Neural Network Limitations in Autonomous Driving Perception, Svetlana Pavlitska, Christopher Gerking, J. Marius Zöllner, arXiv 2026 · http://arxiv.org/abs/2604.20895v1
- [P-2604.18179] Committed SAE-Feature Traces for Audited-Session Substitution Detection in Hosted LLMs, Ziyang Liu, arXiv 2026 · http://arxiv.org/abs/2604.18179v1
- [P-2604.17025] Harness as an Asset: Enforcing Determinism via the Convergent AI Agent Framework (CAAF), Tianbao Zhang, arXiv 2026 · http://arxiv.org/abs/2604.17025v1
- [P-2604.17391] RISC-V Functional Safety for Autonomous Automotive Systems: An Analytical Framework and Research Roadmap for ML-Assisted Certification, Nick Andreasyan, Mikhail Struve, Alexey Popov et al., arXiv 2026 · http://arxiv.org/abs/2604.17391v1
- [P-2604.11549] Human Centered Non Intrusive Driver State Modeling Using Personalized Physiological Signals in Real World Automated Driving, David Puertas-Ramirez, Raul Fernandez-Matellan, David Martin Gomez et al., arXiv 2026 · http://arxiv.org/abs/2604.11549v1
- [P-2604.11749] HistLens: Mapping Idea Change across Concepts and Corpora, Yi Jing, Weiyun Qiu, Yihang Peng et al., arXiv 2026 · http://arxiv.org/abs/2604.11749v1
- [P-2604.08846] Dictionary-Aligned Concept Control for Safeguarding Multimodal LLMs, Jinqi Luo, Jinyu Yang, Tal Neiman et al., arXiv 2026 · http://arxiv.org/abs/2604.08846v1
- [P-2604.09364] Arbitration Failure, Not Perceptual Blindness: How Vision-Language Models Resolve Visual-Linguistic Conflicts, Farhad Nooralahzadeh, Omid Rohanian, Yi Zhang et al., arXiv 2026 · http://arxiv.org/abs/2604.09364v2
- [P-2604.13466] Functional Emotions or Situational Contexts? A Discriminating Test from the Mythos Preview System Card, Hiranya V. Peiris, arXiv 2026 · http://arxiv.org/abs/2604.13466v2
- [P-2604.08461] OVS-DINO: Open-Vocabulary Segmentation via Structure-Aligned SAM-DINO with Language Guidance, Haoxi Zeng, Qiankun Liu, Yi Bin et al., arXiv 2026 · http://arxiv.org/abs/2604.08461v1
- [P-2604.05318] DIA-HARM: Dialectal Disparities in Harmful Content Detection Across 50 English Dialects, Jason Lucas, Matt Murtagh, Ali Al-Lawati et al., arXiv 2026 · http://arxiv.org/abs/2604.05318v1
- [P-2604.05724] Beyond Semantics: Disentangling Information Scope in Sparse Autoencoders for CLIP, Yusung Ro, Jaehyun Choi, Junmo Kim, arXiv 2026 · http://arxiv.org/abs/2604.05724v1
- [P-2604.04720] What Makes Good Multilingual Reasoning? Disentangling Reasoning Traces with Measurable Features, Dayeon Ki, Kevin Duh, Marine Carpuat, arXiv 2026 · http://arxiv.org/abs/2604.04720v1
- [P-2604.16430] HalluSAE: Detecting Hallucinations in Large Language Models via Sparse Auto-Encoders, Boshui Chen, Zhaoxin Fan, Ke Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.16430v1
- [P-2604.03919] Interpreting Video Representations with Spatio-Temporal Sparse Autoencoders, Atahan Dokme, Sriram Vishwanath, arXiv 2026 · http://arxiv.org/abs/2604.03919v1
- [P-2604.02871] SPG: Sparse-Projected Guides with Sparse Autoencoders for Zero-Shot Anomaly Detection, Tomoyasu Nanaumi, Yukino Tsuzuki, Junichi Okubo et al., arXiv 2026 · http://arxiv.org/abs/2604.02871v1
- [P-2604.02206] LEO: Graph Attention Network based Hybrid Multi Sensor Extended Object Fusion and Tracking for Autonomous Driving Applications, Mayank Mayank, Bharanidhar Duraisamy, Florian Geiss, arXiv 2026 · http://arxiv.org/abs/2604.02206v1
- [P-2604.01764] Hidden Meanings in Plain Sight: RebusBench for Evaluating Cognitive Visual Reasoning, Seyed Amir Kasaei, Arash Marioriyad, Mahbod Khaleti et al., arXiv 2026 · http://arxiv.org/abs/2604.01764v1

---

## 메타 / 디버그
- model: gemini-2.5-pro
- backend: gemini-pro-sdk
- matched_n: 92
- matched_total_before_cap: 92
- window_days: 60
- tokens_in_uncached: 8786
- tokens_in_cached_read: 114164
- tokens_out: 6447
- usd_estimate: $0.1108
