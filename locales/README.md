# Language Layer

CapstanAI - LabNote uses one canonical workflow substrate with localized human-facing and AI-facing language surfaces.

Canonical source language: English (`en`).

Current localization work:

| Locale | Language | Status |
| --- | --- | --- |
| `en` | English | canonical source |
| `zh-CN` | Simplified Chinese | in development; terminology review required |

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

For `zh-CN`, first-pass translations are expected to receive an additional Chinese-language nuance and cultural-alignment review before being marked supported.

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

Only the glossary is created during the terminology phase. The remaining locale tree should be populated after terminology review so early wording choices do not propagate through the whole repository.
