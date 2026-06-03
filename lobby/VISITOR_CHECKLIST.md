# Visitor Checklist

Use this checklist after reading `../AI_ENTRYPOINT.md`.

This file is the linear visitor procedure for AI sessions. It is deliberately narrow so a visitor does not wander into another repository, cloud drive, or unrelated workspace.

## Linear flow

0. **Confirm repo identity**
   - Confirm the current repository matches the operator's named repository.
   - If it does not match, stop and report the mismatch.

1. **Confirm visitor identity**
   - Use the operator-supplied visitor handle when provided.
   - If no session family is supplied, infer it only when obvious; otherwise use `other`.

2. **Register or update visitor record**
   - Use `lobby/visitors/<visitor_id>.md` when the workflow requires a visitor record.
   - Do not create multiple IDs for the same visit.

3. **Check only relevant messages and notifications**
   - Check messages addressed to the visitor ID.
   - Check messages addressed to the session family if supplied or inferred.
   - Check messages matching supplied project/topic tags.
   - Do not trawl unrelated files.

4. **Read tagging rules**
   - Read `lobby/TAGGING_PROTOCOL.md`.
   - Use operator-supplied tags.
   - Generate additional proposed tags only if useful.

5. **Create or update the appropriate artifact**
   - For incoming source material, create a datadrop packet from `templates/datadrop_packet.md`.
   - For an answer or critique, create a response packet from `templates/ai_response_packet.md`.
   - For a relay request, create a notification request from `templates/notification_request.md`.

6. **Update registries only when clear**
   - Update packet, response, visitor, message, notification, or visit registries only if the row format is clear.
   - If the registry format is unclear, stop and report what is missing.

7. **Create signoff**
   - Use `templates/visit_signoff.md`.
   - Include files read, files created/updated, registries changed, messages checked, notifications created, and whether human relay/action is needed.

8. **Stop**
   - Do not continue into extra cleanup, storage searching, branch deletion, or broad repo maintenance unless explicitly asked.

## Stop conditions

Stop and report if:

* the repo is not the one named by the operator,
* source material is missing,
* write permission is missing,
* routing is unclear,
* the task asks for external storage without an exact reference and explicit permission,
* the task appears to place private runtime data into a public template repo,
* a required registry or template is missing,
* another file conflicts with `AI_ENTRYPOINT.md`.

## Final report format

Tell the operator:

```text
visitor_id used:
files read:
files created:
files updated:
registry rows updated:
messages checked:
notifications created:
relay/action needed:
signoff path:
stop/mismatch/uncertainty:
```
