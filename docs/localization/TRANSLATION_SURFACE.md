# Translation Surface Inventory

Status: **implemented first-release inventory**
Branch: `i18n/zh-cn-language-layer`
Canonical source language: English (`en`)
First supported locale: Simplified Chinese (`zh-CN`)

## Classification key

- **A - translate for first release:** essential human or AI-facing material needed for complete localized use.
- **B - translate after core route:** useful supporting material, but not required for first successful end-to-end use.
- **C - keep canonical, localize around it:** machine/protocol structure should remain unchanged; translated explanation may be added elsewhere.
- **D - defer:** historical, empty runtime, binary, or otherwise outside the first localization release.

For `zh-CN`, all Class A surfaces and the selected Class B support surfaces needed for the first supported release have been implemented and reviewed. Treatment text below describes the intended handling of each surface, not unfinished work status. Current locale support status is recorded in `locales/README.md`.

## Top-level files

| Path | Class | Treatment | Reason |
| --- | --- | --- | --- |
| `README.md` | A | Full natural-language companion; language selector implemented in canonical README | Public front door and project explanation |
| `AI_ENTRYPOINT.md` | A | Localized companion preserving paths, gates, stop conditions and force | Deterministic AI entry route |
| `CONTRIBUTING.md` | B | Translate contributor-facing prose | Useful public guidance, not required for operation |
| `PRIVACY.md` | A | Translate with strict semantic parity | Public/private boundary |
| `SECURITY.md` | A | Translate with strict semantic parity | Safety-critical guidance |
| `LICENSE` | C | Keep authoritative English license unchanged | Legal source text |
| `.gitignore` | C | No translation | Machine file |
| `bridge_config.json` | C | Preserve keys/values and canonical paths; locale discovery may be added later only as an explicit protocol/config change | Machine-readable routing/config |

## `docs/`

| Path | Class | Treatment |
| --- | --- | --- |
| `docs/ACQUISITION.md` | A | Full localized onboarding; commands/URLs unchanged |
| `docs/quickstart.md` | A | Full localized walkthrough; paths/identifiers unchanged |
| `docs/visitor_lobby_model.md` | A | Translate carefully; `visitor` has project-specific meaning |
| `docs/message_routing_model.md` | A | Translate routing explanation; paths and states unchanged |
| `docs/review_workflow.md` | A | Translate human-review semantics strictly |
| `docs/BRANCH_HYGIENE.md` | A | Translate branch/PR decision rules strictly |
| `docs/REGISTRY_RECORDS.md` | A | Translate prose; preserve JSON keys, paths and examples structurally |
| `docs/storage_policy.md` | A | Translate storage boundaries strictly |
| `docs/DOCUMENT_DEPOSIT_POLICY.md` | A | Translate format/storage rules strictly |
| `docs/CORPUS_IMPORT_POLICY.md` | A | Translate import approval and stop conditions strictly |
| `docs/CONNECTOR_LIMITATIONS.md` | B | Translate after core route |
| `docs/CONNECTOR_SAFE_WORDING.md` | B | Translate after core route, preserving compatibility intent |
| `docs/branding.md` | A | Translate explanation; product names remain unchanged |

## `lobby/`

| Path | Class | Treatment |
| --- | --- | --- |
| `lobby/README.md` | A | Translate |
| `lobby/README_FIRST.md` | A | Translate with strict entry-order and workspace-context parity |
| `lobby/ROUTINE_DEPOSIT_QUICKSTART.md` | A | Translate with strict workflow parity |
| `lobby/TAGGING_PROTOCOL.md` | A | Translate; canonical tag slugs and registry paths unchanged |
| `lobby/VISITOR_CHECKLIST.md` | A | Translate; safety checks and stop conditions unchanged |
| `lobby/visitors/.gitkeep` | D | No translation | Empty runtime placeholder |

## `messages/`

| Path | Class | Treatment |
| --- | --- | --- |
| `messages/README.md` | B | Translate |
| `messages/MESSAGE_FORMAT.md` | A | Localized explanatory/template surface; canonical fields/states unchanged |
| `messages/ROUTING_RULES.md` | A | Translate routing semantics strictly |
| `messages/open/`, `answered/`, `closed/`, `archived/` | D | No translation | Runtime state directories |

## `notifications/`

| Path | Class | Treatment |
| --- | --- | --- |
| `notifications/README.md` | B | Translate |
| `notifications/RELAY_PROTOCOL.md` | A | Translate headings/explanations; canonical fields/status values unchanged |
| runtime notification directories | D | No translation | Runtime state directories |

## `templates/`

### Markdown templates

These are first-release translation targets because users and AI sessions directly write from them:

- `templates/datadrop_packet.md`
- `templates/ai_response_packet.md`
- `templates/message_packet.md`
- `templates/notification_request.md`
- `templates/review_note.md`
- `templates/visit_signoff.md`
- `templates/visitor_registration.md`

Treatment:

- translate titles, explanatory text and prose section headings,
- preserve canonical field identifiers,
- preserve enum/status values,
- preserve path conventions,
- do not invent localized protocol keys.

### JSON templates

These stay structurally canonical:

- `templates/message_record.json`
- `templates/notification_record.json`
- `templates/packet_record.json`
- `templates/response_record.json`
- `templates/tag_record.json`
- `templates/visit_record.json`

Class: C.

Treatment:

- keep keys and machine values unchanged,
- localize only human-readable example strings if doing so is useful and unambiguous,
- provide localized field explanations outside the JSON object rather than translating keys.

## `examples/`

| Area | Class | Treatment |
| --- | --- | --- |
| top-level Markdown examples | B | Optional localized companion examples; not required for the first supported locale |
| `examples/minimal_routine_deposit/` Markdown | A | Create one complete localized worked example |
| example JSON records | C | Preserve canonical keys/statuses; human-readable strings may be localized |

The first supported localized release should contain at least one complete worked path that demonstrates:

```text
packet -> registry record -> visit record -> signoff
```

without changing protocol structure.

## `registry/`

| Area | Class | Treatment |
| --- | --- | --- |
| directory names | C | Keep unchanged |
| JSON keys and state values | C | Keep unchanged |
| CSV headers | C | Keep unchanged |
| tag slugs | C | Keep unchanged |
| tag display names/descriptions | A/B | Localize through locale metadata or mapping, not by replacing canonical tag records |
| `registry/README.md` | B | Translate explanation |
| runtime record directories | D | No translation |

## `archive/`

Class: D for first release.

The archive contains migration and legacy protocol material. Translating it in the first release would create a second apparent operational route and increase maintenance burden. Historical material may be translated later when there is a specific need.

## `assets/`

Class: D/C.

Binary images do not require translation. Alt text and surrounding prose in localized Markdown should be translated. The SVG should not be modified merely for localization unless it contains user-facing embedded text requiring a separate design decision.

## First-release minimum route

A locale should not be called operationally supported until a user and fresh AI session can complete this route without depending on English explanatory prose:

```text
localized README
-> localized acquisition guide
-> localized AI entrypoint
-> localized lobby entry
-> localized visitor checklist
-> localized routine deposit quickstart
-> localized template
-> canonical registry record
-> localized signoff/review guidance
```

## Explicit non-goals for first release

- translating repository paths,
- translating JSON keys,
- translating status enums,
- translating tag slugs,
- translating Git syntax,
- translating the historical archive,
- maintaining a separate language fork,
- claiming legal equivalence for an unofficial translated license,
- treating Simplified Chinese as equivalent to all Chinese locales.
