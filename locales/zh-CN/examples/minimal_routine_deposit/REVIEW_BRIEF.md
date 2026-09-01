# Simplified-Chinese End-to-End Routine Deposit Compatibility Review Brief

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

This is the first end-to-end compatibility specimen for the Simplified-Chinese LabNote language layer.

The test is not merely whether the Chinese reads well. It must demonstrate that a Chinese-facing workflow can produce artifacts that remain compatible with the same canonical machine protocol used by English sessions.

## Core invariants to verify

Please confirm that:

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

The files in this localized example directory are documentation/test specimens. They demonstrate what a live Chinese-language run would create at the canonical runtime paths above.

## Datadrop packet check

Please verify that the Markdown packet follows the current localized `datadrop_packet.md` template:

- title and section headings may be Chinese,
- fields remain canonical English identifiers,
- `status: new` remains an English machine state,
- evidence/source wording remains consistent with the reviewed glossary,
- no Chinese replacement is introduced for machine fields.

## Packet JSON record check

Please compare `packet_record.json` with the canonical `templates/packet_record.json` schema.

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

Please flag any key change, missing required shape, translated status, or localized runtime path.

## Visit JSON record check

Please compare `visit_record.json` with canonical `templates/visit_record.json`.

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

Again, Chinese free text in `notes` is permitted; key names and path semantics are not localized.

## Signoff check

Please verify that the signoff follows the reviewed localized `visit_signoff.md` template:

- the title correctly refers to a visitor-session signoff,
- field names remain English,
- headings may be Chinese,
- `signoff_path` remains canonical,
- no wording suggests that signoff means human approval or acceptance.

## English example drift note

The existing English `examples/minimal_routine_deposit/` Markdown example predates the current Markdown templates and uses an older header/section shape.

This Chinese specimen intentionally follows the **current canonical templates and rules**, not the stale Markdown shape of that older example.

Do not recommend copying older English field names into the Chinese example merely for superficial file-to-file similarity.

If the older English example reveals a genuine source maintenance issue, flag it separately as an English-source cleanup item.

## Review format

Please return two parts.

### Part A — overall assessment

Cover:

1. naturalness,
2. end-to-end protocol parity,
3. Markdown-template parity,
4. JSON schema compatibility,
5. machine/status/path invariance,
6. signoff semantics,
7. absence of parallel localized runtime storage,
8. whether the specimen demonstrates behavioural compatibility,
9. readiness.

### Part B — recommended edits

For each recommendation:

```text
File:
Section / field:
Current:
Recommended:
Reason:
Protocol effect: unchanged / clearer / potential behaviour change
Confidence: high / medium / low
```

Please explicitly flag any potential behaviour change.

## Final verdict

End with one of:

```text
READY AFTER LISTED EDITS
READY AS WRITTEN
REQUIRES ANOTHER REVIEW PASS
```
