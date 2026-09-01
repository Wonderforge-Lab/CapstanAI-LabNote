# Localization Contract

Status: **active**
Canonical source language: English (`en`)
First supported locale: Simplified Chinese (`zh-CN`)

## Purpose

CapstanAI - LabNote should support multiple human languages without creating incompatible workflow dialects.

Localization changes how people and AI sessions read and explain LabNote. It must not silently change the underlying protocol.

Core rule:

```text
one workflow substrate
many language surfaces
```

## Canonical substrate

The following remain canonical and language-invariant unless a later protocol change explicitly says otherwise:

- repository paths and filenames used by the workflow,
- JSON keys,
- JSON/Markdown field identifiers used as protocol fields,
- enum and status values,
- tag slugs,
- packet, response, message, notification and visitor IDs,
- canonical directory names,
- Git commands and command-line flags,
- URLs and repository identifiers,
- code, config keys and machine-readable values,
- safety and routing semantics.

Examples that must remain unchanged inside localized material:

```text
AI_ENTRYPOINT.md
lobby/ROUTINE_DEPOSIT_QUICKSTART.md
registry/packets/<year>/<packet_id>.json
packet_id
visitor_id
status: new | in_review | answered | superseded | archived
human-in-the-loop
```

## Localizable surface

The following may be localized while preserving meaning:

- explanatory prose,
- headings and section titles,
- operator-facing prompts,
- README and onboarding text,
- workflow explanations,
- template section headings,
- human-readable examples,
- tag display names and descriptions,
- troubleshooting text,
- culturally dependent idiom and metaphor where a literal translation would distort meaning.

## Translation priorities

Two translation modes are required.

### Human front door

README, onboarding, explanatory examples and similar material should read naturally in the target language. Preserve intent, tone and accessibility rather than sentence-by-sentence literalism.

Rule:

> Human front door: preserve voice.

### Operational substrate

Entrypoints, lobby rules, safety checks, stop conditions, branch rules, registry instructions and policy files should preserve force and control semantics exactly.

Words equivalent to `must`, `may`, `do not`, `stop`, `ask`, `accepted`, `proposed`, `public/reference-only`, and `controlled live workspace` must not be softened or strengthened accidentally.

Rule:

> Operational substrate: preserve force.

## Product and project names

These names are marks and remain unchanged:

- `CapstanAI`
- `LabNote`
- `CapstanAI - LabNote`
- `WonderForge`

Localized material may explain their meaning but should not replace the names with translated product names.

## Templates

Localized Markdown templates may translate human-facing headings while keeping canonical protocol fields and enum values unchanged.

Preferred pattern:

```text
packet_id:
source_session:
status: new | in_review | answered | superseded | archived

## 背景
## 任务
## 依据材料 / 来源材料
```

Do not create translated JSON keys such as `数据包编号` in place of `packet_id`.

## Tags

Tag slugs remain canonical and language-invariant.

Example:

```text
human-in-the-loop
```

A localized layer may supply a translated display name and description keyed to that slug. It must not create a parallel Chinese slug for the same concept.

## Archive and legal material

- `LICENSE` remains the authoritative Apache-2.0 license text.
- Historical material under `archive/` is outside the first localization release unless specifically selected later.
- Localized legal or policy explanations must not be presented as replacing authoritative source text unless formally reviewed for that purpose.

## Review and support status

A locale begins as provisional and must be reviewed for:

1. protocol fidelity,
2. natural target-language usage,
3. cultural fit and register,
4. terminology consistency,
5. ambiguity around AI-session roles,
6. preservation of stop conditions and human authority.

External native-language review is welcome and should be adjudicated against the canonical English protocol rather than accepted automatically.

The first `zh-CN` release has completed terminology review, native-language/cultural review, end-to-end compatibility testing, and paired adversarial behavioural-parity testing. Its current support status is recorded in `locales/README.md`.

Future locales must complete their own review and parity gates before being marked supported.

## Compatibility test

A localized LabNote route is acceptable only if a fresh AI session using that locale reaches materially the same operational decisions as one using the canonical English route.

At minimum, parity testing should compare:

- workspace-context classification,
- visitor-handle requirement,
- branch versus direct-write decision,
- canonical paths used,
- registry record structure,
- tag state handling,
- privacy and storage boundaries,
- stop conditions,
- human-review and relay behaviour.

A translation that reads well but changes behaviour is a failed translation.
