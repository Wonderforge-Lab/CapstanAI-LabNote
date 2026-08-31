# zh-CN Operational Entry Review Adjudication

Status: reviewed
Locale: `zh-CN`
Canonical source language: `en`

## Review outcome

The Simplified-Chinese operational entry cluster received Chinese-language and protocol-parity review covering:

- `AI_ENTRYPOINT.md`
- `lobby/README_FIRST.md`
- `lobby/VISITOR_CHECKLIST.md`
- `lobby/ROUTINE_DEPOSIT_QUICKSTART.md`

Reviewer verdict: `READY AFTER LISTED EDITS`.

The review found the cluster natural, agent-facing, structurally faithful, and clear about localized instruction paths versus canonical runtime storage paths.

## Accepted changes

### Branch + PR requirement in `AI_ENTRYPOINT.md`

Changed the descriptive wording:

```text
以下情况使用 branch + PR
```

to an explicit requirement:

```text
以下情况必须使用 branch + PR
```

Reason: the English source treats branch + PR as required for the listed non-routine change classes. The Chinese must preserve that modal force.

### Branch + PR requirement in `lobby/README_FIRST.md`

Changed the descriptive wording:

```text
分支/PR 用于...
```

to:

```text
对于以下情况，必须使用 branch + PR...
```

Reason: preserve the same mandatory branch/review boundary across all operational entry files.

## Confirmed without change

The reviewer explicitly confirmed that this standalone stop remains correct:

```text
如果路由、存储权限、二进制文件处理方式或登记库路径不明确，停止。
```

It preserves the English `stop` category and does not incorrectly turn it into `stop and ask`.

The reviewer also confirmed parity for:

- workspace-context gating,
- the current-run visitor-handle write gate,
- prior-context reuse prohibition,
- routine direct-to-default-branch behaviour,
- no task branch for ordinary deposits,
- JSON-per-record canonical registry semantics,
- legacy/optional CSV treatment,
- `accepted` versus `proposed` tag status handling,
- invariant final-report field labels,
- localized instruction paths versus canonical runtime artifact paths.

## Result

The operational entry cluster is accepted as the reviewed Simplified-Chinese baseline.

Later changes to control language in these files should be treated as protocol-affecting localization changes and should receive parity review before broad propagation.
