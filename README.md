# paper_suggestion

연구 주제 발굴 봇 — 사용자 키워드를 받아 최근 60일 학계 논문 메타데이터를 분석해 **트렌드 → 갭 → 연구 제안** 보고서를 자동 생성합니다.

현재 버전: **v0.2** ([backlog 16개 항목 모두 반영](docs/plans/v0.2-backlog.md), 60일 DB, 월별 분할 저장)

## 구조

- **Layer 1: Collector** (Python CLI / cron) — 매일 arXiv·HF·OpenReview·S2에서 메타데이터 수집, **60일 rolling DB** 유지. DB는 `metadb/<YYMM>_rolling.jsonl`로 월 단위 분할.
- **Layer 2: topic-finder skill** (Claude Code) — 사용자 키워드 → 4봇 회의 (Trend → Gap → Skeptic → Proposer) → Markdown 보고서.

자세한 설계: [docs/specs/2026-04-26-paper-suggestion-design.md](docs/specs/2026-04-26-paper-suggestion-design.md)
Claude 세션 오리엔테이션: [CLAUDE.md](CLAUDE.md)

## 설치

```bash
git clone https://github.com/xhrisxavis23/paper_suggestion.git
cd paper_suggestion
python -m venv .venv && source .venv/bin/activate
pip install -r collector/requirements.txt pytest
pytest                              # 29 unit tests should pass
```

## Layer 1 사용 — 메타DB 수집

```bash
# 오늘 데이터 수집 (수동 실행)
python -m collector.main

# 특정 날짜
python -m collector.main --date 2026-04-20

# 일부 소스 스킵 (디버깅용 / S2 키 없을 때)
python -m collector.main --skip-arxiv
python -m collector.main --skip-or --skip-s2
```

산출물:
- `metadb/<YYMM>_rolling.jsonl` — 월별 인덱스. `RollingDB`가 디렉터리를 통째로 읽어 합칩니다 (예: 2602 + 2603 + 2604 = 60일치)
- `metadb/daily/YYYY-MM-DD.md` — 일별 사람용 다이제스트 (**신규 추가된 논문만** 표시)
- `metadb/stats.json` — 마지막 실행 통계 + `failures` 리스트 (S2 rate-limit, arxiv per-cat 실패 등)

자동 실행은 `.github/workflows/daily_collect.yml`이 매일 06:00 UTC에 처리합니다 (CI에서 60일 초과 daily 디지스트 자동 청소).

## Layer 2 사용 — 연구 주제 보고서 생성

Claude Code 내에서:

```
/find-topic "LLM jailbreak defense"
/find-topic "diffusion alignment" --clusters 7 --proposals 3
/find-topic "embodied agent benchmark" --window 30 --dry-run
```

산출물:
- `reports/YYYY-MM-DD-<topic-slug>.md` — 트렌드·갭·제안 보고서
- `reports/.cache/<run-id>/` — 4봇 중간산물 JSON (gitignored, 디버깅·재실행용)

옵션:

| Arg | Default | 설명 |
|---|---|---|
| `--top N` | 10 | 클러스터당 대표 논문 |
| `--clusters K` | 5 | 클러스터 개수 |
| `--proposals P` | 5 | 제안 개수 |
| `--window D` | 60 | rolling window 일수 (≤ DB window) |
| `--expand-only` | off | 키워드 확장만 |
| `--dry-run` | off | 매칭/토큰 추정만 |

## 환경변수

| Var | 필수? | 용도 |
|---|---|---|
| `SEMANTIC_SCHOLAR_API_KEY` | 권장 | S2 search-API rate limit 회피. **없으면 S2 venue가 전부 0건** (rate-limited 표시는 `stats.json.failures`에서 확인) |

## 개발

```bash
pytest                       # unit tests (29 tests, 0.1s)
pytest -m integration        # 네트워크 호출 (slow, deselected by default)
```

DB 형식 / 유틸 직접 사용:

```bash
# 월별 파일 레이아웃 확인
ls metadb/*_rolling.jsonl

# 키워드 매칭 단독 실행 (window 필터 지원)
python -m skills.topic_finder.scripts.match_substring \
    --keywords-file keywords.json \
    --out matched.jsonl \
    --window-days 30
```

## v0.2 변경 요약

- **DB 윈도우 30 → 60일**, `<YYMM>_rolling.jsonl`로 월별 분할 (개별 파일 ≤ ~30 MB)
- **`--window D` 진짜 동작** (이전엔 SKILL.md만 advertise)
- **`stats.json.failures`** — partial failure 노출 (S2 429, arxiv per-cat exception 등)
- **digest = newly-added만** (이전엔 raw fetch list라 동일 paper가 여러 일자에 중복 표시됨)
- **collision-resistant `_short_id`**, **author truncation** 명시 (≤3 verbatim, 4+ et al.)
- **`skills/topic-finder/` → `topic_finder/`** rename + symlink 제거 (Windows 호환)
- **테스트 18 → 29개** — `_date_window` 4종, `RollingDB.append` in-batch dedup, 월별 파티셔닝, `prune` 월별 동작, HF fallback mock 등

전체 변경 내역은 [docs/plans/v0.2-backlog.md](docs/plans/v0.2-backlog.md) 참고.

## 라이선스 / 의존성

- Python 3.11+
- `requests`, `python-dateutil`, `pytest`
- Layer 2는 Claude Sonnet 4.6 사용 (호출당 ~600원)
