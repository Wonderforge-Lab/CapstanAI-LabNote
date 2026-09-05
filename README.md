# CapstanAI LabNote

#### *A simple, file-based ledger for AI-assisted work that outlives the chat.*

CapstanAI is the project name; LabNote is its practical, file-based ledger.

**English** | [简体中文](locales/zh-CN/README.md)

<p align="center">
  <img src="https://img.shields.io/badge/license-Apache--2.0-blue" alt="Apache License 2.0">
  <img src="https://img.shields.io/badge/runtime-none-informational" alt="No LabNote runtime">
</p>

<p align="center">
  <img src="assets/capstanai_labnote_raven.png" alt="CapstanAI LabNote raven perched on a lab notebook with a pearl and fountain pen" width="30%">
</p>

Most AI work starts in a blank room.

A fresh chat often does not know what happened before. One model may not know what another decided. A coding agent may finish its own task without seeing the wider project. Useful work gets stranded in old conversations that nobody wants to reconstruct by hand.

**LabNote gives your AI a room with labels on the drawers.**

It is a lightweight project notebook built from ordinary files. Work, sources, decisions, critiques, handoffs and next steps have somewhere stable to live, so a new session can find the thread instead of starting again.

Set it up once, point each AI at the same entrance, and let the ledger carry the continuity.

With suitable access to the files, LabNote works with browser AIs, coding agents and local models. If an AI cannot reach the files itself, it can still guide you through getting a copy and setting it up.

## What LabNote does well

You may already be running a rough version of this yourself: pasting summaries between chats, writing handoff notes, keeping scattered folders, bookmarking old conversations, and trying to remember which AI was told what.

LabNote turns that repeated coordination work into a visible route through the project. It can be a task list, a handoff ledger, a small working library, an audit trail, or a deliberate drop point between sessions.

It gives a project a durable place to:

- keep the tasks, sources, decisions and next actions that matter;
- pass work between sessions without repeating the whole brief;
- keep critique and review attached to the work they concern; and
- return after a gap with a clear trail instead of a pile of old chats.

LabNote is one part of your stack, not a replacement for your folders, version control, drives or project tools. You, your chosen AI tools, and the workspace each have a role. You decide what belongs in the record, what needs review, and what happens next.

Give each meaningful project its own named LabNote copy. Start with a few tasks, one handoff or a small document trail; let it grow into a fuller record only when the work calls for it.

When a chat ends, a tool changes, or a project goes quiet, the files remain. Kept under normal version control and backup, they give the next session a way back into the work, and a map for rebuilding it.

## Get LabNote

> **Already looking at your own copy?** You have LabNote already—start at
> [`AI_ENTRYPOINT.md`](AI_ENTRYPOINT.md).

If you are already talking to an AI, this is the easiest place to begin. Copy and paste:

```text
Help me set up CapstanAI LabNote for this project. First work out what access you have, then recommend the simplest safe route for me. I want you to explain any terminal commands before I run them.
```

Or make your own copy directly:

| Where you want it | What to do |
| --- | --- |
| **In your own GitHub repository** | [Use this template](https://github.com/Wonderforge-Lab/CapstanAI-LabNote/generate), then choose the name and visibility of your new repository. |
| **On your own computer** | Clone or download the repository. A remote GitHub copy is optional. |

> **Keep live work out of this public repository.** The public CapstanAI LabNote repository is the source scaffold. Put private project material in your own private, controlled or local copy.

Once you have your copy:

1. Give your AI [`AI_ENTRYPOINT.md`](AI_ENTRYPOINT.md) as its starting point.
2. Confirm the workspace context if it asks.
3. Let it follow the LabNote lobby from there.

[Choose the right setup route](docs/ACQUISITION.md), or [follow the first-use walkthrough](docs/quickstart.md).

## A working picture

```text
lobby/          ← every AI session starts here
datadrops/      ← source material and work go in
responses/      ← critiques, replies and signoffs come back
registry/       ← what happened, when and by whom
```

A session enters, reads the relevant route, contributes what it needs to contribute, leaves a traceable record and stops. The human remains in charge.

A typical trail is **packet → response → review → decision**.

Once LabNote is set up, you can say things like:

```text
Put this document in my LabNote and cross-reference it with [document name].

Leave a critique for [AI or agent name] about [document name].

Register this report, tag it properly, and leave a short completion note.
```

The AI gets enough structure to act, enough context to orient itself, and clear stopping points when a human decision is needed. The included validation workflow runs on pushes and pull requests. It checks registry records and provenance/path rules, generated views and Markdown links, locale invariants and freshness, bridge configuration, and tag-promotion separation.

[See how handoffs move through review and decision](docs/review_workflow.md).

## Why clone it instead of making a folder?

You absolutely can make a folder, keep a to-do list and ask an AI to leave better notes. For a short project, that may be all you need.

LabNote is the version you do not have to keep rebuilding. It gives every session the same place to begin, a small method for leaving work behind, and a visible record that still makes sense when you return later or switch tools.

You do not have to use every part of it. The more careful routes are already there when you need review, provenance, auditability or a clean way to pass work on. Until then, it can sit quietly beside the tools you already use.

## Why LabNote stays small

LabNote does not try to save everything as it happens. Not every message belongs in a durable project record. Instead, it preserves the parts you choose to carry forward: the source, the decision, the critique, the handoff and the next action.

That keeps the ledger smaller, clearer and easier to inspect. It avoids needless rereading, resummarising and context loading when a later session only needs the useful trail.

The rails do not make a model smarter, and they cannot make one infallible. They make routine coordination work smaller and clearer: a known entrance, a limited reading route, clear write targets, and defined points to stop and ask.

LabNote itself needs:

- no daemon;
- no database;
- no hosted runtime;
- no repo-resident agent;
- no model API keys.

No shared-memory theatre.

Just ordinary files, clear routes and human-held authority. The ledger is right there in the files, where you can inspect it yourself.

[See how LabNote fits alongside context files, RAG and model memory](docs/WHY_LABNOTE.md).

## Where it earns its keep

**Research, investigations and casework**
Keep sources, evidence, competing explanations, chronology and decisions together across separate sessions.

**Software and technical work**
Carry plans, implementation notes, tests, reviews and handoffs between different tools and agents.

**Writing, study and creative projects**
Preserve outlines, drafts, critiques, open questions and editorial choices without rebuilding the brief every time.

**Long-running or dormant projects**
Return after weeks or months and give a fresh AI a reliable place to find what mattered and what should happen next.

The subject does not matter much. If the work lasts longer than one chat, moves between tools, or would be a nuisance to reconstruct from memory, LabNote can give it a durable spine.

## Why I made it

Fact is, I got sick and tired of chat context windows filling up before I'd even finished thrashing out an idea.

Handoff sheets helped, but each new synthesis risked losing finer points or whole avenues of thought. Ideas would appear in unrelated chats or conversations with another model. Progress reports, critiques and reminders multiplied, and sometimes the project became scattered enough that I lost the thread and started again.

Project areas, canvases and branching chats all help, but I wanted something simpler: a way for one AI session to flow naturally into another without turning the project into a full-on second brain.

Hence LabNote. What began as a fix for my own terrible project memory became my daily driver. I now make one for most substantial projects, and use it to dust down work that has been sitting untouched for months.

At heart, it turns the AI into a low-overhead archivist and coordinator: told what to read, where to put things, what to record and when to stop.

## Licence

[Apache License 2.0](LICENSE) · [CapstanAI LabNote source releases and version history](https://github.com/Wonderforge-Lab/CapstanAI-LabNote/releases)

> **Mind the gap. Mark the crossing.**
