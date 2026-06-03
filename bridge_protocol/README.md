# Bridge Protocol

This folder defines the small manual protocol behind OpenBridge LabNote.

The protocol is intentionally plain:

- packets describe work,
- responses answer packets,
- visitors identify sessions,
- messages route follow-up,
- review records what the human operator accepted or rejected.

There are no agents, runners, webhooks, or background services here. Files are the mechanism.
