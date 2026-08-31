# Simplified-Chinese Operational Entry Review Brief

Target locale: `zh-CN`
Review targets:

- `AI_ENTRYPOINT.md`
- `lobby/README_FIRST.md`
- `lobby/VISITOR_CHECKLIST.md`
- `lobby/ROUTINE_DEPOSIT_QUICKSTART.md`

Status: language and protocol-parity review before the Chinese operational entry route is activated from the canonical entrypoint.

## Review goal

Please review these four files as one operational control cluster.

This pass is stricter than the README/front-door review. Natural Chinese matters, but **protocol force and behavioural parity matter more**.

A fresh AI following the Simplified-Chinese route should make materially the same decisions as one following the English canonical route.

Do not redesign the workflow or soften/strengthen rules for style.

## Architecture to preserve

The Chinese files are localized companion instructions over the same LabNote workspace.

Machine-facing workflow elements remain language-invariant, including:

- write paths,
- file/directory names,
- JSON keys,
- status values such as `accepted` and `proposed`,
- IDs and naming patterns,
- default branch semantics,
- Git branch/PR behaviour,
- final-report field labels shown in code blocks.

Localized documentation may point the reader to a Chinese companion file for instructions. That must **not** create a parallel Chinese storage layout or change where runtime artifacts are written.

## Modal-force audit

Please explicitly audit the Chinese for these distinctions:

### MUST / required

Where the English requires an action, the Chinese should read as a hard requirement, typically using wording such as `必须`, `不得`, or an equally strong construction.

Examples include:

- confirm workspace context before writing,
- no private runtime deposits into public/reference-only workspaces,
- no current-run visitor handle means no write,
- stop when required safety conditions are unclear,
- use branch + PR for the listed non-routine change classes.

### MAY / permitted

Where the English says an action *may* happen, do not turn it into a requirement.

Important example:

- routine deposits in a controlled live workspace **may** write directly to the default branch.

### DO NOT

Check that prohibitions remain prohibitions, including:

- do not assume workspace identity/context,
- do not reuse visitor handles/branches/storage/permissions from prior conversation context without explicit current-run confirmation,
- do not create task branches for ordinary deposits,
- do not edit CSV unless explicitly requested.

### STOP vs STOP AND ASK

These are not interchangeable.

Please preserve where the English specifically says:

- `stop and report`,
- `stop and ask the human operator`,
- `stop` without necessarily asking.

Flag any place where the Chinese changes one category into another.

## Critical gates to stress-test

### Workspace context gate

Before writing, the AI must determine whether the workspace is suitable for live/private work or is public/reference-only.

### Visitor handle gate

The intended rule is:

```text
No current-run visitor handle, no write.
```

Current Chinese rendering:

```text
没有本次运行的访客会话标识（visitor handle），就不得写入。
```

Please check whether this is as unambiguous and memorable as the English.

### Prior-context reuse prohibition

The AI must not reuse visitor handles, branches, storage locations or permissions from an earlier conversation unless the operator explicitly confirms them for the current run.

### Branching rule

Routine deposits use the default branch directly in a controlled live workspace.

Task branches are not created for ordinary deposits.

Branch + PR is for procedure, policy, repository structure, code/scripts, cleanup, risky/bulky imports, many existing-file edits, or explicit review.

Please verify that the Chinese preserves the boundary rather than making branch + PR merely optional in those cases.

### Registry rule

Canonical registry records remain JSON-per-record under `registry/`.

CSV remains legacy/optional rollup only.

### Tag status rule

Operator-supplied missing tags may be added as `accepted` records according to the canonical workflow.

AI-generated useful tags are `proposed`, not `accepted`.

The machine status words must remain English.

### Final report

The final-report field labels remain English intentionally for structural/cross-language consistency.

Please confirm that the Chinese explanation around them makes that choice understandable.

## Localized reading-path check

The Chinese entry route points to companion files such as:

```text
locales/zh-CN/AI_ENTRYPOINT.md
locales/zh-CN/lobby/README_FIRST.md
locales/zh-CN/lobby/VISITOR_CHECKLIST.md
```

while runtime artifact paths remain canonical, for example:

```text
datadrops/shared/inbox/<packet_id>.md
registry/packets/YYYY/<packet_id>.json
responses/signoffs/<packet_id>-signoff.md
```

Please flag any Chinese sentence that could make a reader think localized documentation paths imply localized runtime storage paths.

## Specific wording to review

Please pay particular attention to:

```text
没有本次运行的访客会话标识，就不得写入。
停止并报告该不一致。
停止并向操作者询问。
如果路由、存储权限、二进制文件处理方式或登记库路径不明确，停止。
常规投递可以直接写入该工作区的默认分支。
只有以下情况才使用 branch + PR。
对所提供材料进行足够检查，以推断合适的标签。
报告所创建的文件，然后停止。
```

Check for naturalness, strength and exact behavioural meaning.

## Review format

Please return two parts.

### Part A - overall assessment

Cover:

1. naturalness,
2. developer/agent-facing register,
3. protocol parity,
4. modal-force parity,
5. stop/ask parity,
6. branch/write-mode parity,
7. localized-path clarity,
8. whether the cluster is ready after listed edits.

### Part B - recommended edits

For each change:

```text
File:
Section / step:
Current Chinese:
Recommended Chinese:
Reason:
Protocol effect: unchanged / clearer / potential behaviour change
Confidence: high / medium / low
```

Please call out **any potential behaviour change explicitly**, even if the Chinese sounds natural.

## Final verdict

End with one of:

```text
READY AFTER LISTED EDITS
READY AS WRITTEN
REQUIRES ANOTHER REVIEW PASS
```

If another pass is required, identify the blocking protocol issue precisely.
