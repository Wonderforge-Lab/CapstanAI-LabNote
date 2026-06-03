# Document Deposit Policy

OpenBridge LabNote workspaces are ledgers first, warehouses second.

## Preferred Formats

Prefer text-first, reviewable formats:

- Markdown `.md` for prose documents.
- JSON `.json` for structured records.
- JSONL `.jsonl` for appendable event/trace rows.
- CSV `.csv` for small tables or optional rollups.
- Plain text `.txt` for simple notes.

## Public Template Rule

Do not store private runtime documents in this public template repo.

For live LabNote work, create or use your own private or controlled workspace.

## Live Workspace Routine Deposits

In a controlled live LabNote workspace, routine document deposits do not need a branch.

Use Markdown review surrogates, manifests, JSON records, and signoffs directly on the live workspace default branch unless the operator says otherwise.

Use a branch only for bulky, risky, structural, policy, code, cleanup, or uncertain imports.

## Binary Files

Do not commit binary documents by default.

For `.docx`, `.pdf`, `.zip`, images, or other binary files:

1. If the document is mainly text, create a Markdown review surrogate.
2. Record original filename, file size if known, and SHA256 if available.
3. State that the Markdown file is a review surrogate, not the canonical binary.
4. Ask the operator before committing original binary files.
