# Tagging Protocol

Prefer existing accepted tags.

Accepted tags may be found in:

```text
registry/tags/accepted/*.json
```

Proposed tags should be written to:

```text
registry/tags/proposed/<tag_slug>.json
```

If the operator supplies a tag that is not already accepted, create `registry/tags/accepted/<tag_slug>.json` only through branch + PR, with the required acceptance metadata and `acceptance_basis: operator_supplied`. Do not create it as part of a direct routine deposit.

AI-generated tags must be proposed, not accepted.

Do not move private or workspace-specific tag lists into a public/reference workspace.

Do not create near-duplicate tags.

Explain tag choices in the packet or signoff.
