# Research Topic Suggestion — "smart contract"

생성: 2026-05-06T03:44:12.314773+00:00
DB 윈도우: 1998-12-20 ~ 2026-05-06 (9999d)
모델: gemini-2.5-flash
매칭 논문: 100건
확장 키워드: ['smart contract', 'blockchain contract', 'self-executing contract', 'decentralized application', 'DeFi protocol', 'DAO governance', 'smart contract security', 'smart contract auditing', 'solidity contract', 'web3 agreement']

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — AI/ML 기반 스마트 계약 보안
- **설명**: AI/ML 기술, 특히 LLM, GNN을 활용하여 스마트 계약의 취약점을 탐지하고, 보안 감사 및 공격 코드 생성 등 보안 강화를 위한 연구들을 모았습니다.
- **빈도**: 30건
- **구간별 (≈2499d씩, 오래된→최근)**: 1 → 2 → 18 → 9
- **대표 논문**:
  - [P-NEURIPS-f774ca] Detecting Bugs with Substantial Monetary Consequences by LLM and Rule-based Reasoning — Brian Zhang, ZHUO ZHANG, NeurIPS 2024
  - [P-AAAI-bfaeff] SCALM: Detecting Bad Practices in Smart Contracts Through LLMs — Zongwei Li, Xiaoqi Li, Wenkai Li et al., AAAI 2025
  - [P-2603.26270] Knowdit: Agentic Smart Contract Vulnerability Detection with Auditing Knowledge Summarization — Ziqiao Kong, Wanxu Xia, Chong Wang et al., arXiv 2026

### 클러스터 2 — AI 에이전트 분산 시스템
- **설명**: 블록체인 기반 환경에서 AI 에이전트의 활동 조정, 거버넌스, 자율성 및 상호작용 방식, 그리고 이로 인해 발생할 수 있는 보안 위협 및 신뢰 문제에 대한 연구들을 다룹니다.
- **빈도**: 19건
- **구간별 (≈2499d씩, 오래된→최근)**: 1 → 0 → 9 → 9
- **대표 논문**:
  - [P-ICML-984919] Ethereum AI Agent Coordinator (EAAC): A Framework for AI Agent Activity Coordination — Taehoon Kim, ICML 2024
  - [P-2604.07007] AgentCity: Constitutional Governance for Autonomous Agent Economies via Separation of Power — Anbang Ruan, Xing Zhang, arXiv 2026
  - [P-2508.02773] Web3 x AI Agents: Landscape, Integrations, and Foundational Challenges — Yiming Shen, Jiashuo Zhang, Zhenzhe Shao et al., arXiv 2025

### 클러스터 3 — 분산형 AI/ML & 블록체인 응용
- **설명**: 분산형 머신러닝(페더레이티드 학습), 데이터 마켓플레이스, 제로-지식 증명 기반 ML 등 AI/ML 기술이 블록체인과 융합되어 다양한 실제 응용 분야(예: 스마트 시티, 금융, IoT)에서 신뢰성, 프라이버시, 효율성을 높이는 연구들을 포함합니다.
- **빈도**: 21건
- **구간별 (≈2499d씩, 오래된→최근)**: 0 → 1 → 10 → 10
- **대표 논문**:
  - [P-EXPERTSY-278b02] Blockchain for Large Language Models (LLMs): Applications, challenges, and framework implementation — Ahmad Musamih, Ibrar Yaqoob, Khaled Salah et al., Expert Systems with Applications 2026
  - [P-2512.10372] D2M: A Decentralized, Privacy-Preserving, Incentive-Compatible Data Marketplace for Collaborative Learning — Yash Srivastava, Shalin Jain, Sneha Awathare et al., arXiv 2025
  - [P-2510.16024] On-Chain Decentralized Learning and Cost-Effective Inference for DeFi Attack Mitigation — Abdulrahman Alhaidari, Balaji Palanisamy, Prashant Krishnamurthy, arXiv 2025

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap gap_1 — 대규모 언어 모델(LLM)을 활용한 스마트 계약 보안 연구에서 환각, 제한된 컨텍스트 처리, 도메인 특화 능력 부족 등의 고질적인 문제점이 반복
- **타입**: recurring-limitation
- **설명**: 대규모 언어 모델(LLM)을 활용한 스마트 계약 보안 연구에서 환각, 제한된 컨텍스트 처리, 도메인 특화 능력 부족 등의 고질적인 문제점이 반복적으로 지적됩니다. 이로 인해 LLM의 예측 신뢰성과 실제 적용 가능성이 저해되고 있습니다.
- **근거 논문**: P-NEURIPS-f774ca, P-2505.15242, P-2507.22371, P-2601.06914
- **Skeptic 검토**: ✓ 통과 — 제시된 LLM의 한계는 해당 연구 분야에서 반복적으로 지적되며 다양한 방식으로 개선 시도 중인 '고질적인 제한점'으로 판단되어 유효한 갭입니다.

### Gap gap_3 — AI 에이전트가 암호화폐 및 스마트 계약과 직접 상호작용하는 Web3 환경에서, 에이전트 자체를 악의적인 계약이나 조작된 컨텍스트로부터 보호하고
- **타입**: between-clusters
- **설명**: AI 에이전트가 암호화폐 및 스마트 계약과 직접 상호작용하는 Web3 환경에서, 에이전트 자체를 악의적인 계약이나 조작된 컨텍스트로부터 보호하고, 에이전트의 오작동이 야기할 수 있는 새로운 유형의 AI 위해(harm)를 완화하는 연구가 부족합니다.
- **근거 논문**: P-2507.08249, P-2503.16248
- **Skeptic 검토**: ✓ 통과 — AI 에이전트와 Web3 환경의 상호작용에서 발생하는 새로운 AI 위해 및 에이전트 보호에 대한 연구는 초기 단계이며, 제시된 논문들이 문제 제기 및 초기 탐색에 그치고 있어 추가적인 연구 필요성이 인정됩니다.

### Gap gap_5 — LLM 기반 스마트 계약 테스트 케이스 생성 분야에서 돌연변이 테스팅 기법 중 '돌연변이 우선순위화'를 통해 효율적인 테스트 케이스를 생성하고 
- **타입**: single-shot
- **설명**: LLM 기반 스마트 계약 테스트 케이스 생성 분야에서 돌연변이 테스팅 기법 중 '돌연변이 우선순위화'를 통해 효율적인 테스트 케이스를 생성하고 최적화하는 연구는 특정 단발성 논문에서만 구체적으로 다루어져, 이 분야의 추가적인 탐색이 필요합니다.
- **근거 논문**: P-2505.05584
- **Skeptic 검토**: ✓ 통과 — LLM 기반 스마트 계약 테스트 케이스 생성에서 '돌연변이 우선순위화'라는 특정 기법이 단일 논문에서만 심층적으로 다뤄져, 해당 분야의 추가 연구가 필요하다는 갭 주장은 타당합니다.

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap gap_2** — 블록체인 기반의 분산 AI 에이전트 시스템에서 에이전트의 자율성이 증대됨에 따라, 그들의 행동에 대한 투명한 감사, 책임 있는 거버넌스 모델, 그리고 시스템 전반의 검증 가능한 신뢰를 확립하는 것이 주요 과제로 남아있습니다. · 거부 사유: 해당 클러스터('AI 에이전트 분산 시스템') 내에서 이미 투명한 감사, 책임 있는 거버넌스, 검증 가능한 신뢰를 위한 프레임워크와 아키텍처를 직접적으로 제안하는 논문들이 다수 존재하여 ('arxiv:2604.07007', 'arxiv:2604.04265', 'arxiv:2603.25100') '부족한' 갭으로 보기 어렵습니다.
- **Gap gap_4** — 스마트 계약 코드 수준의 심층적인 취약점 탐지 및 완화 기법(AI/ML 기반 스마트 계약 보안 클러스터)과 페더레이티드 학습, 분산 데이터 마켓 등 복잡한 분산형 AI/ML 응용 시스템(분산형 AI/ML & 블록체인 응용 클러스터)의 전반적인 보안 및 무결성 강화 사이의 명시적인 연계 연구가 부족합니다. · 거부 사유: 제시된 증거 논문들(예: 'title:rafn', 'title:ai-driven zero trust and blockchain framework for secure electric vehicle infrastructure', 'arxiv:2602.08014', 'arxiv:2510.16024')이 AI/ML 기반 보안 기법과 스마트 계약을 활용한 분산형 시스템의 보안 강화를 명시적으로 연계하고 통합하는 연구를 수행하고 있으므로, '연계 연구가 부족하다'는 갭의 전제 자체가 사실과 다릅니다.

</details>

## 3. 연구 제안 (Proposer)

### 제안 1 — C-RAAG
**가설**: 컨텍스트 인식 RAG와 강화 학습 기반의 에이전트 조정 메커니즘을 통합하면 LLM의 스마트 계약 환각 및 제한된 컨텍스트 처리 문제를 완화하여 보안 취약점 탐지 신뢰도를 향상시킬 수 있다.
**메우는 갭**: gap_1
**접근**: 스마트 계약의 전체 실행 맥락(Control Flow Graph, Data Flow Graph, Call Graph)을 동적으로 쿼리하고, 정적 분석 도구의 결과를 RAG 프레임워크에 통합하여 LLM에 풍부한 컨텍스트를 제공한다. 에이전트 기반 시스템에서 각 LLM 에이전트의 역할(분석, 검증, 설명)을 강화 학습으로 조정하여, 불확실성이 높은 경우 추가적인 정보 탐색을 유도하고 다수결 기반의 결함 분류 및 설명 메커니즘을 적용한다.
**Baselines**: LLMBugScanner, SolEval, SCALM, CodeT5, T5, Llama, Claude 3 Opus, Slither, Foundry
**예상 기여**: LLM 기반 스마트 계약 보안 감사의 신뢰성과 설명 가능성을 높여, 실제 배포된 계약의 잠재적 위험을 효과적으로 줄일 수 있다. 특히 복잡한 비즈니스 로직에 내재된 취약점 탐지율을 개선하고, 오탐율을 낮추는 데 기여할 것이다.
**참고**: P-NEURIPS-f774ca, P-2505.15242, P-2507.22371, P-2601.06914, P-2512.02069, P-2509.09942

### 제안 2 — AEGIS-W3A
**가설**: 블록체인 기반의 분산형 신원(DID)과 스마트 계약으로 enforce되는 제로-트러스트 보안 모델을 AI 에이전트 생태계에 도입하면, 악의적인 컨텍스트 조작 및 계약 기반 공격으로부터 에이전트를 보호하고 책임성을 강화하여 새로운 AI 위해를 효과적으로 완화할 수 있다.
**메우는 갭**: gap_3
**접근**: AI 에이전트 간 상호작용 및 스마트 계약 호출에 대한 모든 접근을 제로-트러스트 원칙에 따라 처리하며, DID를 통해 각 에이전트의 신원을 검증하고 권한을 부여한다. 스마트 계약을 활용하여 에이전트의 행동 규칙(policy)을 온체인에서 강제하고, 모든 중요한 의사결정 및 외부 상호작용 이력을 불변의 블록체인에 기록하여 사후 감사를 가능하게 한다. 특히, Context Manipulation 공격에 대응하기 위해, 입력 프롬프트 및 메모리 모듈의 무결성을 검증하는 온체인 해시 검증 메커니즘과, 에이전트 행위 이상 감지 시 스마트 계약을 통한 즉각적인 권한 회수 기능을 구현한다.
**Baselines**: ElizaOS, Random Forest, Autoencoder, Isolation Forest models
**예상 기여**: Web3 환경에서 AI 에이전트의 자율성이 증대됨에 따라 발생할 수 있는 잠재적 보안 위협과 경제적 손실을 줄이고, 에이전트의 신뢰성과 책임성을 크게 향상시켜 Web3 AI 시스템의 안전한 발전을 촉진할 수 있다.
**참고**: P-2507.08249, P-2503.16248, P-2508.02773, P-2508.01332, P-EXPERTSY-47ae22, P-ICML-984919, P-2604.25555

### 제안 3 — OPTI-MUTA
**가설**: 강화 학습 기반의 동적 커리큘럼 학습과 메타 학습을 통합하여 LLM 기반 스마트 계약 테스트 케이스 생성 시 돌연변이 우선순위화의 효율성을 극대화하고, 이를 통해 테스트 스위트의 크기를 줄이면서도 높은 돌연변이 커버리지를 달성할 수 있다.
**메우는 갭**: gap_5
**접근**: `PRIMG`에서 제안된 돌연변이 우선순위화 모듈을 확장하여, 메타 학습 기반의 돌연변이 유용성 예측 모델을 개발한다. 이 모델은 다양한 계약 유형과 취약점 패턴에 걸쳐 학습된 지식을 활용하여 새로운 계약에 대한 초기 우선순위를 정확하게 설정한다. 또한, 강화 학습 에이전트가 생성된 테스트 케이스의 돌연변이 살상 능력을 실시간으로 평가하고, 가장 영향력 있는 돌연변이를 대상으로 하는 테스트 케이스를 생성하도록 동적으로 보상을 조절하는 커리큘럼 학습 전략을 도입한다. 이를 통해 테스트 생성의 탐색 공간을 효율적으로 관리하고, 기존 LLM의 한계인 엣지 케이스 처리 능력을 개선한다.
**Baselines**: PRIMG, GPT-5, SolCMC, Certora Prover, DeepSeek-R1, CodeLlama, Foundry, Slither
**예상 기여**: 스마트 계약 테스트 과정의 효율성을 획기적으로 향상시키고, 테스트 자원 소모를 최소화하면서도 광범위한 취약점을 탐지할 수 있는 고품질 테스트 스위트 생성을 가능하게 한다. 이는 개발 및 감사 프로세스에서 비용과 시간을 절감하는 데 중요한 기여를 할 것이다.
**참고**: P-2505.05584, P-2509.19153, P-2509.23976, P-2601.06914, P-2602.13808, P-NEURIPS-f774ca

## 4. 참고문헌 (메타DB 기반)

### 클러스터 1 — AI/ML 기반 스마트 계약 보안 (30)
- [P-NEURIPS-f774ca] Detecting Bugs with Substantial Monetary Consequences by LLM and Rule-based Reasoning, Brian Zhang, ZHUO ZHANG, NeurIPS 2024 · https://openreview.net/forum?id=hB5NkiET32
- [P-AAAI-bfaeff] SCALM: Detecting Bad Practices in Smart Contracts Through LLMs, Zongwei Li, Xiaoqi Li, Wenkai Li et al., AAAI 2025 · https://openreview.net/forum?id=AWpsdUpOCs
- [P-2603.28128] ORACAL: A Robust and Explainable Multimodal Framework for Smart Contract Vulnerability Detection with Causal Graph Enrichment, Tran Duong Minh Dai, Triet Huynh Minh Le, M. Ali Babar et al., arXiv 2026 · http://arxiv.org/abs/2603.28128v1
- [P-2603.27734] Robust Smart Contract Vulnerability Detection via Contrastive Learning-Enhanced Granular-ball Training, Zeli Wang, Qingxuan Yang, Shuyin Xia et al., arXiv 2026 · http://arxiv.org/abs/2603.27734v1
- [P-2603.26270] Knowdit: Agentic Smart Contract Vulnerability Detection with Auditing Knowledge Summarization, Ziqiao Kong, Wanxu Xia, Chong Wang et al., arXiv 2026 · http://arxiv.org/abs/2603.26270v1
- [P-2603.21149] Emergent Formal Verification: How an Autonomous AI Ecosystem Independently Discovered SMT-Based Safety Across Six Domains, Octavian Untila, arXiv 2026 · http://arxiv.org/abs/2603.21149v1
- [P-2603.13239] Benchmarking Zero-Shot Reasoning Approaches for Error Detection in Solidity Smart Contracts, Eduardo Sardenberg, Antonio José Grandson Busson, Daniel de Sousa Moraes et al., arXiv 2026 · http://arxiv.org/abs/2603.13239v2
- [P-2602.04418] SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing, Indraveni Chebolu, Arnab Mallick, Harmesh Rana, arXiv 2026 · http://arxiv.org/abs/2602.04418v3
- [P-2601.06914] Towards Compositional Generalization in LLMs for Smart Contract Security: A Case Study on Reentrancy Vulnerabilities, Ying Zhou, Jiacheng Wei, Yu Qi et al., arXiv 2026 · http://arxiv.org/abs/2601.06914v1
- [P-2512.09385] BugSweeper: Function-Level Detection of Smart Contract Vulnerabilities Using Graph Neural Networks, Uisang Lee, Changhoon Chung, Junmo Lee et al., arXiv 2025 · http://arxiv.org/abs/2512.09385v2
- [P-2512.02069] Large Language Model based Smart Contract Auditing with LLMBugScanner, Yining Yuan, Yifei Wang, Yichang Xu et al., arXiv 2025 · http://arxiv.org/abs/2512.02069v1
- [P-2511.02780] PoCo: Agentic Proof-of-Concept Exploit Generation for Smart Contracts, Vivi Andersson, Sofia Bobadilla, Harald Hobbelhagen et al., arXiv 2025 · http://arxiv.org/abs/2511.02780v3
- [P-2510.17919] ParaVul: A Parallel Large Language Model and Retrieval-Augmented Framework for Smart Contract Vulnerability Detection, Tenghui Huang, Jinbo Wen, Jiawen Kang et al., arXiv 2025 · http://arxiv.org/abs/2510.17919v1
- [P-2509.19153] LLMs as verification oracles for Solidity, Massimo Bartoletti, Enrico Lipparini, Livio Pompianu, arXiv 2025 · http://arxiv.org/abs/2509.19153v2
- [P-2509.13023] Validating Solidity Code Defects using Symbolic and Concrete Execution powered by Large Language Models, Ştefan-Claudiu Susan, Andrei Arusoaie, Dorel Lucanu, arXiv 2025 · http://arxiv.org/abs/2509.13023v1
- [P-2509.09942] Towards Secure and Explainable Smart Contract Generation with Security-Aware Group Relative Policy Optimization, Lei Yu, Jingyuan Zhang, Xin Wang et al., arXiv 2025 · http://arxiv.org/abs/2509.09942v2
- [P-2509.07131] SoK: Security and Privacy of AI Agents for Blockchain, Nicolò Romandini, Carlo Mazzocca, Kai Otsuki et al., arXiv 2025 · http://arxiv.org/abs/2509.07131v1
- [P-2509.05681] SEASONED: Semantic-Enhanced Self-Counterfactual Explainable Detection of Adversarial Exploiter Contracts, Xng Ai, Shudan Lin, Zecheng Li et al., arXiv 2025 · http://arxiv.org/abs/2509.05681v1
- [P-2508.01371] Prompt to Pwn: Automated Exploit Generation for Smart Contracts, ZeKe Xiao, Qin Wang, Yuekang Li et al., arXiv 2025 · http://arxiv.org/abs/2508.01371v3
- [P-2508.01343] UEChecker: Detecting Unchecked External Call Vulnerabilities in DApps via Graph Analysis, Dechao Kong, Xiaoqi Li, Wenkai Li, arXiv 2025 · http://arxiv.org/abs/2508.01343v2
- [P-2507.22371] SAEL: Leveraging Large Language Models with Adaptive Mixture-of-Experts for Smart Contract Vulnerability Detection, Lei Yu, Shiqi Cheng, Zhirong Huang et al., arXiv 2025 · http://arxiv.org/abs/2507.22371v1
- [P-2507.16840] CASPER: Contrastive Approach for Smart Ponzi Scheme Detecter with More Negative Samples, Weijia Yang, Tian Lan, Leyuan Liu et al., arXiv 2025 · http://arxiv.org/abs/2507.16840v1
- [P-2507.05558] AI Agent Smart Contract Exploit Generation, Arthur Gervais, Liyi Zhou, arXiv 2025 · http://arxiv.org/abs/2507.05558v4
- [P-2506.18245] Smart-LLaMA-DPO: Reinforced Large Language Model for Explainable Smart Contract Vulnerability Detection, Lei Yu, Zhirong Huang, Hang Yuan et al., arXiv 2025 · http://arxiv.org/abs/2506.18245v1
- [P-2506.06735] Ai-Driven Vulnerability Analysis in Smart Contracts: Trends, Challenges and Future Directions, Mesut Ozdag, arXiv 2025 · http://arxiv.org/abs/2506.06735v1
- [P-2505.19059] An Initial Exploration of Fine-tuning Small Language Models for Smart Contract Reentrancy Vulnerability Detection, Ignacio Mariano Andreozzi Pofcher, Joshua Ellul, arXiv 2025 · http://arxiv.org/abs/2505.19059v1
- [P-2505.15242] Adaptive Plan-Execute Framework for Smart Contract Security Auditing, Zhiyuan Wei, Jing Sun, Zijian Zhang et al., arXiv 2025 · http://arxiv.org/abs/2505.15242v2
- [P-2504.21480] A Comprehensive Study of Exploitable Patterns in Smart Contracts: From Vulnerability to Defense, Yuchen Ding, Hongli Peng, Xiaoqi Li, arXiv 2025 · http://arxiv.org/abs/2504.21480v1
- [P-2504.21043] CodeBC: A More Secure Large Language Model for Smart Contract Code Generation in Blockchain, Lingxiang Wang, Hainan Zhang, Qinnan Zhang et al., arXiv 2025 · http://arxiv.org/abs/2504.21043v2
- [P-2504.16113] AI-Based Vulnerability Analysis of NFT Smart Contracts, Xin Wang, Xiaoqi Li, arXiv 2025 · http://arxiv.org/abs/2504.16113v3

### 클러스터 2 — AI 에이전트 분산 시스템 (19)
- [P-ICML-984919] Ethereum AI Agent Coordinator (EAAC): A Framework for AI Agent Activity Coordination, Taehoon Kim, ICML 2024 · https://openreview.net/forum?id=n2dVVwZwPP
- [P-2605.00420] Foresight Arena: An On-Chain Benchmark for Evaluating AI Forecasting Agents, Maksym Nechepurenko, Pavel Shuvalov, arXiv 2026 · http://arxiv.org/abs/2605.00420v1
- [P-2604.25555] From CRUD to Autonomous Agents: Formal Validation and Zero-Trust Security for Semantic Gateways in AI-Native Enterprise Systems, Ignacio Peyrano, arXiv 2026 · http://arxiv.org/abs/2604.25555v1
- [P-2604.07007] AgentCity: Constitutional Governance for Autonomous Agent Economies via Separation of Power, Anbang Ruan, Xing Zhang, arXiv 2026 · http://arxiv.org/abs/2604.07007v1
- [P-2604.04265] Governance-Constrained Agentic AI: Blockchain-Enforced Human Oversight for Safety-Critical Wildfire Monitoring, Ali Akarma, Toqeer Ali Syed, Salman Jan et al., arXiv 2026 · http://arxiv.org/abs/2604.04265v1
- [P-2603.25100] From Logic Monopoly to Social Contract: Separation of Power and the Institutional Foundations for Autonomous Agent Economies, Anbang Ruan, arXiv 2026 · http://arxiv.org/abs/2603.25100v1
- [P-2603.05027] S5-SHB Agent: Society 5.0 enabled Multi-model Agentic Blockchain Framework for Smart Home, Janani Rangila, Akila Siriweera, Incheon Paik et al., arXiv 2026 · http://arxiv.org/abs/2603.05027v2
- [P-2603.04915] EVMbench: Evaluating AI Agents on Smart Contract Security, Justin Wang, Andreas Bigger, Xiaohai Xu et al., arXiv 2026 · http://arxiv.org/abs/2603.04915v1
- [P-2511.15456] Know Your Intent: An Autonomous Multi-Perspective LLM Agent Framework for DeFi User Transaction Intent Mining, Qian'ang Mao, Yuxuan Zhang, Jiaman Chen et al., arXiv 2025 · http://arxiv.org/abs/2511.15456v1
- [P-2510.21117] DAO-AI: Evaluating Collective Decision-Making through Agentic AI in Decentralized Governance, Agostino Capponi, Alfio Gliozzo, Chunghyun Han et al., arXiv 2025 · http://arxiv.org/abs/2510.21117v2
- [P-2509.15956] Swarm Oracle: Trustless Blockchain Agreements through Robot Swarms, Alexandre Pacheco, Hanqing Zhao, Volker Strobel et al., arXiv 2025 · http://arxiv.org/abs/2509.15956v1
- [P-2508.21368] EconAgentic in DePIN Markets: A Large Language Model Approach to the Sharing Economy of Decentralized Physical Infrastructure, Yulin Liu, Mocca Schweitzer, arXiv 2025 · http://arxiv.org/abs/2508.21368v1
- [P-2508.02773] Web3 x AI Agents: Landscape, Integrations, and Foundational Challenges, Yiming Shen, Jiashuo Zhang, Zhenzhe Shao et al., arXiv 2025 · http://arxiv.org/abs/2508.02773v3
- [P-2508.01332] BlockA2A: Towards Secure and Verifiable Agent-to-Agent Interoperability, Zhenhua Zou, Zhuotao Liu, Lepeng Zhao et al., arXiv 2025 · http://arxiv.org/abs/2508.01332v3
- [P-2507.17134] Resilient Multi-Agent Negotiation for Medical Supply Chains:Integrating LLMs and Blockchain for Transparent Coordination, Mariam ALMutairi, Hyungmin Kim, arXiv 2025 · http://arxiv.org/abs/2507.17134v1
- [P-2507.11117] AI Agent Architecture for Decentralized Trading of Alternative Assets, Ailiya Borjigin, Cong He, Charles CC Lee et al., arXiv 2025 · http://arxiv.org/abs/2507.11117v1
- [P-2507.08249] Giving AI Agents Access to Cryptocurrency and Smart Contracts Creates New Vectors of AI Harm, Bill Marino, Ari Juels, arXiv 2025 · http://arxiv.org/abs/2507.08249v2
- [P-2505.09757] Trustless Autonomy: Understanding Motivations, Benefits, and Governance Dilemmas in Self-Sovereign Decentralized AI Agents, Botao Amber Hu, Yuhan Liu, Helena Rong, arXiv 2025 · http://arxiv.org/abs/2505.09757v2
- [P-2503.16248] Real AI Agents with Fake Memories: Fatal Context Manipulation Attacks on Web3 Agents, Atharv Singh Patlan, Peiyao Sheng, S. Ashwin Hebbar et al., arXiv 2025 · http://arxiv.org/abs/2503.16248v3

### 클러스터 3 — 분산형 AI/ML & 블록체인 응용 (20)
- [P-EXPERTSY-47ae22] AI-driven zero trust and blockchain framework for secure electric vehicle infrastructure, Clement Daah, Ysabel Fallot, Amna Qureshi et al., Expert Systems with Applications 2026 · https://doi.org/10.1016/j.eswa.2026.131577
- [P-EXPERTSY-278b02] Blockchain for Large Language Models (LLMs): Applications, challenges, and framework implementation, Ahmad Musamih, Ibrar Yaqoob, Khaled Salah et al., Expert Systems with Applications 2026 · https://doi.org/10.1016/j.eswa.2026.131100
- [P-EXPERTSY-ec81f5] RAFN: A risk-aware feature network for identifying risk factors in supply chain finance, Yang Zhang, Yating Zhao, Wenjuan Lian et al., Expert Systems with Applications 2025 · https://doi.org/10.1016/j.eswa.2025.129874
- [P-2604.22096] Who Audits the Auditor? Tamper-Proof Fraud Detection with Blockchain-Anchored Explainable ML, Zhaohui Wang, arXiv 2026 · http://arxiv.org/abs/2604.22096v1
- [P-2603.11299] Counterweights and Complementarities: The Convergence of AI and Blockchain Powering a Decentralized Future, Yibai Li, Zhiye Jin, Xiaobing et al., arXiv 2026 · http://arxiv.org/abs/2603.11299v1
- [P-2602.17973] PenTiDef: Enhancing Privacy and Robustness in Decentralized Federated Intrusion Detection Systems against Poisoning Attacks, Phan The Duy, Nghi Hoang Khoa, Nguyen Tran Anh Quan et al., arXiv 2026 · http://arxiv.org/abs/2602.17973v1
- [P-2602.08290] Trust-Based Incentive Mechanisms in Semi-Decentralized Federated Learning Systems, Ajay Kumar Shrestha, arXiv 2026 · http://arxiv.org/abs/2602.08290v1
- [P-2602.08014] ICBAC: an Intelligent Contract-Based Access Control framework for supply chain management by integrating blockchain and federated learning, Sadegh Sohani, Salar Ghazi, Farnaz Kamranfar et al., arXiv 2026 · http://arxiv.org/abs/2602.08014v1
- [P-2601.22302] ZK-HybridFL: Zero-Knowledge Proof-Enhanced Hybrid Ledger for Federated Learning, Amirhossein Taherpour, Xiaodong Wang, arXiv 2026 · http://arxiv.org/abs/2601.22302v1
- [P-2512.10372] D2M: A Decentralized, Privacy-Preserving, Incentive-Compatible Data Marketplace for Collaborative Learning, Yash Srivastava, Shalin Jain, Sneha Awathare et al., arXiv 2025 · http://arxiv.org/abs/2512.10372v1
- [P-2511.07577] A Decentralized Retrieval Augmented Generation System with Source Reliabilities Secured on Blockchain, Yining Lu, Wenyi Tang, Max Johnson et al., arXiv 2025 · http://arxiv.org/abs/2511.07577v1 · also_in: hf
- [P-2510.18109] PrivaDE: Privacy-preserving Data Evaluation for Blockchain-based Data Marketplaces, Wan Ki Wong, Sahel Torkamani, Michele Ciampi et al., arXiv 2025 · http://arxiv.org/abs/2510.18109v4
- [P-2510.16024] On-Chain Decentralized Learning and Cost-Effective Inference for DeFi Attack Mitigation, Abdulrahman Alhaidari, Balaji Palanisamy, Prashant Krishnamurthy, arXiv 2025 · http://arxiv.org/abs/2510.16024v1
- [P-2510.06784] Bionetta: Efficient Client-Side Zero-Knowledge Machine Learning Proving, Dmytro Zakharov, Oleksandr Kurbatov, Artem Sdobnov et al., arXiv 2025 · http://arxiv.org/abs/2510.06784v2
- [P-2510.04765] LMM-Incentive: Large Multimodal Model-based Incentive Design for User-Generated Content in Web 3.0, Jinbo Wen, Jiawen Kang, Linfeng Zhang et al., arXiv 2025 · http://arxiv.org/abs/2510.04765v1
- [P-2508.16189] A Relay-Chain-Powered Ciphertext-Policy Attribute-Based Encryption in Intelligent Transportation Systems, Aparna Singh, Geetanjali Rathee, Chaker Abdelaziz Kerrache et al., arXiv 2025 · http://arxiv.org/abs/2508.16189v1
- [P-2505.06632] AI-Powered Anomaly Detection with Blockchain for Real-Time Security and Reliability in Autonomous Vehicles, Rathin Chandra Shit, Sharmila Subudhi, arXiv 2025 · http://arxiv.org/abs/2505.06632v1
- [P-2505.01866] PQS-BFL: A Post-Quantum Secure Blockchain-based Federated Learning Framework, Daniel Commey, Garth V. Crosby, arXiv 2025 · http://arxiv.org/abs/2505.01866v1
- [P-2504.20275] Smart Water Security with AI and Blockchain-Enhanced Digital Twins, Mohammadhossein Homaei, Victor Gonzalez Morales, Oscar Mogollon Gutierrez et al., arXiv 2025 · http://arxiv.org/abs/2504.20275v1
- [P-2503.17426] Enhanced Smart Contract Reputability Analysis using Multimodal Data Fusion on Ethereum, Cyrus Malik, Josef Bajada, Joshua Ellul, arXiv 2025 · http://arxiv.org/abs/2503.17426v2

### 기타 (클러스터 미분류) (31)
- [P-VLDB-ab948d] Practical Declarative Smart Contracts Optimization, Lan Lu, Tao Luo, Jingyi Li et al., VLDB 2024 · https://openreview.net/forum?id=ZVRRgOVA95
- [P-EMNLP-4c9050] SolEval: Benchmarking Large Language Models for Repository-level Solidity Smart Contract Generation, Zhiyuan Peng, Xin Yin, Rui Qian et al., EMNLP 2025 · https://openreview.net/forum?id=v1WxaZvDyn
- [P-2602.22045] DLT-Corpus: A Large-Scale Text Collection for the Distributed Ledger Technology Domain, Walter Hernandez Cruz, Peter Devine, Nikhil Vadgama et al., arXiv 2026 · http://arxiv.org/abs/2602.22045v1 · also_in: hf
- [P-2602.13808] An end-to-end agentic pipeline for smart contract translation and quality evaluation, Abhinav Goel, Chaitya Shah, Agostino Capponi et al., arXiv 2026 · http://arxiv.org/abs/2602.13808v1
- [P-2601.15177] Dynamic Management of a Deep Learning-Based Anomaly Detection System for 5G Networks, Lorenzo Fernández Maimó, Alberto Huertas Celdrán, Manuel Gil Pérez et al., arXiv 2026 · http://arxiv.org/abs/2601.15177v1
- [P-2601.02313] Game of Coding: Coding Theory in the Presence of Rational Adversaries, Motivated by Decentralized Machine Learning, Hanzaleh Akbari Nodehi, Viveck R. Cadambe, Mohammad Ali Maddah-Ali, arXiv 2026 · http://arxiv.org/abs/2601.02313v1
- [P-2511.12971] Esim: EVM Bytecode Similarity Detection Based on Stable-Semantic Graph, Zhuo Chen, Gaoqiang Ji, Yiling He et al., arXiv 2025 · http://arxiv.org/abs/2511.12971v1
- [P-2510.22561] Blockchain Signatures to Ensure Information Integrity and Non-Repudiation in the Digital Era: A comprehensive study, Kaveri Banerjee, Sajal Saha, arXiv 2025 · http://arxiv.org/abs/2510.22561v1
- [P-2510.05487] Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective, Jinho Cha, Sahng-Min Han, Long Pham, arXiv 2025 · http://arxiv.org/abs/2510.05487v1
- [P-2509.24515] Agentic Specification Generator for Move Programs, Yu-Fu Fu, Meng Xu, Taesoo Kim, arXiv 2025 · http://arxiv.org/abs/2509.24515v1
- [P-2509.23976] Curriculum-Guided Reinforcement Learning for Synthesizing Gas-Efficient Financial Derivatives Contracts, Maruf Ahmed Mridul, Oshani Seneviratne, arXiv 2025 · http://arxiv.org/abs/2509.23976v1
- [P-2509.11555] Dstack: A Zero Trust Framework for Confidential Containers, Shunfan Zhou, Kevin Wang, Hang Yin, arXiv 2025 · http://arxiv.org/abs/2509.11555v1
- [P-2508.12671] DIT: Dimension Reduction View on Optimal NFT Rarity Meters, Dmitry Belousov, Yury Yanovich, arXiv 2025 · http://arxiv.org/abs/2508.12671v1
- [P-2507.23087] On LLM-Assisted Generation of Smart Contracts from Business Processes, Fabian Stiehle, Hans Weytjens, Ingo Weber, arXiv 2025 · http://arxiv.org/abs/2507.23087v1
- [P-2508.09993] A Transparent Fairness Evaluation Protocol for Open-Source Language Model Benchmarking on the Blockchain, Hugo Massaroli, Leonardo Iara, Emmanuel Iarussi et al., arXiv 2025 · http://arxiv.org/abs/2508.09993v1
- [P-2507.20774] evalSmarT: An LLM-Based Framework for Evaluating Smart Contract Generated Comments, Fatou Ndiaye Mbodji, arXiv 2025 · http://arxiv.org/abs/2507.20774v1
- [P-2507.19411] SILS: Strategic Influence on Liquidity Stability and Whale Detection in Concentrated-Liquidity DEXs, Ali RajabiNekoo, Laleh Rasoul, Amirfarhad Farhadi et al., arXiv 2025 · http://arxiv.org/abs/2507.19411v1
- [P-2507.15761] GasAgent: A Multi-Agent Framework for Automated Gas Optimization in Smart Contracts, Jingyi Zheng, Zifan Peng, Yule Liu et al., arXiv 2025 · http://arxiv.org/abs/2507.15761v1
- [P-2506.16649] Automated Energy Billing with Blockchain and the Prophet Forecasting Model: A Holistic Approach, Ajesh Thangaraj Nadar, Soham Chandane, Gabriel Nixon Raj et al., arXiv 2025 · http://arxiv.org/abs/2506.16649v1
- [P-2506.00943] Legal Compliance Evaluation of Smart Contracts Generated By Large Language Models, Chanuka Wijayakoon, Hai Dong, H. M. N. Dilum Bandara et al., arXiv 2025 · http://arxiv.org/abs/2506.00943v1
- [P-2506.00505] From Rules to Rewards: Reinforcement Learning for Interest Rate Adjustment in DeFi Lending, Hanxiao Qu, Krzysztof Gogol, Florian Groetschla et al., arXiv 2025 · http://arxiv.org/abs/2506.00505v1
- [P-2505.08542] Guiding LLM-based Smart Contract Generation with Finite State Machine, Hao Luo, Yuhao Lin, Xiao Yan et al., arXiv 2025 · http://arxiv.org/abs/2505.08542v1
- [P-2505.05584] PRIMG : Efficient LLM-driven Test Generation Using Mutant Prioritization, Mohamed Salah Bouafif, Mohammad Hamdaqa, Edward Zulkoski, arXiv 2025 · http://arxiv.org/abs/2505.05584v1
- [P-2504.17539] Proof of Useful Intelligence (PoUI): Blockchain Consensus Beyond Energy Waste, Zan-Kai Chong, Hiroyuki Ohsaki, Bryan Ng, arXiv 2025 · http://arxiv.org/abs/2504.17539v1
- [P-2504.15063] Mining Characteristics of Vulnerable Smart Contracts Across Lifecycle Stages, Hongli Peng, Xiaoqi Li, Wenkai Li, arXiv 2025 · http://arxiv.org/abs/2504.15063v1
- [P-2504.16116] DMind Benchmark: Toward a Holistic Assessment of LLM Capabilities across the Web3 Domain, Enhao Huang, Pengyu Sun, Zixin Lin et al., arXiv 2025 · http://arxiv.org/abs/2504.16116v3
- [P-2504.11702] Clustering and analysis of user behaviour in blockchain: A case study of Planet IX, Dorottya Zelenyanszki, Zhe Hou, Kamanashis Biswas et al., arXiv 2025 · http://arxiv.org/abs/2504.11702v1
- [P-2504.09517] RoboComm: A DID-based scalable and privacy-preserving Robot-to-Robot interaction over state channels, Roshan Singh, Sushant Pandey, arXiv 2025 · http://arxiv.org/abs/2504.09517v3
- [P-2503.06203] Generation of Optimized Solidity Code for Machine Learning Models using LLMs, Nikumbh Sarthak Sham, Sandip Chakraborty, Shamik Sural, arXiv 2025 · http://arxiv.org/abs/2503.06203v1
- [P-2503.01098] Towards Automated Smart Contract Generation: Evaluation, Benchmarking, and Retrieval-Augmented Repair, Zaoyu Chen, Haoran Qin, Nuo Chen et al., arXiv 2025 · http://arxiv.org/abs/2503.01098v2
- [P-2502.16955] MTVHunter: Smart Contracts Vulnerability Detection Based on Multi-Teacher Knowledge Translation, Guokai Sun, Yuan Zhuang, Shuo Zhang et al., arXiv 2025 · http://arxiv.org/abs/2502.16955v1

---

## 메타 / 디버그
- model: gemini-2.5-flash
- backend: gemini-flash-sdk
- matched_n: 100
- matched_total_before_cap: 118
- window_days: 9999
- tokens_in_uncached: 8459
- tokens_in_cached_read: 118568
- tokens_out: 5612
- usd_estimate: $0.0255
