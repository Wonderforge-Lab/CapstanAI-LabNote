# Field Decision Matrix

This matrix records the approved v1 decisions. “Artifact” means Markdown packet/signoff/notification content. “Registry” means canonical JSON.

| Record | Legacy drift | v1 decision |
|---|---|---|
| Packet | `source_session`/ `target_session` versus `source_ai`/ `target_ai` | Use session names in artifact and registry. Registry indexes identity, route, path, state, links, tags, and provenance; it does not mirror packet prose. |
| Response | `responding_session` versus `responding_ai` | Use `responding_session`. Preserve source packet, review state and derivative provenance. |
| Visit | `session_family`/ `human_relay_needed` versus `visitor_family`/ `relay_needed` | Use `session_family` and `relay_needed`. |
| Message | Markdown, JSON and CSV each retain different relationship fields | Retain distinct `to_group`, `reply_to`, `reply_expected`, `response_message_id`, `needs_human_relay`, `related_packet`, `related_response`, and `summary`. |
| Notification | From/to/message/action/summary versus requester/recipient/relay | Use `from_visitor_id`, `to_visitor_id`, `message_id`, `needs_human_action`, and `summary`. |
| Visitor | Markdown and legacy CSV only | Add canonical JSON visitor records under `registry/visitors/`. |
| Tag | JSON only, acceptance evidence absent | Keep JSON-per-record; add acceptance lineage when accepted. |

## Cross-cutting decisions

- `created_at` is the canonical RFC 3339 creation timestamp.
- A CSV `date` is derived, not a competing canonical field.
- Applicable packet, response, and message records carry tags as defined by the contract.
- Packets and responses carry provenance: creator, depositor, origin, source references, derivation, and coverage as applicable.
- Notifications inherit provenance through their required message link; visits do not carry provenance by default.
- Legacy field names are migration inputs only.
