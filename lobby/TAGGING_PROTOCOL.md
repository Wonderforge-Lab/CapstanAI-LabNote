# Tagging Protocol

Tags help AI sessions route packets and responses without forcing the human operator to become a filing clerk.

## Rules

1. Prefer existing `accepted` tags from `registry/tag_registry.csv`.
2. Use operator-supplied tags even if they are not already in the registry.
3. Operator-supplied tags may be recorded as `accepted` because the operator deliberately supplied them for the run.
4. AI-generated tags must be recorded as `proposed`, not `accepted`.
5. Do not create near-duplicate tags.
6. Use `tag_slug` for machine-friendly form.
7. Use `display_name` for human-readable form.
8. Preserve project-specific display names where useful.
9. Tags may be refined by later sessions.
10. Do not turn one report into a cloud of tiny tags unless routing genuinely benefits.

## Tag registry format

Use:

```csv
tag_slug,display_name,status,scope,description,created_by,date_created,notes
```

Suggested statuses:

```text
accepted
proposed
deprecated
superseded
```

Suggested scopes:

```text
project
topic
method
artifact
visitor
workflow
```

## Creating a slug

Lowercase the display name, replace spaces and punctuation with hyphens, and remove repeated hyphens.

Examples:

```text
"Example Project" → example-project
"Human-in-the-loop" → human-in-the-loop
"Visitor routing" → visitor-routing
```

## Public repo caution

This public template repo should use generic example tags only. Do not seed it with private project tags, private visitor handles, or private runtime labels.
