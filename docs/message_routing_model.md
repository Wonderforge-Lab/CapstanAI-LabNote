# Message Routing Model

Messages are directed notes between visitor/session IDs.

Use a message when:

- one assistant session needs another to review something,
- a response needs follow-up,
- the operator needs a compact status note,
- a blocked task needs a human relay.

Canonical message records are JSON-per-record under `registry/messages/`. CSV files, if present, are legacy / optional rollups. The message file carries the useful text. The JSON registry record carries the state.

Do not assume the recipient saw a message until it replies, the human operator confirms delivery, or the message is closed.
