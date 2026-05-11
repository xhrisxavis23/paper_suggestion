# Research Topic Suggestion — "NFT"

생성: 2026-05-06T03:58:36.514492+00:00
DB 윈도우: 1998-12-20 ~ 2026-05-06 (9999d)
모델: gemini-2.5-pro
매칭 논문: 10건
확장 키워드: ['Non-Fungible Token', 'NFT art', 'digital collectible', 'crypto asset', 'blockchain digital asset', 'tokenized digital art', 'on-chain asset', 'ERC-721 standard', 'smart contract asset', 'metaverse digital property', 'web3 digital ownership']

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — NFT 가치평가 및 예측
- **설명**: NFT의 희소성, 가격 변동, 생애 가치 등 경제적 가치를 정량적으로 평가하고 예측하는 방법론에 대한 연구 클러스터입니다.
- **빈도**: 3건
- **구간별 (≈2499d씩, 오래된→최근)**: 0 → 1 → 1 → 1
- **대표 논문**:
  - [P-KDD-177aba] COMET: NFT Price Prediction with Wallet Profiling — Tianfu Wang, Liwei Deng, Chao Wang et al., KDD 2024
  - [P-2508.12671] DIT: Dimension Reduction View on Optimal NFT Rarity Meters — Dmitry Belousov, Yury Yanovich, arXiv 2025
  - [P-2501.04719] Calculating Customer Lifetime Value and Churn using Beta Geometric Negative Binomial and Gamma-Gamma Distribution in a NFT based setting — Sagarnil Das, arXiv 2025

### 클러스터 2 — NFT 마켓플레이스 및 활용
- **설명**: 데이터 거래, 스포츠 선수 NIL, 게임 등 특정 도메인에서 NFT를 활용한 마켓플레이스를 설계하고 사용자 행동을 분석하는 연구입니다.
- **빈도**: 3건
- **구간별 (≈2499d씩, 오래된→최근)**: 1 → 0 → 1 → 1
- **대표 논문**:
  - [P-KDD-23dbaa] NFT-Based Data Marketplace with Digital Watermarking — Saeed Ranjbar Alvar, Mohammad Akbari, David Ming Xuan Yue et al., KDD 2023
  - [P-DECISION-7bfa30] Designing a fair and inclusive digital asset-based name-image-likeness marketplace — Arthur Carvalho, Liudmila Zavolokina, Suman Bhunia et al., Decision Support Systems 2025
  - [P-2504.11702] Clustering and analysis of user behaviour in blockchain: A case study of Planet IX — Dorottya Zelenyanszki, Zhe Hou, Kamanashis Biswas et al., arXiv 2025

### 클러스터 3 — NFT 생태계 데이터 분석
- **설명**: NFT 거래 데이터를 그래프로 분석하거나, 관련 학계 담론 변화를 추적하는 등 NFT 생태계 전반을 거시적으로 분석하는 연구들을 포함합니다.
- **빈도**: 3건
- **구간별 (≈2499d씩, 오래된→최근)**: 1 → 0 → 1 → 1
- **대표 논문**:
  - [P-NEURIPS-5ed0c5] Live Graph Lab: Towards Open, Dynamic and Real Transaction Graphs with NFT — Zhen Zhang, Bingqiao Luo, Shengliang Lu et al., NeurIPS 2023
  - [P-2504.16116] DMind Benchmark: Toward a Holistic Assessment of LLM Capabilities across the Web3 Domain — Enhao Huang, Pengyu Sun, Zixin Lin et al., arXiv 2025
  - [P-2604.16360] Mapping Recent Shifts in Digital Art via Conference Discourse: AI, XR, the Metaverse, and Blockchain/NFTs (2021-2025) — Vasileios Komianos, Emmanuel Rovithis, Athanasios Tsipis, arXiv 2026

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap A — NFT 가치평가 및 예측(클러스터1)에서는 정교한 가격 예측 및 희소성 측정 모델이 개발되고 있지만, NFT 마켓플레이스 및 활용(클러스터2) 
- **타입**: between-clusters
- **설명**: NFT 가치평가 및 예측(클러스터1)에서는 정교한 가격 예측 및 희소성 측정 모델이 개발되고 있지만, NFT 마켓플레이스 및 활용(클러스터2) 연구에서는 이러한 모델들을 적극적으로 통합하지 않고 있습니다. 예를 들어, '공정하고 포용적인' 마켓플레이스 설계를 목표로 하면서도, 복잡한 가치 평가 모델을 활용하여 보상을 최적화하거나 사용자에게 예측 정보를 제공하는 등의 연계가 부족합니다.
- **근거 논문**: P-KDD-177aba, P-2508.12671, P-DECISION-7bfa30
- **Skeptic 검토**: ✓ 통과 — 가치 평가 모델(클러스터1)과 마켓플레이스 메커니즘 설계(클러스터2) 간의 통합이 부족하다는 주장은 타당해 보입니다. 제시된 논문들은 각자의 영역에 집중하고 있어, 둘 사이의 시너지를 탐구하는 연구는 유효한 갭으로 판단됩니다.

### Gap B — 'NFT-Based Data Marketplace with Digital Watermarking' 논문은 데이터의 불법 재배포 문제를 해결하기 
- **타입**: single-shot
- **설명**: 'NFT-Based Data Marketplace with Digital Watermarking' 논문은 데이터의 불법 재배포 문제를 해결하기 위해 워터마킹 기술을 NFT에 접목하는 독창적인 방법을 제안했습니다. 하지만 이후 다른 연구들은 주로 트랜잭션 데이터 분석이나 시장 메커니즘 설계에 집중하며, 이처럼 NFT가 표상하는 디지털 자산 자체의 무결성과 소유권을 기술적으로 보호하는 방식에 대한 후속 연구나 확장을 보여주지 않고 있습니다.
- **근거 논문**: P-KDD-23dbaa
- **Skeptic 검토**: ✓ 통과 — 제시된 메타 데이터 내에서 NFT와 연결된 원본 디지털 자산의 기술적 보호(예: 워터마킹)를 다룬 후속 연구를 찾을 수 없습니다. 다른 연구들은 온체인 데이터 분석에 집중하고 있어, 해당 주제는 단일 연구로 남아있는 유효한 갭으로 보입니다.

### Gap D — 한 논문('Calculating Customer Lifetime Value...')은 전통적인 고객 생애 가치(CLV) 모델을 NFT 트랜잭션 
- **타입**: single-shot
- **설명**: 한 논문('Calculating Customer Lifetime Value...')은 전통적인 고객 생애 가치(CLV) 모델을 NFT 트랜잭션 데이터에 적용하는 새로운 관점을 제시했습니다. 이는 NFT 투자자를 '고객'으로 보고 장기적 가치를 평가하는 접근법입니다. 그러나 다른 가치 평가 연구들은 주로 희소성이나 단기 거래 패턴 기반의 가격 예측에 집중하고 있어, 이와 같이 성숙한 금융/마케팅 모델을 NFT에 접목하려는 시도는 아직 단발성에 그치고 있습니다.
- **근거 논문**: P-2501.04719, P-KDD-177aba
- **Skeptic 검토**: ✓ 통과 — 전통적인 마케팅 모델(CLV)을 NFT에 적용한 연구는 제시된 자료 내에서 유일하며, 다른 가치 평가 연구들은 희소성이나 거래 그래프 등 NFT 네이티브한 접근법에 집중하고 있습니다. 학제간 모델 적용의 확산이 더디다는 주장은 타당합니다.

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap C** — NFT 생태계 데이터 분석(클러스터3) 연구는 전체 거래 네트워크의 거시적 특성을 분석하는 반면, NFT 가치평가 및 예측(클러스터1) 연구는 개별 NFT 가격 같은 미시적 지표에 집중합니다. 거시적 네트워크 동역학(예: 특정 커뮤니티의 부상)이 개별 NFT 가격 변동에 미치는 영향을 정량적으로 연결하는 연구가 부족합니다. · 거부 사유: 다른 클러스터에서 이미 다룸. 증거 논문인 'COMET: NFT Price Prediction with Wallet Profiling' [title:comet: nft price prediction with wallet profiling]은 '커뮤니티 강화 다중 행동 트랜잭션 그래프 모델'을 통해 NFT 생태계 내의 다양한 관계와 상호작용이 가격 변동에 미치는 영향을 분석함으로써, 거시적 동역학을 미시적 가격 예측에 이미 연결하고 있습니다.

</details>

## 3. 연구 제안 (Proposer)

### 제안 1 — DYNA-FAIR
**가설**: NFT 마켓플레이스에서 실시간 가치 평가 모델을 이용해 로열티를 동적으로 조정하면, 정적 로열티 모델보다 더 공정하고 포용적인 자원 분배를 달성할 수 있다.
**메우는 갭**: A
**접근**: COMET과 같은 지갑 프로파일링 기반 가격 예측 모델을 마켓플레이스 백엔드에 통합합니다. NFT 거래 발생 시, 해당 NFT의 예측 가치와 실제 거래 가격의 차이를 계산하여 로열티 비율을 동적으로 조정하는 스마트 컨트랙트를 설계합니다. 이를 통해 저평가된 자산의 판매자에게는 더 높은 보상을, 고평가된 자산에는 낮은 수수료를 적용하여 시장 참여를 유도하고 공정성을 높입니다.
**Baselines**: COMET, ROAR benchmark, fair and inclusive marketplace design principles
**예상 기여**: 기존의 정적인 규칙 기반 마켓플레이스 설계를 넘어, 데이터 기반의 동적 메커니즘을 도입하여 시장의 효율성과 공정성을 동시에 개선하는 새로운 패러다임을 제시합니다. 이는 NFT 가치 평가 연구와 마켓플레이스 설계 연구 간의 실질적인 통합 사례가 될 것입니다.
**참고**: P-KDD-177aba, P-DECISION-7bfa30, P-2508.12671

### 제안 2 — GEN-GUARD
**가설**: 생성형 AI를 이용한 변형 공격에 강인한 다중 계층 워터마킹 기술을 NFT 데이터 마켓플레이스에 적용하면, 원본 디지털 자산의 소유권 추적성과 무결성을 기존 방식보다 효과적으로 보존할 수 있다.
**메우는 갭**: B
**접근**: 기존의 단일 워터마킹 기법을 확장하여, 인지적으로 덜 중요한 데이터 영역과 의미적으로 중요한 특징에 각각 다른 워터마크를 삽입하는 다중 계층 워터마킹 기법을 개발합니다. 이 워터마크가 삽입된 데이터를 NFT의 내용으로 저장하고, 다양한 생성형 AI 기반 편집(inpainting, style transfer 등) 공격 후에도 최소 하나 이상의 워터마크가 남아 소유권 증명이 가능한지 실험적으로 검증합니다.
**Baselines**: Digital Watermarking
**예상 기여**: NFT가 표상하는 디지털 자산의 소유권 보호 문제를 다시 조명하고, 최신 AI 기술 발전에 따른 새로운 위협에 대응하는 기술적 해결책을 제시합니다. 이는 데이터 마켓플레이스의 신뢰성을 높이고 NFT의 활용 범위를 고부가가치 디지털 콘텐츠로 확장하는 데 기여할 것입니다.
**참고**: P-KDD-23dbaa

### 제안 3 — CLV-SEG
**가설**: NFT 보유자의 고객 생애 가치(CLV) 예측 모델과 온체인 행동 데이터 기반 클러스터링을 결합하면, 단기 거래 패턴만으로 식별할 수 없는 고가치 장기 투자자 세그먼트를 효과적으로 식별하고 이탈 가능성을 예측할 수 있다.
**메우는 갭**: D
**접근**: 먼저 'Planet IX'와 같은 특정 dApp의 트랜잭션 데이터를 활용하여 사용자 행동 흐름을 추출하고 Graph Neural Network(GNN)로 임베딩하여 사용자 클러스터를 식별합니다. 다음으로, 각 클러스터 내 사용자들에게 Beta Geometric Negative Binomial Distribution (BGNBD) 및 Gamma-Gamma 모델을 적용하여 CLV를 계산하고, 클러스터별 CLV 분포와 특성을 분석합니다. 이 통합 프로파일링을 통해 '고가치-저활동성' 또는 '저가치-고활동성' 등 복합적인 사용자 세그먼트를 정의하고 이들의 장기적 가치를 평가합니다.
**Baselines**: Beta Geometric Negative Binomial Distribution (BGNBD), Gamma-Gamma Distribution, Graph Neural Network (GNN) based clustering
**예상 기여**: NFT 가치 평가에 전통적인 마케팅 분석 기법을 접목하는 시도를 확장하여, 단일 사용자 가치 평가를 넘어 시장 전체를 세분화하는 프레임워크를 제공합니다. 이는 NFT 프로젝트가 데이터 기반의 정교한 사용자 리텐션 및 마케팅 전략을 수립하는 데 실질적인 도움을 줄 것입니다.
**참고**: P-2501.04719, P-2504.11702, P-KDD-177aba

## 4. 참고문헌 (메타DB 기반)

### 클러스터 1 — NFT 가치평가 및 예측 (3)
- [P-KDD-177aba] COMET: NFT Price Prediction with Wallet Profiling, Tianfu Wang, Liwei Deng, Chao Wang et al., KDD 2024 · https://openreview.net/forum?id=LdQlSTBuv9
- [P-2501.04719] Calculating Customer Lifetime Value and Churn using Beta Geometric Negative Binomial and Gamma-Gamma Distribution in a NFT based setting, Sagarnil Das, arXiv 2025 · http://arxiv.org/abs/2501.04719v1
- [P-2508.12671] DIT: Dimension Reduction View on Optimal NFT Rarity Meters, Dmitry Belousov, Yury Yanovich, arXiv 2025 · http://arxiv.org/abs/2508.12671v1

### 클러스터 2 — NFT 마켓플레이스 및 활용 (3)
- [P-KDD-23dbaa] NFT-Based Data Marketplace with Digital Watermarking, Saeed Ranjbar Alvar, Mohammad Akbari, David Ming Xuan Yue et al., KDD 2023 · https://openreview.net/forum?id=2yD7rYXeOw
- [P-2504.11702] Clustering and analysis of user behaviour in blockchain: A case study of Planet IX, Dorottya Zelenyanszki, Zhe Hou, Kamanashis Biswas et al., arXiv 2025 · http://arxiv.org/abs/2504.11702v1
- [P-DECISION-7bfa30] Designing a fair and inclusive digital asset-based name-image-likeness marketplace, Arthur Carvalho, Liudmila Zavolokina, Suman Bhunia et al., Decision Support Systems 2025 · https://doi.org/10.1016/j.dss.2025.114580

### 클러스터 3 — NFT 생태계 데이터 분석 (3)
- [P-NEURIPS-5ed0c5] Live Graph Lab: Towards Open, Dynamic and Real Transaction Graphs with NFT, Zhen Zhang, Bingqiao Luo, Shengliang Lu et al., NeurIPS 2023 · https://openreview.net/forum?id=zr1e15kczE
- [P-2504.16116] DMind Benchmark: Toward a Holistic Assessment of LLM Capabilities across the Web3 Domain, Enhao Huang, Pengyu Sun, Zixin Lin et al., arXiv 2025 · http://arxiv.org/abs/2504.16116v3
- [P-2604.16360] Mapping Recent Shifts in Digital Art via Conference Discourse: AI, XR, the Metaverse, and Blockchain/NFTs (2021-2025), Vasileios Komianos, Emmanuel Rovithis, Athanasios Tsipis, arXiv 2026 · http://arxiv.org/abs/2604.16360v1

### 기타 (클러스터 미분류) (1)
- [P-2604.20374] Towards Event-Aware Forecasting in DeFi: Insights from On-chain Automated Market Maker Protocols, Huaiyu Jia, Jiehshun You, Yizhi Luo et al., arXiv 2026 · http://arxiv.org/abs/2604.20374v1

---

## 메타 / 디버그
- model: gemini-2.5-pro
- backend: gemini-pro-sdk
- matched_n: 10
- matched_total_before_cap: 10
- window_days: 9999
- tokens_in_uncached: 5478
- tokens_in_cached_read: 12204
- tokens_out: 3821
- usd_estimate: $0.0488
