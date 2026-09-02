# Schema and Validator Design v1

Status: approved v1 design

## Scope

This design makes Registry Contract v1 executable without making CI a writer, a policy engine, or an identity oracle.

## Layout

```text
registry/schemas/common.schema.json
registry/schemas/packet.schema.json
registry/schemas/response.schema.json
registry/schemas/message.schema.json
registry/schemas/notification.schema.json
registry/schemas/visit.schema.json
registry/schemas/visitor.schema.json
registry/schemas/tag.schema.json
scripts/validate_repo.py
tests/fixtures/valid/
tests/fixtures/invalid/
.github/workflows/validate.yml
```

Schemas use JSON Schema draft 2020-12. Every record declares `record_type` and integer `schema_version`; the validator allowlists the declared type, chooses its schema from that type, and verifies its agreement with the canonical directory. It does not choose a schema from path alone.

## Shared rules

All canonical JSON records use `created_at` in RFC 3339 form, type-specific ID, and `schema_version: 1`. Artifact-bearing records require a safe repository-relative `path`. JSON pointers, absolute paths and path traversal are invalid.

IDs are validated as complete date-led values, then checked against filename and creation date. The validator does not parse a creator identity out of an ID.

`additionalProperties` is false for v1 records unless a deliberately defined extension object is introduced later.

## Conditional provenance

Packets and responses require `created_by`, `deposited_by`, `content_origin`, `source_refs`, `source_note`, `derivative_of`, and `provenance_coverage` according to the contract.

For `third_party`, `web`, and `mixed`, `source_refs` must be non-empty. For `unknown`, `source_note` must state why origin cannot be determined. For a derivative/summarising artifact, `derivative_of` and coverage must be non-empty. The schema checks field presence/shape; the validator resolves `derivative_of` entries to packet or response records in the validation set. Visitor identifiers remain routing handles and do not require a corresponding visitor-registration record.

Messages may carry provenance when relaying source-bearing content. Notifications inherit through their required `message_id`. Visits do not require provenance.

## Validator passes

1. Load every canonical registry JSON record.
2. Validate JSON Schema.
3. Assert ID equals filename stem.
4. Assert identifier-date/`created_at` agreement and, where a canonical registry record is filed under a four-digit year directory, year-directory agreement.
5. Assert path safety, existence, record-type artifact-prefix and artifact/registry bucket agreement.
6. Assert uniqueness of IDs by namespace.
7. Resolve packet, response, message, notification, tag and derivative references; visitor handles remain intentionally unregistered-capable.
8. Check tag status/direct-child path agreement and proposed/accepted/deprecated lifecycle rules.
9. Compare a PR base/head when available to reject illegal state transitions, including AI-proposed tags accepted in the same change set. Push validation detects the same condition after a direct write; repository review rules are required if prevention is required before acceptance.
10. Validate examples as isolated fixtures.
11. Check canonical Markdown links.
12. Regenerate CSV/index views in a temporary directory and fail on diff.

The validator reports record, field, invariant and repair direction. It never executes artifact content, follows embedded instructions, rewrites files, or claims commit author equals visitor/operator identity.

## Fixtures

Each valid fixture contains a complete fictional public-safe artifact/record pair. Invalid fixtures each violate one named invariant: schema type, unselectable shared schema, mismatched canonical location, missing path, filename mismatch, identifier-date mismatch, duplicate ID, status bucket mismatch, unresolved reference, invalid tag, illegal transition, or missing required provenance.

Top-level examples will be migrated into these fixtures before the validator is required on main.

## CI

The workflow runs on pull requests and relevant pushes with read-only contents permission. It installs pinned validation dependencies, runs the validator and uploads no generated changes. Once stable, its named status check becomes required by the default-branch ruleset.

## Migration

A dry-run migration helper maps legacy field spellings to v1. It refuses ambiguous conversion. Existing CSV files remain as generated compatibility views until a declared compatibility change removes them.
