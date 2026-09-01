# Language Layer

CapstanAI - LabNote uses one canonical workflow substrate with localized human-facing and AI-facing language surfaces.

Canonical source language: English (`en`).

Current localization work:

| Locale | Language | Status |
| --- | --- | --- |
| `en` | English | canonical source |
| `zh-CN` | Simplified Chinese | first-release translation surface complete candidate; end-to-end specimen reviewed; final completeness review in progress; adversarial parity next |

## Rules

Localized material must follow [`docs/localization/LOCALIZATION_CONTRACT.md`](../docs/localization/LOCALIZATION_CONTRACT.md).

The translation surface is classified in [`docs/localization/TRANSLATION_SURFACE.md`](../docs/localization/TRANSLATION_SURFACE.md).

Core protocol identifiers remain language-invariant. This includes paths, JSON keys, status/enum values, IDs, tag slugs, commands and machine-readable configuration values.

Localized material may translate prose, headings, prompts, explanations and template section labels while preserving protocol meaning.

## Review workflow

A translation should move through these states:

```text
draft
-> protocol review
-> native-language / cultural review
-> parity test
-> supported
```

For `zh-CN`, first-pass translations receive an additional Chinese-language nuance and cultural-alignment review before being marked supported.

A reviewed front-door document does not by itself make the entire locale supported. Operational documents and workflow paths must complete their own translation and parity gates.

## Locale routing

The canonical `AI_ENTRYPOINT.md` may route a current interaction to a reviewed localized operational entrypoint when the human operator has selected that locale.

For Simplified Chinese:

```text
AI_ENTRYPOINT.md
-> locales/zh-CN/AI_ENTRYPOINT.md
-> locales/zh-CN/lobby/README_FIRST.md
-> locales/zh-CN/lobby/VISITOR_CHECKLIST.md
```

Localized instruction paths do not change canonical runtime artifact paths or machine-readable values.

## Locale layout

Current first-release shape:

```text
locales/
├── README.md
└── zh-CN/
    ├── GLOSSARY.md
    ├── README.md
    ├── AI_ENTRYPOINT.md
    ├── docs/
    ├── lobby/
    ├── messages/
    ├── notifications/
    ├── registry/
    ├── templates/
    └── examples/
```

The reviewed glossary gates terminology across the locale. The Chinese README, onboarding route, front-door governance batch, operational entry/lobby control cluster, tagging/document/branch/registry policies, message-routing/review/storage/corpus-import cluster, visitor/session-model + connector + human-relay cluster, corrected concrete communication surface, localized Markdown templates, and complete routine-deposit compatibility specimen have passed their review gates.

Canonical locale routing to the reviewed `zh-CN` operational entrypoint is active on the localization branch. During localization, stale shared-CSV instructions were repaired in the English message/notification surface to match the canonical JSON-per-record registry policy. Machine-facing JSON templates remain canonical and untranslated.

A final completeness sweep identified the remaining inventory/support surfaces: localized `lobby/README.md`, localized `registry/README.md`, and a Simplified-Chinese tag display catalog keyed to canonical tag slugs. Those are now in review. Temporary fallback-to-English clauses were removed where reviewed Chinese companions now exist.

After that narrow completeness gate, the next stage is adversarial behavioural parity testing. The locale must not be marked fully `supported` until that parity gate passes.
