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

Do not commit large raw dumps, long private transcripts, PDFs, datasets, generated bundles, logs, bulky exports, or private file collections.

If a workflow needs lots of supporting material, keep that material outside this public template repo and use a private or controlled LabNote workspace for live work. The operator should decide the approved storage and access rules before any assistant session relies on it.

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

When deploying CapstanAI - LabNote for real work, decide where bulky/private material will live before inviting multiple assistant sessions into the workflow. Do not store private runtime material in this public template repo.
