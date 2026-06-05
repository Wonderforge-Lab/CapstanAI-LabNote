# Bridge Protocol

> Legacy note: current visitor workflow starts at `AI_ENTRYPOINT.md`, then `lobby/README_FIRST.md`, `lobby/VISITOR_CHECKLIST.md`, and for ordinary deposits `lobby/ROUTINE_DEPOSIT_QUICKSTART.md`.
> Canonical registry records are JSON-per-record under `registry/`.
> Do not follow this legacy file unless the operator explicitly instructs you to.

This folder defines the small manual protocol behind CapstanAI - LabNote.

The protocol is intentionally plain:

- packets describe work,
- responses answer packets,
- visitors identify sessions,
- messages route follow-up,
- review records what the human operator accepted or rejected.

There are no agents, runners, webhooks, or background services here. Files are the mechanism.
