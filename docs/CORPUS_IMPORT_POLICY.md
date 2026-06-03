# Corpus Import Policy

OpenBridge LabNote is the ledger, not the warehouse.

This policy exists so visiting AI sessions do not unpack large archives, raw corpora, or bulky file trees into a repository just because they can see a zip or a long report.

## Default rule: manifest first

By default, visitors may create an index or manifest for supplied source material.

A manifest may include:

* source title,
* source summary,
* packet ID,
* archive/file names,
* sizes if known,
* checksums if already available,
* short descriptions,
* stable references supplied by the operator,
* notes about what was not unpacked.

Recommended location:

```text
refs/<packet_id>/EXTRACTED_INDEX.md
```

## Full corpus import requires approval

Do not fully unpack large archives, zip files, raw corpora, or bulky file trees into the repo unless the operator explicitly says:

```text
full corpus import approved
```

or gives an equally clear instruction.

If approval is missing, create a manifest/index and sign off.

## External storage

External storage is denied by default and exact-reference-only.

Use external storage only when the packet or operator instruction explicitly names the exact reference and grants access.

Do not:

* search Google Drive,
* browse cloud folders,
* infer storage locations,
* follow unrelated links,
* look in another repo for missing files.

## Public-template caution

This public repo should not receive private corpora, private chat transcripts, credentials, bulky archives, or project-specific runtime dumps.

For examples, use fictional or public-safe material.

## Stop conditions

Stop and report if:

* the archive is too large for safe repo import,
* the operator has not approved full import,
* the storage location is missing or unclear,
* the material appears private or sensitive,
* the repo appears to be the wrong workspace.
