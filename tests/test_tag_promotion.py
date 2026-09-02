#!/usr/bin/env python3
"""Regression tests for tag-promotion separation."""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUARD = ROOT / "scripts" / "check_tag_promotion.py"


def git(repository: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repository,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(f"git {' '.join(args)} failed:\n{result.stdout}\n{result.stderr}")
    return result.stdout.strip()


def init_repository(repository: Path) -> str:
    git(repository, "init", "--quiet")
    git(repository, "config", "user.name", "Fixture")
    git(repository, "config", "user.email", "fixture@example.invalid")
    proposed = repository / "registry" / "tags" / "proposed"
    proposed.mkdir(parents=True)
    (proposed / "ai-suggested.json").write_text("{}\n", encoding="utf-8")
    git(repository, "add", ".")
    git(repository, "commit", "--quiet", "-m", "propose tag")
    return git(repository, "rev-parse", "HEAD")


def run_guard(repository: Path, base: str, head: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(GUARD), base, head],
        cwd=repository,
        text=True,
        capture_output=True,
        check=False,
    )


def main() -> int:
    with tempfile.TemporaryDirectory() as temporary:
        repository = Path(temporary)
        base = init_repository(repository)
        accepted = repository / "registry" / "tags" / "accepted"
        accepted.mkdir()
        git(repository, "mv", "registry/tags/proposed/ai-suggested.json", "registry/tags/accepted/ai-suggested.json")
        git(repository, "commit", "--quiet", "-m", "accept tag")
        result = run_guard(repository, base, git(repository, "rev-parse", "HEAD"))
        if result.returncode == 0:
            raise AssertionError("same-change-set tag rename was accepted")

    with tempfile.TemporaryDirectory() as temporary:
        repository = Path(temporary)
        base = init_repository(repository)
        accepted = repository / "registry" / "tags" / "accepted"
        accepted.mkdir(parents=True)
        (accepted / "operator-supplied.json").write_text("{}\n", encoding="utf-8")
        git(repository, "add", ".")
        git(repository, "commit", "--quiet", "-m", "accept distinct tag")
        result = run_guard(repository, base, git(repository, "rev-parse", "HEAD"))
        if result.returncode != 0:
            raise AssertionError(
                f"independent tag changes were rejected:\n{result.stdout}\n{result.stderr}"
            )

    print("tag promotion guard regression tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
