# Review Workflow

OpenBridge LabNote is human-in-the-loop by design.

An assistant session may draft, critique, summarize, or propose. The human operator decides what is accepted, rejected, archived, or routed onward.

Typical flow:

```text
packet -> response -> review note -> registry update
```

Use `templates/review_note.md` when the reason for a decision matters. If a response is still pending, do not treat it as accepted work.
