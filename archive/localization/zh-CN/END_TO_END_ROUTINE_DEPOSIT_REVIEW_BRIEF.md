# Archived Simplified-Chinese End-to-End Routine Deposit Compatibility Review Brief

> Historical review handoff. The reviewed specimen remains at `locales/zh-CN/examples/minimal_routine_deposit/`. The English minimal routine-deposit example has since been refreshed to the current Markdown template shapes, so the historical English-drift note below no longer describes the live branch. This file is retained only for audit provenance.

Target locale: `zh-CN`

Review target folder:

```text
locales/zh-CN/examples/minimal_routine_deposit/
```

Files:

- `README.md`
- `datadrop_packet.md`
- `packet_record.json`
- `visit_record.json`
- `signoff.md`

## Purpose

This was the first end-to-end compatibility specimen for the Simplified-Chinese LabNote language layer.

The test was not merely whether the Chinese read well. It had to demonstrate that a Chinese-facing workflow could produce artifacts that remained compatible with the same canonical machine protocol used by English sessions.

## Core invariants checked

1. Human-facing Markdown titles, headings, task descriptions, notes and summaries may be Chinese.
2. Machine-facing field names remain English and unchanged.
3. Machine status/enum values remain English and unchanged.
4. IDs remain stable machine identifiers.
5. Runtime artifact paths remain canonical and do not move under `locales/zh-CN/`.
6. JSON keys remain exactly compatible with the canonical JSON templates.
7. Chinese free-text values inside JSON `notes` fields do not affect machine compatibility.
8. No CSV registry edit is introduced.
9. No task branch is introduced for the fictional routine deposit.
10. No parallel localized runtime tree such as `locales/zh-CN/datadrops/` or `locales/zh-CN/registry/` is created or implied.

## Expected canonical runtime targets represented by the example

```text
datadrops/shared/inbox/20260901-zhcn-example-routine-test.md
registry/packets/2026/20260901-zhcn-example-routine-test.json
registry/visits/2026/20260901-zhcn-example-routine-test-visit.json
responses/signoffs/20260901-zhcn-example-routine-test-signoff.md
```

The files in the localized example directory are documentation/test specimens. They demonstrate what a live Chinese-language run would create at the canonical runtime paths above.

## Datadrop packet check

The review checked that the Markdown packet followed the localized `datadrop_packet.md` template:

- title and section headings may be Chinese,
- fields remain canonical English identifiers,
- `status: new` remains an English machine state,
- evidence/source wording remains consistent with the reviewed glossary,
- no Chinese replacement is introduced for machine fields.

## Packet JSON record check

The review compared `packet_record.json` with the canonical `templates/packet_record.json` schema.

Expected keys:

```text
packet_id
date
source_ai
target_ai
topic
status
path
response_expected
response_packet_id
tags
notes
```

## Visit JSON record check

The review compared `visit_record.json` with canonical `templates/visit_record.json`.

Expected keys:

```text
visit_id
date
visitor_id
visitor_family
checked_messages
answered_messages
created_messages
relay_needed
signoff_path
notes
```

Chinese free text in `notes` was permitted; key names and path semantics were not localized.

## Signoff check

The review verified that the signoff followed the localized `visit_signoff.md` template:

- the title correctly referred to a visitor-session signoff,
- field names remained English,
- headings could be Chinese,
- `signoff_path` remained canonical,
- no wording suggested that signoff meant human approval or acceptance.

## Historical English example drift note

At the time of this review, the English `examples/minimal_routine_deposit/` Markdown example predated the then-current Markdown templates and used an older header/section shape.

That drift was later repaired during the pre-PR forensic sweep. The live English and Simplified-Chinese minimal examples now both follow the current Markdown template shapes while preserving their canonical JSON structures.

## Historical verdict

The specimen later passed review and end-to-end compatibility testing. Final support status is recorded in `locales/README.md`.
