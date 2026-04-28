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

# OpenReview venue ids (active venues).
# - `*.cc/<year>/Conference` form is for OR-native review venues (ICLR, NeurIPS).
#   Returns in-progress submissions before publication.
# - `dblp.org/conf/<UPPER>/<year>` form pulls dblp-imported metadata for venues
#   that don't run on OR (AAAI, ACL family, CVPR, ICCV, KDD, IJCAI, ...).
#   These appear only after the conference finalizes; cdate is set to Jan 1 of
#   the conference year, so they survive the 500-day rolling window from 2025+.
OPENREVIEW_VENUE_IDS = [
    "ICLR.cc/2026/Conference",
    "ICML.cc/2025/Conference",          # OR-native; cdate ~2025 (submission)
    "NeurIPS.cc/2025/Conference",       # OR-native; cdate ~2025-05 (submission)
    "dblp.org/conf/AAAI/2025",
    "dblp.org/conf/ACL/2025",
    "dblp.org/conf/NAACL/2025",
    "dblp.org/conf/EMNLP/2025",
    "dblp.org/conf/IJCNLP/2025",   # AACL-IJCNLP 2025 (joint)
    "dblp.org/conf/IJCAI/2025",
    "dblp.org/conf/CVPR/2025",
    "dblp.org/conf/ICCV/2025",
    "dblp.org/conf/KDD/2025",
]

# HuggingFace daily papers fallback window
HF_FALLBACK_DAYS = 3

# User-Agent for requests
USER_AGENT = "paper-suggestion-bot/0.1"

# Rolling window in days.
# 500 keeps everything published since 2025-01-01 retained as of 2026-04-27
# (2026-04-27 − 500d = 2024-12-14). Bumped from 60 so 2025 conference papers
# survive the daily prune in collector.main. Revisit if storage grows large.
ROLLING_WINDOW_DAYS = 500

# Default paths (relative to repo root)
METADB_DIR = "metadb"
# Rolling DB is partitioned by month under ROLLING_DIR — files named
# <YYMM>_rolling.jsonl (e.g. 2604_rolling.jsonl). See collector.src.db.RollingDB.
ROLLING_DIR = "metadb"
DAILY_DIR = "metadb/daily"
STATS_JSON = "metadb/stats.json"
STATS_HISTORY_JSONL = "metadb/stats_history.jsonl"
