# Datadrop Packet Format

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
