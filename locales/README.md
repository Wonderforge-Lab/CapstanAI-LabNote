# Language Layer

CapstanAI - LabNote uses one canonical workflow substrate with localized human-facing and AI-facing language surfaces.

Canonical source language: English (`en`).

Current localization work:

| Locale | Language | Status |
| --- | --- | --- |
| `en` | English | canonical source |
| `zh-CN` | Simplified Chinese | README reviewed; operational layer in development |

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

## Locale layout

Target shape:

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
    ├── templates/
    └── examples/
```

The reviewed glossary gates terminology across the locale. The Chinese README is now reviewed and linked from the root front door. Remaining operational material should be populated in stages so each surface can receive protocol and Chinese-language review before the locale is marked fully supported.
