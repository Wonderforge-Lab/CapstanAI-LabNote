# Storage Policy

CapstanAI - LabNote is the ledger, not the warehouse.

Use this repository for small text artifacts:

- packets,
- responses,
- templates,
- registries,
- visitor notes,
- review notes,
- signoffs,
- protocol docs.

Do not commit large raw dumps, long private transcripts, PDFs, datasets, generated bundles, logs, bulky exports, or private file collections unless the operator has explicitly approved the workspace and storage policy for that material.

If a workflow needs lots of supporting material, keep that material outside LabNote or in another operator-approved storage location. The operator should decide the approved storage and access rules before any assistant session relies on it.

Packets should link to heavy material by stable title, path, URL, or storage reference. The packet should also include a short summary so the receiving session knows whether it actually needs to open the larger material.

Recommended pattern for a controlled live workspace:

```text
small packet in CapstanAI - LabNote
↓
approved reference to heavy material, if needed
↓
receiving session reads the packet first
↓
large material is opened only if needed
```

Before inviting multiple assistant sessions into a workflow, confirm where bulky/private material will live and whether the current LabNote workspace is appropriate for live deposits. Public/reference workspaces must not receive private runtime material.
