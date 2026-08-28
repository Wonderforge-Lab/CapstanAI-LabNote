# LabNote

#### *For people using multiple AI sessions, Claude Code, Codex, local LLMs, or browser AIs who need handoffs, audit trails, and continuity without building a full agent stack*

<p align="left">
  <img src="assets/capstanai_labnote_raven.png" alt="CapstanAI LabNote raven perched on a lab notebook with a pearl and fountain pen" width="40%">
</p>

LabNote is a lightweight repo-based notebook and coordination layer for humans working across AI sessions, coding agents, local models, and browser AIs. It keeps handoffs, provenance, and project continuity in ordinary files, without requiring a full agent stack.

Fact is, these days I'm a one man band with a terrible memory, and I'm disgracefully disorganised.  
For me, even a small project can burn out and bloat a chat way before the project is finished, and even a medium-size project can involve two or more models and coding agents, and usually spans several chats.

So I often ended up spending too much time as a messenger and coordinator, as I burned tokens and compute passing around updates, progress reports, results of adversarial sweeps, hand-off sheets, etc, just to make sure all the AI elements were up to speed and on the same page.

To keep track of things, I automated big chunks of that admin using deterministic rules, indexed storage and tagging. The AI is mostly relegated to a low-token and low-compute archivist and workflow nudger, getting told what to do, where to put it, and when to stop, so there's little room for the AI to pull any stunts or get sweaty.

So LabNote was made in response to the need for an admin tool for a specific job, because I kept losing track of things, although it became quite a bit more useful than that.  
Because it lets a chat specialise in a single part of a project while pooling with other chats on the same LabNote project repo, it helps span some of the distance between what an individual can do, and what an entire office or lab can.

It's my daily driver now, and I don't start anything without it. I make a new LabNote at the start of each project nowadays, and even use it to dust down old projects. LabNote makes it a million miles easier for me to transition a project from inception to planning and development, and then on to production and revision rounds.

Just set up your own LabNote repo, and take it from there.

**So you bloated out a chat part-way through a project?**  
That's ok. Just open a new one and point it at LabNote for a seamless handover.  
**Sick of manually passing documents/text/reports/plans/etc between Codex and ChatGPT, or between different models?**  
Get them to coordinate and work off the same song-sheet using LabNote instead. Save your time and tokens.  
**You're using AI to find out if onion is bad for your dog [it is] and you get an idea for a project you're working on**  
No need to drop out of the chat you're in. Just tell the AI to drop your idea into LabNote where you can pick it up later.  
**You had to stop working on a project a few months before and you can't remember the details**  
"Hey, pls go into LabNote [project name] and bring me up to speed."

## What LabNote is

Most AI work starts in a blank room.

A fresh chat does not know what happened before. A coding agent may follow a task too narrowly. A browser AI may lose the thread. A local model may need the same context rebuilt by hand. Ordinary context files can help, but they often become instruction blobs: useful in small doses, brittle when they grow.

LabNote gives your AI a room with labels on the drawers.

It gives each AI a deterministic lobby to enter, clear rules to read, fixed places to write, tagging conventions to follow, and stop-points where it must ask the human what to do next.

LabNote is not a heavyweight local agent stack.

No daemon.  
No database.  
No repo-resident agent.  
No model API keys.  
No custom model training.  
No shared-memory theatre.

It is not an autonomous agent framework. It is ordinary repo files, structured so AI contributors can preserve the research signal across fresh sessions, model switches, agent handoffs, critiques, reviews, and long-running projects.

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

A good handoff carries enough provenance and status to show where the work came from, what happened to it, and what should happen next.

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

A normal agent context file usually tells an AI about a repository: how to run tests, where key files live, what style to follow, and what commands to use. That can help, but it can also turn into a long instruction blob as the project grows.

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

Latest published scaffold release: `v0.2.0 - CapstanAI Identity Migration`.

Current canonical development focus includes:

* portable acquisition and bootstrap,
* traceable multi-session coordination,
* visitor/session identity and message routing,
* human review, provenance, and tag hygiene,
* bounded workflow routes.

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
