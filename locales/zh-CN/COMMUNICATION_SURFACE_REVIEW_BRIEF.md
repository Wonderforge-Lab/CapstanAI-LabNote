# Simplified-Chinese Communication Surface Review Brief

Target locale: `zh-CN`

Review targets:

- `messages/README.md`
- `messages/MESSAGE_FORMAT.md`
- `messages/ROUTING_RULES.md`
- `notifications/README.md`

Status: language and protocol-parity review before these Chinese communication companions are marked reviewed.

## Important source note

During localization, three English communication files were found to contain stale shared-CSV registration instructions.

Those English files were repaired on the localization branch to match the repository's current canonical registry policy:

- canonical registry records are JSON-per-record,
- routine message records live under `registry/messages/`,
- routine notification records live under `registry/notifications/`,
- CSV registries, if present, are legacy / optional rollups,
- routine visitor work does not edit CSV unless the operator explicitly asks.

The Chinese drafts intentionally translate the repaired English source, not the stale CSV wording.

## Review goal

Please review these four files as one concrete message/notification workflow surface.

Natural Simplified Chinese matters, but machine invariance and behavioural parity are primary.

## 1. Messages README

Please verify that the Chinese clearly communicates:

- messages are small routed notes between visitor IDs or visitor groups,
- message files are created from `templates/message_packet.md`,
- open message files live under `messages/open/`,
- the canonical registry record is JSON under `registry/messages/`,
- CSV message registries are legacy / optional rollups,
- routine visitor work does not edit CSV unless the operator explicitly asks,
- message files move to `answered/`, `closed/`, or `archived/` as state changes.

Please check whether `未关闭的消息文件` is natural enough for `open messages` without accidentally meaning every non-closed state rather than the `open` workflow bucket.

If you recommend a change, preserve the directory semantics.

## 2. Message format

The machine-facing fields and status values must remain exactly unchanged:

```text
message_id:
from_visitor_id:
to_visitor_id:
to_group:
created_at:
status: open | acknowledged | in_progress | answered | blocked | closed | archived
reply_expected:
needs_human_relay:
related_packet:
related_response:
summary:
```

Only the human-facing Markdown headings are localized.

Please review:

```text
## 消息
## 请求的操作
## 回复说明
## 备注
```

for naturalness and fidelity.

Do not translate status values.

## 3. Routing rules

Please verify:

- `to_visitor_id` is for one known visitor/session,
- `to_group` is for a family or broad recipient group,
- exact visitor messages are checked before group messages,
- canonical JSON message records are created under `registry/messages/`,
- legacy CSV message registries are not edited during routine work unless explicitly requested,
- related packets/responses may be linked when useful,
- `needs_human_relay` is set when the human operator must carry the message to another session,
- delivery must not be assumed until the recipient replies, the operator confirms, or the message is closed.

Please stress-test the final delivery sentence. Preserve the canonical source semantics even if `closed` is not literal proof that the recipient read the message.

## 4. Notifications README

Please verify:

- notifications record manual relay requests for the human operator,
- they are used when sessions cannot directly see each other,
- notification files come from `templates/notification_request.md`,
- open notification files live under `notifications/open/`,
- canonical JSON notification records live under `registry/notifications/`,
- CSV notification registries are legacy / optional rollups,
- routine visitor work does not edit CSV unless explicitly requested.

Check consistency with reviewed `notifications/RELAY_PROTOCOL.md`, where the repository itself does not send notifications and the human operator performs the relay.

## Deliberate non-resolution: archived registry path

The source repository currently has:

- message file state/directory `archived`,
- message format state `archived`,
- canonical registry path documentation for `open`, `answered`, and `closed` message records.

This is a source-level design ambiguity, not a translation problem.

Do **not** invent a new `registry/messages/archived/` path or silently map `archived` to another registry directory during this language review.

If the Chinese wording exposes a problem caused by that source ambiguity, flag it separately as a source-level issue.

## Machine/path invariance

Do not translate or alter:

- message/notification field names,
- message status values,
- `messages/open/`, `answered/`, `closed/`, `archived/`,
- `registry/messages/`,
- `notifications/open/`,
- `registry/notifications/`,
- `templates/message_packet.md`,
- `templates/notification_request.md`,
- `to_visitor_id`,
- `to_group`,
- `needs_human_relay`.

## Review format

Please return two parts.

### Part A - overall assessment

Cover:

1. naturalness,
2. developer/agent-facing register,
3. protocol parity,
4. JSON-vs-CSV registry parity,
5. delivery/human-relay parity,
6. machine/path invariance,
7. cross-file consistency,
8. readiness.

### Part B - recommended edits

For each change:

```text
File:
Section / rule:
Current Chinese:
Recommended Chinese:
Reason:
Protocol effect: unchanged / clearer / potential behaviour change
Confidence: high / medium / low
```

End with one of:

```text
READY AFTER LISTED EDITS
READY AS WRITTEN
REQUIRES ANOTHER REVIEW PASS
```
