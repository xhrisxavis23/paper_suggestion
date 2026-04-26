# paper_suggestion v0.1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a research-topic discovery bot in two layers: (1) Python CLI / cron data collector that maintains a rolling 30-day metadata DB, (2) Claude Code skill running a 4-bot pipeline (Trend-Analyzer → Gap-Hunter → Skeptic → Proposer) that turns a user keyword into a Markdown report containing trends, gaps, and concrete research proposals.

**Architecture:** Layer 1 forks paper_find's 4 scrapers and removes topic filtering, writing per-day `.md` digests + a `rolling.jsonl` index. Layer 2 is a Claude Code skill that loads the index, runs LLM keyword expansion, performs deterministic substring matching, then orchestrates 4 LLM calls (Sonnet 4.6) using prompt files in `prompts/`, finally assembling a Markdown report. paper_search PDF integration is deferred to v0.2.

**Tech Stack:** Python 3.11+, `requests`, `python-dateutil`, `pytest`, Claude Code skill format, GitHub Actions for cron, Sonnet 4.6 for LLM calls.

**Spec:** `docs/specs/2026-04-26-paper-suggestion-design.md`

**Source repos to reference:**
- `/home/dgu/sh/paper_find/` — fork source for Layer 1 scrapers
- `/home/dgu/sh/paper_search/` — pattern reference for Layer 2 skill structure (SKILL.md format)

---

## File Structure

```
paper_suggestion/
├── README.md                                  # User-facing usage doc (Task 21)
├── .gitignore                                 # Task 1
├── pytest.ini                                 # Task 1
│
├── docs/
│   ├── specs/2026-04-26-paper-suggestion-design.md   # exists
│   └── plans/2026-04-26-paper-suggestion-plan.md     # this file
│
├── collector/                                 # Layer 1
│   ├── main.py                                # Task 10
│   ├── requirements.txt                       # Task 1
│   └── src/
│       ├── __init__.py                        # Task 1
│       ├── config.py                          # Task 5
│       ├── models.py                          # Task 2
│       ├── db.py                              # Task 3
│       ├── formatter.py                       # Task 4
│       └── scrapers/
│           ├── __init__.py                    # Task 1
│           ├── arxiv.py                       # Task 6
│           ├── huggingface.py                 # Task 7
│           ├── openreview.py                  # Task 8
│           └── semantic_scholar.py            # Task 9
│
├── skills/topic-finder/                       # Layer 2
│   ├── SKILL.md                               # Task 20
│   ├── prompts/
│   │   ├── expand_keywords.md                 # Task 15
│   │   ├── trend_analyzer.md                  # Task 16
│   │   ├── gap_hunter.md                      # Task 17
│   │   ├── skeptic.md                         # Task 18
│   │   └── proposer.md                        # Task 19
│   └── scripts/
│       ├── __init__.py                        # Task 12
│       ├── load_metadb.py                     # Task 12
│       ├── match_substring.py                 # Task 13
│       └── build_report.py                    # Task 14
│
├── tests/
│   ├── __init__.py                            # Task 1
│   ├── test_models.py                         # Task 2
│   ├── test_db.py                             # Task 3
│   ├── test_formatter.py                      # Task 4
│   ├── test_load_metadb.py                    # Task 12
│   ├── test_match_substring.py                # Task 13
│   └── test_build_report.py                   # Task 14
│
├── metadb/                                    # gitignored, generated
└── reports/                                   # gitignored, generated
└── .github/workflows/daily_collect.yml        # Task 11
```

---

## Phase 0 — Bootstrap

### Task 1: Repository skeleton

**Files:**
- Create: `.gitignore`
- Create: `pytest.ini`
- Create: `collector/requirements.txt`
- Create: `tests/__init__.py`
- Create: `collector/src/__init__.py`
- Create: `collector/src/scrapers/__init__.py`
- Create: `README.md` (stub)

- [ ] **Step 1: Create `.gitignore`**

```
__pycache__/
*.pyc
.pytest_cache/
.venv/
venv/

# Generated data — do not commit
metadb/
reports/
!reports/.gitkeep

.DS_Store
.idea/
.vscode/
```

- [ ] **Step 2: Create `pytest.ini`**

```ini
[pytest]
testpaths = tests
pythonpath = .
markers =
    integration: real network calls, skipped by default
addopts = -m "not integration"
```

- [ ] **Step 3: Create `collector/requirements.txt`**

```
requests>=2.31.0
python-dateutil>=2.8.2
```

- [ ] **Step 4: Create empty `__init__.py` files**

```bash
touch tests/__init__.py
touch collector/src/__init__.py
touch collector/src/scrapers/__init__.py
```

- [ ] **Step 5: Create `README.md` stub**

```markdown
# paper_suggestion

연구 주제 발굴 봇 — 사용자 키워드를 받아 최근 1개월 학계 논문 메타데이터를 분석해 트렌드·갭·연구 제안 보고서를 생성한다.

자세한 사용법은 [docs/specs/](docs/specs/) 참고. README는 v0.1 완료 시 채움 (Task 21).
```

- [ ] **Step 6: Verify pytest discovers tests**

Run: `pip install pytest && pytest --collect-only`  
Expected: `0 tests collected` (no test files yet, but no errors).

- [ ] **Step 7: Commit**

```bash
git add .gitignore pytest.ini collector/requirements.txt collector/src/__init__.py collector/src/scrapers/__init__.py tests/__init__.py README.md
git commit -m "chore: scaffold paper_suggestion repo skeleton"
```

---

### Task 2: Paper data model

**Files:**
- Create: `collector/src/models.py`
- Test: `tests/test_models.py`

**Background:** Paper struct mirrors `paper_find/src/models.py` but adds two fields needed by Layer 2 substring matching: `published_date` (already present) and `categories` (arXiv `cs.*` etc.).

- [ ] **Step 1: Write the failing test**

`tests/test_models.py`:
```python
from datetime import date
from collector.src.models import Paper


def test_paper_get_id_uses_arxiv_id_when_present():
    p = Paper(title="X", arxiv_id="2404.12345v2")
    assert p.get_id() == "arxiv:2404.12345"


def test_paper_get_id_falls_back_to_normalized_title():
    p = Paper(title="  Foo   Bar  ")
    assert p.get_id() == "title:foo bar"


def test_paper_to_jsonl_dict_roundtrip():
    p = Paper(
        title="Sample",
        abstract="abs",
        authors=["Alice", "Bob"],
        url="http://x",
        arxiv_id="2404.0001",
        venue="arXiv",
        published_date=date(2026, 4, 26),
        source="arxiv",
        categories=["cs.LG", "cs.AI"],
    )
    d = p.to_jsonl_dict()
    assert d["id"] == "arxiv:2404.0001"
    assert d["date"] == "2026-04-26"
    assert d["categories"] == ["cs.LG", "cs.AI"]


def test_paper_from_jsonl_dict_roundtrip():
    p1 = Paper(
        title="Sample",
        abstract="abs",
        authors=["Alice"],
        arxiv_id="2404.0001",
        published_date=date(2026, 4, 26),
        source="arxiv",
    )
    d = p1.to_jsonl_dict()
    p2 = Paper.from_jsonl_dict(d)
    assert p2.title == p1.title
    assert p2.arxiv_id == p1.arxiv_id
    assert p2.published_date == p1.published_date
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_models.py -v`  
Expected: FAIL — `ModuleNotFoundError: No module named 'collector.src.models'`

- [ ] **Step 3: Implement `collector/src/models.py`**

```python
"""Paper data model + JSONL serialization."""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import date
from typing import List, Optional


@dataclass
class Paper:
    title: str
    abstract: str = ""
    authors: List[str] = field(default_factory=list)
    url: str = ""
    pdf_url: str = ""
    arxiv_id: Optional[str] = None
    venue: Optional[str] = None  # "arXiv", "NeurIPS", "ICLR", ...
    year: Optional[int] = None
    source: str = ""              # "arxiv" | "hf" | "openreview" | "s2"
    published_date: Optional[date] = None
    categories: List[str] = field(default_factory=list)

    def get_id(self) -> str:
        if self.arxiv_id:
            base = self.arxiv_id.split("v")[0]
            return f"arxiv:{base}"
        normalized = " ".join(self.title.lower().split())
        return f"title:{normalized}"

    def to_jsonl_dict(self) -> dict:
        d = asdict(self)
        d["id"] = self.get_id()
        d["date"] = self.published_date.isoformat() if self.published_date else None
        d.pop("published_date")
        return d

    @classmethod
    def from_jsonl_dict(cls, d: dict) -> "Paper":
        date_str = d.get("date")
        published = date.fromisoformat(date_str) if date_str else None
        return cls(
            title=d["title"],
            abstract=d.get("abstract", ""),
            authors=list(d.get("authors", [])),
            url=d.get("url", ""),
            pdf_url=d.get("pdf_url", ""),
            arxiv_id=d.get("arxiv_id"),
            venue=d.get("venue"),
            year=d.get("year"),
            source=d.get("source", ""),
            published_date=published,
            categories=list(d.get("categories", [])),
        )
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_models.py -v`  
Expected: 4 passed.

- [ ] **Step 5: Commit**

```bash
git add collector/src/models.py tests/test_models.py
git commit -m "feat(collector): add Paper dataclass with JSONL serialization"
```

---

## Phase 1 — Layer 1 Data Layer

### Task 3: `metadb/rolling.jsonl` read/write/prune

**Files:**
- Create: `collector/src/db.py`
- Test: `tests/test_db.py`

**Background:** `db.py` is the only writer to `metadb/rolling.jsonl`. It supports: append (with dedup by `id`), load all, prune (drop entries older than N days). Each line is a JSONL record produced by `Paper.to_jsonl_dict()`.

- [ ] **Step 1: Write the failing test**

`tests/test_db.py`:
```python
from datetime import date, timedelta
from pathlib import Path

import pytest

from collector.src.models import Paper
from collector.src.db import RollingDB


def make_paper(arxiv_id: str, d: date) -> Paper:
    return Paper(
        title=f"Title {arxiv_id}",
        abstract="abs",
        authors=["Alice"],
        arxiv_id=arxiv_id,
        published_date=d,
        source="arxiv",
    )


def test_append_then_load(tmp_path: Path):
    db = RollingDB(tmp_path / "rolling.jsonl")
    p1 = make_paper("2404.0001", date(2026, 4, 26))
    p2 = make_paper("2404.0002", date(2026, 4, 25))

    added = db.append([p1, p2])
    assert added == 2

    loaded = db.load_all()
    ids = {p.get_id() for p in loaded}
    assert ids == {"arxiv:2404.0001", "arxiv:2404.0002"}


def test_append_dedupes_by_id(tmp_path: Path):
    db = RollingDB(tmp_path / "rolling.jsonl")
    p = make_paper("2404.0001", date(2026, 4, 26))

    assert db.append([p]) == 1
    assert db.append([p]) == 0  # second time: no new entries

    loaded = db.load_all()
    assert len(loaded) == 1


def test_prune_drops_old_entries(tmp_path: Path):
    db = RollingDB(tmp_path / "rolling.jsonl")
    today = date(2026, 4, 26)
    fresh = make_paper("2404.0001", today - timedelta(days=10))
    stale = make_paper("2403.0001", today - timedelta(days=40))

    db.append([fresh, stale])
    pruned = db.prune(today=today, window_days=30)

    assert pruned == 1
    remaining_ids = {p.get_id() for p in db.load_all()}
    assert remaining_ids == {"arxiv:2404.0001"}


def test_load_all_on_missing_file_returns_empty(tmp_path: Path):
    db = RollingDB(tmp_path / "nope.jsonl")
    assert db.load_all() == []
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_db.py -v`  
Expected: FAIL — `ModuleNotFoundError: No module named 'collector.src.db'`

- [ ] **Step 3: Implement `collector/src/db.py`**

```python
"""Rolling JSONL metadata database."""
from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path
from typing import Iterable, List

from .models import Paper


class RollingDB:
    """Append-only JSONL DB with id-based dedup + date-based prune."""

    def __init__(self, path: Path):
        self.path = Path(path)

    def load_all(self) -> List[Paper]:
        if not self.path.exists():
            return []
        out: List[Paper] = []
        with self.path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                out.append(Paper.from_jsonl_dict(json.loads(line)))
        return out

    def append(self, papers: Iterable[Paper]) -> int:
        existing_ids = {p.get_id() for p in self.load_all()}
        new_papers = [p for p in papers if p.get_id() not in existing_ids]
        if not new_papers:
            return 0
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as f:
            for p in new_papers:
                f.write(json.dumps(p.to_jsonl_dict(), ensure_ascii=False) + "\n")
        return len(new_papers)

    def prune(self, today: date, window_days: int = 30) -> int:
        cutoff = today - timedelta(days=window_days)
        all_papers = self.load_all()
        kept = [p for p in all_papers if p.published_date and p.published_date >= cutoff]
        dropped = len(all_papers) - len(kept)
        if dropped == 0:
            return 0
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as f:
            for p in kept:
                f.write(json.dumps(p.to_jsonl_dict(), ensure_ascii=False) + "\n")
        return dropped
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_db.py -v`  
Expected: 4 passed.

- [ ] **Step 5: Commit**

```bash
git add collector/src/db.py tests/test_db.py
git commit -m "feat(collector): add RollingDB for jsonl read/write/prune"
```

---

### Task 4: Daily Markdown digest formatter

**Files:**
- Create: `collector/src/formatter.py`
- Test: `tests/test_formatter.py`

**Background:** Per-day human-readable digest at `metadb/daily/YYYY-MM-DD.md`. Groups papers by source, lists title + authors + venue + 1-line abstract excerpt + URL.

- [ ] **Step 1: Write the failing test**

`tests/test_formatter.py`:
```python
from datetime import date

from collector.src.models import Paper
from collector.src.formatter import format_daily_digest


def test_daily_digest_has_header_and_groups_by_source():
    today = date(2026, 4, 26)
    papers = [
        Paper(title="Arxiv One", authors=["A"], arxiv_id="2404.0001",
              source="arxiv", venue="arXiv", published_date=today,
              abstract="Short abstract.", url="http://arxiv.org/abs/2404.0001"),
        Paper(title="HF One", authors=["B"], source="hf", venue="HF",
              published_date=today, abstract="HF abstract.",
              url="http://hf.co/x"),
    ]
    md = format_daily_digest(papers, target_date=today)

    assert md.startswith("# Daily metadata digest — 2026-04-26")
    assert "## arxiv" in md
    assert "## hf" in md
    assert "Arxiv One" in md
    assert "HF One" in md


def test_daily_digest_handles_empty_input():
    md = format_daily_digest([], target_date=date(2026, 4, 26))
    assert "no papers collected" in md.lower()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_formatter.py -v`  
Expected: FAIL — `ModuleNotFoundError`.

- [ ] **Step 3: Implement `collector/src/formatter.py`**

```python
"""Per-day Markdown digest of newly collected metadata."""
from __future__ import annotations

from collections import defaultdict
from datetime import date
from typing import List

from .models import Paper


def format_daily_digest(papers: List[Paper], target_date: date) -> str:
    lines: List[str] = []
    lines.append(f"# Daily metadata digest — {target_date.isoformat()}")
    lines.append("")
    lines.append(f"총 수집: **{len(papers)}건**")
    lines.append("")

    if not papers:
        lines.append("_no papers collected._")
        return "\n".join(lines) + "\n"

    by_source = defaultdict(list)
    for p in papers:
        by_source[p.source or "unknown"].append(p)

    for source in sorted(by_source.keys()):
        bucket = by_source[source]
        lines.append(f"## {source}  ({len(bucket)})")
        lines.append("")
        for p in bucket:
            authors = ", ".join(p.authors[:3]) + (" et al." if len(p.authors) > 3 else "")
            venue_year = f"{p.venue or '—'}"
            if p.year:
                venue_year += f" {p.year}"
            short_abs = (p.abstract or "").strip().replace("\n", " ")
            if len(short_abs) > 200:
                short_abs = short_abs[:200] + "…"
            link = p.url or p.pdf_url or ""
            lines.append(f"- **[{p.title}]({link})** — {authors}")
            lines.append(f"  - {venue_year}")
            if short_abs:
                lines.append(f"  - {short_abs}")
        lines.append("")

    return "\n".join(lines) + "\n"
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_formatter.py -v`  
Expected: 2 passed.

- [ ] **Step 5: Commit**

```bash
git add collector/src/formatter.py tests/test_formatter.py
git commit -m "feat(collector): add daily Markdown digest formatter"
```

---

## Phase 2 — Layer 1 Scrapers (forked from paper_find, filter removed)

### Task 5: Collector config

**Files:**
- Create: `collector/src/config.py`

**Background:** Config holds arXiv categories, S2 venue list, S2 venue alias dictionary (for venue normalization). All topic keywords are removed (this is the key difference vs paper_find).

- [ ] **Step 1: Implement `collector/src/config.py`**

```python
"""Collector configuration: categories, venues, no topic filter."""
from __future__ import annotations

# arXiv categories to collect (no topic filter)
ARXIV_CATEGORIES = [
    "cs.AI",
    "cs.LG",
    "cs.CL",
    "cs.CV",
    "cs.RO",
    "stat.ML",
]

# How many days of arXiv submissions to query each run
ARXIV_LOOKBACK_DAYS = 1

# Max arXiv results per category per run (API hard cap is 2000; safety buffer)
ARXIV_MAX_RESULTS_PER_CATEGORY = 500

# Conferences to query via Semantic Scholar (last 30 days of published papers)
S2_VENUES = ["AAAI", "NeurIPS", "ICML", "ICLR", "CVPR", "KDD"]

# OpenReview venue ids (active venues)
OPENREVIEW_VENUE_IDS = [
    "ICLR.cc/2026/Conference",
    # Add NeurIPS / ICML when active
]

# HuggingFace daily papers fallback window
HF_FALLBACK_DAYS = 3

# User-Agent for requests
USER_AGENT = "paper-suggestion-bot/0.1"

# Rolling window in days
ROLLING_WINDOW_DAYS = 30

# Default paths (relative to repo root)
METADB_DIR = "metadb"
ROLLING_JSONL = "metadb/rolling.jsonl"
DAILY_DIR = "metadb/daily"
STATS_JSON = "metadb/stats.json"
```

- [ ] **Step 2: Verify file imports cleanly**

Run: `python -c "from collector.src import config; print(config.ARXIV_CATEGORIES)"`  
Expected: `['cs.AI', 'cs.LG', 'cs.CL', 'cs.CV', 'cs.RO', 'stat.ML']`

- [ ] **Step 3: Commit**

```bash
git add collector/src/config.py
git commit -m "feat(collector): add config (arXiv categories, S2 venues, paths)"
```

---

### Task 6: arXiv scraper (filter-free)

**Files:**
- Create: `collector/src/scrapers/arxiv.py`
- Test: `tests/test_scrapers.py` (one test, integration-marked)

**Background:** Unlike paper_find which constructs queries with topic-keyword × category combinations, paper_suggestion queries each category once per run with no keyword filter. Result count per category ~50-200/day for cs.LG. Reference paper_find's `_arxiv_date_range` weekend logic for the date window.

- [ ] **Step 1: Reference original**

Read `/home/dgu/sh/paper_find/src/scrapers/arxiv.py` for the API call structure (`requests.get` to `http://export.arxiv.org/api/query`, Atom XML parsing, `_arxiv_date_range` weekend logic).

- [ ] **Step 2: Implement `collector/src/scrapers/arxiv.py`**

```python
"""arXiv scraper — collect ALL papers in configured categories (no topic filter).

Differs from paper_find: no TOPIC_SEARCH_TERMS — query is just per-category
within a date range. Returns every paper arXiv reports for that window.
"""
from __future__ import annotations

import logging
import time
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta, timezone
from typing import List, Tuple

import requests

from ..config import (
    ARXIV_CATEGORIES,
    ARXIV_LOOKBACK_DAYS,
    ARXIV_MAX_RESULTS_PER_CATEGORY,
    USER_AGENT,
)
from ..models import Paper

logger = logging.getLogger(__name__)

ARXIV_API = "http://export.arxiv.org/api/query"
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}
ARXIV_DELAY = 3.0  # API recommends 3-second pacing


def _date_window(target: date, lookback: int) -> Tuple[date, date]:
    """Date window with weekend rollback (arXiv has no Sat/Sun submissions)."""
    weekday = target.weekday()  # 0=Mon ... 6=Sun
    if weekday == 0:                                        # Monday
        return target - timedelta(days=lookback + 2), target
    if weekday in (5, 6):                                   # Sat/Sun
        return target - timedelta(days=lookback + (weekday - 4)), target
    return target - timedelta(days=lookback), target


def _result_to_paper(entry: ET.Element, category: str) -> Paper:
    title = (entry.findtext("atom:title", "", NS) or "").strip()
    abstract = (entry.findtext("atom:summary", "", NS) or "").strip()
    authors = [
        (a.findtext("atom:name", "", NS) or "").strip()
        for a in entry.findall("atom:author", NS)
    ]
    arxiv_url = (entry.findtext("atom:id", "", NS) or "").strip()
    arxiv_id = arxiv_url.rsplit("/", 1)[-1] if arxiv_url else None

    published = entry.findtext("atom:published", "", NS) or ""
    try:
        pub_dt = datetime.fromisoformat(published.replace("Z", "+00:00"))
        pub_date = pub_dt.astimezone(timezone.utc).date()
        year = pub_dt.year
    except Exception:
        pub_date, year = None, None

    pdf_url = ""
    for link in entry.findall("atom:link", NS):
        if link.attrib.get("title") == "pdf":
            pdf_url = link.attrib.get("href", "")
            break

    cats = []
    for c in entry.findall("atom:category", NS):
        term = c.attrib.get("term")
        if term and term.startswith(("cs.", "stat.", "math.", "q-")):
            cats.append(term)
    if category not in cats:
        cats.insert(0, category)

    return Paper(
        title=title,
        abstract=abstract,
        authors=authors,
        url=arxiv_url,
        pdf_url=pdf_url,
        arxiv_id=arxiv_id,
        venue="arXiv",
        year=year,
        source="arxiv",
        published_date=pub_date,
        categories=cats,
    )


class ArxivScraper:
    def __init__(self, session: requests.Session | None = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})

    def fetch(self, target_date: date) -> List[Paper]:
        start, end = _date_window(target_date, ARXIV_LOOKBACK_DAYS)
        out: List[Paper] = []
        for cat in ARXIV_CATEGORIES:
            try:
                out.extend(self._fetch_category(cat, start, end))
            except Exception as e:
                logger.warning("arXiv category %s failed: %s", cat, e)
            time.sleep(ARXIV_DELAY)
        logger.info("arXiv: %d papers across %d categories",
                    len(out), len(ARXIV_CATEGORIES))
        return out

    def _fetch_category(self, category: str, start: date, end: date) -> List[Paper]:
        start_str = start.strftime("%Y%m%d") + "0000"
        end_str = end.strftime("%Y%m%d") + "2359"
        query = (
            f"cat:{category} "
            f"AND submittedDate:[{start_str} TO {end_str}]"
        )
        params = {
            "search_query": query,
            "max_results": ARXIV_MAX_RESULTS_PER_CATEGORY,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        r = self.session.get(ARXIV_API, params=params, timeout=30)
        r.raise_for_status()
        root = ET.fromstring(r.content)
        return [_result_to_paper(e, category) for e in root.findall("atom:entry", NS)]
```

- [ ] **Step 3: Add a smoke integration test**

`tests/test_scrapers.py`:
```python
import pytest
from datetime import date

from collector.src.scrapers.arxiv import ArxivScraper


@pytest.mark.integration
def test_arxiv_scraper_returns_papers_for_yesterday():
    """Live test — hits real arXiv API. Run with: pytest -m integration"""
    s = ArxivScraper()
    papers = s.fetch(date.today())
    assert len(papers) > 0
    sample = papers[0]
    assert sample.source == "arxiv"
    assert sample.arxiv_id
    assert sample.title
```

- [ ] **Step 4: Verify unit tests still pass and integration test discovered**

Run: `pytest -v`  
Expected: existing tests pass, integration test deselected by default.

Run (optional, manual): `pytest -m integration tests/test_scrapers.py -v`  
Expected: 1 passed (network call to arXiv).

- [ ] **Step 5: Commit**

```bash
git add collector/src/scrapers/arxiv.py tests/test_scrapers.py
git commit -m "feat(collector): arXiv scraper with no topic filter"
```

---

### Task 7: HuggingFace scraper

**Files:**
- Create: `collector/src/scrapers/huggingface.py`
- Modify: `tests/test_scrapers.py` (add integration test)

**Background:** HF has two APIs: `/api/daily_papers?date=YYYY-MM-DD` (curated, ~20-50/day) and `/api/papers?q=<query>` (search). Since we have no topic filter, only use the daily endpoint with fallback to recent days if empty.

- [ ] **Step 1: Implement `collector/src/scrapers/huggingface.py`**

```python
"""HuggingFace Daily Papers scraper — curated list only (no topic search)."""
from __future__ import annotations

import logging
from datetime import date, timedelta
from typing import List

import requests

from ..config import HF_FALLBACK_DAYS, USER_AGENT
from ..models import Paper

logger = logging.getLogger(__name__)

HF_DAILY_API = "https://huggingface.co/api/daily_papers"


class HuggingFaceScraper:
    def __init__(self, session: requests.Session | None = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})

    def fetch(self, target_date: date) -> List[Paper]:
        for offset in range(HF_FALLBACK_DAYS + 1):
            d = target_date - timedelta(days=offset)
            papers = self._fetch_one(d)
            if papers:
                logger.info("HF daily %s: %d papers", d, len(papers))
                return papers
        return []

    def _fetch_one(self, d: date) -> List[Paper]:
        try:
            r = self.session.get(
                HF_DAILY_API,
                params={"date": d.isoformat()},
                timeout=30,
            )
            r.raise_for_status()
            data = r.json()
        except Exception as e:
            logger.warning("HF daily %s failed: %s", d, e)
            return []
        return [self._parse(item, d) for item in data if "paper" in item]

    @staticmethod
    def _parse(item: dict, fallback_date: date) -> Paper:
        paper = item.get("paper", {})
        arxiv_id = paper.get("id")
        title = (paper.get("title") or "").strip()
        abstract = (paper.get("summary") or "").strip()
        authors = [a.get("name", "") for a in paper.get("authors", []) if a.get("name")]
        return Paper(
            title=title,
            abstract=abstract,
            authors=authors,
            url=f"https://huggingface.co/papers/{arxiv_id}" if arxiv_id else "",
            pdf_url=f"https://arxiv.org/pdf/{arxiv_id}.pdf" if arxiv_id else "",
            arxiv_id=arxiv_id,
            venue="HF",
            year=fallback_date.year,
            source="hf",
            published_date=fallback_date,
            categories=[],
        )
```

- [ ] **Step 2: Add integration test**

Append to `tests/test_scrapers.py`:
```python
from collector.src.scrapers.huggingface import HuggingFaceScraper


@pytest.mark.integration
def test_hf_scraper_returns_papers():
    s = HuggingFaceScraper()
    papers = s.fetch(date.today())
    assert isinstance(papers, list)
    if papers:
        assert papers[0].source == "hf"
```

- [ ] **Step 3: Verify**

Run: `pytest -v`  
Expected: existing tests pass.

- [ ] **Step 4: Commit**

```bash
git add collector/src/scrapers/huggingface.py tests/test_scrapers.py
git commit -m "feat(collector): HuggingFace daily-papers scraper (no topic search)"
```

---

### Task 8: OpenReview scraper

**Files:**
- Create: `collector/src/scrapers/openreview.py`
- Modify: `tests/test_scrapers.py`

**Background:** OpenReview has a v2 REST API. We list submissions for active venues in `OPENREVIEW_VENUE_IDS` (no topic post-filter). API is unauthenticated for public submissions.

- [ ] **Step 1: Implement `collector/src/scrapers/openreview.py`**

```python
"""OpenReview scraper — submissions for active venues, no topic filter."""
from __future__ import annotations

import logging
from datetime import date, datetime, timezone
from typing import List

import requests

from ..config import OPENREVIEW_VENUE_IDS, USER_AGENT
from ..models import Paper

logger = logging.getLogger(__name__)

OR_API = "https://api2.openreview.net/notes"


class OpenReviewScraper:
    def __init__(self, session: requests.Session | None = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})

    def fetch(self, target_date: date) -> List[Paper]:
        out: List[Paper] = []
        for venue_id in OPENREVIEW_VENUE_IDS:
            try:
                out.extend(self._fetch_venue(venue_id))
            except Exception as e:
                logger.warning("OpenReview %s failed: %s", venue_id, e)
        logger.info("OpenReview: %d papers across %d venues",
                    len(out), len(OPENREVIEW_VENUE_IDS))
        return out

    def _fetch_venue(self, venue_id: str) -> List[Paper]:
        params = {
            "content.venueid": venue_id,
            "limit": 1000,
            "details": "replyCount",
        }
        r = self.session.get(OR_API, params=params, timeout=30)
        r.raise_for_status()
        notes = r.json().get("notes", [])

        out: List[Paper] = []
        venue_short = venue_id.split("/")[0].split(".")[0]
        for n in notes:
            content = n.get("content", {})
            title = (content.get("title", {}) or {}).get("value", "").strip()
            if not title:
                continue
            abstract = (content.get("abstract", {}) or {}).get("value", "").strip()
            authors = (content.get("authors", {}) or {}).get("value", []) or []

            ts_ms = n.get("cdate") or n.get("tcdate")
            pub_date = (
                datetime.fromtimestamp(ts_ms / 1000, tz=timezone.utc).date()
                if ts_ms else None
            )

            forum_id = n.get("forum") or n.get("id")
            url = f"https://openreview.net/forum?id={forum_id}" if forum_id else ""
            pdf_url = f"https://openreview.net/pdf?id={forum_id}" if forum_id else ""

            out.append(Paper(
                title=title,
                abstract=abstract,
                authors=list(authors),
                url=url,
                pdf_url=pdf_url,
                arxiv_id=None,
                venue=venue_short,
                year=pub_date.year if pub_date else None,
                source="openreview",
                published_date=pub_date,
                categories=[],
            ))
        return out
```

- [ ] **Step 2: Add integration test**

Append to `tests/test_scrapers.py`:
```python
from collector.src.scrapers.openreview import OpenReviewScraper


@pytest.mark.integration
def test_openreview_scraper_runs_without_error():
    s = OpenReviewScraper()
    papers = s.fetch(date.today())
    assert isinstance(papers, list)
```

- [ ] **Step 3: Commit**

```bash
git add collector/src/scrapers/openreview.py tests/test_scrapers.py
git commit -m "feat(collector): OpenReview scraper (no topic filter)"
```

---

### Task 9: Semantic Scholar scraper

**Files:**
- Create: `collector/src/scrapers/semantic_scholar.py`
- Modify: `tests/test_scrapers.py`

**Background:** S2 search-by-venue endpoint returns papers published at given venue. We iterate `S2_VENUES` and take recent papers. Optional `S2_API_KEY` env for higher rate limits.

- [ ] **Step 1: Implement `collector/src/scrapers/semantic_scholar.py`**

```python
"""Semantic Scholar scraper — recent papers per configured venue."""
from __future__ import annotations

import logging
import os
import time
from datetime import date, timedelta
from typing import List

import requests

from ..config import ROLLING_WINDOW_DAYS, S2_VENUES, USER_AGENT
from ..models import Paper

logger = logging.getLogger(__name__)

S2_SEARCH = "https://api.semanticscholar.org/graph/v1/paper/search"
S2_FIELDS = "title,abstract,authors,venue,year,publicationDate,externalIds,url"
S2_DELAY = 1.0  # courtesy pacing


class SemanticScholarScraper:
    def __init__(self, session: requests.Session | None = None,
                 api_key: str | None = None):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})
        key = api_key or os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
        if key:
            self.session.headers.update({"x-api-key": key})

    def fetch(self, target_date: date) -> List[Paper]:
        out: List[Paper] = []
        cutoff = target_date - timedelta(days=ROLLING_WINDOW_DAYS)
        for venue in S2_VENUES:
            try:
                out.extend(self._fetch_venue(venue, cutoff, target_date))
            except Exception as e:
                logger.warning("S2 venue %s failed: %s", venue, e)
            time.sleep(S2_DELAY)
        logger.info("S2: %d papers across %d venues", len(out), len(S2_VENUES))
        return out

    def _fetch_venue(self, venue: str, since: date, until: date) -> List[Paper]:
        params = {
            "query": venue,
            "venue": venue,
            "publicationDateOrYear": f"{since.isoformat()}:{until.isoformat()}",
            "fields": S2_FIELDS,
            "limit": 100,
        }
        r = self.session.get(S2_SEARCH, params=params, timeout=30)
        if r.status_code == 429:
            logger.warning("S2 rate-limited at venue %s — backing off", venue)
            time.sleep(5)
            return []
        r.raise_for_status()
        data = r.json().get("data", [])

        out: List[Paper] = []
        for item in data:
            title = (item.get("title") or "").strip()
            if not title:
                continue
            abstract = (item.get("abstract") or "").strip()
            authors = [a.get("name", "") for a in item.get("authors", []) if a.get("name")]
            year = item.get("year")
            pub_str = item.get("publicationDate")
            try:
                pub_date = date.fromisoformat(pub_str) if pub_str else None
            except Exception:
                pub_date = None
            ext = item.get("externalIds") or {}
            arxiv_id = ext.get("ArXiv")
            url = item.get("url", "")
            out.append(Paper(
                title=title,
                abstract=abstract,
                authors=authors,
                url=url,
                pdf_url=f"https://arxiv.org/pdf/{arxiv_id}.pdf" if arxiv_id else "",
                arxiv_id=arxiv_id,
                venue=venue,
                year=year,
                source="s2",
                published_date=pub_date,
                categories=[],
            ))
        return out
```

- [ ] **Step 2: Add integration test**

Append to `tests/test_scrapers.py`:
```python
from collector.src.scrapers.semantic_scholar import SemanticScholarScraper


@pytest.mark.integration
def test_s2_scraper_runs_without_error():
    s = SemanticScholarScraper()
    papers = s.fetch(date.today())
    assert isinstance(papers, list)
```

- [ ] **Step 3: Commit**

```bash
git add collector/src/scrapers/semantic_scholar.py tests/test_scrapers.py
git commit -m "feat(collector): Semantic Scholar venue scraper (no topic filter)"
```

---

## Phase 3 — Layer 1 Orchestration

### Task 10: `collector/main.py` entry point

**Files:**
- Create: `collector/main.py`

**Background:** Wires scrapers + DB + formatter. CLI: `python -m collector.main [--date YYYY-MM-DD] [--skip-arxiv] [--skip-hf] [--skip-or] [--skip-s2]`. Writes daily.md, appends rolling.jsonl, prunes 30+ days, writes stats.json.

- [ ] **Step 1: Implement `collector/main.py`**

```python
"""Daily collector entry point.

Run:
    python -m collector.main                  # today's date
    python -m collector.main --date 2026-04-26
    python -m collector.main --skip-arxiv     # skip a slow source
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from datetime import date
from pathlib import Path

from .src.config import (
    DAILY_DIR,
    METADB_DIR,
    ROLLING_JSONL,
    ROLLING_WINDOW_DAYS,
    STATS_JSON,
)
from .src.db import RollingDB
from .src.formatter import format_daily_digest
from .src.scrapers.arxiv import ArxivScraper
from .src.scrapers.huggingface import HuggingFaceScraper
from .src.scrapers.openreview import OpenReviewScraper
from .src.scrapers.semantic_scholar import SemanticScholarScraper

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="paper_suggestion daily collector")
    p.add_argument("--date", default=str(date.today()))
    p.add_argument("--skip-arxiv", action="store_true")
    p.add_argument("--skip-hf", action="store_true")
    p.add_argument("--skip-or", action="store_true")
    p.add_argument("--skip-s2", action="store_true")
    p.add_argument("--root", default=".",
                   help="Repo root (paths under metadb/ are resolved here)")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    try:
        target_date = date.fromisoformat(args.date)
    except ValueError:
        logger.error("Invalid --date: %s", args.date)
        return 2

    root = Path(args.root)
    rolling_path = root / ROLLING_JSONL
    daily_dir = root / DAILY_DIR
    stats_path = root / STATS_JSON
    daily_dir.mkdir(parents=True, exist_ok=True)

    all_papers = []
    counts: dict[str, int] = {}

    if not args.skip_arxiv:
        try:
            ps = ArxivScraper().fetch(target_date)
            all_papers.extend(ps)
            counts["arxiv"] = len(ps)
        except Exception as e:
            logger.error("arXiv failed: %s", e)
            counts["arxiv"] = 0

    if not args.skip_hf:
        try:
            ps = HuggingFaceScraper().fetch(target_date)
            all_papers.extend(ps)
            counts["hf"] = len(ps)
        except Exception as e:
            logger.error("HF failed: %s", e)
            counts["hf"] = 0

    if not args.skip_or:
        try:
            ps = OpenReviewScraper().fetch(target_date)
            all_papers.extend(ps)
            counts["openreview"] = len(ps)
        except Exception as e:
            logger.error("OpenReview failed: %s", e)
            counts["openreview"] = 0

    if not args.skip_s2:
        try:
            ps = SemanticScholarScraper().fetch(target_date)
            all_papers.extend(ps)
            counts["s2"] = len(ps)
        except Exception as e:
            logger.error("S2 failed: %s", e)
            counts["s2"] = 0

    db = RollingDB(rolling_path)
    added = db.append(all_papers)
    pruned = db.prune(today=target_date, window_days=ROLLING_WINDOW_DAYS)

    digest_md = format_daily_digest(all_papers, target_date)
    daily_path = daily_dir / f"{target_date}.md"
    daily_path.write_text(digest_md, encoding="utf-8")

    total_in_db = len(db.load_all())
    stats = {
        "last_run": target_date.isoformat(),
        "fetched_per_source": counts,
        "total_fetched": len(all_papers),
        "added_to_db": added,
        "pruned": pruned,
        "total_in_rolling": total_in_db,
    }
    stats_path.parent.mkdir(parents=True, exist_ok=True)
    stats_path.write_text(json.dumps(stats, indent=2), encoding="utf-8")

    logger.info("Daily collect done: fetched=%d, added=%d, pruned=%d, in_db=%d",
                len(all_papers), added, pruned, total_in_db)
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Smoke test (no network — skip all sources)**

```bash
python -m collector.main --skip-arxiv --skip-hf --skip-or --skip-s2 --root .
```

Expected output:
```
... Daily collect done: fetched=0, added=0, pruned=0, in_db=0
```

And `metadb/stats.json`, `metadb/daily/<today>.md` files exist.

- [ ] **Step 3: Optional live smoke test (one source only)**

```bash
python -m collector.main --skip-hf --skip-or --skip-s2 --root .
```

Expected: `arXiv: <N> papers ...`, `Daily collect done: fetched=<N>, added=<N> ...` and `metadb/rolling.jsonl` has N lines.

- [ ] **Step 4: Commit**

```bash
git add collector/main.py
git commit -m "feat(collector): orchestration entry point with CLI"
```

---

### Task 11: GitHub Actions cron workflow

**Files:**
- Create: `.github/workflows/daily_collect.yml`

**Background:** Runs `python -m collector.main` at 06:00 UTC daily, then commits any DB changes. Mirrors paper_find's pattern.

- [ ] **Step 1: Implement workflow**

```yaml
name: Daily metadata collect

on:
  schedule:
    - cron: "0 6 * * *"
  workflow_dispatch: {}

permissions:
  contents: write

jobs:
  collect:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install deps
        run: |
          python -m pip install --upgrade pip
          pip install -r collector/requirements.txt

      - name: Run collector
        env:
          SEMANTIC_SCHOLAR_API_KEY: ${{ secrets.SEMANTIC_SCHOLAR_API_KEY }}
        run: |
          python -m collector.main

      - name: Commit DB changes
        run: |
          git config user.name "paper-suggestion-bot"
          git config user.email "noreply@github.com"
          git add metadb/
          if git diff --staged --quiet; then
            echo "No DB changes."
          else
            git commit -m "data: rolling DB update $(date -u +%F)"
            git push
          fi
```

- [ ] **Step 2: Commit**

```bash
git add .github/workflows/daily_collect.yml
git commit -m "ci: add daily collector cron workflow"
```

---

## Phase 4 — Layer 2 Deterministic Helpers

### Task 12: `load_metadb.py` — read rolling.jsonl

**Files:**
- Create: `skills/topic-finder/scripts/__init__.py`
- Create: `skills/topic-finder/scripts/load_metadb.py`
- Test: `tests/test_load_metadb.py`

**Background:** Layer 2 needs to load the same JSONL the collector wrote. Reuse `Paper.from_jsonl_dict`.

- [ ] **Step 1: Write the failing test**

`tests/test_load_metadb.py`:
```python
from datetime import date
from pathlib import Path

from collector.src.models import Paper
from skills.topic_finder.scripts.load_metadb import load_rolling


def test_load_rolling_returns_paper_objects(tmp_path: Path):
    p = Paper(title="Test", arxiv_id="2404.0001",
              published_date=date(2026, 4, 26), source="arxiv")
    target = tmp_path / "rolling.jsonl"
    target.write_text(__import__("json").dumps(p.to_jsonl_dict()) + "\n",
                      encoding="utf-8")

    loaded = load_rolling(target)
    assert len(loaded) == 1
    assert loaded[0].arxiv_id == "2404.0001"


def test_load_rolling_returns_empty_when_missing(tmp_path: Path):
    assert load_rolling(tmp_path / "missing.jsonl") == []
```

NOTE: the test imports `skills.topic_finder` (underscore), but the actual folder is `skills/topic-finder` (hyphen). Python imports require underscores. We work around this by adding a `skills/topic_finder` symlink **or** by putting `skills/topic-finder` directly on `sys.path` via `pytest.ini`. Use the symlink approach for simplicity.

- [ ] **Step 2: Create symlink and `__init__.py`**

```bash
mkdir -p skills
ln -s topic-finder skills/topic_finder
mkdir -p skills/topic-finder/scripts
touch skills/topic-finder/scripts/__init__.py
touch skills/__init__.py
```

- [ ] **Step 3: Implement `skills/topic-finder/scripts/load_metadb.py`**

```python
"""Load the rolling JSONL DB written by the collector."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import List

# Make `collector.src.models` importable when this script runs from the skill dir.
_REPO_ROOT = Path(__file__).resolve().parents[3]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from collector.src.models import Paper


def load_rolling(path: Path) -> List[Paper]:
    path = Path(path)
    if not path.exists():
        return []
    out: List[Paper] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            out.append(Paper.from_jsonl_dict(json.loads(line)))
    return out


if __name__ == "__main__":
    # CLI: dump count for debugging
    p = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("metadb/rolling.jsonl")
    papers = load_rolling(p)
    print(f"{len(papers)} papers in {p}")
```

- [ ] **Step 4: Run test**

Run: `pytest tests/test_load_metadb.py -v`  
Expected: 2 passed.

- [ ] **Step 5: Commit**

```bash
git add skills/__init__.py skills/topic-finder/ skills/topic_finder tests/test_load_metadb.py
git commit -m "feat(skill): add load_metadb helper for Layer 2"
```

---

### Task 13: `match_substring.py` — keyword matching

**Files:**
- Create: `skills/topic-finder/scripts/match_substring.py`
- Test: `tests/test_match_substring.py`

**Background:** Given expanded keywords list and Paper list, return papers whose title or abstract contains any keyword (case-insensitive). Quote-respecting via `str.lower() in haystack.lower()`. Returns matches in original order, deduplicated by paper id.

- [ ] **Step 1: Write the failing test**

`tests/test_match_substring.py`:
```python
from datetime import date

from collector.src.models import Paper
from skills.topic_finder.scripts.match_substring import match_substring


def make(title: str, abstract: str = "", arxiv_id: str = "x") -> Paper:
    return Paper(title=title, abstract=abstract, arxiv_id=arxiv_id,
                 published_date=date(2026, 4, 26), source="arxiv")


def test_match_substring_matches_title():
    papers = [make("LLM jailbreak attacks", arxiv_id="1"),
              make("Image classification", arxiv_id="2")]
    matched = match_substring(papers, ["jailbreak"])
    assert len(matched) == 1
    assert matched[0].arxiv_id == "1"


def test_match_substring_matches_abstract():
    papers = [make("Foo", abstract="adversarial prompt injection", arxiv_id="1")]
    matched = match_substring(papers, ["prompt injection"])
    assert len(matched) == 1


def test_match_substring_case_insensitive():
    papers = [make("LLM Safety", arxiv_id="1")]
    matched = match_substring(papers, ["llm safety"])
    assert len(matched) == 1


def test_match_substring_dedupes_papers():
    p = make("Multi-Agent Coordination", arxiv_id="1")
    matched = match_substring([p], ["multi-agent", "coordination"])
    assert len(matched) == 1


def test_match_substring_returns_empty_when_no_match():
    papers = [make("Foo", arxiv_id="1")]
    assert match_substring(papers, ["bar"]) == []
```

- [ ] **Step 2: Implement**

`skills/topic-finder/scripts/match_substring.py`:
```python
"""Substring matching of expanded keywords against paper title+abstract."""
from __future__ import annotations

from typing import Iterable, List

from collector.src.models import Paper


def match_substring(papers: Iterable[Paper], keywords: List[str]) -> List[Paper]:
    """Return papers where ANY keyword (lowercased) is a substring
    of (title + " " + abstract) lowercased. Order preserved, deduplicated by id."""
    if not keywords:
        return []
    lowered = [k.lower() for k in keywords if k.strip()]
    seen: set[str] = set()
    out: List[Paper] = []
    for p in papers:
        key = p.get_id()
        if key in seen:
            continue
        haystack = f"{p.title} {p.abstract}".lower()
        if any(k in haystack for k in lowered):
            seen.add(key)
            out.append(p)
    return out
```

- [ ] **Step 3: Run test**

Run: `pytest tests/test_match_substring.py -v`  
Expected: 5 passed.

- [ ] **Step 4: Commit**

```bash
git add skills/topic-finder/scripts/match_substring.py tests/test_match_substring.py
git commit -m "feat(skill): add substring keyword matcher"
```

---

### Task 14: `build_report.py` — JSON → Markdown

**Files:**
- Create: `skills/topic-finder/scripts/build_report.py`
- Test: `tests/test_build_report.py`

**Background:** Takes the 4 JSON outputs (clusters / gaps / gaps_validated / proposals) plus matched papers list and assembles the final Markdown report described in spec §7.

- [ ] **Step 1: Write the failing test**

`tests/test_build_report.py`:
```python
from datetime import date

from collector.src.models import Paper
from skills.topic_finder.scripts.build_report import build_report


def make_paper(arxiv_id: str, title: str = "T") -> Paper:
    return Paper(title=title, arxiv_id=arxiv_id,
                 published_date=date(2026, 4, 26), source="arxiv",
                 url=f"http://arxiv.org/abs/{arxiv_id}",
                 venue="arXiv", authors=["A"], year=2026)


def test_build_report_has_all_sections():
    matched = [make_paper("2404.0001"), make_paper("2404.0002")]
    clusters = [{"name": "cluster1", "description": "d", "paper_ids": ["arxiv:2404.0001"],
                 "weekly_count": [1, 2], "top3": ["arxiv:2404.0001"]}]
    gaps_validated = {
        "passed": [{"id": "A", "type": "between-clusters",
                    "description": "g desc", "evidence_papers": ["arxiv:2404.0001"],
                    "skeptic_note": "ok"}],
        "rejected": [{"id": "X", "description": "rejected", "reason": "covered"}],
    }
    proposals = [{"id": 1, "name": "PROPOSAL-A", "fills_gap": "A",
                  "hypothesis": "h", "approach": "a",
                  "baselines": "b", "expected_contribution": "ec",
                  "references": ["arxiv:2404.0001"]}]

    md = build_report(
        topic="LLM safety",
        expanded=["llm safety", "alignment"],
        matched=matched,
        clusters=clusters,
        gaps_validated=gaps_validated,
        proposals=proposals,
        run_meta={"model": "claude-sonnet-4-6", "tokens_in": 100, "tokens_out": 20},
        window=(date(2026, 3, 27), date(2026, 4, 26)),
    )

    assert md.startswith("# Research Topic Suggestion — \"LLM safety\"")
    assert "## 1. 트렌드 요약" in md
    assert "## 2. 갭 분석" in md
    assert "## 3. 연구 제안" in md
    assert "## 4. 참고문헌" in md
    assert "PROPOSAL-A" in md
    assert "<details>" in md  # rejected gaps fold
```

- [ ] **Step 2: Implement**

`skills/topic-finder/scripts/build_report.py`:
```python
"""Assemble the final Markdown report from 4-bot JSON outputs."""
from __future__ import annotations

from datetime import date, datetime, timezone
from typing import Dict, List, Tuple

from collector.src.models import Paper


def build_report(
    *,
    topic: str,
    expanded: List[str],
    matched: List[Paper],
    clusters: List[dict],
    gaps_validated: Dict[str, List[dict]],
    proposals: List[dict],
    run_meta: dict,
    window: Tuple[date, date],
) -> str:
    by_id = {p.get_id(): p for p in matched}
    out: List[str] = []
    out.append(f'# Research Topic Suggestion — "{topic}"')
    out.append("")
    out.append(f"생성: {datetime.now(timezone.utc).isoformat()}")
    out.append(f"DB 윈도우: {window[0].isoformat()} ~ {window[1].isoformat()} (30d)")
    out.append(f"모델: {run_meta.get('model', 'claude-sonnet-4-6')}")
    out.append(f"매칭 논문: {len(matched)}건")
    out.append(f"확장 키워드: {expanded}")
    out.append("")
    out.append("---")
    out.append("")

    # Section 1 — Trends
    out.append("## 1. 트렌드 요약 (Trend-Analyzer)")
    out.append("")
    for i, c in enumerate(clusters, 1):
        out.append(f"### 클러스터 {i} — {c.get('name', '')}")
        out.append(f"- **설명**: {c.get('description', '')}")
        cnt = c.get("weekly_count", [])
        out.append(f"- **빈도**: {sum(cnt) if cnt else len(c.get('paper_ids', []))}건")
        if cnt:
            out.append(f"- **주차별**: {' → '.join(str(x) for x in cnt)}")
        top3 = c.get("top3", [])[:3]
        if top3:
            out.append("- **대표 논문**:")
            for pid in top3:
                p = by_id.get(pid)
                if p:
                    out.append(f"  - [{_short_id(pid)}] {p.title} — {_authors(p)}, {p.venue or '—'} {p.year or ''}")
        out.append("")

    # Section 2 — Gaps
    out.append("## 2. 갭 분석 (Gap-Hunter → Skeptic 검증)")
    out.append("")
    passed = gaps_validated.get("passed", [])
    rejected = gaps_validated.get("rejected", [])
    for g in passed:
        out.append(f"### Gap {g.get('id')} — {g.get('description', '').splitlines()[0][:80]}")
        out.append(f"- **타입**: {g.get('type', '')}")
        out.append(f"- **설명**: {g.get('description', '')}")
        ev = g.get("evidence_papers", [])
        if ev:
            out.append(f"- **근거 논문**: {', '.join(_short_id(x) for x in ev)}")
        out.append(f"- **Skeptic 검토**: ✓ 통과 — {g.get('skeptic_note', '')}")
        out.append("")
    if rejected:
        out.append("<details>")
        out.append("<summary>검토 후 제외된 갭 (참고용)</summary>")
        out.append("")
        for g in rejected:
            out.append(f"- **Gap {g.get('id')}** — {g.get('description', '')} · 거부 사유: {g.get('reason', '')}")
        out.append("")
        out.append("</details>")
        out.append("")

    # Section 3 — Proposals
    out.append("## 3. 연구 제안 (Proposer)")
    out.append("")
    for prop in proposals:
        out.append(f"### 제안 {prop.get('id')} — {prop.get('name', '')}")
        out.append(f"**가설**: {prop.get('hypothesis', '')}")
        out.append(f"**메우는 갭**: {prop.get('fills_gap', '')}")
        out.append(f"**접근**: {prop.get('approach', '')}")
        out.append(f"**Baselines**: {prop.get('baselines', '')}")
        out.append(f"**예상 기여**: {prop.get('expected_contribution', '')}")
        refs = prop.get("references", [])
        if refs:
            out.append(f"**참고**: {', '.join(_short_id(x) for x in refs)}")
        out.append("")

    # Section 4 — References
    out.append("## 4. 참고문헌 (메타DB 기반)")
    out.append("")
    for p in matched:
        sid = _short_id(p.get_id())
        out.append(f"[{sid}] {p.title}, {_authors(p)}, {p.venue or '—'} {p.year or ''} · {p.url}")
    out.append("")

    # Meta
    out.append("---")
    out.append("")
    out.append("## 메타 / 디버그")
    for k, v in run_meta.items():
        out.append(f"- {k}: {v}")
    out.append("")
    return "\n".join(out)


def _short_id(pid: str) -> str:
    """arxiv:2404.0001 → P-2404.0001 (just for display)."""
    if pid.startswith("arxiv:"):
        return f"P-{pid[6:]}"
    return f"P-{pid[:20]}"


def _authors(p: Paper) -> str:
    if not p.authors:
        return "—"
    if len(p.authors) <= 3:
        return ", ".join(p.authors)
    return f"{', '.join(p.authors[:3])} et al."
```

- [ ] **Step 3: Run test**

Run: `pytest tests/test_build_report.py -v`  
Expected: 1 passed.

- [ ] **Step 4: Commit**

```bash
git add skills/topic-finder/scripts/build_report.py tests/test_build_report.py
git commit -m "feat(skill): add JSON→Markdown report builder"
```

---

## Phase 5 — Layer 2 Prompts

### Task 15: `expand_keywords.md`

**Files:**
- Create: `skills/topic-finder/prompts/expand_keywords.md`

- [ ] **Step 1: Write prompt**

```markdown
# Expand Keywords

당신은 학술 논문 검색을 돕는 도우미입니다. 사용자가 준 토픽 키워드 하나에 대해, **메타데이터(제목·초록) substring 매칭에 쓸 수 있는 동의어·관련어·약어 5~12개**를 영문으로 출력하세요.

## 입력
- 사용자 토픽: `{TOPIC}`

## 출력 규칙
- **JSON 배열**만 출력 (다른 설명·머리말 금지)
- 각 항목은 **2~5단어 영문구**
- 다음을 포함:
  - 사용자 토픽 자체 (정규화된 형태)
  - 흔한 동의어 (예: "jailbreak" ↔ "adversarial prompt")
  - 흔한 약어와 풀 네임 둘 다 (예: "LLM", "large language model")
  - 인접 개념 (예: "guardrail bypass" 같은 사용 맥락)
- **너무 일반적인 단어 금지** — "AI", "model", "method" 같은 단독어
- **사용자 토픽이 매우 광범위하면** 6개 이내, 좁으면 12개까지

## 출력 예시
```json
["llm jailbreak", "adversarial prompt", "prompt injection", "red-team prompt", "harmful generation", "guardrail bypass", "safety alignment evasion", "jailbreak defense"]
```
```

- [ ] **Step 2: Commit**

```bash
git add skills/topic-finder/prompts/expand_keywords.md
git commit -m "feat(skill): add expand_keywords prompt"
```

---

### Task 16: `trend_analyzer.md`

**Files:**
- Create: `skills/topic-finder/prompts/trend_analyzer.md`

- [ ] **Step 1: Write prompt**

```markdown
# Trend-Analyzer

당신은 학계 논문 메타데이터를 보고 **트렌드 클러스터**를 도출하는 분석가입니다.

## 입력
- 사용자 토픽: `{TOPIC}`
- 매칭 논문 메타 N건 (각 항목: id, title, abstract, venue, date)
- 목표 클러스터 수: K (기본 5)

## 작업
1. 제목·초록을 보고 논문을 **K개 클러스터**로 묶음
2. 각 클러스터는 **방법론 / 문제정의 / 도메인** 중 하나의 축으로 일관
3. 각 클러스터마다:
   - `name`: 짧은 한글 이름 (5~10자)
   - `description`: 1~2 문장 한글 설명
   - `paper_ids`: 속한 논문의 id 리스트
   - `weekly_count`: 최근 4주차의 빈도 (오래된 → 최근 순으로 길이 4 정수 배열)
   - `top3`: 가장 대표적인 논문 id 3개 (인용 많을 것 같거나 선언적 제목)

## 출력 규칙
- **JSON 배열**만 출력 (배열 외 텍스트 금지)
- 클러스터에 속하지 않는 논문이 있어도 OK (모든 논문을 강제 분류 X)
- 클러스터끼리 같은 논문 중복 X (한 논문은 한 클러스터)

## 금기
- 추측 기반 빈도 (`weekly_count`는 입력 데이터의 date 필드만 보고 산출)
- 모든 클러스터에 같은 keyword만 반복 (`name`은 서로 달라야 함)
```

- [ ] **Step 2: Commit**

```bash
git add skills/topic-finder/prompts/trend_analyzer.md
git commit -m "feat(skill): add trend_analyzer prompt"
```

---

### Task 17: `gap_hunter.md`

**Files:**
- Create: `skills/topic-finder/prompts/gap_hunter.md`

- [ ] **Step 1: Write prompt**

```markdown
# Gap-Hunter

당신은 클러스터링된 트렌드에서 **연구 갭**을 식별하는 분석가입니다.

## 입력
- 클러스터 K개 (각 클러스터의 name, description, paper_ids, top3)
- 매칭 논문 메타 N건 (각 항목: id, title, abstract)

## 갭의 3가지 타입
- **`single-shot`** — 어떤 단발성 논문이 후속 연구로 이어지지 않은 경우. 한 클러스터 안에서 paper 1개만 동떨어져 있거나, 다른 논문들이 그 단발 논문을 인용·확장하지 않은 듯한 경우.
- **`between-clusters`** — 두 클러스터 사이의 빈 공간. 예: 클러스터 A는 "방어", 클러스터 B는 "공격"이지만 둘을 함께 다룬 논문이 거의 없는 영역.
- **`recurring-limitation`** — 여러 논문이 초록에서 같은 한계를 반복 명시 (예: "real-world generalization is poor", "scalability remains open").

## 작업
- **3~7개의 갭 후보**를 출력. 한 타입에 몰리지 말고 가능하면 다양하게.
- 각 갭마다 **메타데이터에 명시된 근거**가 있어야 함 (제목/초록 인용 가능).

## 출력 (JSON 배열)
```json
[
  {
    "id": "A",
    "type": "between-clusters" | "single-shot" | "recurring-limitation",
    "description": "한글 2~4 문장",
    "evidence_papers": ["arxiv:..."],
    "why_gap": "한글 1~2 문장 — 왜 이게 진짜 갭인지"
  }
]
```

## 금기
- 추측 ("아마 안 됐을 것 같음" 류)
- 메타데이터에 없는 사실 ("이 논문은 사실 본문에서 X를 다뤘다" 류)
- 너무 trivial한 갭 ("X+더 많은 ablation")
```

- [ ] **Step 2: Commit**

```bash
git add skills/topic-finder/prompts/gap_hunter.md
git commit -m "feat(skill): add gap_hunter prompt"
```

---

### Task 18: `skeptic.md`

**Files:**
- Create: `skills/topic-finder/prompts/skeptic.md`

- [ ] **Step 1: Write prompt**

```markdown
# Skeptic

당신은 Gap-Hunter가 제출한 갭 후보를 **공격적으로 검증**하는 비판가입니다.

## 입력
- 갭 후보 M개 (id, type, description, evidence_papers, why_gap)
- 클러스터 K개 (참조용)
- 매칭 논문 메타 N건 (참조용)

## 검증 기준 (각 갭에 대해 하나라도 맞으면 거부)
- (a) **다른 클러스터에서 이미 다룸** — 사실은 짝꿍 클러스터 안에 풀렸음
- (b) **다른 분야에서 풀렸음** — 본 메타DB 안에 명시 근거가 있음
- (c) **trivial 함** — 갭이 "X에 ablation 추가" 정도로 작음
- (d) **메타로는 알 수 없음** — 본문 봐야 판정 가능 (메타는 짧으니 Skeptic은 *조심스럽게* 보존도 가능)

## 작업
- 각 갭마다 통과(`passed`)/거부(`rejected`)
- 거부면 4가지 사유 중 하나 + 인용 논문 id

## 출력 (JSON 객체)
```json
{
  "passed": [
    { "id": "A", "type": "...", "description": "...",
      "evidence_papers": [...], "skeptic_note": "한 줄 통과 사유" }
  ],
  "rejected": [
    { "id": "X", "description": "...", "reason": "이미 클러스터 3에서 다룸 [arxiv:...]" }
  ]
}
```

## 금기
- 옹호 (모두 통과시키면 안 됨)
- "잘 모르겠음" — 명시적으로 통과/거부
- 메타DB에 없는 외부 논문 인용
```

- [ ] **Step 2: Commit**

```bash
git add skills/topic-finder/prompts/skeptic.md
git commit -m "feat(skill): add skeptic prompt"
```

---

### Task 19: `proposer.md`

**Files:**
- Create: `skills/topic-finder/prompts/proposer.md`

- [ ] **Step 1: Write prompt**

```markdown
# Proposer

당신은 검증된 갭에 기반해 **새로운 연구 제안**을 만드는 제안자입니다.

## 입력
- 살아남은 갭 (passed) — id, type, description, evidence_papers
- 클러스터 K개 (참조)
- 매칭 논문 메타 N건 (참조)
- 목표 제안 수: P (기본 5)

## 작업
- 각 제안 = `{id, name, fills_gap, hypothesis, approach, baselines, expected_contribution, references}`
- `name`: 짧은 시그니처 (영대문자 약어 권장, 예: `SAFE-COORD`, `MARS`, `DEFAGENT`)
- `hypothesis`: 한 문장 (한글). 검증 가능한 명제.
- `approach`: 2~4 문장. 무엇을 어떻게 할지.
- `baselines`: 메타DB에 등장한 baseline·dataset·모델명에서만 인용.
- `expected_contribution`: 2~3 문장.
- `references`: 메타DB 안 논문 id (외부 논문 금지).

## 금기
- **trivial 확장** ("기존 X에 ablation 추가") — 갭이 명시한 한계를 *정면으로* 풀어야 함.
- 메타DB 외부 논문 인용
- 가설이 검증 불가능 (예: "더 좋은 성능을 보임")
- 모든 제안이 같은 갭만 메우는 경우 (가능하면 갭 분산)

## 출력 (JSON 배열)
```json
[
  {
    "id": 1,
    "name": "SAFE-COORD",
    "fills_gap": "A",
    "hypothesis": "한 문장",
    "approach": "2~4 문장",
    "baselines": "방법·데이터셋·모델명",
    "expected_contribution": "2~3 문장",
    "references": ["arxiv:...", "arxiv:..."]
  }
]
```
```

- [ ] **Step 2: Commit**

```bash
git add skills/topic-finder/prompts/proposer.md
git commit -m "feat(skill): add proposer prompt"
```

---

## Phase 6 — Layer 2 SKILL.md (the wiring)

### Task 20: SKILL.md — end-to-end skill description

**Files:**
- Create: `skills/topic-finder/SKILL.md`

**Background:** This is the file Claude Code reads when the user invokes `/find-topic`. It describes the workflow, instructs Claude how to load each prompt, what JSON to expect from each LLM call, and which Python script to run when.

- [ ] **Step 1: Write SKILL.md**

```markdown
---
name: topic-finder
description: Analyze the rolling 30-day metadata DB for the user's keyword, then run a 4-bot pipeline (Trend-Analyzer → Gap-Hunter → Skeptic → Proposer) to produce a Markdown report containing trends, gaps, and concrete research proposals. Use when the user runs /find-topic or asks to find research gaps / proposals for a topic.
---

# topic-finder

Given a research topic keyword from the user, build `reports/YYYY-MM-DD-<slug>.md` containing:
1. trend clusters from the rolling 30-day metadata DB,
2. validated research gaps,
3. concrete new research proposals,

all citing only papers present in the DB (no hallucinated references).

## Prerequisites

- `metadb/rolling.jsonl` exists and is non-empty (run `python -m collector.main` first if not).
- Python 3.11+ on PATH.
- Claude Sonnet 4.6 — this skill is intentionally Sonnet-tuned for cost.

## Arguments

Parsed from `/find-topic "<keyword>" [options...]`:

| Arg | Default | Notes |
|-----|---------|-------|
| `<keyword>` | (required) | User's topic, free-form quoted string |
| `--top N` | 10 | Representative papers per cluster |
| `--clusters K` | 5 | Number of clusters Trend-Analyzer should output |
| `--proposals P` | 5 | Number of proposals Proposer should output |
| `--window D` | 30 | Rolling window days (must be ≤ DB window) |
| `--expand-only` | off | Stop after keyword expansion + match (debug) |
| `--dry-run` | off | Show match count + token estimate then stop |
| `--output <path>` | `reports/YYYY-MM-DD-<slug>.md` | Output path |

## Pipeline

### §1. Keyword expansion

Read `prompts/expand_keywords.md` and replace `{TOPIC}` with the user keyword. Call Sonnet 4.6 once. Parse the JSON array. Save to `reports/.cache/<run-id>/expanded_keywords.json`.

### §2. Match against rolling DB

Run:
```bash
python -m skills.topic_finder.scripts.match_substring \
    --rolling metadb/rolling.jsonl \
    --keywords-file reports/.cache/<run-id>/expanded_keywords.json \
    --out reports/.cache/<run-id>/matched.jsonl
```

(Note: this CLI flag set is implemented in Task 13's script as a `if __name__ == "__main__"` block — add it now if missing.)

Read the match count.

### §3. Scope confirmation (mandatory)

Show the user:

```
**Topic:** "<keyword>"
**Expanded keywords:** [...]
**매칭 논문:** <N>건 (rolling 30d)
**클러스터 K = <K>, 제안 P = <P>, Sonnet 4.6**
**예상 토큰:** ~150K input, ~25K output
**예상 비용:** ~600원

Approve / 수정 / abort
```

If matched count < 10: warn and suggest a different / broader keyword. If > 500: warn and suggest narrowing.

If the user says abort, stop. If they suggest changes, re-run §1 with new keyword and repeat. Only proceed on explicit approval.

If `--dry-run`: print the summary and stop without §4–§7.
If `--expand-only`: stop after §3 print without §4–§7.

### §4. Trend-Analyzer

Read `prompts/trend_analyzer.md`, fill in `{TOPIC}`, append matched papers (id, title, abstract, venue, date — keep abstract <= 1500 chars per paper to bound input). Single Sonnet 4.6 call. Parse the JSON array. Save to `reports/.cache/<run-id>/clusters.json`.

### §5. Gap-Hunter

Read `prompts/gap_hunter.md`, append clusters.json + matched papers. Single Sonnet call. Save to `gaps.json`.

### §6. Skeptic

Read `prompts/skeptic.md`, append gaps.json + clusters.json + matched papers. Single Sonnet call. Save to `gaps_validated.json`.

### §7. Proposer

Read `prompts/proposer.md`, append gaps_validated.passed + clusters + matched. Single Sonnet call. Save to `proposals.json`.

### §8. Build report

Run:
```bash
python -m skills.topic_finder.scripts.build_report \
    --topic "<keyword>" \
    --expanded-file reports/.cache/<run-id>/expanded_keywords.json \
    --matched-file reports/.cache/<run-id>/matched.jsonl \
    --clusters-file reports/.cache/<run-id>/clusters.json \
    --gaps-validated-file reports/.cache/<run-id>/gaps_validated.json \
    --proposals-file reports/.cache/<run-id>/proposals.json \
    --window-days <D> \
    --output reports/<YYYY-MM-DD>-<slug>.md
```

(Note: this CLI flag set is implemented in Task 14's script — add it now if missing.)

### §9. Final report to user

Tell the user:
- the absolute path to the generated report,
- the cluster / gap / proposal counts,
- total tokens used.

## Failure handling

- If keyword expansion returns < 3 keywords or non-JSON: retry once with the same prompt; if still bad, fail with explicit message.
- If matched count is 0 even after retry with broader expansion: stop and ask user to broaden their topic.
- If a single bot returns malformed JSON: retry once with stricter "Return JSON only, no prose" preamble; if still malformed, save the raw output to the cache dir and fail with the path.
- If any LLM call hits rate limit: wait 60s and retry once.

## Out-of-scope (v0.1)

- PDF body analysis (`--deep` integration with paper_search) — deferred to v0.2.
- Embedding-based matching — substring only.
- Personalization based on user's prior reads.
```

- [ ] **Step 2: Add CLI entrypoints to scripts referenced in SKILL.md**

The SKILL.md references CLI flags `--rolling --keywords-file --out` for `match_substring.py` and `--topic --expanded-file ...` for `build_report.py`. Add these `if __name__ == "__main__":` blocks to those scripts now if not already present.

For `skills/topic-finder/scripts/match_substring.py`, append:
```python
if __name__ == "__main__":
    import argparse
    import json
    from pathlib import Path
    from .load_metadb import load_rolling

    parser = argparse.ArgumentParser()
    parser.add_argument("--rolling", required=True)
    parser.add_argument("--keywords-file", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    keywords = json.loads(Path(args.keywords_file).read_text())
    papers = load_rolling(Path(args.rolling))
    matched = match_substring(papers, keywords)

    with open(args.out, "w", encoding="utf-8") as f:
        for p in matched:
            f.write(json.dumps(p.to_jsonl_dict(), ensure_ascii=False) + "\n")
    print(f"Matched {len(matched)} papers → {args.out}")
```

For `skills/topic-finder/scripts/build_report.py`, append:
```python
if __name__ == "__main__":
    import argparse
    import json
    from pathlib import Path
    from datetime import date, timedelta

    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    parser.add_argument("--expanded-file", required=True)
    parser.add_argument("--matched-file", required=True)
    parser.add_argument("--clusters-file", required=True)
    parser.add_argument("--gaps-validated-file", required=True)
    parser.add_argument("--proposals-file", required=True)
    parser.add_argument("--window-days", type=int, default=30)
    parser.add_argument("--output", required=True)
    parser.add_argument("--model", default="claude-sonnet-4-6")
    args = parser.parse_args()

    expanded = json.loads(Path(args.expanded_file).read_text())
    matched = []
    with open(args.matched_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                matched.append(Paper.from_jsonl_dict(json.loads(line)))
    clusters = json.loads(Path(args.clusters_file).read_text())
    gaps_validated = json.loads(Path(args.gaps_validated_file).read_text())
    proposals = json.loads(Path(args.proposals_file).read_text())

    today = date.today()
    md = build_report(
        topic=args.topic,
        expanded=expanded,
        matched=matched,
        clusters=clusters,
        gaps_validated=gaps_validated,
        proposals=proposals,
        run_meta={"model": args.model},
        window=(today - timedelta(days=args.window_days), today),
    )
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(md, encoding="utf-8")
    print(f"Report → {args.output}")
```

- [ ] **Step 3: Verify script CLIs**

```bash
echo '["llm safety"]' > /tmp/kw.json
python -m skills.topic_finder.scripts.match_substring \
    --rolling metadb/rolling.jsonl \
    --keywords-file /tmp/kw.json \
    --out /tmp/matched.jsonl
```

Expected: prints `Matched <N> papers → /tmp/matched.jsonl` (N=0 if rolling.jsonl empty).

- [ ] **Step 4: Commit**

```bash
git add skills/topic-finder/SKILL.md skills/topic-finder/scripts/
git commit -m "feat(skill): add SKILL.md workflow and script CLI entrypoints"
```

---

## Phase 7 — Polish & Release

### Task 21: README.md — usage docs

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Replace stub README with full usage doc**

```markdown
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
```

- [ ] **Step 2: Commit**

```bash
git add README.md
git commit -m "docs: full README with installation and usage"
```

---

### Task 22: End-to-end smoke + v0.1 tag

**Files:** none

- [ ] **Step 1: Run all unit tests**

```bash
pytest -v
```

Expected: all unit tests pass (integration tests deselected).

- [ ] **Step 2: Live data smoke (one source)**

```bash
python -m collector.main --skip-or --skip-s2
```

Expected:
- `metadb/rolling.jsonl` exists with non-zero papers
- `metadb/daily/<today>.md` exists
- `metadb/stats.json` shows fetched > 0 from arXiv + HF

- [ ] **Step 3: Manually run topic-finder skill once**

In Claude Code:
```
/find-topic "language model agents" --dry-run
```

Expected: scope confirmation panel printed, then exits without 4-bot calls.

```
/find-topic "language model agents" --clusters 4 --proposals 3
```

Expected:
- Scope panel asks for approval
- After approval, 5 LLM calls execute
- `reports/YYYY-MM-DD-language-model-agents.md` is created
- Report has all 4 sections (트렌드 / 갭 / 제안 / 참고문헌)
- All `[P-...]` citations resolve to entries in the matched paper list (no hallucinations)

- [ ] **Step 4: Tag v0.1**

```bash
git tag -a v0.1 -m "v0.1 — collector + topic-finder skill end-to-end"
git log --oneline | head -25
```

- [ ] **Step 5: Final commit**

If anything was tweaked during smoke testing, commit it. Otherwise nothing to commit and the v0.1 tag points to the last task's commit.

---

## Self-Review (against spec)

| Spec section | Tasks covering it |
|---|---|
| §3 Architecture diagram | Tasks 1–22 (whole repo realizes it) |
| §4 Layer 1 Data Collector | Tasks 5–11 |
| §4.2 Sources (arXiv·HF·OR·S2) | Tasks 6–9 |
| §4.3 Storage (`daily/*.md`, `rolling.jsonl`, `stats.json`) | Tasks 3, 4, 10 |
| §4.4 Daily flow + prune | Tasks 3, 10, 11 |
| §5.1 Skill structure | Tasks 12–20 |
| §5.2 Bot specs | Tasks 15–19 (prompts) + Task 20 (wiring) |
| §5.3 Pipeline (5 LLM calls) | Task 20 SKILL.md |
| §5.5 Cache directory | Task 20 (workflow saves to `reports/.cache/`) |
| §6 User interface (`/find-topic`, scope gate) | Task 20 SKILL.md §3 |
| §7 Output report format | Task 14 (build_report) |
| §8 Repo structure | All tasks (paths match) |
| §9 v0.1 scope (no `--deep`) | Task 20 explicitly out-of-scope |
| §11 Success criteria | Task 22 smoke test verifies all 6 |

**Type / signature consistency check:**
- `Paper` dataclass fields used consistently across tasks (Task 2 → 3 → 4 → 6–9 → 12–14).
- `RollingDB.append() / .load_all() / .prune()` (Task 3) match calls in Task 10.
- `format_daily_digest(papers, target_date)` signature (Task 4) matches use in Task 10.
- `match_substring(papers, keywords)` signature (Task 13) matches CLI block in Task 20.
- `build_report(...)` keyword-only signature (Task 14) matches CLI block in Task 20.
- `to_jsonl_dict()` / `from_jsonl_dict()` (Task 2) used in Tasks 3, 12, 13, 20.

**Placeholder / TBD scan:** none in this plan.

**Open risks acknowledged but not blocking v0.1:**
- arXiv API hard cap of 2000/query — current `MAX_RESULTS_PER_CATEGORY = 500` may miss bursty days. Address in v0.2 with pagination if data shows truncation.
- OpenReview venue id list (`OPENREVIEW_VENUE_IDS`) is hardcoded as `ICLR.cc/2026/Conference`. Operator must update each conference cycle. Document in collector/src/config.py inline comment.
- Sonnet 4.6 token budget assumes ~200 matched papers. > 500 matches will exceed input budget — handled by Scope-gate warning (Task 20 §3).
