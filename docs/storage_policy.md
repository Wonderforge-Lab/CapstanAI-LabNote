# Storage Policy

OpenBridge LabNote is the ledger, not the warehouse.

Use this repository for small text artifacts:

- packets,
- responses,
- templates,
- registries,
- visitor notes,
- review notes,
- signoffs,
- protocol docs.

Do not commit large raw dumps, long private transcripts, PDFs, datasets, generated bundles, logs, bulky exports, or private file collections.

If a workflow needs lots of supporting material, put that material in external storage controlled by the operator. This might be Google Drive, Dropbox, OneDrive, S3-compatible storage, a local folder, a network share, or another blob vault that the relevant assistant/session can access.

Packets should link to heavy material by stable title, path, URL, or storage reference. The packet should also include a short summary so the receiving session knows whether it actually needs to open the larger material.

Recommended pattern:

```text
small packet in OpenBridge LabNote
↓
link or reference to heavy material in external storage
↓
receiving session reads the packet first
↓
large material is opened only if needed
```

When deploying OpenBridge LabNote for real work, decide where bulky/private material will live before inviting multiple assistant sessions into the workflow.
