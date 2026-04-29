# Research Topic Suggestion — "jailbreaking"

생성: 2026-04-29T05:36:57.931542+00:00
DB 윈도우: 2025-09-01 ~ 2026-04-29 (240d)
모델: gemini-2.5-pro
매칭 논문: 100건
확장 키워드: ['llm jailbreak', 'prompt injection', 'adversarial prompt']

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — 에이전트 및 도구 사용 취약점
- **설명**: LLM이 외부 도구를 사용하거나, 웹·OS와 상호작용하는 자율 에이전트로 작동할 때 발생하는 보안 위협을 다룹니다. 특히 신뢰할 수 없는 외부 정보(웹페이지, 파일, 도구 출력)를 통해 에이전트를 조종하는 간접 프롬프트 인젝션(Indirect Prompt Injection)과 에이전트 프레임워크 자체의 구조적 취약점에 대한 연구가 중심을 이룹니다.
- **빈도**: 35건
- **분기별 (≈60d씩, 오래된→최근)**: 4 → 0 → 0 → 31
- **대표 논문**:
  - [P-ICLR-7222b8] RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments — Zeyi Liao, Jaylen Jones, Linxi Jiang et al., ICLR 2025
  - [P-2604.11790] ClawGuard: A Runtime Security Framework for Tool-Augmented LLM Agents Against Indirect Prompt Injection — Wei Zhao, Zhe Li, Peixin Zhang et al., arXiv 2026
  - [P-2603.27517] A Systematic Taxonomy of Security Vulnerabilities in the OpenClaw AI Agent Framework — Surada Suwansathit, Yuxuan Zhang, Guofei Gu, arXiv 2026

### 클러스터 2 — 자동화된 공격 기법 및 최적화
- **설명**: 수동적인 프롬프트 엔지니어링을 넘어, 효과적인 탈옥(Jailbreak) 공격을 자동으로 생성하고 최적화하는 방법론을 연구합니다. 경사하강법, 진화 알고리즘, 메타 학습, 퍼징(fuzzing) 등 다양한 기법을 활용하거나 다른 LLM을 공격자 에이전트로 사용하여 새로운 공격 벡터를 탐색합니다.
- **빈도**: 10건
- **분기별 (≈60d씩, 오래된→최근)**: 4 → 0 → 0 → 6
- **대표 논문**:
  - [P-ICLR-e0c25a] Align to Misalign: Automatic LLM Jailbreak with Meta-Optimized LLM Judges — Hamin Koo, Minseon Kim, Jaehyung Kim, ICLR 2025
  - [P-2603.24511] Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs — Alexander Panfilov, Peter Romov, Igor Shilov et al., arXiv 2026
  - [P-ICLR-9fe35a] Obscure but Effective: Classical Chinese Jailbreak Prompt Optimization via Bio-Inspired Search — Xun Huang, Simeng Qin, Xiaoshuang Jia et al., ICLR 2025

### 클러스터 3 — 멀티모달 프롬프트 인젝션
- **설명**: 텍스트뿐만 아니라 이미지, 오디오 등 비언어적 데이터를 통해 모델을 공격하는 기법을 다룹니다. 이미지에 보이지 않게 악성 프롬프트를 삽입(Visual Prompt Injection), 텍스트를 이미지로 렌더링하여 공격(Typographic Attack), 오디오 신호에 명령을 숨기는 등 멀티모달 모델의 새로운 공격 표면을 탐구합니다.
- **빈도**: 13건
- **분기별 (≈60d씩, 오래된→최근)**: 2 → 0 → 0 → 11
- **대표 논문**:
  - [P-ICLR-70053c] VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents — Tri Cao, Bennett Lim, Yue Liu et al., ICLR 2025
  - [P-2604.14604] Hijacking Large Audio-Language Models via Context-Agnostic and Imperceptible Auditory Prompt Injection — Meng Chen, Kun Wang, Li Lu et al., arXiv 2026
  - [P-ICLR-08d850] Misaligned Roles, Misplaced Images: Structural Input Perturbations Expose Multimodal Alignment Blind Spots — Erfan Shayegani, G M Shahariar, Sara Abdali et al., ICLR 2025

### 클러스터 4 — 런타임 방어 및 아키텍처 개선
- **설명**: 탈옥 및 프롬프트 인젝션 공격을 탐지하고 방어하기 위한 기술적 해결책을 제안합니다. 모델의 내부 활성화 값을 모니터링하여 이상 행위를 탐지하거나, 추론 시점에 안전한 방향으로 출력을 유도하는 기법, 혹은 명령어와 데이터를 근본적으로 분리하는 새로운 모델 아키텍처 설계 등을 포함합니다.
- **빈도**: 24건
- **분기별 (≈60d씩, 오래된→최근)**: 8 → 0 → 0 → 16
- **대표 논문**:
  - [P-ICLR-206ec5] ASIDE: Architectural Separation of Instructions and Data in Language Models — Egor Zverev, Evgenii Kortukov, Alexander Panfilov et al., ICLR 2025
  - [P-2604.24542] Layerwise Convergence Fingerprints for Runtime Misbehavior Detection in Large Language Models — Nay Myat Min, Long H. Pham, Jun Sun, arXiv 2026

### 클러스터 5 — 벤치마크 및 평가 체계 구축
- **설명**: 다양한 탈옥 공격과 방어 기법의 성능을 공정하고 신뢰성 있게 측정하기 위한 표준화된 벤치마크, 데이터셋, 평가 플랫폼을 구축하는 연구입니다. 일관성 없는 평가로 인한 혼란을 줄이고, 특정 시나리오(에이전트, 멀티모달 등)에 특화된 안전성 평가 기준을 제시합니다.
- **빈도**: 7건
- **분기별 (≈60d씩, 오래된→최근)**: 2 → 0 → 0 → 5
- **대표 논문**:
  - [P-ICLR-fd7e76] GuidedBench: Measuring and Mitigating the Evaluation Discrepancies of In-the-wild LLM Jailbreak Methods — Ruixuan Huang, Xunguang Wang, Zongjie Li et al., ICLR 2025
  - [P-2604.08499] PIArena: A Platform for Prompt Injection Evaluation — Runpeng Geng, Chenlong Yin, Yanting Wang et al., arXiv 2026
  - [P-2604.15415] HarmfulSkillBench: How Do Harmful Skills Weaponize Your Agents? — Yukun Jiang, Yage Zhang, Michael Backes et al., arXiv 2026

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap B — 다수의 방어 기법 논문에서 보안성과 유용성(utility) 간의 트레이드오프가 반복적으로 언급됩니다. 강력한 보안 조치를 적용할수록 모델의 정상
- **타입**: recurring-limitation
- **설명**: 다수의 방어 기법 논문에서 보안성과 유용성(utility) 간의 트레이드오프가 반복적으로 언급됩니다. 강력한 보안 조치를 적용할수록 모델의 정상적인 업무 수행 능력이 저하되거나, 에이전트의 자율성이 훼손되는 '자율성 세금(Autonomy Tax)' 문제가 발생합니다. 이는 안전을 위해 모델의 핵심 역량을 희생해야 하는 근본적인 딜레마를 시사합니다.
- **근거 논문**: P-ICLR-1a6d61, P-2603.19423
- **Skeptic 검토**: ✓ 통과 — 여러 방어 기법에서 반복적으로 한계점으로 지적되는 근본적인 문제로, 아직 해결책이 등장하지 않은 유효한 연구 갭입니다.

### Gap D — 고전 중국어를 활용하여 탈옥 공격을 시도한 연구는 LLM의 안전 장치가 특정 언어 및 문화권에 편중되어 있을 수 있다는 중요한 가능성을 제시했습
- **타입**: single-shot
- **설명**: 고전 중국어를 활용하여 탈옥 공격을 시도한 연구는 LLM의 안전 장치가 특정 언어 및 문화권에 편중되어 있을 수 있다는 중요한 가능성을 제시했습니다. 이 논문은 영어 중심의 데이터셋과 평가에서 벗어나 '드물거나 생소한 언어'가 새로운 공격 벡터가 될 수 있음을 보였습니다. 하지만 이러한 언어적, 문화적 맹점을 체계적으로 탐구하거나 다른 비주류 언어로 확장하는 후속 연구는 거의 보이지 않습니다.
- **근거 논문**: P-ICLR-9fe35a
- **Skeptic 검토**: ✓ 통과 — 제시된 증거 논문은 독창적인 공격 벡터를 제시했으나, 제공된 메타데이터 내에서 이를 확장하거나 다른 언어에 적용한 후속 연구가 없어 유효한 갭으로 판단됩니다.

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap A** — 자동화된 공격 기법(클러스터 2)과 런타임 방어(클러스터 4) 연구는 활발하지만, 이 둘 사이의 상호작용에 대한 연구는 부족합니다. 대부분의 방어 기법은 알려진 정적 공격 벤치마크에 대해 평가되지만, 공격자가 방어 기법의 존재를 인지하고 실시간으로 전략을 수정하는 '적응적 공격(adaptive attack)'에 대한 강건성은 거의 검증되지 않았습니다. 이는 방어 기술이 실제 위협 환경에서 얼마나 효과적일지에 대한 근본적인 의문을 남깁니다. · 거부 사유: (a) 다른 클러스터에서 이미 다룸. 런타임 방어(클러스터 4)와 벤치마크(클러스터 5) 클러스터에서 '적응적 공격'을 명시적으로 다루고 평가하는 다수의 논문이 존재합니다. [title:adaptive attacks on trusted monitors subvert ai control protocols]
- **Gap C** — 이미지나 오디오를 이용한 멀티모달 공격(클러스터 3) 연구는 매우 활발하게 진행되고 있으나, 이에 대응하는 방어 기술(클러스터 4) 연구는 상대적으로 부족합니다. 클러스터 4의 많은 방어 기법들은 주로 텍스트 기반 위협에 초점을 맞추고 있으며, 시각적/청각적 채널을 통해 들어오는 악성 입력을 탐지하거나 무력화하는 통합적인 방어 프레임워크는 드물게 제안됩니다. 멀티모달 모델의 공격 표면은 넓어졌지만, 방어는 여전히 단일 모달 중심적으로 이루어지고 있습니다. · 거부 사유: (a) 다른 클러스터에서 이미 다룸. 런타임 방어(클러스터 4)에는 VLM을 위한 프롬프트 튜닝 방어 기법이나 텍스트와 시각적 위협을 동시에 완화하는 모달 불가지론적(modal-agnostic) 방어 프레임워크가 이미 포함되어 있습니다. [arxiv:2604.06247]
- **Gap E** — LLM 에이전트의 취약점(클러스터 1)과 벤치마크 구축(클러스터 5)은 별개의 클러스터로 존재하지만, 두 영역을 결합한 동적이고 현실적인 에이전트 보안 평가 환경은 아직 초기 단계입니다. 다수의 에이전트 공격 연구는 특정 시나리오를 가정하고, 벤치마크는 정적 데이터셋에 의존하는 경향이 있습니다. 에이전트가 실제 웹/OS 환경과 상호작용하며 발생하는 다단계(multi-step) 취약점을 체계적으로 평가하고 재현할 수 있는 표준화된 플랫폼은 여전히 부족합니다. · 거부 사유: (a) 다른 클러스터에서 이미 다룸. 이 갭이 지적하는 '동적이고 현실적인 에이전트 보안 평가 환경 구축'은 정확히 벤치마크(클러스터 5)의 핵심 주제입니다. 해당 클러스터의 다수 논문들이 바로 이 문제를 해결하기 위해 제안되었습니다. [title:mcp security bench (msb): benchmarking attacks against model context protocol in llm agents]

</details>

## 3. 연구 제안 (Proposer)

### 제안 1 — ADAPT
**가설**: 강화학습을 통해 에이전트가 보안 정책과 태스크 완료율 사이의 최적 균형점을 동적으로 학습하면, 고정된 방어 정책보다 더 높은 자율성과 유용성을 동시에 달성할 수 있다.
**메우는 갭**: B
**접근**: 논문 'Optimizing Agent Planning for Security and Autonomy'에서 제안한 PRUDENTIA 에이전트와 자율성 측정 지표(HITL load, TCR@k)를 기반으로, 동적 보안-유용성 트레이드오프를 학습하는 강화학습(RL) 프레임워크를 구축한다. 에이전트의 보상 함수는 TCR@k(유용성)와 HITL load(자율성)를 결합하여 정의하며, 에이전트는 각 단계에서 더 엄격하거나 완화된 보안 정책을 선택하는 행동을 학습하여 '자율성 세금(Autonomy Tax)'을 최소화한다. 이는 기존 연구의 정적인 정책 적용 한계를 극복하는 것을 목표로 한다.
**Baselines**: PRUDENTIA, FIDES, AgentDojo, WASP
**예상 기여**: 상황에 따라 유연하게 보안 수준을 조절하는 에이전트를 제안하여 '자율성 세금' 문제를 완화한다. 이는 실용적인 에이전트 시스템에서 보안과 성능의 균형을 맞추는 새로운 패러다임을 제시하며, 고정된 방어 정책의 한계를 넘어선다.
**참고**: P-ICLR-1a6d61, P-2603.19423, P-2604.19657

### 제안 2 — LOTE
**가설**: LLM의 탈옥 성공률은 대상 언어의 통사적 복잡성, 어휘적 모호성, 그리고 훈련 데이터 내 희소성과 정량적으로 예측 가능한 상관관계를 가진다.
**메우는 갭**: D
**접근**: 논문 'Obscure but Effective: Classical Chinese Jailbreak...'의 접근법을 체계적으로 확장하여, 여러 비주류 및 고대 언어(예: 산스크리트어, 아람어, 룬 문자)의 언어학적 특성을 정량화하는 지표(구문 복잡도, 다의어 비율, 코퍼스 희소성)를 개발한다. 이 지표와 각 언어에서의 탈옥 성공률(ASR) 간의 상관관계를 분석하여, 어떤 언어적 특성이 LLM의 안전 얼라인먼트를 우회하는 데 효과적인지 예측하는 모델을 구축한다. CC-BOS에서 사용된 bio-inspired search 기법을 활용하여 여러 언어에 걸쳐 자동화된 공격 프롬프트를 생성 및 최적화한다.
**Baselines**: CC-BOS, GCG, AutoDAN, PAIR, AdvBench
**예상 기여**: 단일 언어의 취약점을 넘어, 어떤 '언어적 특성'이 LLM의 안전성을 약화시키는지에 대한 일반화된 원리를 밝혀낸다. 이는 다국어 LLM의 안전성 평가 및 강화를 위한 체계적인 프레임워크를 제공하고, 문화적, 언어적 맹점을 사전에 식별하는 데 기여할 것이다.
**참고**: P-ICLR-9fe35a, P-ICLR-e0c25a

### 제안 3 — TRUST-AXIS
**가설**: 입력 데이터의 출처(사용자, 신뢰된 도구, 외부 웹)에 따라 각기 다른 직교 변환을 임베딩에 적용하면, 이진 분류 방어보다 더 세밀한 보안 제어가 가능해져 유용성 저하를 최소화할 수 있다.
**메우는 갭**: B
**접근**: 논문 'ASIDE: Architectural Separation of Instructions and Data...'에서 제안한 단일 90도 회전 기법을 다차원 직교 변환으로 확장한다. 각 입력 토큰은 출처에 따라 '사용자 지시', '신뢰된 시스템 출력', '외부 검색 결과' 등 다수의 신뢰도 태그를 부여받고, 각 태그에 해당하는 고유한 직교 행렬로 임베딩이 변환된다. 이를 통해 모델은 내부적으로 정보의 신뢰도를 추적하며, 신뢰도가 낮은 정보에서 파생된 지시를 따를 확률을 낮추도록 학습되어, 전면적인 기능 차단 없이도 인젝션 공격을 억제한다.
**Baselines**: ASIDE, FIDES, CaMeL, AgentDojo, InjecAgent
**예상 기여**: 이진적인 '명령어/데이터' 구분을 넘어, 다차원적인 '신뢰도' 개념을 모델 아키텍처에 통합한다. 이는 보안성과 유용성 간의 트레이드오프, 즉 '자율성 세금' 문제를 완화하는 새로운 아키텍처 수준의 방어 메커니즘을 제시한다.
**참고**: P-ICLR-206ec5, P-ICLR-1a6d61, P-2603.19423

### 제안 4 — CODE-MIX
**가설**: 두 개 이상의 언어를 혼합한 코드 스위칭(Code-Switching) 프롬프트는 단일 언어 프롬프트에 비해 LLM의 안전성 필터를 더 효과적으로 우회할 수 있다.
**메우는 갭**: D
**접근**: 논문 'Obscure but Effective...'에서 영감을 받아, 코드 스위칭을 활용한 자동화된 탈옥 프롬프트 생성 프레임워크를 개발한다. 이 프레임워크는 유해한 지시문의 핵심 어휘를 훈련 데이터에 희소한 언어로 대체하거나, 문법 구조는 한 언어를 유지하면서 어휘는 다른 언어를 차용하는 방식으로 프롬프트를 생성한다. 다양한 언어 쌍(예: 영어-힌디어 'Hinglish', 영어-스페인어 'Spanglish')에 대한 탈옥 성공률을 측정하여, 코드 스위칭이 안전 얼라인먼트에 미치는 영향을 체계적으로 분석한다.
**Baselines**: CC-BOS, GCG, PAIR, TAP, AdvBench, JBB-Behaviors
**예상 기여**: 단일 비주류 언어를 넘어, 현실에서 빈번하게 사용되는 코드 스위칭 현상이 새로운 공격 벡터가 될 수 있음을 입증한다. 이는 다국어 환경에서의 LLM 안전성 강화 연구에 중요한 시사점을 제공하고, 보다 현실적인 언어 사용 패턴에 대한 모델의 강건성 평가 필요성을 제기한다.
**참고**: P-ICLR-9fe35a, P-ICLR-b78bdb

### 제안 5 — INNATE-GUARD
**가설**: 에이전트의 도구 사용 실행 추적(execution trace)에 내재된 안전 신호를 추론 시점에 모니터링하면, 방어용 미세조정으로 인한 역량 저하 없이 간접 프롬프트 인젝션을 효과적으로 방어할 수 있다.
**메우는 갭**: B
**접근**: 논문 'Any-Depth Alignment'에서 제시된, 모델의 재훈련 없이 추론 시점에 '보조 헤더 토큰'을 통해 내재적 안전성을 활성화하는 개념을 에이전트의 도구 호출 시퀀스로 확장한다. 도구 호출 전후의 내부 은닉 상태(hidden states)를 모니터링하여, 유해하거나 의도에서 벗어난 행동과 관련된 비정상적 활성화 패턴을 탐지하는 경량 선형 프로브를 훈련시킨다. 이 프로브는 'The Autonomy Tax'에서 지적한 방어 훈련으로 인한 에이전트 역량 붕괴(agent incompetence bias)를 회피하면서도 보안을 제공한다.
**Baselines**: ADA (Any-Depth Alignment), AgentDojo, SkillInject, MCPSafeBench, WASP
**예상 기여**: 모델 재학습으로 발생하는 '자율성 세금' 문제를 회피하는 새로운 에이전트 방어 패러다임을 제안한다. 이는 모델의 내재된 안전 표현을 활용하여 유용성을 해치지 않으면서도 보안을 강화하는 실용적인 방법을 제공하여 보안-유용성 트레이드오프를 근본적으로 개선할 수 있다.
**참고**: P-ICLR-b78bdb, P-2603.19423, P-ICLR-1a6d61

## 4. 참고문헌 (메타DB 기반)

### 클러스터 1 — 에이전트 및 도구 사용 취약점 (30)
- [P-ICLR-1a6d61] Optimizing Agent Planning for Security and Autonomy, Aashish Kolluri, Rishi Sharma, Manuel Costa et al., ICLR 2025 · https://openreview.net/forum?id=g0aVCDY3gS
- [P-ICLR-8b0fe9] Silent Leaks: Implicit Knowledge Extraction Attack on RAG Systems, Yuhao Wang, Wenjie Qu, Shengfang Zhai et al., ICLR 2025 · https://openreview.net/forum?id=zfVICPB5Sv
- [P-ICLR-c5f436] ChatInject: Abusing Chat Templates for Prompt Injection in LLM Agents, Hwan Chang, Yonghyun Jun, Hwanhee Lee, ICLR 2025 · https://openreview.net/forum?id=WVhgFSKniL
- [P-ICLR-7222b8] RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments, Zeyi Liao, Jaylen Jones, Linxi Jiang et al., ICLR 2025 · https://openreview.net/forum?id=yWwrgcBoK3
- [P-2604.24020] Poster: ClawdGo: Endogenous Security Awareness Training for Autonomous AI Agents, Jiaqi Li, Yang Zhao, Bin Sun et al., arXiv 2026 · http://arxiv.org/abs/2604.24020v1
- [P-2604.19657] An AI Agent Execution Environment to Safeguard User Data, Robert Stanley, Avi Verma, Lillian Tsai et al., arXiv 2026 · http://arxiv.org/abs/2604.19657v1
- [P-2604.17139] The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration, Jiayuan Liu, Shiyi Du, Weihua Du et al., arXiv 2026 · http://arxiv.org/abs/2604.17139v1
- [P-2604.16838] enclawed: A Configurable, Sector-Neutral Hardening Framework for Single-User AI Assistant Gateways, Alfredo Metere, arXiv 2026 · http://arxiv.org/abs/2604.16838v1
- [P-2604.16762] CapSeal: Capability-Sealed Secret Mediation for Secure Agent Execution, Shutong Jin, Ruiyi Guo, Ray C. C. Cheung, arXiv 2026 · http://arxiv.org/abs/2604.16762v1
- [P-2604.11806] Detecting Safety Violations Across Many Agent Traces, Adam Stein, Davis Brown, Hamed Hassani et al., arXiv 2026 · http://arxiv.org/abs/2604.11806v1
- [P-2604.11790] ClawGuard: A Runtime Security Framework for Tool-Augmented LLM Agents Against Indirect Prompt Injection, Wei Zhao, Zhe Li, Peixin Zhang et al., arXiv 2026 · http://arxiv.org/abs/2604.11790v1
- [P-2604.10577] The Blind Spot of Agent Safety: How Benign User Instructions Expose Critical Vulnerabilities in Computer-Use Agents, Xuwei Ding, Skylar Zhai, Linxin Song et al., arXiv 2026 · http://arxiv.org/abs/2604.10577v2 · also_in: hf
- [P-2604.10286] STARS: Skill-Triggered Audit for Request-Conditioned Invocation Safety in Agent Systems, Guijia Zhang, Shu Yang, Xilin Gong et al., arXiv 2026 · http://arxiv.org/abs/2604.10286v1
- [P-2604.09378] BadSkill: Backdoor Attacks on Agent Skills via Model-in-Skill Poisoning, Guiyao Tie, Jiawen Shi, Pan Zhou et al., arXiv 2026 · http://arxiv.org/abs/2604.09378v1
- [P-2604.06550] SkillSieve: A Hierarchical Triage Framework for Detecting Malicious AI Agent Skills, Yinghan Hou, Zongyou Yang, arXiv 2026 · http://arxiv.org/abs/2604.06550v1
- [P-2604.04561] Mapping the Exploitation Surface: A 10,000-Trial Taxonomy of What Makes LLM Agents Exploit Vulnerabilities, Charafeddine Mouzouni, arXiv 2026 · http://arxiv.org/abs/2604.04561v1
- [P-2604.04426] ShieldNet: Network-Level Guardrails against Emerging Supply-Chain Injections in Agentic Systems, Zhuowen Yuan, Zhaorun Chen, Zhen Xiang et al., arXiv 2026 · http://arxiv.org/abs/2604.04426v1
- [P-2604.03870] Your Agent is More Brittle Than You Think: Uncovering Indirect Injection Vulnerabilities in Agentic LLMs, Wenhui Zhu, Xuanzhao Dong, Xiwen Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.03870v1
- [P-2604.03070] Credential Leakage in LLM Agent Skills: A Large-Scale Empirical Study, Zhihao Chen, Ying Zhang, Yi Liu et al., arXiv 2026 · http://arxiv.org/abs/2604.03070v1
- [P-2604.02954] LogicPoison: Logical Attacks on Graph Retrieval-Augmented Generation, Yilin Xiao, Jin Chen, Qinggang Zhang et al., arXiv 2026 · http://arxiv.org/abs/2604.02954v1
- [P-2603.28166] Evaluating Privilege Usage of Agents with Real-World Tools, Quan Zhang, Lianhang Fu, Lvsi Lian et al., arXiv 2026 · http://arxiv.org/abs/2603.28166v2
- [P-2603.28013] Kill-Chain Canaries: Stage-Level Tracking of Prompt Injection Across Attack Surfaces and Model Safety Tiers, Haochuan Kevin Wang, Zechen Zhang, arXiv 2026 · http://arxiv.org/abs/2603.28013v3
- [P-2603.27517] A Systematic Taxonomy of Security Vulnerabilities in the OpenClaw AI Agent Framework, Surada Suwansathit, Yuxuan Zhang, Guofei Gu, arXiv 2026 · http://arxiv.org/abs/2603.27517v1
- [P-2603.24203] Invisible Threats from Model Context Protocol: Generating Stealthy Injection Payload via Tree-based Adaptive Search, Yulin Shen, Xudong Pan, Geng Hong et al., arXiv 2026 · http://arxiv.org/abs/2603.24203v1
- [P-2603.23791] The Cognitive Firewall:Securing Browser Based AI Agents Against Indirect Prompt Injection Via Hybrid Edge Cloud Defense, Qianlong Lan, Anuj Kaul, arXiv 2026 · http://arxiv.org/abs/2603.23791v1
- [P-2603.23064] Mind Your HEARTBEAT! Claw Background Execution Inherently Enables Silent Memory Pollution, Yechao Zhang, Shiqian Zhao, Jie Zhang et al., arXiv 2026 · http://arxiv.org/abs/2603.23064v3
- [P-2603.19974] Trojan's Whisper: Stealthy Manipulation of OpenClaw through Injected Bootstrapped Guidance, Fazhong Liu, Zhuoyan Chen, Tu Lan et al., arXiv 2026 · http://arxiv.org/abs/2603.19974v1
- [P-2603.20320] The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents, Shasha Yu, Fiona Carroll, Barry L. Bentley, arXiv 2026 · http://arxiv.org/abs/2603.20320v1
- [P-2603.19469] A Framework for Formalizing LLM Agent Security, Vincent Siu, Jingxuan He, Kyle Montgomery et al., arXiv 2026 · http://arxiv.org/abs/2603.19469v1
- [P-2603.19423] The Autonomy Tax: Defense Training Breaks LLM Agents, Shawn Li, Yue Zhao, arXiv 2026 · http://arxiv.org/abs/2603.19423v1

### 클러스터 2 — 자동화된 공격 기법 및 최적화 (10)
- [P-ICLR-e0c25a] Align to Misalign: Automatic LLM Jailbreak with Meta-Optimized LLM Judges, Hamin Koo, Minseon Kim, Jaehyung Kim, ICLR 2025 · https://openreview.net/forum?id=gGjwMNAYAr
- [P-ICLR-9fe35a] Obscure but Effective: Classical Chinese Jailbreak Prompt Optimization via Bio-Inspired Search, Xun Huang, Simeng Qin, Xiaoshuang Jia et al., ICLR 2025 · https://openreview.net/forum?id=O7fxz7D6vf
- [P-ICLR-968c7b] The Devil behind the mask: An emergent safety vulnerability of Diffusion LLMs, Zichen Wen, Jiashu Qu, Zhaorun Chen et al., ICLR 2025 · https://openreview.net/forum?id=rIPeatvPy3
- [P-ICLR-ce83de] SEMA: Simple yet Effective Learning for Multi-Turn Jailbreak Attacks, Mingqian Feng, Xiaodong Liu, Weiwei Yang et al., ICLR 2025 · https://openreview.net/forum?id=6eSNG1VNkl
- [P-2604.21860] Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in Large Language Models, Naheed Rayhan, Sohely Jahan, arXiv 2026 · http://arxiv.org/abs/2604.21860v1
- [P-2604.18789] ARES: Adaptive Red-Teaming and End-to-End Repair of Policy-Reward System, Jiacheng Liang, Yao Ma, Tharindu Kumarage et al., arXiv 2026 · http://arxiv.org/abs/2604.18789v1
- [P-2604.12232] TEMPLATEFUZZ: Fine-Grained Chat Template Fuzzing for Jailbreaking and Red Teaming LLMs, Qingchao Shen, Zibo Xiao, Lili Huang et al., arXiv 2026 · http://arxiv.org/abs/2604.12232v1
- [P-2604.05853] Reading Between the Pixels: An Inscriptive Jailbreak Attack on Text-to-Image Models, Zonghao Ying, Haowen Dai, Lianyu Hu et al., arXiv 2026 · http://arxiv.org/abs/2604.05853v2
- [P-2603.24511] Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs, Alexander Panfilov, Peter Romov, Igor Shilov et al., arXiv 2026 · http://arxiv.org/abs/2603.24511v1
- [P-2603.22341] T-MAP: Red-Teaming LLM Agents with Trajectory-aware Evolutionary Search, Hyomin Lee, Sangwoo Park, Yumin Choi et al., arXiv 2026 · http://arxiv.org/abs/2603.22341v1 · also_in: hf

### 클러스터 3 — 멀티모달 프롬프트 인젝션 (13)
- [P-ICLR-08d850] Misaligned Roles, Misplaced Images: Structural Input Perturbations Expose Multimodal Alignment Blind Spots, Erfan Shayegani, G M Shahariar, Sara Abdali et al., ICLR 2025 · https://openreview.net/forum?id=HRkrWi3FWP
- [P-ICLR-70053c] VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents, Tri Cao, Bennett Lim, Yue Liu et al., ICLR 2025 · https://openreview.net/forum?id=UMauKu2azg
- [P-2604.19300] HalluAudio: A Comprehensive Benchmark for Hallucination Detection in Large Audio-Language Models, Feiyu Zhao, Yiming Chen, Wenhuan Lu et al., arXiv 2026 · http://arxiv.org/abs/2604.19300v1
- [P-2604.16966] Visual Inception: Compromising Long-term Planning in Agentic Recommenders via Multimodal Memory Poisoning, Jiachen Qian, arXiv 2026 · http://arxiv.org/abs/2604.16966v1
- [P-2604.14604] Hijacking Large Audio-Language Models via Context-Agnostic and Imperceptible Auditory Prompt Injection, Meng Chen, Kun Wang, Li Lu et al., arXiv 2026 · http://arxiv.org/abs/2604.14604v1
- [P-2604.12616] Every Picture Tells a Dangerous Story: Memory-Augmented Multi-Agent Jailbreak Attacks on VLMs, Jianhao Chen, Haoyang Chen, Hanjie Zhao et al., arXiv 2026 · http://arxiv.org/abs/2604.12616v1
- [P-2604.12371] Reading Between the Pixels: Linking Text-Image Embedding Alignment to Typographic Attack Success on Vision-Language Models, Ravikumar Balakrishnan, Sanket Mendapara, Ankit Garg, arXiv 2026 · http://arxiv.org/abs/2604.12371v2
- [P-2604.09024] Leave My Images Alone: Preventing Multi-Modal Large Language Models from Analyzing Images via Visual Prompt Injection, Zedian Shao, Hongbin Liu, Yuepeng Hu et al., arXiv 2026 · http://arxiv.org/abs/2604.09024v1
- [P-2604.07831] Are GUI Agents Focused Enough? Automated Distraction via Semantic-level UI Element Injection, Wenkui Yang, Chao Jin, Haisu Zhu et al., arXiv 2026 · http://arxiv.org/abs/2604.07831v1
- [P-2603.29418] Adversarial Prompt Injection Attack on Multimodal Large Language Models, Meiwen Ding, Song Xia, Chenqi Kong et al., arXiv 2026 · http://arxiv.org/abs/2603.29418v1
- [P-2603.27522] Hidden Ads: Behavior Triggered Semantic Backdoors for Advertisement Injection in Vision Language Models, Duanyi Yao, Changyue Li, Zhicong Huang et al., arXiv 2026 · http://arxiv.org/abs/2603.27522v1
- [P-2603.21047] When Minor Edits Matter: LLM-Driven Prompt Attack for Medical VLM Robustness in Ultrasound, Yasamin Medghalchi, Milad Yazdani, Amirhossein Dabiriaghdam et al., arXiv 2026 · http://arxiv.org/abs/2603.21047v1
- [P-2603.19127] On Optimizing Multimodal Jailbreaks for Spoken Language Models, Aravind Krishnan, Karolina Stańczak, Dietrich Klakow, arXiv 2026 · http://arxiv.org/abs/2603.19127v1

### 클러스터 4 — 런타임 방어 및 아키텍처 개선 (24)
- [P-ICLR-b78bdb] Any-Depth Alignment: Unlocking Innate Safety Alignment of LLMs to Any-Depth, Jiawei Zhang, Andrew Estornell, David D. Baek et al., ICLR 2025 · https://openreview.net/forum?id=0fuYOuJyzl
- [P-ICLR-05ef44] The Shape of Adversarial Influence: Characterizing LLM Latent Spaces with Persistent Homology, Aideen Fay, Inés García-Redondo, Qiquan Wang et al., ICLR 2025 · https://openreview.net/forum?id=v2PglvLLKT
- [P-ICLR-206ec5] ASIDE: Architectural Separation of Instructions and Data in Language Models, Egor Zverev, Evgenii Kortukov, Alexander Panfilov et al., ICLR 2025 · https://openreview.net/forum?id=C81TnwHiRM
- [P-ICLR-e3690f] DP-Fusion: Token-Level Differentially Private Inference for Large Language Models, Rushil Thareja, Preslav Nakov, Praneeth Vepakomma et al., ICLR 2025 · https://openreview.net/forum?id=WLK37mn0El
- [P-ICLR-f1ebdc] Discrete Latent Features Ablate Adversarial Attack: A Robust Prompt Tuning Framework for VLMs, Yang Chen, Yanbin Wei, James Kwok et al., ICLR 2025 · https://openreview.net/forum?id=lZgORA63ew
- [P-ICLR-5f3dd1] In-Context Watermarks for Large Language Models, Yepeng Liu, Xuandong Zhao, Christopher Kruegel et al., ICLR 2025 · https://openreview.net/forum?id=fD9YRHazW3
- [P-ICLR-6bdc06] Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols, Mikhail Terekhov, Alexander Panfilov, Daniil Dzenhaliou et al., ICLR 2025 · https://openreview.net/forum?id=wSs1Ez3aKl
- [P-ICLR-82e58b] AEGIS: Adversarial Target-Guided Retention-Data-Free Robust Concept Erasure from Diffusion Models, Fengpeng Li, Kemou Li, Qizhou Wang et al., ICLR 2025 · https://openreview.net/forum?id=3y3hnL7KhS
- [P-2604.24542] Layerwise Convergence Fingerprints for Runtime Misbehavior Detection in Large Language Models, Nay Myat Min, Long H. Pham, Jun Sun, arXiv 2026 · http://arxiv.org/abs/2604.24542v1
- [P-2604.18248] Beyond Pattern Matching: Seven Cross-Domain Techniques for Prompt Injection Detection, Thamilvendhan Munirathinam, arXiv 2026 · http://arxiv.org/abs/2604.18248v1
- [P-2604.17125] CASCADE: A Cascaded Hybrid Defense Architecture for Prompt Injection Detection in MCP-Based Systems, İpek Abasıkeleş Turgut, Edip Gümüş, arXiv 2026 · http://arxiv.org/abs/2604.17125v1
- [P-2604.10717] Detecting RAG Extraction Attack via Dual-Path Runtime Integrity Game, Yuanbo Xie, Yingjie Zhang, Yulin Li et al., arXiv 2026 · http://arxiv.org/abs/2604.10717v1
- [P-2604.08169] Activation Steering for Aligned Open-ended Generation without Sacrificing Coherence, Niklas Herbster, Martin Zborowski, Alberto Tosato et al., arXiv 2026 · http://arxiv.org/abs/2604.08169v1
- [P-2604.06247] SALLIE: Safeguarding Against Latent Language & Image Exploits, Guy Azov, Ofer Rivlin, Guy Shtar, arXiv 2026 · http://arxiv.org/abs/2604.06247v1
- [P-2604.05179] Gradient-Controlled Decoding: A Safety Guardrail for LLMs with Dual-Anchor Steering, Purva Chiniya, Kevin Scaria, Sagar Chaturvedi, arXiv 2026 · http://arxiv.org/abs/2604.05179v1
- [P-2604.03941] SafeCtrl: Region-Aware Safety Control for Text-to-Image Diffusion via Detect-Then-Suppress, Lingyun Zhang, Yu Xie, Zhongli Fang et al., arXiv 2026 · http://arxiv.org/abs/2604.03941v1
- [P-2604.01194] AgentWatcher: A Rule-based Prompt Injection Monitor, Yanting Wang, Wei Zou, Runpeng Geng et al., HF 2026 · https://huggingface.co/papers/2604.01194
- [P-2603.30016] Architecting Secure AI Agents: Perspectives on System-Level Defenses Against Indirect Prompt Injection Attacks, Chong Xiang, Drew Zagieboylo, Shaona Ghosh et al., arXiv 2026 · http://arxiv.org/abs/2603.30016v1
- [P-2603.28345] Crossing the NL/PL Divide: Information Flow Analysis Across the NL/PL Boundary in LLM-Integrated Code, Zihao Xu, Xiao Cheng, Ruijie Meng et al., arXiv 2026 · http://arxiv.org/abs/2603.28345v1
- [P-2603.25176] Prompt Attack Detection with LLM-as-a-Judge and Mixture-of-Models, Hieu Xuan Le, Benjamin Goh, Quy Anh Tang, arXiv 2026 · http://arxiv.org/abs/2603.25176v1
- [P-2603.22519] LLMON: An LLM-native Markup Language to Leverage Structure and Semantics at the LLM Interface, Michael Hind, Basel Shbita, Bo Wu et al., arXiv 2026 · http://arxiv.org/abs/2603.22519v2
- [P-2603.22041] DTVI: Dual-Stage Textual and Visual Intervention for Safe Text-to-Image Generation, Binhong Tan, Zhaoxin Wang, Handing Wang, arXiv 2026 · http://arxiv.org/abs/2603.22041v2
- [P-2603.20976] Detection of adversarial intent in Human-AI teams using LLMs, Abed K. Musaffar, Ambuj Singh, Francesco Bullo, arXiv 2026 · http://arxiv.org/abs/2603.20976v1
- [P-2603.19182] Box Maze: A Process-Control Architecture for Reliable LLM Reasoning, Zou Qiang, arXiv 2026 · http://arxiv.org/abs/2603.19182v1

### 클러스터 5 — 벤치마크 및 평가 체계 구축 (7)
- [P-ICLR-fd7e76] GuidedBench: Measuring and Mitigating the Evaluation Discrepancies of In-the-wild LLM Jailbreak Methods, Ruixuan Huang, Xunguang Wang, Zongjie Li et al., ICLR 2025 · https://openreview.net/forum?id=ZVg8y3ibyM
- [P-ICLR-e7c00e] MCP Security Bench (MSB): Benchmarking Attacks Against Model Context Protocol in LLM Agents, Dongsen Zhang, Zekun Li, Xu Luo et al., ICLR 2025 · https://openreview.net/forum?id=irxxkFMrry
- [P-2604.15415] HarmfulSkillBench: How Do Harmful Skills Weaponize Your Agents?, Yukun Jiang, Yage Zhang, Michael Backes et al., arXiv 2026 · http://arxiv.org/abs/2604.15415v1
- [P-2604.08499] PIArena: A Platform for Prompt Injection Evaluation, Runpeng Geng, Chenlong Yin, Yanting Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.08499v1
- [P-2604.07223] TraceSafe: A Systematic Assessment of LLM Guardrails on Multi-Step Tool-Calling Trajectories, Yen-Shan Chen, Sian-Yao Huang, Cheng-Lin Yang et al., arXiv 2026 · http://arxiv.org/abs/2604.07223v1
- [P-2604.01438] ClawSafety: "Safe" LLMs, Unsafe Agents, Bowen Wei, Yunbei Zhang, Jinhao Pan et al., arXiv 2026 · http://arxiv.org/abs/2604.01438v2
- [P-2603.21975] SecureBreak -- A dataset towards safe and secure models, Marco Arazzi, Vignesh Kumar Kembu, Antonino Nocera, arXiv 2026 · http://arxiv.org/abs/2603.21975v1

### 기타 (클러스터 미분류) (16)
- [P-ICLR-8b94ec] On the Impossibility of Separating Intelligence from Judgment: The Computational Intractability of Filtering for AI Alignment, Sarah Ball, Grzegorz Gluch, Shafi Goldwasser et al., ICLR 2025 · https://openreview.net/forum?id=CwoM9T55lG
- [P-2604.21916] MathDuels: Evaluating LLMs as Problem Posers and Solvers, Zhiqiu Xu, Shibo Jin, Shreya Arya et al., arXiv 2026 · http://arxiv.org/abs/2604.21916v1
- [P-2604.20732] Anchor-and-Resume Concession Under Dynamic Pricing for LLM-Augmented Freight Negotiation, Hoang Nguyen, Lu Wang, Marta Gaia Bras, arXiv 2026 · http://arxiv.org/abs/2604.20732v1
- [P-2604.18510] Different Paths to Harmful Compliance: Behavioral Side Effects and Mechanistic Divergence Across LLM Jailbreaks, Md Rysul Kabir, Zoran Tiganj, arXiv 2026 · http://arxiv.org/abs/2604.18510v1
- [P-2604.12168] Fully Homomorphic Encryption on Llama 3 model for privacy preserving LLM inference, Anes Abdennebi, Nadjia Kara, Laaziz Lahlou, arXiv 2026 · http://arxiv.org/abs/2604.12168v1
- [P-2604.10039] Counting to Four is still a Chore for VLMs, Duy Le Dinh Anh, Patrick Amadeus Irawan, Tuan Van Vo, arXiv 2026 · http://arxiv.org/abs/2604.10039v1 · also_in: hf
- [P-2604.06436] The Defense Trilemma: Why Prompt Injection Defense Wrappers Fail?, Manish Bhatt, Sarthak Munshi, Vineeth Sai Narajala et al., arXiv 2026 · http://arxiv.org/abs/2604.06436v3
- [P-2604.05150] Compiled AI: Deterministic Code Generation for LLM-Based Workflow Automation, Geert Trooskens, Aaron Karlsberg, Anmol Sharma et al., arXiv 2026 · http://arxiv.org/abs/2604.05150v1
- [P-2604.03912] Automating Cloud Security and Forensics Through a Secure-by-Design Generative AI Framework, Dalal Alharthi, Ivan Roberto Kawaminami Garcia, arXiv 2026 · http://arxiv.org/abs/2604.03912v1
- [P-2603.25164] PIDP-Attack: Combining Prompt Injection with Database Poisoning Attacks on Retrieval-Augmented Generation Systems, Haozhen Wang, Haoyue Liu, Jionghao Zhu et al., arXiv 2026 · http://arxiv.org/abs/2603.25164v1
- [P-2603.24125] Alignment Reduces Expressed but Not Encoded Gender Bias: A Unified Framework and Study, Nour Bouchouchi, Thiabult Laugel, Xavier Renard et al., arXiv 2026 · http://arxiv.org/abs/2603.24125v1
- [P-2603.20381] The production of meaning in the processing of natural language, Christopher J. Agostino, Quan Le Thien, Nayan D'Souza et al., arXiv 2026 · http://arxiv.org/abs/2603.20381v1
- [P-2603.18382] From Weak Cues to Real Identities: Evaluating Inference-Driven De-Anonymization in LLM Agents, Myeongseob Ko, Jihyun Jeong, Sumiran Singh Thakur et al., arXiv 2026 · http://arxiv.org/abs/2603.18382v1
- [P-2603.17639] VeriGrey: Greybox Agent Validation, Yuntong Zhang, Sungmin Kang, Ruijie Meng et al., arXiv 2026 · http://arxiv.org/abs/2603.17639v1
- [P-2603.17419] Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare, Saikat Maiti, arXiv 2026 · http://arxiv.org/abs/2603.17419v1
- [P-2603.18063] MCP-38: A Comprehensive Threat Taxonomy for Model Context Protocol Systems (v1.0), Yi Ting Shen, Kentaroh Toyoda, Alex Leung, arXiv 2026 · http://arxiv.org/abs/2603.18063v1

---

## 메타 / 디버그
- model: gemini-2.5-pro
- backend: gemini-pro-sdk
- matched_n: 100
- matched_total_before_cap: 419
- window_days: 240
- tokens_in_uncached: 32089
- tokens_in_cached_read: 131464
- tokens_out: 7239
- usd_estimate: $0.1533
- deep: True
- deep_k: 10
- deep_pdfs_ok: 10
- deep_pdfs_failed: 0
- pdf_archive: reports/2026-04-29-jailbreaking-gemini-pro-deep/
- pdf_archive_linked: 10
- pdf_archive_copied: 0
- pdf_archive_missing: 0
