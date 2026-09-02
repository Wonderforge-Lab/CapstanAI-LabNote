#!/usr/bin/env python3
"""Read-only Registry Contract v1 validator scaffold."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker, RefResolver

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "registry" / "schemas"

def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)

def schema_for(record: dict) -> Path:
    record_type = record.get("record_type")
    if not isinstance(record_type, str):
        raise ValueError("missing or invalid record_type")
    path = SCHEMAS / f"{record_type}.schema.json"
    if not path.is_file():
        raise ValueError(f"no schema for record_type {record_type!r}")
    return path

def validate(path: Path) -> list[str]:
    try:
        record = load_json(path)
        schema_path = schema_for(record)
        schema = load_json(schema_path)
        resolver = RefResolver(base_uri=SCHEMAS.as_uri() + "/", referrer=schema)
        validator = Draft202012Validator(schema, resolver=resolver, format_checker=FormatChecker())
        errors = sorted(validator.iter_errors(record), key=lambda error: list(error.absolute_path))
        return [f"{path}: {'/'.join(map(str, error.absolute_path)) or '<record>'}: {error.message}" for error in errors]
    except (OSError, ValueError, json.JSONDecodeError) as error:
        return [f"{path}: {error}"]

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args()
    paths = args.paths or ([] if not args.fixtures else sorted((ROOT / "tests" / "fixtures" / "valid").rglob("*.json")))
    if not paths:
        parser.error("supply JSON paths or --fixtures")
    errors = [item for path in paths for item in validate(path)]
    print("\n".join(errors) if errors else f"validated {len(paths)} record(s)")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
