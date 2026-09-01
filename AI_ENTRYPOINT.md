# AI Entrypoint

This repository contains a `CapstanAI - LabNote` workspace.

## Language Routing

English (`en`) is the canonical protocol language.

If the human operator has selected Simplified Chinese (`zh-CN`) for the current LabNote interaction, use `locales/zh-CN/AI_ENTRYPOINT.md` as the localized instruction surface and follow its localized reading order.

Do not infer a locale solely from repository owner, repository name, path, or other repository metadata. If no localized route has been selected, continue with the English instructions below.

Localized instruction files do not create a parallel protocol. Canonical runtime paths, JSON keys, status/enum values, IDs, tag slugs, Git behaviour, permissions, and write targets remain language-invariant. If localized wording conflicts with the English canonical protocol, the English canonical protocol controls.

Do not assume the workspace is public, private, local, remote, or tied to any particular repository name. Confirm the current workspace context from the repository and the human operator before writing.

If this is a public or reference-only workspace, do not deposit private reports, credentials, private transcripts, private visitor records, or project-specific corpora.

If this is a private or otherwise controlled live workspace, normal LabNote deposits may proceed under the rules below.

Validate LabNote by its expected structure and entrypoint, not by a fixed repository owner or slug. If the expected LabNote structure is missing or materially inconsistent, stop and report the mismatch.

No current-run visitor handle, no write.

Do not reuse visitor handles, branches, storage locations, or permissions from earlier conversation context unless the human operator explicitly confirms them for this run.

If source reports/documents are pasted or uploaded in the current prompt, treat that material as the source material.

## Routine Deposits

Routine deposits in a controlled live workspace may write directly to that workspace's default branch.

Do not create task branches for ordinary deposits.

Use branch + PR for procedure, policy, code, structure, cleanup, risky/bulky imports, many existing-file edits, or explicit review.

For ordinary deposits, use `lobby/ROUTINE_DEPOSIT_QUICKSTART.md`.

## Reading Order

1. `AI_ENTRYPOINT.md`
2. `lobby/README_FIRST.md`
3. `lobby/VISITOR_CHECKLIST.md`

Read `lobby/TAGGING_PROTOCOL.md` when tagging is needed.

Read `docs/DOCUMENT_DEPOSIT_POLICY.md` when depositing documents.

Read `docs/BRANCH_HYGIENE.md` only when the task requires a branch.
