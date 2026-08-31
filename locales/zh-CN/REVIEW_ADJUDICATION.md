# Simplified-Chinese Terminology Review Adjudication

Date: 2026-08-31
Locale: `zh-CN`
Status: **first high-risk terminology gate completed**

## Purpose

This note records the outcome of the first external Simplified-Chinese terminology review for CapstanAI - LabNote and the protocol-fidelity adjudication applied before freezing the high-risk baseline.

The external reviewer focused on naturalness, mainland-China technical usage, connotation and cultural alignment. The LabNote-side adjudication then checked those recommendations against the canonical English workflow meaning.

The resulting terms are maintained in `GLOSSARY.md`.

## Recommendations accepted substantially as proposed

The following changes were adopted because they improve Chinese naturalness without changing workflow meaning:

- `human operator / operator`: prefer `人类操作者 / 操作者` over `人工操作者`.
- `lobby`: use `入口区` rather than `入口大厅` to avoid hotel/chat/game-lobby connotations.
- `registry`: use `登记库` rather than `登记簿` to better signal a digital structured record collection.
- `signoff`: retain `签退记录`; it communicates completion/exit without implying approval.
- `human-held authority`: use `最终决定权由人类掌握`.
- `bounded action`: use `受限操作` rather than the more mathematical `有界操作`.
- `fail closed`: use `默认拒绝（不明确即停止）`, with a longer explanatory form where useful.
- `controlled live workspace`: shorten to `受控工作区`.
- `human-in-the-loop`: retain `人在回路（Human-in-the-loop, HITL）`.
- `ledger`: use `工作台账`, retaining `ledger` on first use.
- `locale`: use `区域设置（locale）`.
- `protocol parity` / `behavioural parity`: use `协议一致性` / `行为一致性`.
- `dormant`: use `休眠` as the default explanation.
- `retired`: use `已停用` rather than `已退役`.

## Recommendations accepted with protocol-fidelity adjustment

### `ask-gate`

External recommendation: `人工确认节点（ask-gate）`.

Adjudicated baseline: `询问节点（ask-gate）`.

Reason: an ask-gate is broader than confirmation or approval. The AI may need to stop and ask for missing information, permission, a choice, or confirmation. Translating it solely as a confirmation node would narrow the control primitive.

### `evidence`

External recommendation: prefer `佐证材料` or `依据材料` to avoid the legal tone of `证据`.

Adjudicated baseline: context-sensitive `依据材料 / 证据`.

Reason: LabNote is intended for software/research work but also investigations and casework. `佐证材料` can imply corroborating material and could incorrectly demote primary evidence. Use `依据材料` in neutral technical/research contexts and `证据` where the evidentiary meaning is real.

### `open`

External recommendation: `开放中`.

Adjudicated baseline: `未关闭` as the explanation of machine value `open`.

Reason: `开放中` can imply publicly available/open access. `待处理` can imply action is necessarily required. `未关闭` is less elegant but more faithful to the generic workflow state, especially because `in_progress` already exists separately.

### `canonical`

External recommendation: `基准（canonical）`.

Adjudicated baseline: accepted as the default localization term, with an explicit definition and English retained on first use.

Reason: `基准` avoids the potentially regulatory feel of `规范`, but can also mean benchmark/baseline. LabNote therefore defines it explicitly as the authoritative project form, path, record or source.

### `human relay`

External recommendation: `人工中转` or `人工转递`.

Adjudicated baseline: `人工转递`.

Reason: both are understandable. `人工转递` stays closer to the project action of carrying a message or notification onward and relies less on a logistics/transshipment metaphor.

## Translation operating rule confirmed

For high-risk or cross-language project terms, retain the canonical English term in parentheses on first use **per file**.

Repeat the English later only when:

- a section is likely to be read independently, or
- the localized term could otherwise become ambiguous.

This keeps cross-language mapping visible without turning every localized document into permanently bilingual prose.

## Glossary lifecycle confirmed

The terminology model is hybrid:

1. Freeze the high-risk semantic spine before broad translation.
2. Keep the wider glossary live.
3. Review newly encountered terms before widespread use.
4. Treat any later change to a frozen term as a controlled terminology revision.
5. When a frozen term changes, audit all existing localized occurrences for consistency.

## Next gate

The terminology gate is now complete enough to begin translation of the Simplified-Chinese front door:

```text
README
ACQUISITION
quickstart
branding
privacy
security
contributing
```

Operational protocol files should follow after the front-door translation receives its own language-quality and protocol-parity review.
