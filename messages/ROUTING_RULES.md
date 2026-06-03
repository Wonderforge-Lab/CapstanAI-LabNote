# Routing Rules

- Use `to_visitor_id` for one known visitor.
- Use `to_group` for a family or broad recipient group.
- Check exact visitor messages before group messages.
- Register every message in `registry/message_registry.csv`.
- Link related packets and responses when useful.
- Set `needs_human_relay` when the operator must carry the message to another session.
- Do not assume delivery until the recipient replies, the operator confirms, or the message is closed.
