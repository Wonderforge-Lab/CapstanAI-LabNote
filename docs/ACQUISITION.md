# Getting CapstanAI LabNote

This guide is only about acquiring a usable LabNote workspace. Once the copy exists, normal LabNote use starts at `AI_ENTRYPOINT.md`.

## Easiest starting prompt

If you are already talking to an AI, you can simply say:

```text
Help me set up CapstanAI LabNote for this project. First work out what access you have, then recommend the simplest safe route for me. I want you to explain any terminal commands before I run them.
```

The AI should determine whether it can access GitHub, whether it can run terminal commands itself, whether you can run terminal commands, and whether you want the workspace locally, on GitHub, or both.

## Recommended routes

### Browser AI + terminal available: local + GitHub

This is the preferred route when you want both a local working copy and a private GitHub workspace.

The browser AI should tailor the commands to your operating system, shell, chosen folder, and private destination repository. A typical Git flow is:

```bash
git clone https://github.com/Wonderforge-Lab/CapstanAI-LabNote.git MyProject-LabNote
cd MyProject-LabNote
git remote rename origin upstream
git remote add origin <YOUR-PRIVATE-REPO-URL>
git push -u origin main
```

Before asking you to run them, the AI should explain that these commands:

- copy the public LabNote repository into a new local folder,
- keep the public source available as `upstream`,
- connect your working copy to your own repository as `origin`,
- push the initial LabNote workspace to your repository.

The AI should also confirm that the destination repository is the one you intend to use and is suitable for the push. It must not guess or invent a private repository URL.

### Browser AI without terminal access: GitHub-only

Use GitHub's **Use this template** flow to create a new private or otherwise controlled repository.

Recommended steps:

1. Open the canonical CapstanAI LabNote repository on GitHub.
2. Choose **Use this template**.
3. Choose **Create a new repository**.
4. Give the new repository a project-specific name.
5. Select **Private** unless you intentionally want a public workspace.
6. Create the repository.
7. Give the AI access to the new workspace and start at `AI_ENTRYPOINT.md`.

GitHub Import is an alternative when template creation is unavailable or unsuitable, but the template route is the simpler default for a GitHub-only user.

### Coding agent or terminal-capable AI

A coding agent can normally perform the clone and repository setup itself, subject to the operator's approval and the permissions available to the agent.

The agent should still:

- state what repository it is copying,
- state the intended local and/or remote destination,
- avoid overwriting a non-empty destination without explicit approval,
- preserve the public source as `upstream` when a private `origin` is created,
- stop if repository identity or permissions are unclear.

### Local-only workspace

Clone LabNote locally:

```bash
git clone https://github.com/Wonderforge-Lab/CapstanAI-LabNote.git MyProject-LabNote
cd MyProject-LabNote
git remote rename origin upstream
```

No private remote is required. The `upstream` name simply makes it clear that the remote points to the public source rather than to your own project repository.

## After acquisition

However LabNote arrived, the next step is the same:

1. Open `AI_ENTRYPOINT.md` with the AI that will use the workspace.
2. Confirm the expected LabNote structure is present.
3. Confirm whether this is a private/controlled live workspace or a public/reference-only workspace.
4. Follow the lobby reading order.

No repository rename or LabNote identity-file edit should be required before first use.
