# Messages

Messages are small routed notes between visitor IDs or visitor groups.

Use `templates/message_packet.md`, place open messages in `messages/open/`, and create the canonical JSON message record under `registry/messages/`.

CSV message registries, if present, are legacy / optional rollups. Do not edit them for routine visitor work unless the operator explicitly asks.

Move message files to `answered/`, `closed/`, or `archived/` when their state changes.
