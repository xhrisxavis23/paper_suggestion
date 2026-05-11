# On-chain × AI/ML 종합 우선순위 — LLM/Multi-Agent 우선

**Sources**:
- 📄 PDF baseline: `/home/dgu_wj92/sh/최근 3년 탑 컨퍼런스 온체인 데이터 연구 심층 분석.pdf` (5편)
- 📚 TRENDS.md (동료 분석, 48편 corpus)
- 🔍 우리 9개 쿼리 매치 (총 257 unique papers, BC×2+ 필터 후 112편)

**점수**: ⭐PDF=100, 📚TRENDS=50, multi-query=15×n, BC=5×match(max5), LLM=6×match(max4), venue weight=3×w

**필터**: PDF/TRENDS 명시 OR 블록체인 키워드 ≥2 매치 (word-boundary)

---

## 🔴 Tier S — 필수 (PDF baseline + TRENDS) — 3편

### Live Graph Lab: Towards Open, Dynamic and Real Transaction Graphs with NFT
- **NeurIPS** | 2023-06-01 | score=175
- Zhen Zhang, Bingqiao Luo, Shengliang Lu, et al.
- [https://openreview.net/forum?id=zr1e15kczE](https://openreview.net/forum?id=zr1e15kczE)
- ⭐Live Graph Lab | 📚TRENDS:live graph lab | BC[blockchain,nft]

### Money Never Sleeps: Maximizing Liquidity Mining Yields in Decentralized Finance
- **KDD** | 2024-01-01 | score=172
- Wangze Ni, Yiwei Zhao, Weijie Sun, et al.
- [https://openreview.net/forum?id=p0XpoNd3DC](https://openreview.net/forum?id=p0XpoNd3DC)
- ⭐Money Never Sleeps | 📚TRENDS:money never sleeps | BC[cryptocurrency,decentralized finance]

### Chainlet Orbits: Topological Address Embedding for Blockchain
- **KDD** | 2025-01-01 | score=167
- Poupak Azad, Baris Coskunuzer, Murat Kantarcioglu, et al.
- [https://openreview.net/forum?id=kDoNkhwucW](https://openreview.net/forum?id=kDoNkhwucW)
- ⭐Chainlet Orbits | 📚TRENDS:chainlet orbits | BC[blockchain]

## 🟠 Tier A — 강력 추천 (TRENDS 명시 또는 강한 LLM/BC 시그널) — 4편

### SolEval: Benchmarking Large Language Models for Repository-level Solidity Smart Contract Generation
- **EMNLP** | 2025-01-01 | score=83
- Zhiyuan Peng, Xin Yin, Rui Qian, et al.
- [https://openreview.net/forum?id=v1WxaZvDyn](https://openreview.net/forum?id=v1WxaZvDyn)
- 📚TRENDS:soleval | BC[ethereum,smart contract,solidity] | LLM[llm]

### BlockScan: Detecting Anomalies in Blockchain Transactions
- **NeurIPS** | 2025-05-10 | score=81
- Jiahao Yu, Xian Wu, Hao Liu, et al.
- [https://openreview.net/forum?id=URB690A5r5](https://openreview.net/forum?id=URB690A5r5)
- 📚TRENDS:blockscan | BC[blockchain,ethereum] | LLM[transformer]

### SCALM: Detecting Bad Practices in Smart Contracts Through LLMs
- **AAAI** | 2025-01-01 | score=81
- Zongwei Li, Xiaoqi Li, Wenkai Li, et al.
- [https://openreview.net/forum?id=AWpsdUpOCs](https://openreview.net/forum?id=AWpsdUpOCs)
- 📚TRENDS:scalm | BC[ethereum,smart contract] | LLM[rag,retrieval-augmented]

### Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics
- **KDD** | 2023-01-01 | score=77
- Youssef Elmougy, Ling Liu
- [https://openreview.net/forum?id=au2qMV3HJk](https://openreview.net/forum?id=au2qMV3HJk)
- 📚TRENDS:demystifying fraudulent | BC[blockchain,cryptocurrency,bitcoin]

## 🟡 Tier B — 관련 (블록체인 + LLM/agent) — 2편

- **[73]** [arXiv] 2025-04-18 — DMind Benchmark: Toward a Holistic Assessment of LLM Capabilities across the Web3 Domain
  - Enhao Huang, Pengyu Sun, et al. | 2쿼리 | BC[blockchain,smart contract,on-chain] | LLM[llm,claude]
- **[50]** [arXiv] 2025-11-19 — Know Your Intent: An Autonomous Multi-Perspective LLM Agent Framework for DeFi User Transaction Intent Mining
  - Qian'ang Mao, Yuxuan Zhang, et al. | BC[blockchain,smart contract,defi] | LLM[llm,large language model,language model]

## 🟡 Tier B — 관련 (블록체인 핵심, LLM 무관) — 4편

- **[71]** [arXiv] 2025-12-10 — BugSweeper: Function-Level Detection of Smart Contract Vulnerabilities Using Graph Neural Networks
  - Uisang Lee, Changhoon Chung, et al. | 📚TRENDS:bugsweeper | BC[ethereum,smart contract,solidity]
- **[67]** [KDD] 2024-01-01 — COMET: NFT Price Prediction with Wallet Profiling
  - Tianfu Wang, Liwei Deng, et al. | 📚TRENDS:comet | BC[nft]
- **[56]** [arXiv] 2026-04-22 — Towards Event-Aware Forecasting in DeFi: Insights from On-chain Automated Market Maker Protocols
  - Huaiyu Jia, Jiehshun You, et al. | 2쿼리 | BC[on-chain,defi,decentralized finance]
- **[51]** [arXiv] 2025-08-18 — DIT: Dimension Reduction View on Optimal NFT Rarity Meters
  - Dmitry Belousov, Yury Yanovich | 2쿼리 | BC[bitcoin,ethereum,nft]

## ⚪ Tier C — 참고 — 66편

- **[40]** [arXiv] 2025-10-20 — ParaVul: A Parallel Large Language Model and Retrieval-Augmented Framework for Smart Contr
- **[40]** [arXiv] 2025-07-23 — Resilient Multi-Agent Negotiation for Medical Supply Chains:Integrating LLMs and Blockchai
- **[39]** [arXiv] 2025-12-02 — Leveraging Large Language Models to Bridge Cross-Domain Transparency in Stablecoins
- **[36]** [ICML] 2024-05-26 — Ethereum AI Agent Coordinator (EAAC): A Framework for AI Agent Activity Coordination
- **[34]** [arXiv] 2025-10-23 — Human-Centered LLM-Agent System for Detecting Anomalous Digital Asset Transactions
- **[34]** [arXiv] 2026-01-08 — Autonomous Agents on Blockchains: Standards, Execution Models, and Trust Boundaries
- **[34]** [arXiv] 2025-07-21 — GasAgent: A Multi-Agent Framework for Automated Gas Optimization in Smart Contracts
- **[34]** [arXiv] 2025-06-23 — Smart-LLaMA-DPO: Reinforced Large Language Model for Explainable Smart Contract Vulnerabil
- **[33]** [arXiv] 2026-03-27 — Knowdit: Agentic Smart Contract Vulnerability Detection with Auditing Knowledge Summarizat
- **[33]** [arXiv] 2026-02-17 — Benchmarking Zero-Shot Reasoning Approaches for Error Detection in Solidity Smart Contract
- **[33]** [arXiv] 2025-07-08 — AI Agent Smart Contract Exploit Generation
- **[33]** [arXiv] 2025-04-28 — CodeBC: A More Secure Large Language Model for Smart Contract Code Generation in Blockchai
- **[33]** [arXiv] 2025-03-20 — Real AI Agents with Fake Memories: Fatal Context Manipulation Attacks on Web3 Agents
- **[32]** [arXiv] 2025-09-14 — Quantum and Classical Machine Learning in Decentralized Finance: Comparative Evidence from
- **[31]** [arXiv] 2025-11-17 — Esim: EVM Bytecode Similarity Detection Based on Stable-Semantic Graph
- **[31]** [arXiv] 2025-10-15 — On-Chain Decentralized Learning and Cost-Effective Inference for DeFi Attack Mitigation
- **[28]** [arXiv] 2026-04-05 — Governance-Constrained Agentic AI: Blockchain-Enforced Human Oversight for Safety-Critical
- **[28]** [arXiv] 2026-02-14 — An end-to-end agentic pipeline for smart contract translation and quality evaluation
- **[28]** [arXiv] 2025-07-30 — SAEL: Leveraging Large Language Models with Adaptive Mixture-of-Experts for Smart Contract
- **[28]** [arXiv] 2025-07-28 — evalSmarT: An LLM-Based Framework for Evaluating Smart Contract Generated Comments
- **[27]** [arXiv] 2025-01-13 — Improving DeFi Accessibility through Efficient Liquidity Provisioning with Deep Reinforcem
- **[27]** [arXiv] 2025-10-06 — LMM-Incentive: Large Multimodal Model-based Incentive Design for User-Generated Content in
- **[27]** [arXiv] 2025-09-28 — Curriculum-Guided Reinforcement Learning for Synthesizing Gas-Efficient Financial Derivati
- **[27]** [arXiv] 2025-08-04 — Web3 x AI Agents: Landscape, Integrations, and Foundational Challenges
- **[27]** [arXiv] 2025-06-07 — Ai-Driven Vulnerability Analysis in Smart Contracts: Trends, Challenges and Future Directi
- **[27]** [arXiv] 2025-03-03 — Towards Automated Smart Contract Generation: Evaluation, Benchmarking, and Retrieval-Augme
- **[26]** [arXiv] 2025-04-30 — A Comprehensive Study of Exploitable Patterns in Smart Contracts: From Vulnerability to De
- **[26]** [arXiv] 2025-04-24 — Proof of Useful Intelligence (PoUI): Blockchain Consensus Beyond Energy Waste
- **[25]** [ICAIF] 2024-01-01 — To Compete or Collude: Bidding Incentives in Ethereum Block Building Auctions
- **[22]** [arXiv] 2025-09-21 — Quantum Adaptive Self-Attention for Financial Rebalancing: An Empirical Study on Automated
- **[22]** [KDD] 2023-01-01 — NFT-Based Data Marketplace with Digital Watermarking
- **[22]** [arXiv] 2025-10-16 — The Bidding Games: Reinforcement Learning for MEV Extraction on Polygon Blockchain
- **[22]** [arXiv] 2026-05-01 — Foresight Arena: An On-Chain Benchmark for Evaluating AI Forecasting Agents
- **[22]** [arXiv] 2026-04-28 — From CRUD to Autonomous Agents: Formal Validation and Zero-Trust Security for Semantic Gat
- **[22]** [arXiv] 2026-04-08 — AgentCity: Constitutional Governance for Autonomous Agent Economies via Separation of Powe
- **[22]** [arXiv] 2025-09-23 — LLMs as verification oracles for Solidity
- **[22]** [arXiv] 2025-07-29 — A Transparent Fairness Evaluation Protocol for Open-Source Language Model Benchmarking on 
- **[22]** [arXiv] 2025-07-15 — AI Agent Architecture for Decentralized Trading of Alternative Assets
- **[22]** [arXiv] 2025-05-13 — Guiding LLM-based Smart Contract Generation with Finite State Machine
- **[22]** [arXiv] 2025-03-08 — Generation of Optimized Solidity Code for Machine Learning Models using LLMs
- **[21]** [arXiv] 2025-03-06 — Slow is Fast! Dissecting Ethereum's Slow Liquidity Drain Scams
- **[21]** [arXiv] 2025-04-06 — SolRPDS: A Dataset for Analyzing Rug Pulls in Solana Decentralized Finance
- **[21]** [arXiv] 2025-07-28 — Deep Reputation Scoring in DeFi: zScore-Based Wallet Ranking from Liquidity and Trading Si
- **[21]** [arXiv] 2026-03-05 — EVMbench: Evaluating AI Agents on Smart Contract Security
- **[21]** [arXiv] 2025-09-08 — SoK: Security and Privacy of AI Agents for Blockchain
- **[21]** [arXiv] 2025-07-25 — SILS: Strategic Influence on Liquidity Stability and Whale Detection in Concentrated-Liqui
- **[21]** [arXiv] 2025-04-18 — AI-Based Vulnerability Analysis of NFT Smart Contracts
- **[21]** [arXiv] 2025-03-21 — Enhanced Smart Contract Reputability Analysis using Multimodal Data Fusion on Ethereum
- **[19]** [Expert Systems wit] 2026-02-08 — AI-driven zero trust and blockchain framework for secure electric vehicle infrastructure
- **[19]** [Expert Systems wit] 2025-09-27 — RAFN: A risk-aware feature network for identifying risk factors in supply chain finance
- **[16]** [arXiv] 2025-06-26 — From On-chain to Macro: Assessing the Importance of Data Source Diversity in Cryptocurrenc
- **[16]** [arXiv] 2025-06-25 — WallStreetFeds: Client-Specific Tokens as Investment Vehicles in Federated Learning
- **[16]** [arXiv] 2025-01-02 — Calculating Customer Lifetime Value and Churn using Beta Geometric Negative Binomial and G
- **[16]** [arXiv] 2026-03-19 — Mapping Recent Shifts in Digital Art via Conference Discourse: AI, XR, the Metaverse, and 
- **[16]** [arXiv] 2025-08-28 — BridgeShield: Enhancing Security for Cross-chain Bridge Applications via Heterogeneous Gra
- **[16]** [arXiv] 2026-03-11 — Counterweights and Complementarities: The Convergence of AI and Blockchain Powering a Dece
- **[16]** [arXiv] 2025-12-11 — D2M: A Decentralized, Privacy-Preserving, Incentive-Compatible Data Marketplace for Collab
- **[16]** [arXiv] 2025-10-26 — Blockchain Signatures to Ensure Information Integrity and Non-Repudiation in the Digital E
- **[16]** [arXiv] 2025-09-16 — Validating Solidity Code Defects using Symbolic and Concrete Execution powered by Large La
- **[16]** [arXiv] 2025-09-06 — SEASONED: Semantic-Enhanced Self-Counterfactual Explainable Detection of Adversarial Explo
- **[16]** [arXiv] 2025-07-19 — CASPER: Contrastive Approach for Smart Ponzi Scheme Detecter with More Negative Samples
- **[16]** [arXiv] 2025-05-31 — From Rules to Rewards: Reinforcement Learning for Interest Rate Adjustment in DeFi Lending
- **[16]** [arXiv] 2025-05-25 — An Initial Exploration of Fine-tuning Small Language Models for Smart Contract Reentrancy 
- **[16]** [arXiv] 2025-04-28 — Smart Water Security with AI and Blockchain-Enhanced Digital Twins
- **[16]** [arXiv] 2025-04-13 — RoboComm: A DID-based scalable and privacy-preserving Robot-to-Robot interaction over stat
- **[16]** [arXiv] 2025-02-24 — MTVHunter: Smart Contracts Vulnerability Detection Based on Multi-Teacher Knowledge Transl
