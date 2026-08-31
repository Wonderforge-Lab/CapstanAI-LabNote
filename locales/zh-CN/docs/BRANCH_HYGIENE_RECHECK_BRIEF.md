# Simplified-Chinese Branch Hygiene Narrow Recheck Brief

Target locale: `zh-CN`

Review target:

- `BRANCH_HYGIENE.md`

Reason for recheck: the previous external handoff copy was truncated before the final force-push rule. The live repository file was complete; this recheck is only to verify the complete corrected handoff.

## Scope

Please review the complete Simplified-Chinese `BRANCH_HYGIENE.md` for:

1. naturalness,
2. modal-force parity,
3. public/reference workspace terminology,
4. branch deletion control,
5. force-push control.

Do not reopen unrelated cluster recommendations unless the complete Branch Hygiene file reveals a genuine new inconsistency.

## Expected hard controls

Please confirm that the Chinese unambiguously preserves all of these:

- routine runtime work in a controlled live workspace writes directly to the default branch,
- the listed non-routine classes **must use `branch + PR`**,
- ordinary datadrops, response packets, messages, signoffs and JSON registry records do not get branches,
- changes to the distributed scaffold in a public/reference-only workspace use branch/PR rather than routine-deposit handling,
- branches are not deleted without operator approval,
- force-push is not used unless explicitly instructed by the operator.

## Force-push sentence to verify

```text
除非操作者明确指示，否则不要强制推送（force-push）。
```

Please verify that this is natural Chinese and has the same hard prohibitive force as:

```text
Do not force-push unless explicitly instructed.
```

## Terminology edit already applied

The previous wording:

```text
公共/参考仓库
```

has been aligned to the frozen workspace terminology:

```text
公共/仅供参考工作区
```

Please confirm this remains natural in context.

## Prior recommendations intentionally not applied elsewhere

For context only:

- `DOCUMENT_DEPOSIT_POLICY.md` retains `首先是工作台账，其次才是大型资料仓库` because the canonical English says `ledgers first, warehouses second`.
- `REGISTRY_RECORDS.md` retains `应创建 JSON 记录文件` because the canonical English says `Visitors should create JSON record files...`.

These decisions preserve source modal/semantic force and are not part of this narrow recheck.

## Requested response

Please return:

```text
Naturalness: pass / issue
Modal-force parity: pass / issue
Public/reference terminology: pass / issue
Branch deletion rule: pass / issue
Force-push rule: pass / issue

Recommended edits (if any):
...

Final verdict:
READY AS WRITTEN
or
READY AFTER LISTED EDITS
or
REQUIRES ANOTHER REVIEW PASS
```
