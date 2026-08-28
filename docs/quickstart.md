# Quickstart

CapstanAI LabNote has three stages: acquire a copy, bootstrap the workspace, then operate it.

## 1. Acquire LabNote

If you are already talking to an AI, the simplest starting point is:

```text
Help me set up CapstanAI LabNote for this project. First work out what access you have, then recommend the simplest safe route for me. I want you to explain any terminal commands before I run them.
```

Preferred routes:

- **Browser AI + terminal available:** AI-guided local clone, with a private GitHub `origin` if wanted.
- **Browser AI without terminal access:** GitHub **Use this template** into a private or otherwise controlled repository.
- **Coding agent or terminal-capable AI:** the agent can normally perform the clone/setup directly, subject to operator approval and repository permissions.
- **Local-only use:** clone locally; no private remote is required.

For exact beginner-friendly steps and example terminal commands, see [`docs/ACQUISITION.md`](ACQUISITION.md).

The acquisition method does not change how LabNote works after the copy exists.

## 2. Bootstrap The Workspace

1. Open `AI_ENTRYPOINT.md` with the AI that will use the workspace.
2. Confirm that the expected LabNote structure is present.
3. Confirm whether the current workspace is private/controlled for live work or public/reference-only.
4. Follow the lobby reading order: `lobby/README_FIRST.md` -> `lobby/VISITOR_CHECKLIST.md`.
5. Create or identify a visitor/session ID before writing.

No repository rename or LabNote identity-file edit should be required before first use.

## 3. Operate LabNote

1. Copy `templates/datadrop_packet.md` for a new packet.
2. Fill in the packet header and task sections.
3. If the packet depends on larger files, add an operator-approved reference and a short summary instead of committing the raw dump.
4. Create a JSON packet record under `registry/packets/<year>/`.
5. Give the packet to the target assistant session.
6. Copy `templates/ai_response_packet.md` for the answer.
7. Create a JSON response record under `registry/responses/<year>/`.
8. Review the response before marking anything accepted.

Small files, clear labels, no mystery memory. That is the trick.
