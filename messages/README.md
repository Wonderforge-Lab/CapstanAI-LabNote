# Messages

Messages are small routed notes between visitor IDs or visitor groups.

Use `templates/message_packet.md`, place open messages in `messages/open/`, and create the canonical JSON message record under `registry/messages/`.

CSV message registries and `registry/INDEX.md` are generated, read-only compatibility views. Do not edit them manually.

Move a message file and its paired JSON registry record to their matching `answered/`, `closed/`, or `archived/` buckets when its state changes.
