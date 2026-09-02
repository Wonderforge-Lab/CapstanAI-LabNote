# Visitor ID Rules

> Superseded historical material. Follow [AI_ENTRYPOINT.md](../../AI_ENTRYPOINT.md) and the active [Registry Contract v1](../../docs/registry/REGISTRY_CONTRACT_V1.md) for current protocol. This file is retained only for provenance.

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
