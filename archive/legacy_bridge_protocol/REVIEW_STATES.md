# Review States

> Legacy note: current visitor workflow starts at `AI_ENTRYPOINT.md`, then `lobby/README_FIRST.md`, `lobby/VISITOR_CHECKLIST.md`, and for ordinary deposits `lobby/ROUTINE_DEPOSIT_QUICKSTART.md`.
> Canonical registry records are JSON-per-record under `registry/`.
> Do not follow this legacy file unless the operator explicitly instructs you to.

- `new`: packet has been created but not reviewed by the recipient.
- `in_review`: packet or material is being examined, or its status is uncertain.
- `answered`: a response has been written for the packet.
- `pending_review`: response is waiting for human review.
- `accepted`: reviewed material is approved for use.
- `rejected`: reviewed material should not be used.
- `superseded`: newer material replaces this item; keep it for provenance.
- `archived`: inactive material retained for reference.
