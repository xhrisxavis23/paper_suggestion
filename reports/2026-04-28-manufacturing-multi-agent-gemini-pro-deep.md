# Research Topic Suggestion — "manufacturing multi agent"

생성: 2026-04-28T09:34:34.297479+00:00
DB 윈도우: 2025-12-29 ~ 2026-04-28 (120d)
모델: gemini-2.5-pro
매칭 논문: 100건
확장 키워드: ['manufacturing', 'industrial', 'factory', 'production', 'assembly', 'multi-agent', 'multiagent', 'multi agent', 'agent-based', 'multi-robot']

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — LLM 기반 에이전트 프레임워크
- **설명**: LLM(대형 언어 모델)을 핵심으로 활용하여 산업 및 제조 환경의 특정 문제를 해결하기 위한 새로운 다중 에이전트 아키텍처 및 프레임워크를 제안하는 연구 그룹입니다. 주로 지식 그래프 구축, 예지 보전, 공정 자동화, 코드 생성 등의 작업을 다룹니다.
- **빈도**: 18건
- **월별 (≈30d씩, 오래된→최근)**: 1 → 4 → 8 → 5
- **대표 논문**:
  - [P-IEEETRAN-bf3127] CoMA-IKG: LLM-Driven Multiagent Framework for Automated Construction of Industrial Knowledge Graph — Jing Zhang, Haiteng Wang, Zidi Jia et al., IEEE Trans. Industrial Informatics 2026
  - [P-2603.29755] CausalPulse: An Industrial-Grade Neurosymbolic Multi-Agent Copilot for Causal Diagnostics in Smart Manufacturing — Chathurangi Shyalika, Utkarshani Jaimini, Cory Henson et al., arXiv 2026
  - [P-2603.02669] IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models — Xiangyu Su, Juzhan Xu, Oliver van Kaick et al., arXiv 2026

### 클러스터 2 — 다중 로봇 협업 및 최적화
- **설명**: 물리적인 제조 또는 산업 환경에서 다수의 로봇(AMR, 드론 등)이나 에이전트의 협업을 다루는 연구 클러스터입니다. 주로 작업 할당, 경로 계획, 스케줄링, 충돌 회피 및 자원 최적화와 같은 핵심적인 운영 문제를 해결하는 데 중점을 둡니다.
- **빈도**: 14건
- **월별 (≈30d씩, 오래된→최근)**: 3 → 0 → 9 → 2
- **대표 논문**:
  - [P-2604.24117] An Analysis of the Coordination Gap between Joint and Modular Learning for Job Shop Scheduling with Transportation Resources — Moritz Link, Jonathan Hoss, Noah Klarmann, arXiv 2026
  - [P-2603.26542] The Multi-AMR Buffer Storage, Retrieval, and Reshuffling Problem: Exact and Heuristic Approaches — Max Disselnmeyer, Thomas Bömer, Laura Dörr et al., arXiv 2026
  - [P-2603.20577] LASER: Level-Based Asynchronous Scheduling and Execution Regime for Spatiotemporally Constrained Multi-Robot Timber Manufacturing — Zhenxiang Huang, Lior Skoury, Tim Stark et al., arXiv 2026

### 클러스터 3 — 시스템 아키텍처, 거버넌스 및 보안
- **설명**: 산업 및 기업 환경에서 다중 에이전트 시스템을 안정적으로 배포하고 운영하기 위한 시스템 수준의 아키텍처, 거버넌스, 보안 및 신뢰성 문제를 다룹니다. 특정 알고리즘 개발보다는 안전 정책, 데이터 프라이버시, 공격 탐지, 시스템 확장성을 보장하는 프레임워크에 초점을 맞춥니다.
- **빈도**: 15건
- **월별 (≈30d씩, 오래된→최근)**: 0 → 2 → 7 → 6
- **대표 논문**:
  - [P-2604.17240] Safe and Policy-Compliant Multi-Agent Orchestration for Enterprise AI — Vinil Pasupuleti, Shyalendar Reddy Allala, Siva Rama Krishna Varma Bayyavarapu et al., arXiv 2026
  - [P-2603.17787] Governed Memory: A Production Architecture for Multi-Agent Workflows — Hamed Taheri, arXiv 2026
  - [P-2603.15408] TrinityGuard: A Unified Framework for Safeguarding Multi-Agent Systems — Kai Wang, Biaojie Zeng, Zeming Wei et al., arXiv 2026

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap B — 다수의 논문들이 새로운 다중 에이전트 '프레임워크'나 '아키텍처'를 제안하지만, 이들의 실제 산업 환경으로의 확장성(scalability)과 배
- **타입**: recurring-limitation
- **설명**: 다수의 논문들이 새로운 다중 에이전트 '프레임워크'나 '아키텍처'를 제안하지만, 이들의 실제 산업 환경으로의 확장성(scalability)과 배포 복잡성은 반복적으로 나타나는 한계점입니다. 많은 연구가 시뮬레이션 환경이나 특정 데이터셋에서 검증되어, 대규모의 동적인 실제 산업 환경에서의 성능, 비용, 안정성을 입증하는 데에는 한계가 있습니다. 이는 실제 배포 시 계산 비용과 통신 오버헤드가 기하급수적으로 증가할 수 있기 때문입니다.
- **근거 논문**: P-2603.22651, P-2603.26542, P-2603.29755
- **Skeptic 검토**: ✓ 통과 — 증거 논문들이 '산업 스케일에서는 계산적으로 다루기 어렵다'거나 '생산 스케일링 전략'을 벤치마킹하는 등, 확장성이 핵심적인 실용적 제약 조건임을 명확히 보여주므로 통과합니다.

### Gap C — LLM 기반의 고수준 인지 계획(클러스터 1)과 물리 로봇의 저수준 실시간 제어(클러스터 2)를 효과적으로 통합하는 방법에 대한 연구가 부족합니
- **타입**: between-clusters
- **설명**: LLM 기반의 고수준 인지 계획(클러스터 1)과 물리 로봇의 저수준 실시간 제어(클러스터 2)를 효과적으로 통합하는 방법에 대한 연구가 부족합니다. 클러스터 1의 연구들은 복잡한 추론과 작업 분해에 강점을 보이지만, LLM의 확률적이고 느린 응답 시간은 클러스터 2에서 요구하는 빠르고 결정론적인 로봇 제어와 상충됩니다. 이 두 계층을 매끄럽게 연결하는 '신경-심볼릭' 인터페이스나 하이브리드 아키텍처가 필요합니다.
- **근거 논문**: P-2603.02669, P-2604.00061, P-IEEETRAN-91eb27
- **Skeptic 검토**: ✓ 통과 — 증거 논문(`arxiv:2603.02669`)이 LLM을 고수준 계획에만 사용하고 저수준 실행은 결정론적 솔버에 의존하는 아키텍처를 제시함으로써, 두 영역 간의 기술적 격차가 실재함을 입증하므로 통과합니다.

### Gap E — 다중 에이전트 LLM 시스템의 API 호출 비용 및 토큰 효율성은 실용화를 가로막는 주요 장벽으로 여러 논문에서 암시되거나 직접적으로 언급됩니다
- **타입**: recurring-limitation
- **설명**: 다중 에이전트 LLM 시스템의 API 호출 비용 및 토큰 효율성은 실용화를 가로막는 주요 장벽으로 여러 논문에서 암시되거나 직접적으로 언급됩니다. 복잡한 문제를 해결하기 위해 여러 에이전트가 협업하면 LLM 호출이 크게 증가하여 상당한 비용과 지연을 유발합니다. 일부 연구는 비용-정확도 트레이드오프를 분석하거나 프롬프트 압축을 시도하지만, 비용 효율적인 협업 프로토콜이나 경량 에이전트 설계는 여전히 중요한 연구 과제입니다.
- **근거 논문**: P-2603.22651, P-2603.23525, P-2604.19856
- **Skeptic 검토**: ✓ 통과 — 증거 논문들이 '높은 API 비용'을 명시적으로 언급하고 비용-정확도 트레이드오프와 프롬프트 압축을 직접적으로 연구하는 등, 비용이 시스템 설계의 핵심 제약임을 강력하게 뒷받침하므로 통과합니다.

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap A** — 물리적 다중 로봇 시스템(클러스터 2)과 LLM 에이전트 보안 및 거버넌스(클러스터 3) 사이에 명확한 연구 갭이 존재합니다. 클러스터 3의 연구들은 프롬프트 인젝션, 데이터 유출, 정책 준수 등 정보 시스템 수준의 위협을 다루지만, 이러한 보안 모델이 실시간으로 동작하는 물리적 로봇 시스템에 어떻게 적용될 수 있는지에 대한 연구는 부족합니다. 예를 들어, 로봇 운영 기술(OT) 환경에서의 에이전트 공격 탐지 및 방어 프레임워크는 아직 초기 단계에 머물러 있습니다. · 거부 사유: 다른 클러스터에서 이미 다룸. 증거로 제시된 논문 `arxiv:2603.24221` 자체가 '로봇 환경에서의 자율 침투 테스트'를 다루며, 클러스터 3(보안)의 개념을 클러스터 2(로봇)의 도메인에 직접 적용하고 있어 해당 갭이 이미 메타DB 내에서 해결되고 있음을 보여줍니다.
- **Gap D** — 다중 로봇 협업 클러스터 내에서, `arxiv:2603.01076` 논문은 비정방 시스템의 분산 제어 가능성에 대한 고전 제어 이론 기반의 수학적 토대를 제시합니다. 이 연구는 MARL(다중 에이전트 강화학습) 환경의 안정성을 보장하기 위한 엄밀한 접근법을 제안하지만, 클러스터 내 다른 연구들은 주로 휴리스틱, 최적화 기법, 또는 실용적인 시스템 프레임워크에 초점을 맞추고 있습니다. 이 이론적 연구를 후속으로 확장하거나 실제 시스템에 적용한 연구는 보이지 않습니다. · 거부 사유: trivial 함. 해당 논문이 유일한 이론적 접근이라는 전제가 틀렸습니다. 같은 클러스터 내의 `title:virtual damping injection adaptive feedback system for quadcopter formation applications via order reduction approach` 역시 PD 제어기, 전달 함수 등 엄밀한 제어 이론을 사용하므로, `arxiv:2603.01076`이 단발성 연구라는 주장의 근거가 약합니다.

</details>

## 3. 연구 제안 (Proposer)

### 제안 1 — SCALE-MAS
**가설**: 동적 자원 할당과 통신 압축을 결합한 경량 오케스트레이션 레이어는 기존 다중 에이전트 프레임워크의 산업 배포 시 통신 오버헤드와 계산 비용을 특정 임계치 이하로 유지할 수 있다.
**메우는 갭**: B
**접근**: 본 연구는 기존 다중 에이전트 시스템 위에 동작하는 미들웨어 오케스트레이션 레이어를 제안한다. 이 레이어는 실시간으로 시스템의 계산 부하와 통신 대역폭을 모니터링하며, 강화학습(PPO) 기반 정책을 사용해 에이전트의 활성화 빈도와 메시지 페이로드 크기를 동적으로 조절한다. 이를 통해 복잡하고 무거운 에이전트 프레임워크를 자원이 제한된 산업용 엣지 디바이스 환경에서도 안정적으로 운영할 수 있도록 한다.
**Baselines**: CausalPulse, hierarchical supervisor-worker, reflexive self-correcting loop
**예상 기여**: 학술적 프로토타입과 실제 산업 등급 시스템 간의 격차를 해소하는 실용적인 배포 솔루션을 제공한다. 새로운 아키텍처를 제안하는 대신 기존 아키텍처의 확장성과 경제성을 확보하는 데 중점을 두어, 산업 현장에서의 다중 에이전트 시스템 도입을 가속화할 수 있다.
**참고**: P-2603.29755, P-2603.22651, P-2603.26542

### 제안 2 — NEXUS-CTRL
**가설**: LLM이 생성한 상위 수준의 작업 계획을 결정론적 제어 프리미티브(control primitive)로 변환하고 실시간으로 검증하는 신경-심볼릭 인터페이스는 다중 로봇 시스템의 작업 성공률을 높이면서도 응답 지연 시간을 허용 범위 내로 유지할 수 있다.
**메우는 갭**: C
**접근**: LLM이 고수준의 작업 계획 그래프를 생성하면, 제안하는 NEXUS-CTRL 계층이 각 그래프 노드를 사전 정의되고 정형적으로 검증 가능한 '스킬'로 변환한다. 이 스킬은 MPC(Model Predictive Control)나 최적 제어 솔버를 위한 제약 조건 집합으로 표현된다. 이 2계층 아키텍처는 LLM의 확률적 출력을 결정론적이고 안전이 보장된 물리적 행동으로 변환하여, 인지적 계획과 물리적 제어 사이의 간극을 효과적으로 연결한다.
**Baselines**: IMR-LLM, decentralised model predictive control (MPC), A* search
**예상 기여**: 물리적 시스템에 LLM 기반 자율성을 안전하게 배포하기 위한 구체적이고 구현 가능한 아키텍처를 제공한다. 미션 크리티컬한 로봇 제어에 확률적 모델을 사용할 때 발생하는 안전 및 신뢰성 문제를 정면으로 해결하여, 산업 자동화 분야에서 LLM의 활용 가능성을 크게 확장할 것이다.
**참고**: P-2603.02669, P-2603.19838, P-2604.00061

### 제안 3 — ECO-AGENTS
**가설**: 대형 언어 모델(LLM)과 특정 작업에 맞게 증류된 소형 모델(SLM)을 계층적으로 결합하고, 작업 복잡도에 따라 동적으로 호출을 라우팅하는 다중 에이전트 시스템은 순수 LLM 기반 시스템 대비 API 비용을 50% 이상 절감하면서도 95% 수준의 작업 정확도를 유지할 수 있다.
**메우는 갭**: E
**접근**: 중앙 오케스트레이터 에이전트(LLM)가 복잡한 작업을 분해한 뒤, 각 하위 작업의 요구사항을 분석하여 강력한 추론이 필요하면 다른 LLM 에이전트에게, 단순하고 반복적인 작업은 경량화된 PEFT(Parameter-Efficient Fine-Tuned) 모델들에게 동적으로 라우팅한다. 이 라우팅 결정은 작업에 필요한 추론 능력과 비용을 예측하는 학습된 정책에 의해 이루어지며, 에이전트 간 통신에는 압축된 구조적 포맷을 사용하여 토큰 사용량을 최소화한다.
**Baselines**: reflexive architectures, prompt compression
**예상 기여**: 비용 효율적이면서도 강력한 다중 에이전트 시스템을 구축하기 위한 구체적인 아키텍처 패턴을 제시한다. 예산 제약이 중요한 실제 산업 환경에서 에이전트 기술의 경제적 실행 가능성을 높여, 기술 도입의 핵심 장벽 중 하나를 해결한다.
**참고**: P-2603.22651, P-2603.23525, P-2604.19856

## 4. 참고문헌 (메타DB 기반)

### 클러스터 1 — LLM 기반 에이전트 프레임워크 (18)
- [P-EXPERTSY-537c52] Agentic AI for autonomous preventive maintenance policy governance: a multi-agent framework for dynamic industrial environments, Adolfo Crespo Márquez, Juan F. Gómez Fernández, Expert Systems with Applications 2026 · https://doi.org/10.1016/j.eswa.2026.131767
- [P-IEEETRAN-bf3127] CoMA-IKG: LLM-Driven Multiagent Framework for Automated Construction of Industrial Knowledge Graph, Jing Zhang, Haiteng Wang, Zidi Jia et al., IEEE Trans. Industrial Informatics 2026 · https://doi.org/10.1109/tii.2026.3660116
- [P-2604.19856] ChipCraftBrain: Validation-First RTL Generation via Multi-Agent Orchestration, Cagri Eryilmaz, arXiv 2026 · http://arxiv.org/abs/2604.19856v1
- [P-2604.14989] Dr.~RTL: Autonomous Agentic RTL Optimization through Tool-Grounded Self-Improvement, Wenji Fang, Yao Lu, Shang Liu et al., arXiv 2026 · http://arxiv.org/abs/2604.14989v1
- [P-2604.09889] In-situ process monitoring for defect detection in wire-arc additive manufacturing: an agentic AI approach, Pallock Halder, Satyajit Mojumder, arXiv 2026 · http://arxiv.org/abs/2604.09889v1
- [P-2604.05550] AutoSOTA: An End-to-End Automated Research System for State-of-the-Art AI Model Discovery, Yu Li, Chenyang Shao, Xinyang Liu et al., arXiv 2026 · http://arxiv.org/abs/2604.05550v1
- [P-2604.04208] Towards Agentic Defect Reasoning: A Graph-Assisted Retrieval Framework for Laser Powder Bed Fusion, Muhammad Rizwan Awan, Volker Pickert, Muhammad Waqar Ashraf et al., arXiv 2026 · http://arxiv.org/abs/2604.04208v1
- [P-2603.29755] CausalPulse: An Industrial-Grade Neurosymbolic Multi-Agent Copilot for Causal Diagnostics in Smart Manufacturing, Chathurangi Shyalika, Utkarshani Jaimini, Cory Henson et al., arXiv 2026 · http://arxiv.org/abs/2603.29755v1
- [P-2603.24629] Sketch2Simulation: Automating Flowsheet Generation via Multi Agent Large Language Models, Abdullah Bahamdan, Emma Pajak, John D. Hedengren et al., arXiv 2026 · http://arxiv.org/abs/2603.24629v1
- [P-2603.16313] Learning to Predict, Discover, and Reason in High-Dimensional Event Sequences, Hugo Math, arXiv 2026 · http://arxiv.org/abs/2603.16313v2
- [P-2603.07970] Advancing Automated Algorithm Design via Evolutionary Stagewise Design with LLMs, Chen Lu, Ke Xue, Chengrui Gao et al., arXiv 2026 · http://arxiv.org/abs/2603.07970v1
- [P-2603.02669] IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models, Xiangyu Su, Juzhan Xu, Oliver van Kaick et al., arXiv 2026 · http://arxiv.org/abs/2603.02669v1
- [P-2603.01654] CeProAgents: A Hierarchical Agents System for Automated Chemical Process Development, Yuhang Yang, Ruikang Li, Jifei Ma et al., arXiv 2026 · http://arxiv.org/abs/2603.01654v1
- [P-2602.20543] Beyond Human Performance: A Vision-Language Multi-Agent Approach for Quality Control in Pharmaceutical Manufacturing, Subhra Jyoti Mandal, Lara Rachidi, Puneet Jain et al., arXiv 2026 · http://arxiv.org/abs/2602.20543v1
- [P-2602.16738] Self-Evolving Multi-Agent Network for Industrial IoT Predictive Maintenance, Rebin Saleh, Khanh Pham Dinh, Balázs Villányi et al., arXiv 2026 · http://arxiv.org/abs/2602.16738v1
- [P-2602.13370] G2CP: A Graph-Grounded Communication Protocol for Verifiable and Efficient Multi-Agent Reasoning, Karim Ben Khaled, Davy Monticolo, arXiv 2026 · http://arxiv.org/abs/2602.13370v1
- [P-2603.12813] Context is all you need: Towards autonomous model-based process design using agentic AI in flowsheet simulations, Pascal Schäfer, Lukas J. Krinke, Martin Wlotzka et al., arXiv 2026 · http://arxiv.org/abs/2603.12813v1
- [P-2603.22651] Benchmarking Multi-Agent LLM Architectures for Financial Document Processing: A Comparative Study of Orchestration Patterns, Cost-Accuracy Tradeoffs and Production Scaling Strategies, Siddhant Kulkarni, Yukta Kulkarni, arXiv 2026 · http://arxiv.org/abs/2603.22651v1

### 클러스터 2 — 다중 로봇 협업 및 최적화 (14)
- [P-IEEETRAN-91eb27] Distributed Moving Horizon Estimation Over Sporadically Observing Sensor Networks: An L-Step Approach With Stability Guarantees, Antonello Venturino, Cristina Stoica, Sylvain Bertrand et al., IEEE Trans. Industrial Informatics 2026 · https://doi.org/10.1109/tii.2026.3659476
- [P-IEEETRAN-f4c14f] Fairness-Aware Deterministic Joint Offloading and Scheduling for Industrial Edge Computing, Yingfei Yao, Nan Zhou, Shunchun Yao et al., IEEE Trans. Industrial Informatics 2026 · https://doi.org/10.1109/tii.2026.3654608
- [P-IEEETRAN-e7e4c2] Virtual Damping Injection Adaptive Feedback System for Quadcopter Formation Applications via Order Reduction Approach, Kwan Soo Kim, Chao Xu, Seok-Kyoon Kim et al., IEEE Trans. Industrial Informatics 2026 · https://doi.org/10.1109/tii.2026.3657595
- [P-2604.24117] An Analysis of the Coordination Gap between Joint and Modular Learning for Job Shop Scheduling with Transportation Resources, Moritz Link, Jonathan Hoss, Noah Klarmann, arXiv 2026 · http://arxiv.org/abs/2604.24117v1
- [P-2604.00061] Advancing Multi-Robot Networks via MLLM-Driven Sensing, Communication, and Computation: A Comprehensive Survey, Hyun Jong Yang, Howon Lee, Kyuhong Shim et al., arXiv 2026 · http://arxiv.org/abs/2604.00061v1
- [P-2603.26542] The Multi-AMR Buffer Storage, Retrieval, and Reshuffling Problem: Exact and Heuristic Approaches, Max Disselnmeyer, Thomas Bömer, Laura Dörr et al., arXiv 2026 · http://arxiv.org/abs/2603.26542v2
- [P-2603.23967] Wireless communication empowers online scheduling of partially-observable transportation multi-robot systems in a smart factory, Yaxin Liao, Qimei Cui, Kwang-Cheng Chen et al., arXiv 2026 · http://arxiv.org/abs/2603.23967v1
- [P-2603.23690] ROSCell: A ROS2-Based Framework for Automated Formation and Orchestration of Multi-Robot Systems, Jiangtao Shuai, Marvin Carl May, Sonja Schimmler et al., arXiv 2026 · http://arxiv.org/abs/2603.23690v1
- [P-2603.21545] Auction-Based Task Allocation with Energy-Conscientious Trajectory Optimization for AMR Fleets, Jiachen Li, Soovadeep Bakshi, Jian Chu et al., arXiv 2026 · http://arxiv.org/abs/2603.21545v1
- [P-2603.20577] LASER: Level-Based Asynchronous Scheduling and Execution Regime for Spatiotemporally Constrained Multi-Robot Timber Manufacturing, Zhenxiang Huang, Lior Skoury, Tim Stark et al., arXiv 2026 · http://arxiv.org/abs/2603.20577v1
- [P-2603.19838] Multi-Agent Motion Planning on Industrial Magnetic Levitation Platforms: A Hybrid ADMM-HOCBF approach, Bavo Tistaert, Stan Servaes, Alejandro Gonzalez-Garcia et al., arXiv 2026 · http://arxiv.org/abs/2603.19838v1
- [P-2603.18260] Manufacturing Micro-Patterned Surfaces with Multi-Robot Systems, Annalisa T. Taylor, Malachi Landis, Ping Guo et al., arXiv 2026 · http://arxiv.org/abs/2603.18260v1
- [P-2603.07973] VORL-EXPLORE: A Hybrid Learning Planning Approach to Multi-Robot Exploration in Dynamic Environments, Ning Liu, Sen Shen, Zheng Li et al., arXiv 2026 · http://arxiv.org/abs/2603.07973v1
- [P-2603.01076] Feasible Pairings for Decentralized Integral Controllability of Non-Square Systems, Yuhao Tong, Steven W. Su, arXiv 2026 · http://arxiv.org/abs/2603.01076v1

### 클러스터 3 — 시스템 아키텍처, 거버넌스 및 보안 (15)
- [P-2604.17240] Safe and Policy-Compliant Multi-Agent Orchestration for Enterprise AI, Vinil Pasupuleti, Shyalendar Reddy Allala, Siva Rama Krishna Varma Bayyavarapu et al., arXiv 2026 · http://arxiv.org/abs/2604.17240v1
- [P-2604.16339] Semantic Consensus: Process-Aware Conflict Detection and Resolution for Enterprise Multi-Agent LLM Systems, Vivek Acharya, arXiv 2026 · http://arxiv.org/abs/2604.16339v1
- [P-2604.12129] Aethon: A Reference-Based Replication Primitive for Constant-Time Instantiation of Stateful AI Agents, Swanand Rao, Kiran Kashalkar, Parvathi Somashekar et al., arXiv 2026 · http://arxiv.org/abs/2604.12129v1
- [P-2604.11548] SemaClaw: A Step Towards General-Purpose Personal AI Agents through Harness Engineering, Ningyan Zhu, Huacan Wang, Jie Zhou et al., arXiv 2026 · http://arxiv.org/abs/2604.11548v1 · also_in: hf
- [P-2604.06392] Qualixar OS: A Universal Operating System for AI Agent Orchestration, Varun Pratap Bhardwaj, arXiv 2026 · http://arxiv.org/abs/2604.06392v1 · also_in: hf
- [P-2604.01647] Exploring Robust Multi-Agent Workflows for Environmental Data Management, Boyuan Guan, Jason Liu, Yanzhao Wu et al., arXiv 2026 · http://arxiv.org/abs/2604.01647v1
- [P-2603.28013] Kill-Chain Canaries: Stage-Level Tracking of Prompt Injection Across Attack Surfaces and Model Safety Tiers, Haochuan Kevin Wang, Zechen Zhang, arXiv 2026 · http://arxiv.org/abs/2603.28013v3
- [P-2603.24221] Environment-Grounded Multi-Agent Workflow for Autonomous Penetration Testing, Michael Somma, Markus Großpointner, Paul Zabalegui et al., arXiv 2026 · http://arxiv.org/abs/2603.24221v1
- [P-2603.17787] Governed Memory: A Production Architecture for Multi-Agent Workflows, Hamed Taheri, arXiv 2026 · http://arxiv.org/abs/2603.17787v1
- [P-2603.15727] ClawWorm: Self-Propagating Attacks Across LLM Agent Ecosystems, Yihao Zhang, Zeming Wei, Xiaokun Luan et al., arXiv 2026 · http://arxiv.org/abs/2603.15727v2
- [P-2603.15408] TrinityGuard: A Unified Framework for Safeguarding Multi-Agent Systems, Kai Wang, Biaojie Zeng, Zeming Wei et al., arXiv 2026 · http://arxiv.org/abs/2603.15408v1
- [P-2603.09002] Security Considerations for Multi-agent Systems, Tam Nguyen, Moses Ndebugre, Dheeraj Arremsetty, arXiv 2026 · http://arxiv.org/abs/2603.09002v1
- [P-2603.02345] RIVA: Leveraging LLM Agents for Reliable Configuration Drift Detection, Sami Abuzakuk, Lucas Crijns, Anne-Marie Kermarrec et al., arXiv 2026 · http://arxiv.org/abs/2603.02345v1
- [P-2602.11510] AgentLeak: A Full-Stack Benchmark for Privacy Leakage in Multi-Agent LLM Systems, Faouzi El Yagoubi, Godwin Badu-Marfo, Ranwa Al Mallah, arXiv 2026 · http://arxiv.org/abs/2602.11510v2
- [P-2602.11301] The PBSAI Governance Ecosystem: A Multi-Agent AI Reference Architecture for Securing Enterprise AI Estates, John M. Willis, arXiv 2026 · http://arxiv.org/abs/2602.11301v1

### 기타 (클러스터 미분류) (42)
- [P-2604.23993] EPM-RL: Reinforcement Learning for On-Premise Product Mapping in E-Commerce, Minhyeong Yu, Wonduk Seo, arXiv 2026 · http://arxiv.org/abs/2604.23993v1
- [P-2604.20658] Cooperative Profiles Predict Multi-Agent LLM Team Performance in AI for Science Workflows, Shivani Kumar, Adarsh Bharathwaj, David Jurgens, arXiv 2026 · http://arxiv.org/abs/2604.20658v1
- [P-2604.19540] Mesh Memory Protocol: Semantic Infrastructure for Multi-Agent LLM Systems, Hongwei Xu, arXiv 2026 · http://arxiv.org/abs/2604.19540v1
- [P-2604.17745] HiRAS: A Hierarchical Multi-Agent Framework for Paper-to-Code Generation and Execution, Hanhua Hong, Yizhi LI, Jiaoyan Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.17745v1
- [P-2604.16950] AutoPKG: An Automated Framework for Dynamic E-commerce Product-Attribute Knowledge Graph Construction, Pollawat Hongwimol, Haoning Shang, Chutong Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.16950v1
- [P-2604.11518] From Translation to Superset: Benchmark-Driven Evolution of a Production AI Agent from Rust to Python, Jinhua Wang, Biswa Sengupta, arXiv 2026 · http://arxiv.org/abs/2604.11518v1
- [P-2604.10992] ArtiCAD: Articulated CAD Assembly Design via Multi-Agent Code Generation, Yuan Shui, Yandong Guan, Zhanwei Zhang et al., arXiv 2026 · http://arxiv.org/abs/2604.10992v2
- [P-2604.09285] SAGE: A Service Agent Graph-guided Evaluation Benchmark, Ling Shi, Yuqin Dai, Ziyin Wang et al., arXiv 2026 · http://arxiv.org/abs/2604.09285v1
- [P-2604.07927] EigentSearch-Q+: Enhancing Deep Research Agents with Structured Reasoning Tools, Boer Zhang, Mingyan Wu, Dongzhuoran Zhou et al., arXiv 2026 · http://arxiv.org/abs/2604.07927v2
- [P-2604.06633] Argus: Reorchestrating Static Analysis via a Multi-Agent Ensemble for Full-Chain Security Vulnerability Detection, Zi Liang, Qipeng Xie, Jun He et al., arXiv 2026 · http://arxiv.org/abs/2604.06633v1
- [P-2604.05731] FoleyDesigner: Immersive Stereo Foley Generation with Precise Spatio-Temporal Alignment for Film Clips, Mengtian Li, Kunyan Dai, Yi Ding et al., arXiv 2026 · http://arxiv.org/abs/2604.05731v1
- [P-2604.04875] DIRECT: Video Mashup Creation via Hierarchical Multi-Agent Planning and Intent-Guided Editing, Ke Li, Maoliang Li, Jialiang Chen et al., arXiv 2026 · http://arxiv.org/abs/2604.04875v1
- [P-2604.03656] Beyond Retrieval: Modeling Confidence Decay and Deterministic Agentic Platforms in Generative Engine Optimization, XinYu Zhao, ChengYou Li, XiangBao Meng et al., arXiv 2026 · http://arxiv.org/abs/2604.03656v1
- [P-2604.03042] Enhancing Multi-Robot Exploration Using Probabilistic Frontier Prioritization with Dirichlet Process Gaussian Mixtures, John Lewis Devassy, Meysam Basiri, Mário A. T. Figueiredo et al., arXiv 2026 · http://arxiv.org/abs/2604.03042v1
- [P-2604.01520] LLM Agents as Social Scientists: A Human-AI Collaborative Platform for Social Science Automation, Lei Wang, Yuanzi Li, Jinchao Wu et al., arXiv 2026 · http://arxiv.org/abs/2604.01520v1
- [P-2604.00189] Making Sense of AI Agents Hype: Adoption, Architectures, and Takeaways from Practitioners, Ruoyu Su, Matteo Esposito, Roberta Capuano et al., arXiv 2026 · http://arxiv.org/abs/2604.00189v1
- [P-2603.28928] Towards Computational Social Dynamics of Semi-Autonomous AI Agents, S. O. Lidarity, U. N. Ionize, C. O. Llective et al., arXiv 2026 · http://arxiv.org/abs/2603.28928v1
- [P-2603.27303] Self-evolving AI agents for protein discovery and directed evolution, Yang Tan, Lingrong Zhang, Mingchen Li et al., arXiv 2026 · http://arxiv.org/abs/2603.27303v1
- [P-2603.27303] Self-evolving AI agents for protein discovery and directed evolution, Yang Tan, Lingrong Zhang, Mingchen Li et al., arXiv 2026 · http://arxiv.org/abs/2603.27303v1
- [P-2603.21489] Effective Strategies for Asynchronous Software Engineering Agents, Jiayi Geng, Graham Neubig, arXiv 2026 · http://arxiv.org/abs/2603.21489v1 · also_in: hf
- [P-2603.21489] Effective Strategies for Asynchronous Software Engineering Agents, Jiayi Geng, Graham Neubig, arXiv 2026 · http://arxiv.org/abs/2603.21489v1 · also_in: hf
- [P-2603.20678] AI-Driven Multi-Agent Simulation of Stratified Polyamory Systems: A Computational Framework for Optimizing Social Reproductive Efficiency, Yicai Xing, arXiv 2026 · http://arxiv.org/abs/2603.20678v1
- [P-2603.20131] An Agentic Multi-Agent Architecture for Cybersecurity Risk Management, Ravish Gupta, Saket Kumar, Shreeya Sharma et al., arXiv 2026 · http://arxiv.org/abs/2603.20131v2
- [P-2603.14553] An End-to-end Architecture for Collider Physics and Beyond, Shi Qiu, Zeyu Cai, Jiashen Wei et al., arXiv 2026 · http://arxiv.org/abs/2603.14553v1
- [P-2603.14052] A Multi-Agent Perception-Action Alliance for Efficient Long Video Reasoning, Yichang Xu, Gaowen Liu, Ramana Rao Kompella et al., arXiv 2026 · http://arxiv.org/abs/2603.14052v3
- [P-2603.15672] DRCY: Agentic Hardware Design Reviews, Kyle Dumont, Nicholas Herbert, Hayder Tirmazi et al., arXiv 2026 · http://arxiv.org/abs/2603.15672v1
- [P-2603.13023] daVinci-Env: Open SWE Environment Synthesis at Scale, Dayuan Fu, Shenyu Wu, Yunze Wu et al., arXiv 2026 · http://arxiv.org/abs/2603.13023v2 · also_in: hf
- [P-2603.13023] daVinci-Env: Open SWE Environment Synthesis at Scale, Dayuan Fu, Shenyu Wu, Yunze Wu et al., arXiv 2026 · http://arxiv.org/abs/2603.13023v2 · also_in: hf
- [P-2603.09152] DataFactory: Collaborative Multi-Agent Framework for Advanced Table Question Answering, Tong Wang, Chi Jin, Yongkang Chen et al., arXiv 2026 · http://arxiv.org/abs/2603.09152v1
- [P-2603.06007] MASFactory: A Graph-centric Framework for Orchestrating LLM-Based Multi-Agent Systems with Vibe Graphing, Yang Liu, Jinxuan Cai, Yishen Li et al., arXiv 2026 · http://arxiv.org/abs/2603.06007v1
- [P-2603.23525] Prompt Compression in Production Task Orchestration: A Pre-Registered Randomized Trial, Warren Johnson, Charles Lee, arXiv 2026 · http://arxiv.org/abs/2603.23525v1
- [P-2603.06007] MASFactory: A Graph-centric Framework for Orchestrating LLM-Based Multi-Agent Systems with Vibe Graphing, Yang Liu, Jinxuan Cai, Yishen Li et al., arXiv 2026 · http://arxiv.org/abs/2603.06007v1
- [P-2603.03565] Build, Judge, Optimize: A Blueprint for Continuous Improvement of Multi-Agent Consumer Assistants, Alejandro Breen Herrera, Aayush Sheth, Steven G. Xu et al., arXiv 2026 · http://arxiv.org/abs/2603.03565v1
- [P-2603.03565] Build, Judge, Optimize: A Blueprint for Continuous Improvement of Multi-Agent Consumer Assistants, Alejandro Breen Herrera, Aayush Sheth, Steven G. Xu et al., arXiv 2026 · http://arxiv.org/abs/2603.03565v1
- [P-2603.03565] Build, Judge, Optimize: A Blueprint for Continuous Improvement of Multi-Agent Consumer Assistants, Alejandro Breen Herrera, Aayush Sheth, Steven G. Xu et al., arXiv 2026 · http://arxiv.org/abs/2603.03565v1
- [P-2603.00805] NERFIFY: A Multi-Agent Framework for Turning NeRF Papers into Code, Seemandhar Jain, Keshav Gupta, Kunal Gupta et al., arXiv 2026 · http://arxiv.org/abs/2603.00805v1
- [P-2603.19248] DuCCAE: A Hybrid Engine for Immersive Conversation via Collaboration, Augmentation, and Evolution, Xin Shen, Zhishu Jiang, Jiaye Yang et al., arXiv 2026 · http://arxiv.org/abs/2603.19248v1
- [P-2603.08736] Autonomous Edge-Deployed AI Agents for Electric Vehicle Charging Infrastructure Management, Mohammed Cherifi, arXiv 2026 · http://arxiv.org/abs/2603.08736v1
- [P-2603.00130] Agentic Hives: Equilibrium, Indeterminacy, and Endogenous Cycles in Self-Organizing Multi-Agent Systems, Jean-Philippe Garnier, arXiv 2026 · http://arxiv.org/abs/2603.00130v1
- [P-2603.02240] SuperLocalMemory: Privacy-Preserving Multi-Agent Memory with Bayesian Trust Defense Against Memory Poisoning, Varun Pratap Bhardwaj, arXiv 2026 · http://arxiv.org/abs/2603.02240v1
- [P-2602.11790] Beyond End-to-End Video Models: An LLM-Based Multi-Agent System for Educational Video Generation, Lingyong Yan, Jiulong Wu, Dong Xie et al., arXiv 2026 · http://arxiv.org/abs/2602.11790v1
- [P-2604.20848] MATRAG: Multi-Agent Transparent Retrieval-Augmented Generation for Explainable Recommendations, Sushant Mehta, arXiv 2026 · http://arxiv.org/abs/2604.20848v1

---

## 메타 / 디버그
- model: gemini-2.5-pro
- backend: gemini-pro-sdk
- matched_n: 100
- matched_total_before_cap: 136
- window_days: 120
- tokens_in_uncached: 9544
- tokens_in_cached_read: 160160
- tokens_out: 6955
- usd_estimate: $0.1311
- deep: True
- deep_k: 5
- deep_pdfs_ok: 0
- deep_pdfs_failed: 5
- pdf_archive: reports/2026-04-28-manufacturing-multi-agent-gemini-pro-deep/
- pdf_archive_linked: 0
- pdf_archive_copied: 0
- pdf_archive_missing: 5
