# Upgrading a LabNote Workspace

CapstanAI - LabNote is a template scaffold, not a remotely controlled runtime. A live workspace does not automatically pull upstream changes.

Use this guide when you choose to adopt a newer scaffold release.

## Before You Start

1. Record the workspace’s current commit and make a recoverable backup or branch.
2. Read the target release notes and migration notes.
3. Decide which upstream changes apply to this workspace; do not overwrite local packets, records, private material, or operator-specific policy by default.
4. Perform structural, policy, script, schema, or broad cleanup changes through a branch and PR.

## Recommended Upgrade Flow

1. Fetch the released scaffold version into a separate branch.
2. Compare it against the live workspace and classify changes as safe scaffold additions, deliberate protocol migrations, or local policy conflicts.
3. Apply schema, template, and validator changes together. Do not leave a canonical registry half-migrated.
4. Run the registry validator, generated-view check, validator smoke suite, generated-view smoke suite, Markdown-link test, and bridge-config test.
5. Review the diff, including generated CSV and INDEX views.
6. Merge only after the upgrade branch is approved.

## Versioning Rules

- JSON records carry schema_version; migrate records before enabling a new schema as required CI.
- bridge_config.json carries its own schema_version.
- Generated CSV files and registry/INDEX.md are projections, not migration inputs.

## Live Data

Never treat an upgrade as permission to import, delete, or rewrite local runtime material. Preserve provenance and stop for operator direction if a migration affects private data, storage location, approval state, or record semantics.
