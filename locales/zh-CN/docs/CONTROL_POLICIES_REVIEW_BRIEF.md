# Simplified-Chinese Control Policies Review Brief

Target locale: `zh-CN`
Review targets:

- `lobby/TAGGING_PROTOCOL.md`
- `docs/DOCUMENT_DEPOSIT_POLICY.md`
- `docs/BRANCH_HYGIENE.md`
- `docs/REGISTRY_RECORDS.md`

Status: language and protocol-parity review before these Chinese control-policy companions are treated as reviewed operational documentation.

## Review goal

Please review these four files as one control-policy cluster.

Natural Chinese matters, but behavioural parity with the English canonical files is the primary requirement.

Do not redesign the source protocol to make the Chinese more internally uniform. If two English source files express related rules differently, preserve the intended distinction and flag any genuine source ambiguity rather than silently resolving it.

## Language-invariant elements

The following must remain unchanged where they appear:

- repository paths,
- JSON keys,
- status values such as `accepted` and `proposed`,
- `created_by: operator` semantics,
- tag slugs,
- IDs and naming patterns,
- Git concepts such as `branch + PR`, `force-push`,
- JSON example keys and machine-readable values.

Chinese prose may explain these elements but must not replace them with localized machine forms.

## 1. Tagging protocol

Please verify these rules remain exact:

- prefer existing accepted tags,
- accepted tag records live under `registry/tags/accepted/`,
- proposed tag records live under `registry/tags/proposed/`,
- when the **operator** supplies a missing tag, an accepted JSON record may be created with `created_by` set to `operator`,
- AI-generated tags must be `proposed`, not `accepted`,
- private/workspace-specific tag lists must not be moved into a public/reference-only workspace,
- near-duplicate tags must not be created,
- tag choices should be explained in the packet or signoff.

Stress-test the wording:

```text
AI 自行生成的标签必须作为 proposed 提交，不得直接标记为 accepted。
```

Check that this cannot be read as allowing an AI to self-accept a tag through some alternate path.

## 2. Document deposit policy

Please verify:

- LabNote is primarily a ledger rather than a warehouse,
- text-first reviewable formats are preferred,
- workspace context must be confirmed before document deposit,
- private runtime documents must not be stored in public/reference-only workspaces,
- routine document deposits in controlled live workspaces do not need a branch,
- Markdown review surrogates, manifests, JSON records and signoffs normally go directly to the default branch unless the operator says otherwise,
- branch flow is reserved for bulky/risky/structural/policy/code/cleanup/uncertain imports,
- binary documents are not committed by default,
- text-heavy binary documents should receive a Markdown review surrogate,
- original filename, known size and available SHA256 should be recorded,
- the Markdown surrogate must not be confused with the canonical binary,
- the operator must be asked before committing the original binary.

Please pay special attention to:

```text
只有对于大体量、高风险、结构性、政策、代码、清理或不确定性较高的导入，才使用分支流程。
```

The English source says `Use a branch only for...`, while `BRANCH_HYGIENE.md` separately says `Use branch + PR for...` specified change classes. Please preserve the source relationship. If you think the two English rules themselves create a meaningful ambiguity, flag it explicitly instead of silently changing one.

## 3. Branch hygiene

Please verify these are hard controls:

- routine runtime work in a controlled live workspace writes directly to the default branch,
- the listed non-routine classes require `branch + PR`,
- ordinary datadrops, response packets, messages, signoffs and JSON registry records do not get branches,
- changes to the distributed scaffold in a public/reference repository use branch/PR rather than routine-deposit handling,
- branches are not deleted without operator approval,
- force-push is not used unless explicitly instructed.

Stress-test:

```text
以下情况必须使用 branch + PR
```

and:

```text
除非操作者明确指示，否则不要强制推送（force-push）。
```

Check that the modal force matches the English.

## 4. Registry records

Please verify:

- canonical registry records are JSON-per-record,
- CSV is legacy/optional rollup only,
- routine visitors create JSON records rather than edit shared CSV ledgers,
- all canonical paths remain exactly unchanged,
- CSV may remain as a human-readable index and may be regenerated or updated later,
- routine visitor writes do not require CSV updates,
- operator-supplied missing tags may create accepted records with `created_by = operator` and `status = accepted`,
- AI-generated tags must go under `registry/tags/proposed/`,
- canonical naming patterns remain unchanged,
- JSON examples remain machine-compatible and are not localized internally.

The Chinese visitor-rule code block currently translates only the human-facing instructions:

```text
创建 JSON 记录
不要编辑 CSV
在签退记录中说明已创建的记录
```

Please confirm this is natural and does not look like a machine-readable block that should have remained English.

## Cross-file consistency checks

Please compare the four files for consistency around:

- `accepted` versus `proposed`,
- operator authority,
- branch versus `branch + PR`,
- public/reference-only workspace restrictions,
- default-branch routine writes,
- registry JSON versus CSV,
- review surrogate versus canonical binary,
- `signoff`,
- `canonical`,
- `manifest`,
- force-push.

Do not erase deliberate source distinctions simply to make terminology look identical.

## Review format

Please return two parts.

### Part A - overall assessment

Cover:

1. naturalness,
2. developer/agent-facing register,
3. protocol parity,
4. modal-force parity,
5. cross-file consistency,
6. machine/path invariance,
7. whether the cluster is ready after listed edits.

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

Please explicitly flag any recommendation that would alter behaviour rather than merely clarify the Chinese.

## Final verdict

End with one of:

```text
READY AFTER LISTED EDITS
READY AS WRITTEN
REQUIRES ANOTHER REVIEW PASS
```

If another pass is required, identify the blocking protocol issue precisely.
