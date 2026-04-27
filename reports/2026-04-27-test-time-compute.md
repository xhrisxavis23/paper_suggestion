# Research Topic Suggestion — "test-time compute"

생성: 2026-04-27T04:17:52.979836+00:00
DB 윈도우: 2026-02-26 ~ 2026-04-27 (60d)
모델: claude-sonnet-4-6
매칭 논문: 80건
확장 키워드: ['test-time compute', 'test-time computation', 'inference-time compute', 'test-time scaling', 'inference scaling laws', 'chain-of-thought reasoning', 'thinking tokens', 'extended thinking', 'process reward model', 'best-of-n sampling', 'self-consistency decoding', 'reasoning budget']

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — 추론 과잉 억제
- **설명**: LLM이 답을 이미 결정한 뒤에도 불필요한 추론 토큰을 생성하는 과잉사고(overthinking) 현상을 진단하고, 조기 종료·단계별 가지치기·KV 캐시 증발 등으로 토큰 효율을 높이는 연구군.
- **빈도**: 7건
- **주차별**: 0 → 1 → 1 → 5
- **대표 논문**:
  - [P-2604.22266] Large Language Models Decide Early and Explain Later — Ayan Datta, Zhixue Zhao, Bhuvanesh Verma et al., arXiv 2026
  - [P-2604.18002] Neural Garbage Collection: Learning to Forget while Learning to Reason — Michael Y. Li, Jubayer Ibn Hamid, Emily B. Fox et al., arXiv 2026
  - [P-2604.17304] Efficient Test-Time Scaling via Temporal Reasoning Aggregation — Jiakun Li, Xingwei He, Kefan Li et al., arXiv 2026

### 클러스터 2 — 프로세스 보상 모델
- **설명**: 추론 단계별 정확도를 평가하는 프로세스 리워드 모델(PRM)을 설계·훈련·적용하여 Best-of-N 선택 및 검증 품질을 높이는 연구군.
- **빈도**: 10건
- **주차별**: 0 → 1 → 6 → 3
- **대표 논문**:
  - [P-2604.16535] SCATR: Simple Calibrated Test-Time Ranking — Divya Shyamal, Marta Knežević, Lan Tran et al., arXiv 2026
  - [P-2604.18547] FUSE: Ensembling Verifiers with Zero Labeled Data — Joonhyuk Lee, Virginia Ma, Sarah Zhao et al., arXiv 2026
  - [P-2604.09482] Process Reward Agents for Steering Knowledge-Intensive Reasoning — Jiwoong Sohn, Tomasz Sternal, Kenneth Styppa et al., arXiv 2026

### 클러스터 3 — 적응형 컴퓨트 배분
- **설명**: 쿼리 난이도에 따라 추론 예산을 동적으로 조절하거나, 계층적 캐스케이드·다중 에이전트 협의로 고비용 컴퓨트를 불확실한 입력에만 집중시키는 연구군.
- **빈도**: 9건
- **주차별**: 0 → 1 → 5 → 3
- **대표 논문**:
  - [P-2604.21018] Adaptive Test-Time Compute Allocation with Evolving In-Context Demonstrations — Bowen Zuo, Dongruo Zhou, Yinglun Zhu, arXiv 2026
  - [P-2604.14853] Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization — Zhiyuan Zhai, Bingcong Li, Bingnan Xiao et al., arXiv 2026
  - [P-2604.12262] CascadeDebate: Multi-Agent Deliberation for Cost-Aware LLM Cascades — Raeyoung Chang, Dongwook Kwon, Jisoo Lee et al., arXiv 2026

### 클러스터 4 — 병렬 탐색·샘플링
- **설명**: Best-of-N, 트리 탐색, 다양성 보존 샘플링 등 복수의 추론 경로를 병렬 생성·집계하여 테스트 시점 성능을 확장하는 연구군.
- **빈도**: 11건
- **주차별**: 0 → 1 → 7 → 3
- **대표 논문**:
  - [P-2604.16529] Scaling Test-Time Compute for Agentic Coding — Joongwon Kim, Wannan Yang, Kelvin Niu et al., arXiv 2026
  - [P-2604.17288] Clover: A Neural-Symbolic Agentic Harness with Stochastic Tree-of-Thoughts for Verified RTL Repair — Zizhang Luo, Yansong Xu, Runlin Guo et al., arXiv 2026
  - [P-2604.15453] (1D) Ordered Tokens Enable Efficient Test-Time Search — Zhitong Gao, Parham Rezaei, Ali Cy et al., arXiv 2026

### 클러스터 5 — RL 훈련·신뢰성
- **설명**: RLVR·탐색적 정책 훈련이 테스트 시점 스케일링에 미치는 영향을 분석하고, 보상 해킹·인과성 결여 등 신뢰성 문제를 진단·개선하는 연구군.
- **빈도**: 11건
- **주차별**: 0 → 2 → 4 → 5
- **대표 논문**:
  - [P-2604.22074] Outcome Rewards Do Not Guarantee Verifiable or Causally Important Reasoning — Qinan Yu, Alexa Tartaglini, Peter Hase et al., arXiv 2026
  - [P-2604.19295] TEMPO: Scaling Test-time Training for Large Reasoning Models — Qingyang Zhang, Xinke Kong, Haitao Wu et al., arXiv 2026
  - [P-2604.09459] From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models — Chenchen Zhang, arXiv 2026

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap A — 클러스터 '추론 과잉 억제'와 '프로세스 보상 모델' 사이에 존재하는 갭: PRM 점수 수렴을 추론 종료 트리거로 활용하는 연구가 어느 클러스터
- **타입**: between-clusters
- **설명**: 클러스터 '추론 과잉 억제'와 '프로세스 보상 모델' 사이에 존재하는 갭: PRM 점수 수렴을 추론 종료 트리거로 활용하는 연구가 어느 클러스터에도 없다.
- **근거 논문**: P-2604.22266, P-2604.17304, P-2604.09482, P-2604.16535
- **Skeptic 검토**: ✓ 통과 — 가장 유사한 작업인 2604.18419('Knowing When to Quit')은 RL 프레임워크 내에서 학습된 가치 함수를 종료 기준으로 사용하지만, PRM 점수를 직접 수렴 신호로 사용하는 메커니즘과는 설계 원리가 다르다. 2604.09482(PRA)는 PRM을 단계 점수화에만 사용하고 종료 결정에는 연결하지 않음이 메타에서 명확히 확인된다.

### Gap C — LLM 에이전트가 태스크 해결에 결정적인 정보를 발견하고도 활용하지 못하는 '환경적 호기심 결여' 현상이 실증되었으나, 이를 해소하는 아키텍처·
- **타입**: single-shot
- **설명**: LLM 에이전트가 태스크 해결에 결정적인 정보를 발견하고도 활용하지 못하는 '환경적 호기심 결여' 현상이 실증되었으나, 이를 해소하는 아키텍처·훈련 방법이 메타DB에 없다.
- **근거 논문**: P-2604.17609
- **Skeptic 검토**: ✓ 통과 — 단일 논문 근거이며 '후속 작업 부재'라는 시점적 한계가 있으나, 클러스터 3·4의 병렬 스케일링 논문 어느 것도 이 구체적 실패 모드를 훈련/아키텍처 수준에서 다루지 않음이 메타에서 확인된다. 보존 가능.

### Gap D — 관계 항수(arity)·지식 전체 열거가 필요한 구조적 추론에서 추가 TTS가 성능을 개선하지 못한다는 한계가 4개 논문에서 수렴하지만, 표현 
- **타입**: recurring-limitation
- **설명**: 관계 항수(arity)·지식 전체 열거가 필요한 구조적 추론에서 추가 TTS가 성능을 개선하지 못한다는 한계가 4개 논문에서 수렴하지만, 표현 수준의 아키텍처적 해법이 없다.
- **근거 논문**: P-2604.12176, P-2604.17621, P-2604.09338, P-2604.14140
- **Skeptic 검토**: ✓ 통과 — 2604.12176·2604.09338 모두 명시적으로 'increased test-time compute does not resolve this failure'라고 기술하고 있어 (a)(b) 사유로 거부할 근거가 메타 내에 없다. 4개 논문의 수렴이 갭을 뒷받침한다.

### Gap E — 추론 능력 훈련(RLVR)과 컴퓨트 배분 결정을 end-to-end RL로 공동 학습하는 연구가 어느 클러스터에도 없다.
- **타입**: between-clusters
- **설명**: 추론 능력 훈련(RLVR)과 컴퓨트 배분 결정을 end-to-end RL로 공동 학습하는 연구가 어느 클러스터에도 없다.
- **근거 논문**: P-2604.14853, P-2604.08369, P-2604.22074, P-2604.19295
- **Skeptic 검토**: ✓ 통과 — 2604.18002(NGC)가 추론과 KV캐시 관리를 end-to-end RL로 공동 최적화하지만 이는 메모리 관리이지 컴퓨트 예산 배분이 아니다. 2604.14853은 '2-stage pipeline'임을 논문 자체에서 명시하고, 2604.08369는 training-free로 설계 원리가 다르다.

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap B** — 포스트 트레이닝이 출력 다양성을 붕괴시켜 TTS의 전제를 훼손하지만 훈련 시점에서 다양성과 정확도를 동시에 달성하는 방법론이 없다는 주장. · 거부 사유: 갭 후보가 직접 증거 논문으로 제시한 arxiv:2604.17654(Poly-EPO)가 이 갭을 이미 다루고 있다. 추상에서 'explicitly encourages optimistic exploration... preserves greater diversity in model generations... improves pass@k coverage'라고 명시하며, 훈련 시점에서 탐색(다양성)과 활용(정확도)을 공동 최적화하는 포스트트레이닝 방법을 제안한다. 갭 설명의 핵심 조건('훈련 시점에서 다양성과 정확도를 동시에 달성하는 방법론이 없다')이 증거 논문 집합 내에서 직접 반박된다. '이미 붕괴된 다양성 복원'이라는 재해석으로 갭을 구출하려 해도, 그 새 갭은 원 설명에 기재되지 않았고 메타에서 뒷받침하는 추가 증거도 없다 [arxiv:2604.17654].

</details>

## 3. 연구 제안 (Proposer)

### 제안 1 — PRM-HALT
**가설**: 추론 단계별 PRM 점수의 슬라이딩 분산이 설정된 임계값 이하로 수렴하는 시점은 LLM의 최종 답이 안정화된 시점과 유의미하게 일치하며, 이를 조기 종료 트리거로 활용하면 정확도 손실 2% 이내에서 추론 토큰을 25% 이상 절감할 수 있다.
**메우는 갭**: A
**접근**: 추론 생성 중 매 K 스텝마다 기존 PRM을 호출해 단계 점수를 수집하고, 최근 W개 점수의 슬라이딩 분산이 ε 이하로 떨어지면 생성을 즉시 종료한다. PRM 호출 비용을 줄이기 위해 캐시된 중간 레이어 표현을 재사용하는 경량 프록시 PRM을 병용하며, 훈련은 불필요하다. SCATR 방식의 소형 보정 집합으로 ε와 W를 태스크별로 자동 설정한다.
**Baselines**: TRACE (arxiv:2604.17304), SCATR (arxiv:2604.16535), SAT (arxiv:2604.07922), PRA (arxiv:2604.09482), GSM8K, MATH, AIME
**예상 기여**: PRM 점수 수렴을 최초로 추론 조기 종료의 의미론적 트리거로 체계화하여, 단순 답변 일관성 기반 방법보다 종료 오판율을 낮춘다. 훈련이 불필요해 임의의 오픈소스 PRM·추론 모델 쌍에 플러그인 방식으로 적용 가능하다.
**참고**: P-2604.22266, P-2604.17304, P-2604.09482, P-2604.16535, P-2604.07922

### 제안 2 — PRM-GATE
**가설**: PRM 단계 점수 시퀀스를 입력으로 학습된 경량 게이팅 헤드는, 단순 분산 임계값 휴리스틱보다 낮은 정확도 손실로 더 많은 추론 토큰을 절감하는 수렴 분류기가 될 수 있다.
**메우는 갭**: A
**접근**: 기존 PRM 위에 1-레이어 바이너리 분류 헤드를 부착하고, 각 추론 단계에서 '이후 추가 추론이 답을 바꾸지 않을 확률'을 예측하도록 학습한다. 레이블은 forced answer completion(arxiv:2604.22266)과 동일한 방식으로 중간 prefix에서 답을 강제 추출해 이후 답 변경 여부를 자동 생성하므로 수동 주석이 불필요하다. 추론 시 게이팅 점수가 δ를 초과하면 종료하며, δ는 Lagrangian 예산 제약(arxiv:2604.14853)을 참조해 정확도-토큰 트레이드오프로 자동 조정한다.
**Baselines**: Knowing When to Quit (arxiv:2604.18419), TRACE (arxiv:2604.17304), SCATR (arxiv:2604.16535), CPMI (arxiv:2604.10660), Qwen2.5-7B, MATH, GPQA Diamond
**예상 기여**: PRM을 단순 점수 제공자에서 종료 결정자로 역할 확장하는 최초의 훈련 기반 방법을 제안한다. 레이블 자동 생성 파이프라인 덕분에 임의 추론 데이터셋에서 게이팅 헤드를 훈련할 수 있어 도메인 확장성이 높다.
**참고**: P-2604.22266, P-2604.18419, P-2604.16535, P-2604.10660, P-2604.14853

### 제안 3 — EXPLOIT-STEER
**가설**: 에이전트 롤아웃 중 예상치 못한 고관련성 관찰(anomalous-relevant observation)을 탐지하고 그 활용 여부를 평가하는 보조 보상을 RL 훈련에 추가하면, 환경적 호기심 결여 현상이 완화되어 태스크 성공률이 유의미하게 향상된다.
**메우는 갭**: C
**접근**: 관찰 토큰과 태스크 목표 임베딩 간의 실시간 의미적 유사도를 모니터링하는 경량 이상 감지 모듈을 에이전트 스캐폴드에 부착한다. 이 모듈이 '기대 유사도 분포 상위 5% 이상'의 관찰을 감지하면, 에이전트가 해당 발견을 이후 행동 계획에 명시적으로 반영했는지 여부를 평가하는 보조 보상 신호를 부여한다. GRPO 기반 정책 최적화로 주 태스크 보상과 보조 보상을 공동 학습하며, 이상 감지 모듈은 frozen 상태로 유지해 임의의 기존 LLM 에이전트에 플러그인 적용 가능하도록 한다.
**Baselines**: TrACE (arxiv:2604.08369), Three Roles One Model (arxiv:2604.11465), AggAgent (arxiv:2604.11753), AppWorld, Terminal-Bench, SWE-Bench Verified
**예상 기여**: 환경적 호기심 결여를 아키텍처 수정 없이 보조 보상만으로 해소하는 최초의 훈련 방법을 제시한다. 이상 감지 기반 보조 보상은 재현 가능한 정량적 레이블 생성이 가능해, 기존 에이전트 벤치마크에서의 실패 원인 분석 도구로도 활용된다.
**참고**: P-2604.17609, P-2604.08369, P-2604.11753, P-2604.22074, P-2604.11465

### 제안 4 — ARITY-BIND
**가설**: 관계 항수(arity)에 비례하여 독립적 엔티티 바인딩 슬롯을 명시적으로 할당하는 n-튜플 어텐션 레이어를 기존 트랜스포머에 추가하면, 추가 TTS로 해소되지 않았던 고차 관계 추론 실패율이 유의미하게 감소한다.
**메우는 갭**: D
**접근**: 각 어텐션 헤드에 'arity slot' 위치 인코딩을 도입해 헤드 k가 항수 k의 관계 바인딩을 전담하도록 구조화한다. 학습 데이터는 PDDL 기반 계획 문제에서 자동 생성된 다항식 관계 샘플(arxiv:2604.17957)과 KnowledgeBerg·REL·Spatial-Gym 벤치마크 데이터를 혼합해 구성한다. 기존 트랜스포머 가중치를 고정하고 arity-aware 레이어만 학습하므로 추가 파라미터 수를 전체의 3% 이내로 제한한다.
**Baselines**: KnowledgeBerg (arxiv:2604.17621), REL (arxiv:2604.12176), Spatial-Gym (arxiv:2604.09338), LongCoT (arxiv:2604.14140), Qwen3-14B, GPT-4o
**예상 기여**: 고차 관계 추론 실패가 컴퓨트 부족이 아닌 표현 수준의 구조적 문제임을 아키텍처 개입을 통해 최초 검증한다. 소수 파라미터 추가만으로 TTS 대비 동등 이상의 성능을 달성하면, compute-efficient 정확도 향상의 대안 경로를 제시한다.
**참고**: P-2604.12176, P-2604.17621, P-2604.09338, P-2604.14140, P-2604.17957

### 제안 5 — UNIFY-RL
**가설**: 추론 품질과 단계별 컴퓨트 예산 배분을 단일 RL 정책으로 end-to-end 공동 학습하면, 두 단계 파이프라인보다 동일한 총 토큰 예산 내에서 더 높은 정확도를 달성할 수 있다.
**메우는 갭**: E
**접근**: 토큰 생성과 '계속/중단' 이진 행동을 동일한 정책 네트워크에서 공동 샘플링하는 통합 행동 공간을 설계한다. 보상은 정답 여부(outcome reward)와 소비 토큰 수에 대한 비용 페널티의 가중 합으로 구성하며, TEMPO의 EM 기반 재보정(arxiv:2604.19295)을 주기적으로 적용해 보상 드리프트를 방지한다. CIR·SR 보조 보상(arxiv:2604.22074)을 통합해 추론 인과성이 낮은 단계에서 조기 중단을 촉진한다.
**Baselines**: TEMPO (arxiv:2604.19295), Adaptive TTS via Constrained Policy Optimization (arxiv:2604.14853), TrACE (arxiv:2604.08369), GRPO, Qwen2.5-7B, MATH, AIME, GPQA Diamond
**예상 기여**: 추론 능력 훈련과 동적 컴퓨트 배분을 분리하지 않는 최초의 통합 RL 프레임워크를 제안한다. 두 목표의 공동 최적화가 상충하지 않고 시너지를 낼 수 있음을 실험적으로 검증함으로써, 테스트 시점 효율화를 훈련 시점에 내재화하는 새로운 연구 방향을 개척한다.
**참고**: P-2604.14853, P-2604.08369, P-2604.22074, P-2604.19295, P-2604.09459

## 4. 참고문헌 (메타DB 기반)

### 클러스터 1 — 추론 과잉 억제 (7)
- [P-2604.22266] Large Language Models Decide Early and Explain Later, Ayan Datta, Zhixue Zhao, Bhuvanesh Verma et al., arXiv 2026 · http://arxiv.org/abs/2604.22266v1
- [P-2604.10739] When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling, Shu Zhou, Rui Ling, Junan Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.10739v1
- [P-2604.17304] Efficient Test-Time Scaling via Temporal Reasoning Aggregation, Jiakun Li, Xingwei He, Kefan Li et al., arXiv 2026 · http://arxiv.org/abs/2604.17304v1
- [P-2604.07922] SAT: Balancing Reasoning Accuracy and Efficiency with Stepwise Adaptive Thinking, Weiyang Huang, Xuefeng Bai, Kehai Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.07922v1
- [P-2604.18419] Knowing When to Quit: A Principled Framework for Dynamic Abstention in LLM Reasoning, Hen Davidov, Nachshon Cohen, Oren Kalinsky et al., arXiv 2026 · http://arxiv.org/abs/2604.18419v1
- [P-2604.18002] Neural Garbage Collection: Learning to Forget while Learning to Reason, Michael Y. Li, Jubayer Ibn Hamid, Emily B. Fox et al., arXiv 2026 · http://arxiv.org/abs/2604.18002v1
- [P-2604.20090] Less Languages, Less Tokens: An Efficient Unified Logic Cross-lingual Chain-of-Thought Reasoning Framework, Chenyuan Zhang, Qiguang Chen, Xie Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.20090v1

### 클러스터 2 — 프로세스 보상 모델 (10)
- [P-2604.18547] FUSE: Ensembling Verifiers with Zero Labeled Data, Joonhyuk Lee, Virginia Ma, Sarah Zhao et al., arXiv 2026 · http://arxiv.org/abs/2604.18547v1
- [P-2604.17957] Process Reward Models Meet Planning: Generating Precise and Scalable Datasets for Step-Level Rewards, Raffaele Pisano, Roberto Navigli, arXiv 2026 · http://arxiv.org/abs/2604.17957v1
- [P-2604.16535] SCATR: Simple Calibrated Test-Time Ranking, Divya Shyamal, Marta Knežević, Lan Tran et al., arXiv 2026 · http://arxiv.org/abs/2604.16535v2
- [P-2604.16004] AgentV-RL: Scaling Reward Modeling with Agentic Verifier, Jiazheng Zhang, Ziche Fu, Zhiheng Xi et al., arXiv 2026 · http://arxiv.org/abs/2604.16004v1
- [P-2604.13197] Unleashing Implicit Rewards: Prefix-Value Learning for Distribution-Level Optimization, Shiping Gao, Hongzhan Chen, Xiaojun Quan et al., arXiv 2026 · http://arxiv.org/abs/2604.13197v1
- [P-2604.09482] Process Reward Agents for Steering Knowledge-Intensive Reasoning, Jiwoong Sohn, Tomasz Sternal, Kenneth Styppa et al., arXiv 2026 · http://arxiv.org/abs/2604.09482v1
- [P-2604.10660] Efficient Process Reward Modeling via Contrastive Mutual Information, Nakyung Lee, Sangwoo Hong, Jungwoo Lee, arXiv 2026 · http://arxiv.org/abs/2604.10660v1
- [P-2604.10701] Bringing Value Models Back: Generative Critics for Value Modeling in LLM Reinforcement Learning, Zikang Shan, Han Zhong, Liwei Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.10701v1
- [P-2604.17282] MedPRMBench: A Fine-grained Benchmark for Process Reward Models in Medical Reasoning, Lingyan Wu, Xiang Zheng, Weiqi Zhai et al., arXiv 2026 · http://arxiv.org/abs/2604.17282v1
- [P-2604.10034] AI Achieves a Perfect LSAT Score, Bonmu Ku, arXiv 2026 · http://arxiv.org/abs/2604.10034v1

### 클러스터 3 — 적응형 컴퓨트 배분 (9)
- [P-2604.21018] Adaptive Test-Time Compute Allocation with Evolving In-Context Demonstrations, Bowen Zuo, Dongruo Zhou, Yinglun Zhu, arXiv 2026 · http://arxiv.org/abs/2604.21018v1
- [P-2604.14853] Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization, Zhiyuan Zhai, Bingcong Li, Bingnan Xiao et al., arXiv 2026 · http://arxiv.org/abs/2604.14853v1
- [P-2604.12647] Adaptive Test-Time Scaling for Zero-Shot Respiratory Audio Classification, Tsai-Ning Wang, Herman Teun den Dekker, Lin-Lin Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.12647v1
- [P-2604.12262] CascadeDebate: Multi-Agent Deliberation for Cost-Aware LLM Cascades, Raeyoung Chang, Dongwook Kwon, Jisoo Lee et al., arXiv 2026 · http://arxiv.org/abs/2604.12262v1
- [P-2604.08369] Don't Overthink It: Inter-Rollout Action Agreement as a Free Adaptive-Compute Signal for LLM Agents, Khushal Sethi, arXiv 2026 · http://arxiv.org/abs/2604.08369v1
- [P-2604.13521] C-voting: Confidence-Based Test-Time Voting without Explicit Energy Functions, Kenji Kubo, Shunsuke Kamiya, Masanori Koyama et al., arXiv 2026 · http://arxiv.org/abs/2604.13521v1
- [P-2604.17353] Hive: A Multi-Agent Infrastructure for Algorithm- and Task-Level Scaling, Zizhang Luo, Yuhao Luo, Youwei Xiao et al., arXiv 2026 · http://arxiv.org/abs/2604.17353v1
- [P-2604.11465] Three Roles, One Model: Role Orchestration at Inference Time to Close the Performance Gap Between Small and Large Agents, S. Aaron McClendon, Jorge Gallego-Feliciano, Stavros Zervoudakis et al., arXiv 2026 · http://arxiv.org/abs/2604.11465v2
- [P-2604.16913] The Cognitive Penalty: Ablating System 1 and System 2 Reasoning in Edge-Native SLMs for Decentralized Consensus, Syed Muhammad Aqdas Rizvi, arXiv 2026 · http://arxiv.org/abs/2604.16913v1

### 클러스터 4 — 병렬 탐색·샘플링 (11)
- [P-2604.15453] (1D) Ordered Tokens Enable Efficient Test-Time Search, Zhitong Gao, Parham Rezaei, Ali Cy et al., arXiv 2026 · http://arxiv.org/abs/2604.15453v1
- [P-2604.15614] Flexible Empowerment at Reasoning with Extended Best-of-N Sampling, Taisuke Kobayashi, arXiv 2026 · http://arxiv.org/abs/2604.15614v1
- [P-2604.16931] Playing Psychic: Using Thought Trees to Predict Reasoning Models Accuracy on Coding Tasks, Jiaxin Fang, Runyuan He, Sahil Bhatia et al., arXiv 2026 · http://arxiv.org/abs/2604.16931v1
- [P-2604.17288] Clover: A Neural-Symbolic Agentic Harness with Stochastic Tree-of-Thoughts for Verified RTL Repair, Zizhang Luo, Yansong Xu, Runlin Guo et al., arXiv 2026 · http://arxiv.org/abs/2604.17288v1
- [P-2604.09921] A Tale of Two Temperatures: Simple, Efficient, and Diverse Sampling from Diffusion Language Models, Theo X. Olausson, Metod Jazbec, Xi Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.09921v1
- [P-2604.16027] Where does output diversity collapse in post-training?, Constantinos Karouzos, Xingwei Tan, Nikolaos Aletras, arXiv 2026 · http://arxiv.org/abs/2604.16027v1
- [P-2604.19730] FASTER: Value-Guided Sampling for Fast RL, Perry Dong, Alexander Swerdlow, Dorsa Sadigh et al., arXiv 2026 · http://arxiv.org/abs/2604.19730v1
- [P-2604.16529] Scaling Test-Time Compute for Agentic Coding, Joongwon Kim, Wannan Yang, Kelvin Niu et al., arXiv 2026 · http://arxiv.org/abs/2604.16529v1
- [P-2604.11753] Agentic Aggregation for Parallel Scaling of Long-Horizon Agentic Tasks, Yoonsang Lee, Howard Yen, Xi Ye et al., arXiv 2026 · http://arxiv.org/abs/2604.11753v1
- [P-2604.15259] Stability and Generalization in Looped Transformers, Asher Labovich, arXiv 2026 · http://arxiv.org/abs/2604.15259v2
- [P-2604.10734] Self-Correcting RAG: Enhancing Faithfulness via MMKP Context Selection and NLI-Guided MCTS, Shijia Xu, Zhou Wu, Xiaolong Jia et al., arXiv 2026 · http://arxiv.org/abs/2604.10734v1

### 클러스터 5 — RL 훈련·신뢰성 (11)
- [P-2604.22074] Outcome Rewards Do Not Guarantee Verifiable or Causally Important Reasoning, Qinan Yu, Alexa Tartaglini, Peter Hase et al., arXiv 2026 · http://arxiv.org/abs/2604.22074v1
- [P-2604.19295] TEMPO: Scaling Test-time Training for Large Reasoning Models, Qingyang Zhang, Xinke Kong, Haitao Wu et al., arXiv 2026 · http://arxiv.org/abs/2604.19295v1
- [P-2604.17912] Learning to Correct: Calibrated Reinforcement Learning for Multi-Attempt Chain-of-Thought, Muhammed Emrullah Ildiz, Halil Alperen Gozeten, Ege Onur Taga et al., arXiv 2026 · http://arxiv.org/abs/2604.17912v1
- [P-2604.15149] LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking, Lukas Helff, Quentin Delfosse, David Steinmann et al., arXiv 2026 · http://arxiv.org/abs/2604.15149v1
- [P-2604.14140] LongCoT: Benchmarking Long-Horizon Chain-of-Thought Reasoning, Sumeet Ramesh Motwani, Daniel Nichols, Charles London et al., arXiv 2026 · http://arxiv.org/abs/2604.14140v1
- [P-2604.14265] Reinforcement Learning via Value Gradient Flow, Haoran Xu, Kaiwen Hu, Somayeh Sojoudi et al., arXiv 2026 · http://arxiv.org/abs/2604.14265v1
- [P-2604.06834] On the Step Length Confounding in LLM Reasoning Data Selection, Bing Wang, Rui Miao, Chen Shen et al., arXiv 2026 · http://arxiv.org/abs/2604.06834v1
- [P-2604.09459] From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models, Chenchen Zhang, arXiv 2026 · http://arxiv.org/abs/2604.09459v2
- [P-2604.17654] Poly-EPO: Training Exploratory Reasoning Models, Ifdita Hasan Orney, Jubayer Ibn Hamid, Shreya S Ramanujam et al., arXiv 2026 · http://arxiv.org/abs/2604.17654v1
- [P-2604.10693] FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning, Yuxi Sun, Aoqi Zuo, Haotian Xie et al., arXiv 2026 · http://arxiv.org/abs/2604.10693v2
- [P-2604.17794] Bridging the Reasoning Gap in Vietnamese with Small Language Models via Test-Time Scaling, Bui The Trung, Do Minh Duc, Nguyen Van Vinh et al., arXiv 2026 · http://arxiv.org/abs/2604.17794v1

### 기타 (클러스터 미분류) (32)
- [P-2604.22615] GazeVLA: Learning Human Intention for Robotic Manipulation, Chengyang Li, Kaiyi Xiong, Yuan Xu et al., arXiv 2026 · http://arxiv.org/abs/2604.22615v1
- [P-2604.21786] From Codebooks to VLMs: Evaluating Automated Visual Discourse Analysis for Climate Change on Social Media, Katharina Prasse, Steffen Jung, Isaac Bravo et al., arXiv 2026 · http://arxiv.org/abs/2604.21786v1
- [P-2604.21032] Unlocking Multi-Spectral Data for Multi-Modal Models with Guided Inputs and Chain-of-Thought Reasoning, Dahun Kim, Ganesh Satish Mallya, Anelia Angelova, arXiv 2026 · http://arxiv.org/abs/2604.21032v1
- [P-2604.19859] DR-Venus: Towards Frontier Edge-Scale Deep Research Agents with Only 10K Open Data, Venus Team, Sunhao Dai, Yong Deng et al., arXiv 2026 · http://arxiv.org/abs/2604.19859v1
- [P-2604.17621] KnowledgeBerg: Evaluating Systematic Knowledge Coverage and Compositional Reasoning in Large Language Models, Xiao Zhang, Qianru Meng, Yongjian Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.17621v1
- [P-2604.17182] Layer-wise MoE Routing Locality under Shared-Prefix Code Generation: Token-Identity Decomposition and Compile-Equivalent Fork Redundancy, Shun-ichiro Hayashi, Daichi Mukunoki, Tetsuya Hoshino et al., arXiv 2026 · http://arxiv.org/abs/2604.17182v1
- [P-2604.17609] Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity, Leon Engländer, Sophia Althammer, Ahmet Üstün et al., arXiv 2026 · http://arxiv.org/abs/2604.17609v1
- [P-2604.17319] E2E-GMNER: End-to-End Generative Grounded Multimodal Named Entity Recognition, Meng Zhang, Jinzhong Ning, Xiaolong Wu et al., arXiv 2026 · http://arxiv.org/abs/2604.17319v1
- [P-2604.16648] FRIGID: Scaling Diffusion-Based Molecular Generation from Mass Spectra at Training and Inference Time, Montgomery Bohde, Hongxuan Liu, Mrunali Manjrekar et al., arXiv 2026 · http://arxiv.org/abs/2604.16648v1
- [P-2604.15727] Structured Abductive-Deductive-Inductive Reasoning for LLMs via Algebraic Invariants, Sankalp Gilda, Shlok Gilda, arXiv 2026 · http://arxiv.org/abs/2604.15727v1
- [P-2604.15664] Stargazer: A Scalable Model-Fitting Benchmark Environment for AI Agents under Astrophysical Constraints, Xinge Liu, Terry Jingchen Zhang, Bernhard Schölkopf et al., arXiv 2026 · http://arxiv.org/abs/2604.15664v1
- [P-2604.15972] Weak-Link Optimization for Multi-Agent Reasoning and Collaboration, Haoyu Bian, Chaoning Zhang, Jiaquan Zhang et al., arXiv 2026 · http://arxiv.org/abs/2604.15972v1
- [P-2604.15385] Prompt-Driven Code Summarization: A Systematic Literature Review, Afia Farjana, Zaiyu Cheng, Antonio Mastropaolo, arXiv 2026 · http://arxiv.org/abs/2604.15385v1
- [P-2604.14910] Reward-Aware Trajectory Shaping for Few-step Visual Generation, Rui Li, Bingyu Li, Yuanzhi Liang et al., arXiv 2026 · http://arxiv.org/abs/2604.14910v2
- [P-2604.13804] Character Beyond Speech: Leveraging Role-Playing Evaluation in Audio Large Language Models via Reinforcement Learning, Dongjie Fu, Fangming Feng, Xize Cheng et al., arXiv 2026 · http://arxiv.org/abs/2604.13804v1
- [P-2604.12955] Modeling Copilots for Text-to-Model Translation, Serdar Kadioglu, Karthik Uppuluri, Akash Singirikonda, arXiv 2026 · http://arxiv.org/abs/2604.12955v2
- [P-2604.12176] Evaluating Relational Reasoning in LLMs with REL, Lukas Fesser, Yasha Ektefaie, Ada Fang et al., arXiv 2026 · http://arxiv.org/abs/2604.12176v1
- [P-2604.11784] ClawGUI: A Unified Framework for Training, Evaluating, and Deploying GUI Agents, Fei Tang, Zhiqiong Lu, Boxuan Zhang et al., arXiv 2026 · http://arxiv.org/abs/2604.11784v1
- [P-2604.11547] Eliciting Medical Reasoning with Knowledge-enhanced Data Synthesis: A Semi-Supervised Reinforcement Learning Approach, Haolin Li, Shuyang Jiang, Ruipeng Zhang et al., arXiv 2026 · http://arxiv.org/abs/2604.11547v1
- [P-2604.11177] Do Thought Streams Matter? Evaluating Reasoning in Gemini Vision-Language Models for Video Scene Understanding, Shivam Sharma, Sankalp Nagaonkar, Ashish Choithani et al., arXiv 2026 · http://arxiv.org/abs/2604.11177v1
- [P-2604.11025] Test-time Scaling over Perception: Resolving the Grounding Paradox in Thinking with Images, Zheng Jiang, Yiming Chen, Nan He et al., arXiv 2026 · http://arxiv.org/abs/2604.11025v1
- [P-2604.10539] IceCache: Memory-efficient KV-cache Management for Long-Sequence LLMs, Yuzhen Mao, Qitong Wang, Martin Ester et al., arXiv 2026 · http://arxiv.org/abs/2604.10539v1
- [P-2604.10556] Lost in Diffusion: Uncovering Hallucination Patterns and Failure Modes in Diffusion Large Language Models, Zhengnan Guo, Fei Tan, arXiv 2026 · http://arxiv.org/abs/2604.10556v1
- [P-2604.10425] DiningBench: A Hierarchical Multi-view Benchmark for Perception and Reasoning in the Dietary Domain, Song Jin, Juntian Zhang, Xun Zhang et al., arXiv 2026 · http://arxiv.org/abs/2604.10425v1
- [P-2604.09494] RecaLLM: Addressing the Lost-in-Thought Phenomenon with Explicit In-Context Retrieval, Kyle Whitecross, Negin Rahimi, arXiv 2026 · http://arxiv.org/abs/2604.09494v1
- [P-2604.09338] Mind the Gap Between Spatial Reasoning and Acting! Step-by-Step Evaluation of Agents With Spatial-Gym, Lars Benedikt Kaesberg, Tianyu Yang, Niklas Bauer et al., arXiv 2026 · http://arxiv.org/abs/2604.09338v1
- [P-2604.08879] GRASP: Grounded CoT Reasoning with Dual-Stage Optimization for Multimodal Sarcasm Target Identification, Faxian Wan, Xiaocui Yang, Yifan Cao et al., arXiv 2026 · http://arxiv.org/abs/2604.08879v1
- [P-2604.08425] Learning Who Disagrees: Demographic Importance Weighting for Modeling Annotator Distributions with DiADEM, Samay U. Shetty, Tharindu Cyril Weerasooriya, Deepak Pandita et al., arXiv 2026 · http://arxiv.org/abs/2604.08425v1
- [P-2604.07944] On-Policy Distillation of Language Models for Autonomous Vehicle Motion Planning, Amirhossein Afsharrad, Amirhesam Abedsoltan, Ahmadreza Moradipari et al., arXiv 2026 · http://arxiv.org/abs/2604.07944v1
- [P-2604.08516] MolmoWeb: Open Visual Web Agent and Open Data for the Open Web, Tanmay Gupta, Piper Wolters, Zixian Ma et al., arXiv 2026 · http://arxiv.org/abs/2604.08516v1
- [P-2604.07277] Android Coach: Improve Online Agentic Training Efficiency with Single State Multiple Actions, Guo Gan, Yuxuan Ding, Cong Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.07277v1
- [P-2604.07415] SubSearch: Intermediate Rewards for Unsupervised Guided Reasoning in Complex Retrieval, Roxana Petcu, Evangelos Kanoulas, Maarten de Rijke, arXiv 2026 · http://arxiv.org/abs/2604.07415v1

---

## 메타 / 디버그
- model: claude-sonnet-4-6
- backend: cli
- matched_n: 80
- matched_total_before_cap: 250
- window_days: 60
