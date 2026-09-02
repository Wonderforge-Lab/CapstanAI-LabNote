#!/usr/bin/env python3
"""Check repository-relative Markdown links without fetching external URLs."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:")


def target_path(raw_target: str) -> str | None:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if not target or target.startswith("#") or target.startswith(SKIP_PREFIXES):
        return None
    return target.split("#", 1)[0]


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for match in LINK.finditer(text):
        target = target_path(match.group(1))
        if target is None:
            continue
        candidate = (path.parent / target).resolve()
        try:
            candidate.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{path}: link escapes repository: {target}")
            continue
        if not candidate.exists():
            errors.append(f"{path}: missing link target: {target}")
    return errors


def main() -> int:
    paths = sorted(ROOT.rglob("*.md"))
    errors = [error for path in paths for error in check_file(path)]
    print("\n".join(errors) if errors else f"checked {len(paths)} Markdown files")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
