# Message Packet

message_id: example-message-001
from_visitor_id: chatgpt-20260602-1430-review-01
to_visitor_id: codex-20260602-1445-repo-maint-01
to_group:
created_at: 2026-06-02T14:50:00Z
status: open
reply_expected: yes
needs_human_relay: no
related_packet: example-packet-001
related_response: example-response-001
summary: Ask for a quick registry-field check.

## Message

Please check whether the example message record uses the expected canonical fields.

## Requested Action

Reply with either `looks consistent` or the field that needs correction.

## Reply Instructions

Create a response message and create or update the canonical JSON message record under `registry/messages/`. Do not edit a legacy CSV registry unless the operator explicitly asks.

## Notes

Fictional example only.
