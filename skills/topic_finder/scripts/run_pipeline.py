"""End-to-end driver for the 4-bot pipeline.

v0.4 (I-3): adds Gemini backend in addition to Sonnet.

Backends, selected by `--model`:
  - `sonnet`        Anthropic SDK (cache_control=ephemeral) → CLI fallback
                    (`claude --model sonnet -p`) when SDK / key is missing.
  - `gemini-pro`    Google google-genai SDK on `gemini-2.5-pro` with
                    `cached_content` for the matched-papers prefix.
  - `gemini-flash`  Same SDK on `gemini-2.5-flash` (cheaper, less reasoning).

The pipeline is identical across backends; only the LLM call shape differs.
The matched-papers JSON block is cached (Anthropic ephemeral / Gemini explicit
`cached_content`) so trend's call seeds the cache and gap/skeptic/proposer
reuse the prefix — same I-3 saving on Gemini as on Sonnet.

Output: `reports/<YYYY-MM-DD>-<slug>.md` plus per-stage JSONs under
`reports/.cache/<run-id>/`. Run-meta in the report header records model
and per-bot token usage so cost diffs across backends are visible.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import date, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))

from collector.src.models import Paper  # noqa: E402
from skills.topic_finder.scripts.build_report import build_report  # noqa: E402
from skills.topic_finder.scripts.load_metadb import load_rolling  # noqa: E402
from skills.topic_finder.scripts.match_substring import match_substring  # noqa: E402

PROMPT_DIR = REPO_ROOT / "skills" / "topic_finder" / "prompts"
CACHE_DIR = REPO_ROOT / "reports" / ".cache"
MAX_CACHE_RUNS = 30

SONNET_MODEL = "claude-sonnet-4-6"
GEMINI_PRO_MODEL = "gemini-2.5-pro"
GEMINI_FLASH_MODEL = "gemini-2.5-flash"

# Per-million-token prices (USD) for cost telemetry — informational only.
# Sources: Anthropic pricing page, Google AI pricing page (2026-04).
_PRICES = {
    SONNET_MODEL:        {"in": 3.00,  "in_cached": 0.30,  "out": 15.00},
    GEMINI_PRO_MODEL:    {"in": 1.25,  "in_cached": 0.31,  "out": 10.00},
    GEMINI_FLASH_MODEL:  {"in": 0.30,  "in_cached": 0.075, "out": 2.50},
}


def _load_dotenv() -> None:
    """Best-effort .env load: avoid hard dep on python-dotenv."""
    env = REPO_ROOT / ".env"
    if not env.exists():
        return
    for line in env.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip())


# ----------------------------- Anthropic backend ---------------------------

def _try_anthropic_sdk():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return None
    try:
        import anthropic  # type: ignore
    except ImportError:
        return None
    return anthropic.Anthropic()


def call_sonnet_sdk(client, *, system: str, cached_context: str,
                    user_block: str, label: str, usage_log: list) -> str:
    print(f"  [{label}/sonnet-sdk] cached={len(cached_context)}c  user={len(user_block)}c",
          flush=True)
    resp = client.messages.create(
        model=SONNET_MODEL,
        max_tokens=8192,
        system=[
            {"type": "text", "text": system},
            {"type": "text", "text": cached_context,
             "cache_control": {"type": "ephemeral"}},
        ],
        messages=[{"role": "user", "content": user_block}],
    )
    u = resp.usage
    usage_log.append({
        "label": label, "model": SONNET_MODEL,
        "in": u.input_tokens, "in_cached_read": getattr(u, "cache_read_input_tokens", 0),
        "in_cached_write": getattr(u, "cache_creation_input_tokens", 0),
        "out": u.output_tokens,
    })
    parts = [b.text for b in resp.content if getattr(b, "type", "") == "text"]
    return "\n".join(parts).strip()


def call_sonnet_cli(prompt: str, *, label: str, usage_log: list) -> str:
    """CLI fallback (no SDK / key): pipe prompt via stdin to dodge ARG_MAX."""
    print(f"  [{label}/sonnet-cli] prompt={len(prompt)}c (via stdin)", flush=True)
    proc = subprocess.run(
        ["claude", "--model", "sonnet", "-p"],
        input=prompt, capture_output=True, text=True, timeout=600,
    )
    if proc.returncode != 0:
        sys.stderr.write(proc.stderr)
        raise RuntimeError(f"sonnet-cli failed for {label}: rc={proc.returncode}")
    usage_log.append({"label": label, "model": SONNET_MODEL, "in": None, "out": None,
                      "note": "cli fallback — no token telemetry"})
    return proc.stdout.strip()


# ------------------------------ Gemini backend -----------------------------

class GeminiCtx:
    """Holds an SDK client + a single CreatedCache object reused across bots."""
    def __init__(self, model: str):
        from google import genai  # type: ignore
        from google.genai import types  # type: ignore
        if not os.environ.get("GOOGLE_API_KEY"):
            raise RuntimeError("GOOGLE_API_KEY not set in environment / .env")
        self.client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
        self.types = types
        self.model = model
        self.cache_name: str | None = None  # populated after seed_cache

    def seed_cache(self, cached_context: str, system_for_cache: str = "") -> None:
        """Create a Gemini cached_content for the matched-papers block.
        Gemini min tokens: pro=4096, flash=1024 — our block is well above both."""
        cache = self.client.caches.create(
            model=self.model,
            config=self.types.CreateCachedContentConfig(
                system_instruction=(system_for_cache or
                                    "You are a research-paper meta-analyst. "
                                    "Always respond in valid JSON only, no prose."),
                contents=[cached_context],
                ttl="3600s",
            ),
        )
        self.cache_name = cache.name
        print(f"  [gemini] cached_content created: {cache.name}", flush=True)

    def cleanup(self) -> None:
        if self.cache_name:
            try:
                self.client.caches.delete(name=self.cache_name)
            except Exception as e:  # noqa: BLE001 — best-effort cleanup
                print(f"  [gemini] cache delete warning: {e}", flush=True)


def call_gemini_sdk(ctx: GeminiCtx, *, system: str, user_block: str,
                    label: str, usage_log: list) -> str:
    """Bot-specific system goes inline; matched-papers prefix lives in cache."""
    print(f"  [{label}/{ctx.model}] user={len(user_block)}c  cached={ctx.cache_name}",
          flush=True)
    resp = ctx.client.models.generate_content(
        model=ctx.model,
        contents=[system + "\n\n" + user_block],
        config=ctx.types.GenerateContentConfig(
            cached_content=ctx.cache_name,
            response_mime_type="application/json",
            max_output_tokens=8192,
        ),
    )
    um = getattr(resp, "usage_metadata", None)
    if um:
        usage_log.append({
            "label": label, "model": ctx.model,
            "in": getattr(um, "prompt_token_count", 0),
            "in_cached_read": getattr(um, "cached_content_token_count", 0),
            "out": getattr(um, "candidates_token_count", 0),
        })
    return (resp.text or "").strip()


# ----------------------------- Common helpers ------------------------------

def strip_fences(text: str) -> str:
    text = text.strip()
    fence = re.match(r"^```(?:json)?\s*\n(.*?)\n```\s*$", text, re.DOTALL)
    return fence.group(1).strip() if fence else text


def prune_cache_dirs(keep: int = MAX_CACHE_RUNS) -> int:
    if not CACHE_DIR.exists():
        return 0
    dirs = sorted([d for d in CACHE_DIR.iterdir() if d.is_dir()],
                  key=lambda d: d.stat().st_mtime, reverse=True)
    pruned = 0
    for d in dirs[keep:]:
        shutil.rmtree(d, ignore_errors=True)
        pruned += 1
    return pruned


def papers_to_context(papers, max_abstract: int = 1500) -> list[dict]:
    return [
        {
            "id": p.get_id(),
            "title": p.title,
            "abstract": (p.abstract or "")[:max_abstract],
            "venue": p.venue or "",
            "date": p.published_date.isoformat() if p.published_date else "",
        }
        for p in papers
    ]


def estimate_cost(usage_log: list) -> dict:
    """Sum per-bot tokens × per-model unit price → USD estimate."""
    totals = {"in_uncached": 0, "in_cached_read": 0, "in_cached_write": 0,
              "out": 0, "usd": 0.0}
    for row in usage_log:
        m = row.get("model")
        price = _PRICES.get(m)
        if not price or row.get("in") is None:
            continue
        cached = row.get("in_cached_read", 0) or 0
        write = row.get("in_cached_write", 0) or 0
        uncached = max(0, (row.get("in", 0) or 0) - cached - write)
        out = row.get("out", 0) or 0
        totals["in_uncached"] += uncached
        totals["in_cached_read"] += cached
        totals["in_cached_write"] += write
        totals["out"] += out
        totals["usd"] += (uncached * price["in"]
                         + cached * price["in_cached"]
                         + write * price["in"]   # cache write billed at full input
                         + out * price["out"]) / 1_000_000
    return totals


# ------------------------------- Pipeline ----------------------------------

def main(topic: str, *, window_days: int = 60, k_clusters: int = 5,
         p_proposals: int = 5, max_papers: int = 200,
         keywords_file: Path | None = None,
         model: str = "sonnet") -> Path:
    _load_dotenv()
    pruned = prune_cache_dirs()
    if pruned:
        print(f"[cache] pruned {pruned} old run dir(s)")

    # Backend selection
    gemini_ctx: GeminiCtx | None = None
    anth_client = None
    if model == "sonnet":
        anth_client = _try_anthropic_sdk()
        backend = "sonnet-sdk" if anth_client else "sonnet-cli"
        active_model = SONNET_MODEL
    elif model in ("gemini-pro", "gemini-flash"):
        gemini_model_id = (GEMINI_PRO_MODEL if model == "gemini-pro"
                           else GEMINI_FLASH_MODEL)
        gemini_ctx = GeminiCtx(gemini_model_id)
        backend = f"{model}-sdk"
        active_model = gemini_model_id
    else:
        raise ValueError(f"unknown --model: {model!r}. "
                         f"Expected one of: sonnet, gemini-pro, gemini-flash")
    print(f"[backend] {backend}  ({active_model})")

    run_id = f"v04-{date.today().isoformat()}-{model}-{topic.replace(' ', '-')}"
    cache = CACHE_DIR / run_id
    cache.mkdir(parents=True, exist_ok=True)
    print(f"[topic] {topic}\n[run]   {run_id}")

    usage: list = []

    def call_json(*, label: str, system: str, cached: str, user: str):
        if backend == "sonnet-sdk":
            raw = call_sonnet_sdk(anth_client, system=system, cached_context=cached,
                                  user_block=user, label=label, usage_log=usage)
        elif backend == "sonnet-cli":
            raw = call_sonnet_cli(system + "\n\n" + cached + "\n\n" + user,
                                  label=label, usage_log=usage)
        else:  # gemini-*
            raw = call_gemini_sdk(gemini_ctx, system=system, user_block=user,
                                  label=label, usage_log=usage)
        try:
            return json.loads(strip_fences(raw))
        except json.JSONDecodeError:
            retry_user = ("Return ONLY valid JSON, no prose, no markdown fences.\n\n"
                          + user)
            if backend == "sonnet-sdk":
                raw2 = call_sonnet_sdk(anth_client, system=system, cached_context=cached,
                                       user_block=retry_user, label=f"{label}/retry",
                                       usage_log=usage)
            elif backend == "sonnet-cli":
                raw2 = call_sonnet_cli(system + "\n\n" + cached + "\n\n" + retry_user,
                                       label=f"{label}/retry", usage_log=usage)
            else:
                raw2 = call_gemini_sdk(gemini_ctx, system=system, user_block=retry_user,
                                       label=f"{label}/retry", usage_log=usage)
            try:
                return json.loads(strip_fences(raw2))
            except json.JSONDecodeError as e:
                (cache / f"{label}_raw.txt").write_text(raw2, encoding="utf-8")
                raise RuntimeError(f"{label}: invalid JSON after retry: {e}")

    # §1. expand keywords
    if keywords_file is not None:
        expanded = json.loads(Path(keywords_file).read_text(encoding="utf-8"))
        if not isinstance(expanded, list) or len(expanded) < 3:
            raise RuntimeError(f"keywords-file bad shape: {expanded!r}")
        (cache / "expanded_keywords.json").write_text(
            json.dumps(expanded, ensure_ascii=False, indent=2))
        print(f"[1/5] using preset keywords ({len(expanded)}): {expanded}")
    else:
        expand_tmpl = (PROMPT_DIR / "expand_keywords.md").read_text()
        expand_prompt = expand_tmpl.replace("{TOPIC}", topic)
        # Expansion has no shared cache; hit each backend without cached context.
        if backend == "sonnet-sdk":
            raw = call_sonnet_sdk(anth_client, system="You are a research keyword expander.",
                                  cached_context="", user_block=expand_prompt,
                                  label="expand", usage_log=usage)
        elif backend == "sonnet-cli":
            raw = call_sonnet_cli(expand_prompt, label="expand", usage_log=usage)
        else:
            # No cache yet at expansion time; bypass cached_content.
            resp = gemini_ctx.client.models.generate_content(
                model=gemini_ctx.model,
                contents=[expand_prompt],
                config=gemini_ctx.types.GenerateContentConfig(
                    response_mime_type="application/json", max_output_tokens=2048,
                ),
            )
            um = getattr(resp, "usage_metadata", None)
            if um:
                usage.append({"label": "expand", "model": gemini_ctx.model,
                              "in": getattr(um, "prompt_token_count", 0),
                              "in_cached_read": 0,
                              "out": getattr(um, "candidates_token_count", 0)})
            raw = (resp.text or "").strip()
        try:
            expanded = json.loads(strip_fences(raw))
        except json.JSONDecodeError:
            raise RuntimeError(f"expand returned non-JSON: {raw[:200]!r}")
        if not isinstance(expanded, list) or len(expanded) < 3:
            raise RuntimeError(f"expand returned bad shape: {expanded!r}")
        (cache / "expanded_keywords.json").write_text(
            json.dumps(expanded, ensure_ascii=False, indent=2))
        print(f"[1/5] expanded keywords ({len(expanded)}): {expanded}")

    # §2. match
    since = date.today() - timedelta(days=window_days)
    papers = load_rolling(since=since)
    matched_full = match_substring(papers, expanded)
    matched = match_substring(papers, expanded, max_papers=max_papers)
    cap_msg = (f", capped from {len(matched_full)} to {max_papers}"
               if len(matched_full) > max_papers else "")
    print(f"[2/5] matched {len(matched)} papers (window={window_days}d{cap_msg})")
    matched_path = cache / "matched.jsonl"
    with matched_path.open("w", encoding="utf-8") as f:
        for p in matched:
            f.write(json.dumps(p.to_jsonl_dict(), ensure_ascii=False) + "\n")

    cached_papers_block = (
        "## 매칭 논문 (id / title / abstract / venue / date)\n"
        + json.dumps(papers_to_context(matched), ensure_ascii=False)
    )

    # Gemini: seed the cached_content once before bot calls.
    if gemini_ctx:
        gemini_ctx.seed_cache(cached_papers_block)

    try:
        # §3. trend
        ta_tmpl = (PROMPT_DIR / "trend_analyzer.md").read_text()
        clusters = call_json(
            label="trend",
            system=ta_tmpl.replace("{TOPIC}", topic),
            cached=cached_papers_block,
            user=f"## 목표 클러스터 수\nK = {k_clusters}",
        )
        (cache / "clusters.json").write_text(json.dumps(clusters, ensure_ascii=False, indent=2))
        print(f"[3/5] clusters: {len(clusters)}")

        # §4. gap
        gh_tmpl = (PROMPT_DIR / "gap_hunter.md").read_text()
        gaps = call_json(
            label="gap",
            system=gh_tmpl,
            cached=cached_papers_block,
            user="## 클러스터 K개\n" + json.dumps(clusters, ensure_ascii=False),
        )
        (cache / "gaps.json").write_text(json.dumps(gaps, ensure_ascii=False, indent=2))
        print(f"      gap candidates: {len(gaps)}")

        # §5. skeptic
        sk_tmpl = (PROMPT_DIR / "skeptic.md").read_text()
        gaps_validated = call_json(
            label="skeptic",
            system=sk_tmpl,
            cached=cached_papers_block,
            user=("## 갭 후보\n" + json.dumps(gaps, ensure_ascii=False)
                  + "\n\n## 클러스터\n" + json.dumps(clusters, ensure_ascii=False)),
        )
        (cache / "gaps_validated.json").write_text(
            json.dumps(gaps_validated, ensure_ascii=False, indent=2))
        print(f"[4/5] gaps passed: {len(gaps_validated.get('passed', []))} / "
              f"rejected: {len(gaps_validated.get('rejected', []))}")

        # §6. proposer
        pr_tmpl = (PROMPT_DIR / "proposer.md").read_text()
        proposals = call_json(
            label="proposer",
            system=pr_tmpl,
            cached=cached_papers_block,
            user=("## 살아남은 갭\n"
                  + json.dumps(gaps_validated.get("passed", []), ensure_ascii=False)
                  + "\n\n## 클러스터\n" + json.dumps(clusters, ensure_ascii=False)
                  + f"\n\n## 목표 제안 수\nP = {p_proposals}"),
        )
        (cache / "proposals.json").write_text(
            json.dumps(proposals, ensure_ascii=False, indent=2))
        print(f"[5/5] proposals: {len(proposals)}")
    finally:
        if gemini_ctx:
            gemini_ctx.cleanup()

    # Cost telemetry
    totals = estimate_cost(usage)
    if usage:
        print("[cost] per-bot token usage:")
        for row in usage:
            print(f"  - {row.get('label')} ({row.get('model')}): "
                  f"in={row.get('in')} cached={row.get('in_cached_read', 0)} "
                  f"out={row.get('out')}")
        print(f"[cost] totals: in_uncached={totals['in_uncached']}  "
              f"in_cached_read={totals['in_cached_read']}  out={totals['out']}  "
              f"≈ ${totals['usd']:.4f}")
    (cache / "usage.json").write_text(
        json.dumps({"per_call": usage, "totals": totals}, ensure_ascii=False, indent=2))

    # §7. report
    today = date.today()
    md = build_report(
        topic=topic, expanded=expanded, matched=matched,
        clusters=clusters, gaps_validated=gaps_validated, proposals=proposals,
        run_meta={
            "model": active_model, "backend": backend,
            "matched_n": len(matched),
            "matched_total_before_cap": len(matched_full),
            "window_days": window_days,
            "tokens_in_uncached": totals["in_uncached"],
            "tokens_in_cached_read": totals["in_cached_read"],
            "tokens_out": totals["out"],
            "usd_estimate": f"${totals['usd']:.4f}",
        },
        window=(today - timedelta(days=window_days), today),
    )
    slug = topic.lower().replace(" ", "-")
    suffix = "" if model == "sonnet" else f"-{model}"
    report_path = REPO_ROOT / "reports" / f"{today.isoformat()}-{slug}{suffix}.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(md, encoding="utf-8")
    print(f"[done] report → {report_path}")
    return report_path


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("topic")
    ap.add_argument("--window-days", type=int, default=60)
    ap.add_argument("--clusters", type=int, default=5)
    ap.add_argument("--proposals", type=int, default=5)
    ap.add_argument("--max-papers", type=int, default=200)
    ap.add_argument("--model", default="sonnet",
                    choices=["sonnet", "gemini-pro", "gemini-flash"])
    ap.add_argument("--keywords-file", type=Path, default=None)
    args = ap.parse_args()
    t0 = time.time()
    main(args.topic, window_days=args.window_days, k_clusters=args.clusters,
         p_proposals=args.proposals, max_papers=args.max_papers,
         keywords_file=args.keywords_file, model=args.model)
    print(f"[wall] {time.time() - t0:.1f}s")
