# Datadrop Packet Format

> Legacy note: current visitor workflow starts at `AI_ENTRYPOINT.md`, then `lobby/README_FIRST.md`, `lobby/VISITOR_CHECKLIST.md`, and for ordinary deposits `lobby/ROUTINE_DEPOSIT_QUICKSTART.md`.
> Canonical registry records are JSON-per-record under `registry/`.
> Do not follow this legacy file unless the operator explicitly instructs you to.

Use this header:

```text
# Datadrop Packet

packet_id:
source_session:
target_session:
created_by:
created_at:
status: new | in_review | answered | superseded | archived
topic:
purpose:
inputs_included:
expected_response:
constraints:
do_not_use:
related_packets:
```

Then use these sections:

```text
## Context

## Task

## Evidence / Source Material

## Questions for Receiving Session

## Output Requested

## Notes
```
