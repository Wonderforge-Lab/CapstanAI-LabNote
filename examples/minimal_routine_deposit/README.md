# Minimal Routine Deposit Example

This folder shows a fictional, public-safe routine deposit using the current Markdown template shapes and canonical JSON record structure.

Example visitor: `example-visitor`

Example packet: `20260603-example-visitor-routine-test`

The example demonstrates:

- Markdown packet creation from the current `templates/datadrop_packet.md` shape.
- JSON packet record creation.
- JSON visit record creation.
- Signoff creation from the current `templates/visit_signoff.md` shape.
- Regenerated compatibility views, with no manual CSV registry edit.
- No task branch for ordinary live-workspace runtime work.

The fictional operator wrote the report; the visitor deposits it. These provenance
values describe this example, not the authorship of every future deposit.

In a disposable copy, place the packet at the JSON record's `path`, the signoff
at `signoff_path`, and the JSON files under `registry/packets/2026/` and
`registry/visits/2026/`, named after their respective IDs. Then run:

```sh
python scripts/generate_registry_views.py
python scripts/validate_repo.py --registry
python scripts/generate_registry_views.py --check
```

The validator smoke suite tests this exact copy-and-validate sequence in a
temporary workspace. Do not put test deposits in the public source repository.
