# Lobby

Every assistant session checks in through the lobby before handling LabNote work.

AI visitors start at:

```text
../AI_ENTRYPOINT.md
```

That file is the canonical start point. This lobby README is supporting documentation. If this file conflicts with `../AI_ENTRYPOINT.md`, follow `../AI_ENTRYPOINT.md` and report the conflict in the visit signoff.

Linear visitor flow:

1. Read `../AI_ENTRYPOINT.md`.
2. Read `VISITOR_CHECKLIST.md`.
3. Read `TAGGING_PROTOCOL.md`.
4. Reuse an existing visitor ID or register a new one.
5. Check only relevant message and notification registries.
6. Do the requested work.
7. Create a signoff.
8. Record the visit in `registry/visit_registry.csv` when the registry format is clear.
9. Stop.

The lobby is a paper trail, not a login system.
