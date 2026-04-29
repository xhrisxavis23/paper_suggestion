"""Auto-commit + push helper for collector outputs.

Stages `metadb/` only (so unrelated dirty files are left untouched), commits
with the given message, and pushes to the current branch's tracking remote.

Returns the commit SHA on success, None if there was nothing to commit. Push
failures are logged but not raised — the commit is preserved locally so a
later manual `git push` recovers without losing work. Hard misconfig (not a
git repo) is also logged and returns None.
"""
from __future__ import annotations

import logging
import subprocess
from pathlib import Path

logger = logging.getLogger(__name__)


def commit_metadb(root: Path, message: str) -> str | None:
    repo = Path(root).resolve()
    if not (repo / ".git").exists():
        logger.warning("git_sync: %s is not a git repo, skipping push", repo)
        return None

    def _run(*args: str, check: bool = True) -> subprocess.CompletedProcess:
        return subprocess.run(
            ["git", "-C", str(repo), *args],
            capture_output=True, text=True, check=check,
        )

    _run("add", "metadb/")
    diff = _run("diff", "--staged", "--quiet", check=False)
    if diff.returncode == 0:
        logger.info("git_sync: no metadb changes to commit")
        return None

    _run("commit", "-m", message)
    sha = _run("rev-parse", "HEAD").stdout.strip()
    logger.info("git_sync: committed %s — %s", sha[:8], message)

    push = _run("push", check=False)
    if push.returncode != 0:
        logger.warning(
            "git_sync: push failed (commit %s preserved locally)\n%s",
            sha[:8], push.stderr.strip(),
        )
    else:
        logger.info("git_sync: pushed %s to remote", sha[:8])
    return sha
