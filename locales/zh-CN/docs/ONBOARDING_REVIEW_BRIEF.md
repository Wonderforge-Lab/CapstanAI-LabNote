# Simplified-Chinese Onboarding Review Brief

Target locale: `zh-CN`
Review targets:

- [`ACQUISITION.md`](ACQUISITION.md)
- [`quickstart.md`](quickstart.md)

Canonical sources:

- [`../../../docs/ACQUISITION.md`](../../../docs/ACQUISITION.md)
- [`../../../docs/quickstart.md`](../../../docs/quickstart.md)

Status: language, cultural and protocol-parity review before the Chinese onboarding route is linked as localized operational documentation.

## Review goal

Please review these two files as one onboarding flow.

A Simplified-Chinese user should be able to:

1. understand how to obtain a LabNote workspace safely,
2. choose an appropriate acquisition route,
3. reach `AI_ENTRYPOINT.md`,
4. understand the public/reference-only versus private/controlled distinction,
5. reach the lobby in the correct order,
6. understand that no current-run visitor handle means no writing,
7. complete the minimal packet/response workflow without changing canonical machine identifiers.

The translation should sound natural to a mainland Simplified-Chinese technical reader while preserving the exact operational force of the English source.

## Hard invariants

Do not translate or alter:

- Git commands,
- repository URLs,
- placeholders such as `<YOUR-PRIVATE-REPO-URL>`,
- paths,
- JSON-related path structure,
- machine state `accepted`,
- Git remote names `origin` and `upstream`,
- GitHub UI labels where keeping the English label helps the user find the actual control.

## Safety points to stress-test

Please confirm that the Chinese does **not** weaken any of these:

### Destination repository

For the simple local + GitHub flow, the destination repository must be new and empty.

If it already contains commits or files, the user/AI must stop and choose a safe alternative rather than force-pushing over it.

### Repository URL

The AI must not guess or invent a private repository URL.

### Terminal commands

The AI should explain terminal commands before asking the user to run them.

### Operator authority

A coding agent may perform setup only subject to operator approval and available permissions.

### Public workspace safety

A public/reference-only workspace is not an appropriate destination for private runtime material.

### Visitor handle gate

The quickstart states that the current-run visitor handle must be supplied by the operator. If none is supplied, the AI must stop and ask before writing.

Please check that the Chinese wording communicates a hard stop, not a suggestion.

### Review before `accepted`

The response must be reviewed before anything is marked `accepted`.

## Cross-file consistency

Please compare the two translations for consistent wording around:

- browser AI with/without terminal access,
- operator approval,
- private/controlled workspace,
- public/reference-only workspace,
- acquisition,
- setup / bootstrap,
- lobby,
- visitor handle,
- packet,
- review.

The acquisition prompt appears in both files and should remain identical.

## Specific wording to review

Please pay special attention to:

```text
初始化（bootstrap）工作区
目标私有仓库
强制推送
入口区（lobby）
本次运行访客会话标识（visitor handle）
小文件，清楚的标签，不靠神秘记忆。诀窍就这么简单。
```

Check whether each is natural, precise and appropriate for developer-oriented but accessible Chinese documentation.

The final quickstart line is intentionally light in tone. Preserve that lightness if revising it, but do not make it childish or obscure.

## Review format

Please return two parts.

### Part A - overall assessment

Cover:

1. naturalness,
2. technical register,
3. cultural fit,
4. protocol parity,
5. cross-file consistency,
6. safety-language strength,
7. whether the pair is ready to publish after listed edits.

### Part B - recommended edits

For each change:

```text
File:
Section:
Current Chinese:
Recommended Chinese:
Reason:
Semantic effect: unchanged / clearer / potential meaning change
Confidence: high / medium / low
```

Do not rewrite natural passages merely for stylistic preference.

## Final verdict

End with one of:

```text
READY AFTER LISTED EDITS
READY AS WRITTEN
REQUIRES ANOTHER REVIEW PASS
```

If you choose `REQUIRES ANOTHER REVIEW PASS`, identify the blocking protocol or language issue clearly.
