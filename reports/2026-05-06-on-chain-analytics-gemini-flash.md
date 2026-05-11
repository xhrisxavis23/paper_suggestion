# Research Topic Suggestion — "on-chain analytics"

생성: 2026-05-06T03:35:22.235293+00:00
DB 윈도우: 1998-12-20 ~ 2026-05-06 (9999d)
모델: gemini-2.5-flash
매칭 논문: 6건
확장 키워드: ['on-chain analytics', 'blockchain analytics', 'decentralized finance analytics', 'crypto data analysis', 'blockchain data analysis', 'web3 analytics', 'cryptocurrency market analysis', 'on-chain metrics', 'tokenomics analysis', 'transaction flow analysis']

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — 블록체인 이상 탐지
- **설명**: 블록체인 트랜잭션 및 디지털 자산 데이터에서 비정상적인 패턴을 탐지하고 분석하는 시스템과 방법론을 다룹니다. 특히 Transformer 기반 모델 및 LLM-Agent 시스템을 활용한 접근법을 포함합니다.
- **빈도**: 2건
- **구간별 (≈2499d씩, 오래된→최근)**: 0 → 0 → 1 → 1
- **대표 논문**:
  - [P-NEURIPS-9eb19f] BlockScan: Detecting Anomalies in Blockchain Transactions — Jiahao Yu, Xian Wu, Hao Liu et al., NeurIPS 2025
  - [P-2510.20102] Human-Centered LLM-Agent System for Detecting Anomalous Digital Asset Transactions — Gyuyeon Na, Minjung Park, Hyeonjeong Cha et al., arXiv 2025

### 클러스터 2 — AI 기반 데이터 해석 및 투명성
- **설명**: AI 에이전트 및 대규모 언어 모델(LLM)을 사용하여 복잡한 블록체인 데이터의 해석 가능성을 높이고 스테이블코인 등 디지털 자산의 투명성을 확보하는 연구를 포함합니다.
- **빈도**: 2건
- **구간별 (≈2499d씩, 오래된→최근)**: 0 → 0 → 1 → 1
- **대표 논문**:
  - [P-2506.02068] Enhancing Interpretability of Quantum-Assisted Blockchain Clustering via AI Agent-Based Qualitative Analysis — Yun-Cheng Tsai, Yen-Ku Liu, Samuel Yen-Chi Chen, arXiv 2025
  - [P-2512.02418] Leveraging Large Language Models to Bridge Cross-Domain Transparency in Stablecoins — Yuexin Xiang, Yuchen Lei, Yuanzhe Zhang et al., arXiv 2025

### 클러스터 3 — 데이터 관리 및 시장 예측
- **설명**: 블록체인 데이터의 효과적인 관리와 인공지능 활용 기회를 모색하며, 다양한 온체인 및 거시경제 지표를 통합하여 암호화폐 시장을 예측하는 방법론을 다룹니다.
- **빈도**: 2건
- **구간별 (≈2499d씩, 오래된→최근)**: 1 → 0 → 0 → 1
- **대표 논문**:
  - [P-VLDB-2ddbfe] Data Management and AI for Blockchain Data Analysis: A Round Trip and Opportunities — Arijit Khan, VLDB 2024
  - [P-2506.21246] From On-chain to Macro: Assessing the Importance of Data Source Diversity in Cryptocurrency Market Forecasting — Giorgos Demosthenous, Chryssis Georgiou, Eliada Polydorou, arXiv 2025

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap gap_2_quantum_interpretability — `arxiv:2506.02068` 논문은 양자 강화 클러스터링 모델의 제한된 해석 가능성을 지적하며 AI 에이전트를 통한 질적 분석을 제안합니다
- **타입**: single-shot
- **설명**: `arxiv:2506.02068` 논문은 양자 강화 클러스터링 모델의 제한된 해석 가능성을 지적하며 AI 에이전트를 통한 질적 분석을 제안합니다. 그러나 다른 이상 탐지 또는 데이터 해석 연구에서 양자 기술의 해석 가능성을 심층적으로 다루거나 해당 논문의 발견('singleton cluster phenomenon')을 확장한 사례는 보이지 않습니다.
- **근거 논문**: P-2506.02068
- **Skeptic 검토**: ✓ 통과 — `arxiv:2506.02068`이 제시한 양자 해석 가능성 문제는 본 메타DB의 다른 논문에서 확장되거나 해결되지 않았습니다.

### Gap gap_3_stablecoin_systemic_gaps — `arxiv:2512.02418` 논문은 LLM을 활용하여 스테이블코인의 공시 자료와 실제 온체인 데이터 간의 체계적인 불일치('systemat
- **타입**: recurring-limitation
- **설명**: `arxiv:2512.02418` 논문은 LLM을 활용하여 스테이블코인의 공시 자료와 실제 온체인 데이터 간의 체계적인 불일치('systematic gaps')를 탐지하고 정량화하는 프레임워크를 제시합니다. 이는 스테이블코인 투명성 분야에서 반복되는 근본적인 문제점임을 시사합니다.
- **근거 논문**: P-2512.02418
- **Skeptic 검토**: ✓ 통과 — `arxiv:2512.02418`은 체계적인 불일치를 탐지하지만, 이를 해결하거나 예방하는 정책/기술적 접근 방식은 다루지 않아 유효한 갭입니다.

### Gap gap_5_human_centered_anomaly_deepening — `arxiv:2510.20102` 논문은 인간 중심의 LLM 에이전트 시스템을 제안하며 이상 탐지에서 해석 가능성, 상호작용 및 의사결정 투명성
- **타입**: single-shot
- **설명**: `arxiv:2510.20102` 논문은 인간 중심의 LLM 에이전트 시스템을 제안하며 이상 탐지에서 해석 가능성, 상호작용 및 의사결정 투명성을 강조합니다. 그러나 이와 같이 '인간 중심'이라는 철학을 시스템 설계의 핵심 원칙으로 삼아 이상 탐지 모델의 지속적인 개선이나 사용자 피드백 루프를 통합하는 등 더 깊이 있는 연구는 아직 초기 단계로 보입니다.
- **근거 논문**: P-2510.20102
- **Skeptic 검토**: ✓ 통과 — `arxiv:2510.20102`가 상호작용과 해석 가능성에 초점을 맞추지만, 인간 피드백을 통한 모델의 지속적인 개선 및 전체 라이프사이클 통합은 심화된 연구가 필요합니다.

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap gap_1_anomaly_market_link** — 블록체인 트랜잭션 이상 탐지 연구(클러스터 1)는 비정상적인 활동을 식별하는 데 중점을 두지만, 이러한 이상 현상이 암호화폐 시장 예측(클러스터 3)에 미치는 영향을 분석하거나 시장 예측 모델에 통합하는 연구는 명확히 나타나지 않습니다. · 거부 사유: 다른 클러스터에서 이미 다룸 [arxiv:2506.21246]
- **Gap gap_4_data_management_ai_ops** — `title:data management and ai for blockchain data analysis: a round trip and opportunities`는 블록체인 데이터 분석을 위한 데이터 관리 및 AI 기회에 대한 포괄적인 관점을 제시하지만, 다른 클러스터의 구체적인 AI 응용(예: 복잡한 이상 탐지, 다중 소스 시장 예측)에서 발생하는 특화된 데이터 관리 문제나 요구 사항에 대한 상세한 연결 고리는 부족합니다. · 거부 사유: 다른 분야에서 풀렸음 [title:blockscan: detecting anomalies in blockchain transactions, arxiv:2506.21246, arxiv:2512.02418]

</details>

## 3. 연구 제안 (Proposer)

### 제안 1 — QIC-AGENT
**가설**: 양자 강화 블록체인 클러스터링 모델에서 발생하는 싱글톤 클러스터 현상은 AI 에이전트의 다단계 질적 분석 프레임워크를 통해 효과적으로 식별되고 그 원인이 심층적으로 해석될 수 있다.
**메우는 갭**: gap_2_quantum_interpretability
**접근**: arxiv:2506.02068이 제안한 AI 에이전트 기반 질적 분석 프레임워크를 확장하여, 싱글톤 클러스터 형성의 메커니즘을 파악하기 위한 추가적인 양자 특징 중요도 분석 모듈을 통합한다. 이 모듈은 Quantum Neural Networks (QNN) 및 Quantum Features (QF)의 각 파라미터가 클러스터 결과에 미치는 영향을 역추적하여 해석 가능한 인사이트를 제공한다. 더 나아가, AI 에이전트가 이러한 특징 중요도를 기반으로 이상 클러스터 패턴에 대한 가설을 생성하고 검증하는 반복적 추론 과정을 설계한다.
**Baselines**: Quantum Neural Networks (QNN), Quantum Features (QF), Silhouette Score, Davies Bouldin Index, Calinski Harabasz Index
**예상 기여**: 본 연구는 양자 강화 블록체인 클러스터링의 고질적인 해석 가능성 문제를 해결하고, 특히 'singleton cluster phenomenon'과 같은 특정 현상의 발생 원인을 심층적으로 규명하는 데 기여할 것이다. 이는 금융 사기 탐지 및 블록체인 거버넌스와 같은 민감한 분야에서 양자 기술의 신뢰성 높은 적용을 가능하게 할 것이다.
**참고**: P-2506.02068

### 제안 2 — STAB-GUARD
**가설**: LLM 기반의 지속적인 감시 및 예측 시스템은 스테이블코인의 공시 자료와 온체인 데이터 간의 체계적인 불일치 발생을 사전에 감지하고, 잠재적 위험을 예측하여 투명성 문제를 해결하는 데 기여할 수 있다.
**메우는 갭**: gap_3_stablecoin_systemic_gaps
**접근**: arxiv:2512.02418에서 제시된 LLM 기반 통합 프레임워크를 확장하여, 단순히 불일치를 탐지하는 것을 넘어 불일치 발생 시 특정 조건(예: 특정 거래량 증가, 비정상적 토큰 소각/발행 패턴)과 공시 내용의 불일치 정도를 실시간으로 모니터링한다. 이를 위해, 다중 체인 발행 기록 및 공시 문서의 시계열 데이터를 학습하여 미래의 'systematic gaps' 발생 가능성을 예측하는 LLM 기반 시계열 예측 모델을 개발한다. 또한, 탐지된 불일치에 기반하여 규제 준수 및 시장 안정성 측면에서 잠재적 위험도를 평가하고 경고를 생성하는 모듈을 통합한다.
**Baselines**: LLM-based automated framework, quantitative market data, qualitative disclosure narratives, multi-chain issuance records
**예상 기여**: 본 연구는 스테이블코인의 체계적인 투명성 불일치를 사후 탐지하는 것을 넘어, 선제적으로 감지하고 예측함으로써 잠재적 위험을 관리하는 데 기여할 것이다. 이는 스테이블코인 시장의 신뢰도를 높이고 규제 기관 및 투자자에게 중요한 의사결정 지원 도구를 제공할 것이다.
**참고**: P-2512.02418

### 제안 3 — HCLA-LOOP
**가설**: 인간 중심의 LLM 에이전트 시스템에 사용자 피드백 루프와 능동 학습 메커니즘을 통합함으로써, 이상 탐지 모델은 사용자의 전문 지식을 지속적으로 반영하고 시간이 지남에 따라 탐지 정확도 및 해석 가능성을 향상시킬 수 있다.
**메우는 갭**: gap_5_human_centered_anomaly_deepening
**접근**: arxiv:2510.20102의 HCLA 시스템의 Rule Abstraction, Evidence Scoring, Expert-Style Justification 역할을 기반으로, 사용자 피드백을 수집하고 이를 모델 학습에 활용하는 능동 학습(Active Learning) 모듈을 추가한다. 사용자가 탐지된 이상 거래에 대한 오탐(false positive) 또는 미탐(false negative)을 표시하고, 해당 피드백을 바탕으로 Rule Abstraction 에이전트가 새로운 규칙을 제안하거나 기존 규칙의 가중치를 조정하도록 한다. 이를 통해 시스템은 사용자의 실제 경험과 도메인 지식을 지속적으로 반영하여 모델의 성능과 신뢰성을 점진적으로 최적화한다.
**Baselines**: HCLA (Human-Centered LLM-Agent system), classical anomaly detectors, cryptocurrency anomaly dataset
**예상 기여**: 본 연구는 인간 중심 이상 탐지 시스템이 단순히 해석 가능성을 제공하는 것을 넘어, 사용자 피드백을 통해 모델이 지속적으로 학습하고 진화할 수 있는 프레임워크를 제시할 것이다. 이는 탐지 정확도 향상뿐만 아니라, 사용자와 AI 시스템 간의 상호작용을 심화하여 실제 금융 포렌식 및 규제 준수 환경에서의 효용성을 극대화할 것이다.
**참고**: P-2510.20102

## 4. 참고문헌 (메타DB 기반)

### 클러스터 1 — 블록체인 이상 탐지 (2)
- [P-NEURIPS-9eb19f] BlockScan: Detecting Anomalies in Blockchain Transactions, Jiahao Yu, Xian Wu, Hao Liu et al., NeurIPS 2025 · https://openreview.net/forum?id=URB690A5r5
- [P-2510.20102] Human-Centered LLM-Agent System for Detecting Anomalous Digital Asset Transactions, Gyuyeon Na, Minjung Park, Hyeonjeong Cha et al., arXiv 2025 · http://arxiv.org/abs/2510.20102v3

### 클러스터 2 — AI 기반 데이터 해석 및 투명성 (2)
- [P-2506.02068] Enhancing Interpretability of Quantum-Assisted Blockchain Clustering via AI Agent-Based Qualitative Analysis, Yun-Cheng Tsai, Yen-Ku Liu, Samuel Yen-Chi Chen, arXiv 2025 · http://arxiv.org/abs/2506.02068v1
- [P-2512.02418] Leveraging Large Language Models to Bridge Cross-Domain Transparency in Stablecoins, Yuexin Xiang, Yuchen Lei, Yuanzhe Zhang et al., arXiv 2025 · http://arxiv.org/abs/2512.02418v3

### 클러스터 3 — 데이터 관리 및 시장 예측 (2)
- [P-VLDB-2ddbfe] Data Management and AI for Blockchain Data Analysis: A Round Trip and Opportunities, Arijit Khan, VLDB 2024 · https://openreview.net/forum?id=zBKWzDtZyV
- [P-2506.21246] From On-chain to Macro: Assessing the Importance of Data Source Diversity in Cryptocurrency Market Forecasting, Giorgos Demosthenous, Chryssis Georgiou, Eliada Polydorou, arXiv 2025 · http://arxiv.org/abs/2506.21246v1

---

## 메타 / 디버그
- model: gemini-2.5-flash
- backend: gemini-flash-sdk
- matched_n: 6
- matched_total_before_cap: 6
- window_days: 9999
- tokens_in_uncached: 5409
- tokens_in_cached_read: 6300
- tokens_out: 4042
- usd_estimate: $0.0122
