# Research Topic Suggestion — "DeFi liquidity"

생성: 2026-05-06T03:39:13.831184+00:00
DB 윈도우: 1998-12-20 ~ 2026-05-06 (9999d)
모델: gemini-2.5-flash
매칭 논문: 17건
확장 키워드: ['decentralized finance liquidity', 'DeFi liquidity', 'liquidity pool', 'liquidity provision', 'automated market maker', 'AMM liquidity', 'yield farming', 'liquidity mining', 'decentralized exchange liquidity', 'token liquidity', 'crypto asset liquidity']

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — 유동성 공급 최적화
- **설명**: 탈중앙화 금융(DeFi) 환경에서 유동성 공급자가 수익을 극대화하고 비영구적 손실을 최소화하기 위한 다양한 전략과 방법론(심층 강화 학습, 양자 머신러닝 등)을 연구하는 클러스터입니다.
- **빈도**: 8건
- **구간별 (≈2499d씩, 오래된→최근)**: 1 → 1 → 2 → 4
- **대표 논문**:
  - [P-KDD-bb9f3d] Money Never Sleeps: Maximizing Liquidity Mining Yields in Decentralized Finance — Wangze Ni, Yiwei Zhao, Weijie Sun et al., KDD 2024
  - [P-2501.07508] Improving DeFi Accessibility through Efficient Liquidity Provisioning with Deep Reinforcement Learning — Haonan Xu, Alessio Brini, arXiv 2025
  - [P-2602.19419] RAmmStein: Regime Adaptation in Mean-reverting Markets with Stein Thresholds -- Optimal Impulse Control in Concentrated AMMs — Pranay Anchuri, arXiv 2026

### 클러스터 2 — DeFi 사기 및 위협 탐지
- **설명**: 러그 풀, 느린 유동성 고갈 사기(SLID), 시빌 공격과 같은 탈중앙화 금융(DeFi) 생태계의 다양한 사기 및 보안 위협을 식별하고 방어하기 위한 탐지 방법론과 데이터셋 구축을 다룹니다.
- **빈도**: 3건
- **구간별 (≈2499d씩, 오래된→최근)**: 0 → 0 → 3 → 0
- **대표 논문**:
  - [P-2503.04850] Slow is Fast! Dissecting Ethereum's Slow Liquidity Drain Scams — Minh Trung Tran, Nasrin Sohrabi, Zahir Tari et al., arXiv 2025
  - [P-2504.07132] SolRPDS: A Dataset for Analyzing Rug Pulls in Solana Decentralized Finance — Abdulrahman Alhaidari, Bhavani Kalal, Balaji Palanisamy et al., arXiv 2025
  - [P-2505.09313] Detecting Sybil Addresses in Blockchain Airdrops: A Subgraph-based Feature Propagation and Fusion Approach — Qiangqiang Liu, Qian Huang, Frank Fan et al., arXiv 2025

### 클러스터 3 — 시장 구조 및 참여자 행동 분석
- **설명**: 금융 시장에서 다양한 유형의 참여자(기관 투자자, 정보 보유 트레이더, 노이즈 트레이더 등)의 상호작용이 유동성, 자산 가격, 시장 구성에 미치는 영향을 분석하고 사용자 행동 및 평판 시스템을 연구합니다.
- **빈도**: 6건
- **구간별 (≈2499d씩, 오래된→최근)**: 1 → 1 → 3 → 1
- **대표 논문**:
  - [P-ICAIF-3b067a] Detecting Collective Liquidity Taking Distributions — Andrei-Bogdan Balcau, Leandro Sánchez-Betancourt, Stefan Sarkadi et al., ICAIF 2024
  - [P-QUANTITA-0b6335] Asset prices when large investors interact strategically — Giuliano Curatola, Quantitative Finance 2024
  - [P-QUANTITA-4c71bf] When order execution meets informed trading — Longjie Xu, Yufeng Shi, Quantitative Finance 2025

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap A — 탈중앙화 금융(DeFi) 환경에서 유동성 공급 최적화 전략이 러그 풀이나 느린 유동성 고갈(SLID)과 같은 DeFi 사기에 대한 내성을 어떻게
- **타입**: between-clusters
- **설명**: 탈중앙화 금융(DeFi) 환경에서 유동성 공급 최적화 전략이 러그 풀이나 느린 유동성 고갈(SLID)과 같은 DeFi 사기에 대한 내성을 어떻게 통합할 수 있는지에 대한 연구가 부족합니다. 현재 최적화 연구는 주로 수익 극대화에 초점을 맞추는 반면, 사기 탐지 연구는 사기를 사후에 식별하는 데 중점을 둡니다.
- **근거 논문**: P-KDD-bb9f3d, P-2501.07508, P-2503.04850, P-2504.07132
- **Skeptic 검토**: ✓ 통과 — 유동성 공급 최적화와 DeFi 사기 탐지 연구 간의 통합적인 접근 방식이 부족함을 명확히 지적합니다.

### Gap D — 거시 경제 및 지정학적 위험이 DeFi 유동성 시장에 미치는 영향에 대한 분석(`arxiv:2510.12416`)은 독특합니다. 다른 논문들이 
- **타입**: single-shot
- **설명**: 거시 경제 및 지정학적 위험이 DeFi 유동성 시장에 미치는 영향에 대한 분석(`arxiv:2510.12416`)은 독특합니다. 다른 논문들이 DeFi 유동성 공급 또는 시장 구조에 이러한 외부 거시적 요인을 통합한 사례는 거의 없습니다.
- **근거 논문**: P-2510.12416
- **Skeptic 검토**: ✓ 통과 — 거시 경제 및 지정학적 위험이 DeFi 유동성에 미치는 영향을 다룬 연구는 메타DB 내에서 매우 독특하며, 이를 DeFi 시장의 다른 측면과 통합하는 연구는 부재합니다.

### Gap E — 단일 프로토콜(예: Uniswap) 내 사용자 행동 분석 및 평판 점수화는 이루어지고 있으나, 다양한 DeFi 프로토콜에 걸쳐 확장 가능하고 통
- **타입**: between-clusters
- **설명**: 단일 프로토콜(예: Uniswap) 내 사용자 행동 분석 및 평판 점수화는 이루어지고 있으나, 다양한 DeFi 프로토콜에 걸쳐 확장 가능하고 통합된 평판 시스템 또는 위험 평가 프레임워크에 대한 연구는 부족합니다.
- **근거 논문**: P-2507.20494, P-2505.09313, P-2503.04850
- **Skeptic 검토**: ✓ 통과 — 제시된 증거 논문들이 단일 프로토콜 또는 특정 유형의 위험 탐지에 초점을 맞추고 있어, cross-protocol 평판 시스템의 부재를 지지합니다.

### Gap F — 페더레이티드 러닝(FL)의 인센티브 문제를 해결하기 위해 DeFi 플랫폼(AMMs)을 활용한 보상 분배 프레임워크(`arxiv:2506.2051
- **타입**: single-shot
- **설명**: 페더레이티드 러닝(FL)의 인센티브 문제를 해결하기 위해 DeFi 플랫폼(AMMs)을 활용한 보상 분배 프레임워크(`arxiv:2506.20518`)를 제안했지만, 이 접근 방식이 실제 DeFi 유동성 시장의 역학에 어떻게 통합되거나 영향을 미치는지에 대한 심층적인 후속 연구는 보이지 않습니다.
- **근거 논문**: P-2506.20518
- **Skeptic 검토**: ✓ 통과 — FL 인센티브를 위해 DeFi를 활용한 연구는 존재하지만, 그 메커니즘이 DeFi 유동성 시장 자체에 미치는 영향을 분석하는 연구는 다루지 않습니다.

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap B** — DeFi 환경에서 강화 학습 및 머신러닝 기반 유동성 공급 전략의 실제 적용 및 일반화 능력에 대한 지속적인 한계가 나타납니다. 특히 급변하는 시장 조건(regime shifts)에 대한 적응력과 광범위한 데이터셋에서의 성능 검증이 중요한 도전 과제로 언급됩니다. · 거부 사유: 이미 클러스터 1 (유동성 공급 최적화)에서 다룸. `arxiv:2501.07508`, `arxiv:2511.22101`, `arxiv:2602.19419`, `arxiv:2510.15903` 등 여러 논문에서 ML/RL 기반 유동성 공급 전략의 적응성 및 일반화 능력을 개선하기 위한 연구가 활발히 진행 중이며, 이는 해결해야 할 '한계'가 아닌 클러스터 내의 주요 연구 도전 과제로 다루어지고 있습니다.
- **Gap C** — 금융 시장 참여자(기관 투자자, 정보 보유 트레이더 등)의 전략적 행동과 유동성 시장 구성에 대한 심층 분석이 유동성 공급 최적화 모델에 직접적으로 통합되지 않고 있습니다. 최적화 모델은 주로 개별 LP의 수익 극대화에 초점을 맞춥니다. · 거부 사유: 이미 클러스터 1 (유동성 공급 최적화)과 클러스터 3 (시장 구조 및 참여자 행동 분석)에서 다룸. `arxiv:2601.00324`는 'Liquidity Games'와 'Rational Swarms'를 통합하여 다중 에이전트 환경에서 유동성 제공자의 전략적 행동과 시장 효율성을 연구하며, 이는 금융 시장 참여자의 전략적 행동을 유동성 공급 모델에 통합하려는 시도로 볼 수 있습니다.

</details>

## 3. 연구 제안 (Proposer)

### 제안 1 — SAFENET-LP
**가설**: 유동성 공급 최적화 전략에 실시간 사기 위험 탐지 메커니즘을 통합하면 수익성을 유지하면서 러그 풀 및 느린 유동성 고갈 사기로부터 자산을 보호하여 투자자의 위험 노출을 현저히 줄일 수 있다.
**메우는 갭**: A
**접근**: 기존 딥 강화 학습 기반 유동성 공급 에이전트(예: Proximal Policy Optimization)에 SLID(Slow Liquidity Drain) 및 러그 풀 탐지 모델의 위험 점수를 추가 상태 변수로 통합한다. 에이전트는 이 위험 점수를 기반으로 유동성 풀에 대한 포지션 진입, 조정, 철회 결정을 동적으로 학습하며, 고위험 풀을 회피하거나 일찍 철회하여 잠재적 손실을 최소화한다. 이는 'Money Never Sleeps'에서 다루는 YMLM 문제에 사기 회피 제약 조건을 추가하는 것이다.
**Baselines**: Proximal Policy Optimization (PPO), DDQN, Random Forest, Gradient Boosting, Uniswap v3
**예상 기여**: 본 연구는 유동성 공급의 수익성 최적화와 사기 위험 관리라는 두 가지 중요한 문제를 동시에 해결하는 통합 프레임워크를 제공한다. 이는 DeFi 투자자의 자산 보호를 강화하고 생태계의 전반적인 신뢰성을 높일 것이다.
**참고**: P-KDD-bb9f3d, P-2501.07508, P-2503.04850, P-2504.07132, P-2602.19419

### 제안 2 — GEODEFI-LIQ
**가설**: 거시경제 및 지정학적 요인(예: Global Financial Cycle 지표, 지정학적 위험 지수)을 DeFi 유동성 풀 모델에 통합하면 유동성 변동성과 투자자 행동을 더 정확하게 예측하고, 외부 충격에 대한 DeFi 시장의 회복력을 평가할 수 있다.
**메우는 갭**: D
**접근**: arxiv:2510.12416에서 제안된 지정학적/거시경제적 충격의 전파 채널 분석을 활용하여, 이러한 외부 요인들을 Uniswap v3와 같은 AMM의 유동성 공급 및 가격 예측 모델의 추가 입력 피처로 사용한다. 구체적으로, Global Financial Cycle(GFC) 지표 및 정책 불확실성 지수를 포함한 외부 데이터를 AMM의 가격 동역학 및 유동성 깊이 예측을 위한 심층 학습 모델(예: QuantumRWKV, QASA Hybrid)에 통합하여 그 영향을 정량적으로 분석한다.
**Baselines**: QuantumRWKV, QASA Hybrid, Random Forest, Gradient Boosting, Logistic Regression, Uniswap v3
**예상 기여**: 본 연구는 DeFi 시장의 내생적 요인뿐만 아니라 외생적 거시경제 및 지정학적 요인이 유동성에 미치는 영향을 체계적으로 분석하여, DeFi 시장 분석의 범위를 확장한다. 이는 보다 견고한 위험 관리 모델과 정책 권고를 가능하게 할 것이다.
**참고**: P-2510.12416, P-2510.15903, P-2509.16955, P-2604.20374

### 제안 3 — CROSS-REP
**가설**: 여러 DeFi 프로토콜에 걸친 지갑 활동 데이터를 통합하여 구축된 평판 시스템은 단일 프로토콜 기반 시스템보다 악성 행위자를 더 효과적으로 식별하고, 전체 DeFi 생태계의 유동성 위험을 더 정확하게 평가할 수 있다.
**메우는 갭**: E
**접근**: Uniswap v3 (LP/Swap Score), Aave/Morpho (대출/차입 행동), 그리고 Sybil 공격 탐지 모델에서 파생된 지표들을 결합하여 다중 프로토콜 지갑 행동 특징 벡터를 구축한다. 이 특징 벡터를 입력으로 하는 그래프 신경망(GNN) 또는 딥 잔차 신경망(Deep Residual Neural Network)을 사용하여 지갑의 교차 프로토콜 평판 점수와 위험 등급을 산출한다. arxiv:2507.20494의 zScore 프레임워크를 확장하여 Pool-level context 뿐만 아니라 Protocol-level context를 통합한다.
**Baselines**: zScore, LightGBM, Uniswap v3, Aave, Morpho, Pendle
**예상 기여**: 본 연구는 DeFi 환경에서 지갑의 신뢰도를 종합적으로 평가할 수 있는 확장 가능한 교차 프로토콜 평판 프레임워크를 제시한다. 이는 프로토콜 간 상호작용이 증가하는 DeFi 생태계에서 사용자 신뢰를 높이고, 사기 및 위험 관리를 위한 기반을 마련할 것이다.
**참고**: P-2507.20494, P-2505.09313, P-2503.04850, P-2604.20374

## 4. 참고문헌 (메타DB 기반)

### 클러스터 1 — 유동성 공급 최적화 (8)
- [P-KDD-bb9f3d] Money Never Sleeps: Maximizing Liquidity Mining Yields in Decentralized Finance, Wangze Ni, Yiwei Zhao, Weijie Sun et al., KDD 2024 · https://openreview.net/forum?id=p0XpoNd3DC
- [P-2501.07508] Improving DeFi Accessibility through Efficient Liquidity Provisioning with Deep Reinforcement Learning, Haonan Xu, Alessio Brini, arXiv 2025 · http://arxiv.org/abs/2501.07508v1
- [P-2511.22101] Adaptive Dueling Double Deep Q-networks in Uniswap V3 Replication and Extension with Mamba, Zhaofeng Zhang, arXiv 2025 · http://arxiv.org/abs/2511.22101v1
- [P-2602.19419] RAmmStein: Regime Adaptation in Mean-reverting Markets with Stein Thresholds -- Optimal Impulse Control in Concentrated AMMs, Pranay Anchuri, arXiv 2026 · http://arxiv.org/abs/2602.19419v2
- [P-2601.00324] Multiagent Reinforcement Learning for Liquidity Games, Alicia Vidler, Gal A. Kaminka, arXiv 2026 · http://arxiv.org/abs/2601.00324v1
- [P-2510.15903] Quantum and Classical Machine Learning in Decentralized Finance: Comparative Evidence from Multi-Asset Backtesting of Automated Market Makers, Chi-Sheng Chen, Aidan Hung-Wen Tsai, arXiv 2025 · http://arxiv.org/abs/2510.15903v1
- [P-2509.16955] Quantum Adaptive Self-Attention for Financial Rebalancing: An Empirical Study on Automated Market Makers in Decentralized Finance, Chi-Sheng Chen, Aidan Hung-Wen Tsai, arXiv 2025 · http://arxiv.org/abs/2509.16955v1
- [P-2604.20374] Towards Event-Aware Forecasting in DeFi: Insights from On-chain Automated Market Maker Protocols, Huaiyu Jia, Jiehshun You, Yizhi Luo et al., arXiv 2026 · http://arxiv.org/abs/2604.20374v1

### 클러스터 2 — DeFi 사기 및 위협 탐지 (3)
- [P-2503.04850] Slow is Fast! Dissecting Ethereum's Slow Liquidity Drain Scams, Minh Trung Tran, Nasrin Sohrabi, Zahir Tari et al., arXiv 2025 · http://arxiv.org/abs/2503.04850v3
- [P-2504.07132] SolRPDS: A Dataset for Analyzing Rug Pulls in Solana Decentralized Finance, Abdulrahman Alhaidari, Bhavani Kalal, Balaji Palanisamy et al., arXiv 2025 · http://arxiv.org/abs/2504.07132v1
- [P-2505.09313] Detecting Sybil Addresses in Blockchain Airdrops: A Subgraph-based Feature Propagation and Fusion Approach, Qiangqiang Liu, Qian Huang, Frank Fan et al., arXiv 2025 · http://arxiv.org/abs/2505.09313v1

### 클러스터 3 — 시장 구조 및 참여자 행동 분석 (6)
- [P-ICAIF-3b067a] Detecting Collective Liquidity Taking Distributions, Andrei-Bogdan Balcau, Leandro Sánchez-Betancourt, Stefan Sarkadi et al., ICAIF 2024 · https://openreview.net/forum?id=WV83vWYA94
- [P-QUANTITA-0b6335] Asset prices when large investors interact strategically, Giuliano Curatola, Quantitative Finance 2024 · https://doi.org/10.1080/14697688.2024.2387821
- [P-QUANTITA-4c71bf] When order execution meets informed trading, Longjie Xu, Yufeng Shi, Quantitative Finance 2025 · https://doi.org/10.1080/14697688.2025.2479049
- [P-2507.20494] Deep Reputation Scoring in DeFi: zScore-Based Wallet Ranking from Liquidity and Trading Signals, Dhanashekar Kandaswamy, Ashutosh Sahoo, Akshay SP et al., arXiv 2025 · http://arxiv.org/abs/2507.20494v1
- [P-2506.20518] WallStreetFeds: Client-Specific Tokens as Investment Vehicles in Federated Learning, Arno Geimer, Beltran Fiz Pontiveros, Radu State, arXiv 2025 · http://arxiv.org/abs/2506.20518v1
- [P-2510.12416] Geopolitics, Geoeconomics, and Sovereign Risk: Different Shocks, Different Channels, Alvaro Ortiz, Tomasa Rodrigo, Pablo Saborido, arXiv 2025 · http://arxiv.org/abs/2510.12416v7

---

## 메타 / 디버그
- model: gemini-2.5-flash
- backend: gemini-flash-sdk
- matched_n: 17
- matched_total_before_cap: 17
- window_days: 9999
- tokens_in_uncached: 6421
- tokens_in_cached_read: 20116
- tokens_out: 4901
- usd_estimate: $0.0157
