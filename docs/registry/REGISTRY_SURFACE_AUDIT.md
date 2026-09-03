# Registry Surface Audit

> **Historical pre-v1 audit.** The findings below describe the repository at the stated baseline and are preserved as design provenance, not as a current defect list. Registry Contract v1 and its supporting schemas, validators, generated views, templates, and lifecycle rules have since resolved several items recorded here. For current normative behaviour, see `docs/registry/REGISTRY_CONTRACT_V1.md` and `docs/REGISTRY_RECORDS.md`.

Baseline: `main` at `824a36dc4c7bebb661fab7511aea6eac3984fa1b`.

## Scope

The census read 121 Markdown, JSON, and CSV protocol surfaces. It covered active English material, supported zh-CN machine-invariant surfaces, templates, examples, registry views, routing material, configuration, and archive references. Binary assets were out of scope.

## Findings

### Three conflicting models

Packet and response Markdown templates use session terminology. Their JSON templates use AI terminology. Their CSV headers use session terminology.

Visit Markdown/CSV use `session_family` and `human_relay_needed`; JSON uses `visitor_family` and `relay_needed`.

Message Markdown defines group routing, reply expectation, human-relay need, related artifacts, and summary. JSON retains only a parent-message relation; CSV retains a partly different subset, including `response_message_id`.

Notification Markdown/CSV use from/to visitor routing, message linkage, human action and summary. JSON instead uses requester/recipient and relay state.

### Lifecycle/path drift

Message artifacts have open, answered, closed, and archived directories. Registry message directories omit archived. Notification artifacts have open, delivered, and closed directories. Registry notification directories omit delivered.

The templates declare separate packet, response, message, notification, visitor, and tag status vocabularies, but no canonical transition table exists.

### Canonical-record gap

`visitor_registry.csv` is described as legacy/optional while visitor registration has no canonical JSON record path or JSON template.

### Example and compatibility drift

Top-level examples use non-canonical placeholder IDs. The minimal routine-deposit specimen uses the legacy JSON field vocabulary. CSV headers omit tags and cannot represent all active JSON relationships.

### Security/trust drift

`SECURITY.md` correctly states that repository files do not execute, but omits the fact that capable sessions can read and act on content. No control-plane allowlist or provenance contract distinguishes an authenticated deposit from authored or authorised content.

### Config/history drift

`bridge_config.json` is not in the entry reading order and lacks schema versioning. The naming-migration archive note describes keys that do not exist in the current config.

## Disposition

The discrepancies are design debt, not evidence of corrupt records. The repository is lightly populated, so Registry Contract v1 can be introduced before a large live-data migration is needed.

See `FIELD_DECISION_MATRIX.md`, `STATUS_LIFECYCLE_MATRIX.md`, and `REGISTRY_CONTRACT_V1.md`.
