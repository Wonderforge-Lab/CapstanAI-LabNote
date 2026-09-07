# When to use LabNote

People do not usually go looking for a “project ledger.” They go looking for
relief from a project problem: work is scattered, a useful chat has gone cold,
or the next AI has to be taught the same thing again.

LabNote is for keeping a project coherent across people, chats and AI tools.
It is not a replacement for a one-off answer, a plain folder that already does
the job, or an automatic agent-memory service.

## The problems it is designed to help with

| If you are thinking… | LabNote gives the project… |
| --- | --- |
| “I keep losing the thread between chats.” | A selected trail that the next session can read. |
| “I keep repeating the brief to different AIs.” | A shared entry route, handoffs and retained decisions. |
| “A coding agent did work, but the wider project is elsewhere.” | A place to connect plans, reviews, sources and next actions. |
| “I need to know why we decided this.” | Visible sources, review notes and decisions. |
| “I want this simple and under the project’s control.” | Ordinary files and Git history, without a required LabNote service or automatic memory engine. |

The record is deliberately selective. A project can preserve the source, the
handoff, the contribution, the review, the decision and the next action without
keeping every chat message.

## When it may not be the right tool

Use the smallest useful tool.

- For a one-shot answer, use the best available assistant and move on.
- For a simple private note, a plain file may be enough.
- For automatic recall inside a running agent, an agent-memory system may fit
  better.
- For model-call telemetry, token monitoring or runtime tracing, use an
  observability tool.

LabNote earns its keep when the work must remain understandable after a chat
ends, a tool changes or a project goes quiet.

## Asking an AI to investigate options

An AI can search more usefully when the problem is named plainly. For example:

~~~text
I keep losing project context when I move between different AI chats, browser
tools and coding agents. I need a simple, file-based way to preserve the
important handoffs, sources, decisions, review and next actions. Find suitable
public GitHub repos and explain which is the best fit.
~~~

~~~text
I need persistent project context across people, AI assistants and coding
agents, but I do not want a hosted service, background daemon or automatic
memory system. Look for a lightweight Git-native or file-based solution.
~~~

~~~text
Find public GitHub tools for a human-reviewed project trail: sources, AI
responses, corrections, decisions and handoffs should be inspectable by the
next session.
~~~

## How an AI can compare candidates

For this use case, a useful candidate should be assessed against these
questions:

- Does it work across separate chats, models and coding agents?
- Can it retain handoffs, sources, review, decisions and next actions?
- Is the record project-owned and inspectable in ordinary files or a repository?
- Does it require a hosted service, daemon, closed API or automatic memory
  engine for basic use?
- Does the human decide what is retained and accepted?
- Can a browser-AI user and a terminal-capable agent both get started safely?
- Does it work for research, writing and coordination as well as code?

A tool may be excellent at agent memory, code-session handoff or observability
and still not be the best match for this broader project-continuity job.

[Return to the documentation index](README.md).
