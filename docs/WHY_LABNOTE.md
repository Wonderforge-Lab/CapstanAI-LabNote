# LabNote alongside context files, agent memory and observability

LabNote is a human-controlled project ledger for work that moves between AI
assistants, coding agents, chats and people. It keeps selected project
continuity in visible Markdown artifacts and structured JSON registry records.

Its job is not to enlarge a model's context window, automatically remember
everything, or trace every model call. Its job is to keep the project thread:
the sources, handoffs, responses, reviews, decisions and next actions that
people decide should travel forward.

## The record is selective

Not every message belongs in a durable project record. LabNote keeps the
stepping stones that make the next piece of work understandable:

- a source or incoming packet;
- a response, contribution or draft;
- a review or correction;
- a decision or signoff; and
- the next action or handoff.

That makes the retained trail smaller and easier to inspect than a full
transcript or a growing context blob. An AI can help prepare the record, but
the workspace does not silently harvest conversations: the human decides what
belongs and what needs review.

## Model context is not project continuity

A long context window can help a model read more in one sitting. It does not,
by itself, decide what should remain important after the session, show the next
tool why a decision was made, or create a selective record that a human can
inspect.

LabNote does not enlarge a model's native memory. A human or an AI session
deliberately writes the record, so the trail can be checked, corrected,
reviewed and carried to another tool.

Context length is useful. Project continuity is a separate job.

## Agent memory is a different trade-off

Some AI-memory systems automatically extract, compress, index and retrieve
information across interactions. That can be useful when an agent needs
automatic recall.

LabNote takes a different route. Basic ledger use needs no LabNote background
service, database or model API key, and it does not make an automatic memory
store. It keeps the selected project record in the repository, where the
people running the project can see and govern it.

These approaches can coexist. Use automatic memory when automatic retrieval is
the need; use LabNote when the project needs a deliberate, visible handoff and
decision trail.

## Context files set local rules

Files such as `AGENTS.md` or `CLAUDE.md` are useful ways to tell an AI about
a repository: where important files are, how to run tests and what local rules
apply.

LabNote complements them. Its job is to route ongoing project work: where a
session begins, what it should read, where it may leave work, how that work is
reviewed and when the session should stop and ask.

A context file tells an AI what kind of repository it is in. LabNote gives it a
route through the work happening there.

## An audit trail is not full observability

AI-observability tools can trace prompts, model calls, tool calls, timing and
token use. They answer runtime questions such as “what did this system call?”

LabNote records a different layer: the project artifacts people choose to
retain, and the review, decision and handoff around them. It is a
project-level, human-controlled audit trail—not a claim to capture every model
call or every action automatically.

## Rails make the routine legible

The rails do not make a model deterministic, smarter or infallible. They make
routine coordination work clearer: a known entry, a bounded reading route,
clear write targets and defined points to stop and ask.

That means an incorrect contribution can remain visible as part of the record:
it can be reviewed, corrected, rejected or superseded rather than quietly
becoming unexamined “memory.”

## Use the smallest useful amount

If a one-shot answer is enough, use the best tool available and get on with it.
If a plain folder is enough, use a plain folder.

Use LabNote when you want a visible working trail that can grow with the
project without becoming a hidden service or a second brain. Start with the
smallest record that will genuinely help the next session.

[Return to the documentation index](README.md).
