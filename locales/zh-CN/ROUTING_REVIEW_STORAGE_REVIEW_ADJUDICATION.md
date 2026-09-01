# Simplified-Chinese Routing / Review / Storage Adjudication

Status: completed

External Simplified-Chinese review returned `READY AS WRITTEN` for:

- `docs/message_routing_model.md`
- `docs/review_workflow.md`
- `docs/storage_policy.md`
- `docs/CORPUS_IMPORT_POLICY.md`

No wording changes were recommended.

## Review findings accepted

The review confirmed:

- natural Simplified-Chinese technical prose,
- developer/agent-facing register,
- protocol parity,
- modal-force parity,
- human-held final authority,
- storage/import safety parity,
- cross-file terminology consistency,
- preservation of invariant paths and machine semantics.

Specific source-level distinctions were confirmed rather than normalized away:

- `storage_policy.md` and `CORPUS_IMPORT_POLICY.md` preserve the absolute `ledger, not the warehouse` contrast;
- `DOCUMENT_DEPOSIT_POLICY.md` separately preserves its canonical `ledgers first, warehouses second` wording;
- English `should` semantics remain `应` where appropriate rather than being strengthened automatically to `必须`.

## Result

All four Chinese files are promoted from draft to reviewed.

English remains the canonical source if any future protocol conflict is discovered.
