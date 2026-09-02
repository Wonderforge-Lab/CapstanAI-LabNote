#!/usr/bin/env python3
"""Validate the versioned bridge configuration."""
from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "bridge_config.json"
SCHEMA = ROOT / "config" / "bridge_config.schema.json"


def main() -> int:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    errors = sorted(
        Draft202012Validator(schema).iter_errors(config),
        key=lambda error: list(error.absolute_path),
    )
    if errors:
        detail = "\n".join(error.message for error in errors)
        raise AssertionError(f"bridge configuration is invalid:\n{detail}")
    print("bridge configuration schema test passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
