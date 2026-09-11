# CapstanAI LabNote

*A human-controlled, git-native project ledger for work across AI chats and sessions.*

CapstanAI LabNote gives you somewhere to keep the documents, decisions and handoff notes you want to carry between AI sessions. You can use different assistants for different parts of a project, then bring their work together in a repository of your own.

You choose what gets saved and when. LabNote gives the AI instructions for finding its way around, recording the work you approve and reporting back.

<p align="center">
  <img src="https://img.shields.io/badge/license-Apache--2.0-blue" alt="Apache License 2.0">
  <img src="https://img.shields.io/badge/runtime-none-informational" alt="No LabNote runtime">
</p>

<p align="center">
  <img src="assets/capstanai_labnote_raven.png" alt="CapstanAI LabNote raven perched on a lab notebook with a pearl and fountain pen" width="30%">
</p>

*Mind the gap. Mark the crossing.*

## Why use it?

I used to copy summaries between chats, keep handoff notes, save useful responses and even try to remember which AI was told what. It was time-consuming. So I put LabNote together to help me keep on top of progress.

LabNote can be used simply as a handoff for one chat to another, or it can scale to allow several chats/models/coding agents to pool resources for a project with you at the helm.

You might ask one AI to investigate a question, take its report to another for a critique, then save your decision alongside both. When you come back to the project, you have the work and the reasons for the decision there to refer to.

I think of it as a room with labels on the drawers. A new AI still needs to read the relevant material, but it has somewhere to start.

You can keep research, development notes, drafts, study material or a few things you don't want to lose track of. Give each project its own LabNote and use as much of it as you need. For a short project, an ordinary folder and a few handoff notes may be enough.

[Is LabNote suitable for your project?](docs/WHEN_TO_USE_LABNOTE.md)

## Get LabNote

If you're already talking to an AI, you can give it this:

```text
Help me set up CapstanAI LabNote for this project. First work out what access you have, then recommend the simplest safe route for me. I want you to explain any terminal commands before I run them.
```

The AI should help you work out whether you want LabNote on your computer, on GitHub or both, and what it can do to help you get it there.

You can also make a copy yourself:

| Where you want it | What to do |
| --- | --- |
| Your own GitHub repository | Select [Use this template](https://github.com/Wonderforge-Lab/CapstanAI-LabNote/generate), then choose a name and whether the repository is public or private. |
| Your computer | Clone or download the repository. You don't have to keep a copy on GitHub. |
| Both | Follow the [setup guide](docs/ACQUISITION.md) to connect your local copy to your own GitHub repository. |

**This public repository is the template. Please put project work in your own copy.** For confidential material, use a private repository or a suitably protected local folder.

Already downloaded LabNote or created your own repository from the template? Ask your AI to read the [`AI_ENTRYPOINT.md`](AI_ENTRYPOINT.md) file in that folder or repository. It should follow the entry instructions, confirm which workspace it's using and ask for the information it needs.

Browser AIs, coding agents and local models can work directly when they have suitable access to the files. If an assistant can't reach them, it can explain the manual steps.

Setting up LabNote doesn't give the AI permission to start saving project material on its own. Tell it when you want to begin recording work.

[Setup options](docs/ACQUISITION.md) · [First-use walkthrough](docs/quickstart.md)

## Using your LabNote

Once it's set up, you can ask for things like:

```text
Put this document in my LabNote and cross-reference it with [document name].

Leave a critique for [AI or agent name] about [document name].

Register this report, tag it, and tell me when the deposit is verified.
```

A *deposit* is the process of saving material with the records describing it. The AI follows the relevant instructions, creates the required records, regenerates the registry views, checks the whole deposit and reports back.

The main folders give the work somewhere to go:

| Folder | What you will find there |
| --- | --- |
| `lobby/` | Instructions the AI follows when entering and using your LabNote. |
| `datadrops/` | The documents and source material you've deposited. |
| `responses/` | Replies, critiques and signoffs. |
| `registry/` | Records describing the deposits, including when they were made and by whom. |

If you want another opinion on a piece of work, you can pass it to another AI for review and keep that response with the project. A fuller review can follow the **packet → response → review → decision** sequence.

An AI may suggest that something is worth recording; you decide whether to go ahead. LabNote's instructions require the AI to wait for you to start or approve that step. This is an operating rule, rather than a technical barrier to writing files.

[Follow a worked example, including a corrected AI claim](docs/WORKED_CONTINUITY_TRAIL.md) · [More about reviews and decisions](docs/review_workflow.md)

### Let contributors take turns

You can have several people or AIs researching, reading and preparing material at once. When they're ready to save it in the same LabNote, they need to take turns.

Approve one contributor's deposit and wait for its completion report. That report should confirm that the whole deposit has been saved and verified where you intended it to go: your computer, GitHub or both. Then you can approve the next contributor.

Everyone using that LabNote needs to coordinate those turns, even if they're working in different chats, tools or local copies. Before writing, the contributor must confirm with the human that the deposit is authorised and no other writer is active.

Each AI contributor needs a unique session handle assigned by the human. This convention is part of the process to put the AI on the right track from the outset, and for auditing purposes; it doesn't reserve a turn or give permission to write.

LabNote has no automatic queue or locking service. Simultaneous deposits, including a swarm of agents trying to save work at once, are unsupported.

If a deposit fails or its publication can't be verified, the contributor must preserve the prepared work and report what's missing or uncertain. Resolve that attempt with the human before the next writer starts; don't blindly retry or force-push over somebody else's work.

[Deposit instructions, verification and what to do if a step fails](lobby/ROUTINE_DEPOSIT_QUICKSTART.md)

## Keep what matters to you

You don't have to save a whole conversation because it produced something useful. You might want just the source document, a critique, the decision you reached or a note saying what to try next.

When you return, you can point the next AI towards those records. If it needs more background, you can bring that in too. LabNote doesn't automatically capture conversations or give an assistant memory of material it hasn't read.

How useful this is will depend on what you keep and how well it's described. An AI can still misunderstand a source or reach the wrong conclusion; keeping its work and the reviews gives you something to check when that happens.

Keep normal backups of your LabNote, as you would with other project files. It sits alongside existing tools, including version control and project applications.

## What you need

LabNote is file-based and git-native. Its documents are ordinary Markdown files, with structured JSON records in the registry. You can inspect and copy them without a specialised LabNote application.

Basic ledger use requires no background service, database, hosted runtime, resident agent or model API key. You don't need a separate CapstanAI engine.

There's no LabNote MCP server to install either; LabNote neither includes nor requires one. Your assistant may use an external connector, including MCP, to reach files or GitHub. That belongs to the assistant's setup.

[How LabNote fits alongside context files and model memory](docs/WHY_LABNOTE.md)

## Checks and development

The repository includes a validation workflow that runs on GitHub pushes and pull requests. It checks registry records, file paths, provenance rules, generated views, Markdown links, bridge configuration and tag-promotion separation.

These checks can catch structural mistakes in the record. You still need to review the content; a correctly filed report can contain an incorrect conclusion.

You can look through the development history and its supporting evidence, or browse the releases to see how the repository has changed.

[Development history](docs/PROJECT_EVOLUTION.md) · [Releases](https://github.com/Wonderforge-Lab/CapstanAI-LabNote/releases)

## How it became my daily driver

Fact is, I got sick and tired of chat context windows filling up before I'd even finished thrashing out an idea.

Handoff sheets helped, but each new synthesis risked losing finer points or whole avenues of thought. Ideas would appear in unrelated chats or conversations with another model. Progress reports, critiques and reminders multiplied, and sometimes I lost the thread and started again.

Project areas, canvases and branching chats all helped. I wanted somewhere to keep the parts that mattered, so I could bring another AI into the work without rebuilding the brief.

LabNote grew out of that through repeated use, discussion and revision with different AI assistants. I now make a copy for most substantial projects, and use it to dust down work that has been sitting untouched for months.

## Licence

[Apache License 2.0](LICENSE)

*Mind the gap. Mark the crossing.*
