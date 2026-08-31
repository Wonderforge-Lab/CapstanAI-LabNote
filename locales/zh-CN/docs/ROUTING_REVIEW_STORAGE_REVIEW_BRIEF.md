# Simplified-Chinese Routing / Review / Storage Review Brief

Target locale: `zh-CN`

Review targets:

- `message_routing_model.md`
- `review_workflow.md`
- `storage_policy.md`
- `CORPUS_IMPORT_POLICY.md`

Status: language and protocol-parity review before these Chinese operational companions are marked reviewed.

## Review goal

Please review these four files as one operational cluster covering message routing, human review authority, storage boundaries, and corpus import controls.

Natural Chinese matters, but behavioural and modal-force parity with the English canonical files is primary.

Do not strengthen or weaken the source merely to make the Chinese sound more decisive.

## 1. Message routing model

Please verify these semantics:

- messages are directed notes between visitor/session IDs,
- messages may be used for review requests, follow-up, compact operator status, or blocked tasks needing human relay,
- canonical message records are JSON-per-record under `registry/messages/`,
- CSV, if present, is legacy/optional rollup,
- the message file carries useful text while the JSON record carries state,
- the recipient must not be assumed to have seen a message until one of three source-defined conditions occurs:
  1. the recipient replies,
  2. the human operator confirms delivery,
  3. the message is closed.

Please stress-test the final Chinese sentence. Do not silently reinterpret `closed` as proof of literal human/AI reading if the English source itself uses closure as one of the workflow resolution conditions.

## 2. Review workflow

Please verify:

- LabNote is human-in-the-loop by design,
- assistant sessions may draft, critique, summarize, or propose,
- the human operator decides what is accepted, rejected, archived, or routed onward,
- the canonical typical-flow code block remains unchanged,
- `templates/review_note.md` is used when decision reasoning matters,
- a response that is still pending must not be treated as accepted work.

Please check whether this Chinese sentence preserves authority cleanly:

```text
由操作者决定哪些内容被接受、拒绝、归档或继续路由到下一步。
```

The translation must not suggest joint AI/human final authority.

## 3. Storage policy

The canonical source here says:

```text
CapstanAI - LabNote is the ledger, not the warehouse.
```

Therefore the Chinese intentionally uses the absolute contrast:

```text
CapstanAI - LabNote 是工作台账（ledger），而不是大型资料仓库（warehouse）。
```

This differs intentionally from `DOCUMENT_DEPOSIT_POLICY.md`, whose English source says `ledgers first, warehouses second`.

Please preserve that source-level distinction.

Also verify:

- LabNote is for small text artifacts,
- large/private/heavy collections require explicit operator approval of workspace and storage policy,
- bulky supporting material should live outside LabNote or in another operator-approved location,
- the operator should decide storage and access rules before assistant sessions rely on the material,
- packets link to heavy material using stable title/path/URL/storage reference,
- packets include a short summary so the receiving session can decide whether opening the heavy material is necessary,
- public/reference-only workspaces must not receive private runtime material.

Pay attention to the modal force of `should` in the English source. Do not automatically turn it into `必须` unless the English is genuinely mandatory.

## 4. Corpus import policy

Please verify:

- public/reference-only workspaces must not store private runtime corpora, private transcripts, bulky archives, credentials, or project-specific runtime dumps,
- controlled workspaces follow operator-approved storage policy,
- bulky material defaults to manifest/index first,
- the recommended path `refs/<packet_id>/EXTRACTED_INDEX.md` remains unchanged,
- full unpack/import requires explicit operator approval and an appropriate workspace,
- if approval is missing, create a manifest/index and sign off,
- each listed stop condition remains a hard `stop and report` condition.

Stress-test:

```text
如果缺少批准，请创建清单/索引并签退。
```

and:

```text
出现以下任一情况时，停止并报告：
```

Please confirm these preserve the English behaviour exactly.

## Machine/path invariance

Do not translate or alter:

- `registry/messages/`,
- `templates/review_note.md`,
- `refs/<packet_id>/EXTRACTED_INDEX.md`,
- packet IDs,
- paths,
- JSON/state semantics.

Conceptual prose around them may be localized.

## Cross-file consistency

Please compare the four files for consistency around:

- human relay,
- operator authority,
- accepted work,
- ledger versus warehouse,
- public/reference-only workspace,
- private runtime material,
- manifest,
- operator approval,
- stop/report semantics.

Do not erase deliberate distinctions inherited from different English source files.

## Review format

Please return two parts.

### Part A - overall assessment

Cover:

1. naturalness,
2. developer/agent-facing register,
3. protocol parity,
4. modal-force parity,
5. human-authority parity,
6. storage/import safety parity,
7. cross-file consistency,
8. readiness.

### Part B - recommended edits

For each change:

```text
File:
Section / rule:
Current Chinese:
Recommended Chinese:
Reason:
Protocol effect: unchanged / clearer / potential behaviour change
Confidence: high / medium / low
```

Explicitly flag any recommendation that would change source behaviour.

## Final verdict

End with one of:

```text
READY AFTER LISTED EDITS
READY AS WRITTEN
REQUIRES ANOTHER REVIEW PASS
```

If another pass is needed, identify the blocking protocol issue precisely.
