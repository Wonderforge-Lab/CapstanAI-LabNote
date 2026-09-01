# Simplified-Chinese Communication Surface Review Adjudication

Locale: `zh-CN`

Review target cluster:

- `messages/README.md`
- `messages/MESSAGE_FORMAT.md`
- `messages/ROUTING_RULES.md`
- `notifications/README.md`

External reviewer verdict: `READY AFTER LISTED EDITS`

## Accepted edits

### 1. `MESSAGE_FORMAT.md` title

Changed:

```text
消息工作包
```

to:

```text
消息格式
```

Reason: `MESSAGE_FORMAT.md` defines the message layout rather than a LabNote packet artifact. The change avoids conflating the file with the frozen `工作包（packet）` concept.

Protocol effect: unchanged; terminology clarified.

### 2. `messages/README.md` open-state wording

Changed:

```text
把未关闭的消息文件放入 messages/open/
```

to:

```text
将状态为 open 的消息文件放入 messages/open/
```

Reason: `未关闭` could include `acknowledged`, `in_progress`, `blocked`, or `answered`. The canonical directory instruction refers specifically to the `open` state/bucket.

Protocol effect: clearer and less overbroad; no intended behaviour change.

## Confirmed without edit

The reviewer confirmed:

- JSON-per-record is the canonical routine registry form;
- CSV registries are legacy/optional rollups;
- `to_visitor_id`, `to_group`, and `needs_human_relay` retain their distinct roles;
- delivery is not assumed before recipient reply, operator confirmation, or message closure;
- machine field names, status values, paths, and template paths remain unchanged;
- human relay remains a human/operator action.

## Source-level ambiguity deliberately not resolved

The source repository has an `archived` message file state/directory while canonical registry documentation currently lists `open`, `answered`, and `closed` message registry paths.

Localization did not invent a `registry/messages/archived/` path or silently remap the state. This remains a source-level protocol question for separate adjudication.

## Result

The Simplified-Chinese communication surface is reviewed after the two accepted wording edits.

If any localized text conflicts with the English canonical protocol, the English canonical source remains authoritative.
