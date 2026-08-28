# Document Deposit Policy

CapstanAI - LabNote workspaces are ledgers first, warehouses second.

## Preferred Formats

Prefer text-first, reviewable formats:

- Markdown `.md` for prose documents.
- JSON `.json` for structured records.
- JSONL `.jsonl` for appendable event/trace rows.
- CSV `.csv` for small tables or optional rollups.
- Plain text `.txt` for simple notes.

## Workspace Context

Do not assume the current LabNote workspace is public, private, local, remote, or tied to a particular repository name.

Before depositing documents, confirm the current workspace context. Do not store private runtime documents in a public or reference-only workspace. In a private or otherwise controlled live workspace, normal document deposits may proceed under the rules below.

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
