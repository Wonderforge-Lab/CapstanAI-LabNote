# Simplified-Chinese End-to-End Compatibility Review Adjudication

Status: reviewed
Locale: `zh-CN`

## External review verdict

The end-to-end routine-deposit specimen received the external verdict:

```text
READY AFTER LISTED EDITS
```

The reviewer passed:

- naturalness,
- end-to-end protocol parity,
- Markdown-template parity,
- JSON schema compatibility,
- machine/status/path invariance,
- signoff semantics,
- behavioural compatibility.

The reviewer proposed one wording change:

```text
依据材料 / 来源材料
->
佐证材料 / 来源材料
```

## Adjudication

The proposed wording change was **not adopted**.

The reviewed and frozen `zh-CN` glossary explicitly defines `evidence` as context-sensitive:

```text
依据材料 / 证据
```

It further states that `佐证材料` must not be used as a global replacement because it can imply corroboration and may demote primary evidence.

The reviewed Markdown template layer therefore retains:

```text
## 依据材料 / 来源材料
```

The worked compatibility example remains aligned with that reviewed template and glossary decision.

## Final disposition

The specimen is accepted as reviewed **without changing the evidence/source heading**.

No machine-facing field names, status values, IDs, JSON keys, or runtime paths were changed.

The specimen demonstrates that Simplified-Chinese Markdown instructions and free-text content can coexist with canonical English machine structure and canonical runtime storage paths.
