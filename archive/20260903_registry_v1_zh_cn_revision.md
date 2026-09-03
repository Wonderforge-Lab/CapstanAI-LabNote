# 2026-09-03 Revision: Registry v1 and Simplified Chinese

## Release

`v0.3.0 - Registry v1 and Simplified Chinese Revision`

This revision makes the Registry v1 workflow and Simplified-Chinese documentation route part of the published CapstanAI - LabNote scaffold.

## What Changed

- Registry v1 records, paths, lifecycle rules, generated compatibility-view boundaries, and validator coverage are aligned across the active English documentation surface.
- The public README now routes readers to Simplified Chinese, and the localized entrypoint provides a complete localized reading order without creating a parallel protocol.
- The Simplified-Chinese documentation, lobby, message and notification guidance, templates, and example signoff have received pair review for coverage, machine literals, operational parity, and native readability.
- The final polish corrects accepted terminology, path, generated-view, completion-state, and wording defects found during that review.

## Compatibility Promise

English remains the canonical protocol language. The Simplified-Chinese route does not change canonical runtime paths, JSON keys, status or enum values, IDs, tag slugs, schemas, code, configuration, Git behaviour, permissions, or write targets.

No historical release is rewritten: `v0.1.0` and `v0.2.0 - CapstanAI Identity Migration` remain preserved as historical public releases.

## Validation Record

The final revision head was checked with:

- `scripts/validate_repo.py --fixtures`
- `scripts/validate_repo.py --examples`
- `scripts/validate_repo.py --registry --enforce-filename --check-references --check-tags --check-lifecycle --check-unique-ids`
- `scripts/check_markdown_links.py`
- `scripts/check_tag_promotion.py`
- `git diff --check`

The release tag must point to the exact audited merge commit on `main`.

## Deliberately Deferred

- A richer deterministic CapstanAI layer and relay, vault, and protocol modules remain future work.
- Automated hosted status checks are not asserted by this revision; the recorded validator commands remain the release gate evidence.
