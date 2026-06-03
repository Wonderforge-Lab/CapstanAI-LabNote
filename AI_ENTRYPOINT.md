# AI Entrypoint

If you are an AI session entering this repository, read this file first.

This is the canonical start point for AI visitors. If any other lobby or workflow file conflicts with this file, follow `AI_ENTRYPOINT.md` and report the conflict in your signoff.

## Repository identity

Canonical public template repo:

```text
Wonderforge-Lab/OpenBridge-LabNote
```

This repository is the public OpenBridge LabNote template and reference scaffold. It is not a private runtime workspace unless the operator explicitly says they are using this repo for a specific public test.

If the operator names a different repository, stop and use that named repository instead. Do not treat OpenBridge LabNote as the runtime workspace for a different repo.

## Workspace boundary

Default rule:

```text
Use only the repository named by the operator for the current run.
```

For runs inside this public repo:

* do not use Google Drive,
* do not use other repos,
* do not infer external storage,
* do not browse cloud folders,
* do not search for missing material elsewhere,
* do not follow public/private repo confusion into a nearby project.

External storage is denied by default and exact-reference-only. It may be used only when a packet or operator instruction explicitly names a storage reference and grants permission for that exact reference.

If source material is pasted in the prompt, treat the pasted text as the source material.

## Required visitor flow

Follow this order:

```text
0. Confirm repository identity.
1. Confirm visitor handle or create a visitor ID if the operator asks you to.
2. Read lobby/VISITOR_CHECKLIST.md.
3. Read lobby/TAGGING_PROTOCOL.md.
4. Check only messages or notifications relevant to the visitor ID, session family, supplied tags, or assigned task.
5. Create or update the appropriate packet, response, signoff, or supporting index.
6. Update registries only when the registry format is clear.
7. Create a visit signoff.
8. Tell the operator what was done, what was not done, and whether relay/action is needed.
9. Stop.
```

## Stop conditions

Stop and report instead of improvising if:

* this repository is not the repo named for the run,
* required source material is missing,
* routing is unclear,
* write permission is missing,
* an instruction asks you to use external storage without an exact reference,
* a private-runtime task appears to be aimed at the public template repo,
* the task would require deleting, renaming, or reorganising existing material without explicit approval,
* the repo procedure conflicts with the operator's hard boundary.

## Public-template rule

This public repository may document a process. It must not receive private visitor reports, private runtime data, private chat transcripts, credentials, raw bulky corpora, or project-specific handoff material unless the operator explicitly confirms the run is a public/example test and the material is public-safe.

Mind the gap. Mark the crossing.
