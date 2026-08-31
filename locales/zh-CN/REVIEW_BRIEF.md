# Simplified-Chinese Terminology Review Brief

Target locale: `zh-CN`
Review target: [`GLOSSARY.md`](GLOSSARY.md)
Status: terminology gate before broad translation

## What we need from the reviewer

Please review the proposed Simplified-Chinese terminology for naturalness, technical clarity, cultural alignment and consistency.

The goal is **not** to redesign CapstanAI - LabNote or freely reinterpret its protocol. The English protocol meaning is the reference constraint. Where the English concept itself is ambiguous, please flag that explicitly rather than silently choosing a different meaning.

## Architecture to preserve

CapstanAI - LabNote uses one canonical workflow substrate with localized language surfaces.

The following remain language-invariant:

- repository paths and filenames used by the workflow,
- JSON keys,
- enum/status values,
- IDs,
- tag slugs,
- Git commands and flags,
- machine-readable configuration keys and values.

Chinese localization may change prose, headings, explanations and template section labels, but must not create a parallel Chinese protocol.

Example:

```text
packet_id:
status: new | in_review | answered | superseded | archived

## 背景
## 任务
```

The headings may be Chinese. `packet_id` and the status values remain canonical.

## Important semantic traps

Please pay special attention to these distinctions:

### `visitor`

A visitor is **not a human guest**. It is a labelled AI-session identity used for routing and provenance.

### `signoff`

A signoff is an end-of-visit completion record. It does **not automatically mean approval or acceptance**.

### `registry`

The registry is the structured record area under `registry/`, primarily JSON-per-record. Avoid a translation that misleadingly evokes only the Windows Registry.

### `packet`

A LabNote packet is a bounded work/context artifact passed between sessions. It is not specifically a network packet.

### `relay`

Human relay means the human operator carries a message or notification onward because the repository itself does not send notifications.

### `ask-gate`

An ask-gate is a control point where the AI must stop and ask the human instead of guessing or continuing.

### human authority

The human operator retains final authority. Chinese wording must not soften stop conditions, approval requirements or human-review gates.

## Review requested

For each glossary term that needs adjustment, please provide:

```text
Canonical English term:
Current proposed Chinese:
Recommended Chinese:
Reason:
Connotation / cultural note:
Keep English on first use? yes/no
Confidence: high / medium / low
```

You do not need to comment on terms that are already natural and unambiguous unless doing so helps establish a consistent style.

## Broader questions

Please also give a short opinion on:

1. Whether the overall register should be more developer-oriented, research-oriented, or general-user friendly.
2. Whether `入口大厅` is a sensible rendering of the project metaphor `lobby`, or whether another term would better signal deterministic AI-session entry.
3. Whether `工作包` is suitable for `packet`, or whether `资料包`, `任务包`, or another term is clearer.
4. Whether `登记簿` is suitable for `registry` in this architecture.
5. Whether `签退记录` correctly communicates `signoff` without implying approval.
6. Whether `人在回路` is the best Simplified-Chinese technical rendering for Human-in-the-loop in this context.
7. Whether `人工操作者` sounds natural for the human operator who retains workflow authority.
8. Any term that would sound translated, bureaucratic, childish, gaming-oriented, legally overstrong, or otherwise culturally odd to a mainland Simplified-Chinese technical reader.

## What comes next

After terminology review, the accepted glossary will gate translation of:

```text
README
acquisition / quickstart
AI entrypoint
lobby workflow
policies
routing / review docs
templates
worked examples
```

Broad translation should not begin until the high-risk terms are stable enough to avoid propagating inconsistent wording across the repository.
