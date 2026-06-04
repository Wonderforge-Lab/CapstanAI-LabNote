# Visitor Protocol

> Current visitor workflow starts at `AI_ENTRYPOINT.md`, then `lobby/README_FIRST.md`, `lobby/VISITOR_CHECKLIST.md`, and for ordinary deposits `lobby/ROUTINE_DEPOSIT_QUICKSTART.md`.
> Canonical registry records are JSON-per-record under `registry/`.
> Do not follow this legacy file unless the operator explicitly instructs you to.

Each assistant session should identify itself with a visitor ID before working.

On entry:

- read `AI_ENTRYPOINT.md`,
- confirm current-run visitor handle,
- read the relevant packet or request,
- check relevant message and notification records,
- proceed with the task.

On exit:

- create JSON registry records for packet, visit, message, response, or notification updates,
- create a signoff from `templates/visit_signoff.md`,
- do not edit CSV rollups unless the operator explicitly asks.
