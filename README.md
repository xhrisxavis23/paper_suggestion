# paper_suggestion

연구 주제 발굴 봇 — 사용자 키워드를 받아 최근 학계 논문 메타데이터를 분석해 **트렌드 → 갭 → 연구 제안** 보고서를 자동 생성합니다.

현재 버전: **v0.3** ([backlog 17개 항목 모두 반영](docs/plans/v0.3-backlog.md), 토큰 예산 강제, prompt caching, 백필 CLI, opt-in S2/OR). v0.3 마무리 패치로 **rolling window 500일 + 12개 학회 venue + arxiv 재시도 로직** 반영. 다음 마일스톤은 [v0.4-backlog.md](docs/plans/v0.4-backlog.md).

## 구조

- **Layer 1: Collector** (Python CLI / cron) — 매일 arXiv·HF 메타데이터 수집 (S2/OR는 `--with-s2` / `--with-or` 옵트인). **500일 rolling DB** 유지 (2025-01-01 이후 데이터 보존), `metadb/<YYMM>_rolling.jsonl`로 월별 분할.
- **Layer 2: topic-finder skill** (Claude Code) — 사용자 키워드 → 매칭 (substring 또는 embedding) → top-200 cap → 4봇 회의 (Trend → Gap → Skeptic → Proposer, prompt cached) → Markdown 보고서.

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

# 백필 — OR/S2는 target_date 무시하므로 루프 시작 시 1번만 fetch (one-shot)
python -m collector.backfill --start 2025-01-01 --end 2026-04-27 --with-or
python -m collector.backfill --days 30 --with-s2
```

산출물:
- `metadb/<YYMM>_rolling.jsonl` — 월별 인덱스. RollingDB가 디렉터리 통째로 읽어 합침
- `metadb/daily/YYYY-MM-DD.md` — 일별 사람용 다이제스트 (신규 추가 paper만, 주말은 스킵)
- `metadb/stats.json` — 마지막 실행 스냅샷
- `metadb/stats_history.jsonl` — append-only 이력 (CI가 90일 초과분 청소)

자동 실행:
- `.github/workflows/daily_collect.yml` — GitHub Actions 매일 06:00 UTC (pytest 게이트 통과 후 commit)
- 로컬 cron 옵션: `0 6 * * * cd <repo> && .venv/bin/python -m collector.main --with-or >> cron_collect.log 2>&1` (시스템 TZ가 KST면 06:00 KST)

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
| `--deep` | off | v0.4 I-1: 상위 `--deep-k` 매칭 논문의 PDF 본문에서 intro/method/limitations를 추출해 Skeptic·Proposer에만 추가 컨텍스트로 주입. Trend/Gap은 메타만. PDF 캐시는 `metadb/.pdfs/` (gitignored). |
| `--deep-k` | 10 | `--deep`이 켜졌을 때 PDF를 받는 논문 수 |
| `--expand-only` | off | 키워드 확장만 |
| `--dry-run` | off | §3 scope 요약만 보고 4봇 실행 없이 중단 (§3는 항상 표시 후 사용자 승인 필요; --dry-run은 그 이후를 건너뜀) |

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
- Layer 2는 Claude Sonnet 4.6 사용 (호출당 ~600원, 캐싱 시 ~300원)
