# Visitor Lobby Model

The lobby gives assistant sessions a public, file-based way to say "this is who is speaking in this workflow."

A visitor is not a person. It is a labelled session identity used for routing and provenance.

Visitors:

- use the current-run visitor handle supplied or explicitly confirmed by the human operator,
- register a visitor profile if one is needed,
- check messages on entry,
- do the requested work,
- record created or answered messages,
- sign off before leaving.

Do not invent a visitor handle or silently reuse one from earlier conversation context.

A canonical visitor registration lives at `registry/visitors/<visitor_id>.json`. A small optional visitor profile may live under `lobby/visitors/` for human-facing orientation; it is not a substitute for the canonical registration record. Keep optional profiles small and generic.
