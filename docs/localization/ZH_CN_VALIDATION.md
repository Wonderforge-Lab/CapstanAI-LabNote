# Simplified-Chinese (`zh-CN`) Validation

Status: **supported**
Canonical protocol source: English (`en`)
Validated locale: Simplified Chinese (`zh-CN`)

## Purpose

This record summarizes the validation evidence for the first supported non-English CapstanAI - LabNote language layer.

The locale follows one core rule:

```text
one workflow substrate
many language surfaces
```

Chinese localizes human-facing and AI-facing language. Canonical runtime paths, JSON keys, protocol field identifiers, enum/status values, IDs, tag slugs, Git behaviour, permissions, write targets, storage rules, routing rules and human authority remain language-invariant.

## Validation gates completed

The first-release `zh-CN` surface completed:

1. localization-contract and translation-surface classification;
2. high-risk terminology review and glossary stabilization;
3. front-door and onboarding review;
4. governance and operational-policy review;
5. session, connector, relay, routing, storage and corpus review;
6. concrete message and notification surface review;
7. Markdown-template review;
8. a complete Chinese-facing routine-deposit compatibility specimen;
9. first-release inventory/completeness review;
10. paired English / Simplified-Chinese adversarial behavioural testing;
11. a controlled frozen-source narrow retest of the remaining parity suspects;
12. a final pre-PR forensic/hygiene sweep.

External Simplified-Chinese language review was supplied through DeepSeek and then adjudicated against the canonical English source and the project glossary. Reviewer suggestions were not automatically accepted where they would change protocol force, terminology meaning or machine compatibility.

## End-to-end compatibility specimen

The worked example lives at:

```text
locales/zh-CN/examples/minimal_routine_deposit/
```

It demonstrates Chinese human-facing Markdown alongside canonical machine structure and canonical runtime destinations.

The specimen preserves:

- English machine field names;
- English enum/status values;
- canonical IDs;
- canonical tag slugs;
- canonical JSON-per-record structure;
- canonical runtime paths;
- direct-write behaviour for ordinary controlled-workspace deposits;
- human authority and relay semantics.

It does not create a localized runtime tree under `locales/zh-CN/`.

## Behavioural parity

A 30-scenario adversarial matrix tested English and Simplified-Chinese behaviour across:

- workspace-context classification;
- visitor-handle requirements;
- direct-write versus branch/PR decisions;
- force-push handling;
- canonical paths and machine values;
- accepted/proposed tag authority;
- message delivery and human relay;
- connector fail-closed behaviour;
- document/binary handling;
- corpus-import gates;
- acquisition routes;
- public/reference versus controlled-workspace boundaries.

A subsequent three-scenario frozen-source retest targeted the remaining cases where the first paired run differed in output labeling or stop/ask interpretation.

Final disposition:

```text
unresolved translation drift: 0
unresolved localized routing defects: 0
machine/path invariance failures: 0
safety/stop/ask parity failures attributable to localization: 0
human-authority parity failures: 0
```

`zh-CN` is therefore supported while English remains the canonical protocol source.

## English-source consistency repairs discovered during localization

Localization exposed stale English communication guidance that still pointed routine work at shared CSV registries.

The canonical English repairs cover:

- `messages/README.md`;
- `messages/ROUTING_RULES.md`;
- `notifications/README.md`.

Routine communication records now follow the repository's existing canonical JSON-per-record policy; CSV files remain legacy/optional rollups.

Older English examples were also refreshed so their Markdown shapes and registry guidance match current canonical templates and policies.

See `docs/localization/COMMUNICATION_REGISTRY_SOURCE_DRIFT.md` for the source-level consistency note.

## Shared protocol debt deliberately not changed

The validation process surfaced several pre-existing canonical design questions that are not localization defects and were intentionally not changed in the language-layer work:

- message file/status `archived` exists while canonical message-registry path documentation currently lists `open`, `answered` and `closed`;
- corpus-import wording contains a sequencing question between manifest-first fallback and the missing-full-import-approval stop condition;
- some Markdown and JSON artifacts use different canonical field names, including `source_session` / `target_session` versus `source_ai` / `target_ai`, and `session_family` / `human_relay_needed` versus `visitor_family` / `relay_needed`;
- the public/reference runtime boundary could be stated more explicitly in a future canonical protocol clarification.
- Registry Contract v1 now treats CSV files and `registry/INDEX.md` as generated compatibility views; `locales/zh-CN/registry/README.md` retains the earlier legacy/optional-rollup wording and is queued for Wave 4 correction.

Any repair to those items should be made as an explicit English-source protocol/schema decision and then propagated to localized surfaces.

## Release-surface hygiene

Raw reviewer prompts, review briefs, interim adjudications, blind-run packets and test matrices were development scaffolding. They were removed from the final release surface before merge.

The durable public evidence is this validation summary, the localization contract, the translation-surface classification, the supported locale itself, and the working compatibility specimen. Development history remains available through Git/PR history without making operational readers walk through the review workbench.
