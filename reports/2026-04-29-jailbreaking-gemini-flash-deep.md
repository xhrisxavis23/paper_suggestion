# Research Topic Suggestion — "jailbreaking"

생성: 2026-04-29T05:22:14.986446+00:00
DB 윈도우: 2025-12-31 ~ 2026-04-29 (119d)
모델: gemini-2.5-flash
매칭 논문: 100건
확장 키워드: ['llm jailbreak', 'prompt injection', 'adversarial prompt']

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — 에이전트 시스템 공격 분석
- **설명**: LLM 기반 에이전트 시스템의 특유의 구조(도구, 메모리, 다단계 작업 등)를 악용하는 새로운 공격 벡터와 취약점을 분석합니다.
- **빈도**: 22건
- **월별 (≈29d씩, 오래된→최근)**: 3 → 9 → 6 → 4
- **대표 논문**:
  - [P-2604.21860] Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in Large Language Models — Naheed Rayhan, Sohely Jahan, arXiv 2026
  - [P-2603.27517] A Systematic Taxonomy of Security Vulnerabilities in the OpenClaw AI Agent Framework — Surada Suwansathit, Yuxuan Zhang, Guofei Gu, arXiv 2026
  - [P-2604.03870] Your Agent is More Brittle Than You Think: Uncovering Indirect Injection Vulnerabilities in Agentic LLMs — Wenhui Zhu, Xuanzhao Dong, Xiwen Chen et al., arXiv 2026

### 클러스터 2 — 에이전트 시스템 방어 전략
- **설명**: LLM 에이전트의 프롬프트 주입 및 기타 공격에 대응하기 위한 방어 아키텍처, 프레임워크, 그리고 특정 메커니즘을 제안합니다.
- **빈도**: 20건
- **월별 (≈29d씩, 오래된→최근)**: 3 → 6 → 7 → 4
- **대표 논문**:
  - [P-2603.30016] Architecting Secure AI Agents: Perspectives on System-Level Defenses Against Indirect Prompt Injection Attacks — Chong Xiang, Drew Zagieboylo, Shaona Ghosh et al., arXiv 2026
  - [P-2604.11790] ClawGuard: A Runtime Security Framework for Tool-Augmented LLM Agents Against Indirect Prompt Injection — Wei Zhao, Zhe Li, Peixin Zhang et al., arXiv 2026
  - [P-2603.13424] Agent Privilege Separation in OpenClaw: A Structural Defense Against Prompt Injection — Darren Cheng, Wen-Kwang Tsao, arXiv 2026

### 클러스터 3 — 멀티모달 LLM 공격 및 방어
- **설명**: 시각, 오디오, 텍스트 등 다양한 양식(모달리티)을 통합하는 대규모 언어 모델에 대한 공격 및 방어 기법을 다룹니다.
- **빈도**: 14건
- **월별 (≈29d씩, 오래된→최근)**: 2 → 4 → 5 → 3
- **대표 논문**:
  - [P-2604.14604] Hijacking Large Audio-Language Models via Context-Agnostic and Imperceptible Auditory Prompt Injection — Meng Chen, Kun Wang, Li Lu et al., arXiv 2026
  - [P-2603.03637] Image-based Prompt Injection: Hijacking Multimodal LLMs through Visually Embedded Adversarial Instructions — Neha Nagaraja, Lan Zhang, Zhilong Wang et al., arXiv 2026
  - [P-2604.06247] SALLIE: Safeguarding Against Latent Language & Image Exploits — Guy Azov, Ofer Rivlin, Guy Shtar, arXiv 2026

### 클러스터 4 — 일반 LLM 공격 탐지 및 방어
- **설명**: 에이전트나 멀티모달 특정적이지 않은 일반적인 LLM의 프롬프트 주입 및 탈옥 공격에 대한 탐지 및 완화 기술을 탐구합니다.
- **빈도**: 10건
- **월별 (≈29d씩, 오래된→최근)**: 2 → 2 → 3 → 3
- **대표 논문**:
  - [P-2604.24542] Layerwise Convergence Fingerprints for Runtime Misbehavior Detection in Large Language Models — Nay Myat Min, Long H. Pham, Jun Sun, arXiv 2026
  - [P-2604.18248] Beyond Pattern Matching: Seven Cross-Domain Techniques for Prompt Injection Detection — Thamilvendhan Munirathinam, arXiv 2026

### 클러스터 5 — 공격 기법 개발 및 평가
- **설명**: 새로운 공격 기법(레드팀 포함)을 개발하거나, 기존 공격 및 방어 메커니즘의 평가 프레임워크 또는 이론적 분석을 제시합니다.
- **빈도**: 22건
- **월별 (≈29d씩, 오래된→최근)**: 8 → 10 → 4 → 0
- **대표 논문**:
  - [P-2603.24511] Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs — Alexander Panfilov, Peter Romov, Igor Shilov et al., arXiv 2026
  - [P-2604.08499] PIArena: A Platform for Prompt Injection Evaluation — Runpeng Geng, Chenlong Yin, Yanting Wang et al., arXiv 2026
  - [P-2603.11331] Jailbreak Scaling Laws for Large Language Models: Polynomial-Exponential Crossover — Indranil Halder, Annesya Banerjee, Cengiz Pehlevan, arXiv 2026

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap C — LLM의 자연어 처리에서 의미 생성의 근본적인 메커니즘을 양자 논리 및 정보 이론적 관점에서 분석하고, 이것이 프롬프트 주입 방어에 미치는 영향
- **타입**: single-shot
- **설명**: LLM의 자연어 처리에서 의미 생성의 근본적인 메커니즘을 양자 논리 및 정보 이론적 관점에서 분석하고, 이것이 프롬프트 주입 방어에 미치는 영향을 다루는 연구는 독특하며 후속 연구가 미진합니다.
- **근거 논문**: P-2603.20381
- **Skeptic 검토**: ✓ 통과 — 이 갭은 LLM 의미 생성의 근본적인 이론적 메커니즘을 양자 논리 및 정보 이론적 관점에서 접근하여 프롬프트 주입 방어에 대한 통찰을 얻으려는 매우 독특한 연구 방향을 제시하며, 현재 다른 클러스터의 논문들에서 명시적으로 다루어지지 않는 고유한 접근법입니다.

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap A** — 현재 방어 기법들은 종종 단발성 공격에 국한되거나, 적응형 공격에 취약하며, 다양한 시나리오에 걸쳐 일반화되지 못하는 한계가 있습니다. · 거부 사유: 다른 클러스터에서 이미 다룸. arxiv:2604.24542와 arxiv:2604.18248을 포함한 '일반 LLM 공격 탐지 및 방어' 클러스터 내의 여러 논문들이 이미 적응형 공격에 대한 취약성과 일반화 문제를 명시적으로 지적하고 이를 해결하기 위한 새로운 방어 기법을 제안하고 있습니다. Gap은 이들 논문이 해결하고자 하는 '문제'를 서술할 뿐, '해결되지 않은 연구 갭'을 나타내지 않습니다.
- **Gap B** — LLM 에이전트 시스템의 복잡한 다단계 상호작용과 동적인 맥락을 전반적으로 이해하고 방어하는 통합적인 아키텍처 연구는 부족합니다. · 거부 사유: 다른 클러스터에서 이미 다룸. '에이전트 시스템 방어 전략' 클러스터의 여러 논문(예: arxiv:2603.30016, arxiv:2603.11619, arxiv:2603.03205, arxiv:2603.07191)이 LLM 에이전트의 복잡한 다단계 상호작용과 동적인 맥락을 전반적으로 이해하고 방어하기 위한 '시스템 수준' 및 '통합적인 아키텍처'를 명시적으로 제안하고 연구하고 있습니다.
- **Gap D** — LLM과 에이전트의 안전성을 높이려는 노력이 종종 모델의 핵심 기능이나 유틸리티를 저하시키거나, 새로운 종류의 성능 저하를 야기한다는 문제가 여러 연구에서 반복적으로 제기됩니다. · 거부 사유: 다른 클러스터에서 이미 다룸. 이 갭은 LLM 안전성 강화와 유틸리티 유지 간의 근본적인 트레이드오프를 지적하고 있는데, 이는 '일반 LLM 공격 탐지 및 방어' 및 '공격 기법 개발 및 평가' 클러스터의 여러 논문(예: arxiv:2603.19423, arxiv:2603.06436, arxiv:2604.05179)에서 명시적으로 인식하고 해결하거나 이론적으로 분석하는 대상입니다.
- **Gap E** — 멀티모달(특히 시각) 입력의 미묘한 의미론적 콘텐츠가 에이전트의 장기 기억을 오염시키고 미래 계획을 조작하는 복합적인 공격에 대한 체계적인 방어 연구는 제한적입니다. · 거부 사유: 다른 클러스터에서 이미 다룸. Gap E에서 언급된 '멀티모달 입력의 의미론적 콘텐츠가 에이전트의 장기 기억을 오염시키고 미래 계획을 조작하는 복합적인 공격'에 대해, 증거 논문인 arxiv:2604.16966은 'Visual Inception'이라는 공격을 식별하고 이를 완화하기 위한 'CognitiveGuard'라는 듀얼 프로세스 방어 프레임워크를 제안하여 직접적으로 해당 문제를 해결하고 있습니다. 이 연구는 '에이전트 시스템 공격 분석' 클러스터에 포함되어 있으며, 갭으로 지적된 '체계적인 방어 연구'가 이미 진행 중임을 보여줍니다.
- **Gap F** — LLM 안전성 연구의 핵심 도구인 벤치마크들의 학술적 영향력, 코드 품질, 윤리적 고려사항에 대한 체계적이고 포괄적인 평가 및 개선 연구가 부족합니다. · 거부 사유: 다른 클러스터에서 이미 다룸. 증거 논문인 arxiv:2603.04459 ('Benchmark of Benchmarks')는 LLM 안전성 벤치마크의 학술적 영향력, 코드 품질, 윤리적 고려사항에 대한 '최초의 다차원 평가'를 제시하며, 이 갭이 주장하는 '부족한 연구'를 직접적으로 수행하고 있습니다. 즉, 이 연구는 갭을 채우는 역할을 합니다. 이 논문은 '공격 기법 개발 및 평가' 클러스터에 포함되어 있습니다.

</details>

## 3. 연구 제안 (Proposer)

### 제안 1 — CONTEXT-GUARD
**가설**: LLM의 의미 생성에 내재된 양자 논리적 맥락성을 활용하여 프롬프트 주입 공격 시도 시 의미적 불일치를 탐지하고 방어할 수 있다.
**메우는 갭**: C
**접근**: 논문 'The production of meaning in the processing of natural language'에서 제시된 CHSH $|S|$ 파라미터와 같은 맥락성 지표를 실시간으로 모니터링하여, 악의적인 프롬프트 주입으로 인한 비정상적인 의미 구성 변화를 탐지한다. 이를 위해, 정상적인 상호작용과 악의적인 프롬프트 주입 시퀀스에서 맥락성 지표의 분포를 학습하고, 임계값을 초과하는 이상 징후 발생 시 추가적인 필터링이나 거부 메커니즘을 트리거한다.
**Baselines**: Layerwise Convergence Fingerprinting (LCF), Mirror design pattern, PromptShield
**예상 기여**: LLM의 내부 의미 생성 메커니즘에 기반한 새로운 차원의 프롬프트 주입 방어 기법을 제시하여, 기존의 표면적 패턴 매칭이나 의미론적 분류 방어의 한계를 극복한다. 이론적 맥락성 연구가 실용적인 보안 솔루션으로 이어지는 길을 연다.
**참고**: P-2603.20381, P-2604.24542, P-2603.11875, P-2604.03912

### 제안 2 — INFO-ENTANGLEMENT
**가설**: LLM 내부의 정보 흐름에서 양자 정보 이론적 '얽힘(entanglement)' 개념을 적용하여, 프롬프트 주입 공격으로 인한 비정상적인 정보 전파 또는 분리 패턴을 식별하고 방어할 수 있다.
**메우는 갭**: C
**접근**: LLM의 내부 은닉 상태(hidden states) 간의 상호 정보량(mutual information) 또는 양자 얽힘 유사 지표를 계산하여, 정상적인 추론 과정과 악의적인 명령에 의해 조작된 정보 흐름 간의 통계적 차이를 분석한다. 이를 통해 특정 레이어나 토큰에서 발생하는 정보 왜곡을 탐지하고, 공격 시도 시 응답 생성을 조기에 중단하거나 안전한 대안으로 전환한다.
**Baselines**: Layerwise Convergence Fingerprinting (LCF), SALLIE's internal activation analysis, Gradient-Controlled Decoding (GCD)
**예상 기여**: LLM 내부의 저수준(low-level) 정보 처리 과정을 양자 정보 이론의 관점에서 해석하고, 이를 활용하여 보다 근본적이고 모델 변경 없는 프롬프트 주입 방어 메커니즘을 개발한다. LLM의 블랙박스 특성을 일부 해명하고, 새로운 진단 도구를 제공한다.
**참고**: P-2603.20381, P-2604.24542, P-2604.06247, P-2604.05179

### 제안 3 — DYN-REALIGN
**가설**: LLM의 동적 맥락성을 정보 이론적으로 모델링하고, 이를 기반으로 프롬프트 주입 공격으로 인해 흐트러진 의도된 맥락적 균형을 실시간으로 재정렬하여 방어할 수 있다.
**메우는 갭**: C
**접근**: `The production of meaning in the processing of natural language`에서 언급된 맥락성 유지의 중요성에 착안하여, 매 턴(turn) 또는 토큰 생성 단계마다 현재 LLM의 내부 상태가 '안전한 맥락 공간'에 속하는지 정보 이론적 거리 척도를 통해 검증한다. 만약 이탈이 감지되면, 특정 '안전 앵커(safety anchor)' 프롬프트나 내부 활성화 스티어링 (activation steering)을 통해 모델의 의미 생성 궤적을 의도된 안전한 맥락으로 되돌린다.
**Baselines**: Activation Steering (SwFC, StTP, StMP), Box Maze framework, DPO-based suppression
**예상 기여**: 프롬프트 주입으로 인한 의미론적 맥락 이탈을 동적으로 감지하고 수정하는 새로운 방어 패러다임을 제안한다. 이는 일회성 필터링을 넘어선 지속적인 안전성 유지 메커니즘을 제공하며, LLM의 복잡한 추론 과정에 대한 이해를 심화시킨다.
**참고**: P-2603.20381, P-2604.08169, P-2603.19182, P-2604.03941

### 제안 4 — QUANTA-ROBUST
**가설**: 프롬프트 주입 공격의 성공률이 LLM의 의미 생성 과정에서 나타나는 양자 맥락성 관련 파라미터와 특정 상관관계를 가지므로, 이를 정량화하여 모델의 공격 취약성을 예측하고 방어 전략을 강화할 수 있다.
**메우는 갭**: C
**접근**: `The production of meaning in the processing of natural language`에서 사용된 CHSH $|S|$ 파라미터나 다른 정보 이론적 불확실성 지표를 사용하여, 다양한 프롬프트 주입 공격 시나리오 하에서 LLM의 내부 의미 생성 과정의 '모호성' 또는 '비고전성'을 측정한다. 이러한 지표와 실제 공격 성공률 간의 상관관계를 분석하여, 높은 상관관계를 보이는 지표를 기반으로 동적 방어 임계값을 설정하거나, 공격에 취약한 모델의 내부 상태를 식별한다.
**Baselines**: Attack success rate (ASR) metrics from competitions, TEMPLATEFUZZ, PIArena
**예상 기여**: 양자 맥락성 개념을 LLM의 공격 취약성 예측 및 평가에 활용하는 새로운 방법을 제시한다. 이는 방어 메커니즘의 설명 가능성을 높이고, 특정 공격에 대한 모델의 내재적 강점을 이해하는 데 기여한다.
**참고**: P-2603.20381, P-2603.15714, P-2603.24511, P-2604.12232, P-2604.08499

### 제안 5 — AGENT-INFOSEC
**가설**: LLM 에이전트의 다단계 실행 과정에서 발생하는 정보 흐름의 양자 정보 이론적 이상 징후를 탐지함으로써 프롬프트 주입 및 기타 에이전트 특정 공격을 방어할 수 있다.
**메우는 갭**: C
**접근**: `The production of meaning in the processing of natural language`에서 제안된 '맥락성 유지'와 다른 정보 이론적 개념을 에이전트의 내부 의사 결정 및 도구 호출 궤적에 적용한다. 각 단계에서 에이전트의 '정보 상태'를 정의하고, 정상적인 에이전트 동작과 공격받은 에이전트 동작 간의 정보 이론적 거리 변화를 측정한다. 이를 통해 프롬프트 주입이 에이전트의 계획이나 도구 사용에 비정상적인 정보적 영향을 미치는 지점을 실시간으로 식별하고 개입한다.
**Baselines**: Formalized LLM agent security framework, ClawGuard, AgentWatcher, Kill-chain canaries
**예상 기여**: 에이전트 시스템의 복잡한 다단계 상호작용 속에서 정보 이론 기반의 새로운 보안 감시 및 방어 메커니즘을 구축한다. 이는 기존 에이전트 방어 기법이 놓치기 쉬운 내부 정보 흐름 조작에 대한 강력한 방어를 제공한다.
**참고**: P-2603.20381, P-2603.19469, P-2604.11790, P-2604.01194, P-2603.28013

## 4. 참고문헌 (메타DB 기반)

### 클러스터 1 — 에이전트 시스템 공격 분석 (19)
- [P-2604.21860] Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in Large Language Models, Naheed Rayhan, Sohely Jahan, arXiv 2026 · http://arxiv.org/abs/2604.21860v1
- [P-2604.16966] Visual Inception: Compromising Long-term Planning in Agentic Recommenders via Multimodal Memory Poisoning, Jiachen Qian, arXiv 2026 · http://arxiv.org/abs/2604.16966v1
- [P-2604.15415] HarmfulSkillBench: How Do Harmful Skills Weaponize Your Agents?, Yukun Jiang, Yage Zhang, Michael Backes et al., arXiv 2026 · http://arxiv.org/abs/2604.15415v1
- [P-2604.09378] BadSkill: Backdoor Attacks on Agent Skills via Model-in-Skill Poisoning, Guiyao Tie, Jiawen Shi, Pan Zhou et al., arXiv 2026 · http://arxiv.org/abs/2604.09378v1
- [P-2604.07831] Are GUI Agents Focused Enough? Automated Distraction via Semantic-level UI Element Injection, Wenkui Yang, Chao Jin, Haisu Zhu et al., arXiv 2026 · http://arxiv.org/abs/2604.07831v1
- [P-2604.04561] Mapping the Exploitation Surface: A 10,000-Trial Taxonomy of What Makes LLM Agents Exploit Vulnerabilities, Charafeddine Mouzouni, arXiv 2026 · http://arxiv.org/abs/2604.04561v1
- [P-2604.03870] Your Agent is More Brittle Than You Think: Uncovering Indirect Injection Vulnerabilities in Agentic LLMs, Wenhui Zhu, Xuanzhao Dong, Xiwen Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.03870v1
- [P-2604.03070] Credential Leakage in LLM Agent Skills: A Large-Scale Empirical Study, Zhihao Chen, Ying Zhang, Yi Liu et al., arXiv 2026 · http://arxiv.org/abs/2604.03070v1
- [P-2603.28345] Crossing the NL/PL Divide: Information Flow Analysis Across the NL/PL Boundary in LLM-Integrated Code, Zihao Xu, Xiao Cheng, Ruijie Meng et al., arXiv 2026 · http://arxiv.org/abs/2603.28345v1
- [P-2603.28013] Kill-Chain Canaries: Stage-Level Tracking of Prompt Injection Across Attack Surfaces and Model Safety Tiers, Haochuan Kevin Wang, Zechen Zhang, arXiv 2026 · http://arxiv.org/abs/2603.28013v3
- [P-2603.27517] A Systematic Taxonomy of Security Vulnerabilities in the OpenClaw AI Agent Framework, Surada Suwansathit, Yuxuan Zhang, Guofei Gu, arXiv 2026 · http://arxiv.org/abs/2603.27517v1
- [P-2603.24203] Invisible Threats from Model Context Protocol: Generating Stealthy Injection Payload via Tree-based Adaptive Search, Yulin Shen, Xudong Pan, Geng Hong et al., arXiv 2026 · http://arxiv.org/abs/2603.24203v1
- [P-2603.23064] Mind Your HEARTBEAT! Claw Background Execution Inherently Enables Silent Memory Pollution, Yechao Zhang, Shiqian Zhao, Jie Zhang et al., arXiv 2026 · http://arxiv.org/abs/2603.23064v3
- [P-2603.19974] Trojan's Whisper: Stealthy Manipulation of OpenClaw through Injected Bootstrapped Guidance, Fazhong Liu, Zhuoyan Chen, Tu Lan et al., arXiv 2026 · http://arxiv.org/abs/2603.19974v1
- [P-2603.20320] The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents, Shasha Yu, Fiona Carroll, Barry L. Bentley, arXiv 2026 · http://arxiv.org/abs/2603.20320v1
- [P-2603.18382] From Weak Cues to Real Identities: Evaluating Inference-Driven De-Anonymization in LLM Agents, Myeongseob Ko, Jihyun Jeong, Sumiran Singh Thakur et al., arXiv 2026 · http://arxiv.org/abs/2603.18382v1
- [P-2603.11619] Taming OpenClaw: Security Analysis and Mitigation of Autonomous LLM Agent Threats, Xinhao Deng, Yixiang Zhang, Jiaqing Wu et al., arXiv 2026 · http://arxiv.org/abs/2603.11619v1
- [P-2603.10163] Compatibility at a Cost: Systematic Discovery and Exploitation of MCP Clause-Compliance Vulnerabilities, Nanzi Yang, Weiheng Bai, Kangjie Lu, arXiv 2026 · http://arxiv.org/abs/2603.10163v1
- [P-2603.03633] Goal-Driven Risk Assessment for LLM-Powered Systems: A Healthcare Case Study, Neha Nagaraja, Hayretdin Bahsi, arXiv 2026 · http://arxiv.org/abs/2603.03633v1

### 클러스터 2 — 에이전트 시스템 방어 전략 (20)
- [P-2604.24020] Poster: ClawdGo: Endogenous Security Awareness Training for Autonomous AI Agents, Jiaqi Li, Yang Zhao, Bin Sun et al., arXiv 2026 · http://arxiv.org/abs/2604.24020v1
- [P-2604.19657] An AI Agent Execution Environment to Safeguard User Data, Robert Stanley, Avi Verma, Lillian Tsai et al., arXiv 2026 · http://arxiv.org/abs/2604.19657v1
- [P-2604.17139] The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration, Jiayuan Liu, Shiyi Du, Weihua Du et al., arXiv 2026 · http://arxiv.org/abs/2604.17139v1
- [P-2604.17125] CASCADE: A Cascaded Hybrid Defense Architecture for Prompt Injection Detection in MCP-Based Systems, İpek Abasıkeleş Turgut, Edip Gümüş, arXiv 2026 · http://arxiv.org/abs/2604.17125v1
- [P-2604.16838] enclawed: A Configurable, Sector-Neutral Hardening Framework for Single-User AI Assistant Gateways, Alfredo Metere, arXiv 2026 · http://arxiv.org/abs/2604.16838v1
- [P-2604.16762] CapSeal: Capability-Sealed Secret Mediation for Secure Agent Execution, Shutong Jin, Ruiyi Guo, Ray C. C. Cheung, arXiv 2026 · http://arxiv.org/abs/2604.16762v1
- [P-2604.11790] ClawGuard: A Runtime Security Framework for Tool-Augmented LLM Agents Against Indirect Prompt Injection, Wei Zhao, Zhe Li, Peixin Zhang et al., arXiv 2026 · http://arxiv.org/abs/2604.11790v1
- [P-2604.10286] STARS: Skill-Triggered Audit for Request-Conditioned Invocation Safety in Agent Systems, Guijia Zhang, Shu Yang, Xilin Gong et al., arXiv 2026 · http://arxiv.org/abs/2604.10286v1
- [P-2604.04426] ShieldNet: Network-Level Guardrails against Emerging Supply-Chain Injections in Agentic Systems, Zhuowen Yuan, Zhaorun Chen, Zhen Xiang et al., arXiv 2026 · http://arxiv.org/abs/2604.04426v1
- [P-2604.01194] AgentWatcher: A Rule-based Prompt Injection Monitor, Yanting Wang, Wei Zou, Runpeng Geng et al., HF 2026 · https://huggingface.co/papers/2604.01194
- [P-2603.30016] Architecting Secure AI Agents: Perspectives on System-Level Defenses Against Indirect Prompt Injection Attacks, Chong Xiang, Drew Zagieboylo, Shaona Ghosh et al., arXiv 2026 · http://arxiv.org/abs/2603.30016v1
- [P-2603.23791] The Cognitive Firewall:Securing Browser Based AI Agents Against Indirect Prompt Injection Via Hybrid Edge Cloud Defense, Qianlong Lan, Anuj Kaul, arXiv 2026 · http://arxiv.org/abs/2603.23791v1
- [P-2603.19469] A Framework for Formalizing LLM Agent Security, Vincent Siu, Jingxuan He, Kyle Montgomery et al., arXiv 2026 · http://arxiv.org/abs/2603.19469v1
- [P-2603.19182] Box Maze: A Process-Control Architecture for Reliable LLM Reasoning, Zou Qiang, arXiv 2026 · http://arxiv.org/abs/2603.19182v1
- [P-2603.17419] Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare, Saikat Maiti, arXiv 2026 · http://arxiv.org/abs/2603.17419v1
- [P-2603.16215] CoMAI: A Collaborative Multi-Agent Framework for Robust and Equitable Interview Evaluation, Gengxin Sun, Ruihao Yu, Liangyi Yin et al., arXiv 2026 · http://arxiv.org/abs/2603.16215v1
- [P-2603.13424] Agent Privilege Separation in OpenClaw: A Structural Defense Against Prompt Injection, Darren Cheng, Wen-Kwang Tsao, arXiv 2026 · http://arxiv.org/abs/2603.13424v1
- [P-2603.12230] Security Considerations for Artificial Intelligence Agents, Ninghui Li, Kaiyuan Zhang, Kyle Polley et al., arXiv 2026 · http://arxiv.org/abs/2603.12230v2
- [P-2603.07191] Governance Architecture for Autonomous Agent Systems: Threats, Framework, and Engineering Practice, Yuxu Ge, arXiv 2026 · http://arxiv.org/abs/2603.07191v2
- [P-2603.03205] Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use, Aradhye Agarwal, Gurdit Siyan, Yash Pandya et al., arXiv 2026 · http://arxiv.org/abs/2603.03205v1 · also_in: hf

### 클러스터 3 — 멀티모달 LLM 공격 및 방어 (14)
- [P-2604.14604] Hijacking Large Audio-Language Models via Context-Agnostic and Imperceptible Auditory Prompt Injection, Meng Chen, Kun Wang, Li Lu et al., arXiv 2026 · http://arxiv.org/abs/2604.14604v1
- [P-2604.12616] Every Picture Tells a Dangerous Story: Memory-Augmented Multi-Agent Jailbreak Attacks on VLMs, Jianhao Chen, Haoyang Chen, Hanjie Zhao et al., arXiv 2026 · http://arxiv.org/abs/2604.12616v1
- [P-2604.12371] Reading Between the Pixels: Linking Text-Image Embedding Alignment to Typographic Attack Success on Vision-Language Models, Ravikumar Balakrishnan, Sanket Mendapara, Ankit Garg, arXiv 2026 · http://arxiv.org/abs/2604.12371v2
- [P-2604.09024] Leave My Images Alone: Preventing Multi-Modal Large Language Models from Analyzing Images via Visual Prompt Injection, Zedian Shao, Hongbin Liu, Yuepeng Hu et al., arXiv 2026 · http://arxiv.org/abs/2604.09024v1
- [P-2604.06247] SALLIE: Safeguarding Against Latent Language & Image Exploits, Guy Azov, Ofer Rivlin, Guy Shtar, arXiv 2026 · http://arxiv.org/abs/2604.06247v1
- [P-2604.03941] SafeCtrl: Region-Aware Safety Control for Text-to-Image Diffusion via Detect-Then-Suppress, Lingyun Zhang, Yu Xie, Zhongli Fang et al., arXiv 2026 · http://arxiv.org/abs/2604.03941v1
- [P-2604.05853] Reading Between the Pixels: An Inscriptive Jailbreak Attack on Text-to-Image Models, Zonghao Ying, Haowen Dai, Lianyu Hu et al., arXiv 2026 · http://arxiv.org/abs/2604.05853v2
- [P-2603.29418] Adversarial Prompt Injection Attack on Multimodal Large Language Models, Meiwen Ding, Song Xia, Chenqi Kong et al., arXiv 2026 · http://arxiv.org/abs/2603.29418v1
- [P-2603.27522] Hidden Ads: Behavior Triggered Semantic Backdoors for Advertisement Injection in Vision Language Models, Duanyi Yao, Changyue Li, Zhicong Huang et al., arXiv 2026 · http://arxiv.org/abs/2603.27522v1
- [P-2603.22041] DTVI: Dual-Stage Textual and Visual Intervention for Safe Text-to-Image Generation, Binhong Tan, Zhaoxin Wang, Handing Wang, arXiv 2026 · http://arxiv.org/abs/2603.22041v2
- [P-2603.21047] When Minor Edits Matter: LLM-Driven Prompt Attack for Medical VLM Robustness in Ultrasound, Yasamin Medghalchi, Milad Yazdani, Amirhossein Dabiriaghdam et al., arXiv 2026 · http://arxiv.org/abs/2603.21047v1
- [P-2603.19127] On Optimizing Multimodal Jailbreaks for Spoken Language Models, Aravind Krishnan, Karolina Stańczak, Dietrich Klakow, arXiv 2026 · http://arxiv.org/abs/2603.19127v1
- [P-2603.07708] VoiceSHIELD-Small: Real-Time Malicious Speech Detection and Transcription, Sumit Ranjan, Sugandha Sharma, Ubaid Abbas et al., arXiv 2026 · http://arxiv.org/abs/2603.07708v1
- [P-2603.03637] Image-based Prompt Injection: Hijacking Multimodal LLMs through Visually Embedded Adversarial Instructions, Neha Nagaraja, Lan Zhang, Zhilong Wang et al., arXiv 2026 · http://arxiv.org/abs/2603.03637v1

### 클러스터 4 — 일반 LLM 공격 탐지 및 방어 (9)
- [P-2604.24542] Layerwise Convergence Fingerprints for Runtime Misbehavior Detection in Large Language Models, Nay Myat Min, Long H. Pham, Jun Sun, arXiv 2026 · http://arxiv.org/abs/2604.24542v1
- [P-2604.18789] ARES: Adaptive Red-Teaming and End-to-End Repair of Policy-Reward System, Jiacheng Liang, Yao Ma, Tharindu Kumarage et al., arXiv 2026 · http://arxiv.org/abs/2604.18789v1
- [P-2604.18248] Beyond Pattern Matching: Seven Cross-Domain Techniques for Prompt Injection Detection, Thamilvendhan Munirathinam, arXiv 2026 · http://arxiv.org/abs/2604.18248v1
- [P-2604.08169] Activation Steering for Aligned Open-ended Generation without Sacrificing Coherence, Niklas Herbster, Martin Zborowski, Alberto Tosato et al., arXiv 2026 · http://arxiv.org/abs/2604.08169v1
- [P-2604.05179] Gradient-Controlled Decoding: A Safety Guardrail for LLMs with Dual-Anchor Steering, Purva Chiniya, Kevin Scaria, Sagar Chaturvedi, arXiv 2026 · http://arxiv.org/abs/2604.05179v1
- [P-2604.03912] Automating Cloud Security and Forensics Through a Secure-by-Design Generative AI Framework, Dalal Alharthi, Ivan Roberto Kawaminami Garcia, arXiv 2026 · http://arxiv.org/abs/2604.03912v1
- [P-2603.25176] Prompt Attack Detection with LLM-as-a-Judge and Mixture-of-Models, Hieu Xuan Le, Benjamin Goh, Quy Anh Tang, arXiv 2026 · http://arxiv.org/abs/2603.25176v1
- [P-2603.22519] LLMON: An LLM-native Markup Language to Leverage Structure and Semantics at the LLM Interface, Michael Hind, Basel Shbita, Bo Wu et al., arXiv 2026 · http://arxiv.org/abs/2603.22519v2
- [P-2603.11875] The Mirror Design Pattern: Strict Data Geometry over Model Scale for Prompt Injection Detection, J Alex Corll, arXiv 2026 · http://arxiv.org/abs/2603.11875v2

### 클러스터 5 — 공격 기법 개발 및 평가 (22)
- [P-2604.08499] PIArena: A Platform for Prompt Injection Evaluation, Runpeng Geng, Chenlong Yin, Yanting Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.08499v1
- [P-2604.10717] Detecting RAG Extraction Attack via Dual-Path Runtime Integrity Game, Yuanbo Xie, Yingjie Zhang, Yulin Li et al., arXiv 2026 · http://arxiv.org/abs/2604.10717v1
- [P-2604.10577] The Blind Spot of Agent Safety: How Benign User Instructions Expose Critical Vulnerabilities in Computer-Use Agents, Xuwei Ding, Skylar Zhai, Linxin Song et al., arXiv 2026 · http://arxiv.org/abs/2604.10577v2 · also_in: hf
- [P-2604.01438] ClawSafety: "Safe" LLMs, Unsafe Agents, Bowen Wei, Yunbei Zhang, Jinhao Pan et al., arXiv 2026 · http://arxiv.org/abs/2604.01438v2
- [P-2603.28166] Evaluating Privilege Usage of Agents with Real-World Tools, Quan Zhang, Lianhang Fu, Lvsi Lian et al., arXiv 2026 · http://arxiv.org/abs/2603.28166v2
- [P-2603.25164] PIDP-Attack: Combining Prompt Injection with Database Poisoning Attacks on Retrieval-Augmented Generation Systems, Haozhen Wang, Haoyue Liu, Jionghao Zhu et al., arXiv 2026 · http://arxiv.org/abs/2603.25164v1
- [P-2604.02954] LogicPoison: Logical Attacks on Graph Retrieval-Augmented Generation, Yilin Xiao, Jin Chen, Qinggang Zhang et al., arXiv 2026 · http://arxiv.org/abs/2604.02954v1
- [P-2603.24511] Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs, Alexander Panfilov, Peter Romov, Igor Shilov et al., arXiv 2026 · http://arxiv.org/abs/2603.24511v1
- [P-2603.22341] T-MAP: Red-Teaming LLM Agents with Trajectory-aware Evolutionary Search, Hyomin Lee, Sangwoo Park, Yumin Choi et al., arXiv 2026 · http://arxiv.org/abs/2603.22341v1 · also_in: hf
- [P-2603.21975] SecureBreak -- A dataset towards safe and secure models, Marco Arazzi, Vignesh Kumar Kembu, Antonino Nocera, arXiv 2026 · http://arxiv.org/abs/2603.21975v1
- [P-2603.20976] Detection of adversarial intent in Human-AI teams using LLMs, Abed K. Musaffar, Ambuj Singh, Francesco Bullo, arXiv 2026 · http://arxiv.org/abs/2603.20976v1
- [P-2603.17639] VeriGrey: Greybox Agent Validation, Yuntong Zhang, Sungmin Kang, Ruijie Meng et al., arXiv 2026 · http://arxiv.org/abs/2603.17639v1
- [P-2603.18063] MCP-38: A Comprehensive Threat Taxonomy for Model Context Protocol Systems (v1.0), Yi Ting Shen, Kentaroh Toyoda, Alex Leung, arXiv 2026 · http://arxiv.org/abs/2603.18063v1
- [P-2603.17123] Security Assessment and Mitigation Strategies for Large Language Models: A Comprehensive Defensive Framework, Taiwo Onitiju, Iman Vakilinia, arXiv 2026 · http://arxiv.org/abs/2603.17123v1
- [P-2603.15417] Amplification Effects in Test-Time Reinforcement Learning: Safety and Reasoning Vulnerabilities, Vanshaj Khattar, Md Rafi ur Rashid, Moumita Choudhury et al., arXiv 2026 · http://arxiv.org/abs/2603.15417v1
- [P-2603.15714] How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition, Mateusz Dziemian, Maxwell Lin, Xiaohan Fu et al., arXiv 2026 · http://arxiv.org/abs/2603.15714v1
- [P-2603.14355] Exposing Long-Tail Safety Failures in Large Language Models through Efficient Diverse Response Sampling, Suvadeep Hajra, Palash Nandi, Tanmoy Chakraborty, arXiv 2026 · http://arxiv.org/abs/2603.14355v1
- [P-2603.13026] PISmith: Reinforcement Learning-based Red Teaming for Prompt Injection Defenses, Chenlong Yin, Runpeng Geng, Yanting Wang et al., arXiv 2026 · http://arxiv.org/abs/2603.13026v1
- [P-2603.12681] Colluding LoRA: A Compositional Vulnerability in LLM Safety Alignment, Sihao Ding, arXiv 2026 · http://arxiv.org/abs/2603.12681v2
- [P-2603.11331] Jailbreak Scaling Laws for Large Language Models: Polynomial-Exponential Crossover, Indranil Halder, Annesya Banerjee, Cengiz Pehlevan, arXiv 2026 · http://arxiv.org/abs/2603.11331v2
- [P-2603.10521] IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs, Chuan Guo, Juan Felipe Ceron Uribe, Sicheng Zhu et al., arXiv 2026 · http://arxiv.org/abs/2603.10521v1
- [P-2603.04459] Benchmark of Benchmarks: Unpacking Influence and Code Repository Quality in LLM Safety Benchmarks, Junjie Chu, Xinyue Shen, Ye Leng et al., arXiv 2026 · http://arxiv.org/abs/2603.04459v2

### 기타 (클러스터 미분류) (16)
- [P-2604.21916] MathDuels: Evaluating LLMs as Problem Posers and Solvers, Zhiqiu Xu, Shibo Jin, Shreya Arya et al., arXiv 2026 · http://arxiv.org/abs/2604.21916v1
- [P-2604.20732] Anchor-and-Resume Concession Under Dynamic Pricing for LLM-Augmented Freight Negotiation, Hoang Nguyen, Lu Wang, Marta Gaia Bras, arXiv 2026 · http://arxiv.org/abs/2604.20732v1
- [P-2604.19300] HalluAudio: A Comprehensive Benchmark for Hallucination Detection in Large Audio-Language Models, Feiyu Zhao, Yiming Chen, Wenhuan Lu et al., arXiv 2026 · http://arxiv.org/abs/2604.19300v1
- [P-2604.18510] Different Paths to Harmful Compliance: Behavioral Side Effects and Mechanistic Divergence Across LLM Jailbreaks, Md Rysul Kabir, Zoran Tiganj, arXiv 2026 · http://arxiv.org/abs/2604.18510v1
- [P-2604.12232] TEMPLATEFUZZ: Fine-Grained Chat Template Fuzzing for Jailbreaking and Red Teaming LLMs, Qingchao Shen, Zibo Xiao, Lili Huang et al., arXiv 2026 · http://arxiv.org/abs/2604.12232v1
- [P-2604.12168] Fully Homomorphic Encryption on Llama 3 model for privacy preserving LLM inference, Anes Abdennebi, Nadjia Kara, Laaziz Lahlou, arXiv 2026 · http://arxiv.org/abs/2604.12168v1
- [P-2604.11806] Detecting Safety Violations Across Many Agent Traces, Adam Stein, Davis Brown, Hamed Hassani et al., arXiv 2026 · http://arxiv.org/abs/2604.11806v1
- [P-2604.10039] Counting to Four is still a Chore for VLMs, Duy Le Dinh Anh, Patrick Amadeus Irawan, Tuan Van Vo, arXiv 2026 · http://arxiv.org/abs/2604.10039v1 · also_in: hf
- [P-2604.07223] TraceSafe: A Systematic Assessment of LLM Guardrails on Multi-Step Tool-Calling Trajectories, Yen-Shan Chen, Sian-Yao Huang, Cheng-Lin Yang et al., arXiv 2026 · http://arxiv.org/abs/2604.07223v1
- [P-2604.06550] SkillSieve: A Hierarchical Triage Framework for Detecting Malicious AI Agent Skills, Yinghan Hou, Zongyou Yang, arXiv 2026 · http://arxiv.org/abs/2604.06550v1
- [P-2604.06436] The Defense Trilemma: Why Prompt Injection Defense Wrappers Fail?, Manish Bhatt, Sarthak Munshi, Vineeth Sai Narajala et al., arXiv 2026 · http://arxiv.org/abs/2604.06436v3
- [P-2604.05150] Compiled AI: Deterministic Code Generation for LLM-Based Workflow Automation, Geert Trooskens, Aaron Karlsberg, Anmol Sharma et al., arXiv 2026 · http://arxiv.org/abs/2604.05150v1
- [P-2603.24125] Alignment Reduces Expressed but Not Encoded Gender Bias: A Unified Framework and Study, Nour Bouchouchi, Thiabult Laugel, Xavier Renard et al., arXiv 2026 · http://arxiv.org/abs/2603.24125v1
- [P-2603.20381] The production of meaning in the processing of natural language, Christopher J. Agostino, Quan Le Thien, Nayan D'Souza et al., arXiv 2026 · http://arxiv.org/abs/2603.20381v1
- [P-2603.19423] The Autonomy Tax: Defense Training Breaks LLM Agents, Shawn Li, Yue Zhao, arXiv 2026 · http://arxiv.org/abs/2603.19423v1
- [P-2603.11281] ThReadMed-QA: A Multi-Turn Medical Dialogue Benchmark from Real Patient Questions, Monica Munnangi, Saiph Savage, arXiv 2026 · http://arxiv.org/abs/2603.11281v1

---

## 메타 / 디버그
- model: gemini-2.5-flash
- backend: gemini-flash-sdk
- matched_n: 100
- matched_total_before_cap: 212
- window_days: 119
- tokens_in_uncached: 24954
- tokens_in_cached_read: 163635
- tokens_out: 7938
- usd_estimate: $0.0396
- deep: True
- deep_k: 10
- deep_pdfs_ok: 9
- deep_pdfs_failed: 1
- pdf_archive: reports/2026-04-29-jailbreaking-gemini-flash-deep/
- pdf_archive_linked: 9
- pdf_archive_copied: 0
- pdf_archive_missing: 1
