<p align="center">
  <img src="assets/wonderforge_logo.png" alt="WonderForge: Imagination, Engineered." width="100%">
</p>

# LabNote

*Repo-native coordination for AI-assisted research and engineering.*
*A WonderForge project for the upcoming CapstanAI ecosystem.*

Most AI work starts in a blank room.

A fresh chat does not know what happened before. A coding agent may follow a task too narrowly. A browser AI may lose the thread. A local model may need the same context rebuilt by hand. Ordinary context files can help, but they often become instruction blobs: useful in small doses, brittle when they grow.

LabNote gives your AI a room with labels on the drawers.

It is a lightweight repo-based notebook and coordination layer for humans working with AI assistants, coding agents, local models, and browser-based AI sessions. It gives each AI a deterministic lobby to enter, clear rules to read, fixed places to write, tagging conventions to follow, and stop-points where it must ask the human what to do next.

LabNote is not a heavyweight local agent stack.

No daemon.
No database.
No repo-resident agent.
No model API keys.
No custom model training.
No shared-memory theatre.

Just ordinary repo files, structured so AI contributors can preserve the research signal across fresh sessions, model switches, agent handoffs, critiques, reviews, and long-running projects.

Once LabNote is set up, you can ask an AI or agent to do things like:

```text
Put this document in my LabNote repo and cross-reference it with [document name].
```

```text
Leave a critique for [AI/Agent name] about [document name].
```

```text
Register this report, tag it properly, and leave a short completion note.
```

LabNote gives the AI enough structure to act, and enough constraint to stop guessing.

## Why use LabNote?

* **Preserve research signal** across AI sessions, tools, models, and handoffs.
* **Reduce task tunnel vision** by giving agents fixed routes, not vague vibes.
* **Control completion pressure** with ask-gates, stop-points, signoffs, and human review.
* **Keep handoffs auditable** through packets, responses, reviews, decisions, and signoffs.
* **Use tag hygiene from the start** with clear conventions and a proposal path for new tags.
* **Stay repo-native and low-bloat**: LabNote stores ordinary text records, not hidden runtime machinery.
* **Avoid local-agent overhead**: no daemon, database, API server, or background automation required.
* **Work across tools**: any AI or agent that can read and write repo files can participate.
* **Keep the human in control**: the operator remains the decision-maker.

## Why not just use `AGENTS.md`?

`AGENTS.md`, `CLAUDE.md`, and similar context files are useful. LabNote can work alongside them.

But LabNote is solving a different problem.

A normal agent context file usually tells an AI about a repository: how to run tests, where key files live, what style to follow, and what commands to use. That can help, but it can also turn into a long instruction blob. As the file grows, the agent may spend more time exploring, rereading, testing, and satisfying extra requirements instead of cleanly completing the task.

LabNote is not just a bigger context file.

LabNote gives the AI a structured workflow:

* where to enter
* what to read first
* where to deposit work
* how to tag it
* how to leave a signoff
* how to hand work to another AI
* when to stop and ask the human

The difference is simple:

| Ordinary agent context file               | LabNote                                                                |
| ----------------------------------------- | ---------------------------------------------------------------------- |
| Tells the AI about the repo               | Gives the AI a route through the work                                  |
| Can become a large instruction blob       | Uses nested, role-specific instructions                                |
| Often focuses on task execution           | Also handles handoffs, review, provenance, and stop-points             |
| May increase exploration and context load | Keeps work bounded through packet routes and ask-gates                 |
| Usually lives as one file                 | Uses a small repo structure, templates, registry records, and signoffs |
| Helps one agent orient itself             | Helps many AI sessions coordinate over time                            |

LabNote is built to reduce **task tunnel vision**: the failure mode where an AI pushes too hard toward finishing the visible task and loses sight of constraints, provenance, handoff quality, or human control.

It is also designed to reduce **completion-pressure failure**: the situation where an agent treats “finish the task” as more important than “follow the route, preserve the record, and stop when the rules say stop.”

That is why LabNote uses:

* deterministic lobby entry
* nested instruction routes
* packet records
* tag hygiene
* JSON-per-record registries
* human-readable signoffs
* ask-gated stop conditions
* human-in-the-loop review

`AGENTS.md` can tell an AI what kind of project it is in.

LabNote tells the AI how to behave inside the project.


## Built around five principles

1. **Human-held authority**
   LabNote supports the human-in-the-loop. It does not replace them.

2. **Deterministic entry**
   Every AI enters through the lobby, reads the same rules, and follows the same route.

3. **Bounded action**
   The AI gets fixed targets, allowed paths, stop conditions, and ask-gates.

4. **Traceable work**
   Documents, critiques, tags, decisions, handoffs, and signoffs leave a clear trail.

5. **Growth without bloat**
   LabNote can grow into richer workflows without requiring a local daemon, database, model install, or repo-resident agent.

## Included

* Lobby system for AI and human contributors.
* Noticeboard for contributor messages and review requests.
* Contributor lookup and visit records.
* Packet, response, review, and signoff templates.
* JSON-per-record activity and packet registry.
* Dynamic tagging conventions with hygiene rules.
* Proposal path for new tags.
* Cross-reference-friendly document storage.
* Growth paths for future CapstanAI modules.

## Design stance

LabNote is deliberately boring where boring is useful.

No ghosts.
No hidden agent.
No secret automation layer.
No shared-memory theatre.
No Skynet... we hope.

The repo is the ledger.
The human is the authority.
The AI is a contributor with a route to follow.

## What it does

CapstanAI LabNote gives you a simple file-based workflow for:

* passing tasks between AI sessions
* recording who said what
* tracking packets, responses, reviews, and decisions
* keeping outputs reviewable
* preserving provenance
* avoiding giant paste-dumps and context confusion
* giving AI assistants identifiable contributor roles instead of letting them remain mysterious blobs of helpful fog

It is designed for people working across multiple AI sessions, assistants, models, or coding tools who do not want to run a full local agent stack just to keep the work coherent.

The workflow uses nested instructions, named visitors, packet records, tag hygiene, and human review to reduce task tunnel vision and completion-pressure failure.

## What it is not

CapstanAI LabNote is not:

* an autonomous agent framework
* a background runner
* a shared-memory system
* a replacement for human judgement
* a secret automation layer
* a place to store credentials, private keys, tokens, or sensitive raw dumps

The human remains the decision-maker.

AI assistants may contribute, review, critique, and respond.
The operator steers the ship.

## Public template versus live workspace

CapstanAI LabNote is a public template and reference scaffold.

Do not store private runtime deposits, transcripts, credentials, private visitor records, or project-specific corpora in this public template repo.

For live use, create or use your own private or controlled LabNote workspace.

In a controlled live workspace, routine deposits may write directly to the default branch.

Branches and pull requests are reserved for:

* procedure changes
* policy changes
* code changes
* structural changes
* cleanup
* risky or bulky imports
* many existing-file edits
* explicit review

Canonical registry records are JSON-per-record under `registry/`.

CSV registries, if present, are legacy or optional rollups.

## Core idea

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

A good handoff should carry:

* source
* status
* tags
* linked references
* contributor identity
* signoff
* next action or stop condition

## Why this exists

AI sessions are useful, but they often suffer from:

* lost context
* repeated explanations
* unclear authorship
* messy handoffs
* overlong chats
* vague “we discussed this somewhere” memory sludge
* task tunnel vision
* completion-pressure failure
* context-bloat drift

CapstanAI LabNote gives those sessions a shared external notebook without pretending they have shared internal memory.

It helps each assistant know:

```text
Who am I in this workflow?
What has been handed to me?
Where should I look?
Where should I write?
How should I tag this?
Who is waiting for my answer?
What should I tell the operator?
What decision has already been made?
When should I stop and ask?
```

## Basic workflow

1. Start at `AI_ENTRYPOINT.md`.
2. Read `lobby/README_FIRST.md`, then `lobby/VISITOR_CHECKLIST.md`.
3. For ordinary deposits, follow `lobby/ROUTINE_DEPOSIT_QUICKSTART.md`.
4. Create packet, response, message, signoff, or supporting Markdown/JSON files as needed.
5. Create JSON-per-record registry files under `registry/`.
6. Do not edit CSV rollups unless the operator explicitly asks.
7. The human reviews accepted, rejected, archived, or routed material.

## Repository structure

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

## Human-in-the-loop by design

CapstanAI LabNote assumes that humans remain responsible for:

* deciding what is accepted
* deciding what is shared
* deciding what is acted on
* deciding what is archived
* deciding what leaves the local or private workspace

AI assistants can help keep the factory running.
They do not own the factory.

## Storage policy

CapstanAI LabNote is the ledger, not the warehouse.

Use this repository for small, inspectable text artifacts:

* packets
* responses
* templates
* registries
* protocols
* review notes
* signoffs

Do not use this repository for:

* large raw data
* private files
* credentials
* logs
* bulky archives
* long private transcripts
* unreviewed sensitive dumps

For live work, use a private or controlled LabNote workspace. Keep bulky or private material outside this public template repo. Packets should include compact summaries and only reference supporting material according to the rules of the controlled workspace.

## Status

CapstanAI LabNote is an early public scaffold.

Current planned release:

```text
v0.2.0 - CapstanAI Identity Migration
```

`v0.1.0 - First Public Template` remains the historical first public template release under the OpenBridge LabNote name.

## v0.2.0 - CapstanAI Identity Migration

This release migrates the public-facing LabNote identity from OpenBridge LabNote to CapstanAI LabNote.

It preserves the existing human-in-the-loop workflow, JSON-per-record registry model, public/private boundary, routine deposit flow, and provenance-preserving examples.

`v0.1.0 - First Public Template` remains preserved as the historical first public template release.

Current focus:

* manual handoffs
* traceable AI session coordination
* visitor/session identity
* message routing
* human review
* clean provenance
* tag hygiene
* bounded workflow routes

CapstanAI may later grow a richer deterministic layer, along with relay, vault, and protocol modules. LabNote begins as the simplest useful ledger.

```text
packets, provenance, replies, and decisions
```

## Motto

```text
Mind the gap. Mark the crossing.
```

## License

Apache License 2.0.


