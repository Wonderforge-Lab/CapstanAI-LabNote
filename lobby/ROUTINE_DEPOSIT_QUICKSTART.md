# Routine Deposit Quickstart

Use this file for ordinary visitor deposits in a live CapstanAI - LabNote workspace.

A routine deposit means a visitor is placing a normal packet, response, message, signoff, or small supporting Markdown/JSON record into a LabNote workspace.

## Workspace Context

Do not assume this copy is public, private, local, remote, or tied to a particular repository name.

Before writing, confirm that it is a private or otherwise controlled live workspace. If it is public or reference-only, do not deposit private runtime material.

## Default Write Mode For Live Workspaces

Routine deposits in a controlled live workspace may write directly to that workspace's default branch.

Do not create a task branch for ordinary deposits.

Use a branch + PR only for procedure, policy, repo structure, code/script changes, cleanup, risky/bulky imports, many existing-file edits, or explicit human review.

## Quick Flow

1. Confirm that the expected LabNote structure is present and determine the current workspace context.
2. Confirm current-run visitor handle.
3. If no current-run visitor handle is supplied, stop and ask the human operator.
4. Use the default branch unless the operator explicitly names another branch.
5. Register visitor if missing.
6. Check only relevant messages and notifications.
7. Read `lobby/TAGGING_PROTOCOL.md` if tags are needed.
8. Read `docs/DOCUMENT_DEPOSIT_POLICY.md` if depositing documents.
9. Inspect supplied material enough to infer tags.
10. Match inferred tags to accepted registry tags.
11. Add operator-supplied missing tags as accepted JSON records.
12. Add AI-generated tags as proposed JSON records only if useful.
13. Create packet, response, message, or signoff files.
14. Create JSON registry record files.
15. Do not edit CSV unless the operator explicitly asks.
16. Add a `README_FIRST` notice if team review or relay is needed.
17. Report files created and stop.

The entrypoint, lobby front door, and visitor checklist are prerequisites for this quickstart; this file does not repeat them.

## Canonical Naming

Use this pattern unless the operator supplies a better one:

```text
packet_id:
YYYYMMDD-<visitor_id>-<short-topic>

packet:
datadrops/shared/inbox/<packet_id>.md

packet record:
registry/packets/YYYY/<packet_id>.json

visit_id:
<packet_id>-visit

visit record:
registry/visits/YYYY/<visit_id>.json

signoff:
responses/signoffs/<packet_id>-signoff.md
```

## Minimal Final Report To Operator

```text
visitor_id:
files created:
JSON registry records created:
messages checked:
notifications checked:
README_FIRST notice added:
relay/action needed:
signoff path:
stopped:
```
