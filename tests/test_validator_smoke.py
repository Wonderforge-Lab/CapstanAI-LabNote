#!/usr/bin/env python3
"""Smoke tests for the Registry Contract v1 validator scaffold."""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_repo.py"

def run(path: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), str(ROOT / path)],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )

def main() -> int:
    valid = run("tests/fixtures/valid/packet/record.json")
    if valid.returncode != 0:
        raise AssertionError(f"valid fixture failed:\n{valid.stdout}\n{valid.stderr}")
    invalid = run("tests/fixtures/invalid/packet/record.json")
    if invalid.returncode == 0 or "source_refs" not in invalid.stdout:
        raise AssertionError(f"invalid fixture did not fail as expected:\n{invalid.stdout}\n{invalid.stderr}")
    print("validator smoke tests passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
