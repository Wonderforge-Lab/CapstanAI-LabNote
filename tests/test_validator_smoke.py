#!/usr/bin/env python3
"""Smoke tests for the Registry Contract v1 validator."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_repo.py"

INVALID_FIXTURES = {
    "packet source provenance": ("tests/fixtures/invalid/packet/record.json",),
    "response derivation provenance": ("tests/fixtures/invalid/response/record.json",),
    "message recipient routing": ("tests/fixtures/invalid/message/record.json",),
    "notification status vocabulary": ("tests/fixtures/invalid/notification/record.json",),
    "visit relay boolean": ("tests/fixtures/invalid/visit/record.json",),
    "visitor identifier grammar": ("tests/fixtures/invalid/visitor/record.json",),
    "accepted-tag acceptance record": ("tests/fixtures/invalid/tag/record.json",),
    "artifact path resolution": ("tests/fixtures/invalid/path/record.json",),
    "filename identifier agreement": (
        "--enforce-filename",
        "tests/fixtures/invalid/filename/not-the-packet-id.json",
    ),
    "typed reference resolution": (
        "--check-references",
        "tests/fixtures/valid/packet/record.json",
        "tests/fixtures/invalid/reference/record.json",
    ),
}


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def assert_valid(label: str, *args: str) -> None:
    result = run(*args)
    if result.returncode != 0:
        raise AssertionError(f"{label} failed:\n{result.stdout}\n{result.stderr}")


def root_args(args: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(str(ROOT / arg) if arg.endswith(".json") else arg for arg in args)


def main() -> int:
    assert_valid("valid schema fixtures", "--fixtures", "--check-references")
    assert_valid("contract examples", "--examples", "--check-references")

    for invariant, args in INVALID_FIXTURES.items():
        invalid = run(*root_args(args))
        if invalid.returncode == 0:
            raise AssertionError(
                f"invalid fixture passed for {invariant}:\n{invalid.stdout}\n{invalid.stderr}"
            )

    print(f"validator smoke tests passed ({len(INVALID_FIXTURES)} invalid invariants)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
