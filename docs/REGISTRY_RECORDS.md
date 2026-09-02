# Registry Records

Canonical registry records are one JSON file per record. JSON is the structured index, state, relationship, and provenance envelope for its linked Markdown artifact; it is not required to duplicate the artifact body.

The authoritative field, status, lifecycle, provenance, and compatibility rules are in [Registry Contract v1](registry/REGISTRY_CONTRACT_V1.md). The JSON schemas under `registry/schemas/` and `scripts/validate_repo.py` enforce that contract.

## Canonical Paths

Packets:

```text
registry/packets/<year>/<packet_id>.json
```

Responses:

```text
registry/responses/<year>/<response_id>.json
```

Visits:

```text
registry/visits/<year>/<visit_id>.json
```

Visitors:

```text
registry/visitors/<visitor_id>.json
```

Messages:

```text
registry/messages/open/<message_id>.json
registry/messages/answered/<message_id>.json
registry/messages/closed/<message_id>.json
registry/messages/archived/<message_id>.json
```

Notifications:

```text
registry/notifications/open/<notification_id>.json
registry/notifications/delivered/<notification_id>.json
registry/notifications/closed/<notification_id>.json
```

Tags:

```text
registry/tags/proposed/<tag_slug>.json
registry/tags/accepted/<tag_slug>.json
registry/tags/deprecated/<tag_slug>.json
```

The status determines the message, notification, or tag storage bucket. Use the per-record-type lifecycle table in the contract; do not invent a new status or directory.

## Visitor Rule

For ordinary visitor work:

```text
create one canonical JSON record
create or update its linked artifact as needed
validate the record
mention it in the signoff
do not edit a CSV registry
```

Use the corresponding file in `templates/` as the starting envelope. The checked, public-safe record/artifact pairs under `examples/contract_v1/` show complete packet, response, message, and visit records.

## Tags

Tags are controlled vocabulary records, not free text.

- A session-created tag begins under `registry/tags/proposed/`.
- A proposed tag cannot become accepted in the same change set.
- An operator-supplied tag may be accepted directly only with the required acceptance metadata and `acceptance_basis: operator_supplied`. It is a control-plane change and uses branch + PR.
- Records may use only tags that resolve to a proposed or accepted tag record.

## Generated Compatibility Views

The CSV registries and `registry/INDEX.md` are generated, read-only compatibility views. They are not canonical and must not be edited manually.

When canonical JSON changes, regenerate the views locally with `scripts/generate_registry_views.py` and commit the resulting views. CI checks that committed views match the canonical JSON records.
