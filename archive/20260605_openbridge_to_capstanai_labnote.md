# 2026-06-05 Naming Migration: OpenBridge To CapstanAI - LabNote

## Old Names Retired

- OpenBridge
- OpenBridge-LabNote
- OpenBridge - LabNote
- OpenBridge LabNote
- AI Bridge Lab / AI BridgeLab as product or ecosystem naming

## New Canonical Name

- Display name: CapstanAI - LabNote
- Repo/package-safe slug: `capstanai-labnote`
- Ecosystem / project family: CapstanAI
- Notebook component: LabNote

## Reason

The rename avoids naming collision and confusion around OpenBridge while preserving the LabNote concept under the more distinctive CapstanAI ecosystem identity.

CapstanAI is named for capstan machinery:

- nautical capstan: controlled line-hauling under tension,
- engineering capstan/turret machine: modular multi-head staged work,
- project meaning: governed multi-head AI workflow system.

## What Changed

- Active public docs now identify the project as CapstanAI - LabNote.
- `bridge_config.json` now includes `project_name: "CapstanAI - LabNote"` and `project_slug: "capstanai-labnote"`.
- The active branding guide now describes CapstanAI as the ecosystem and LabNote as the first simple ledger component.
- A new accepted JSON tag record was added at `registry/tags/accepted/capstanai-labnote.json`.
- The minimal routine deposit example packet record now includes `capstanai-labnote` in its `tags` array for discoverability.

## What Was Intentionally Preserved

- Historical Git history and old commits.
- Existing packet IDs and example IDs.
- The current GitHub repository name, `Wonderforge-Lab/OpenBridge-LabNote`, unless the HITL later decides to rename it.
- The repository identifier field `public_template_repo` in `bridge_config.json`, because it currently points to the real GitHub repository.
- The old social preview asset filename `assets/openbridge_social_preview.png`; it is not referenced by active docs and can be replaced in a separate asset refresh.
- Wording in migration/provenance notes that names the retired project identity.

## Tag-Discoverability Rule

Tag record creation is not enough.

Relevant packet records must also include the tag in their `tags` arrays.

For this migration:

- `registry/tags/accepted/capstanai-labnote.json` makes the tag exist.
- `examples/minimal_routine_deposit/packet_record.json` includes `capstanai-labnote` so the example packet is discoverable by the new project tag.

No active packet registry records were found under `registry/packets/`; that folder currently contains `.gitkeep` scaffolding only.

## Deprecated Tag Handling

No existing `openbridge-labnote` JSON tag record was found.

No tag record was deleted.

If an `openbridge-labnote` tag is added later for historical reasons, it should be marked deprecated with this note:

```text
Superseded by capstanai-labnote during CapstanAI - LabNote rename.
Preserved for historical/provenance references.
```

## Remaining Legacy References

- `bridge_config.json`: `public_template_repo` still contains `Wonderforge-Lab/OpenBridge-LabNote`. Classification: repo metadata / real repository identifier, intentionally preserved.
- `registry/tags/accepted/capstanai-labnote.json`: note mentions OpenBridge-LabNote. Classification: historical/provenance, intentionally preserved.
- `examples/minimal_routine_deposit/packet_record.json`: note mentions OpenBridge-LabNote. Classification: historical/provenance, intentionally preserved.
- `docs/migrations/20260605_openbridge_to_capstanai_labnote.md`: this migration note names retired identities. Classification: historical/provenance, intentionally preserved.
- `assets/openbridge_social_preview.png`: old-name asset filename. Classification: asset metadata needing HITL follow-up if a refreshed CapstanAI social preview is wanted.

## HITL Follow-Up Items

- Decide whether to rename the GitHub repository from `Wonderforge-Lab/OpenBridge-LabNote` to a CapstanAI-aligned repository name.
- Update GitHub repository topics: the current topic list still includes `openbridge`; suggested replacements include `capstanai` and `capstanai-labnote`.
- Review the GitHub repository description and decide whether to mention CapstanAI - LabNote explicitly.
- Replace or rename the old social preview image if a refreshed CapstanAI asset is wanted.
- `v0.1.0` should remain preserved as the historical first public template release.
- The next public release should be `v0.2.0 - CapstanAI Identity Migration`.

## v0.2.0 - CapstanAI Identity Migration

This release migrates the public-facing LabNote identity from OpenBridge LabNote to CapstanAI - LabNote.

It preserves the existing human-in-the-loop workflow, JSON-per-record registry model, public/private boundary, routine deposit flow, and provenance-preserving examples.

`v0.1.0` remains preserved as the historical first public template release.
