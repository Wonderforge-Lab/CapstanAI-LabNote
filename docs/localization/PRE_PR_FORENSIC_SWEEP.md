# zh-CN Pre-PR Forensic Sweep

Date: 2026-09-01
Branch: `i18n/zh-cn-language-layer`
Locale: `zh-CN`

## Purpose

This sweep was performed after the Simplified-Chinese first-release language layer passed translation, native-language/cultural review, end-to-end compatibility testing, and paired adversarial behavioural-parity testing.

The sweep is a pre-PR hygiene and provenance pass. It is not a new localization phase and does not reopen already-passed language decisions without evidence of a real defect.

## Result

No unresolved localization blocker was found.

The supported `zh-CN` route remains consistent with the canonical English protocol on:

- workspace context and privacy boundaries,
- visitor-handle gating,
- direct-write versus branch/PR decisions,
- canonical runtime paths,
- JSON keys and status/enum values,
- tag slugs and accepted/proposed authority,
- human review authority,
- message delivery and human relay,
- connector fail-closed behaviour,
- binary-document handling,
- corpus-import boundaries.

## Repairs made during the sweep

### 1. Localization metadata promoted from historical draft state

`docs/localization/LOCALIZATION_CONTRACT.md` still said `Status: draft for review` even though `zh-CN` had passed the full support gate.

It is now marked active, records Simplified Chinese as the first supported locale, and describes future-locale review requirements prospectively.

Its sample Chinese template heading was also aligned with the reviewed template/glossary baseline:

```text
## 依据材料 / 来源材料
```

### 2. Translation inventory promoted from Stage 0

`docs/localization/TRANSLATION_SURFACE.md` still presented itself as a Stage 0 inventory and contained future-tense implementation wording.

It is now marked as the implemented first-release inventory and explicitly distinguishes classification/treatment from unfinished work status.

### 3. Localized quickstart kept on the supported `zh-CN` route

`locales/zh-CN/docs/quickstart.md` still named root English lobby paths in its bootstrap sequence.

It now starts at the canonical root `AI_ENTRYPOINT.md` and, after `zh-CN` selection, explicitly continues through:

```text
locales/zh-CN/lobby/README_FIRST.md
locales/zh-CN/lobby/VISITOR_CHECKLIST.md
```

This changes only the localized instruction route. Runtime storage paths remain canonical.

### 4. English minimal routine-deposit example refreshed

The English Markdown example had drifted behind the current Markdown templates.

Repairs:

- `examples/minimal_routine_deposit/datadrop_packet.md` now uses current `source_session` / `target_session` fields and current section names.
- `examples/minimal_routine_deposit/signoff.md` now follows the current `templates/visit_signoff.md` shape.
- its README now states that the example follows the current Markdown template shapes.
- canonical JSON example records were not migrated because they already match the current JSON templates.

The Simplified-Chinese example README was updated to remove its now-obsolete warning about stale English Markdown.

### 5. Example message registry wording aligned with JSON-per-record policy

`examples/example_message_packet.md` previously said to "update the message registry", which was ambiguous after CSV registries became legacy/optional.

It now explicitly instructs creation/update of the canonical JSON message record and says not to edit a legacy CSV registry unless the operator asks.

### 6. Superseded review artefacts removed from live operational/example surfaces

The audit trail was preserved while removing misleading stale state:

- the partial control-policy adjudication was moved to `archive/localization/zh-CN/` and removed from `locales/zh-CN/docs/`;
- the interim adversarial-parity adjudication was moved to `archive/localization/zh-CN/` after the final paired adjudication superseded it;
- the end-to-end example review brief was moved out of the live example folder into `archive/localization/zh-CN/`.

Active final adjudications remain under `locales/zh-CN/`.

## Intentional English-source changes on this branch

The localization branch contains a small number of deliberate English-source changes:

1. root `README.md` adds the Simplified-Chinese selector;
2. root `AI_ENTRYPOINT.md` adds deterministic locale routing while keeping English canonical;
3. `messages/README.md`, `messages/ROUTING_RULES.md`, and `notifications/README.md` repair stale shared-CSV instructions to match the existing JSON-per-record registry policy;
4. English examples were refreshed during this sweep to match current templates and registry guidance.

No canonical machine schema, status enum, tag slug, branch policy, storage policy, document policy, connector policy, or runtime directory was changed as part of the sweep.

## Shared protocol/design debt discovered but intentionally not changed

These are not `zh-CN` defects and are not currently localization blockers. They should be handled only through an explicit canonical protocol/schema decision.

### A. Message `archived` state versus registry directories

The message-file surface includes:

```text
messages/archived/
```

and `archived` is a message status, while canonical registry path documentation currently lists message registry directories for `open`, `answered`, and `closed` but not `archived`.

This was already recorded in `docs/localization/COMMUNICATION_REGISTRY_SOURCE_DRIFT.md` and remains deliberately unresolved.

### B. Corpus-import fallback versus stop-condition wording

`docs/CORPUS_IMPORT_POLICY.md` says that when full-import approval is missing, a manifest/index should be created and the run signed off. The same file also lists missing full-import approval among stop conditions.

The paired parity test showed both language routes choosing the same safe behaviour, but the exact sequencing semantics could be clarified later in the canonical English source.

### C. Markdown versus JSON field-set asymmetries

Current canonical Markdown and JSON artefacts are not one-to-one field mirrors. Examples include:

```text
Markdown packet: source_session / target_session
JSON packet record: source_ai / target_ai

Markdown signoff: session_family / human_relay_needed
JSON visit record: visitor_family / relay_needed
```

Message Markdown and message JSON records also intentionally carry different content/state fields.

Localization preserves these canonical field sets exactly. Any harmonization would be a protocol/schema migration and should not be smuggled into a language-layer PR.

### D. Public/reference runtime boundary could be stated more explicitly

The canonical route positively permits ordinary runtime deposits in controlled live workspaces and prohibits private runtime material in public/reference workspaces. The adversarial tests consistently interpreted public/reference copies as non-live scaffolds for ordinary runtime work, including public-safe deposits.

A future canonical wording pass could make that negative boundary more explicit, but no English/Chinese behavioural divergence remains.

## Review artefacts retained intentionally

Files ending in `_REVIEW_BRIEF.md`, `_REVIEW_ADJUDICATION.md`, and the adversarial test-matrix/run records are retained as localization provenance and test evidence.

They are not part of the operational reading order. Superseded artefacts that carried contradictory live status were moved to `archive/localization/zh-CN/` during this sweep.

## Pre-PR disposition

`zh-CN` remains **supported** on the localization branch.

Pre-PR localization status:

```text
unresolved translation drift: 0
unresolved localized routing defects: 0
machine/path invariance failures: 0
localization safety/stop/ask failures: 0
human-authority parity failures: 0
known shared protocol debts: documented separately, non-blocking for localization
```

No pull request is opened by this sweep.
