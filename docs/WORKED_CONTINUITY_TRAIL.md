# A worked continuity trail

This fictional example shows the smallest useful shape of a LabNote trail. It
does not represent a live project or a deposit in this public source
repository.

## The question

A small team is choosing a durable, visible colour for a new pedestrian bridge.
They want the next person or AI to understand the evidence, what was proposed,
what was challenged and what still needs doing.

They do **not** need every chat message preserved.

## 1. Keep the useful source

The operator selects two useful items: a supplier's finish guide and a local
design brief. They are placed in the appropriate project route with short
descriptions and references.

The record says what these sources are for. It does not turn a pile of browser
tabs or a full conversation transcript into “memory.”

## 2. Frame a packet

A packet asks an AI to produce a shortlist using those sources:

~~~
Task: propose three colour options for the pedestrian bridge.

Use: the recorded finish guide and design brief.

Include: the source behind each option, any uncertainty and a recommended next
check.

Do not decide the final colour.
~~~

The packet gives the next session a bounded question rather than asking it to
guess the whole project.

## 3. Keep the AI response beside the task

The AI returns a shortlist and recommends a dark blue finish. It correctly
links the supplier guide, but it also claims that the design brief requires
dark blue.

That claim is not supported by the brief.

The response remains useful, but it is not silently treated as accepted work.

## 4. Review the claim

A human reviewer leaves a short review note:

~~~
The design brief requires good contrast and low glare; it does not require
dark blue. Keep dark blue as an option, remove the unsupported claim, and ask
for a contrast check against the planned surroundings.
~~~

The review is attached to the response it concerns, rather than becoming an
untraceable correction in a later chat.

## 5. Record the decision and next action

The operator decides:

~~~
Decision: no final colour selected.

Accepted: dark blue, white and yellow remain the shortlist.

Rejected: the unsupported statement that dark blue is required.

Next action: obtain a contrast assessment before choosing.
~~~

The decision is deliberately small. It says what changed, what was accepted,
what was rejected and what should happen next.

## 6. Let the next session continue

A later AI or person starts at the shared entry route and finds the retained
sources, packet, response, review and decision. It does not need the original
chat to know:

- what the question was;
- why one claim was corrected;
- what has not yet been decided; or
- what to do next.

## What this demonstrates

LabNote does not make the AI's first answer correct, and it does not capture
everything automatically. It gives the project a visible route for preserving
the selected work, examining a mistake and carrying the corrected state
forward.

For the practical file-and-record steps, see the [first-use
walkthrough](quickstart.md) and [review workflow](review_workflow.md).
