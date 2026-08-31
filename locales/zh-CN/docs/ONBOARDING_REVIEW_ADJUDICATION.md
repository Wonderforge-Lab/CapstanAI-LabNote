# zh-CN Onboarding Review Adjudication

Status: reviewed onboarding baseline
Locale: `zh-CN`

This note records the adjudication of the external Simplified-Chinese review of `ACQUISITION.md` and `quickstart.md`.

## Accepted changes

### Empty destination repository

Changed:

```text
目标私有仓库应该是新建且为空的。
```

to:

```text
目标私有仓库必须是新建且为空的。
```

Reason: the English source treats this as a hard requirement for the simple local + GitHub flow. `必须` preserves that operational force; `应该` could be read as advisory.

### Quickstart closing line

Changed:

```text
不靠神秘记忆
```

to:

```text
不靠模糊记忆
```

Reason: `模糊记忆` is more idiomatic in Chinese while preserving the intended contrast between structured records and unreliable recall.

## Review outcome

The reviewer returned:

```text
READY AFTER LISTED EDITS
```

Both listed edits were accepted. The acquisition and quickstart translations are therefore treated as reviewed localized operational documentation, subject to the English canonical source on any protocol conflict.
