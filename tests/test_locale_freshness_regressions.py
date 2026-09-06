#!/usr/bin/env python3
"""Regression tests for locale-pair freshness and survival."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "tests" / "test_locale_freshness.py"


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
    (repository / "tests").mkdir()
    (repository / "locales" / "zh-CN").mkdir(parents=True)
    shutil.copy2(CHECKER, repository / "tests" / CHECKER.name)
    (repository / "tests" / "locale_review_acknowledgements.json").write_text(
        json.dumps({"schema_version": 1, "acknowledgements": []}) + "\n",
        encoding="utf-8",
    )
    (repository / "README.md").write_text("English source\n", encoding="utf-8")
    (repository / "locales" / "zh-CN" / "README.md").write_text(
        "Chinese counterpart\n", encoding="utf-8"
    )
    git(repository, "init", "--quiet")
    git(repository, "config", "user.name", "Fixture")
    git(repository, "config", "user.email", "fixture@example.invalid")
    git(repository, "add", ".")
    git(repository, "commit", "--quiet", "-m", "initial pair")
    return git(repository, "rev-parse", "HEAD")


def commit(repository: Path, message: str) -> str:
    git(repository, "add", "-A")
    git(repository, "commit", "--quiet", "-m", message)
    return git(repository, "rev-parse", "HEAD")


def run_checker(repository: Path, base: str, head: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "tests/test_locale_freshness.py", base, head],
        cwd=repository,
        text=True,
        capture_output=True,
        check=False,
    )


def expect_failure(result: subprocess.CompletedProcess[str], label: str) -> None:
    if result.returncode == 0:
        raise AssertionError(f"{label} was not rejected")


def main() -> int:
    with tempfile.TemporaryDirectory() as temporary:
        repository = Path(temporary)
        base = init_repository(repository)
        (repository / "locales" / "zh-CN" / "README.md").unlink()
        head = commit(repository, "delete localized counterpart")
        expect_failure(run_checker(repository, base, head), "localized deletion")

    with tempfile.TemporaryDirectory() as temporary:
        repository = Path(temporary)
        base = init_repository(repository)
        git(repository, "mv", "README.md", "GUIDE.md")
        head = commit(repository, "rename canonical source only")
        expect_failure(run_checker(repository, base, head), "unpaired source rename")

    with tempfile.TemporaryDirectory() as temporary:
        repository = Path(temporary)
        base = init_repository(repository)
        git(repository, "mv", "README.md", "GUIDE.md")
        git(repository, "mv", "locales/zh-CN/README.md", "locales/zh-CN/GUIDE.md")
        head = commit(repository, "rename both sides of pair")
        result = run_checker(repository, base, head)
        if result.returncode != 0:
            raise AssertionError(
                f"paired rename was rejected:\n{result.stdout}\n{result.stderr}"
            )

    print("locale freshness regression tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
