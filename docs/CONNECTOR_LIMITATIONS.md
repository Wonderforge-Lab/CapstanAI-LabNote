# Connector Limitations

Different AI sessions may have different tool access. Some can read and write individual repository files directly. Some can only suggest patches. Some cannot safely handle multi-file archives or large imports.

OpenBridge LabNote should fail closed when tool access is unclear.

## GitHub File Connectors

A GitHub file connector may be good at:

- reading individual UTF-8 files,
- creating or updating individual Markdown or JSON files,
- opening pull requests,
- checking recent PRs or branches.

It may be awkward for:

- unzipping archives,
- importing whole folder trees,
- committing many binary files,
- preserving file modes,
- applying multi-file local patches atomically,
- bulk registry edits.

When a full archive or corpus import is awkward, prefer a manifest/index drop unless the operator explicitly approves a full import and the tool can safely do it.

## Registry Edits

Shared CSV edits are brittle through file APIs. Prefer JSON-per-record registry files for ordinary visitor work.

If the registry format or path is unclear, stop and report rather than inventing a new format.

## Stop Rather Than Improvise

If the connector cannot perform the requested operation safely, create a signoff or report explaining:

```text
what was attempted
what tool limitation appeared
what was not changed
what a human or local coding run should do next
```

A stopped run with a clear explanation is a successful safety behaviour.
