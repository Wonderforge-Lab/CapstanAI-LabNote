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
12. a final pre-PR forensic/hygiene sweep;
13. a Registry Contract v1 source-alignment and native-language review.

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

## Wave 4: Registry Contract v1 source alignment

Registry Contract v1 and its enforcement work introduced new operational English source material after the first-release locale review. Wave 4 reconciled the selected zh-CN operational route without creating a parallel protocol.

The external Simplified-Chinese review compared:

```text
base:          068e75281c0a33b16e993ca0d7506c947bf4affe
reviewed head: 1556e1fa33efc371f0aca95fbd92fea32038ddef
```

The review passed with no blockers, should-fix findings, minor findings, or new regressions. It confirmed:

- English remains the canonical language route and zh-CN does not create a parallel protocol;
- the control-plane/content-plane boundary and direct-deposit boundary retain their original force;
- `私密转录文本` preserves the full scope of private transcripts;
- generated CSV and `registry/INDEX.md` views remain generated, read-only compatibility views;
- accepted-tag authority, machine identifiers, paths, enums, and template fields remain invariant;
- `source_refs` and `source_note` remain distinct, and `unknown` origin still requires an explanation rather than fabricated references.

Wave 4 also introduced an explicit locale-invariant CI check. It verifies declared source-to-locale counterparts and the protocol literals that must remain unchanged; it deliberately does not attempt to compare translated prose mechanically.

## English-source consistency repairs discovered during localization

Localization exposed stale English communication guidance that still pointed routine work at shared CSV registries.

The canonical English repairs cover:

- `messages/README.md`;
- `messages/ROUTING_RULES.md`;
- `notifications/README.md`.

Routine communication records now follow the canonical JSON-per-record policy. CSV files and `registry/INDEX.md` are generated, read-only compatibility views.

Older English examples were also refreshed so their Markdown shapes and registry guidance match current canonical templates and policies.

See `docs/localization/COMMUNICATION_REGISTRY_SOURCE_DRIFT.md` for the source-level consistency note.

## Remaining source-level question deliberately not changed

The validation process surfaced one pre-existing canonical design question that is not a localization defect and was intentionally not changed in the language-layer work:

- corpus-import wording contains a sequencing question between manifest-first fallback and the missing-full-import-approval stop condition;

Any repair to that item should be made as an explicit English-source policy decision and then propagated to localized surfaces.

## Release-surface hygiene

Raw reviewer prompts, review briefs, interim adjudications, blind-run packets and test matrices were development scaffolding. They were removed from the final release surface before merge.

The durable public evidence is this validation summary, the localization contract, the translation-surface classification, the supported locale itself, and the working compatibility specimen. Development history remains available through Git/PR history without making operational readers walk through the review workbench.
