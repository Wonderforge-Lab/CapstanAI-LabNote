# Connector Limitations

Different AI sessions may have different tool access. Some can read and write GitHub files directly. Some can only suggest patches. Some can inspect Drive or local files, and some cannot.

OpenBridge LabNote should fail closed when tool access is unclear.

## GitHub file connectors

A GitHub file connector may be good at:

* reading individual UTF-8 files,
* creating or updating individual Markdown/CSV/JSON files,
* opening pull requests,
* checking recent PRs or branches.

It may be awkward for:

* unzipping archives,
* importing whole folder trees,
* committing many binary files,
* preserving file modes,
* applying multi-file local patches atomically,
* bulk registry edits.

When a full archive or corpus import is awkward, prefer a manifest/index drop unless the operator explicitly approves a full import and the tool can safely do it.

## External storage connectors

Do not use external storage connectors unless the packet or operator instruction explicitly names the exact storage reference and grants access.

Do not search Google Drive, Dropbox, OneDrive, local mounts, or other repos just because source material appears to be missing.

## Registry edits

CSV registry edits are brittle through file APIs. Before replacing a registry file:

1. fetch the current file,
2. preserve existing rows,
3. append only the intended row,
4. avoid duplicate IDs,
5. report the update in the signoff.

If the registry format is unclear, stop and report rather than inventing a new format.

## Stop rather than improvise

If the connector cannot perform the requested operation safely, create a signoff or report explaining:

```text
what was attempted
what tool limitation appeared
what was not changed
what a human or local Codex-style run should do next
```

A stopped run with a clear explanation is a successful safety behaviour.
