# Control Policies Review Adjudication

Locale: `zh-CN`
Status: **reviewed**

This note records the external Simplified-Chinese review and final adjudication for:

- `lobby/TAGGING_PROTOCOL.md`
- `docs/DOCUMENT_DEPOSIT_POLICY.md`
- `docs/BRANCH_HYGIENE.md`
- `docs/REGISTRY_RECORDS.md`

## Final result

The cluster is approved as reviewed Simplified-Chinese operational documentation.

The final narrow recheck of `BRANCH_HYGIENE.md` returned:

```text
Naturalness: pass
Modal-force parity: pass
Public/reference terminology: pass
Branch deletion rule: pass
Force-push rule: pass
Recommended edits: None
Final verdict: READY AS WRITTEN
```

The earlier blocking issue was caused by a truncated external handoff copy. The live repository file was complete and contained the intended hard control:

```text
除非操作者明确指示，否则不要强制推送（force-push）。
```

## Accepted recommendation

The workspace terminology in `BRANCH_HYGIENE.md` was aligned from:

```text
公共/参考仓库
```

to the frozen terminology:

```text
公共/仅供参考工作区
```

This was a terminology consistency change only.

## Recommendations intentionally not adopted

### Document deposit opening

The reviewer proposed changing:

```text
首先是工作台账（ledger），其次才是大型资料仓库（warehouse）
```

to a stronger ledger-not-warehouse contrast.

This was not adopted because the canonical English source says:

```text
CapstanAI - LabNote workspaces are ledgers first, warehouses second.
```

The Chinese therefore preserves the source's deliberate primary/secondary distinction rather than replacing it with an absolute exclusion.

### Registry visitor JSON wording

The reviewer proposed changing:

```text
访客会话应创建 JSON 记录文件，而不是编辑共享 CSV 台账。
```

to use `必须`.

This was not adopted because the canonical English source says:

```text
Visitors should create JSON record files instead of editing shared CSV ledgers.
```

Changing `应` to `必须` would strengthen the canonical source.

## Protocol invariants confirmed

The review and adjudication preserve:

- accepted versus proposed tag authority,
- operator-supplied accepted tags,
- AI-generated tags remaining proposed,
- JSON-per-record registry structure,
- CSV as legacy/optional rollup,
- canonical paths and JSON examples,
- routine default-branch writes,
- branch + PR hard controls,
- branch deletion approval,
- no force-push unless explicitly instructed,
- binary-document ask gate,
- review surrogate versus canonical binary distinction.

No runtime paths, JSON keys, status values, tag slugs, IDs, Git semantics, or write targets were localized or changed.
