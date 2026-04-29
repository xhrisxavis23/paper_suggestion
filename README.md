# paper_suggestion

연구 주제 발굴 봇 — 사용자 키워드를 받아 최근 학계 논문 메타데이터를 분석해 **트렌드 → 갭 → 연구 제안** 보고서를 자동 생성합니다.

현재 버전: **v0.4 (closed 2026-04-29)** — [백로그 Important 4개 + `import_pdf` 보너스 모두 shipped](docs/plans/v0.4-backlog.md). 핵심 변경: **`--deep` PDF 본문 분석 + 아카이브 번들**, **OpenAlex 저널 수집 (`--with-journal`)**, **Gemini 백엔드 (default `gemini-flash`)**, Flash truncation 가드, **페이월 PDF 수동 import 워크플로우**. **매일 한국시간(KST) 06:15에 한 번** GitHub Actions cron이 arxiv/HF/OR/S2/journal 전체를 한 번에 모으고, 수집 후 자동으로 metadb 변경분을 commit·push 합니다. 다음 마일스톤: [v0.5](docs/plans/v0.5-backlog.md) (Unpaywall fallback, venue preset, mixed-model 라우팅, Trend SVG 등).

## 구조

- **Layer 1: Collector** (Python CLI / cron) — **매일 KST 06:15** (= UTC 21:15) GitHub Actions가 arXiv·HF·OpenReview(12 학회)·Semantic Scholar·OpenAlex(저널) **전체**를 한 번에 수집하고 자동 commit·push. **500일 rolling DB** 유지 (2025-01-01 이후 데이터 보존), `metadb/<YYMM>_rolling.jsonl`로 `published_date.YYMM` 기준 월별 분할 — back-dated 저널/학회 import도 자동으로 올바른 파일에 라우팅됨.
- **Layer 2: topic-finder skill** (Claude Code) — 사용자 키워드 → 매칭 (substring 또는 embedding) → top-100 cap → 4봇 회의 (Trend → Gap → Skeptic → Proposer, prompt cached, default Gemini Flash) → Markdown 보고서. `--deep`이면 상위 N편 PDF 본문(intro/method/limitations) 추출 후 Skeptic·Proposer에 추가 컨텍스트 주입.

자세한 설계: [docs/specs/2026-04-26-paper-suggestion-design.md](docs/specs/2026-04-26-paper-suggestion-design.md)
Claude 세션 오리엔테이션: [CLAUDE.md](CLAUDE.md)

## 설치

```bash
git clone https://github.com/xhrisxavis23/paper_suggestion.git
cd paper_suggestion
python -m venv .venv && source .venv/bin/activate
pip install -r collector/requirements.txt pytest
cp .env.example .env             # SEMANTIC_SCHOLAR_API_KEY / ANTHROPIC_API_KEY 채우기 (선택)
pytest                           # 40 unit tests should pass

# 첫 클론이면 16개월치 백필 (2025-01-01부터)
python -m collector.backfill --start 2025-01-01 --end "$(date +%F)" --with-or

# (선택) 임베딩 매칭 사용 시
pip install -r collector/requirements-embedding.txt   # sentence-transformers + faiss-cpu (~2GB)
```

## Layer 1 사용 — 메타DB 수집

```bash
# 오늘 데이터 (arxiv + hf 기본)
python -m collector.main

# 특정 날짜
python -m collector.main --date 2026-04-20

# Semantic Scholar 포함 (API key 필요)
python -m collector.main --with-s2

# OpenReview 포함 (12개 venue 사전 등록 — AAAI/ACL/NAACL/EMNLP/IJCNLP/IJCAI/CVPR/ICCV/KDD/ICLR/ICML/NeurIPS)
python -m collector.main --with-or

# 저널 포함 (OpenAlex, v0.4 — IEEE Trans. Industrial Informatics + Expert Systems with Applications)
python -m collector.main --with-journal

# 백필 — OR/S2/journal은 target_date 무시하므로 루프 시작 시 1번만 fetch (one-shot)
python -m collector.backfill --start 2025-01-01 --end 2026-04-27 --with-or --with-journal
python -m collector.backfill --days 30 --with-s2

# 자동 commit·push 끄기 (디버깅·로컬 실험 시)
python -m collector.main --no-push
python -m collector.backfill --start 2025-01-01 --no-push
```

> **자동 commit·push 기본 켜짐** — `main`은 1회당, `backfill`은 range 끝나고 1회 `metadb/`만 stage→commit→push. 메시지: `data: rolling DB update YYYY-MM-DD` / `data: backfill <start>..<end>`. push 실패하면 commit은 로컬에 보존되니 나중에 `git push`만 다시 하면 복구. 로직: [`collector/src/git_sync.py`](collector/src/git_sync.py).

산출물:
- `metadb/<YYMM>_rolling.jsonl` — 월별 인덱스. RollingDB가 디렉터리 통째로 읽어 합침
- `metadb/daily/YYYY-MM-DD.md` — 일별 사람용 다이제스트 (신규 추가 paper만, 주말은 스킵)
- `metadb/stats.json` — 마지막 실행 스냅샷
- `metadb/stats_history.jsonl` — append-only 이력 (CI가 90일 초과분 청소)

자동 실행:
- `.github/workflows/daily_collect.yml` — GitHub Actions **매일 KST 06:15** (= UTC 21:15, cron `15 21 * * *`), **`--with-s2 --with-or --with-journal`** 모두 켜고 실행 (pytest 게이트 통과 후 bot 계정으로 commit·push). `OPENALEX_MAILTO` secret 설정 시 OpenAlex polite pool에 들어감 (rate-limit 완화). GHA cron은 정각 부하로 수~수십 분 지연되는 게 흔해서 `15` 분으로 둠.
- 로컬 cron 옵션: `15 6 * * * cd <repo> && .venv/bin/python -m collector.main --with-s2 --with-or --with-journal >> cron_collect.log 2>&1` (시스템 TZ가 KST 가정 — UTC면 `15 21 * * *`)
- 로컬 수동 실행도 자동 commit·push가 기본이므로, GHA가 무엇을 돌리든 동일한 결과가 항상 origin에 반영됨 (충돌 시 push 실패 → commit 보존).

## Layer 2 사용 — 연구 주제 보고서 생성

Claude Code 내에서:

```
/find-topic "LLM jailbreak defense"
/find-topic "rag" --max-papers 150 --window 30
/find-topic "diffusion alignment" --match-mode embedding --top-k 200
```

산출물:
- `reports/YYYY-MM-DD-<topic-slug>.md` — 트렌드·갭·제안 보고서 (참고문헌은 클러스터별로 그룹화)
- `reports/.cache/<run-id>/` — 4봇 중간산물 JSON (gitignored, 30개 초과 시 자동 청소)

옵션:

| Arg | Default | 설명 |
|---|---|---|
| `--clusters K` | 3 | 클러스터 개수 |
| `--proposals P` | 3 | 제안 개수 |
| `--window D` | 100 | rolling window 일수 (≤ DB window) |
| `--max-papers M` | 100 | 4봇에 전달되는 hard cap. venue weight desc + date desc로 정렬 후 컷 (top-tier 학회가 arXiv-only보다 우선) |
| `--match-mode` | `substring` | `substring` 또는 `embedding` (heavyweight, 옵트인) |
| `--model` | `gemini-flash` | v0.4 default. `sonnet` / `gemini-pro` / `gemini-flash`. Gemini는 `google-genai` SDK + `GOOGLE_API_KEY` 필요. Flash ~$0.01 / Pro ~$0.06 / Sonnet ~$0.20. |
| `--deep` | off | v0.4 I-1: 상위 `--deep-k` 매칭 논문의 PDF 본문에서 intro/method/limitations를 추출해 Skeptic·Proposer에만 추가 컨텍스트로 주입. Trend/Gap은 메타만. 원본 PDF는 `metadb/.pdfs/`에 캐시되고, `reports/<stem>/`에 하드링크 + `manifest.json` 함께 저장 (둘 다 gitignored, 디스크 0 추가). |
| `--deep-k` | 10 | `--deep`이 켜졌을 때 PDF를 받는 논문 수 |
| `--expand-only` | off | 키워드 확장만 |
| `--dry-run` | off | §3 scope 요약만 보고 4봇 실행 없이 중단 (§3는 항상 표시 후 사용자 승인 필요; --dry-run은 그 이후를 건너뜀) |

### `--deep` 모드 — 두 캐시 위치 이해

`--deep`은 두 군데에 PDF를 둡니다:

| 위치 | 누가 보는가 | 키 형식 | 토픽별 분리? |
|---|---|---|---|
| `metadb/.pdfs/<key>.{pdf,json}` | **파이프라인** (deep 모드 캐시) | `h-<sha1>` (전역 해시) — `arxiv:<id>`는 `<id>` 그대로 | X — 전역 평면 |
| `reports/<stem>/P-<short-id>.pdf` + `manifest.json` | **사람** (보고서 번들) | `P-<short-id>.pdf` | O — 토픽별 폴더 |

캐시는 paper-id 기반 **전역**이라 같은 논문이 다른 토픽에서 또 잡혀도 한 번 받으면 영구 재사용. 보고서 번들은 사람이 보기 좋게 토픽별 폴더로 사본을 둠. 캐시 → 보고서 폴더는 hardlink (디스크 0 추가).

### 페이월 venue PDF 워크플로우 (TII / ESWA 등)

OA가 아닌 venue (IEEE TII, Elsevier ESWA 등)는 `--deep`이 자동으로 PDF를 받지 못합니다 — `paper.pdf_url`이 비어 있거나 DOI 게이트웨이 HTML을 반환하기 때문. 이런 경우 PDF는 **사람이** 기관 access로 받아서 캐시에 주입해야 합니다 (`import_pdf` 스크립트).

#### 어떤 논문이 자동인가 / 수동인가

| Venue | `--deep` 자동? | 이유 |
|---|---|---|
| arXiv | ✅ | `pdf_url` = `arxiv.org/pdf/<id>` — 무료 |
| OpenReview (ICLR/ICML/NeurIPS) | ✅ | OA |
| HF daily papers | ✅ | arXiv 링크 보유 |
| dblp 학회 (CVPR/ICCV/ACL 등) | ⚠️ 부분적 | `pdf_url`이 출판사 게이트일 수 있음 |
| **IEEE TII** | ❌ | IEEE Xplore 구독 필요 |
| **Elsevier ESWA** | ❌ | Hybrid OA — 저자가 OA 비용 안 냈으면 페이월 |

#### 단발 import (PDF 1편)

```bash
# 1. /find-topic --deep 실행. manifest.json 안에 raw_pdf:"missing" 표시된 항목 확인
cat reports/<stem>/manifest.json | jq '.papers[] | select(.raw_pdf == "missing")'

# 2. 기관 access로 PDF 다운로드 (예: ScienceDirect, IEEE Xplore)

# 3. import — short-id는 manifest의 short_id 필드 (P- 프리픽스 있어도 없어도 됨)
python -m skills.topic_finder.scripts.import_pdf \
    --pdf ~/Downloads/coma-ikg.pdf \
    --manifest reports/<stem>/manifest.json \
    --short-id IEEETRAN-bf3127

# 4. /find-topic --deep 재실행 — 캐시 히트로 본문이 deep_context에 포함됨
```

#### 일괄 import (여러 편 한 번에)

두 가지 인박스 위치 지원:

**(A) `metadb/pdf_inbox/<short-id>.pdf`** — 전용 인박스. 임포트 후 `.imported/`로 자동 이동.

```bash
mv ~/Downloads/coma.pdf metadb/pdf_inbox/IEEETRAN-bf3127.pdf
mv ~/Downloads/eswa.pdf metadb/pdf_inbox/EXPERTSY-537c52.pdf
python -m skills.topic_finder.scripts.import_pdf \
    --manifest reports/<stem>/manifest.json --inbox
```

**(B) `reports/<stem>/<short-id>.pdf`** — 보고서 폴더에 직접 드롭. 임포트 후 **그대로 유지** (보고서 번들과 함께 보관).

```bash
cp ~/Downloads/*.pdf reports/<stem>/   # 파일명을 short-id로 rename할 필요 없음 — short-id 일치만 봄
python -m skills.topic_finder.scripts.import_pdf \
    --manifest reports/<stem>/manifest.json \
    --inbox --inbox-dir reports/<stem>/
```

(B)는 `--inbox-dir`이 manifest의 부모 폴더와 같은지 자동 감지 → 같으면 파일 이동 안 함. 이미 캐시에 있는 paper는 자동 skip이라 재실행 안전.

자세한 README와 사용 예: [`metadb/pdf_inbox/README.md`](metadb/pdf_inbox/README.md)

### gap 개수는 왜 파라미터가 없나?

`--clusters K`, `--proposals P`는 사용자가 직접 정하지만 갭 개수는 `gap_hunter.md` 안에 **3~7 범위**로 고정되어 있습니다. **갭은 *발견*하는 것이지 *생성*하는 게 아니다** — N개를 강제하면 LLM이 없는 갭을 만들어내는 위험이 있습니다. 3~7 range는 데이터가 허용하는 만큼만 출력하라는 soft cap.

Gap-Hunter 출력의 일부는 Skeptic이 (a)다른 클러스터에서 이미 다룸 / (b)다른 분야에서 풀림 / (c)trivial / (d)메타로 판단 불가 4가지 사유 중 하나로 reject할 수 있습니다. **6→1 같이 reject가 많은 결과는 토픽이 saturated**하다는 시그널이지 버그가 아니에요.

### 토큰 예산 — 왜 cap이 필요한가

60일 DB로 인기 토픽을 매칭하면 sonnet 200K 컨텍스트를 한참 초과합니다:

| Topic | Matches | ~Tokens |
|---|---|---|
| `llm safety` | 2,545 | ~909K |
| `rag` | 6,563 | ~2,336K |
| `agent` | 3,511 | ~1,238K |
| `video generation` | 305 | ~110K |

`--max-papers 200`이면 ~75K input tokens라 sonnet 200K 안에 여유롭게 들어갑니다.

## 환경변수

| Var | 필수? | 용도 |
|---|---|---|
| `SEMANTIC_SCHOLAR_API_KEY` | `--with-s2` 시 권장 | 없으면 모든 venue가 rate-limit (`stats.failures`에 기록) |
| `ANTHROPIC_API_KEY` | Sonnet SDK 모드 시 권장 | SDK + `cache_control` 사용 (~50% 비용 절감). 없으면 `claude` CLI fallback |
| `GOOGLE_API_KEY` | `--model gemini-*` 시 필수 | https://aistudio.google.com/apikey . `google-genai` SDK + `cached_content` 사용 |

## 개발

```bash
pytest                       # 40 unit tests, 0.1s
pytest -m integration        # 네트워크 호출 (slow, deselected by default)
```

DB / 매칭 단독 사용:

```bash
# 매칭 + 60일 윈도우 + top-200 cap
python -m skills.topic_finder.scripts.match_substring \
    --keywords-file keywords.json \
    --out matched.jsonl \
    --window-days 60 \
    --max-papers 200

# 임베딩 매칭
python -m skills.topic_finder.scripts.match_embedding \
    --topic "sparse autoencoder" \
    --out matched.jsonl \
    --window-days 60 --top-k 200
```

## v0.4 변경 요약

**Important (4 — 모두 shipped)**
- **I-1 `--deep` 모드**: 상위 `--deep-k` 매칭 논문의 PDF 본문에서 intro/method/limitations 추출 → Skeptic·Proposer에 추가 컨텍스트 주입. 원본 PDF는 `metadb/.pdfs/` 캐시 + `reports/<stem>/`에 하드링크 (gitignored, 디스크 0 추가). pypdf + 제목 정규식.
- **I-2 Journal coverage**: OpenAlex 기반 저널 scraper (`--with-journal`). 현재 IEEE Trans. Industrial Informatics + Expert Systems with Applications 2개 등록 (`JOURNAL_TARGETS`에 ISSN 추가하면 확장). paratext (TOC/errata) 자동 컷, per-venue 200편 cap. venue weight=3 (AAAI tier, > arXiv).
- **I-3 Gemini 백엔드**: `/find-topic --model {sonnet|gemini-pro|gemini-flash}`, **default = `gemini-flash`** (~$0.01/run vs Sonnet ~$0.20). Anthropic ephemeral cache와 동일하게 Gemini `cached_content` (TTL 1h)로 4봇 prefix 공유. per-bot 토큰 telemetry → `usage.json`.
- **I-4 Flash truncation 가드**: trend 프롬프트에 `paper_ids ≤ 30` 제약 + `finish_reason` 로깅으로 향후 MAX_TOKENS 트런케이션이 silently malformed JSON으로 빠지는 것 방지.

**보너스 (post-ship verification 도중 추가)**
- **`import_pdf` 스크립트**: 페이월 venue PDF를 사람이 받은 후 deep 캐시에 주입. 단발 모드 (`--pdf` + `--short-id`) + 인박스 모드 (`metadb/pdf_inbox/` 또는 `reports/<stem>/` 직접 드롭). 캐시는 paper-id 기반 영구 보존. 자세한 사용법은 위 §"페이월 venue PDF 워크플로우" 참고.

**인프라**
- **매일 KST 06:15** cron이 **arxiv + HF + OR + S2 + journal** 전부 한 번에 수집 (`.github/workflows/daily_collect.yml`)
- 수집 후 `metadb/` 변경분을 자동 commit·push (로컬 `main`/`backfill`도 동일, [`collector/src/git_sync.py`](collector/src/git_sync.py); `--no-push`로 opt-out)
- backfill 시 OR/S2/journal은 one-shot, arxiv/HF만 per-day
- RollingDB가 `published_date.YYMM` 기준 자동 라우팅 — back-dated 저널 import도 정확히 해당 월 파일에 들어감

전체 변경 내역은 [docs/plans/v0.4-backlog.md](docs/plans/v0.4-backlog.md). v0.5 백로그(미해결 + 새 항목)는 [docs/plans/v0.5-backlog.md](docs/plans/v0.5-backlog.md).

## v0.3 변경 요약

**Important (5)**
- **I-1 token budget**: `--max-papers` (default 200), date+venue 랭킹. 인기 토픽 컨텍스트 OOM 방지
- **I-2 backfill CLI**: `python -m collector.backfill`
- **I-3 prompt caching**: 4봇 공유 컨텍스트에 `cache_control: ephemeral`, ~50% input cost 절감 (SDK 모드)
- **I-4 stats history**: `metadb/stats_history.jsonl` append-only, 실패 발생 시점 추적 가능
- **I-5 OR/S2 opt-in**: 두 소스 모두 default off (현재 환경에서 0건 기여), 명시적 opt-in 필요

**Minor (12)**
- M-1 주말 digest skip / M-2 embedding match (opt-in) / M-3-4 missing test coverage / M-5 cache auto-prune
- M-6 concurrent scrapers / M-7 pytest in CI / M-8 `Paper.year` derived / M-9 `.env.example`
- M-10 `also_in` HF/arxiv merge / M-11 bibliography grouped by cluster / M-12 file lock for concurrent writers

**v0.3 마무리 패치** (post-shipping)
- Rolling window 60일 → **500일** (2025-01-01 이후 데이터 보존, conference 학회 cycle 1번 이상 포함)
- OR venue 1개 → **12개** (dblp.org/conf/ 패턴으로 비-OR-native 학회 metadata 가져옴 + ICLR/ICML/NeurIPS OR-native)
- Backfill 리팩터: OR/S2를 per-day가 아닌 **one-shot** 호출 (482일 × OR 호출 = ~5h 절감)
- arXiv 429/5xx/Timeout **재시도** with exponential backoff (5/15/45/90s)

전체 변경 내역은 [docs/plans/v0.3-backlog.md](docs/plans/v0.3-backlog.md) 참고.

## 라이선스 / 의존성

- Python 3.11+
- 코어: `requests`, `python-dateutil`, `pytest`
- SDK 캐싱: `anthropic` (옵션)
- 임베딩 매칭: `sentence-transformers`, `faiss-cpu` (옵션, ~2GB)
- Layer 2 default: **gemini-flash** (호출당 ~$0.01 ≈ 15원). Sonnet 4.6 / gemini-pro도 선택 가능 (Sonnet ~$0.20, Pro ~$0.06–0.15)
