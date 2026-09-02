#!/usr/bin/env python3
"""Smoke test for repository-relative Markdown links."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts" / "check_markdown_links.py"


def main() -> int:
    result = subprocess.run(
        [sys.executable, str(CHECKER)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(f"Markdown link check failed:\n{result.stdout}\n{result.stderr}")
    print("Markdown link smoke test passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
