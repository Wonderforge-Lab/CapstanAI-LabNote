# Communication Registry Source Drift Repair

Status: **source-level consistency repair merged into the canonical English source**

## Finding

During Simplified-Chinese localization, three canonical English communication files were found to contain stale instructions that conflicted with the repository's newer registry policy:

- `messages/README.md`
- `messages/ROUTING_RULES.md`
- `notifications/README.md`

The stale instructions told visitors to update shared CSV registries.

Current canonical registry policy is defined by:

- `registry/README.md`
- `docs/REGISTRY_RECORDS.md`
- `docs/message_routing_model.md`

These define JSON-per-record registry files as canonical and CSV files as legacy / optional rollups.

## Repair

The three canonical communication files were updated so that routine work now:

- creates canonical JSON records under `registry/messages/` or `registry/notifications/`,
- treats CSV registries as legacy / optional rollups,
- does not edit CSV during routine visitor work unless the operator explicitly asks.

No message field names, status values, delivery semantics, message-file directories, notification-file directories, or human-relay semantics were changed.

## Deliberate non-change

The message file surface includes an `archived` state/directory while the current registry path documentation lists `open`, `answered`, and `closed` registry directories.

That separate source-level ambiguity was not expanded or resolved during this repair because doing so would require a new registry-state design decision rather than a localization consistency fix.

## Localization rule

Chinese communication files should translate the repaired English source, not the stale pre-repair CSV instructions.
