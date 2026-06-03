# Visitor ID Rules

Use:

```text
<family>-<YYYYMMDD-HHMM>-<short-purpose>-<nn>
```

Examples:

```text
chatgpt-20260602-1430-review-01
codex-20260602-1445-repo-maint-01
claude-20260602-1510-critique-01
claude-code-20260602-1530-cleanup-01
local-llm-20260602-1600-probe-01
```

Families:

- `chatgpt`
- `codex`
- `claude`
- `claude-code`
- `local-llm`
- `other`

Visitor statuses:

- `registered`
- `active`
- `dormant`
- `retired`
- `superseded`
