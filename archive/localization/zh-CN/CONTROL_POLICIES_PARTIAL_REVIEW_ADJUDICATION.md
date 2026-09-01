# Archived Simplified-Chinese Control Policies Partial Review Adjudication

> Historical review artifact. This partial adjudication was superseded by `locales/zh-CN/CONTROL_POLICIES_REVIEW_ADJUDICATION.md` after the complete Branch Hygiene recheck passed. It is retained here only for audit provenance and is not an active review status.

Reviewed cluster:

- `lobby/TAGGING_PROTOCOL.md`
- `docs/DOCUMENT_DEPOSIT_POLICY.md`
- `docs/BRANCH_HYGIENE.md`
- `docs/REGISTRY_RECORDS.md`

## Historical review outcome

The Chinese-language reviewer found the cluster broadly natural and protocol-faithful but could not issue a final readiness verdict because the handed-off copy of `BRANCH_HYGIENE.md` was truncated before the final force-push rule.

The live repository file was subsequently checked and was complete. The canonical safety rule was present:

```text
除非操作者明确指示，否则不要强制推送（force-push）。
```

A narrow recheck of the complete Branch Hygiene file was therefore required before the cluster could be promoted to reviewed.

## Recommendation 1 - Document Deposit opening contrast

Reviewer recommendation:

```text
CapstanAI - LabNote 工作区主要是工作台账（ledger），而不是大型资料仓库（warehouse）。
```

Decision: **rejected**.

Reason: the English canonical source says:

```text
CapstanAI - LabNote workspaces are ledgers first, warehouses second.
```

The existing Chinese:

```text
CapstanAI - LabNote 工作区首先是工作台账（ledger），其次才是大型资料仓库（warehouse）。
```

preserves the deliberate first/second hierarchy. Replacing it with `而不是` would change the source meaning by removing the possibility of a secondary warehouse role.

## Recommendation 2 - Registry visitor JSON wording

Reviewer recommendation: change `应创建 JSON 记录文件` to `必须创建 JSON 记录文件`.

Decision: **rejected**.

Reason: the English canonical source says:

```text
Visitors should create JSON record files instead of editing shared CSV ledgers.
```

The Chinese `应创建` preserves that `should` force. Changing it to `必须创建` would strengthen the source requirement.

The later visitor-rule block remains imperative, as in the English source:

```text
创建 JSON 记录
不要编辑 CSV
在签退记录中说明已创建的记录
```

## Recommendation 3 - Public/reference workspace wording

Reviewer recommendation: replace `公共/参考仓库` with the frozen terminology `公共/仅供参考工作区`.

Decision: **accepted**.

Applied wording:

```text
如果当前工作区是公共/仅供参考工作区，对将要分发的 LabNote 框架进行更改时，必须使用分支/PR 流程，而不是把这些更改当作常规投递处理。
```

This was terminology alignment only and did not change behaviour.

## Historical blocking issue - truncated Branch Hygiene handoff

Decision: **handoff artifact, not repository defect**.

The live branch contained the complete final rules:

```text
未经操作者批准，不要删除分支。

除非操作者明确指示，否则不要强制推送（force-push）。
```

The complete file was later resubmitted and passed the narrow recheck. See the active final adjudication at `locales/zh-CN/CONTROL_POLICIES_REVIEW_ADJUDICATION.md`.
