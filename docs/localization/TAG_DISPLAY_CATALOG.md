# Tag Display Catalogue

Status: canonical English display source

Canonical tag state, slug, scope, creator, and acceptance metadata live in registry/tags/**/*.json. This catalogue supplies the English display text that localized catalogues may translate without creating new slugs.

| Canonical tag slug | English display name | English description |
| --- | --- | --- |
| capstanai-labnote | CapstanAI - LabNote | Public LabNote template component of the CapstanAI multi-AI workflow ecosystem. |
| example-project | Example Project | Public-safe example project tag for template demonstrations. |
| human-in-the-loop | Human-in-the-loop | Work involving human review, approval, or routing. |
| provenance | Provenance | Work involving source tracking, handoff records, or decision trails. |
| workflow-testing | Workflow Testing | Public-safe tag for testing LabNote workflow mechanics. |

## Localization rule

- Keep the canonical tag slug in machine records.
- Localize only the display name and description.
- Do not create a language-specific equivalent slug.
- Review localized display text whenever its canonical tag record changes.
