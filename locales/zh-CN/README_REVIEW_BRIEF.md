# Simplified-Chinese README Review Brief

Target locale: `zh-CN`  
Review target: [`README.md`](README.md)  
Canonical source: [`../../README.md`](../../README.md)  
Status: language/cultural review before publishing the Chinese front door

## What we need from the reviewer

Please review the Simplified-Chinese README as a complete piece of Chinese technical writing, not merely sentence-by-sentence translation.

The translation should preserve the meaning and safety boundaries of the English source, but it should sound as though it was written naturally for a mainland Simplified-Chinese reader.

We are especially interested in:

- naturalness and rhythm,
- cultural fit,
- technical precision,
- preservation of the author's informal human voice,
- metaphor quality,
- semantic parity with the English source,
- consistency with the reviewed glossary.

Do not redesign LabNote or weaken/strengthen protocol claims merely to make the prose smoother. If the English source itself creates a genuine ambiguity, flag it.

## Register target

Use a **developer-oriented but accessible** register.

The README should feel:

- clear,
- human,
- technically competent,
- conversational where the English is conversational,
- slightly informal in the personal origin section,
- precise where safety/workflow behaviour is described.

Please avoid making it sound like:

- corporate marketing copy,
- government or institutional documentation,
- a literal machine translation,
- gaming UI text,
- academic prose where the source is personal,
- oversimplified consumer-app copy.

## Terminology baseline

Use [`GLOSSARY.md`](GLOSSARY.md) as the reviewed baseline.

High-risk terminology should not be changed casually. If you recommend changing one of the frozen terms, explicitly explain why the current reviewed term fails in this README context.

Important examples include:

```text
visitor -> 访客会话
lobby -> 入口区
packet -> 工作包
registry -> 登记库
signoff -> 签退记录
provenance -> 溯源信息
ask-gate -> 询问节点
controlled live workspace -> 受控工作区
ledger -> 工作台账
canonical -> 基准（canonical）
human-in-the-loop -> 人在回路（Human-in-the-loop, HITL）
```

Machine identifiers, paths, Git terms, status values and product names must remain invariant where the localization contract requires it.

## Specific passages to stress-test

### 1. Opening promise

Does the opening quickly tell a Chinese reader what LabNote is and why they might care, without sounding promotional or vague?

### 2. "Why I made it"

This section intentionally uses a personal, slightly exasperated voice. Please check whether the Chinese sounds like a real person describing a genuine workflow problem.

In particular, review phrases such as:

```text
说实话，我受够了一件事……
只为了让大家还在看同一张地图。
于是就有了 LabNote。
拿它出来掸掸灰，再接着做。
```

Please preserve personality where possible rather than flattening the section into formal documentation.

### 3. Blank-room / labelled-drawers metaphor

English source concept:

```text
Most AI work starts in a blank room.
LabNote gives your AI a room with labels on the drawers.
```

Current Chinese:

```text
大多数 AI 工作，都是从一间空屋子开始的。
LabNote 给 AI 的，是一间抽屉都贴好标签的屋子。
```

Please judge whether this metaphor feels natural and memorable in Chinese or whether a small rewrite would preserve the image better.

### 4. "No shared-memory theatre"

Current Chinese:

```text
也不演“共享记忆”这出戏。
```

The English line is deliberately dry and mildly sardonic. Please check whether this Chinese line preserves that tone without sounding childish, hostile or confusing.

### 5. "Ledger, not the warehouse"

Current Chinese:

```text
LabNote 是工作台账（ledger），不是大型资料仓库（warehouse）。
```

We deliberately use `大型资料仓库` here because Chinese also commonly uses `仓库` for a Git repository. Please check whether this wording preserves the intended contrast: LabNote stores small inspectable records and references, not the heavy source corpus itself.

### 6. Motto

English:

```text
Mind the gap. Mark the crossing.
```

Current Chinese candidate:

```text
留意间隙，标记交接处。
```

This is **not frozen**. Please propose alternatives if you can preserve the compact rhythm and the underlying idea of noticing continuity gaps and marking the handoff/crossing between sessions.

The English motto will remain visible alongside the Chinese version.

### 7. Acquisition prompt

Please ensure this remains something a Chinese user could naturally paste into an AI chat:

```text
请帮我为这个项目设置 CapstanAI LabNote。先判断你目前具备哪些访问能力，再向我推荐最简单、最安全的方式。如果需要我运行任何终端命令，请先解释命令的作用。
```

Do not weaken the requirement that the AI assess its available access first or explain terminal commands before the user runs them.

### 8. Safety and authority language

Please verify that Chinese wording preserves all of the following:

- final decision authority remains human-held,
- public/reference-only copies must not receive private runtime material,
- AI behaviour is bounded,
- ask-gates require stopping and asking rather than guessing,
- operator approval remains required where the English says it is required,
- credentials/private keys/tokens must not be stored in LabNote.

## Review format

Please return two parts.

### Part A - overall assessment

Give a short assessment covering:

1. naturalness,
2. register,
3. cultural fit,
4. voice,
5. semantic parity,
6. whether it is ready to publish after your proposed edits.

### Part B - recommended edits

For each passage you would change, use:

```text
Section:
Current Chinese:
Recommended Chinese:
Reason:
Semantic effect: unchanged / clearer / potential meaning change
Confidence: high / medium / low
```

Please do not rewrite passages merely for stylistic preference if the current Chinese is already natural and faithful.

## Final requested verdict

End with one of:

```text
READY AFTER LISTED EDITS
READY AS WRITTEN
REQUIRES ANOTHER REVIEW PASS
```

If you choose `REQUIRES ANOTHER REVIEW PASS`, explain the blocking issues clearly.
