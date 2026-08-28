# AI Response Packet Format

> Legacy note: current visitor workflow starts at `AI_ENTRYPOINT.md`, then `lobby/README_FIRST.md`, `lobby/VISITOR_CHECKLIST.md`, and for ordinary deposits `lobby/ROUTINE_DEPOSIT_QUICKSTART.md`.
> Canonical registry records are JSON-per-record under `registry/`.
> Do not follow this legacy file unless the operator explicitly instructs you to.

Use this header:

```text
# AI Response Packet

response_id:
responding_session:
source_packet_id:
created_at:
status: pending_review | accepted | rejected | archived
confidence: low | medium | high
response_type: answer | critique | synthesis | counterproposal | review
```

Then use these sections:

```text
## Summary

## Response

## Assumptions

## Uncertainties

## Recommended Next Step

## Files To Promote / Archive

## Housekeeping Notes
```
