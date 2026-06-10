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

## How it works

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

Each handoff leaves a clear trail:

```text
packet → response → review → decision
```

A good handoff carries: source, status, tags, linked references, contributor identity, signoff, and a next action or stop condition.

## Getting started

1. Click **Use this template** to create your own private or controlled LabNote workspace.
2. Open `AI_ENTRYPOINT.md` and hand it to your AI session as the starting point.
3. Follow the lobby — `lobby/README_FIRST.md` → `lobby/VISITOR_CHECKLIST.md` → `lobby/ROUTINE_DEPOSIT_QUICKSTART.md`.

See [`docs/quickstart.md`](docs/quickstart.md) for a full walkthrough.

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

docs/
  Plain-English guides including docs/quickstart.md and docs/REGISTRY_RECORDS.md.

archive/
  Superseded or closed material.
```

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

For live work, use a private or controlled LabNote workspace. Keep bulky or private material outside this public template repo.

## Status

Current release: `v0.2.0 - CapstanAI Identity Migration`

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
