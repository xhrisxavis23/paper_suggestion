# Research Topic Suggestion — "manufacturing"

생성: 2026-04-27T01:12:36.472092+00:00
DB 윈도우: 2026-03-28 ~ 2026-04-27 (30d)
모델: claude-sonnet-4-6
매칭 논문: 44건
확장 키워드: ['manufacturing', 'smart manufacturing', 'industry 4.0', 'predictive maintenance', 'defect detection', 'factory automation', 'industrial AI', 'production optimization']

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — 시각 결함 검출
- **설명**: 산업 표면·부품의 결함을 비전·tomography 기반으로 자동 검출. DDPM·diffusion·foundation 모델·feature fusion 같은 unsupervised/self-supervised 방법이 우세. MVTec·custom 데이터셋이 핵심 벤치마크.
- **빈도**: 10건
- **주차별**: 4 → 3 → 3 → 0
- **대표 논문**:
  - [P-2604.19240] Industrial Surface Defect Detection via Diffusion Generation and Asymmetric Student-Teacher Network — Shuo Feng, Runlin Zhou, Yuyang Li et al., arXiv 2026
  - [P-2604.19259] Feature Perturbation Pool-based Fusion Network for Unified Multi-Class Industrial Defect Detection — Yuanchan Xu, Wenjun Zang, Ying Wu, arXiv 2026
  - [P-2604.19206] When Can We Trust Deep Neural Networks? Towards Reliable Industrial Deployment with an Interpretability Guide — Hang-Cheng Dong, Yuhao Jiang, Yibo Jiao et al., arXiv 2026

### 클러스터 2 — Predictive Maintenance / PHM
- **설명**: 센서·시계열 데이터로 설비 상태 모니터링·고장 예측. Federated learning·spiking neural net·SPC chart·LLM 에이전트 PHM 벤치마크까지 다양. 항공·전력·반도체·시멘트 등 산업별 응용.
- **빈도**: 10건
- **주차별**: 3 → 3 → 4 → 0
- **대표 논문**:
  - [P-2604.19903] A Multi-Plant Machine Learning Framework for Emission Prediction, Forecasting, and Control in Cement Manufacturing — Sheikh Junaid Fayaz, Nestor D. Montiel-Bohorquez, Wilson Ricardo Leal da Silva et al., arXiv 2026
  - [P-2604.01532] PHMForge: A Scenario-Driven Agentic Benchmark for Industrial Asset Lifecycle Maintenance — Ayan Das, Dhaval Patel, arXiv 2026
  - [P-2604.06451] Quality-preserving Model for Electronics Production Quality Tests Reduction — Noufa Haneefa, Teddy Lazebnik, Einav Peretz-Andersson, arXiv 2026

### 클러스터 3 — 인간-로봇 협업 생산
- **설명**: Cobot·AMR·dexterous grasping이 작업장 인간과 공존하며 작업 수행. 안전·피로·공간 인식·계획-할당의 다층 적응이 핵심. 강화학습·diffusion motion·VLM grasping 등 정책 학습 방법.
- **빈도**: 8건
- **주차별**: 2 → 4 → 2 → 0
- **대표 논문**:
  - [P-2604.19670] Multi-Cycle Spatio-Temporal Adaptation in Human-Robot Teaming — Alex Cuellar, Michael Hagenow, Julie Shah, arXiv 2026
  - [P-2604.12669] A hierarchical spatial-aware algorithm with efficient reinforcement learning for human-robot task planning and allocation in production — Jintao Xue, Xiao Li, Nianmin Zhang, arXiv 2026
  - [P-2604.01364] From Automation to Augmentation: A Framework for Designing Human-Centric Work Environments in Society 5.0 — Cristian Espinal Maya, arXiv 2026

### 클러스터 4 — AM 물리 surrogate / PINN
- **설명**: Additive Manufacturing(LPBF·DED·WAAM) 의 열-역학 시뮬레이션을 PINN·neural surrogate로 가속. 데이터 효율성·zero-shot 일반화·privacy preserving 강조. 결함 reasoning 까지 agentic 흐름.
- **빈도**: 5건
- **주차별**: 2 → 1 → 2 → 0
- **대표 논문**:
  - [P-2604.16649] FLARE: A Data-Efficient Surrogate for Predicting Displacement Fields in Directed Energy Deposition — Kittipong Thiamchaiboonthawee, Ghadi Nehme, Ram Mohan Telikicherla et al., arXiv 2026
  - [P-2604.14562] Material-Agnostic Zero-Shot Thermal Inference for Metal Additive Manufacturing via a Parametric PINN Framework — Hyeonsu Lee, Jihoon Jeong, arXiv 2026
  - [P-2604.09889] In-situ process monitoring for defect detection in wire-arc additive manufacturing: an agentic AI approach — Pallock Halder, Satyajit Mojumder, arXiv 2026

### 클러스터 5 — LLM/Agent 기반 공정 계획
- **설명**: LLM·multi-agent 가 공정 계획·스케줄링·CAD·문서 추출을 수행. Industry 4.0 의 의사결정 자동화 — RL·SAT·MIQP 같은 고전 최적화에 LLM autoformalize·KG retrieval 접목.
- **빈도**: 8건
- **주차별**: 1 → 3 → 3 → 1
- **대표 논문**:
  - [P-2604.21029] Integrated packing, placement, scheduling, and routing of personalized production: a pharmaceutical Industry 4.0 use-case with a planar transport system — Viktor Emil Korladinov, Antonin Novak, Zdeněk Hanzálek et al., arXiv 2026
  - [P-2604.16804] AutoOR: Scalably Post-training LLMs to Autoformalize Operations Research Problems — Sumeet Ramesh Motwani, Chuan Du, Aleksander Petrov et al., arXiv 2026
  - [P-2604.15184] Agent-Aided Design for Dynamic CAD Models — Mitch Adler, Matthew Russo, Michael Cafarella, arXiv 2026

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap A — C1(시각 결함 검출)와 C4(AM PINN/surrogate)가 거의 분리되어 있다. 시각 결함 검출은 사후 image-level anomal
- **타입**: between-clusters
- **설명**: C1(시각 결함 검출)와 C4(AM PINN/surrogate)가 거의 분리되어 있다. 시각 결함 검출은 사후 image-level anomaly score만 출력하고, AM 물리 surrogate는 displacement·temperature를 예측하지만 결함 형성 시점에는 침묵한다. 두 신호를 실시간으로 결합해 결함이 시각으로 보이기 전 단계에서 process parameter 조정으로 막는 closed-loop 시스템이 없음.
- **근거 논문**: P-2604.19240, P-2604.16649, P-2604.14562, P-2604.09889, P-2604.04208
- **Skeptic 검토**: ✓ 통과 — 통과 — 2604.09889는 in-situ acoustic+process이지만 PINN 물리 fusion은 없고, 2604.04208은 LPBF 결함 reasoning이지만 retrospective. 어느 클러스터도 PINN-vision real-time 결합을 다루지 않는다.

### Gap B — C2(PHM)와 C3(인간-로봇 협업)이 분리되어 있다. PHM은 설비 health를 추정하지만 그 정보가 task allocation에 들어가
- **타입**: between-clusters
- **설명**: C2(PHM)와 C3(인간-로봇 협업)이 분리되어 있다. PHM은 설비 health를 추정하지만 그 정보가 task allocation에 들어가지 않고, 인간-로봇 task planning(EBQ&SAP·PF-CD3Q)은 인간 fatigue만 고려하고 robot/sensor degradation은 무시한다.
- **근거 논문**: P-2604.12669, P-2604.12667, P-2604.01532, P-2604.13465
- **Skeptic 검토**: ✓ 통과 — 통과 — 2604.12667가 fatigue-predictive RL을 하지만 dyad의 robot side는 정적 가정. 2604.01532 PHMForge가 PHM agent 능력을 평가만 하고 task allocation closed-loop은 미포함. Robot health → task planner pipeline은 비어있음.

### Gap C — Industrial sensor/image 데이터의 cross-machine·cross-plant 분산이 반복 한계로 명시. Industrial
- **타입**: recurring-limitation
- **설명**: Industrial sensor/image 데이터의 cross-machine·cross-plant 분산이 반복 한계로 명시. Industrial-specific foundation model이 없어 매번 새 plant·machine마다 재학습 필요.
- **근거 논문**: P-2604.05335, P-2604.19903, P-2604.14562, P-2604.13465
- **Skeptic 검토**: ✓ 통과 — 통과 (보존적) — 2604.05335는 범용 MOMENT를 시도하지만 산업 특화는 아니라고 자체 인정. 2604.19903는 plant간 3-5x 분산을 정량적으로 보고. PINN(2604.14562)이 material-agnostic을 부분 해결하지만 sensor signal까지 통합한 FM은 부재.

### Gap E — LLM/Agent 기반 공정 계획이 cutting·packing·CAD에는 진출했지만 PHM 정보를 받아 maintenance schedulin
- **타입**: between-clusters
- **설명**: LLM/Agent 기반 공정 계획이 cutting·packing·CAD에는 진출했지만 PHM 정보를 받아 maintenance scheduling으로 변환하는 closed-loop 에이전트가 없음. PHMForge가 평가는 하지만 실용 시스템은 부재.
- **근거 논문**: P-2604.01532, P-2604.16804, P-2604.16280, P-2604.06770
- **Skeptic 검토**: ✓ 통과 — 통과 — PHMForge(2604.01532) task completion 68%로 실용 한계 노출. AutoOR(2604.16804)·KG+LLM(2604.16280)·FlowExtract(2604.06770) 모두 PHM 입력 미지원. PHM→LLM→Schedule end-to-end pipeline 명백히 비어있음.

### Gap F — SNN 기반 power converter PHM(2604.15714)이 270x 에너지 절감을 보이지만 후속·확장 0건. 다른 industria
- **타입**: single-shot
- **설명**: SNN 기반 power converter PHM(2604.15714)이 270x 에너지 절감을 보이지만 후속·확장 0건. 다른 industrial 설비 적용이나 SNN+federated 결합 같은 자연스러운 확장 비어있음.
- **근거 논문**: P-2604.15714, P-2604.13465, P-2604.08474
- **Skeptic 검토**: ✓ 통과 — 통과 — UMW(2604.13465)·aerospace FL(2604.08474) 같은 always-on edge 요구가 명시된 작업이 conventional NN만 쓰고 SNN 시도 안 함. 단발 SNN 결과를 다른 설비로 확장하는 것은 명확한 미개척 영역.

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap D** — Defect 합성 데이터 생성·평가 protocol 표준화 부재 — 각 논문마다 자체 augmentation·metric 사용 · 거부 사유: Skeptic 거부: research gap이라기보다 community-infrastructure work에 가까움. FORGE(2604.07413)가 부분적으로 multimodal eval framework를 제시하고 있고, 표준 protocol 자체를 만드는 작업은 단일 연구실의 정면 연구 주제로는 trivial(c). 새 method 제안 없이 benchmark만 만드는 것은 갭 D의 본질.

</details>

## 3. 연구 제안 (Proposer)

### 제안 1 — PHYDET
**가설**: AM 공정에서 PINN 기반 thermo-mechanical surrogate 예측과 in-situ vision 결함 검출을 cross-attention으로 융합하면, 결함이 시각으로 가시화되기 ≥ 5초 전 단계에서 80% 이상 정확도로 결함을 예측해 process parameter를 자동 조정할 수 있다.
**메우는 갭**: A
**접근**: (1) FLARE 식 displacement surrogate를 process parameter 입력으로 fine-tune해 thermal-mechanical embedding을 추출. (2) DDPM 기반 결함 검출의 visual feature와 PINN embedding을 cross-attention layer로 결합한 PHYDET head가 defect probability + estimated time-to-defect를 동시 출력. (3) 임계 초과 시 Bayesian optimization으로 laser power·deposition velocity를 자동 조정하는 closed-loop. (4) LPBF/WAAM 실험에서 결함 감소율과 lookahead horizon을 측정.
**Baselines**: FLARE displacement surrogate, Material-Agnostic PINN AM, Industrial DDPM defect detection, in-situ WAAM agentic monitoring
**예상 기여**: PINN과 vision 결함 검출의 첫 real-time fusion. 사후 검출이 아닌 사전 예방 closed-loop으로 AM 공정 yield 향상. LPBF/WAAM 양쪽에 일반화 가능한 process-level intervention framework.
**참고**: P-2604.16649, P-2604.14562, P-2604.19240, P-2604.09889, P-2604.04208

### 제안 2 — DYNDUO
**가설**: Robot의 PHM 신호(bearing wear·motor current·thermal margin)를 task allocator의 state에 포함하면 dyad-level(인간 fatigue + 로봇 health) cumulative degradation이 30% 감소하면서 production throughput은 ±5% 이내로 보존된다.
**메우는 갭**: B
**접근**: (1) PF-CD3Q의 fatigue particle filter 옆에 Kalman filter 기반 robot PHM estimator를 병렬 배치해 dyad state {human_fatigue, robot_health}를 구성. (2) Constrained dueling DQN을 dyad-state로 확장 — robot health 임계 미달 시 무거운 작업 action을 mask. (3) PHMForge의 bearing/motor/gearbox scenario를 manufacturing 셀 시뮬레이션에 embed. (4) 32명 user study(EBQ&SAP 패턴)로 효율·주관 만족도 평가.
**Baselines**: PF-CD3Q safe RL, EBQ&SAP hierarchical TPA, PHMForge benchmark, RAPIDDS spatio-temporal adaptation
**예상 기여**: Human-robot 협업 최초의 dyad-state(둘 다 동적 health 모델) 정책. Robot durability 향상 + 예방 정비 cost 절감 동시 검증. Industry 5.0의 human-centric ergonomics 정의를 robot health까지 확장.
**참고**: P-2604.12667, P-2604.12669, P-2604.01532, P-2604.19670

### 제안 3 — INDUS-FM
**가설**: 다중 plant·다중 sensor type(vibration·current·acoustic·image)으로 self-supervised pretraining한 industrial foundation model은 downstream defect/health task에서 fine-tuning sample 100건만으로 plant-specific full-train과 동등 이상 성능(F1 격차 ≤ 0.03)을 낸다.
**메우는 갭**: C
**접근**: (1) 공개 multi-plant 데이터(C-MAPSS, MVTec, SAMSON cavitation 4건, MIMII 등)를 통합한 IndusCorpus 구축. (2) Masked autoencoding + multi-modal contrastive (image-time series-tabular 3-way alignment) pretraining. (3) Encoder freeze → light adapter fine-tune. (4) Cement multi-plant (3-5x 분산), Cross-machine anomaly, UMW unknown fault 세 벤치마크에서 few-shot 평가. (5) Federated variant도 비교.
**Baselines**: MOMENT (general TS FM), Cross-Machine Anomaly (2604.05335 자체 baseline), Cement Multi-Plant ML, Material-Agnostic PINN, Adaptive UMW continual
**예상 기여**: 산업 특화 첫 multi-modal foundation model. Plant간 3-5x 분산을 < 1.5x로 축소 목표. Privacy-preserving variant까지 검증해 collaborative pretraining 가능성 입증.
**참고**: P-2604.05335, P-2604.19903, P-2604.14562, P-2604.13465

### 제안 4 — PHMAGENT
**가설**: PHM 시계열을 LLM-friendly patch token으로 인코딩한 후 ReAct 스타일 agent가 RUL·cost·safety constraint를 보고 maintenance schedule을 출력하면, PHMForge 현재 baseline 68% 대비 task completion 85% 이상을 달성한다.
**메우는 갭**: E
**접근**: (1) PHM time series → patch tokens (1초 windows × 3 modalities). (2) AutoOR 식 RL post-training으로 8B LLM에 schedule formulation 능력 주입. (3) MCP tool: simulator, cost calculator, MTBF predictor, RUL estimator. (4) PHMForge 75 scenario(turbofan/bearing/motor/gearbox)에서 single-shot ReAct vs PHMAGENT closed-loop 비교. (5) Ablation: patch token 없이 raw text vs token 비교.
**Baselines**: PHMForge (Claude Sonnet 4 / GPT-4o / Granite 3.0-8B), AutoOR LLM autoformalize, KG+LLM Manufacturing interpretability, FlowExtract procedural KG
**예상 기여**: PHM-conditioned LLM agent의 첫 closed-loop 시스템. PHMForge SOTA. PHM token encoder는 다른 산업 LLM agent에도 재사용 가능한 모듈로 공개.
**참고**: P-2604.01532, P-2604.16804, P-2604.16280, P-2604.06770

### 제안 5 — SPYRO-PHM
**가설**: Power converter용 SNN 아키텍처(2604.15714)를 ultrasonic metal welding의 multi-sensor 입력으로 확장하면, conventional MLP baseline 대비 fault detection accuracy ≥ 95%를 유지하면서 inference energy를 ≥ 100x 절감해 always-on edge 배포가 가능하다.
**메우는 갭**: F
**접근**: (1) LIF SNN encoder를 4-modal(current·voltage·acoustic·force)로 확장하고 differentiable ODE physics loss 유지. (2) Spike-rate 기반 unknown fault detector — 2604.13465의 hidden-layer threshold를 SNN spike sparsity로 대체. (3) Federated SNN (2604.08474 inspired): spike sparsity 보존 가능한 quantized aggregation. (4) Loihi 2/Akida 하드웨어 측정으로 energy·throughput 정량화.
**Baselines**: Neuromorphic SNN power converter (원 paper), Adaptive UMW continual learning, Aerospace federated quantization (INT4)
**예상 기여**: SNN-PHM의 power converter 너머 일반화. Always-on edge industrial monitoring 실용성 입증. Federated SNN 첫 사례 + spike sparsity와 communication efficiency의 trade-off 정량화.
**참고**: P-2604.15714, P-2604.13465, P-2604.08474

## 4. 참고문헌 (메타DB 기반)

[P-2604.21029] Integrated packing, placement, scheduling, and routing of personalized production: a pharmaceutical Industry 4.0 use-case with a planar transport system, Viktor Emil Korladinov, Antonin Novak, Zdeněk Hanzálek et al., arXiv 2026 · http://arxiv.org/abs/2604.21029v1
[P-2604.19903] A Multi-Plant Machine Learning Framework for Emission Prediction, Forecasting, and Control in Cement Manufacturing, Sheikh Junaid Fayaz, Nestor D. Montiel-Bohorquez, Wilson Ricardo Leal da Silva et al., arXiv 2026 · http://arxiv.org/abs/2604.19903v1
[P-2604.19670] Multi-Cycle Spatio-Temporal Adaptation in Human-Robot Teaming, Alex Cuellar, Michael Hagenow, Julie Shah, arXiv 2026 · http://arxiv.org/abs/2604.19670v1
[P-2604.19377] Towards Energy Impact on AI-Powered 6G IoT Networks: Centralized vs. Decentralized, Anjie Qiu, Donglin Wang, Sanket Partani et al., arXiv 2026 · http://arxiv.org/abs/2604.19377v1
[P-2604.19240] Industrial Surface Defect Detection via Diffusion Generation and Asymmetric Student-Teacher Network, Shuo Feng, Runlin Zhou, Yuyang Li et al., arXiv 2026 · http://arxiv.org/abs/2604.19240v1
[P-2604.19259] Feature Perturbation Pool-based Fusion Network for Unified Multi-Class Industrial Defect Detection, Yuanchan Xu, Wenjun Zang, Ying Wu, arXiv 2026 · http://arxiv.org/abs/2604.19259v1
[P-2604.19206] When Can We Trust Deep Neural Networks? Towards Reliable Industrial Deployment with an Interpretability Guide, Hang-Cheng Dong, Yuhao Jiang, Yibo Jiao et al., arXiv 2026 · http://arxiv.org/abs/2604.19206v1
[P-2604.16804] AutoOR: Scalably Post-training LLMs to Autoformalize Operations Research Problems, Sumeet Ramesh Motwani, Chuan Du, Aleksander Petrov et al., arXiv 2026 · http://arxiv.org/abs/2604.16804v1
[P-2604.16280] Using Large Language Models and Knowledge Graphs to Improve the Interpretability of Machine Learning Models in Manufacturing, Thomas Bayer, Alexander Lohr, Sarah Weiß et al., arXiv 2026 · http://arxiv.org/abs/2604.16280v1
[P-2604.16649] FLARE: A Data-Efficient Surrogate for Predicting Displacement Fields in Directed Energy Deposition, Kittipong Thiamchaiboonthawee, Ghadi Nehme, Ram Mohan Telikicherla et al., arXiv 2026 · http://arxiv.org/abs/2604.16649v1
[P-2604.15714] Neuromorphic Parameter Estimation for Power Converter Health Monitoring Using Spiking Neural Networks, Hyeongmeen Baik, Hamed Poursiami, Maryam Parsa et al., arXiv 2026 · http://arxiv.org/abs/2604.15714v1
[P-2604.18627] Vision-Based Human Awareness Estimation for Enhanced Safety and Efficiency of AMRs in Industrial Warehouses, Maximilian Haug, Christian Stippel, Lukas Pscherer et al., arXiv 2026 · http://arxiv.org/abs/2604.18627v1
[P-2604.15184] Agent-Aided Design for Dynamic CAD Models, Mitch Adler, Matthew Russo, Michael Cafarella, arXiv 2026 · http://arxiv.org/abs/2604.15184v1
[P-2604.14562] Material-Agnostic Zero-Shot Thermal Inference for Metal Additive Manufacturing via a Parametric PINN Framework, Hyeonsu Lee, Jihoon Jeong, arXiv 2026 · http://arxiv.org/abs/2604.14562v1
[P-2604.13465] Adaptive Unknown Fault Detection and Few-Shot Continual Learning for Condition Monitoring in Ultrasonic Metal Welding, Ahmadreza Eslaminia, Kuan-Chieh Lu, Klara Nahrstedt et al., arXiv 2026 · http://arxiv.org/abs/2604.13465v1
[P-2604.12879] FastGrasp: Learning-based Whole-body Control method for Fast Dexterous Grasping with Mobile Manipulators, Heng Tao, Yiming Zhong, Zemin Yang et al., arXiv 2026 · http://arxiv.org/abs/2604.12879v1
[P-2604.12669] A hierarchical spatial-aware algorithm with efficient reinforcement learning for human-robot task planning and allocation in production, Jintao Xue, Xiao Li, Nianmin Zhang, arXiv 2026 · http://arxiv.org/abs/2604.12669v2
[P-2604.12667] Safe reinforcement learning with online filtering for fatigue-predictive human-robot task planning and allocation in production, Jintao Xue, Xiao Li, Nianmin Zhang, arXiv 2026 · http://arxiv.org/abs/2604.12667v2
[P-2604.11154] Environmental Footprint of GenAI Research: Insights from the Moshi Foundation Model, Marta López-Rauhut, Loic Landrieu, Mathieu Aubry et al., arXiv 2026 · http://arxiv.org/abs/2604.11154v1
[P-2604.10969] Towards Automated Solar Panel Integrity: Hybrid Deep Feature Extraction for Advanced Surface Defect Identification, Muhammad Junaid Asif, Muhammad Saad Rafaqat, Usman Nazakat et al., arXiv 2026 · http://arxiv.org/abs/2604.10969v1
[P-2604.12095] A Nonparametric Adaptive EWMA Control Chart for Binary Monitoring of Multiple Stream Processes, Faruk Muritala, Austin Brown, Dhrubajyoti Ghosh et al., arXiv 2026 · http://arxiv.org/abs/2604.12095v1
[P-2604.11320] CLASP: Closed-loop Asynchronous Spatial Perception for Open-vocabulary Desktop Object Grasping, Yiran Ling, Wenxuan Li, Siying Dong et al., arXiv 2026 · http://arxiv.org/abs/2604.11320v1
[P-2604.10953] Diffusion Reinforcement Learning Based Online 3D Bin Packing Spatial Strategy Optimization, Jie Han, Tong Li, Qingyang Xu et al., arXiv 2026 · http://arxiv.org/abs/2604.10953v1
[P-2604.09889] In-situ process monitoring for defect detection in wire-arc additive manufacturing: an agentic AI approach, Pallock Halder, Satyajit Mojumder, arXiv 2026 · http://arxiv.org/abs/2604.09889v1
[P-2604.08844] Spectral Geometry of LoRA Adapters Encodes Training Objective and Predicts Harmful Compliance, Roi Paul, arXiv 2026 · http://arxiv.org/abs/2604.08844v1
[P-2604.09023] CAD 100K: A Comprehensive Multi-Task Dataset for Car Related Visual Anomaly Detection, Jiahua Pang, Ying Li, Dongpu Cao et al., arXiv 2026 · http://arxiv.org/abs/2604.09023v1
[P-2604.08474] Quantization Impact on the Accuracy and Communication Efficiency Trade-off in Federated Learning for Aerospace Predictive Maintenance, Abdelkarim Loukili, arXiv 2026 · http://arxiv.org/abs/2604.08474v1
[P-2604.07413] FORGE: Fine-grained Multimodal Evaluation for Manufacturing Scenarios, Xiangru Jian, Hao Xu, Wei Pang et al., arXiv 2026 · http://arxiv.org/abs/2604.07413v2
[P-2604.06770] FlowExtract: Procedural Knowledge Extraction from Maintenance Flowcharts, Guillermo Gil de Avalle, Laura Maruster, Eric Sloot et al., arXiv 2026 · http://arxiv.org/abs/2604.06770v1
[P-2604.16459] Deep Hierarchical Knowledge Loss for Fault Intensity Diagnosis, Yu Sha, Shuiping Gou, Bo Liu et al., arXiv 2026 · http://arxiv.org/abs/2604.16459v1
[P-2604.07097] Novel Anomaly Detection Scenarios and Evaluation Metrics to Address the Ambiguity in the Definition of Normal Samples, Reiji Saito, Satoshi Kamiya, Kazuhiro Hotta, arXiv 2026 · http://arxiv.org/abs/2604.07097v1
[P-2604.06451] Quality-preserving Model for Electronics Production Quality Tests Reduction, Noufa Haneefa, Teddy Lazebnik, Einav Peretz-Andersson, arXiv 2026 · http://arxiv.org/abs/2604.06451v1
[P-2604.05335] Cross-Machine Anomaly Detection Leveraging Pre-trained Time-series Model, Yangmeng Li, Kei Sano, Toshihiro Kitao et al., arXiv 2026 · http://arxiv.org/abs/2604.05335v1
[P-2604.05490] A Weak-Signal-Aware Framework for Subsurface Defect Detection: Mechanisms for Enhancing Low-SCR Hyperbolic Signatures, Wenbo Zhang, Zekun Long, Zican Liu et al., arXiv 2026 · http://arxiv.org/abs/2604.05490v1
[P-2604.05077] Feature-Aware Anisotropic Local Differential Privacy for Utility-Preserving Graph Representation Learning in Metal Additive Manufacturing, MD Shafikul Islam, Mahathir Mohammad Bappy, Saifur Rahman Tushar et al., arXiv 2026 · http://arxiv.org/abs/2604.05077v1
[P-2604.03656] Beyond Retrieval: Modeling Confidence Decay and Deterministic Agentic Platforms in Generative Engine Optimization, XinYu Zhao, ChengYou Li, XiangBao Meng et al., arXiv 2026 · http://arxiv.org/abs/2604.03656v1
[P-2604.04208] Towards Agentic Defect Reasoning: A Graph-Assisted Retrieval Framework for Laser Powder Bed Fusion, Muhammad Rizwan Awan, Volker Pickert, Muhammad Waqar Ashraf et al., arXiv 2026 · http://arxiv.org/abs/2604.04208v1
[P-2604.03741] Shower-Aware Dual-Stream Voxel Networks for Structural Defect Detection in Cosmic-Ray Muon Tomography, Parthiv Dasgupta, Sambhav Agarwal, Palash Dutta et al., arXiv 2026 · http://arxiv.org/abs/2604.03741v1
[P-2604.02128] SEAL: An Open, Auditable, and Fair Data Generation Framework for AI-Native 6G Networks, Sunder Ali Khowaja, Kapal Dev, Engin Zeydan et al., arXiv 2026 · http://arxiv.org/abs/2604.02128v1
[P-2604.03322] VitaTouch: Property-Aware Vision-Tactile-Language Model for Robotic Quality Inspection in Manufacturing, Junyi Zong, Qingxuan Jia, Meixian Shi et al., arXiv 2026 · http://arxiv.org/abs/2604.03322v1
[P-2604.01732] Solving the Two-dimensional single stock size Cutting Stock Problem with SAT and MaxSAT, Tuyen Van Kieu, Chi Linh Hoang, Khanh Van To, arXiv 2026 · http://arxiv.org/abs/2604.01732v2
[P-2604.01532] PHMForge: A Scenario-Driven Agentic Benchmark for Industrial Asset Lifecycle Maintenance, Ayan Das, Dhaval Patel, arXiv 2026 · http://arxiv.org/abs/2604.01532v1
[P-2604.01991] Integrated Identification of Collaborative Robots for Robot Assisted 3D Printing Processes, Alessandro Dimauro, Davide Tebaldi, Fabio Pini et al., arXiv 2026 · http://arxiv.org/abs/2604.01991v1
[P-2604.01364] From Automation to Augmentation: A Framework for Designing Human-Centric Work Environments in Society 5.0, Cristian Espinal Maya, arXiv 2026 · http://arxiv.org/abs/2604.01364v1

---

## 메타 / 디버그
- model: claude-sonnet-4-6
