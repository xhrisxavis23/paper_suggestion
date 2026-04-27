# Research Topic Suggestion — "sparse autoencoder"

생성: 2026-04-27T03:00:49.178460+00:00
DB 윈도우: 2026-02-26 ~ 2026-04-27 (60d)
모델: claude-sonnet-4-6
매칭 논문: 80건
확장 키워드: ['sparse autoencoder', 'SAE', 'sparse dictionary learning', 'mechanistic interpretability', 'superposition hypothesis', 'polysemantic neurons', 'monosemantic features', 'feature decomposition', 'activation sparsity', 'sparse coding', 'transcoder', 'dictionary features']

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — SAE 훈련·설계
- **설명**: SAE의 활성화 함수·정규화·원자성을 개선해 더 안정적이고 해석 가능한 특징을 학습하는 연구들. 스파시티-재구성 트레이드오프와 cross-seed 일관성 향상에 초점을 맞춘다.
- **빈도**: 4건
- **주차별**: 2 → 1 → 1 → 0
- **대표 논문**:
  - [P-2604.06495] Improving Robustness In Sparse Autoencoders via Masked Regularization — Vivek Narayanaswamy, Kowshik Thopalli, Bhavya Kailkhura et al., arXiv 2026
  - [P-2604.03436] MetaSAEs: Joint Training with a Decomposability Penalty Produces More Atomic Sparse Autoencoder Latents — Matthew Levinson, arXiv 2026
  - [P-2604.14925] Improving Sparse Autoencoder with Dynamic Attention — Dongsheng Wang, Jinsen Zhang, Dawei Su et al., arXiv 2026

### 클러스터 2 — LLM 특징 분석
- **설명**: SAE를 활용해 대형 언어 모델 내부의 불확실성·다국어·추론 특징을 추출·분석하는 연구들. 개념 표현 구조를 규명하고 개념 탐색 도구를 제공한다.
- **빈도**: 6건
- **주차별**: 3 → 2 → 0 → 1
- **대표 논문**:
  - [P-2604.19974] Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders — Het Patel, Tiejin Chen, Hua Wei et al., arXiv 2026
  - [P-2603.03031] Step-Level Sparse Autoencoder for Reasoning Process Interpretation — Xuan Yang, Jiayu Liu, Yuhang Lai et al., arXiv 2026
  - [P-2603.02908] SAE as a Crystal Ball: Interpretable Features Predict Cross-domain Transferability of LLMs without Training — Qi Zhang, Yifei Wang, Xiaohan Wang et al., arXiv 2026

### 클러스터 3 — 안전·정렬 적용
- **설명**: SAE 특징을 활용해 환각 탐지, 탈옥 방어, 보상 해킹 모니터링 등 LLM 안전·정렬 문제를 해결하는 연구들. 특징 수준 개입으로 위험 신호를 조기 탐지하거나 모델 안전성을 강화한다.
- **빈도**: 8건
- **주차별**: 2 → 3 → 3 → 0
- **대표 논문**:
  - [P-2604.16430] HalluSAE: Detecting Hallucinations in Large Language Models via Sparse Auto-Encoders — Boshui Chen, Zhaoxin Fan, Ke Wang et al., arXiv 2026
  - [P-2604.08846] Dictionary-Aligned Concept Control for Safeguarding Multimodal LLMs — Jinqi Luo, Jinyu Yang, Tal Neiman et al., arXiv 2026
  - [P-2604.18756] Towards Understanding the Robustness of Sparse Autoencoders — Ahson Saiyed, Sabrina Sadiekh, Chirag Agarwal, arXiv 2026

### 클러스터 4 — 비전·멀티모달
- **설명**: 비전 트랜스포머·비디오·멀티모달 모델에 SAE를 적용해 시각적·공간적 특징을 해석하고 편향을 완화하는 연구들. 텍스트 중심 해석 방법론을 시각 도메인으로 확장한다.
- **빈도**: 6건
- **주차별**: 3 → 1 → 2 → 0
- **대표 논문**:
  - [P-2604.03919] Interpreting Video Representations with Spatio-Temporal Sparse Autoencoders — Atahan Dokme, Sriram Vishwanath, arXiv 2026
  - [P-2604.05724] Beyond Semantics: Disentangling Information Scope in Sparse Autoencoders for CLIP — Yusung Ro, Jaehyun Choi, Junmo Kim, arXiv 2026
  - [P-2604.13304] Can Cross-Layer Transcoders Replace Vision Transformer Activations? An Interpretable Perspective on Vision — Gerasimos Chatzoudis, Konstantinos D. Polyzos, Zhuowei Li et al., arXiv 2026

### 클러스터 5 — 도메인 확장 응용
- **설명**: 정보 검색·생물 기초 모델·게임 AI 등 비전통 도메인에 SAE를 적용하는 연구들. SAE가 생성하는 해석 가능한 희소 표현을 언어 모델 너머의 과학·공학 분야에서 활용한다.
- **빈도**: 3건
- **주차별**: 1 → 1 → 0 → 1
- **대표 논문**:
  - [P-2604.21511] From Tokens to Concepts: Leveraging SAE for SPLADE — Yuxuan Zong, Mathias Vast, Basile Van Cooten et al., arXiv 2026
  - [P-2603.13277] Learning Retrieval Models with Sparse Autoencoders — Thibault Formal, Maxime Louis, Hervé Dejean et al., arXiv 2026
  - [P-2603.02952] Sparse autoencoders reveal organized biological knowledge but minimal regulatory logic in single-cell foundation models: a comparative atlas of Geneformer and scGPT — Ihor Kendiukhov, arXiv 2026

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap A — SAE 훈련·설계 클러스터는 더 원자적이고 안정적인 특징 학습을 '안전·정렬 응용의 기반'으로 동기화하지만 실제 안전 실험을 수행하지 않는다. 
- **타입**: between-clusters
- **설명**: SAE 훈련·설계 클러스터는 더 원자적이고 안정적인 특징 학습을 '안전·정렬 응용의 기반'으로 동기화하지만 실제 안전 실험을 수행하지 않는다. 반대로 안전·정렬 클러스터는 HalluSAE, CWAC, CRaFT 모두 개선되지 않은 표준 SAE를 그대로 사용한다. 더 원자적인 SAE 특징이 실제로 더 나은 할루시네이션 탐지나 탈옥 방어로 이어지는지는 어느 논문도 직접 검증하지 않는다.
- **근거 논문**: P-2604.03436, P-2604.16430, P-2604.12384, P-2604.01604
- **Skeptic 검토**: ✓ 통과 — arxiv:2604.18756이 L0 스파시티-방어 성능의 단조 관계를 보이지만, 이는 스파시티 수준 조정이며 MetaSAE-style '원자성(subspace blending 억제)' 개선이 안전 성능에 미치는 효과와는 별개다. 두 클러스터의 실증적 연결 부재는 메타만으로도 확인된다.

### Gap B — 비전·멀티모달 클러스터는 AVLLM에서 오디오 신호가 시각 표현에 구조적으로 억압된다는 'fundamental modality bias'를 발견
- **타입**: between-clusters
- **설명**: 비전·멀티모달 클러스터는 AVLLM에서 오디오 신호가 시각 표현에 구조적으로 억압된다는 'fundamental modality bias'를 발견했다(2604.02605). 그러나 안전·정렬 클러스터의 멀티모달 방어(DACO 2604.08846, SALLIE 2604.06247)는 텍스트·이미지 양태만 다루며 오디오 모달리티를 완전히 배제한다.
- **근거 논문**: P-2604.02605, P-2604.08846, P-2604.06247
- **Skeptic 검토**: ✓ 통과 — SALLIE(2604.06247)는 'token-level fusion pipelines'에, DACO(2604.08846)는 'caption-image stimuli'에 국한됨을 초록에서 명시한다. 2604.02605의 오디오 억압이 안전 취약점으로 연결되는 연구는 메타DB 내 전무하다.

### Gap C — arxiv:2603.05487만이 Vision-Language-Action(VLA) 모델에 mechanistic interpretability를
- **타입**: single-shot
- **설명**: arxiv:2603.05487만이 Vision-Language-Action(VLA) 모델에 mechanistic interpretability를 적용했다. VLA 내부 표현의 선형 관찰·제어 가능성을 π₀.₅와 OpenVLA에서 실증했으나, 구현 지능 도메인의 후속 연구 및 안전·정렬 클러스터와의 연결이 전무하다.
- **근거 논문**: P-2603.05487
- **Skeptic 검토**: ✓ 통과 — 2603.05487은 다섯 클러스터 어디에도 귀속되지 않는다. 도메인 확장 클러스터(체스 AI 2604.10158, 단세포 2603.01752 등) 역시 VLA 안전·정렬과 무관하다. 단발성 확인된다.

### Gap D — SAE 특징 기반 개입의 인스턴스 수준 일반화 실패가 여러 논문에서 반복적으로 보고된다. 2604.11467 전문가 인터뷰(N=8)에서 8/8 
- **타입**: recurring-limitation
- **설명**: SAE 특징 기반 개입의 인스턴스 수준 일반화 실패가 여러 논문에서 반복적으로 보고된다. 2604.11467 전문가 인터뷰(N=8)에서 8/8 참가자가 ripple effects와 제한된 일반화를 핵심 위험으로 지적했고, 2604.11061(Pando)은 모델이 오해를 유도할 때 SAE가 신뢰할 수 있는 이득을 제공하지 못함을 통제 실험으로 보였다.
- **근거 논문**: P-2604.11467, P-2604.11061, P-2604.06495
- **Skeptic 검토**: ✓ 통과 — LLM 특징 분석(2604.11061)과 안전·정렬(2604.11467) 두 클러스터에서 독립적으로 확인된 반복 한계다. 2604.06495(Masked Regularization)는 OOD 갭만 부분 완화하며 일반화 실패를 훈련 목표로 직접 해결한 논문은 메타DB 내 없다.

### Gap F — 안전·정렬 클러스터의 SAE 모니터링(2603.04069)은 토큰 생성 단계의 보상 해킹을 탐지하지만, 연속 잠재 추론 모델에서는 backdoo
- **타입**: between-clusters
- **설명**: 안전·정렬 클러스터의 SAE 모니터링(2603.04069)은 토큰 생성 단계의 보상 해킹을 탐지하지만, 연속 잠재 추론 모델에서는 backdoor 정보가 개별 벡터가 아닌 '집합적 궤적'에 인코딩된다. ThoughtSteer(2604.00770)는 이 구조가 'every token-level defense'를 우회함을 세 벤치마크에서 실증했다.
- **근거 논문**: P-2604.00770, P-2603.04069
- **Skeptic 검토**: ✓ 통과 — ThoughtSteer가 probe AUC≥0.999의 선형 분리 가능성을 확인했으나, 이는 궤적 수준 탐지가 필요하다는 의미이며 개별 활성화 벡터를 분해하는 SAE 방식의 구조적 한계를 오히려 확인한다. 메타DB 내 어떤 논문도 연속 추론 패러다임에서의 SAE 모니터링 재설계를 다루지 않는다.

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap E** — SAE 훈련·설계 클러스터의 개선 연구들(MetaSAEs, Weight Regularization)이 소형 모델(GPT-2 Large, Pythia-70M)에서만 완전히 검증되는 반면, 안전·정렬 응용은 Gemma-2-9B 이상의 대형 모델을 대상으로 한다는 스케일 갭. · 거부 사유: (c) trivial — MetaSAEs(arxiv:2604.03436)는 논문 본문에서 Gemma-2-9B 결과가 'directional'(미수렴 SAE 기준)임을 스스로 명시하며 스케일 한계를 인지하고 있다. 해결 경로는 신규 방법론 없이 동일한 훈련 파이프라인에 더 많은 컴퓨팅 자원을 투입하는 엔지니어링 과제이며, 'X를 더 큰 모델에서 재실행'은 연구 갭이 아닌 ablation at scale에 해당한다.

</details>

## 3. 연구 제안 (Proposer)

### 제안 1 — ATOMSAFE
**가설**: MetaSAE 분해 페널티로 훈련된 더 원자적인 SAE 특징은 표준 SAE 특징 대비 HalluSAE 프레임워크의 할루시네이션 탐지 AUROC와 CWAC의 유해 점수 억제율을 통계적으로 유의미하게 향상시킨다.
**메우는 갭**: A
**접근**: MetaSAE(arxiv:2604.03436)의 분해 페널티 목표로 훈련한 SAE를 HalluSAE(arxiv:2604.16430)의 잠재 위상 전이 탐지 파이프라인과 CWAC(arxiv:2604.12384)의 안전 서브스페이스 제약에 직접 교체 삽입한다. 동일 모델(Gemma-2-9B)에서 표준 TopK SAE와 MetaSAE를 각각 두 파이프라인에 연결한 통제 실험을 수행하고 할루시네이션 탐지 AUROC, 유해 점수, fuzzing 점수를 동시에 기록한다. 원자성 지표(mean |φ|, fuzzing 점수)와 안전 성능 사이의 회귀 분석으로 원자성-안전 전이의 인과 관계를 정량화한다. 추가로 CRaFT(arxiv:2604.01604)의 회로 영향 귀속을 활용해 원자적 특징이 활성화 크기 기반 선택보다 더 인과적인 거부 특징을 산출하는지 비교 검증한다.
**Baselines**: 표준 TopK SAE, MetaSAE, HalluSAE, CWAC, CRaFT; 평가 데이터셋: TruthfulQA, AdvBench jailbreak 벤치마크
**예상 기여**: SAE 원자성 개선이 실제 안전 응용으로 전이됨을 최초로 실증하며, SAE 훈련·설계 클러스터와 안전·정렬 클러스터 사이의 실증적 연결 공백을 채운다. 원자성과 안전 성능 사이의 정량적 관계 모델을 제시해 향후 SAE 훈련 시 안전 목표를 설계 목표에 직접 반영할 수 있는 기준을 수립한다. 할루시네이션 탐지와 탈옥 방어를 동시에 개선하는 단일 SAE 훈련 전략의 가능성을 열어 안전 SAE 연구의 새로운 방향을 제공한다.
**참고**: P-2604.03436, P-2604.16430, P-2604.12384, P-2604.01604

### 제안 2 — AUDIOSHIELD
**가설**: AVLLM의 시각 편향으로 억압된 오디오 표현은 텍스트·이미지 전용 방어(SALLIE, DACO)가 탐지하지 못하는 고유한 탈옥 공격 표면을 형성하며, 오디오 특징을 명시적으로 분리하는 SAE 채널을 추가하면 오디오 양태 탈옥 탐지 F1이 유의미하게 상승한다.
**메우는 갭**: B
**접근**: arxiv:2604.02605의 AVLLM 해석 분석에서 오디오 억압이 발생하는 층을 대상으로 오디오 전용 SAE를 훈련해 억압된 오디오 잠재 특징을 복원한다. 이 오디오 특징 사전을 SALLIE(arxiv:2604.06247)의 k-NN 층별 분류기에 세 번째 모달리티 채널로 통합한 AudioSALLIE 변형체를 구성한다. 적대적 오디오 명령 삽입·오디오-이미지 불일치 공격을 포함한 새 혼합 모달 탈옥 벤치마크를 구성하고, DACO(arxiv:2604.08846)·SALLIE 대비 탐지 F1과 거짓 음성률을 측정한다. 오디오 억압 계수(probing AUC 차이)와 공격 성공률 사이의 상관을 분석해 편향이 취약점으로 전환되는 임계 조건을 규명한다.
**Baselines**: SALLIE, DACO, DACO-400K, MM-SafetyBench; 기반 모델: Phi-3.5-vision-instruct, SmolVLM2-2.2B-Instruct
**예상 기여**: 멀티모달 안전 연구에서 오디오 모달리티가 체계적으로 누락된 공백을 최초로 실증하고, AVLLM 모달리티 편향이 실제 안전 취약점으로 전환됨을 인과적으로 입증한다. 텍스트·이미지·오디오 세 모달리티를 동시에 방어하는 최초의 SAE 기반 통합 MLLM 안전 프레임워크를 제공해 향후 옴니모달 안전 연구의 기준선을 설정한다.
**참고**: P-2604.02605, P-2604.08846, P-2604.06247

### 제안 3 — VLA-GUARD
**가설**: π₀.₅와 OpenVLA의 잔차 스트림에 존재하는 선형 관찰 가능한 특징 구조를 이용해 훈련된 SAE 안전 모니터는, 위험 행동(충돌 경로·금지 구역 침입)을 출력 토큰 투영 이전 잠재 표현 단계에서 탐지 AUROC 0.85 이상으로 조기 식별할 수 있다.
**메우는 갭**: C
**접근**: arxiv:2603.05487의 선형 분류기 및 최적 제어 개입 방법론을 확장해, 위험 행동 시뮬레이션(충돌·제약 위반)과 안전 행동 궤적의 잔차 스트림에 SAE를 훈련한다. 훈련된 SAE 특징에 보상 해킹 모니터(arxiv:2603.04069)의 경량 선형 분류기 구조를 적용해 행동 토큰 생성 전 위험 신호를 실시간 탐지하는 VLA-GUARD 파이프라인을 구성한다. π₀.₅와 OpenVLA 양 아키텍처에서 탐지 AUROC·개입 성공률·closed-loop 성능 저하를 시뮬레이션 환경에서 측정한다. 위험 신호의 조기 출현 레이어 및 시간 구조를 분석해 토큰 수준 모니터링과의 비교 우위를 확인한다.
**Baselines**: 미세조정 없는 OpenVLA·π₀.₅ 기본 모델, 토큰 수준 보상 해킹 모니터(arxiv:2603.04069); 시뮬레이션: MuJoCo 기반 로봇 조작 태스크
**예상 기여**: VLA 기계적 해석 가능성을 안전·정렬 응용과 최초로 연결해 구현 지능 도메인에서 SAE 안전 모니터링의 실현 가능성을 실증한다. 미세조정 없이 실시간으로 위험 행동을 탐지·차단하는 경량 프레임워크를 제공해 물리적 로봇 배포 전 안전 검증 비용을 대폭 절감하고, VLA 안전 연구의 후속 방향을 개방한다.
**참고**: P-2603.05487, P-2603.04069

### 제안 4 — CAUSALSAE
**가설**: 마스킹 정규화로 특징 흡수를 억제한 후 FAP 스타일 인과 귀속으로 개입 목표를 선택하면, 표준 SAE 개입 대비 인스턴스 수준 ripple effect 범위가 측정 가능하게 감소하고 교차 인스턴스 일반화 정확도가 통계적으로 유의미하게 향상된다.
**메우는 갭**: D
**접근**: 마스킹 정규화(arxiv:2604.06495)를 적용해 공동 활성화 기반 특징 흡수를 억제한 SAE를 훈련하고, 이후 PIE 프레임워크(arxiv:2604.16889)의 FAP 귀속 점수로 개입 목표 특징을 선택해 인과적으로 필수적인 특징에만 조정을 가하는 CAUSALSAE 파이프라인을 구성한다. Pando 벤치마크(arxiv:2604.11061)의 misleading explanation 조건을 핵심 평가 환경으로 채택해, 모델 언어 출력에 의존할 수 없는 정렬 감사 환경에서 개입의 인과적 신뢰성을 측정한다. 개입 전후 활성화 변화의 파급 범위(ripple effect 반경)와 non-target 특징 변화 크기를 정량화하고, activation magnitude 기반 선택·FAP 단독·마스킹 정규화 단독 대비 비교한다.
**Baselines**: 표준 TopK SAE 개입, 마스킹 정규화 SAE 단독, FAP 귀속 단독, activation magnitude 기반 특징 선택; Pando 벤치마크 720 모델, CLIP 디버깅 태스크(arxiv:2604.11467 재현)
**예상 기여**: 두 클러스터(LLM 특징 분석, 안전·정렬)에서 독립적으로 관찰된 인스턴스 수준 일반화 실패를 훈련 목표와 귀속 전략의 결합으로 최초 직접 해결한다. SAE 개입의 실용적 신뢰성 향상을 위한 인과 기반 특징 선택 기준을 제시해 전문가 사용자가 ripple effect 없이 가설 검증 워크플로우를 수행할 수 있도록 한다.
**참고**: P-2604.06495, P-2604.16889, P-2604.11061, P-2604.11467

### 제안 5 — TRAJSENTRY
**가설**: 연속 잠재 추론 모델에서 backdoor 정보는 개별 활성화 벡터가 아닌 집합적 잠재 궤적에 인코딩되므로, 추론 패스 전체의 SAE 특징 활성화 시계열을 집계하는 궤적 수준 모니터는 ThoughtSteer 유형 공격 탐지에서 토큰 수준 SAE 모니터 대비 AUROC 0.1 이상의 우위를 달성한다.
**메우는 갭**: F
**접근**: ThoughtSteer(arxiv:2604.00770)가 확인한 궤적 수준 선형 분리 가능성(probe AUC≥0.999)에 기초해, 각 연속 추론 패스의 잔차 스트림 활성화에 SAE를 적용하고 특징 활성화 벡터를 추론 단계 시계열로 집계하는 TRAJSENTRY를 설계한다. 보상 해킹 모니터(arxiv:2603.04069)의 경량 선형 분류기 구조를 차용해 집계 궤적에 대한 이상 탐지기를 훈련하고, 토큰 수준 모니터링과 궤적 수준 모니터링의 탐지 신호를 직접 비교한다. Coconut·SimCoT 아키텍처에서 ThoughtSteer의 세 벤치마크(GSM8K, ProntoQA, ProofWriter)를 재현해 탐지 AUROC·false negative rate·클린 정확도 유지율을 모델 스케일(124M~3B)별로 측정한다.
**Baselines**: 토큰 수준 SAE 모니터(arxiv:2603.04069), ThoughtSteer 논문의 다섯 가지 능동 방어 기준선; 아키텍처: Coconut, SimCoT; 벤치마크: GSM8K, ProntoQA, ProofWriter
**예상 기여**: 연속 추론 패러다임에서 SAE 모니터링을 토큰 수준에서 궤적 수준으로 재설계하는 최초 프레임워크를 제공해, 현재 모든 토큰 수준 방어를 구조적으로 우회하는 공격 표면에 실용적 방어를 확립한다. ThoughtSteer가 발견한 궤적 서명의 선형 분리 가능성이 실제 탐지에 활용 가능함을 실증하며, 향후 연속 추론 모델 안전 인프라 설계의 기준선을 제공한다.
**참고**: P-2604.00770, P-2603.04069

## 4. 참고문헌 (메타DB 기반)

[P-2604.21691] There Will Be a Scientific Theory of Deep Learning, Jamie Simon, Daniel Kunin, Alexander Atanasov et al., arXiv 2026 · http://arxiv.org/abs/2604.21691v1
[P-2604.21511] From Tokens to Concepts: Leveraging SAE for SPLADE, Yuxuan Zong, Mathias Vast, Basile Van Cooten et al., arXiv 2026 · http://arxiv.org/abs/2604.21511v1
[P-2604.20467] Mechanistic Interpretability Tool for AI Weather Models, Kirsten I. Tempest, Matthias Beylich, George C. Craig, arXiv 2026 · http://arxiv.org/abs/2604.20467v1
[P-2604.19974] Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders, Het Patel, Tiejin Chen, Hua Wei et al., arXiv 2026 · http://arxiv.org/abs/2604.19974v1
[P-2604.20895] Towards a Systematic Risk Assessment of Deep Neural Network Limitations in Autonomous Driving Perception, Svetlana Pavlitska, Christopher Gerking, J. Marius Zöllner, arXiv 2026 · http://arxiv.org/abs/2604.20895v1
[P-2604.18756] Towards Understanding the Robustness of Sparse Autoencoders, Ahson Saiyed, Sabrina Sadiekh, Chirag Agarwal, arXiv 2026 · http://arxiv.org/abs/2604.18756v1
[P-2604.18179] Committed SAE-Feature Traces for Audited-Session Substitution Detection in Hosted LLMs, Ziyang Liu, arXiv 2026 · http://arxiv.org/abs/2604.18179v1
[P-2604.18050] The Topological Dual of a Dataset: A Logic-to-Topology Encoding for AlphaGeometry-Style Data, Anthony Bordg, arXiv 2026 · http://arxiv.org/abs/2604.18050v1
[P-2604.17031] Where is the Mind? Persona Vectors and LLM Individuation, Pierre Beckmann, Patrick Butlin, arXiv 2026 · http://arxiv.org/abs/2604.17031v1
[P-2604.17025] Harness as an Asset: Enforcing Determinism via the Convergent AI Agent Framework (CAAF), Tianbao Zhang, arXiv 2026 · http://arxiv.org/abs/2604.17025v1
[P-2604.17622] STRIKE: Additive Feature-Group-Aware Stacking Framework for Credit Default Prediction, Swattik Maiti, Ritik Pratap Singh, Fardina Fathmiul Alam, arXiv 2026 · http://arxiv.org/abs/2604.17622v1
[P-2604.17391] RISC-V Functional Safety for Autonomous Automotive Systems: An Analytical Framework and Research Roadmap for ML-Assisted Certification, Nick Andreasyan, Mikhail Struve, Alexey Popov et al., arXiv 2026 · http://arxiv.org/abs/2604.17391v1
[P-2604.16889] Prune, Interpret, Evaluate: A Cross-Layer Transcoder-Native Framework for Efficient Circuit Discovery via Feature Attribution, Qinhao Chen, Linyang He, Nima Mesgarani, arXiv 2026 · http://arxiv.org/abs/2604.16889v1
[P-2604.14925] Improving Sparse Autoencoder with Dynamic Attention, Dongsheng Wang, Jinsen Zhang, Dawei Su et al., arXiv 2026 · http://arxiv.org/abs/2604.14925v1
[P-2604.14477] Seeing Through Circuits: Faithful Mechanistic Interpretability for Vision Transformers, Nina Żukowska, Wolfgang Stammer, Bernt Schiele et al., arXiv 2026 · http://arxiv.org/abs/2604.14477v1
[P-2604.13694] Weight Patching: Toward Source-Level Mechanistic Localization in LLMs, Chenghao Sun, Chengsheng Zhang, Guanzheng Qin et al., arXiv 2026 · http://arxiv.org/abs/2604.13694v1
[P-2604.13950] Causal Drawbridges: Characterizing Gradient Blocking of Syntactic Islands in Transformer LMs, Sasha Boguraev, Kyle Mahowald, arXiv 2026 · http://arxiv.org/abs/2604.13950v1
[P-2604.13304] Can Cross-Layer Transcoders Replace Vision Transformer Activations? An Interpretable Perspective on Vision, Gerasimos Chatzoudis, Konstantinos D. Polyzos, Zhuowei Li et al., arXiv 2026 · http://arxiv.org/abs/2604.13304v1
[P-2604.12384] Preventing Safety Drift in Large Language Models via Coupled Weight and Activation Constraints, Songping Peng, Zhiheng Zhang, Daojian Zeng et al., arXiv 2026 · http://arxiv.org/abs/2604.12384v1
[P-2604.12806] Interpretable Relational Inference with LLM-Guided Symbolic Dynamics Modeling, Xiaoxiao Liang, Juyuan Zhang, Liming Pan et al., arXiv 2026 · http://arxiv.org/abs/2604.12806v1
[P-2604.11467] From Attribution to Action: A Human-Centered Application of Activation Steering, Tobias Labarta, Maximilian Dreyer, Katharina Weitz et al., arXiv 2026 · http://arxiv.org/abs/2604.11467v1
[P-2604.11061] Pando: Do Interpretability Methods Work When Models Won't Explain Themselves?, Ziqian Zhong, Aashiq Muhamed, Mona T. Diab et al., arXiv 2026 · http://arxiv.org/abs/2604.11061v1
[P-2604.11962] The Linear Centroids Hypothesis: How Deep Network Features Represent Data, Thomas Walker, Ahmed Imtiaz Humayun, Randall Balestriero et al., arXiv 2026 · http://arxiv.org/abs/2604.11962v1
[P-2604.11549] Human Centered Non Intrusive Driver State Modeling Using Personalized Physiological Signals in Real World Automated Driving, David Puertas-Ramirez, Raul Fernandez-Matellan, David Martin Gomez et al., arXiv 2026 · http://arxiv.org/abs/2604.11549v1
[P-2604.11749] HistLens: Mapping Idea Change across Concepts and Corpora, Yi Jing, Weiyun Qiu, Yihang Peng et al., arXiv 2026 · http://arxiv.org/abs/2604.11749v1
[P-2604.10158] Tracing the Thought of a Grandmaster-level Chess-Playing Transformer, Rui Lin, Zhenyu Jin, Guancheng Zhou et al., arXiv 2026 · http://arxiv.org/abs/2604.10158v1
[P-2604.08846] Dictionary-Aligned Concept Control for Safeguarding Multimodal LLMs, Jinqi Luo, Jinyu Yang, Tal Neiman et al., arXiv 2026 · http://arxiv.org/abs/2604.08846v1
[P-2604.09364] Arbitration Failure, Not Perceptual Blindness: How Vision-Language Models Resolve Visual-Linguistic Conflicts, Farhad Nooralahzadeh, Omid Rohanian, Yi Zhang et al., arXiv 2026 · http://arxiv.org/abs/2604.09364v2
[P-2604.13466] Functional Emotions or Situational Contexts? A Discriminating Test from the Mythos Preview System Card, Hiranya V. Peiris, arXiv 2026 · http://arxiv.org/abs/2604.13466v2
[P-2604.08461] OVS-DINO: Open-Vocabulary Segmentation via Structure-Aligned SAM-DINO with Language Guidance, Haoxi Zeng, Qiankun Liu, Yi Bin et al., arXiv 2026 · http://arxiv.org/abs/2604.08461v1
[P-2604.08764] Revisiting Anisotropy in Language Transformers: The Geometry of Learning Dynamics, Raphael Bernas, Fanny Jourdan, Antonin Poché et al., arXiv 2026 · http://arxiv.org/abs/2604.08764v1
[P-2604.07019] ConceptTracer: Interactive Analysis of Concept Saliency and Selectivity in Neural Representations, Ricardo Knauer, Andre Beinrucker, Erik Rodner, arXiv 2026 · http://arxiv.org/abs/2604.07019v1
[P-2604.06495] Improving Robustness In Sparse Autoencoders via Masked Regularization, Vivek Narayanaswamy, Kowshik Thopalli, Bhavya Kailkhura et al., arXiv 2026 · http://arxiv.org/abs/2604.06495v1
[P-2604.06086] LAG-XAI: A Lie-Inspired Affine Geometric Framework for Interpretable Paraphrasing in Transformer Latent Spaces, Olexander Mazurets, Olexander Barmak, Leonid Bedratyuk et al., arXiv 2026 · http://arxiv.org/abs/2604.06086v1
[P-2604.06005] Disentangling MLP Neuron Weights in Vocabulary Space, Asaf Avrahamy, Yoav Gur-Arieh, Mor Geva, arXiv 2026 · http://arxiv.org/abs/2604.06005v1
[P-2604.05318] DIA-HARM: Dialectal Disparities in Harmful Content Detection Across 50 English Dialects, Jason Lucas, Matt Murtagh, Ali Al-Lawati et al., arXiv 2026 · http://arxiv.org/abs/2604.05318v1
[P-2604.05724] Beyond Semantics: Disentangling Information Scope in Sparse Autoencoders for CLIP, Yusung Ro, Jaehyun Choi, Junmo Kim, arXiv 2026 · http://arxiv.org/abs/2604.05724v1
[P-2604.06256] Spectral Edge Dynamics Reveal Functional Modes of Learning, Yongzhong Xu, arXiv 2026 · http://arxiv.org/abs/2604.06256v1
[P-2604.06247] SALLIE: Safeguarding Against Latent Language & Image Exploits, Guy Azov, Ofer Rivlin, Guy Shtar, arXiv 2026 · http://arxiv.org/abs/2604.06247v1
[P-2604.04720] What Makes Good Multilingual Reasoning? Disentangling Reasoning Traces with Measurable Features, Dayeon Ki, Kevin Duh, Marine Carpuat, arXiv 2026 · http://arxiv.org/abs/2604.04720v1
[P-2604.16430] HalluSAE: Detecting Hallucinations in Large Language Models via Sparse Auto-Encoders, Boshui Chen, Zhaoxin Fan, Ke Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.16430v1
[P-2604.05090] Multilingual Language Models Encode Script Over Linguistic Structure, Aastha A K Verma, Anwoy Chatterjee, Mehak Gupta et al., arXiv 2026 · http://arxiv.org/abs/2604.05090v2
[P-2604.04037] Geometric Limits of Knowledge Distillation: A Minimum-Width Theorem via Superposition Theory, Nilesh Sarkar, Dawar Jyoti Deka, arXiv 2026 · http://arxiv.org/abs/2604.04037v2
[P-2604.03919] Interpreting Video Representations with Spatio-Temporal Sparse Autoencoders, Atahan Dokme, Sriram Vishwanath, arXiv 2026 · http://arxiv.org/abs/2604.03919v1
[P-2604.03764] Automated Attention Pattern Discovery at Scale in Large Language Models, Jonathan Katzy, Razvan-Mihai Popescu, Erik Mekkes et al., arXiv 2026 · http://arxiv.org/abs/2604.03764v1
[P-2604.03532] LangFIR: Discovering Sparse Language-Specific Features from Monolingual Data for Language Steering, Sing Hieng Wong, Hassan Sajjad, A. B. Siddique, arXiv 2026 · http://arxiv.org/abs/2604.03532v1
[P-2604.03436] MetaSAEs: Joint Training with a Decomposability Penalty Produces More Atomic Sparse Autoencoder Latents, Matthew Levinson, arXiv 2026 · http://arxiv.org/abs/2604.03436v1
[P-2604.02685] Finding Belief Geometries with Sparse Autoencoders, Matthew Levinson, arXiv 2026 · http://arxiv.org/abs/2604.02685v1
[P-2604.02605] Do Audio-Visual Large Language Models Really See and Hear?, Ramaneswaran Selvakumar, Kaousheik Jayakumar, S Sakshi et al., arXiv 2026 · http://arxiv.org/abs/2604.02605v1
[P-2604.04030] Jellyfish: Zero-Shot Federated Unlearning Scheme with Knowledge Disentanglement, Houzhe Wang, Xiaojie Zhu, Chi Chen, arXiv 2026 · http://arxiv.org/abs/2604.04030v1
[P-2604.02871] SPG: Sparse-Projected Guides with Sparse Autoencoders for Zero-Shot Anomaly Detection, Tomoyasu Nanaumi, Yukino Tsuzuki, Junichi Okubo et al., arXiv 2026 · http://arxiv.org/abs/2604.02871v1
[P-2604.02206] LEO: Graph Attention Network based Hybrid Multi Sensor Extended Object Fusion and Tracking for Autonomous Driving Applications, Mayank Mayank, Bharanidhar Duraisamy, Florian Geiss, arXiv 2026 · http://arxiv.org/abs/2604.02206v1
[P-2604.01619] Automatic Image-Level Morphological Trait Annotation for Organismal Images, Vardaan Pahuja, Samuel Stevens, Alyson East et al., arXiv 2026 · http://arxiv.org/abs/2604.01619v2
[P-2604.01604] CRaFT: Circuit-Guided Refusal Feature Selection via Cross-Layer Transcoders, Su-Hyeon Kim, Hyundong Jin, Yejin Lee et al., arXiv 2026 · http://arxiv.org/abs/2604.01604v1
[P-2604.01764] Hidden Meanings in Plain Sight: RebusBench for Evaluating Cognitive Visual Reasoning, Seyed Amir Kasaei, Arash Marioriyad, Mahbod Khaleti et al., arXiv 2026 · http://arxiv.org/abs/2604.01764v1
[P-2604.00770] Thinking Wrong in Silence: Backdoor Attacks on Continuous Latent Reasoning, Swapnil Parekh, arXiv 2026 · http://arxiv.org/abs/2604.00770v1
[P-2604.00443] Polysemanticity or Polysemy? Lexical Identity Confounds Superposition Metrics, Iyad Ait Hou, Rebecca Hwa, arXiv 2026 · http://arxiv.org/abs/2604.00443v1
[P-2604.22345] Preference Heads in Large Language Models: A Mechanistic Framework for Interpretable Personalization, Weixu Zhang, Ye Yuan, Changjiang Han et al., arXiv 2026 · http://arxiv.org/abs/2604.22345v1
[P-2602.22968] Certified Circuits: Stability Guarantees for Mechanistic Circuits, Alaa Anani, Tobias Lorenz, Bernt Schiele et al., arXiv 2026 · http://arxiv.org/abs/2602.22968v2
[P-2602.22600] Transformers converge to invariant algorithmic cores, Joshua S. Schiffman, arXiv 2026 · http://arxiv.org/abs/2602.22600v1
[P-2602.23164] MetaOthello: A Controlled Study of Multiple World Models in Transformers, Aviral Chawla, Galen Hall, Juniper Lovato, arXiv 2026 · http://arxiv.org/abs/2602.23164v1
[P-2602.23405] On De-Individuated Neurons: Continuous Symmetries Enable Dynamic Topologies, George Bird, arXiv 2026 · http://arxiv.org/abs/2602.23405v1
[P-2602.22719] Interpreting and Steering State-Space Models via Activation Subspace Bottlenecks, Vamshi Sunku Mohan, Kaustubh Gupta, Aneesha Das et al., arXiv 2026 · http://arxiv.org/abs/2602.22719v1
[P-2602.24014] Interpretable Debiasing of Vision-Language Models for Social Fairness, Na Min An, Yoonna Jang, Yusuke Hirota et al., arXiv 2026 · http://arxiv.org/abs/2602.24014v1
[P-2603.13277] Learning Retrieval Models with Sparse Autoencoders, Thibault Formal, Maxime Louis, Hervé Dejean et al., arXiv 2026 · http://arxiv.org/abs/2603.13277v1
[P-2603.01822] Emerging Human-like Strategies for Semantic Memory Foraging in Large Language Models, Eric Lacosse, Mariana Duarte, Peter M. Todd et al., arXiv 2026 · http://arxiv.org/abs/2603.01822v1
[P-2603.01752] Causal Circuit Tracing Reveals Distinct Computational Architectures in Single-Cell Foundation Models: Inhibitory Dominance, Biological Coherence, and Cross-Model Convergence, Ihor Kendiukhov, arXiv 2026 · http://arxiv.org/abs/2603.01752v2
[P-2603.03131] Joint Training Across Multiple Activation Sparsity Regimes, Haotian Wang, arXiv 2026 · http://arxiv.org/abs/2603.03131v1
[P-2603.02908] SAE as a Crystal Ball: Interpretable Features Predict Cross-domain Transferability of LLMs without Training, Qi Zhang, Yifei Wang, Xiaohan Wang et al., arXiv 2026 · http://arxiv.org/abs/2603.02908v1
[P-2603.03031] Step-Level Sparse Autoencoder for Reasoning Process Interpretation, Xuan Yang, Jiayu Liu, Yuhang Lai et al., arXiv 2026 · http://arxiv.org/abs/2603.03031v1
[P-2603.02952] Sparse autoencoders reveal organized biological knowledge but minimal regulatory logic in single-cell foundation models: a comparative atlas of Geneformer and scGPT, Ihor Kendiukhov, arXiv 2026 · http://arxiv.org/abs/2603.02952v1
[P-2603.04069] Monitoring Emergent Reward Hacking During Generation via Internal Activations, Patrick Wilhelm, Thorsten Wittkopp, Odej Kao, arXiv 2026 · http://arxiv.org/abs/2603.04069v1
[P-2603.04198] Stable and Steerable Sparse Autoencoders with Weight Regularization, Piotr Jedryszek, Oliver M. Crook, arXiv 2026 · http://arxiv.org/abs/2603.04198v1
[P-2603.04146] LISTA-Transformer Model Based on Sparse Coding and Attention Mechanism and Its Application in Fault Diagnosis, Shuang Liu, Lina Zhao, Tian Wang et al., arXiv 2026 · http://arxiv.org/abs/2603.04146v1
[P-2603.05228] The Geometric Inductive Bias of Grokking: Bypassing Phase Transitions via Architectural Topology, Alper Yıldırım, arXiv 2026 · http://arxiv.org/abs/2603.05228v2
[P-2603.04981] Rethinking Representativeness and Diversity in Dynamic Data Selection, Yuzhe Zhou, Zhenglin Hua, Haiyun Guo et al., arXiv 2026 · http://arxiv.org/abs/2603.04981v1
[P-2603.05708] Interpretable Perception and Reasoning for Audiovisual Geolocation, Yiyang Su, Xiaoming Liu, arXiv 2026 · http://arxiv.org/abs/2603.05708v1
[P-2603.05716] Introducing the transitional autonomous vehicle lane-changing dataset: Empirical Experiments, Abhinav Sharma, Zijun He, Danjue Chen, arXiv 2026 · http://arxiv.org/abs/2603.05716v1
[P-2603.05487] Observing and Controlling Features in Vision-Language-Action Models, Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann et al., arXiv 2026 · http://arxiv.org/abs/2603.05487v1
[P-2603.23524] Navigating the Concept Space of Language Models, Wilson E. Marcílio-Jr, Danilo M. Eler, arXiv 2026 · http://arxiv.org/abs/2603.23524v1

---

## 메타 / 디버그
- model: claude-sonnet-4-6
- matched_n: 80
- window_days: 60
