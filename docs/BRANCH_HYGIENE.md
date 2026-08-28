# Branch Hygiene

Routine runtime work in a controlled live workspace writes directly to the default branch.

Use branch + PR for:

- procedure changes
- policy changes
- repo structure changes
- code or script changes
- risky or bulky imports
- cleanup operations
- editing many existing files
- explicit review

Do not create branches for ordinary datadrops, response packets, messages, signoffs, or JSON registry records.

If the current workspace is a public/reference repository, use branches/PRs for changes to the distributed LabNote scaffold rather than treating those changes as routine deposits.

Do not delete branches without operator approval.

Do not force-push unless explicitly instructed.
