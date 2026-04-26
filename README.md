# paper_suggestion

연구 주제 발굴 봇 — 사용자 키워드를 받아 최근 1개월 학계 논문 메타데이터를 분석해 **트렌드 → 갭 → 연구 제안** 보고서를 자동 생성합니다.

## 구조

- **Layer 1: Collector** (Python CLI / cron) — 매일 arXiv·HF·OpenReview·S2에서 메타데이터 수집, 30일 rolling DB 유지.
- **Layer 2: topic-finder skill** (Claude Code) — 사용자 키워드 → 4봇 회의 (Trend → Gap → Skeptic → Proposer) → Markdown 보고서.

자세한 설계: [docs/specs/2026-04-26-paper-suggestion-design.md](docs/specs/2026-04-26-paper-suggestion-design.md)

## 설치

```bash
git clone <repo>
cd paper_suggestion
python -m venv .venv && source .venv/bin/activate
pip install -r collector/requirements.txt pytest
pytest                              # all unit tests should pass
```

## Layer 1 사용 — 메타DB 수집

```bash
# 오늘 데이터 수집 (수동 실행)
python -m collector.main

# 특정 날짜
python -m collector.main --date 2026-04-20

# 일부 소스 스킵 (디버깅용)
python -m collector.main --skip-arxiv
```

산출물:
- `metadb/daily/YYYY-MM-DD.md` — 일별 사람용 다이제스트
- `metadb/rolling.jsonl` — 30일 인덱스 (Layer 2 입력)
- `metadb/stats.json` — 마지막 실행 통계

자동 실행은 `.github/workflows/daily_collect.yml`이 매일 06:00 UTC에 처리합니다.

## Layer 2 사용 — 연구 주제 보고서 생성

Claude Code 내에서:

```
/find-topic "LLM jailbreak defense"
/find-topic "diffusion alignment" --clusters 7 --proposals 3
/find-topic "embodied agent benchmark" --dry-run
```

산출물:
- `reports/YYYY-MM-DD-<topic-slug>.md` — 트렌드·갭·제안 보고서
- `reports/.cache/<run-id>/` — 4봇 중간산물 JSON (디버깅·재실행용)

옵션:

| Arg | Default | 설명 |
|---|---|---|
| `--top N` | 10 | 클러스터당 대표 논문 |
| `--clusters K` | 5 | 클러스터 개수 |
| `--proposals P` | 5 | 제안 개수 |
| `--window D` | 30 | rolling window |
| `--expand-only` | off | 키워드 확장만 |
| `--dry-run` | off | 매칭/토큰 추정만 |

## 환경변수

| Var | 필수? | 용도 |
|---|---|---|
| `SEMANTIC_SCHOLAR_API_KEY` | 옵션 | S2 rate limit 완화 |

## 개발

```bash
pytest                       # unit tests
pytest -m integration        # 네트워크 호출 (slow)
```

## 라이선스 / 의존성

- Python 3.11+
- `requests`, `python-dateutil`, `pytest`
- `paper_find` 의 4 스크레이퍼를 fork (filter 제거)
- Layer 2는 Claude Sonnet 4.6 사용 (호출당 ~600원)
