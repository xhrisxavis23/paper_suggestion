# paper_suggestion — 연구 주제 발굴 봇 설계

**작성일**: 2026-04-26  
**상태**: Brainstorming 완료, 구현 대기  
**관련 자산**: `paper_find/` (Layer 1 fork 원본), `paper_search/` (Layer 2 패턴 참고, v0.2 통합 후보)

---

## 1. 미션

사용자가 입력한 연구 키워드에 대해, 최근 1개월 학계 논문 메타데이터를 분석해 **(1) 현재 트렌드 → (2) 미개척 갭 → (3) 새로운 연구 제안**의 흐름을 한 보고서로 자동 생성한다.

대전제: 사용자가 "이런 트렌드가 있고, 그 중 아직 안 된 부분이 저런 것들이 있어서 연구하면 좋겠다" 라고 읽을 수 있는 단일 마크다운 산출물을 만든다.

---

## 2. 사용 모드 (합의된 결정)

| 결정 사항 | 합의 내용 |
|---|---|
| 메인 사용 방식 | **on-demand 키워드 입력** (`/find-topic "..."`) |
| 데이터 수집 | **매일 백그라운드** cron으로 메타데이터 누적 — 트렌드 시계열 보존 |
| DB 정책 | **무필터 수집** (paper_find의 토픽 필터 제거), 1개월 rolling window |
| 메타 vs 본문 | **메타데이터(제목·초록)만** — 토큰 효율 최우선. PDF 본문 분석은 v0.2로 연기 |
| 키워드 매칭 | **LLM 키워드 확장 + substring** — 한 번의 LLM 호출로 동의어 5~10개 확장 후 deterministic 매칭 |
| 회의 메커니즘 | **역할 봇 4종 직렬 파이프라인** (논문 페르소나 토론·자유 토론 아님) |
| LLM 모델 | **Claude Sonnet 4.6** — 토큰 절약 |
| 도구 형태 | **하이브리드** — 수집은 Python CLI / cron, 회의는 Claude Code 스킬 |

---

## 3. 고수준 아키텍처

```
┌────────────────────────────────────────────────────────────┐
│  Layer 1: Data Collector  (Python CLI, cron 자동)           │
│                                                             │
│  매일 cron 실행 → 4개 스크레이퍼 (arXiv·HF·OpenReview·S2)   │
│           ↓                                                 │
│  무필터 메타데이터 (제목·초록·저자·venue·날짜·url)          │
│           ↓                                                 │
│  metadb/daily/YYYY-MM-DD.md  (per-day, 사람 검토용)         │
│  metadb/rolling.jsonl        (30일 인덱스, 매칭 입력)       │
│  metadb/stats.json           (모니터링)                     │
└────────────────────────────────────────────────────────────┘
                          │
                          ▼  사용자 발화: /find-topic "X"
┌────────────────────────────────────────────────────────────┐
│  Layer 2: Topic-Finder Skill  (Claude Code skill, on-demand)│
│                                                             │
│  ① LLM 키워드 확장 (X → 동의어/관련어 리스트)               │
│  ② rolling.jsonl substring 매칭 → 관련 논문 N건             │
│  ③ Scope confirmation (사용자 승인)                         │
│                                                             │
│  ┌────────── 4-bot 회의 (직렬 파이프라인) ──────────┐     │
│  │ 🔍 Trend-Analyzer → 토픽 클러스터 K개            │     │
│  │ 🕳️ Gap-Hunter     → 갭 후보 M개                 │     │
│  │ 😈 Skeptic        → 살아남은 갭 + 거부 사유      │     │
│  │ 💡 Proposer       → 연구 제안 P개 + 인용          │     │
│  └──────────────────────────────────────────────────┘     │
│                                                             │
│  ④ Python: JSON 산출물 → Markdown 보고서 조립               │
│  ⑤ reports/YYYY-MM-DD-<slug>.md                            │
└────────────────────────────────────────────────────────────┘
```

---

## 4. Layer 1: Data Collector

### 4.1 책임
- 매일 외부 학술 API에서 신규 메타데이터 수집
- 1개월 rolling window 유지 (30일 초과분 자동 prune)
- LLM 호출 없음, 결정론적 처리

### 4.2 수집 대상

paper_find의 4개 스크레이퍼를 fork하여 **토픽 필터 제거** (무필터 수집).

| 소스 | 카테고리 / 대상 | 비고 |
|---|---|---|
| **arXiv** | `cs.AI`, `cs.LG`, `cs.CL`, `cs.CV`, `cs.RO`, `stat.ML` | 일별 신규 제출. 카테고리는 config로 변경 가능 |
| **HuggingFace** | Daily Papers (큐레이션) + 최근 7일 trending | 일별 |
| **OpenReview** | ICLR / NeurIPS / ICML 활성 venue | 신규 submission |
| **Semantic Scholar** | AAAI · NeurIPS · ICML · ICLR · CVPR · KDD published in last 30d | 일별 |

### 4.3 저장 구조

```
metadb/
├── daily/
│   ├── 2026-04-26.md             # 일별 다이제스트 (paper_find output 형식 유사)
│   └── ... (60일분 보관)
├── rolling.jsonl                 # 60일 인덱스, 한 줄 = 한 논문
└── stats.json                    # 마지막 실행 시각, 소스별 건수, 실패 목록
```

> Note: `categories` is currently arxiv-only. HF / OpenReview / S2 entries leave it `[]`. A future category-based filter would silently exclude non-arxiv papers if not handled explicitly.

#### `rolling.jsonl` 한 줄 스키마
```json
{
  "id": "arxiv:2404.12345",
  "title": "...",
  "abstract": "...",
  "authors": ["..."],
  "venue": "arXiv" | "NeurIPS" | "ICLR" | ...,
  "date": "2026-04-26",
  "url": "...",
  "pdf_url": "...",
  "source": "arxiv" | "hf" | "openreview" | "s2",
  "categories": ["cs.LG", "cs.AI"]
}
```

### 4.4 일일 실행 흐름

```
cron 06:00 UTC (KST 15:00)
   ↓
collector/main.py
   ↓
4개 스크레이퍼 병렬 실행 → 신규 메타 수집
   ↓
dedupe (arxiv_id > doi > normalized title)
   ↓
daily/YYYY-MM-DD.md 작성 + rolling.jsonl append
   ↓
30일 초과분 prune (daily 폴더 + rolling.jsonl)
   ↓
git add metadb/ && git commit
```

### 4.5 의존성
`requests`, `python-dateutil` (paper_find 그대로). 옵션: `SEMANTIC_SCHOLAR_API_KEY` env (요청 한도 ↑).

---

## 5. Layer 2: Topic-Finder Skill

### 5.1 구조

`paper_search`의 SKILL.md 패턴 차용. SKILL.md가 워크플로우 명시, `prompts/*.md` 페르소나 로드, `scripts/*.py` 결정론적 처리.

```
skills/topic-finder/
├── SKILL.md                      # 4단계 워크플로우 명시
├── prompts/
│   ├── expand_keywords.md        # ① LLM 키워드 확장
│   ├── trend_analyzer.md         # ③
│   ├── gap_hunter.md             # ④
│   ├── skeptic.md                # ⑤
│   └── proposer.md               # ⑥
└── scripts/
    ├── load_metadb.py            # rolling.jsonl 로딩
    ├── match_substring.py        # ② substring 매칭
    └── build_report.py           # ⑦ JSON → Markdown
```

### 5.2 봇 사양

#### ① 🔍 Trend-Analyzer
| | |
|---|---|
| **입력** | 사용자 키워드 X + 확장 키워드 + 매칭 논문 메타 N건 (보통 50~200) |
| **작업** | 제목·초록 기반으로 토픽 클러스터 K개 (3~7) 도출. 빈도 + 주차별 시계열 + 대표 논문 3 |
| **출력** | `clusters.json`<br>`[{name, description, paper_ids, weekly_count, top3}, ...]` |
| **프롬프트 핵심** | 클러스터 축은 *방법론 / 문제정의 / 도메인* 중 하나로 일관 |

#### ② 🕳️ Gap-Hunter
| | |
|---|---|
| **입력** | `clusters.json` + 매칭 논문 메타 |
| **작업** | 3 타입 갭 식별:<br>(1) **선행 O 후속 X** — 단발 논문<br>(2) **클러스터 사이 빈공간** — 두 토픽 결합 안 된 영역<br>(3) **반복되는 한계** — 여러 논문이 같은 limitation 명시 |
| **출력** | `gaps.json`<br>`[{type, description, evidence_papers, why_gap}, ...]` |
| **프롬프트 핵심** | 추측 금지. 메타데이터에 명시된 근거가 있어야 함 |

#### ③ 😈 Skeptic
| | |
|---|---|
| **입력** | `gaps.json` (필요 시 메타DB 재참조) |
| **작업** | 각 갭에 도전: (a) 진짜 미개척인가 (b) 다른 분야에서 풀렸나 (c) trivial 한가 (d) 메타로는 알 수 없는 영역인가 |
| **출력** | `gaps_validated.json` — 살아남은 갭 + 거부된 갭 (사유 포함) |
| **프롬프트 핵심** | 옹호하지 말고 깐다. 거부 사유는 메타DB의 다른 클러스터·논문 인용 |

#### ④ 💡 Proposer
| | |
|---|---|
| **입력** | 살아남은 갭 + 클러스터 + 매칭 논문 메타 |
| **작업** | 갭마다 1~2개 연구 제안 = {시그니처 명명, 한 줄 가설, 접근, baseline·dataset, 예상 기여} |
| **출력** | `proposals.json` |
| **프롬프트 핵심** | trivial 확장 금지 (X+ablation). 갭이 명시한 한계를 정면으로 푸는 제안만. 인용은 메타DB 안 논문 [P*]만 |

### 5.3 진행 흐름 (직렬 파이프라인)

```
SKILL.md
  → §1 키워드 확장             (1 LLM 호출, ≈10K tokens)
  → §2 substring 매칭          (Python 결정론, 0 tokens)
  → §3 Scope confirmation      (사용자 승인 게이트)
  → §4 Trend-Analyzer          (1 LLM 호출, ≈35K tokens)
  → §5 Gap-Hunter              (1 LLM 호출, ≈30K tokens)
  → §6 Skeptic                 (1 LLM 호출, ≈25K tokens)
  → §7 Proposer                (1 LLM 호출, ≈35K tokens)
  → §8 보고서 조립             (Python, 0 tokens)
```

총 **5번의 LLM 호출** (확장 1 + 4봇 4). 각 호출은 직전 산출만 받음 (컨텍스트 누적 X).

### 5.4 토큰 비용 추정 (Sonnet 4.6 기준)

- 매칭 200건 메타 ≈ 25K input tokens
- 5번 LLM 호출 평균 30K input + 5K output
- 총 ≈ **150K input + 25K output ≈ 1500~2000원/회당** → **Sonnet 4.6은 약 ~600원**

### 5.5 산출물 cache

```
reports/.cache/<run-id>/
├── expanded_keywords.json
├── matched_papers.json
├── clusters.json
├── gaps.json
├── gaps_validated.json
└── proposals.json
```

각 단계 산출물을 보관 → 디버깅·재실행 시 특정 단계부터 재시작 가능.

---

## 6. 사용자 인터페이스

### 6.1 명령어

```
/find-topic "<키워드>"  [옵션...]
```

### 6.2 인자

| 인자 | 기본값 | 설명 |
|---|---|---|
| `<키워드>` (positional) | (필수) | 사용자 관심 토픽 (자유 문구) |
| `--top N` | 10 | 클러스터마다 노출할 대표 논문 수 |
| `--clusters K` | 5 | 추출할 클러스터 개수 (3~7 권장) |
| `--proposals P` | 5 | 최종 제안 개수 |
| `--window D` | 30 | rolling window 일수 |
| `--expand-only` | off | 매칭만 하고 4봇 회의 안 함 (디버그) |
| `--dry-run` | off | 매칭 건수 + 예상 토큰 보고 종료 |
| `--output <path>` | `reports/YYYY-MM-DD-<slug>.md` | 보고서 경로 |

### 6.3 호출 예시

```
/find-topic "multi-agent LLM safety"
/find-topic "diffusion alignment" --clusters 7 --proposals 3
/find-topic "embodied agent benchmark" --dry-run
```

### 6.4 Scope confirmation 게이트

키워드 확장 결과를 사용자에게 보여주고 명시적 승인 받은 뒤 4봇 회의 시작:

```
**Topic:** "multi-agent LLM safety"
**Expanded keywords:** [multi-agent, agent collaboration, llm safety,
  agent alignment, multi-agent debate, agent coordination risks, ...]
**매칭 논문:** 87건 (rolling 30d 기준)
**클러스터 K = 5, 제안 P = 5, Sonnet 4.6**
**예상 토큰:** ~150K input, ~25K output
**예상 비용:** ~600원

Approve / 수정 / abort
```

매칭이 너무 적으면(<10건) 경고 + 재키워드 제안. 너무 많으면(>500건) 좁힘 추천.

---

## 7. Output 보고서 형식

`reports/YYYY-MM-DD-<topic-slug>.md`:

```markdown
# Research Topic Suggestion — "<키워드>"

생성: <ISO timestamp>
DB 윈도우: <YYYY-MM-DD> ~ <YYYY-MM-DD> (30d)
모델: claude-sonnet-4-6
매칭 논문: <N>건
확장 키워드: [k1, k2, ...]

---

## 1. 트렌드 요약 (Trend-Analyzer)

### 클러스터 1 — <이름>
- **핵심 주장**: ...
- **빈도**: 22건 (전체의 25%)
- **시계열**: 4주 전 3건 → 최근 주 9건 (▲ 증가)
- **대표 논문**: [P1], [P2], [P3]

### 클러스터 2 — ...

---

## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)

### Gap A — <짧은 제목>
- **타입**: 클러스터 사이 빈공간 / 선행 O 후속 X / 반복되는 한계
- **설명**: ...
- **근거 논문**: [P5], [P12], [P18]
- **Skeptic 검토**: ✓ 통과 — <한 줄 사유>

### Gap B — ...

<details>
<summary>검토 후 제외된 갭 (참고용)</summary>

- **Gap X** — 거부 사유: 클러스터 3에서 이미 다룸 [P22]

</details>

---

## 3. 연구 제안 (Proposer)

### 제안 1 — <시그니처 명명>
**가설**: ...
**메우는 갭**: Gap A
**접근**: ...
**Baselines**: ...
**예상 기여**: ...
**참고**: [P5], [P12], [P18]

### 제안 2 — ...

---

## 4. 참고문헌 (메타DB 기반)

[P1] Title, Authors, Venue YYYY · <url>
...

---

## 메타 / 디버그
- 4봇 호출 횟수: 5
- 실제 토큰: 138K input / 21K output
- 비용 추정: ~600원
- 중간산물: `reports/.cache/<run-id>/`
```

### 핵심 설계 의도
- **트렌드 → 갭 → 제안** 한 페이지 내려가며 읽는 구조
- **모든 인용은 [P*] 메타DB 안 논문만** — 환각 방지
- **거부된 갭은 `<details>` 접어둠** — 검토 흔적 보존, 본문 가독성 유지
- **시그니처 명명** — Proposer가 제안마다 짧은 이름 부여

---

## 8. 디렉터리 구조 (전체)

```
paper_suggestion/
├── README.md                              # 사용자용 사용법 / 설치 / 호출 예시
├── docs/
│   └── specs/
│       └── 2026-04-26-paper-suggestion-design.md  # 본 문서
│
├── collector/                             # Layer 1
│   ├── main.py                            # cron 진입점
│   ├── src/
│   │   ├── config.py                      # arXiv 카테고리, S2 venue 등
│   │   ├── db.py                          # rolling.jsonl 쓰기/prune
│   │   ├── models.py                      # Paper dataclass
│   │   ├── formatter.py                   # daily/*.md 생성
│   │   └── scrapers/
│   │       ├── arxiv.py                   # ← paper_find fork
│   │       ├── huggingface.py             # ← paper_find fork
│   │       ├── openreview.py              # ← paper_find fork
│   │       └── semantic_scholar.py        # ← paper_find fork
│   └── requirements.txt                   # requests, python-dateutil
│
├── skills/topic-finder/                   # Layer 2 (Claude Code 스킬)
│   ├── SKILL.md                           # 4단계 워크플로우
│   ├── prompts/
│   │   ├── expand_keywords.md
│   │   ├── trend_analyzer.md
│   │   ├── gap_hunter.md
│   │   ├── skeptic.md
│   │   └── proposer.md
│   └── scripts/
│       ├── load_metadb.py
│       ├── match_substring.py
│       └── build_report.py
│
├── metadb/                                # 데이터 저장 (gitignore 옵션)
│   ├── daily/
│   ├── rolling.jsonl
│   └── stats.json
│
├── reports/                               # 보고서 출력
│   └── .cache/                            # 중간산물
│
└── .github/workflows/
    └── daily_collect.yml                  # Layer 1 cron
```

---

## 9. v0.1 범위 / Out-of-Scope

### v0.1 포함
- [x] Layer 1: 4개 스크레이퍼 fork + 무필터 수집 + rolling 30일
- [x] Layer 2: 4봇 직렬 파이프라인 (메타데이터만)
- [x] LLM 키워드 확장 + substring 매칭
- [x] Scope confirmation 게이트
- [x] Markdown 보고서
- [x] Sonnet 4.6 모델
- [x] 일별 GitHub Actions cron
- [x] README 사용법 문서

### v0.2 후보 (deferred)
- `--deep` 옵션: paper_search §6+ 호출하여 핵심 논문 PDF 본문 분석
- 임베딩 기반 매칭 (sentence-transformers + FAISS)
- 사용자 작업 추적 / 개인화 (D 옵션)
- Trend-Analyzer 시계열 시각화 (matplotlib SVG)
- Slack/Discord webhook 통지

### 명시적 Out-of-Scope (YAGNI)
- 논문 페르소나 토론 (A 옵션) — 토큰 부담 ↑, B로 충분
- 자유 토론 / 라운드 반복 — 직렬 파이프라인이 더 일관적
- Vector DB 인프라 (Chroma, Pinecone 등)
- 웹 UI (보고서는 Markdown으로 충분)
- 다국어 키워드 매칭 (영문만; 메타DB 자체가 영문)

---

## 10. 의존성 관계

```
paper_find  ──fork──→  collector/src/scrapers/  (필터 제거)
paper_search  ─참고→   skills/topic-finder/SKILL.md  (워크플로우 패턴)
                        skills/topic-finder/scripts/  (subprocess 호출은 v0.2)
```

paper_find의 자산을 코드 복사로 받되, 가져온 뒤로는 paper_find와 독립 진화 (paper_find의 토픽 필터 정책과 다른 길로 갈 가능성 ↑).

---

## 11. 성공 기준 (v0.1 완료 정의)

- [ ] `python collector/main.py` 1회 실행 시 `metadb/rolling.jsonl` ≥ 100건
- [ ] `/find-topic "<키워드>"` 한 번 실행 시 `reports/*.md` 생성, 4봇 모두 정상 동작
- [ ] 보고서에 클러스터 ≥ 3개, 갭 ≥ 2개, 제안 ≥ 2개
- [ ] 보고서의 모든 [P*] 인용이 매칭 논문 메타 안에 실재 (환각 0건)
- [ ] cron 1회 자동 실행 성공 (GitHub Actions 로그 확인)
- [ ] README의 사용법대로 따라했을 때 첫 실행이 막힘 없이 끝남

---

## 12. 합의된 결정 요약

이 spec은 다음 8개 결정으로 구성됨 (brainstorming 대화에서 합의):

1. 봇 산출물: 트렌드(A) + 연구 제안(B) 조합
2. 호출 방식: on-demand 메인 + 매일 자동 DB 갱신
3. DB 역할: 메타데이터만, 1개월 rolling
4. "회의": 역할 봇 4종 (B 옵션)
5. DB 수집 범위: 무필터 (A 옵션)
6. 키워드 매칭: LLM 확장 + substring (B 옵션)
7. 도구 형태: CLI + Claude 스킬 하이브리드 (C 옵션)
8. paper_search 통합: v0.2로 연기 (β 옵션)

---

**Next**: 본 spec 사용자 검토 후 → `superpowers:writing-plans` 스킬로 구현 plan 작성.
