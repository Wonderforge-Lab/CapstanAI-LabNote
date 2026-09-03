# LabNote

#### *A lightweight project notebook for keeping AI-assisted work coherent across sessions, tools and time.*

**English** | [简体中文](locales/zh-CN/README.md)

<p align="left">
  <img src="assets/capstanai_labnote_raven.png" alt="CapstanAI LabNote raven perched on a lab notebook with a pearl and fountain pen" width="40%">
</p>

LabNote helps you keep track of long-running projects that involve AI.

If a project outlives one chat, moves between different AI tools, gets picked up again months later, or simply becomes too complicated to hold in your head, LabNote gives the work somewhere stable to live.

It's a lightweight, repo-based notebook and coordination layer built from ordinary files. AI sessions can leave behind useful work, provenance, decisions, critiques, handoffs and next steps, so the next session does not have to start from a blank room.

You can use it with ChatGPT, Codex, Claude Code, local models, browser AIs, coding agents, or any other AI that can work with ordinary repository files.

## What can you use LabNote for?

LabNote is deliberately general-purpose.

**Software and technical projects**  
Coordinate planning, implementation, testing, review and handoffs across different AI tools.

**Research and investigations**  
Keep sources, findings, competing hypotheses, evidence and synthesis organised across separate sessions.

**Writing and creative work**  
Carry outlines, drafts, critiques, continuity notes and editorial decisions through a long project.

**Casework and life admin**  
Keep chronology, correspondence, evidence, drafts, decisions and next actions together.

**Learning and academic work**  
Preserve research notes, questions, explanations, progress and tutor-session continuity.

**Dormant projects**  
Come back after weeks or months and ask a fresh AI to bring you up to speed without rebuilding the whole context by hand.

Those are just a few examples.

If the work lasts longer than one chat, benefits from more than one AI session, or would be a drag to reconstruct from memory, then LabNote probably has a use for it.

## Why I made it

Fact is, I got sick and tired of the context window for chats filling up long before I'd even finished thrashing out an idea for a project. Sure, you can generate a handoff sheet for the next AI, but that means asking it to synthesise the whole chat, which means some finer points and even entire avenues of thought can be lost.  
At the same time, I'd keep catching myself coming up with development ideas on an unrelated chat, or even on a chat with another model. This meant that things would get scattered and I'd lose track to the point that sometimes I'd even abandon a project and start from scratch.  

To try and keep the sprawl under control, I burned time, tokens and compute, passing around progress reports, handover sheets, documents, critiques and reminders - all just to keep everything on the same page.
AI platforms have tried to address continuity with things like project areas, canvases and branching chats. They help, but they still don't do the job for me.  
I needed something simpler and more intuitive; something that would let one AI chat flow naturally into another, and would also let me keep track of projects without things turning into a full-on second-brain.  
Hence LabNote.  
What started as a fix for my own terrible project memory turned into something considerably more useful.
  
Fundamentally, using LabNote, the AI is mostly relegated to a low-token, low-compute archivist and coordinator. It's told what to read, where to put things, what to record and when to stop.

LabNote is my daily driver now. I make a new one for most substantial projects, and I even use it to dust down old work that has been sitting untouched for months.

## The basic idea

Most AI work starts in a blank room.

A fresh chat does not know what happened before. One model may not know what another decided. A coding agent may solve its narrow task but miss the wider project. Useful reasoning can disappear into an old conversation nobody wants to reread.

LabNote gives your AI a room with labels on the drawers.

A session can enter, find the relevant work, contribute what it needs to contribute, leave a traceable record, and stop.

The human remains in charge.

A typical trail is:

```text
packet → response → review → decision
```

No daemon.  
No database.  
No repo-resident agent.  
No model API keys.  
No shared-memory theatre.

Just ordinary files arranged so useful project knowledge survives the chat that created it.

## How it works

That simple trail expands into a repeatable handoff:

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

A good handoff carries enough provenance and status to show where the work came from, what happened to it, and what should happen next.

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

## Get LabNote

If you are already talking to an AI, the easiest starting point is:

```text
Help me set up CapstanAI LabNote for this project. First work out what access you have, then recommend the simplest safe route for me. I want you to explain any terminal commands before I run them.
```

Common routes:

| Environment | Suggested route |
| --- | --- |
| Browser AI + terminal available | AI-guided local clone, then connect to a private GitHub repo if wanted |
| Browser AI without terminal access | GitHub **Use this template** route |
| Coding agent or terminal-capable AI | Agent clones/copies and configures the workspace, subject to operator approval |
| Local-only project | Clone or copy locally; no remote required |

See [`docs/ACQUISITION.md`](docs/ACQUISITION.md) for exact beginner-friendly steps and terminal guidance.

The acquisition method does not change how LabNote works after the copy exists.

### Public source, live workspace

The canonical CapstanAI LabNote repository is public so people can inspect and acquire the scaffold. A copied workspace may be private, public, local-only, or otherwise controlled. Portable LabNote workflow files do not depend on a fixed repository owner, slug, or visibility.

If the current workspace is public or reference-only, do not deposit private runtime material there. Controlled live workspaces follow the runtime and storage rules linked below.

## First use

1. Acquire the workspace.
2. Give your AI `AI_ENTRYPOINT.md` as its starting point.
3. Confirm the workspace context if the AI asks.
4. Let the AI follow the LabNote lobby from there.

No repository rename or LabNote identity-file edit should be required before first use. You do not need to learn the whole filing system before using it.

See [`docs/quickstart.md`](docs/quickstart.md) for the longer walkthrough.

## Why it helps

* **Preserve continuity** across fresh chats, models, tools, coding agents, and dormant projects.
* **Cut coordination admin** by letting AI sessions leave structured work for each other instead of making the human relay everything by hand.
* **Keep work auditable** through labelled packets, provenance, responses, reviews, visit records, and signoffs.
* **Bound AI behaviour** with deterministic entry, fixed routes, ask-gates, stop-points, and human review.
* **Stay repo-native and low-bloat** so any capable AI that can read and write ordinary repo files can participate without a daemon, database, or hidden runtime.

## Why not just use `AGENTS.md`?

`AGENTS.md`, `CLAUDE.md`, and similar context files are useful. LabNote can work alongside them, but it is solving a different problem.

A typical agent context file usually tells an AI about a repository: how to run tests, where key files live, what style to follow, and what commands to use. That can help, but it can also turn into a long instruction blob as the project grows.

LabNote is not just a bigger context file. It gives the AI a structured workflow: where to enter, what to read first, where to deposit work, how to tag it, how to sign off, how to hand work onward, and when to stop and ask the human.

| Ordinary agent context file | LabNote |
| --- | --- |
| Tells the AI about the repo | Gives the AI a route through the work |
| Can become a large instruction blob | Uses nested, role-specific instructions |
| Often focuses on task execution | Also handles handoffs, review, provenance, and stop-points |
| May increase exploration and context load | Keeps work bounded through packet routes and ask-gates |
| Usually lives as one file | Uses a small repo structure, templates, registry records, and signoffs |
| Helps one agent orient itself | Helps many AI sessions coordinate over time |

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

## Where to go next

LabNote is the ledger, not the warehouse. Keep the workspace focused on small, inspectable records and approved references to heavier material. Do not store credentials, private keys, or tokens in LabNote.

| Area | Need | Read |
| --- | --- | --- |
| **Start** | Set up LabNote | [`docs/ACQUISITION.md`](docs/ACQUISITION.md) |
| **Start** | Beginner walkthrough | [`docs/quickstart.md`](docs/quickstart.md) |
| **Start** | Give an AI its starting instructions | [`AI_ENTRYPOINT.md`](AI_ENTRYPOINT.md) |
| **Work** | Make a normal deposit | [`lobby/ROUTINE_DEPOSIT_QUICKSTART.md`](lobby/ROUTINE_DEPOSIT_QUICKSTART.md) |
| **Work** | Understand visitor/session identity | [`docs/visitor_lobby_model.md`](docs/visitor_lobby_model.md) |
| **Work** | Route messages between sessions | [`docs/message_routing_model.md`](docs/message_routing_model.md) |
| **Work** | Review a response or decision | [`docs/review_workflow.md`](docs/review_workflow.md) |
| **Reference** | Branch and PR rules | [`docs/BRANCH_HYGIENE.md`](docs/BRANCH_HYGIENE.md) |
| **Reference** | Registry records and paths | [`docs/REGISTRY_RECORDS.md`](docs/REGISTRY_RECORDS.md) |
| **Reference** | Storage rules | [`docs/storage_policy.md`](docs/storage_policy.md) |
| **Reference** | Document and binary deposit rules | [`docs/DOCUMENT_DEPOSIT_POLICY.md`](docs/DOCUMENT_DEPOSIT_POLICY.md) |

Detailed runtime rules live in those canonical files rather than being duplicated here.

## Status

Latest published scaffold release: `v0.3.1 - Registry Guidance Cleanup`.

This patch release:

* removes stale live guidance that still allowed manual CSV registry edits,
* marks the localization source-drift note and pre-v1 registry audit as historical provenance,
* leaves Registry Contract v1, schemas, runtime paths, machine fields, statuses, localization protocol, and generated views unchanged.

`v0.3.0 - Registry v1 and Simplified Chinese Revision` remains the feature baseline beneath this patch.

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
