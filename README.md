# OpenBridge LabNote

OpenBridge LabNote is the all-in-one human-in-the-loop notebook for coordinating AI sessions through labelled packets and provenance-rich handoffs, with every decision kept traceable.

It is designed for people who work across multiple AI sessions, assistants, models, or coding agents, but do not want to pretend those systems share a single memory, identity, or brain.

No ghosts.
No agents.
No shared-memory theatre.
No Skynet...we hope.

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

1. Create a packet from a template.
2. Put it in the appropriate inbox.
3. Add or update the packet registry.
4. The receiving AI reads the packet.
5. The receiving AI writes a response.
6. The response is placed in pending review.
7. The human reviews the response.
8. The response is accepted, rejected, archived, or routed onward.
9. The registry is updated.

## Planned Structure

```text
bridge_protocol/
  Packet and response formats.

lobby/
  Visitor registration and check-in rules for AI sessions.

messages/
  Directed messages between AI sessions.

notifications/
  Relay notes for the human operator.

registry/
  CSV ledgers for packets, responses, visitors, messages, notifications, and visits.

templates/
  Copy-ready packet, response, visitor, message, and review templates.

examples/
  Fictional example packets and handoffs.

docs/
  Plain-English guides and storage policy.

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

Use this repository for small, inspectable text artifacts:

* packets
* responses
* templates
* registries
* protocols
* review notes
* signoffs

Do not use this repository for large raw data, private files, credentials, logs, or bulky archives.

Large supporting material should live in an external storage area such as Google Drive, Dropbox, local storage, or another blob vault. Link to it from the relevant packet when needed.

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


