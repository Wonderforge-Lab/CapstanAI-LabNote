# Visitor Lobby Model

The lobby gives assistant sessions a public, file-based way to say "this is who is speaking in this workflow."

A visitor is not a person. It is a labelled session identity used for routing and provenance.

Visitors:

- register or reuse a visitor ID,
- check messages on entry,
- do the requested work,
- record created or answered messages,
- sign off before leaving.

Visitor profiles can live under `lobby/visitors/`. Keep them small and generic.
