# Branch Hygiene

Branch hygiene keeps AI-assisted repo work reviewable instead of turning the rafters into a branch-gremlin nest.

## Default rule

Create at most one task branch per visitor run.

Recommended branch pattern:

```text
labnote/<visitor_id>-<short-topic>-<YYYYMMDD>
```

Examples:

```text
labnote/example-visitor-routing-test-20260603
labnote/codex-doc-cleanup-20260603
```

## What visitors should not do

Do not create repeated scratch branches while probing write mechanics.

Do not create branches in other repositories.

Do not delete branches unless the operator explicitly approves deletion.

Do not force-push unless the operator explicitly asks and the risk is understood.

## If branch creation fails

Stop and report:

```text
branch creation failed
branch attempted
repo
reason/error
next safe option
```

## Cleanup policy

Branch cleanup is a maintenance decision.

A visiting AI session may recommend branch deletion, but should not delete branches without explicit operator approval.

## Public repo caution

For this public template repo, task branches should contain only generic, public-safe procedural changes. Do not create branches containing private reports, private visitor data, private project tags, credentials, or raw runtime material.
