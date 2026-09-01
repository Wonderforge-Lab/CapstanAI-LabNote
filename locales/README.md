# Language Layer

CapstanAI - LabNote uses one canonical workflow substrate with localized human-facing and AI-facing language surfaces.

Canonical source language: English (`en`).

| Locale | Language | Status |
| --- | --- | --- |
| `en` | English | canonical source |
| `zh-CN` | Simplified Chinese | **supported** |

## Rules

Localized material follows [`docs/localization/LOCALIZATION_CONTRACT.md`](../docs/localization/LOCALIZATION_CONTRACT.md).

The first-release translation surface is classified in [`docs/localization/TRANSLATION_SURFACE.md`](../docs/localization/TRANSLATION_SURFACE.md).

Core protocol identifiers remain language-invariant. This includes paths, JSON keys, status/enum values, IDs, tag slugs, commands and machine-readable configuration values.

Localized material may translate prose, headings, prompts, explanations and Markdown template section labels while preserving protocol meaning.

## Locale routing

The canonical root `AI_ENTRYPOINT.md` routes to a supported localized operational entrypoint only when the human operator selects that locale.

For Simplified Chinese:

```text
AI_ENTRYPOINT.md
-> locales/zh-CN/AI_ENTRYPOINT.md
-> locales/zh-CN/lobby/README_FIRST.md
-> locales/zh-CN/lobby/VISITOR_CHECKLIST.md
```

If no localized route is selected, English remains the default.

Localized instruction paths do not change canonical runtime artifact paths or machine-readable values.

## Locale layout

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

Machine-facing JSON templates remain canonical and untranslated. Localized Markdown templates preserve canonical field identifiers and status values.

## Validation

`zh-CN` has completed terminology, native-language/cultural, operational-policy, end-to-end compatibility and adversarial behavioural-parity validation.

Final validation outcome:

```text
unresolved translation drift: 0
unresolved localized routing defects: 0
machine/path invariance failures: 0
safety/stop/ask parity failures attributable to localization: 0
human-authority parity failures: 0
```

See [`docs/localization/ZH_CN_VALIDATION.md`](../docs/localization/ZH_CN_VALIDATION.md) for the consolidated validation record.

English remains the canonical protocol source.