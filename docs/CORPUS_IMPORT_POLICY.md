# Corpus Import Policy

OpenBridge LabNote is the ledger, not the warehouse.

This public repo is a template/reference. Do not store private runtime corpora, private transcripts, bulky archives, credentials, or project-specific runtime dumps here.

## Default Rule: Manifest First

For bulky source material in a controlled live workspace, prefer a manifest or extracted index before importing a full corpus.

A manifest may include:

- source title,
- source summary,
- packet ID,
- archive/file names,
- sizes if known,
- checksums if already available,
- short descriptions,
- stable references supplied by the operator,
- notes about what was not unpacked.

Recommended location:

```text
refs/<packet_id>/EXTRACTED_INDEX.md
```

## Full Corpus Import Requires Approval

Do not fully unpack large archives, raw corpora, or bulky file trees unless the operator explicitly approves the import and the workspace is appropriate for that material.

If approval is missing, create a manifest/index and sign off.

## Stop Conditions

Stop and report if:

- the archive is too large for safe repo import,
- the operator has not approved full import,
- the storage location is missing or unclear,
- the material appears private or sensitive,
- the repo appears to be the wrong workspace.
