#!/usr/bin/env python3
"""Smoke test for generated registry compatibility views."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "scripts" / "generate_registry_views.py"


def main() -> int:
    result = subprocess.run(
        [sys.executable, str(GENERATOR), "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(f"generated views are stale:\n{result.stdout}\n{result.stderr}")
    print("generated view smoke test passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
