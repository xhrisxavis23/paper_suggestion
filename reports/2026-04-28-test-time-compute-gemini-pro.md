# Research Topic Suggestion — "test-time compute"

생성: 2026-04-28T07:30:01.560657+00:00
DB 윈도우: 2026-02-27 ~ 2026-04-28 (60d)
모델: gemini-2.5-pro
매칭 논문: 200건
확장 키워드: ['test-time computation', 'computation at test time', 'test-time adaptation', 'TTA', 'inference-time adaptation', 'test-time training', 'TTT', 'on-the-fly adaptation', 'adaptive inference', 'conditional computation', 'dynamic neural network']

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — VLM 테스트 시점 적응
- **설명**: Vision-Language Model(VLM)을 소스 데이터 없이 테스트 데이터에 적응시켜 분포 변화(distribution shift)에 대한 강건성을 높이는 연구. 주로 CLIP과 같은 모델의 제로샷 성능을 향상시키는 데 초점을 맞춥니다.
- **빈도**: 4건
- **월별 (≈15d씩, 오래된→최근)**: 0 → 0 → 2 → 2
- **대표 논문**:
  - [P-2604.21360] Prototype-Based Test-Time Adaptation of Vision-Language Models — Zhaohong Huang, Yuxin Zhang, Wenjing Liu et al., arXiv 2026
  - [P-2604.21728] Ramen: Robust Test-Time Adaptation of Vision-Language Models with Active Sample Selection — Wenxuan Bao, Yanjun Zhao, Xiyuan Yang et al., arXiv 2026
  - [P-2604.19093] Multi-modal Test-time Adaptation via Adaptive Probabilistic Gaussian Calibration — Jinglin Xu, Yi Li, Chuxiong Sun et al., arXiv 2026

### 클러스터 2 — 분포 변화 대응 강건성
- **설명**: 도메인 및 의미 변화(semantic shift)가 결합된 현실적인 테스트 환경에서의 강건성 확보를 목표로 하는 연구. OOD(Out-of-Distribution) 탐지 성능을 높이거나, 연속적인 도메인 변화에 대응하는 방법론을 제안합니다.
- **빈도**: 4건
- **월별 (≈15d씩, 오래된→최근)**: 2 → 1 → 0 → 1
- **대표 논문**:
  - [P-2604.21772] Back to Source: Open-Set Continual Test-Time Adaptation via Domain Compensation — Yingkai Yang, Chaoqi Chen, Hui Huang, arXiv 2026
  - [P-2604.15756] TTL: Test-time Textual Learning for OOD Detection with Pretrained Vision-Language Models — Jinlun Ye, Jiang Liao, Runhe Lai et al., arXiv 2026
  - [P-2604.17542] Dual Strategies for Test-Time Adaptation — Nam Nguyen Phuong, Duc Nguyen The Minh, Phi Le Nguyen et al., arXiv 2026

### 클러스터 3 — 추론 모델의 테스트 시점 훈련
- **설명**: 테스트 시점에 모델 파라미터를 직접 업데이트하여 추론 능력을 지속적으로 향상시키는 Test-Time Training(TTT) 연구. 주로 LLM의 복잡한 추론 작업에서 추가적인 계산을 통해 성능을 극대화하는 기법을 다룹니다.
- **빈도**: 4건
- **월별 (≈15d씩, 오래된→최근)**: 1 → 0 → 2 → 1
- **대표 논문**:
  - [P-2604.19295] TEMPO: Scaling Test-time Training for Large Reasoning Models — Qingyang Zhang, Xinke Kong, Haitao Wu et al., arXiv 2026
  - [P-2604.20915] Absorber LLM: Harnessing Causal Synchronization for Test-Time Training — Zhixin Zhang, Shabo Zhang, Chengcan Wu et al., arXiv 2026
  - [P-2604.17912] Learning to Correct: Calibrated Reinforcement Learning for Multi-Attempt Chain-of-Thought — Muhammed Emrullah Ildiz, Halil Alperen Gozeten, Ege Onur Taga et al., arXiv 2026

### 클러스터 4 — 의료 영상 분석 적용
- **설명**: EEG 신호 분석, 의료 영상 분할 등 특정 의료 도메인에 테스트 시점 적응을 적용하는 연구. 장비나 환자 집단 간의 데이터 분포 차이를 극복하여 임상 환경에서의 모델 일반화 성능을 높입니다.
- **빈도**: 2건
- **월별 (≈15d씩, 오래된→최근)**: 0 → 2 → 0 → 0
- **대표 논문**:
  - [P-2604.16926] Test-Time Adaptation for EEG Foundation Models: A Systematic Study under Real-World Distribution Shifts — Gabriel Jason Lee, Jathurshan Pradeepkumar, Jimeng Sun, arXiv 2026
  - [P-2604.17451] SegTTA: Training-Free Test-Time Augmentation for Zero-Shot Medical Imaging Segmentation — Yihong Yao, Chunlei Li, Canxuan Gang et al., arXiv 2026

### 클러스터 5 — 효율적/블랙박스 적응
- **설명**: API를 통해서만 접근 가능한 블랙박스 모델을 적응시키거나, 쿼리 비용 및 지연 시간을 최소화하는 등 실용적 제약 조건 하에서 테스트 시점 적응의 효율성을 높이는 연구입니다.
- **빈도**: 2건
- **월별 (≈15d씩, 오래된→최근)**: 1 → 1 → 0 → 0
- **대표 논문**:
  - [P-2604.15609] Adapting in the Dark: Efficient and Stable Test-Time Adaptation for Black-Box Models — Yunbei Zhang, Shuaicheng Niu, Chengyi Cai et al., arXiv 2026
  - [P-2604.17337] AutoSearch: Adaptive Search Depth for Efficient Agentic RAG via Reinforcement Learning — Jingbo Sun, Wenyue Chong, Songjun Tu et al., arXiv 2026

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap A — 여러 연구에서 기존 테스트 시점 적응(TTA) 방법론이 불안정하거나 오히려 성능 저하를 일으킬 수 있다는 한계를 반복적으로 지적하고 있습니다. 
- **타입**: recurring-limitation
- **설명**: 여러 연구에서 기존 테스트 시점 적응(TTA) 방법론이 불안정하거나 오히려 성능 저하를 일으킬 수 있다는 한계를 반복적으로 지적하고 있습니다. EEG 데이터 분석 연구(arxiv:2604.16926)에서는 "표준 TTA 방법이 일관성 없는 이득을 보이며 종종 성능을 저하시킨다"고 언급했으며, 추론 모델 연구(arxiv:2604.19295)에서도 "기존 TTT 방법들이 빠르게 정체되어 성능 고원과 다양성 붕괴로 이어진다"고 명시했습니다. 이는 TTA의 안정성과 지속적인 효과가 아직 해결되지 않은 주요 과제임을 보여줍니다.
- **근거 논문**: P-2604.16926, P-2604.19295
- **Skeptic 검토**: ✓ 통과 — 의료, 언어 추론 등 서로 다른 클러스터의 논문들이 공통적으로 TTA의 근본적인 불안정성 문제를 제기하고 있어, 이것이 해결되지 않은 핵심 과제라는 주장은 타당합니다.

### Gap B — 다수의 고급 TTA 연구들이 라벨 없는 테스트 데이터에만 의존한다는 핵심 가정을 위반하고 외부 정보에 의존하는 경향을 보입니다. 'TEMPO'(
- **타입**: recurring-limitation
- **설명**: 다수의 고급 TTA 연구들이 라벨 없는 테스트 데이터에만 의존한다는 핵심 가정을 위반하고 외부 정보에 의존하는 경향을 보입니다. 'TEMPO'(arxiv:2604.19295)는 "라벨링된 데이터셋에서의 주기적인 비평가 재보정"을 요구하며, 'CAL-GRPO'(arxiv:2604.17912)는 "강력한 검증기 피드백(hard verifier feedback)"을 사용합니다. 또 다른 연구(arxiv:2604.18107) 역시 "지연된 피드백(delayed feedback)"을 활용합니다. 이는 순수한 비지도 적응의 한계를 드러내며, 현실적인 배포 시나리오를 제약하는 공통된 한계입니다.
- **근거 논문**: P-2604.19295, P-2604.17912, P-2604.18107
- **Skeptic 검토**: ✓ 통과 — 복잡한 추론 작업을 다루는 최신 연구들이 라벨, 검증기 등 외부 감독에 의존하는 것은 사실이며, 이는 완전한 비지도(unsupervised) 패러다임 내에서 안정적인 성능 확보가 여전히 어렵다는 것을 시사하여 유효한 갭입니다.

### Gap D — 'AdaExplore'(arxiv:2604.16625) 연구는 TTA를 커널 코드 생성이라는 매우 전문화되고 구조화된 도메인에 적용한 유일한 사
- **타입**: single-shot
- **설명**: 'AdaExplore'(arxiv:2604.16625) 연구는 TTA를 커널 코드 생성이라는 매우 전문화되고 구조화된 도메인에 적용한 유일한 사례입니다. 이 논문은 실행 피드백을 통해 반복적인 실패를 학습하고 재사용 가능한 유효성 규칙 메모리를 구축하는 독특한 접근법을 제시합니다. 하지만 이 클러스터의 다른 논문들은 일반적인 수학 문제 풀이나 Chain-of-Thought 추론에 집중하고 있어, 코드와 같은 정형 언어 생성에 TTA를 적용하는 연구는 후속 연구로 이어지지 않은 것으로 보입니다.
- **근거 논문**: P-2604.16625
- **Skeptic 검토**: ✓ 통과 — 제시된 논문 풀 내에서 TTA를 코드 생성과 같은 정형적(formal)이고 구조적인 도메인에 적용한 사례는 실제로 해당 논문이 유일하여, 이 분야의 탐구가 부족하다는 주장은 설득력이 있습니다.

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap C** — 현재 TTA 연구는 크게 두 갈래로 나뉩니다. 하나는 Vision-Language 모델(VLM)의 강건한 '분류' 성능 향상(VLM 테스트 시점 적응 클러스터)이고, 다른 하나는 대규모 언어 모델(LLM)의 복잡한 '추론' 능력 향상(추론 모델의 테스트 시점 훈련 클러스터)입니다. VLM 적응 연구들은 주로 분류 정확도에 초점을 맞추는 반면, LLM 적응 연구는 텍스트 기반의 추론 과정 자체를 개선합니다. 이 두 영역을 통합하여, 시각과 언어 정보 모두에서 발생하는 분포 변화에 동적으로 적응하며 복잡한 '멀티모달 추론'을 수행하는 TTA 연구는 부족합니다. · 거부 사유: 다른 클러스터에서 이미 다룸. 'VLM 테스트 시점 적응' 클러스터의 'PDF'(arxiv:2604.18107) 논문은 'Vision-Language-Action' 모델을 위한 테스트 시점 적응을 다루며, 이는 순차적 의사결정 환경에서 멀티모달 추론에 TTA를 적용한 사례에 해당하여 제안된 갭을 이미 해결하고 있습니다.
- **Gap E** — TTA 연구는 두 가지 상반된 패러다임으로 나뉩니다. 한쪽은 모델 파라미터를 직접 업데이트하는 '화이트박스' 접근법('추론 모델의 테스트 시점 훈련' 클러스터)이며, 다른 한쪽은 API를 통해서만 모델에 접근 가능한 '블랙박스' 접근법('효율적/블랙박스 적응' 클러스터)입니다. 'BETA'(arxiv:2604.15609)는 경량 화이트박스 모델을 사용해 블랙박스 모델을 모사하는 접근을 하지만, 두 패러다임 사이의 넓은 회색 지대, 즉 제한된 그래디언트나 신뢰도 점수 등 부분적인 정보만 제공되는 '그레이박스(grey-box)' 시나리오에 대한 연구는 거의 없습니다. · 거부 사유: 다른 클러스

</details>

## 3. 연구 제안 (Proposer)

### 제안 1 — STAB-TTA
**가설**: 테스트 시점 적응의 불안정성은 자기 생성 보상 신호의 표류(drift) 때문이므로, 모델의 내부 표현 일관성을 정규화하면 성능 저하 없이 안정적인 적응이 가능하다.
**메우는 갭**: A
**접근**: 기존 엔트로피 최소화와 같은 출력 기반 최적화에 더해, 소스 도메인이나 초기 테스트 샘플에서 추출한 앵커 표현을 기준으로 내부 활성화의 일관성을 유지하는 정규화 항을 도입합니다. 모델이 앵커 표현 공간에서 크게 벗어나는 것을 방지함으로써, 치명적인 망각이나 성능 붕괴로 이어지는 불안정한 업데이트를 억제합니다. 이 방법은 EEG 데이터와 같이 기존 TTA가 불안정한 성능을 보이는 벤치마크에서 평가될 것입니다.
**Baselines**: TENT, TPT, NeuroAdapt-Bench, ImageNet-C
**예상 기여**: 분포 변화 환경에서 TTA의 안정성을 명백히 개선하고 성능 저하를 방지하는 새로운 정규화 기법을 제안합니다. 이를 통해 실제 배포 환경에서 더 신뢰성 높은 TTA 프레임워크를 제공할 수 있습니다.
**참고**: P-2604.16926, P-2604.19295, P-2604.15609

### 제안 2 — VETO-RL
**가설**: 강력한 검증기(verifier)가 제공하는 명시적 피드백은 모델이 생성한 여러 추론 경로 간의 상호 일관성 점수로 대체될 수 있으며, 이를 통해 외부 감독 없이도 테스트 시점 적응이 가능하다.
**메우는 갭**: B
**접근**: 외부 검증기 대신, 모델이 동일한 문제에 대해 생성한 여러 Chain-of-Thought 경로들을 비교하는 자체 검증 메커니즘을 개발합니다. 다수의 추론 경로가 동일한 최종 답안으로 수렴하는지, 혹은 단일 경로 내에 논리적 모순이 없는지를 측정하여 내부 일관성 점수를 생성합니다. 이 점수를 강화학습의 보상 신호로 사용하여, 외부 피드백 없이도 모델이 스스로 추론 과정을 개선하도록 유도합니다.
**Baselines**: CAL-GRPO, TEMPO, AIME 2024
**예상 기여**: 비용이 많이 들고 현실적으로 구하기 어려운 외부 검증기에 대한 의존성을 제거한 실용적인 완전 비지도 TTA 방법을 제안합니다. 이는 복잡한 추론 LLM의 배포 가능성을 크게 향상시킬 것입니다.
**참고**: P-2604.17912, P-2604.19295, P-2604.18107

### 제안 3 — FORMAL-ADAPT
**가설**: 실행 실패 피드백을 통해 재사용 가능한 유효성 규칙 메모리를 구축하는 'AdaExplore'의 접근법은 커널 코드 생성을 넘어 일반적인 형식 증명 및 기호 논리 추론 문제로 일반화될 수 있다.
**메우는 갭**: D
**접근**: Dafny와 같은 형식 검증기를 실행 피드백의 원천으로 활용하여 'AdaExplore' 프레임워크를 일반화합니다. 에이전트가 생성한 논리적 증명이나 코드가 검증에 실패할 때마다, 실패 원인을 분석하여 '잘못된 추론 패턴' 또는 '제약 조건 위반'과 같은 규칙을 학습하고 메모리에 축적합니다. 이 메모리는 후속 생성 과정에서 제약 조건으로 작용하여, 점진적으로 더 정확하고 효율적인 결과물을 생성하도록 유도합니다.
**Baselines**: AdaExplore, NL2VC-60, Dafny verifier
**예상 기여**: 실패 기반 TTA의 적용 범위를 특정 코딩 도메인에서 검증 가능한 추론이 필요한 광범위한 형식적 과제로 확장합니다. 이는 신경망 기반 생성 모델과 기호적 검증 시스템 사이의 간극을 메우는 중요한 다리가 될 것입니다.
**참고**: P-2604.16625, P-2604.22601

### 제안 4 — RHYTHM-TTA
**가설**: 단일 적응 전략을 고수하는 대신 테스트 데이터 분포의 통계적 변화를 감지하여 적응(adaptation)과 고정(fixation) 모드를 동적으로 전환하면 TTA의 전반적인 안정성을 높일 수 있다.
**메우는 갭**: A
**접근**: 모델 예측의 신뢰도 분포나 특징 공간의 통계량을 모니터링하는 경량 온라인 변화점 탐지 메커니즘을 구현합니다. 급격한 분포 변화가 감지되면 시스템은 '적응 모드'로 전환하여 모델 파라미터를 업데이트하고, 분포가 안정화되면 '고정 모드'로 전환하여 과적합과 표류를 방지합니다. 이는 지속적이지만 노이즈가 많은 업데이트로 인한 성능 붕괴를 막고, 비정상(non-stationary) 환경에서 모델의 강건성을 확보합니다.
**Baselines**: DualTTA, TENT, NeuroAdapt-Bench, ImageNet-C
**예상 기여**: '언제' 적응할지를 지능적으로 결정하는 메타-알고리즘을 통해 TTA의 핵심적인 불안정성 문제를 해결합니다. 이는 변화가 잦은 실제 환경에서 TTA의 신뢰도를 높이는 실용적인 제어 계층을 제공합니다.
**참고**: P-2604.17542, P-2604.16926, P-2604.19295

### 제안 5 — SELF-ALIGN
**가설**: 사전 훈련된 Vision-Language Model의 내재된 멀티모달 정렬(multimodal alignment) 자체를 내부 교정 신호로 활용하면, 외부 라벨이나 피드백 없이 순수 비지도 방식으로 테스트 시점 적응을 수행할 수 있다.
**메우는 갭**: B
**접근**: 테스트 이미지가 주어지면 VLM의 언어 모델 부분을 사용하여 해당 이미지에 대한 캡션을 생성합니다. 그 다음, 원본 이미지 임베딩과 생성된 캡션의 텍스트 임베딩 간의 코사인 유사도를 측정하여 '자체 일관성 점수'를 계산합니다. 이 점수가 높은 신뢰도 샘플에 대해 멀티모달 정렬을 최대화하는 방향으로 모델을 적응시켜, 외부 정보 없이 모델 스스로의 이해를 감독 신호로 활용합니다.
**Baselines**: CLIP, Ramen, PTA
**예상 기여**: 모델의 고유한 구조를 적응에 활용하는 완전한 제로-리소스 TTA 방법을 제시합니다. 이는 추가적인 데이터나 라벨을 사용할 수 없는 현실적인 배포 시나리오에 매우 실용적인 해결책이 될 것입니다.
**참고**: P-2604.19295, P-2604.21728, P-2604.21360

## 4. 참고문헌 (메타DB 기반)

### 클러스터 1 — VLM 테스트 시점 적응 (4)
- [P-2604.21728] Ramen: Robust Test-Time Adaptation of Vision-Language Models with Active Sample Selection, Wenxuan Bao, Yanjun Zhao, Xiyuan Yang et al., arXiv 2026 · http://arxiv.org/abs/2604.21728v1
- [P-2604.21360] Prototype-Based Test-Time Adaptation of Vision-Language Models, Zhaohong Huang, Yuxin Zhang, Wenjing Liu et al., arXiv 2026 · http://arxiv.org/abs/2604.21360v1
- [P-2604.19093] Multi-modal Test-time Adaptation via Adaptive Probabilistic Gaussian Calibration, Jinglin Xu, Yi Li, Chuxiong Sun et al., arXiv 2026 · http://arxiv.org/abs/2604.19093v1
- [P-2604.18107] Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models, Zehua Zang, Xi Wang, Fuchun Sun et al., arXiv 2026 · http://arxiv.org/abs/2604.18107v1

### 클러스터 2 — 분포 변화 대응 강건성 (4)
- [P-2604.21772] Back to Source: Open-Set Continual Test-Time Adaptation via Domain Compensation, Yingkai Yang, Chaoqi Chen, Hui Huang, arXiv 2026 · http://arxiv.org/abs/2604.21772v1
- [P-2604.15756] TTL: Test-time Textual Learning for OOD Detection with Pretrained Vision-Language Models, Jinlun Ye, Jiang Liao, Runhe Lai et al., arXiv 2026 · http://arxiv.org/abs/2604.15756v1
- [P-2604.17542] Dual Strategies for Test-Time Adaptation, Nam Nguyen Phuong, Duc Nguyen The Minh, Phi Le Nguyen et al., arXiv 2026 · http://arxiv.org/abs/2604.17542v1
- [P-2604.15494] ProtoTTA: Prototype-Guided Test-Time Adaptation, Mohammad Mahdi Abootorabi, Parvin Mousavi, Purang Abolmaesumi et al., arXiv 2026 · http://arxiv.org/abs/2604.15494v1

### 클러스터 3 — 추론 모델의 테스트 시점 훈련 (4)
- [P-2604.19295] TEMPO: Scaling Test-time Training for Large Reasoning Models, Qingyang Zhang, Xinke Kong, Haitao Wu et al., arXiv 2026 · http://arxiv.org/abs/2604.19295v1 · also_in: hf
- [P-2604.20915] Absorber LLM: Harnessing Causal Synchronization for Test-Time Training, Zhixin Zhang, Shabo Zhang, Chengcan Wu et al., arXiv 2026 · http://arxiv.org/abs/2604.20915v1
- [P-2604.16625] AdaExplore: Failure-Driven Adaptation and Diversity-Preserving Search for Efficient Kernel Generation, Weihua Du, Jingming Zhuo, Yixin Dong et al., arXiv 2026 · http://arxiv.org/abs/2604.16625v1
- [P-2604.17912] Learning to Correct: Calibrated Reinforcement Learning for Multi-Attempt Chain-of-Thought, Muhammed Emrullah Ildiz, Halil Alperen Gozeten, Ege Onur Taga et al., arXiv 2026 · http://arxiv.org/abs/2604.17912v1

### 클러스터 4 — 의료 영상 분석 적용 (2)
- [P-2604.16926] Test-Time Adaptation for EEG Foundation Models: A Systematic Study under Real-World Distribution Shifts, Gabriel Jason Lee, Jathurshan Pradeepkumar, Jimeng Sun, arXiv 2026 · http://arxiv.org/abs/2604.16926v1 · also_in: hf
- [P-2604.17451] SegTTA: Training-Free Test-Time Augmentation for Zero-Shot Medical Imaging Segmentation, Yihong Yao, Chunlei Li, Canxuan Gang et al., arXiv 2026 · http://arxiv.org/abs/2604.17451v1

### 클러스터 5 — 효율적/블랙박스 적응 (2)
- [P-2604.15609] Adapting in the Dark: Efficient and Stable Test-Time Adaptation for Black-Box Models, Yunbei Zhang, Shuaicheng Niu, Chengyi Cai et al., arXiv 2026 · http://arxiv.org/abs/2604.15609v1
- [P-2604.17337] AutoSearch: Adaptive Search Depth for Efficient Agentic RAG via Reinforcement Learning, Jingbo Sun, Wenyue Chong, Songjun Tu et al., arXiv 2026 · http://arxiv.org/abs/2604.17337v1

### 기타 (클러스터 미분류) (184)
- [P-2604.22601] From Natural Language to Verified Code: Toward AI Assisted Problem-to-Code Generation with Dafny-Based Formal Verification, Md Erfan, Md Kamal Hossain Chowdhury, Ahmed Ryan et al., arXiv 2026 · http://arxiv.org/abs/2604.22601v1
- [P-2604.22209] UniSonate: A Unified Model for Speech, Music, and Sound Effect Generation with Text Instructions, Chunyu Qiang, Xiaopeng Wang, Kang Yin et al., arXiv 2026 · http://arxiv.org/abs/2604.22209v1
- [P-2604.22190] From Global to Local: Rethinking CLIP Feature Aggregation for Person Re-Identification, Aotian Zheng, Winston Sun, Bahaa Alattar et al., arXiv 2026 · http://arxiv.org/abs/2604.22190v1
- [P-2604.22639] Adversarial Malware Generation in Linux ELF Binaries via Semantic-Preserving Transformations, Lukáš Hrdonka, Martin Jureček, arXiv 2026 · http://arxiv.org/abs/2604.22639v1
- [P-2604.22569] Adversarial Co-Evolution of Malware and Detection Models: A Bilevel Optimization Perspective, Olha Jurečková, Martin Jureček, Matouš Kozák et al., arXiv 2026 · http://arxiv.org/abs/2604.22569v1
- [P-2604.22170] Sharpness-Aware Poisoning: Enhancing Transferability of Injective Attacks on Recommender Systems, Junsong Xie, Yonghui Yang, Pengyang Shao et al., arXiv 2026 · http://arxiv.org/abs/2604.22170v1
- [P-2604.22158] Near-Optimal Regret for the Safe Learning-based Control of the Constrained Linear Quadratic Regulator, Spencer Hutchinson, Nanfei Jiang, Mahnoosh Alizadeh, arXiv 2026 · http://arxiv.org/abs/2604.22158v1
- [P-2604.22606] Dharma, Data and Deception: An LLM-Powered Rhetorical Analysis of Cow-Urine Health Claims on YouTube, Sheza Munir, Ratna Kandala, Anamta Khan et al., arXiv 2026 · http://arxiv.org/abs/2604.22606v1
- [P-2604.22739] Inter-Stance: A Dyadic Multimodal Corpus for Conversational Stance Analysis, Xiang Zhang, Xiaotian Li, Taoyue Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.22739v1
- [P-2604.22552] Transferable Physical-World Adversarial Patches Against Pedestrian Detection Models, Shihui Yan, Ziqi Zhou, Yufei Song et al., arXiv 2026 · http://arxiv.org/abs/2604.22552v1
- [P-2604.22310] Revisiting Geometric Obfuscation with Dual Convergent Lines for Privacy-Preserving Image Queries in Visual Localization, Jeonggon Kim, Heejoon Moon, Je Hyeong Hong, arXiv 2026 · http://arxiv.org/abs/2604.22310v1
- [P-2604.22220] Breaking Watermarks in the Frequency Domain: A Modulated Diffusion Attack Framework, Chunpeng Wang, Binyan Qu, Xiaoyu Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.22220v1
- [P-2604.21860] Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in Large Language Models, Naheed Rayhan, Sohely Jahan, arXiv 2026 · http://arxiv.org/abs/2604.21860v1
- [P-2604.21748] StructMem: Structured Memory for Long-Horizon Behavior in LLMs, Buqiang Xu, Yijun Chen, Jizhan Fang et al., arXiv 2026 · http://arxiv.org/abs/2604.21748v1
- [P-2604.21700] Stealthy Backdoor Attacks against LLMs Based on Natural Style Triggers, Jiali Wei, Ming Fan, Guoheng Sun et al., arXiv 2026 · http://arxiv.org/abs/2604.21700v1
- [P-2604.21529] Architectures for Robust Self-Organizing Energy Systems under Information and Control Constraints, Emilie Frost, Astrid Nieße, arXiv 2026 · http://arxiv.org/abs/2604.21529v1
- [P-2604.21515] Satisfying Rationality Postulates of Structured Argumentation Through Deductive Support -- Technical Report, Marcos Cramer, Tom Friese, arXiv 2026 · http://arxiv.org/abs/2604.21515v1
- [P-2604.21416] CSC: Turning the Adversary's Poison against Itself, Yuchen Shi, Xin Guo, Huajie Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.21416v1
- [P-2604.21310] Adversarial Evasion in Non-Stationary Malware Detection: Minimizing Drift Signals through Similarity-Constrained Perturbations, Pawan Acharya, Lan Zhang, arXiv 2026 · http://arxiv.org/abs/2604.21310v1
- [P-2604.21798] An effective variant of the Hartigan $k$-means algorithm, François Clément, Stefan Steinerberger, arXiv 2026 · http://arxiv.org/abs/2604.21798v1
- [P-2604.21623] A-THENA: Early Intrusion Detection for IoT with Time-Aware Hybrid Encoding and Network-Specific Augmentation, Ioannis Panopoulos, Maria Lamprini A. Bartsioka, Sokratis Nikolaidis et al., arXiv 2026 · http://arxiv.org/abs/2604.21623v1
- [P-2604.21197] Toward Efficient Membership Inference Attacks against Federated Large Language Models: A Projection Residual Approach, Guilin Deng, Silong Chen, Yuchuan Luo et al., arXiv 2026 · http://arxiv.org/abs/2604.21197v1
- [P-2604.21916] MathDuels: Evaluating LLMs as Problem Posers and Solvers, Zhiqiu Xu, Shibo Jin, Shreya Arya et al., arXiv 2026 · http://arxiv.org/abs/2604.21916v1
- [P-2604.21767] Misinformation Span Detection in Videos via Audio Transcripts, Breno Matos, Rennan C. Lima, Savvas Zannettou et al., arXiv 2026 · http://arxiv.org/abs/2604.21767v1
- [P-2604.21564] Measuring Opinion Bias and Sycophancy via LLM-based Coercion, Rodrigo Nogueira, Giovana Kerche Bonás, Thales Sales Almeida et al., arXiv 2026 · http://arxiv.org/abs/2604.21564v1
- [P-2604.21627] DCMorph: Face Morphing via Dual-Stream Cross-Attention Diffusion, Tahar Chettaoui, Eduarda Caldeira, Guray Ozgur et al., arXiv 2026 · http://arxiv.org/abs/2604.21627v1
- [P-2604.21519] Gmd: Gaussian mixture descriptor for pair matching of 3D fragments, Meijun Xiong, Zhenguo Shi, Xinyu Zhou et al., arXiv 2026 · http://arxiv.org/abs/2604.21519v1
- [P-2604.21311] an interpretable vision transformer framework for automated brain tumor classification, Chinedu Emmanuel Mbonu, Tochukwu Sunday Belonwu, Okwuchukwu Ejike Chukwuogo et al., arXiv 2026 · http://arxiv.org/abs/2604.21311v1
- [P-2604.21740] A Case Study in Recovery of Drones using Discrete-Event Systems, Liam P. Burns, Dayse M. Cavalcanti, Felipe G. Cabral et al., arXiv 2026 · http://arxiv.org/abs/2604.21740v1
- [P-2604.22117] PermaFrost-Attack: Stealth Pretraining Seeding(SPS) for planting Logic Landmines During LLM Training, Harsh Kumar, Rahul Maity, Tanmay Joshi et al., arXiv 2026 · http://arxiv.org/abs/2604.22117v1
- [P-2604.22084] Generating Synthetic Malware Samples Using Generative AI, Tiffany Bao, Kylie Trousil, Quang Duy Tran et al., arXiv 2026 · http://arxiv.org/abs/2604.22084v1
- [P-2604.22081] Insect-inspired modular architectures as inductive biases for reinforcement learning, Anne E. Staples, arXiv 2026 · http://arxiv.org/abs/2604.22081v1
- [P-2604.22076] PrivUn: Unveiling Latent Ripple Effects and Shallow Forgetting in Privacy Unlearning, Xiaoyi Chen, Haoyuan Wang, Siyuan Tang et al., arXiv 2026 · http://arxiv.org/abs/2604.22076v1
- [P-2604.22118] Robust Camera-to-Mocap Calibration and Verification for Large-Scale Multi-Camera Data Capture, Tianyi Liu, Christopher Twigg, Patrick Grady et al., arXiv 2026 · http://arxiv.org/abs/2604.22118v1
- [P-2604.21159] Adaptive Instruction Composition for Automated LLM Red-Teaming, Jesse Zymet, Andy Luo, Swapnil Shinde et al., arXiv 2026 · http://arxiv.org/abs/2604.21159v1
- [P-2604.21131] Cross-Session Threats in AI Agents: Benchmark, Evaluation, and Algorithms, Ari Azarafrooz, arXiv 2026 · http://arxiv.org/abs/2604.21131v1
- [P-2604.20994] Breaking MCP with Function Hijacking Attacks: Novel Threats for Function Calling and Agentic Models, Yannis Belkhiter, Giulio Zizzo, Sergio Maffeis et al., arXiv 2026 · http://arxiv.org/abs/2604.20994v1
- [P-2604.20833] AVISE: Framework for Evaluating the Security of AI Systems, Mikko Lempinen, Joni Kemppainen, Niklas Raesalmi, arXiv 2026 · http://arxiv.org/abs/2604.20833v1
- [P-2604.20806] OMIBench: Benchmarking Olympiad-Level Multi-Image Reasoning in Large Vision-Language Model, Qiguang Chen, Chengyu Luan, Jiajun Wu et al., arXiv 2026 · http://arxiv.org/abs/2604.20806v1
- [P-2604.20771] DAIRE: A lightweight AI model for real-time detection of Controller Area Network attacks in the Internet of Vehicles, Shahid Alam, Amina Jameel, Zahida Parveen et al., arXiv 2026 · http://arxiv.org/abs/2604.20771v1
- [P-2604.20665] The Expense of Seeing: Attaining Trustworthy Multimodal Reasoning Within the Monolithic Paradigm, Karan Goyal, Dikshant Kukreja, arXiv 2026 · http://arxiv.org/abs/2604.20665v1
- [P-2604.20606] Beyond ZOH: Advanced Discretization Strategies for Vision Mamba, Fady Ibrahim, Guangjun Liu, Guanghui Wang, arXiv 2026 · http://arxiv.org/abs/2604.20606v1
- [P-2604.20932] Adaptive Defense Orchestration for RAG: A Sentinel-Strategist Architecture against Multi-Vector Attacks, Pranav Pallerla, Wilson Naik Bhukya, Bharath Vemula et al., arXiv 2026 · http://arxiv.org/abs/2604.20932v1
- [P-2604.20930] SafeRedirect: Defeating Internal Safety Collapse via Task-Completion Redirection in Frontier LLMs, Chao Pan, Yu Wu, Xin Yao, arXiv 2026 · http://arxiv.org/abs/2604.20930v1
- [P-2604.20255] uLEAD-TabPFN: Uncertainty-aware Dependency-based Anomaly Detection with TabPFN, Sha Lu, Jixue Liu, Stefan Peters et al., arXiv 2026 · http://arxiv.org/abs/2604.20255v1
- [P-2604.20229] Enhancing Speaker Verification with Whispered Speech via Post-Processing, Magdalena Gołębiowska, Piotr Syga, arXiv 2026 · http://arxiv.org/abs/2604.20229v1
- [P-2604.20211] Towards Secure Logging: Characterizing and Benchmarking Logging Code Security Issues with LLMs, He Yang Yuan, Xin Wang, Kundi Yao et al., arXiv 2026 · http://arxiv.org/abs/2604.20211v1
- [P-2604.20158] Stateless Decision Memory for Enterprise AI Agents, Vasundra Srinivasan, arXiv 2026 · http://arxiv.org/abs/2604.20158v1
- [P-2604.20134] AgentSOC: A Multi-Layer Agentic AI Framework for Security Operations Automation, Joyjit Roy, Samaresh Kumar Singh, arXiv 2026 · http://arxiv.org/abs/2604.20134v1
- [P-2604.20945] Breaking Bad: Interpretability-Based Safety Audits of State-of-the-Art LLMs, Krishiv Agarwal, Ramneet Kaur, Colin Samplawski et al., arXiv 2026 · http://arxiv.org/abs/2604.20945v1
- [P-2604.20704] Auto-ART: Structured Literature Synthesis and Automated Adversarial Robustness Testing, Abhijit Talluri, arXiv 2026 · http://arxiv.org/abs/2604.20704v1
- [P-2604.20495] Towards Certified Malware Detection: Provable Guarantees Against Evasion Attacks, Nandakrishna Giri, Asmitha K. A., Serena Nicolazzo et al., arXiv 2026 · http://arxiv.org/abs/2604.20495v1
- [P-2604.20483] Forecasting Individual NetFlows using a Predictive Masked Graph Autoencoder, Georgios Anyfantis, Pere Barlet-Ros, arXiv 2026 · http://arxiv.org/abs/2604.20483v2
- [P-2604.20934] SDNGuardStack: An Explainable Ensemble Learning Framework for High-Accuracy Intrusion Detection in Software-Defined Networks, Ashikuzzaman, Md. Saifuzzaman Abhi, Mahabubur Rahman et al., arXiv 2026 · http://arxiv.org/abs/2604.20934v1
- [P-2604.20572] Ask Only When Needed: Proactive Retrieval from Memory and Skills for Experience-Driven Lifelong Agents, Yuxuan Cai, Jie Zhou, Qin Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.20572v1
- [P-2604.21041] Projected Gradient Unlearning for Text-to-Image Diffusion Models: Defending Against Concept Revival Attacks, Aljalila Aladawi, Mohammed Talha Alam, Fakhri Karray, arXiv 2026 · http://arxiv.org/abs/2604.21041v1
- [P-2604.20585] On the Impact of Face Segmentation-Based Background Removal on Recognition and Morphing Attack Detection, Eduarda Caldeira, Guray Ozgur, Fadi Boutros et al., arXiv 2026 · http://arxiv.org/abs/2604.20585v1
- [P-2604.20291] Efficient INT8 Single-Image Super-Resolution via Deployment-Aware Quantization and Teacher-Guided Training, Pham Phuong Nam Nguyen, Nam Tien Le, Thi Kim Trang Vo et al., arXiv 2026 · http://arxiv.org/abs/2604.20291v1
- [P-2604.20712] Visual-Tactile Peg-in-Hole Assembly Learning from Peg-out-of-Hole Disassembly, Yongqiang Zhao, Xuyang Zhang, Zhuo Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.20712v1
- [P-2604.19550] LoopCTR: Unlocking the Loop Scaling Power for Click-Through Rate Prediction, Jiakai Tang, Runfeng Zhang, Weiqiu Wang et al., HF 2026 · https://huggingface.co/papers/2604.19550
- [P-2604.20011] Frictionless Love: Associations Between AI Companion Roles and Behavioral Addiction, Vibhor Agarwal, Ke Zhou, Edyta Paulina Bogucka et al., arXiv 2026 · http://arxiv.org/abs/2604.20011v1
- [P-2604.19998] What Makes a Good AI Review? Concern-Level Diagnostics for AI Peer Review, Ming Jin, arXiv 2026 · http://arxiv.org/abs/2604.19998v1
- [P-2604.19936] Generalization and Membership Inference Attack a Practical Perspective, Fateme Rahmani, Mahdi Jafari Siavoshani, Mohammad Hossein Rohban, arXiv 2026 · http://arxiv.org/abs/2604.19936v1
- [P-2604.19657] An AI Agent Execution Environment to Safeguard User Data, Robert Stanley, Avi Verma, Lillian Tsai et al., arXiv 2026 · http://arxiv.org/abs/2604.19657v1
- [P-2604.19653] A Dual Perspective on Synthetic Trajectory Generators: Utility Framework and Privacy Vulnerabilities, Aya Cherigui, Florent Guépin, Arnaud Legendre et al., arXiv 2026 · http://arxiv.org/abs/2604.19653v1
- [P-2604.19561] Detecting Data Contamination in Large Language Models, Juliusz Janicki, Savvas Chamezopoulos, Evangelos Kanoulas et al., arXiv 2026 · http://arxiv.org/abs/2604.19561v1
- [P-2604.19533] Cyber Defense Benchmark: Agentic Threat Hunting Evaluation for LLMs in SecOps, Alankrit Chona, Igor Kozlov, Ambuj Kumar, arXiv 2026 · http://arxiv.org/abs/2604.19533v3
- [P-2604.19354] Do Agents Dream of Root Shells? Partial-Credit Evaluation of LLM Agents in Capture The Flag Challenges, Ali Al-Kaswan, Maksim Plotnikov, Maxim Hájek et al., arXiv 2026 · http://arxiv.org/abs/2604.19354v1
- [P-2604.19131] Has Automated Essay Scoring Reached Sufficient Accuracy? Deriving Achievable QWK Ceilings from Classical Test Theory, Masaki Uto, arXiv 2026 · http://arxiv.org/abs/2604.19131v1
- [P-2604.19083] ProjLens: Unveiling the Role of Projectors in Multimodal Model Safety, Kun Wang, Cheng Qian, Miao Yu et al., arXiv 2026 · http://arxiv.org/abs/2604.19083v1
- [P-2604.20024] Replicable Bandits with UCB based Exploration, Rohan Deb, Udaya Ghai, Karan Singh et al., arXiv 2026 · http://arxiv.org/abs/2604.20024v1
- [P-2604.19993] Algorithm and Hardware Co-Design for Efficient Complex-Valued Uncertainty Estimation, Zehuan Zhang, Mark Chen, He Li et al., arXiv 2026 · http://arxiv.org/abs/2604.19993v1
- [P-2604.20907] Achieving the Kesten-Stigum bound in the non-uniform hypergraph stochastic block model, Manuel Fernandez, Ludovic Stephan, Yizhe Zhu, arXiv 2026 · http://arxiv.org/abs/2604.20907v1
- [P-2604.19526] Evaluating LLM-Generated Obfuscated XSS Payloads for Machine Learning-Based Detection, Divyesh Gabbireddy, Suman Saha, arXiv 2026 · http://arxiv.org/abs/2604.19526v1
- [P-2604.19399] Optimal Routing for Federated Learning over Dynamic Satellite Networks: Tractable or Not?, Yi Zhao, Di Yuan, Tao Deng et al., arXiv 2026 · http://arxiv.org/abs/2604.19399v1
- [P-2604.18970] Mechanistic Anomaly Detection via Functional Attribution, Hugo Lyons Keenan, Christopher Leckie, Sarah Erfani, arXiv 2026 · http://arxiv.org/abs/2604.18970v1
- [P-2604.19716] Discovering a Shared Logical Subspace: Steering LLM Logical Reasoning via Alignment of Natural-Language and Symbolic Views, Feihao Fang, My T. Thai, Yuanyuan Lei, arXiv 2026 · http://arxiv.org/abs/2604.19716v1
- [P-2604.19508] Bangla Key2Text: Text Generation from Keywords for a Low Resource Language, Tonmoy Talukder, G M Shahariar, arXiv 2026 · http://arxiv.org/abs/2604.19508v1
- [P-2604.19499] Rank-Turbulence Delta and Interpretable Approaches to Stylometric Delta Metrics, Dmitry Pronin, Evgeny Kazartsev, arXiv 2026 · http://arxiv.org/abs/2604.19499v2
- [P-2604.19274] HarDBench: A Benchmark for Draft-Based Co-Authoring Jailbreak Attacks for Safe Human-LLM Collaborative Writing, Euntae Kim, Soomin Han, Buru Chang, arXiv 2026 · http://arxiv.org/abs/2604.19274v1
- [P-2604.19124] Detoxification for LLM: From Dataset Itself, Wei Shao, Yihang Wang, Gaoyu Zhu et al., arXiv 2026 · http://arxiv.org/abs/2604.19124v1
- [P-2604.18976] STAR-Teaming: A Strategy-Response Multiplex Network Approach to Automated LLM Red Teaming, MinJae Jung, YongTaek Lim, Chaeyun Kim et al., arXiv 2026 · http://arxiv.org/abs/2604.18976v1
- [P-2604.20047] PASTA: A Patch-Agnostic Twofold-Stealthy Backdoor Attack on Vision Transformers, Dazhuang Liu, Yanqi Qiao, Rui Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.20047v1
- [P-2604.19570] RF-HiT: Rectified Flow Hierarchical Transformer for General Medical Image Segmentation, Ahmed Marouane Djouama, Abir Belaala, Abdellah Zakaria Sellam et al., arXiv 2026 · http://arxiv.org/abs/2604.19570v1
- [P-2604.19365] Detection of T-shirt Presentation Attacks in Face Recognition Systems, Mathias Ibsen, Loris Tim Ide, Christian Rathgeb et al., arXiv 2026 · http://arxiv.org/abs/2604.19365v1
- [P-2604.19350] Attend what matters: Leveraging vision foundational models for breast cancer classification using mammograms, Samyak Sanghvi, Piyush Miglani, Sarvesh Shashikumar et al., arXiv 2026 · http://arxiv.org/abs/2604.19350v1
- [P-2604.19522] GenerativeMPC: VLM-RAG-guided Whole-Body MPC with Virtual Impedance for Bimanual Mobile Manipulation, Marcelino Julio Fernando, Miguel Altamirano Cabrera, Jeffrin Sam et al., arXiv 2026 · http://arxiv.org/abs/2604.19522v1
- [P-2604.19469] Wrench-Aware Admittance Control for Unknown-Payload Manipulation, Hossein Gholampour, Logan E. Beaver, arXiv 2026 · http://arxiv.org/abs/2604.19469v1
- [P-2604.19059] AeroBridge-TTA: Test-Time Adaptive Language-Conditioned Control for UAVs, Lingxue Lyu, arXiv 2026 · http://arxiv.org/abs/2604.19059v1
- [P-2604.18907] Gradient-Based Program Synthesis with Neurally Interpreted Languages, Matthew V. Macfarlane, Clément Bonnet, Herke van Hoof et al., arXiv 2026 · http://arxiv.org/abs/2604.18907v1
- [P-2604.18874] How Adversarial Environments Mislead Agentic AI?, Zhonghao Zhan, Huichi Zhou, Zhenhao Li et al., arXiv 2026 · http://arxiv.org/abs/2604.18874v1
- [P-2604.18867] Hierarchically Robust Zero-shot Vision-language Models, Junhao Dong, Yifei Zhang, Hao Zhu et al., arXiv 2026 · http://arxiv.org/abs/2604.18867v1
- [P-2604.18860] Temporal UI State Inconsistency in Desktop GUI Agents: Formalizing and Defending Against TOCTOU Attacks on Computer-Use Agents, Wenpeng Xu, arXiv 2026 · http://arxiv.org/abs/2604.18860v1
- [P-2604.18779] Mango: Multi-Agent Web Navigation via Global-View Optimization, Weixi Tong, Yifeng Di, Tianyi Zhang, arXiv 2026 · http://arxiv.org/abs/2604.18779v1
- [P-2604.18756] Towards Understanding the Robustness of Sparse Autoencoders, Ahson Saiyed, Sabrina Sadiekh, Chirag Agarwal, arXiv 2026 · http://arxiv.org/abs/2604.18756v1
- [P-2604.18718] Towards Optimal Agentic Architectures for Offensive Security Tasks, Isaac David, Arthur Gervais, arXiv 2026 · http://arxiv.org/abs/2604.18718v1
- [P-2604.18487] Adversarial Humanities Benchmark: Results on Stylistic Robustness in Frontier Model Safety, Marcello Galisai, Susanna Cifani, Francesco Giarrusso et al., arXiv 2026 · http://arxiv.org/abs/2604.18487v1
- [P-2604.18179] Committed SAE-Feature Traces for Audited-Session Substitution Detection in Hosted LLMs, Ziyang Liu, arXiv 2026 · http://arxiv.org/abs/2604.18179v1
- [P-2604.18663] Beyond Explicit Refusals: Soft-Failure Attacks on Retrieval-Augmented Generation, Wentao Zhang, Yan Zhuang, ZhuHang Zheng et al., arXiv 2026 · http://arxiv.org/abs/2604.18663v1
- [P-2604.18660] Evaluating Answer Leakage Robustness of LLM Tutors against Adversarial Student Attacks, Jin Zhao, Marta Knežević, Tanja Käser, arXiv 2026 · http://arxiv.org/abs/2604.18660v1
- [P-2604.18050] The Topological Dual of a Dataset: A Logic-to-Topology Encoding for AlphaGeometry-Style Data, Anthony Bordg, arXiv 2026 · http://arxiv.org/abs/2604.18050v1
- [P-2604.17866] Latent Abstraction for Retrieval-Augmented Generation, Ha Lan N. T, Minh-Anh Nguyen, Dung D. Le, arXiv 2026 · http://arxiv.org/abs/2604.17866v1
- [P-2604.17805] Ranking Abuse via Strategic Pairwise Data Perturbations, Junyi Yao, Zihao Zheng, Jiayu Long, arXiv 2026 · http://arxiv.org/abs/2604.17805v1
- [P-2604.17803] Adversarial Arena: Crowdsourcing Data Generation through Interactive Competition, Prasoon Goyal, Sattvik Sahai, Michael Johnston et al., arXiv 2026 · http://arxiv.org/abs/2604.17803v1
- [P-2604.17677] Semantic Entanglement in Vector-Based Retrieval: A Formal Framework and Context-Conditioned Disentanglement Pipeline for Agentic RAG Systems, Nick Loghmani, arXiv 2026 · http://arxiv.org/abs/2604.17677v1
- [P-2604.17674] Towards Intelligent Legal Document Analysis: CNN-Driven Classification of Case Law Texts, Moinul Hossain, Sourav Rabi Das, Zikrul Shariar Ayon et al., arXiv 2026 · http://arxiv.org/abs/2604.17674v1
- [P-2604.18846] Trainability Beyond Linearity in Variational Quantum Objectives, Gordon Ma, Xiufan Li, arXiv 2026 · http://arxiv.org/abs/2604.18846v1
- [P-2604.18716] TrEEStealer: Stealing Decision Trees via Enclave Side Channels, Jonas Sander, Anja Rabich, Nick Mahling et al., arXiv 2026 · http://arxiv.org/abs/2604.18716v1
- [P-2604.18697] Beyond Indistinguishability: Measuring Extraction Risk in LLM APIs, Ruixuan Liu, David Evans, Li Xiong, arXiv 2026 · http://arxiv.org/abs/2604.18697v1
- [P-2604.18438] Scalable Physics-Informed Neural Differential Equations and Data-Driven Algorithms for HVAC Systems, Hanfeng Zhai, Hongtao Qiao, Hassan Mansour et al., arXiv 2026 · http://arxiv.org/abs/2604.18438v2
- [P-2604.18080] Dynamic Risk Assessment by Bayesian Attack Graphs and Process Mining, Francesco Vitale, Simone Guarino, Stefano Perone et al., arXiv 2026 · http://arxiv.org/abs/2604.18080v1
- [P-2604.18066] Enhancing Anomaly-Based Intrusion Detection Systems with Process Mining, Francesco Vitale, Francesco Grimaldi, Massimiliano Rak et al., arXiv 2026 · http://arxiv.org/abs/2604.18066v1
- [P-2604.18758] Syntax as a Rosetta Stone: Universal Dependencies for In-Context Coptic Translation, Abhishek Purushothama, Emma Thronson, Alexia Guo et al., arXiv 2026 · http://arxiv.org/abs/2604.18758v1
- [P-2604.18248] Beyond Pattern Matching: Seven Cross-Domain Techniques for Prompt Injection Detection, Thamilvendhan Munirathinam, arXiv 2026 · http://arxiv.org/abs/2604.18248v1
- [P-2604.17842] QuickScope: Certifying Hard Questions in Dynamic LLM Benchmarks, Taylor Lundy, Narun K. Raman, Kevin Leyton-Brown, arXiv 2026 · http://arxiv.org/abs/2604.17842v1
- [P-2604.18853] DDF2Pol: A Dual-Domain Feature Fusion Network for PolSAR Image Classification, Mohammed Q. Alkhatib, arXiv 2026 · http://arxiv.org/abs/2604.18853v1
- [P-2604.18562] AnchorSeg: Language Grounded Query Banks for Reasoning Segmentation, Rui Qian, Chuanhang Deng, Qiang Huang et al., arXiv 2026 · http://arxiv.org/abs/2604.18562v3
- [P-2604.18549] Advancing Vision Transformer with Enhanced Spatial Priors, Qihang Fan, Huaibo Huang, Mingrui Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.18549v1
- [P-2604.18537] MetaCloak-JPEG: JPEG-Robust Adversarial Perturbation for Preventing Unauthorized DreamBooth-Based Deepfake Generation, Tanjim Rahaman Fardin, S M Zunaid Alam, Mahadi Hasan Fahim et al., arXiv 2026 · http://arxiv.org/abs/2604.18537v1
- [P-2604.17961] DifFoundMAD: Foundation Models meet Differential Morphing Attack Detection, Lazaro J. Gonzalez-Soler, André Dörsch, Christian Rathgeb et al., arXiv 2026 · http://arxiv.org/abs/2604.17961v1
- [P-2604.18905] Task-Adaptive Admittance Control for Human-Quadrotor Cooperative Load Transportation with Dynamic Cable-Length Regulation, Shuai Li, Ton T. H. Duong, Damiano Zanotto, arXiv 2026 · http://arxiv.org/abs/2604.18905v1
- [P-2502.07408] Maximal Brain Damage Without Data or Optimization: Disrupting Neural Networks via Sign-Bit Flips, Ido Galil, Moshe Kimhi, Ran El-Yaniv, HF 2026 · https://huggingface.co/papers/2502.07408 · also_in: arxiv
- [P-2604.16254] ArtifactNet: Detecting AI-Generated Music via Forensic Residual Physics, Heewon Oh, HF 2026 · https://huggingface.co/papers/2604.16254
- [P-2604.14663] EdgeDetect: Importance-Aware Gradient Compression with Homomorphic Aggregation for Federated Intrusion Detection, Noor Islam S. Mohammad, HF 2026 · https://huggingface.co/papers/2604.14663
- [P-2604.17596] Terminal Wrench: A Dataset of 331 Reward-Hackable Environments and 3,632 Exploit Trajectories, Ivan Bercovich, Ivgeni Segal, Kexun Zhang et al., arXiv 2026 · http://arxiv.org/abs/2604.17596v1 · also_in: hf
- [P-2604.17562] SafeAgent: A Runtime Protection Architecture for Agentic Systems, Hailin Liu, Eugene Ilyushin, Jie Ni et al., arXiv 2026 · http://arxiv.org/abs/2604.17562v1
- [P-2604.17267] Rectification Difficulty and Optimal Sample Allocation in LLM-Augmented Surveys, Zikun Ye, Hema Yoganarasimhan, arXiv 2026 · http://arxiv.org/abs/2604.17267v1
- [P-2604.17175] RosettaSearch: Multi-Objective Inference-Time Search for Protein Sequence Design, Meghana Kshirsagar, Allen Nie, Ching-An Cheng et al., arXiv 2026 · http://arxiv.org/abs/2604.17175v1
- [P-2604.17627] SLO-Guard: Crash-Aware, Budget-Consistent Autotuning for SLO-Constrained LLM Serving, Christian Lysenstøen, arXiv 2026 · http://arxiv.org/abs/2604.17627v1
- [P-2604.17568] Diverse Dictionary Learning, Yujia Zheng, Zijian Li, Shunxing Fan et al., arXiv 2026 · http://arxiv.org/abs/2604.17568v1 · also_in: hf
- [P-2604.17384] Towards a Data-Parameter Correspondence for LLMs: A Preliminary Discussion, Ou Wu, arXiv 2026 · http://arxiv.org/abs/2604.17384v1
- [P-2604.17215] Continual Safety Alignment via Gradient-Based Sample Selection, Thong Bach, Dung Nguyen, Thao Minh Le et al., arXiv 2026 · http://arxiv.org/abs/2604.17215v1
- [P-2604.17297] CRISP: Compressing Redundancy in Chain-of-Thought via Intrinsic Saliency Pruning, Yangsong Lan, Hongliang Dai, Piji Li, arXiv 2026 · http://arxiv.org/abs/2604.17297v1
- [P-2604.17476] Privatar: Scalable Privacy-preserving Multi-user VR via Secure Offloading, Jianming Tong, Hanshen Xiao, Krishna Kumar Nair et al., arXiv 2026 · http://arxiv.org/abs/2604.17476v1
- [P-2604.17321] R-FLoRA: Residual-Statistic-Gated Low-Rank Adaptation for Single-Image Face Morphing Attack Detection, Raghavendra Ramachandra, arXiv 2026 · http://arxiv.org/abs/2604.17321v1
- [P-2604.17318] When Background Matters: Breaking Medical Vision Language Models by Transferable Attack, Akash Ghosh, Subhadip Baidya, Sriparna Saha et al., arXiv 2026 · http://arxiv.org/abs/2604.17318v1 · also_in: hf
- [P-2604.17287] Spectral Forensics of Diffusion Attention Graphs for Copy-Move Forgery Detection, H. M. Shadman Tabib, Tasriad Ahmed Tias, Nafis Tahmid, arXiv 2026 · http://arxiv.org/abs/2604.17287v1
- [P-2604.17410] Algorithmic Contiguity from Low-Degree Heuristic II: Predicting Detection-Recovery Gaps, Zhangsong Li, arXiv 2026 · http://arxiv.org/abs/2604.17410v1
- [P-2604.17125] CASCADE: A Cascaded Hybrid Defense Architecture for Prompt Injection Detection in MCP-Based Systems, İpek Abasıkeleş Turgut, Edip Gümüş, arXiv 2026 · http://arxiv.org/abs/2604.17125v1
- [P-2604.16966] Visual Inception: Compromising Long-term Planning in Agentic Recommenders via Multimodal Memory Poisoning, Jiachen Qian, arXiv 2026 · http://arxiv.org/abs/2604.16966v1
- [P-2604.16824] SafeDream: Safety World Model for Proactive Early Jailbreak Detection, Bo Yan, Weikai Lin, Yada Zhu et al., arXiv 2026 · http://arxiv.org/abs/2604.16824v1
- [P-2604.16812] Introspection Adapters: Training LLMs to Report Their Learned Behaviors, Keshav Shenoy, Li Yang, Abhay Sheshadri et al., arXiv 2026 · http://arxiv.org/abs/2604.16812v1
- [P-2604.16780] FairNVT: Improving Fairness via Noise Injection in Vision Transformers, Qiaoyue Tang, Sepidehsadat Hosseini, Mengyao Zhai et al., arXiv 2026 · http://arxiv.org/abs/2604.16780v1
- [P-2604.17158] Lightweight Cybersickness Detection based on User-Specific Eye and Head Tracking Data in Virtual Reality, Yijun Wang, Mihai Bâce, Maria Torres Vega, arXiv 2026 · http://arxiv.org/abs/2604.17158v1
- [P-2604.16995] SPS: Steering Probability Squeezing for Better Exploration in Reinforcement Learning for Large Language Models, Yifu Huo, Chenglong Wang, Ziming Zhu et al., arXiv 2026 · http://arxiv.org/abs/2604.16995v1
- [P-2604.17053] Jailbreaking Large Language Models with Morality Attacks, Ying Su, Mingen Zheng, Weili Diao et al., arXiv 2026 · http://arxiv.org/abs/2604.17053v1
- [P-2604.17163] PPEDCRF: Dynamic-CRF-Guided Selective Perturbation for Background-Based Location Privacy in Video Sequences, Bo Ma, Weiqi Yan, Jinsong Wu, arXiv 2026 · http://arxiv.org/abs/2604.17163v1
- [P-2604.17052] OASIS: On-Demand Hierarchical Event Memory for Streaming Video Reasoning, Zhijia Liang, Jiaming Li, Weikai Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.17052v1
- [P-2604.17041] SIF: Semantically In-Distribution Fingerprints for Large Vision-Language Models, Yifei Zhao, Qian Lou, Mengxin Zheng, arXiv 2026 · http://arxiv.org/abs/2604.17041v1
- [P-2604.16783] EdgeVTP: Exploration of Latency-efficient Trajectory Prediction for Edge-based Embedded Vision Applications, Seungjin Kim, Reza Jafarpourmarzouni, Christopher Neff et al., arXiv 2026 · http://arxiv.org/abs/2604.16783v1
- [P-2604.16689] The Query Channel: Information-Theoretic Limits of Masking-Based Explanations, Erciyes Karakaya, Ozgur Ercetin, arXiv 2026 · http://arxiv.org/abs/2604.16689v1
- [P-2604.16116] The Relic Condition: When Published Scholarship Becomes Material for Its Own Replacement, Lin Deng, Chang-bo Liu, arXiv 2026 · http://arxiv.org/abs/2604.16116v1
- [P-2604.16575] Evaluating Temporal and Structural Anomaly Detection Paradigms for DDoS Traffic, Yasmin Souza Lima, Rodrigo Moreira, Larissa F. Rodrigues Moreira et al., arXiv 2026 · http://arxiv.org/abs/2604.16575v1
- [P-2604.16606] SafeLM: Unified Privacy-Aware Optimization for Trustworthy Federated Large Language Models, Noor Islam S. Mohammad, Uluğ Bayazıt, arXiv 2026 · http://arxiv.org/abs/2604.16606v1
- [P-2604.16087] The Harder Path: Last Iterate Convergence for Uncoupled Learning in Zero-Sum Games with Bandit Feedback, Côme Fiegel, Pierre Ménard, Tadashi Kozuno et al., arXiv 2026 · http://arxiv.org/abs/2604.16087v1
- [P-2604.16075] Towards Universal Convergence of Backward Error in Linear System Solvers, Michał Dereziński, Yuji Nakatsukasa, Elizaveta Rebrova, arXiv 2026 · http://arxiv.org/abs/2604.16075v1
- [P-2604.15821] Breaking the Training Barrier of Billion-Parameter Universal Machine Learning Interatomic Potentials, Yuanchang Zhou, Hongyu Wang, Yiming Du et al., arXiv 2026 · http://arxiv.org/abs/2604.15821v1
- [P-2604.15780] Pruning Unsafe Tickets: A Resource-Efficient Framework for Safer and More Robust LLMs, Wai Man Si, Mingjie Li, Michael Backes et al., arXiv 2026 · http://arxiv.org/abs/2604.15780v1
- [P-2604.15725] Reasoning-targeted Jailbreak Attacks on Large Reasoning Models via Semantic Triggers and Psychological Framing, Zehao Wang, Lanjun Wang, arXiv 2026 · http://arxiv.org/abs/2604.15725v1
- [P-2604.15718] NeuroLip: An Event-driven Spatiotemporal Learning Framework for Cross-Scene Lip-Motion-based Visual Speaker Recognition, Junguang Yao, Wenye Liu, Stjepan Picek et al., arXiv 2026 · http://arxiv.org/abs/2604.15718v1
- [P-2604.16037] Stochasticity in Tokenisation Improves Robustness, Sophie Steger, Rui Li, Sofiane Ennadir et al., arXiv 2026 · http://arxiv.org/abs/2604.16037v1
- [P-2604.16576] On the Robustness of LLM-Based Dense Retrievers: A Systematic Analysis of Generalizability and Stability, Yongkang Li, Panagiotis Eustratiadis, Yixing Fan et al., arXiv 2026 · http://arxiv.org/abs/2604.16576v1 · also_in: hf
- [P-2604.15789] A Systematic Study of Training-Free Methods for Trustworthy Large Language Models, Wai Man Si, Mingjie Li, Michael Backes et al., arXiv 2026 · http://arxiv.org/abs/2604.15789v1
- [P-2604.16548] A Survey on the Security of Long-Term Memory in LLM Agents: Toward Mnemonic Sovereignty, Zehao Lin, Chunyu Li, Kai Chen, arXiv 2026 · http://arxiv.org/abs/2604.16548v1
- [P-2604.15648] HyperGVL: Benchmarking and Improving Large Vision-Language Models in Hypergraph Understanding and Reasoning, Yanbin Wei, Chun Kang, Siwei Li et al., arXiv 2026 · http://arxiv.org/abs/2604.15648v1
- [P-2604.16231] Dental Panoramic Radiograph Analysis Using YOLO26 From Tooth Detection to Disease Diagnosis, Khawaja Azfar Asif, Rafaqat Alam Khan, arXiv 2026 · http://arxiv.org/abs/2604.16231v1
- [P-2604.16070] TableSeq: Unified Generation of Structure, Content, and Layout, Laziz Hamdi, Amine Tamasna, Pascal Boisson et al., arXiv 2026 · http://arxiv.org/abs/2604.16070v1
- [P-2604.15967] TwoHamsters: Benchmarking Multi-Concept Compositional Unsafety in Text-to-Image Models, Chaoshuo Zhang, Yibo Liang, Mengke Tian et al., arXiv 2026 · http://arxiv.org/abs/2604.15967v1
- [P-2604.15862] Splats in Splats++: Robust and Generalizable 3D Gaussian Splatting Steganography, Yijia Guo, Wenkai Huang, Tong Hu et al., arXiv 2026 · http://arxiv.org/abs/2604.15862v1
- [P-2604.15708] APC: Transferable and Efficient Adversarial Point Counterattack for Robust 3D Point Cloud Recognition, Geunyoung Jung, Soohong Kim, Inseok Kong et al., arXiv 2026 · http://arxiv.org/abs/2604.15708v1
- [P-2604.16021] Neurosymbolic Repo-level Code Localization, Xiufeng Xu, Xiufeng Wu, Zejun Zhang et al., arXiv 2026 · http://arxiv.org/abs/2604.16021v2
- [P-2604.15709] Bilevel Optimization of Agent Skills via Monte Carlo Tree Search, Chenyi Huang, Haoting Zhang, Jingxu Xu et al., arXiv 2026 · http://arxiv.org/abs/2604.15709v1
- [P-2604.16543] Conjunctive Prompt Attacks in Multi-Agent LLM Systems, Nokimul Hasan Arif, Qian Lou, Mengxin Zheng, arXiv 2026 · http://arxiv.org/abs/2604.16543v1
- [P-2509.25843] ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack, Yein Park, Jungwoo Park, Jaewoo Kang, HF 2026 · https://huggingface.co/papers/2509.25843 · also_in: arxiv
- [P-2604.15482] Harmonizing Multi-Objective LLM Unlearning via Unified Domain Representation and Bidirectional Logit Distillation, Yisheng Zhong, Sijia Liu, Zhuangdi Zhu, arXiv 2026 · http://arxiv.org/abs/2604.15482v1
- [P-2604.16532] Beyond Attack Success Rate: A Multi-Metric Evaluation of Adversarial Transferability in Medical Imaging Models, Emily Curl, Kofi Ampomah, Md Erfan et al., arXiv 2026 · http://arxiv.org/abs/2604.16532v1
- [P-2604.15415] HarmfulSkillBench: How Do Harmful Skills Weaponize Your Agents?, Yukun Jiang, Yage Zhang, Michael Backes et al., arXiv 2026 · http://arxiv.org/abs/2604.15415v1
- [P-2604.15063] No More Guessing: a Verifiable Gradient Inversion Attack in Federated Learning, Francesco Diana, Chuan Xu, André Nusser et al., arXiv 2026 · http://arxiv.org/abs/2604.15063v1
- [P-2604.15022] Route to Rome Attack: Directing LLM Routers to Expensive Models via Adversarial Suffix Optimization, Haochun Tang, Yuliang Yan, Jiahua Lu et al., arXiv 2026 · http://arxiv.org/abs/2604.15022v1
- [P-2604.15001] COEVO: Co-Evolutionary Framework for Joint Functional Correctness and PPA Optimization in LLM-Based RTL Generation, Heng Ping, Peiyu Zhang, Shixuan Li et al., arXiv 2026 · http://arxiv.org/abs/2604.15001v2
- [P-2604.14987] AI-Enabled Covert Channel Detection in RF Receiver Architectures, Abdelrahman Emad Abdelazim, Alan Rodrigo Diaz-Rizo, Hassan Aboushady et al., arXiv 2026 · http://arxiv.org/abs/2604.14987v1
- [P-2604.15242] Optimal last-iterate convergence in matrix games with bandit feedback using the log-barrier, Come Fiegel, Pierre Menard, Tadashi Kozuno et al., arXiv 2026 · http://arxiv.org/abs/2604.15242v1
- [P-2604.15115] FedIDM: Achieving Fast and Stable Convergence in Byzantine Federated Learning through Iterative Distribution Matching, He Yang, Dongyi Lv, Wei Xi et al., arXiv 2026 · http://arxiv.org/abs/2604.15115v1
- [P-2604.14957] MLDAS: Machine Learning Dynamic Algorithm Selection for Software-Defined Networking Security, Pablo Benlloch, Oscar Romero, Antonio Leon et al., arXiv 2026 · http://arxiv.org/abs/2604.14957v1

---

## 메타 / 디버그
- model: gemini-2.5-pro
- backend: gemini-pro-sdk
- matched_n: 200
- matched_total_before_cap: 1447
- window_days: 60
- tokens_in_uncached: 7034
- tokens_in_cached_read: 249092
- tokens_out: 5936
- usd_estimate: $0.1454
