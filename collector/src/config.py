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
S2_VENUES = ["AAAI", "NeurIPS", "ICML", "ICLR", "CVPR", "KDD", "SIGMOD", "VLDB"]

# OpenReview venue ids (active venues).
# - `*.cc/<year>/Conference` form is for OR-native review venues (ICLR, ICML,
#   NeurIPS). Returns in-progress submissions for upcoming years and full
#   accepted-paper bibliography for past years.
# - `dblp.org/conf/<UPPER>/<year>` form pulls dblp-imported metadata for venues
#   that don't run on OR (AAAI, ACL family, CVPR, ICCV/ECCV, KDD, SIGMOD/VLDB,
#   AISTATS, ICAIF, ...). These appear only after the conference finalizes;
#   cdate is set to Jan 1 of the conference year. Each entry is verified to
#   return >0 papers via the OpenReview API.
# - Biennial venues (ICCV odd years; ECCV even years; AACL-IJCNLP odd years)
#   intentionally have only the years they actually ran.
# - Workshops use `<HOST>.cc/<year>/Workshop/<acronym>`. The scraper sets
#   venue = "<HOST>" (e.g., "NeurIPS"), so workshop papers inherit the
#   host conference's venue weight.
OPENREVIEW_VENUE_IDS = [
    # === ICLR (OR-native; ICLR 2023 only available via dblp form) ===
    "dblp.org/conf/ICLR/2023",
    "ICLR.cc/2024/Conference",
    "ICLR.cc/2025/Conference",
    "ICLR.cc/2026/Conference",
    # === ICML (OR-native) ===
    "ICML.cc/2023/Conference",
    "ICML.cc/2024/Conference",
    "ICML.cc/2025/Conference",
    # === NeurIPS (OR-native) ===
    "NeurIPS.cc/2023/Conference",
    "NeurIPS.cc/2024/Conference",
    "NeurIPS.cc/2025/Conference",
    # NeurIPS Datasets & Benchmarks track (separate from main Conference).
    # 2023 uses /Track/ prefix; 2024/2025 dropped it.
    "NeurIPS.cc/2023/Track/Datasets_and_Benchmarks",
    "NeurIPS.cc/2024/Datasets_and_Benchmarks_Track",
    "NeurIPS.cc/2025/Datasets_and_Benchmarks_Track",
    # === AAAI (annual) ===
    "dblp.org/conf/AAAI/2023",
    "dblp.org/conf/AAAI/2024",
    "dblp.org/conf/AAAI/2025",
    # === ACL family — NLP ===
    "dblp.org/conf/ACL/2023",
    "dblp.org/conf/ACL/2024",
    "dblp.org/conf/ACL/2025",
    "dblp.org/conf/NAACL/2024",            # NAACL 2023 not in dblp-OR; 2025 covered
    "dblp.org/conf/NAACL/2025",
    "dblp.org/conf/EMNLP/2023",
    "dblp.org/conf/EMNLP/2024",
    "dblp.org/conf/EMNLP/2025",
    "dblp.org/conf/IJCNLP/2023",           # AACL-IJCNLP 2023 (biennial)
    "dblp.org/conf/IJCNLP/2025",           # AACL-IJCNLP 2025 (biennial)
    # === IJCAI (annual) ===
    "dblp.org/conf/IJCAI/2023",
    "dblp.org/conf/IJCAI/2024",
    "dblp.org/conf/IJCAI/2025",
    # === CV (CVPR annual; ICCV/ECCV alternate biennial) ===
    "dblp.org/conf/CVPR/2023",
    "dblp.org/conf/CVPR/2024",
    "dblp.org/conf/CVPR/2025",
    "dblp.org/conf/ICCV/2023",             # biennial: 2023, 2025
    "dblp.org/conf/ICCV/2025",
    "dblp.org/conf/ECCV/2022",             # biennial: 2022, 2024
    "dblp.org/conf/ECCV/2024",
    # === Data mining / DB ===
    "dblp.org/conf/KDD/2023",
    "dblp.org/conf/KDD/2024",
    "dblp.org/conf/KDD/2025",
    "dblp.org/conf/SIGMOD/2023",
    "dblp.org/conf/SIGMOD/2024",
    "dblp.org/conf/SIGMOD/2025",
    "dblp.org/conf/VLDB/2023",
    "dblp.org/conf/VLDB/2024",
    "dblp.org/conf/VLDB/2025",
    # === AISTATS ===
    "dblp.org/conf/AISTATS/2023",
    "dblp.org/conf/AISTATS/2024",
    "dblp.org/conf/AISTATS/2025",
    # === ICAIF — finance-dedicated venue ===
    "dblp.org/conf/ICAIF/2020",
    "dblp.org/conf/ICAIF/2021",
    "dblp.org/conf/ICAIF/2022",
    "dblp.org/conf/ICAIF/2023",
    "dblp.org/conf/ICAIF/2024",
    "dblp.org/conf/ICAIF/2025",
    # === Finance/OR workshops at NeurIPS/ICML ===
    "NeurIPS.cc/2025/Workshop/GenAI_in_Finance",
    "NeurIPS.cc/2025/Workshop/MLxOR",
    "ICML.cc/2024/Workshop/Agentic_Markets",
]

# Journal targets queried via OpenAlex (`--with-journal`).
# Each entry: ISSN (any one of print/electronic) + a short display name used
# as `Paper.venue`. OpenAlex's `primary_location.source.issn` filter accepts
# the ISSN with or without a hyphen and matches on either ISSN form.
# Add new journals by extending this list.
JOURNAL_TARGETS = [
    {"issn": "1551-3203", "name": "IEEE Trans. Industrial Informatics"},
    {"issn": "0957-4174", "name": "Expert Systems with Applications"},
    # Finance / IE-aligned journals
    {"issn": "2640-3943", "name": "Journal of Financial Data Science"},
    {"issn": "1469-7688", "name": "Quantitative Finance"},
    {"issn": "0167-9236", "name": "Decision Support Systems"},
]

# Per-journal cap per fetch — guards against unexpected publication spikes
# and bounds the JSONL growth from a one-shot pull.
JOURNAL_PER_VENUE_LIMIT = 200

# HuggingFace daily papers fallback window
HF_FALLBACK_DAYS = 3

# User-Agent for requests
USER_AGENT = "paper-suggestion-bot/0.1"

# How far back the OpenAlex (--with-journal) and Semantic Scholar (--with-s2)
# scrapers should query. NOT a prune window — the DB is append-only. This
# only caps the "from_publication_date" filter on those external APIs so a
# single fetch doesn't drag the entire venue history. Set to 1500 days
# (~4 years) to cover 2023 onwards; bump if you want older backfill.
SCRAPE_WINDOW_DAYS = 1500

# Default paths (relative to repo root)
METADB_DIR = "metadb"
# Rolling DB is partitioned by month under ROLLING_DIR — files named
# <YYMM>_rolling.jsonl (e.g. 2604_rolling.jsonl). See collector.src.db.RollingDB.
ROLLING_DIR = "metadb"
DAILY_DIR = "metadb/daily"
STATS_JSON = "metadb/stats.json"
STATS_HISTORY_JSONL = "metadb/stats_history.jsonl"
