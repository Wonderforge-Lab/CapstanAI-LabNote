<p align="center">
  <img src="assets/wonderforge_logo.png" alt="WonderForge: Imagination, Engineered." width="100%">
</p>

# OpenBridge LabNote

*A WonderForge project.*

OpenBridge LabNote is the all-in-one human-in-the-loop notebook for coordinating AI sessions through labelled packets and provenance-rich handoffs, with every decision kept traceable.

It is designed for people who work across multiple AI sessions, assistants, models, or coding helpers, but do not want to pretend those systems share a single memory, identity, or brain.

No ghosts.
No agents.
No shared-memory theatre.
No Skynet... we hope.

Just a well-labelled bridge.

## What It Does

OpenBridge LabNote gives you a simple file-based workflow for:

* passing tasks between AI sessions
* recording who said what
* tracking packets, responses, and decisions
* keeping outputs reviewable
* preserving provenance
* avoiding giant paste-dumps and context confusion
* making AI assistants identifiable contributors instead of mysterious blobs of helpful fog

It is deliberately boring in the places where boring is useful.

## What It Is Not

OpenBridge LabNote is not:

* an autonomous agent framework
* a background runner
* a shared-memory system
* a replacement for human judgement
* a secret automation layer
* a place to store credentials, private keys, tokens, or sensitive raw dumps

The human remains the decision-maker.

AI assistants may contribute, review, critique, and respond.
The operator steers the ship.

## Public Template Versus Live Workspace

OpenBridge LabNote is a public template/reference repo.

Do not store private runtime deposits, transcripts, reports, credentials, or project-specific corpora in this public repo.

For live use, create or use your own private or controlled LabNote workspace.

In a controlled live workspace, routine deposits may write directly to the default branch.

Branches/PRs are reserved for procedure, policy, code, structure, cleanup, risky/bulky imports, many existing-file edits, or explicit review.

Canonical registry records are JSON-per-record under `registry/`.

CSV registries, if present, are legacy/optional rollups.

## Core Idea

The basic pattern is:

```text
Human or AI creates a packet
↓
Packet goes into the right inbox
↓
A receiving AI session reads only what it needs
↓
The receiving session writes a response
↓
The response is reviewed
↓
The decision is recorded
```

Each handoff should leave a clear trail:

```text
packet → response → review → decision
```

## Why This Exists

AI sessions are useful, but they often suffer from:

* lost context
* repeated explanations
* unclear authorship
* messy handoffs
* overlong chats
* vague “we discussed this somewhere” memory sludge

OpenBridge LabNote gives those sessions a shared external notebook without pretending they have shared internal memory.

It helps each assistant know:

```text
Who am I in this workflow?
What has been handed to me?
Who is waiting for my answer?
What should I tell the operator?
What decision has already been made?
```

## Basic Workflow

1. Start at `AI_ENTRYPOINT.md`.
2. Read `lobby/README_FIRST.md`, then `lobby/VISITOR_CHECKLIST.md`.
3. For ordinary deposits, follow `lobby/ROUTINE_DEPOSIT_QUICKSTART.md`.
4. Create packet, response, message, signoff, or supporting Markdown/JSON files as needed.
5. Create JSON-per-record registry files under `registry/`.
6. Do not edit CSV rollups unless the operator explicitly asks.
7. The human reviews accepted, rejected, archived, or routed material.

## Repository Structure

```text
AI_ENTRYPOINT.md
  Canonical AI visitor start point.

bridge_config.json
  Machine-readable public-template policy.

bridge_protocol/
  Packet and response formats.

lobby/
  Visitor registration, check-in rules, and routine deposit quickstart.

messages/
  Directed messages between AI sessions.

notifications/
  Relay notes for the human operator.

registry/
  JSON-per-record registry files; CSV files, if present, are legacy/optional rollups.

templates/
  Copy-ready packet, response, visitor, message, and review templates.

examples/
  Fictional example packets and handoffs.

examples/minimal_routine_deposit/
  Minimal public-safe routine deposit example.

docs/
  Plain-English guides including `docs/REGISTRY_RECORDS.md`.

archive/
  Superseded or closed material.
```

## Human-In-The-Loop By Design

OpenBridge LabNote assumes that humans remain responsible for:

* deciding what is accepted
* deciding what is shared
* deciding what is acted on
* deciding what is archived
* deciding what leaves the local/private workspace

AI assistants can help keep the factory running.
They do not own the factory.

## Storage Policy

OpenBridge LabNote is the ledger, not the warehouse.

Use this repository for small, inspectable text artifacts:

* packets
* responses
* templates
* registries
* protocols
* review notes
* signoffs

Do not use this repository for large raw data, private files, credentials, logs, bulky archives, or long private transcripts.

For live work, use a private or controlled LabNote workspace. Keep bulky/private material outside this public template repo. Packets should include compact summaries and only reference supporting material according to the rules of the controlled workspace.

## Status

OpenBridge LabNote is an early public scaffold.

Current focus:

* manual handoffs
* traceable AI session coordination
* visitor/session identity
* message routing
* human review
* clean provenance

Future OpenBridge components may explore richer relay, vault, or protocol layers, but LabNote starts with the simplest useful thing:

```text
packets, provenance, replies, and decisions
```

## Motto

```text

Mind the gap. Mark the crossing.
```

## License

Apache License 2.0.
