# Communication Registry Source Drift Repair

Status: **historical source-level consistency repair; later superseded in part by Registry Contract v1**

> This note records an intermediate repair made during Simplified-Chinese localization. At that point, JSON-per-record was already canonical, while CSV registries were still described as legacy / optional rollups that could be manually edited on explicit operator request. Registry Contract v1 later replaced that exception: CSV registries and `registry/INDEX.md` are now generated, read-only compatibility views and must not be edited manually.

## Finding

During Simplified-Chinese localization, three canonical English communication files were found to contain stale instructions that conflicted with the repository's newer registry policy:

- `messages/README.md`
- `messages/ROUTING_RULES.md`
- `notifications/README.md`

The stale instructions told visitors to update shared CSV registries.

At the time of this repair, canonical registry policy was defined by:

- `registry/README.md`
- `docs/REGISTRY_RECORDS.md`
- `docs/message_routing_model.md`

Those sources defined JSON-per-record registry files as canonical and CSV files as legacy / optional rollups.

## Repair at that stage

The three canonical communication files were updated so that routine work:

- created canonical JSON records under `registry/messages/` or `registry/notifications/`;
- treated CSV registries as legacy / optional rollups;
- did not edit CSV during routine visitor work unless the operator explicitly asked.

No message field names, status values, delivery semantics, message-file directories, notification-file directories, or human-relay semantics were changed by that repair.

## Current policy after Registry Contract v1

Registry Contract v1 subsequently strengthened the compatibility-view rule:

- canonical records remain JSON-per-record;
- CSV registries and `registry/INDEX.md` are generated, read-only compatibility views;
- generated views must not be edited manually;
- when canonical JSON changes, regenerate the views with `scripts/generate_registry_views.py` and commit the resulting generated output.

See `docs/REGISTRY_RECORDS.md`, `docs/registry/REGISTRY_CONTRACT_V1.md`, and `registry/README.md` for current normative behaviour.

## Deliberate non-change at the time

The message file surface included an `archived` state/directory while the then-current registry path documentation listed `open`, `answered`, and `closed` registry directories.

That separate source-level ambiguity was not expanded or resolved during the original localization repair because doing so required a registry-state design decision rather than a localization consistency fix. Registry Contract v1 later resolved the lifecycle/path model explicitly.

## Localization rule

Localized communication files should follow the current canonical English source and Registry Contract v1. Historical wording in this note is provenance, not operative guidance.
