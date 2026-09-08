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

## Human-Paced Deposit Cycle

One live workspace has one active writer at a time. People and agents may read and prepare material in parallel, but must not deposit simultaneously. The human coordinates turns across all people, sessions, tools and copies publishing to that workspace. A current-run visitor handle identifies a contributor; it is not write permission or a reserved turn. LabNote supplies no automatic queue or lock.

The cycle is: human authorizes this turn → contributor writes the complete deposit → verifies the agreed destination → reports completion → human authorizes the next turn. A failed, partial or unverified attempt must be resolved with the human before another writer starts.

## Quick Flow

1. Confirm that the expected LabNote structure is present and determine the current workspace context.
2. Confirm current-run visitor handle.
3. If no current-run visitor handle is supplied, stop and ask the human operator.
4. Before any write, confirm with the human that this specific deposit is authorized and no other writer is active. If another writer is active or the turn is unclear, stop and ask. Confirm the destination—local, GitHub or both—and use the default branch unless the operator explicitly names another branch.
5. Register visitor if missing.
6. Check only relevant messages and notifications.
7. Read `lobby/TAGGING_PROTOCOL.md` if tags are needed.
8. Read `docs/DOCUMENT_DEPOSIT_POLICY.md` if depositing documents.
9. Inspect supplied material enough to infer tags.
10. Match inferred tags to accepted registry tags.
11. Do not create an accepted tag record as part of this direct deposit. For an operator-supplied missing tag, use branch + PR with the required acceptance metadata, or ask the operator whether to record it as a proposal instead.
12. Add AI-generated tags as proposed JSON records only if useful.
13. Create packet, response, message, or signoff files.
14. Create JSON registry record files.
15. If team review or relay is needed, use messages/notifications and their JSON records under the existing routing rules. Do not edit `README_FIRST` as part of a routine direct deposit; lobby changes require branch + PR.
16. Regenerate required CSV and `registry/INDEX.md` views from the final canonical records using `scripts/generate_registry_views.py`; do not edit those views manually. If the available tools cannot do this, report the limitation and ask the human for help completing the deposit.
17. Complete and verify the whole deposit at the agreed destination as described below. Report its outcome and stop; do not start another deposit automatically.

The entrypoint, lobby front door, and visitor checklist are prerequisites for this quickstart; this file does not repeat them.

## Completion And Recovery

- A deposit includes its artifacts, required JSON records and any required regenerated views—not just the document. Before writing, inspect the current destination so prepared work is not applied over a stale copy.
- For local-only use, read back the files in the agreed local workspace and check that the records point to the intended artifacts and the required views are current. No remote push is required.
- For GitHub use, verify the files and records on the agreed remote repository and branch after publication. A draft, local commit or attempted push alone is not proof of remote completion. If both destinations were requested, verify and report each separately.
- Report any validation failures or pending/unavailable checks separately from file presence; do not call the deposit fully verified while required work or verification remains outstanding.
- If a write is rejected, interrupted or uncertain, preserve prepared work in its approved location. Tell the human what is confirmed present, what is missing or unverified, and what assistance is needed. Do not report success for a partial deposit.
- Before any human-authorized retry, inspect what landed and complete only the missing authorized work. Do not blindly replay a bundle, create duplicate records, overwrite another contribution, hand-merge generated views or force-push as recovery. If you cannot establish the destination state, stop and report that uncertainty.
- The human resolves an outstanding failed or uncertain turn before authorizing another writer. Neither a unique handle nor an apparently idle repository proves that the previous deposit completed.

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

These are operator-facing report labels, not additional JSON registry fields.

```text
visitor_id:
intended destination(s):
deposit outcome:
verification evidence:
validation/check status:
missing or unverified work:
files created:
JSON registry records created:
messages checked:
notifications checked:
review/relay message or notification paths:
relay/action needed:
signoff path:
stopped:
```
