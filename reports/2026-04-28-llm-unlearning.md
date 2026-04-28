# Research Topic Suggestion — "llm unlearning"

생성: 2026-04-28T05:38:29.969648+00:00
DB 윈도우: 2025-04-28 ~ 2026-04-28 (365d)
모델: claude-sonnet-4-6
매칭 논문: 50건
확장 키워드: ['llm unlearning', 'language model unlearning', 'knowledge unlearning', 'concept erasure', 'concept unlearning', 'tofu benchmark', 'wmdp benchmark', 'llm forgetting', 'selective forgetting', 'harmful knowledge removal', 'copyright unlearning', 'memorization removal']

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — LLM 언러닝 알고리즘
- **설명**: LLM에서 특정 지식을 제거하기 위한 최적화·학습 방법론을 다루는 연구들. 경사 기반, 강화학습, 증류, 표현 유도 등 다양한 파라미터 수정 기법이 포함된다.
- **빈도**: 23건
- **분기별 (≈91d씩, 오래된→최근)**: 7 → 10 → 0 → 6
- **대표 논문**:
  - [P-NEURIPS-652cbf] Simplicity Prevails: Rethinking Negative Preference Optimization for LLM Unlearning — Chongyu Fan, Jiancheng Liu, Licong Lin et al., NeurIPS 2025
  - [P-NEURIPS-5d5ed4] RULE: Reinforcement UnLEarning Achieves Forget-retain Pareto Optimality — Chenlong Zhang, Zhuoran Jin, Hongbang Yuan et al., NeurIPS 2025
  - [P-NEURIPS-b885ac] Distillation Robustifies Unlearning — Bruce W. Lee, Addie Foote, Alex Infanger et al., NeurIPS 2025

### 클러스터 2 — 확산 모델 개념 소거
- **설명**: 텍스트-이미지 확산 모델(및 시각적 자기회귀 모델)에서 유해·저작권·스타일 등 특정 개념을 선택적으로 제거하는 연구들. 파인튜닝 기반과 학습 불필요(training-free) 방식 모두 포함된다.
- **빈도**: 16건
- **분기별 (≈91d씩, 오래된→최근)**: 6 → 8 → 0 → 2
- **대표 논문**:
  - [P-NEURIPS-016c3a] When Are Concepts Erased From Diffusion Models? — Kevin Lu, Nicky Kriplani, Rohit Gandikota et al., NeurIPS 2025
  - [P-ICLR-9416cd] SPEED: Scalable, Precise, and Efficient Concept Erasure for Diffusion Models — Ouxiang Li, Yuan Wang, Xinting Hu et al., ICLR 2025
  - [P-ICLR-ba1f61] Forget Many, Forget Right: Scalable and Precise Concept Unlearning in Diffusion Models — Kaiyuan Deng, Gen Li, Yang Xiao et al., ICLR 2025

### 클러스터 3 — 언러닝 평가·강건성
- **설명**: 언러닝 효과를 측정하는 평가 지표 및 벤치마크 개발, 그리고 언러닝 후 재공격·역추적에 대한 강건성 분석을 중점적으로 다루는 연구들.
- **빈도**: 6건
- **분기별 (≈91d씩, 오래된→최근)**: 2 → 3 → 0 → 1
- **대표 논문**:
  - [P-ICLR-2ee5d3] WaterDrum: Watermark-based Data-centric Unlearning Metric — Xinyang Lu, Xinyuan Niu, Gregory Kang Ruey Lau et al., ICLR 2025
  - [P-ICLR-320a2e] Unlearning Isn't Invisible: Detecting Unlearning Traces in LLMs from Model Outputs — Yiwei Chen, Soumyadeep Pal, Yimeng Zhang et al., ICLR 2025
  - [P-NEURIPS-7f253a] Do LLMs Really Forget? Evaluating Unlearning  with Knowledge Correlation and Confidence Awareness — Rongzhe Wei, Peizhi Niu, Hans Hao-Hsun Hsu et al., NeurIPS 2025

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap A — 'Unlearning Isn't Invisible'은 단순 분류기만으로 언러닝 여부를 90%+ 정확도로 탐지할 수 있음을 보였고, 'Keepin
- **타입**: single-shot
- **설명**: 'Unlearning Isn't Invisible'은 단순 분류기만으로 언러닝 여부를 90%+ 정확도로 탐지할 수 있음을 보였고, 'Keeping an Eye'는 언러닝 신호가 일반 토큰과 연결될 경우 정상 사용자 피해를 경고한다. 그러나 LLM 알고리즘 클러스터의 어떤 논문도 trace-minimization을 명시적 설계 목표로 삼지 않는다.
- **근거 논문**: P-ICLR-320a2e, P-NEURIPS-a7f436
- **Skeptic 검토**: ✓ 통과 — PRISM의 이중 공간 평활화가 표현 공간 강건성을 다루나, 목표는 jailbreak 방어이지 언러닝 흔적 최소화가 아니다. 탐지 논문이 평가 클러스터에 존재하더라도 이를 알고리즘 설계 제약으로 내면화한 후속 작업이 코퍼스 전체에 없음을 메타데이터로 확인.

### Gap B — LLM 언러닝 알고리즘 클러스터(RULE, PURGE, LUNAR 등)와 확산 모델 개념 소거 클러스터(EraseFlow, AEGIS, SPEE
- **타입**: between-clusters
- **설명**: LLM 언러닝 알고리즘 클러스터(RULE, PURGE, LUNAR 등)와 확산 모델 개념 소거 클러스터(EraseFlow, AEGIS, SPEED 등)는 retain-forget 트레이드오프 구조를 공유하지만, 강화학습·GFlowNet·표현 리디렉션 방법이 각 도메인 간 상호 적용된 사례가 없다.
- **근거 논문**: P-NEURIPS-5d5ed4, P-ICLR-eaff2c, P-NEURIPS-959c93, P-NEURIPS-adaac1, P-NEURIPS-a39980
- **Skeptic 검토**: ✓ 통과 — CURE(직교 투영)와 REGLU(LoRA 직교 표현)이 수학적으로 수렴하나, 자기회귀 토큰 생성 공간과 확산 점수 함수 공간의 구조 차이는 직접 전이를 비자명하게 만든다. 두 커뮤니티의 완전한 병렬 발전은 클러스터 내 상호 인용 부재로 메타데이터 수준에서 확인 가능.

### Gap C — 실제 배포 환경에서 정제된 forget/retain set이 불가용한 시나리오를 정면으로 다루는 방법론이 2–3편에 불과하고 전용 벤치마크가 없
- **타입**: recurring-limitation
- **설명**: 실제 배포 환경에서 정제된 forget/retain set이 불가용한 시나리오를 정면으로 다루는 방법론이 2–3편에 불과하고 전용 벤치마크가 없다.
- **근거 논문**: P-2604.21251, P-ICLR-ddd8ef, P-2604.16591, P-2604.12459
- **Skeptic 검토**: ✓ 통과 — DRAGON(retain 없음), CAP(클로즈드소스), RASLIG(forget 검색), arxiv:2604.12459(GDPR 순차 언러닝)가 각각 한 측면만 해결한다. 세 제약 동시 해결 프레임워크와 전용 벤치마크 부재는 확인 가능. 다만 갭 서술이 세 하위 문제를 하나로 묶어 후속 연구 목표가 모호하다는 점은 제안 단계에서 구체화 필요.

### Gap D — 확산 모델 개념 소거 평가는 CLIP·FID·NSFW 탐지기 등 시각적 품질 지표에만 의존하며, LLM 언러닝 평가 클러스터가 발전시킨 데이터 
- **타입**: between-clusters
- **설명**: 확산 모델 개념 소거 평가는 CLIP·FID·NSFW 탐지기 등 시각적 품질 지표에만 의존하며, LLM 언러닝 평가 클러스터가 발전시킨 데이터 출처 수준의 소거 완전성 지표가 존재하지 않는다.
- **근거 논문**: P-ICLR-2ee5d3, P-NEURIPS-016c3a, P-NEURIPS-7f253a
- **Skeptic 검토**: ✓ 통과 — 'When Are Concepts Erased?'가 시각적 프로빙 다양화(classifier guidance, trajectory modification)를 제안하나, 데이터 출처 수준의 소거 완전성 검증이라는 정의 자체를 다루지 않는다. WaterDrum은 텍스트 워터마킹 의존 구조상 이미지 생성 도메인에 직접 이식 불가 — 확산 모델 전용 데이터 중심 지표 개발이 독립 연구로 성립.

### Gap F — 'Learning-Time Encoding Shapes Unlearning in LLMs'는 훈련 시 지식 인코딩 방식이 사후 언러닝 난이도를 
- **타입**: recurring-limitation
- **설명**: 'Learning-Time Encoding Shapes Unlearning in LLMs'는 훈련 시 지식 인코딩 방식이 사후 언러닝 난이도를 결정함을 실증했으나, 이를 사전 설계 원칙으로 발전시킨 연구가 코퍼스 전체에 없다.
- **근거 논문**: P-ICLR-f60687, P-ICLR-8a4120, P-NEURIPS-adaac1
- **Skeptic 검토**: ✓ 통과 — 인코딩 다양성 → 언러닝 용이성 인과 관계는 신뢰할 수 있는 실증이며, '패러프레이즈 추가'로 환원되지 않는 설계 원칙(지식 격리 커리큘럼, disentangled 인코딩 등) 탐구가 잔존한다. CLUE·LUNAR는 사후 위치 파악만 수행하며 사전 설계를 다루지 않음을 메타데이터로 확인.

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap E** — 에이전트 외부 메모리 관리(FSFM, H²-EMV)와 파라미터 언러닝(LLM 알고리즘 클러스터)을 통합하는 프레임워크 부재 · 거부 사유: (c) trivial — 두 메커니즘은 작동 층위(세션 벡터 DB 항목 삭제 vs. 모델 가중치 수정), 발화 조건(운영 효율성·세션 보안 vs. GDPR 규제 준수), 시간 규모(실시간 vs. 배포 후 일괄)가 완전히 다르다. '통합'의 실체는 레이어드 아키텍처에서 두 컴포넌트를 독립 구동하는 엔지니어링 구성으로, 새로운 알고리즘이나 이론이 요구되지 않는다. MEM1이 이미 RL로 컨텍스트 내 상태 선택적 통합을 다루고, 파라미터 언러닝은 별도 규제 프로세스로 처리되는 것이 표준 배포 패턴이다. 두 층위를 동시에 필요로 하는 위협 모델도 코퍼스 내 어떤 논문에도 수립되어 있지 않다.

</details>

## 3. 연구 제안 (Proposer)

### 제안 1 — GHOST-UNLEARN
**가설**: 언러닝 최적화 목표에 적대적 흔적 탐지기를 공동 훈련시키는 정규화 항을 추가하면, 단순 분류기 기반 언러닝 탐지 정확도를 우연 수준(~50%)으로 낮추면서 WMDP·TOFU 벤치마크 기준 forget efficacy를 유지할 수 있다.
**메우는 갭**: A
**접근**: 언러닝 파라미터 업데이트와 동시에, 모델 출력 로짓 및 중간 활성화 패턴에서 언러닝 여부를 구분하는 이진 탐지기 네트워크를 min-max 방식으로 공동 훈련한다. 탐지기 손실의 역전파를 통해 언러닝 모델이 원본 모델과 구분 불가능한 활성화 분포를 유지하도록 표현 공간 정규화 항을 추가한다. LUNAR의 선형 표현 리디렉션을 탐지기 혼동 제약과 결합하여, forget-set에서는 능력을 제거하되 활성화 매니폴드 형태는 언러닝 전과 유사하게 유지한다. 평가는 'Unlearning Isn't Invisible' 탐지 프로토콜을 적대적 평가 지표로 채택한다.
**Baselines**: LUNAR, PRISM(Dual-Space Smoothness), SimNPO, WMDP Bio/Cyber, TOFU, MUSE
**예상 기여**: 언러닝 탐지 정확도를 명시적 설계 제약으로 삼는 최초의 trace-minimizing 언러닝 프레임워크를 제시한다. 언러닝 흔적 최소화와 jailbreak 공격 표면 축소가 동시 달성 가능함을 실증하여 언러닝 알고리즘 평가에 새로운 축을 정립한다. 기존 WMDP·TOFU 기준에서 comparable한 forgetting을 유지하면서 탐지 공격에 대한 저항성을 추가로 확보한다.
**참고**: P-ICLR-320a2e, P-NEURIPS-a7f436, P-NEURIPS-adaac1, P-ICLR-87e305, P-NEURIPS-652cbf

### 제안 2 — GFLOW-ERASE
**가설**: EraseFlow의 GFlowNet trajectory-balance 목적함수를 LLM 자기회귀 토큰 생성 경로 공간에 재정의하면, RULE·PURGE의 검증 가능 보상 신호를 활용하면서 forget-retain Pareto 프론티어를 개선하고 자연스러운 거부 응답 다양성을 확보할 수 있다.
**메우는 갭**: B
**접근**: LLM 토큰 시퀀스 생성 과정을 확산 디노이징 경로에 대응시켜, trajectory-balance 목적함수를 자기회귀 토큰 공간에서 재정의한다. GFlowNet 보상 신호를 RULE의 경계 쿼리 기반 거부 최적화와 결합하여, 금지 개념 관련 생성에 대한 거부를 stochastic policy로 학습한다. PURGE의 group-relative 정책 최적화를 초기화 방법으로 활용하고, GFlowNet 파인튜닝으로 policy diversity를 확장한다. LLM→확산 방향의 방법론 이전 가능성을 검증하기 위해, LUNAR의 활성화 리디렉션 개념을 확산 모델 score function 공간에 대응하는 ablation도 포함한다.
**Baselines**: RULE, PURGE(GRPO), EraseFlow, RWKU, WMDP Bio/Cyber
**예상 기여**: LLM 언러닝과 확산 모델 개념 소거 간 방법론적 시너지의 첫 실증 검증을 제공하여 두 커뮤니티를 연결하는 이론적 교량을 구축한다. GFlowNet의 생성 다양성 촉진 특성이 LLM 언러닝의 자연스러운 응답 생성 문제를 완화함을 보인다. forget-retain 트레이드오프의 공통 수학적 구조를 규명하여 도메인 독립적 언러닝 이론의 토대를 마련한다.
**참고**: P-NEURIPS-5d5ed4, P-ICLR-eaff2c, P-NEURIPS-959c93, P-NEURIPS-adaac1, P-ICLR-8a4120, P-NEURIPS-a39980

### 제안 3 — PROOF-ERASE
**가설**: 확산 모델 학습 데이터에 불가시적 주파수 도메인 워터마크를 삽입하면, 소거 후 생성 이미지의 워터마크 신호 잔존율을 측정하여 CLIP·FID 기반 평가가 포착하지 못하는 부분적 소거(spurious erasure)를 데이터 출처 수준에서 정량화할 수 있다.
**메우는 갭**: D
**접근**: 훈련 데이터에 불가시적 주파수 도메인 워터마크(DCT 계수 조작)를 개념별로 삽입하고, 소거 후 생성 이미지의 워터마크 신호 감쇠율로 소거 완전성을 정의하는 평가 프레임워크를 구축한다. SPEED, AEGIS, ScaPre 등 대표적 소거 방법에 적용하여 기존 CLIP·FID·NSFW 지표와의 상관관계 및 괴리를 체계적으로 분석한다. nudity·artistic style·object 등 다양한 개념 유형과 adversarial prompt 공격 강도별 워터마크 잔존 곡선을 구축하여, LLM 영역의 WaterDrum과 대칭적인 데이터 중심 확산 모델 소거 벤치마크로 공개한다.
**Baselines**: SPEED, AEGIS, ScaPre(Forget Many Forget Right), WaterDrum, UnlearnCanvas, NSFW 탐지기
**예상 기여**: 확산 모델 전용 데이터 출처 수준 소거 완전성 지표를 최초로 제안하여 기존 시각적 평가의 과대 추정 문제를 정량화한다. LLM의 WaterDrum과 대칭적인 이미지 도메인 평가 체계를 제공하여 두 도메인 간 평가 방법론 통합 가능성을 시사한다. 새로운 벤치마크 데이터셋이 후속 소거 방법 개발의 표준 평가 기반으로 기능한다.
**참고**: P-ICLR-2ee5d3, P-NEURIPS-016c3a, P-ICLR-9416cd, P-ICLR-82e58b, P-ICLR-ba1f61, P-NEURIPS-7f253a

## 4. 참고문헌 (메타DB 기반)

### 클러스터 1 — LLM 언러닝 알고리즘 (23)
- [P-ICLR-ff3c8f] Downgrade to Upgrade: Optimizer Simplification Enhances Robustness in LLM Unlearning, Yicheng Lang, Yihua Zhang, Chongyu Fan et al., ICLR 2025 · https://openreview.net/forum?id=Sswng2ToR4
- [P-ICLR-12ca0d] DUET: Distilled LLM Unlearning from an Efficiently Contextualized Teacher, Yisheng Zhong, Zhengbang Yang, Zhuangdi Zhu, ICLR 2025 · https://openreview.net/forum?id=Xa6QRrXrKX
- [P-ICLR-ddd8ef] DRAGON: Guard LLM Unlearning in Context via Negative Detection and Reasoning, Yaxuan Wang, Chris Yuhao Liu, Quan Liu et al., ICLR 2025 · https://openreview.net/forum?id=vQLUAkl5SG
- [P-ICLR-87e305] Dual-Space Smoothness for Robust and Balanced LLM Unlearning, Han Yan, Zheyuan Liu, Meng Jiang, ICLR 2025 · https://openreview.net/forum?id=VIMW3eys6x
- [P-ICLR-eaff2c] Reinforcement Unlearning via Group Relative Policy Optimization, Efstratios Zaradoukas, Bardh Prenkaj, Gjergji Kasneci, ICLR 2025 · https://openreview.net/forum?id=BjWwqPE7mk
- [P-ICLR-f60687] Learning-Time Encoding Shapes Unlearning in LLMs, Ruihan Wu, Konstantin Garov, Kamalika Chaudhuri, ICLR 2025 · https://openreview.net/forum?id=BcjZCertEk
- [P-ICLR-8bbd97] Explainable LLM Unlearning through Reasoning, Junfeng Liao, Qizhou Wang, Shanshan Ye et al., ICLR 2025 · https://openreview.net/forum?id=wec4qy2XIF
- [P-ICLR-5dcc16] LLM Unlearning with LLM Beliefs, Kemou Li, Qizhou Wang, Yue Wang et al., ICLR 2025 · https://openreview.net/forum?id=qCfYOLAzti
- [P-ICLR-8a4120] CLUE: Conflict-guided Localization for LLM Unlearning Framework, Hang Chen, Jiaying Zhu, Xinyu Yang et al., ICLR 2025 · https://openreview.net/forum?id=jtRYvazBWv
- [P-ICLR-25e420] Robust LLM Unlearning via Post Judgment and Multi-round Thinking, Xinrui Chen, Xu Cao, Jianhao Zhang et al., ICLR 2025 · https://openreview.net/forum?id=GBTUVO9vkj
- [P-NEURIPS-adaac1] LLM Unlearning via Neural Activation Redirection, William F. Shen, Xinchi Qiu, Meghdad Kurmanji et al., NeurIPS 2025 · https://openreview.net/forum?id=teB4aqJsNP
- [P-NEURIPS-6b8b16] Constrained Entropic Unlearning: A Primal-Dual Framework for Large Language Models, Taha Entesari, Arman Hatami, Rinat Khaziev et al., NeurIPS 2025 · https://openreview.net/forum?id=ZtB34bQI54
- [P-NEURIPS-652cbf] Simplicity Prevails: Rethinking Negative Preference Optimization for LLM Unlearning, Chongyu Fan, Jiancheng Liu, Licong Lin et al., NeurIPS 2025 · https://openreview.net/forum?id=JbvSQm5h1l
- [P-NEURIPS-b885ac] Distillation Robustifies Unlearning, Bruce W. Lee, Addie Foote, Alex Infanger et al., NeurIPS 2025 · https://openreview.net/forum?id=UTGjik64IK
- [P-NEURIPS-7bef44] Wisdom is Knowing What not to Say: Hallucination-Free LLMs Unlearning via Attention Shifting, Chenchen Tan, Youyang Qu, Xinghao Li et al., NeurIPS 2025 · https://openreview.net/forum?id=LNWyf2RR1V
- [P-NEURIPS-4f4467] Elastic Robust Unlearning of Specific Knowledge in Large Language Models, Yize Sui, Jing Ren, Wenjing Yang et al., NeurIPS 2025 · https://openreview.net/forum?id=VrXjAfdwrN
- [P-NEURIPS-5d5ed4] RULE: Reinforcement UnLEarning Achieves Forget-retain Pareto Optimality, Chenlong Zhang, Zhuoran Jin, Hongbang Yuan et al., NeurIPS 2025 · https://openreview.net/forum?id=heIh4lkBEd
- [P-2604.21251] CAP: Controllable Alignment Prompting for Unlearning in LLMs, Zhaokun Wang, Jinyu Guo, Jingwen Pu et al., arXiv 2026 · http://arxiv.org/abs/2604.21251v1
- [P-2604.17396] Representation-Guided Parameter-Efficient LLM Unlearning, Zeguan Xiao, Lang Mo, Yun Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.17396v1
- [P-2604.16591] Randomized Antipodal Search Done Right for Data Pareto Improvement of LLM Unlearning, Ziwen Liu, Huawei Lin, Yide Ran et al., arXiv 2026 · http://arxiv.org/abs/2604.16591v1
- [P-2604.15482] Harmonizing Multi-Objective LLM Unlearning via Unified Domain Representation and Bidirectional Logit Distillation, Yisheng Zhong, Sijia Liu, Zhuangdi Zhu, arXiv 2026 · http://arxiv.org/abs/2604.15482v1
- [P-2604.14808] Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem, Zeguan Xiao, Siqing Li, Yong Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.14808v1
- [P-2604.12459] Operationalising the Right to be Forgotten in LLMs: A Lightweight Sequential Unlearning Framework for Privacy-Aligned Deployment in Politically Sensitive Environments, Esen Kurt, Haithem Afli, arXiv 2026 · http://arxiv.org/abs/2604.12459v1

### 클러스터 2 — 확산 모델 개념 소거 (16)
- [P-ICLR-cc0ddd] Co-occurring Associated REtained concepts in Diffusion Unlearning, Miso Kim, Georu Lee, Yunji Kim et al., ICLR 2025 · https://openreview.net/forum?id=Ryc7jKP6H9
- [P-ICLR-58608b] Localized Concept Erasure in Text-to-Image Diffusion Models via High-Level Representation Misdirection, Uichan Lee, Jeonghyeon Kim, Sangheum Hwang, ICLR 2025 · https://openreview.net/forum?id=JSjOlFLUsS
- [P-ICLR-dc1cf6] CASteer: Cross-Attention Steering for Controllable Concept Erasure, Tatiana Gaintseva, Andreea-Maria Oncescu, Chengcheng Ma et al., ICLR 2025 · https://openreview.net/forum?id=6D5Odqol1B
- [P-ICLR-8896e4] SDErasure: Concept-Specific Trajectory Shifting for Concept Erasure via Adaptive Diffusion Classifier, Fengyuan Miao, Shancheng Fang, Lingyun Yu et al., ICLR 2025 · https://openreview.net/forum?id=EWM9JQ6gX7
- [P-ICLR-ba1f61] Forget Many, Forget Right: Scalable and Precise Concept Unlearning in Diffusion Models, Kaiyuan Deng, Gen Li, Yang Xiao et al., ICLR 2025 · https://openreview.net/forum?id=zt7IPzsXrT
- [P-ICLR-82e58b] AEGIS: Adversarial Target-Guided Retention-Data-Free Robust Concept Erasure from Diffusion Models, Fengpeng Li, Kemou Li, Qizhou Wang et al., ICLR 2025 · https://openreview.net/forum?id=3y3hnL7KhS
- [P-ICLR-9416cd] SPEED: Scalable, Precise, and Efficient Concept Erasure for Diffusion Models, Ouxiang Li, Yuan Wang, Xinting Hu et al., ICLR 2025 · https://openreview.net/forum?id=aoEtzdRkGh
- [P-ICLR-ccebeb] Closing the Safety Gap: Surgical Concept Erasure in Visual Autoregressive Models, Xinhao Zhong, Yimin Zhou, Zhiqi Zhang et al., ICLR 2025 · https://openreview.net/forum?id=tlYSbw5GXY
- [P-NEURIPS-016c3a] When Are Concepts Erased From Diffusion Models?, Kevin Lu, Nicky Kriplani, Rohit Gandikota et al., NeurIPS 2025 · https://openreview.net/forum?id=UKt31LbRPI
- [P-NEURIPS-5ca6ce] Semantic Surgery: Zero-Shot Concept Erasure in Diffusion Models, Lexiang Xiong, Liu Chengyu, Jingwen Ye et al., NeurIPS 2025 · https://openreview.net/forum?id=3FTVceZQrh
- [P-NEURIPS-959c93] EraseFlow: Learning Concept Erasure Policies via GFlowNet-Driven Alignment, Naga Sai Abhiram kusumba, Maitreya Patel, Kyle Min et al., NeurIPS 2025 · https://openreview.net/forum?id=igB289kbej
- [P-NEURIPS-277bfb] CURE: Concept Unlearning via Orthogonal Representation Editing in Diffusion Models, Shristi Das Biswas, Arani Roy, Kaushik Roy, NeurIPS 2025 · https://openreview.net/forum?id=zprMrpiLgT
- [P-NEURIPS-a39980] Localizing Knowledge in Diffusion Transformers, Arman Zarei, Samyadeep Basu, Keivan Rezaei et al., NeurIPS 2025 · https://openreview.net/forum?id=SiBVbL7rsX
- [P-NEURIPS-fa1223] Obliviator Reveals the Cost of Nonlinear Guardedness in Concept Erasure, Ramin Akbari, Milad Afshari, Vishnu Boddeti, NeurIPS 2025 · https://openreview.net/forum?id=GcjpjIHDZn
- [P-2604.15829] Beyond Text Prompts: Precise Concept Erasure through Text-Image Collaboration, Jun Li, Lizhi Xiong, Ziqiang Li et al., arXiv 2026 · http://arxiv.org/abs/2604.15829v1
- [P-2604.16483] Dynamic Eraser for Guided Concept Erasure in Diffusion Models, Qinghui Gong, arXiv 2026 · http://arxiv.org/abs/2604.16483v1

### 클러스터 3 — 언러닝 평가·강건성 (6)
- [P-ICLR-2ee5d3] WaterDrum: Watermark-based Data-centric Unlearning Metric, Xinyang Lu, Xinyuan Niu, Gregory Kang Ruey Lau et al., ICLR 2025 · https://openreview.net/forum?id=5GVfneFvhq
- [P-ICLR-320a2e] Unlearning Isn't Invisible: Detecting Unlearning Traces in LLMs from Model Outputs, Yiwei Chen, Soumyadeep Pal, Yimeng Zhang et al., ICLR 2025 · https://openreview.net/forum?id=bqEnnzfhBZ
- [P-ICLR-d39c87] Randomized Antipodal Search Done Right for Data Pareto Improvement of LLM Unlearning, Ziwen Liu, Huawei Lin, Yide Ran et al., ICLR 2025 · https://openreview.net/forum?id=Xn6EnJZghu
- [P-NEURIPS-7f253a] Do LLMs Really Forget? Evaluating Unlearning  with Knowledge Correlation and Confidence Awareness, Rongzhe Wei, Peizhi Niu, Hans Hao-Hsun Hsu et al., NeurIPS 2025 · https://openreview.net/forum?id=BmEH70Wjcu
- [P-NEURIPS-a7f436] Keeping an Eye on LLM Unlearning: The Hidden Risk and Remedy, Jie Ren, Zhenwei DAI, Xianfeng Tang et al., NeurIPS 2025 · https://openreview.net/forum?id=MgN8Px0NA5
- [P-2604.15166] Class Unlearning via Depth-Aware Removal of Forget-Specific Directions, Arman Hatami, Romina Aalishah, Ilya E. Monosov, arXiv 2026 · http://arxiv.org/abs/2604.15166v1

### 기타 (클러스터 미분류) (5)
- [P-ICLR-c4447a] MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents, Zijian Zhou, Ao Qu, Zhaoxuan Wu et al., ICLR 2025 · https://openreview.net/forum?id=XY8AaxDSLb
- [P-ICLR-e4c8b4] Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions, Yuanzhe Hu, Yu Wang, Julian McAuley, ICLR 2025 · https://openreview.net/forum?id=DT7JyQC3MR
- [P-NEURIPS-52ca09] Enhancing the Maximum Effective Window for Long-Term Time Series Forecasting, Jiahui Zhang, Zhengyang Zhou, Wenjie Du et al., NeurIPS 2025 · https://openreview.net/forum?id=Gmwsy7TlFI
- [P-2604.20300] FSFM: A Biologically-Inspired Framework for Selective Forgetting of Agent Memory, Yingjie Gu, Wenjian Xiong, Liqiang Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.20300v2
- [P-2604.11306] Learning to Forget -- Hierarchical Episodic Memory for Lifelong Robot Deployment, Leonard Bärmann, Joana Plewnia, Alex Waibel et al., arXiv 2026 · http://arxiv.org/abs/2604.11306v1

---

## 메타 / 디버그
- model: claude-sonnet-4-6
- backend: cli
- matched_n: 50
- matched_total_before_cap: 233
- window_days: 365
