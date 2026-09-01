# Simplified-Chinese Markdown Template Layer Review Brief

Target locale: `zh-CN`

Review targets:

- `templates/datadrop_packet.md`
- `templates/ai_response_packet.md`
- `templates/message_packet.md`
- `templates/notification_request.md`
- `templates/review_note.md`
- `templates/visit_signoff.md`
- `templates/visitor_registration.md`

Status: language and protocol-parity review before the Chinese Markdown template layer is marked reviewed.

## Architecture to preserve

These are localized Markdown companion templates over the same canonical LabNote protocol.

The Chinese version may translate:

- document titles,
- Markdown section headings,
- brief human-facing explanatory notes.

The Chinese version must **not** translate or alter:

- field names,
- JSON-related identifiers,
- status values,
- enum values,
- IDs,
- canonical paths,
- session-family values,
- machine-readable semantics.

The repository's `.json` templates remain canonical and are intentionally **not duplicated as translated JSON templates** under `locales/zh-CN/`.

## Cross-template invariant audit

Please verify that every machine-facing line is identical in meaning and spelling to the English source.

Examples include:

```text
packet_id:
status: new | in_review | answered | superseded | archived
```

```text
status: pending_review | accepted | rejected | archived
confidence: low | medium | high
response_type: answer | critique | synthesis | counterproposal | review
```

```text
status: open | acknowledged | in_progress | answered | blocked | closed | archived
needs_human_relay:
```

```text
status: needed | told_to_human | delivered_by_human | confirmed | cancelled
```

```text
decision: accepted | rejected | in_review | archived | superseded
```

```text
session_family: chatgpt | codex | claude | claude-code | local-llm | other
status: registered | active | dormant | retired | superseded
```

No Chinese substitute should appear inside these machine fields or enum sets.

## 1. Datadrop packet

Current title:

```text
资料投递工作包
```

Please verify this remains consistent with the frozen glossary:

- datadrop -> `资料投递`
- packet -> `工作包`

Current headings:

```text
背景
任务
依据材料 / 来源材料
给接收会话的问题
请求的输出
备注
```

Please check whether `依据材料 / 来源材料` naturally preserves the broad English `Evidence / Source Material` without demoting primary evidence or sounding legalistic.

## 2. AI response packet

Current title:

```text
AI 回复工作包
```

Please review these headings in particular:

```text
不确定项
建议的下一步
需提升 / 归档的文件
整理说明
```

The English source says:

```text
Uncertainties
Recommended Next Step
Files To Promote / Archive
Housekeeping Notes
```

`promote` here means moving/recognizing files as work worth promoting onward in the LabNote workflow. It does not mean marketing promotion or a Git operation. Please propose a more natural Chinese heading if `需提升 / 归档的文件` is awkward or misleading, without inventing new protocol meaning.

Likewise, check whether `整理说明` is the best concise rendering of `Housekeeping Notes` in this operational context.

## 3. Message packet

Unlike `messages/MESSAGE_FORMAT.md`, this file **is** the concrete `message_packet.md` artifact template.

Therefore the current title is intentionally:

```text
消息工作包
```

Please verify that this is natural and does not recreate the earlier confusion around the format-specification file.

The machine field/status block must remain unchanged.

## 4. Notification request

Current title:

```text
人工转递通知
```

Headings:

```text
需要转递什么
需要让谁知道
为什么重要
需要什么确认
```

Please compare with the already reviewed `notifications/RELAY_PROTOCOL.md` wording for consistency.

## 5. Review note

Current title:

```text
审阅记录
```

Current headings:

```text
决策摘要
理由
后续跟进
整理说明
```

Please verify that `理由` accurately conveys `Reasoning` in a decision record, and whether `整理说明` remains appropriate for `Housekeeping Notes`.

Final human authority remains governed by the reviewed workflow; this template must not imply AI authority merely because the `reviewer:` field is language-invariant.

## 6. Visit signoff

Current title:

```text
访问签退记录
```

Please check whether this is the most natural technical rendering of `Visit Signoff` given the frozen terms:

- visit -> access/visit record concept,
- signoff -> `签退记录`.

Headings:

```text
已完成工作
未结事项
转递说明
签退
```

Please flag any wording that could make `signoff` sound like cryptographic signing, approval authority, or employment attendance rather than closing a visitor/session run.

## 7. Visitor registration

Current title:

```text
访客会话登记
```

Current headings:

```text
适用范围
已知上下文
备注
```

Please verify that `适用范围` is natural for the English `Scope` in a visitor/session profile and that `访客会话登记` clearly refers to registering a session identity, not a human guest.

## Compatibility test

A Simplified-Chinese AI filling these templates should be able to produce artifacts that remain structurally compatible with English LabNote tooling and records.

Please explicitly check that translating the Markdown headings would not cause the AI to translate field names or enum values by analogy.

## Review format

Please return two parts.

### Part A - overall assessment

Cover:

1. naturalness,
2. developer/agent-facing register,
3. protocol parity,
4. field/enum invariance,
5. cross-template terminology consistency,
6. artifact compatibility,
7. readiness.

### Part B - recommended edits

For each change:

```text
File:
Section / heading:
Current Chinese:
Recommended Chinese:
Reason:
Protocol effect: unchanged / clearer / potential behaviour change
Confidence: high / medium / low
```

Do not rewrite natural headings merely for preference.

## Final verdict

End with one of:

```text
READY AFTER LISTED EDITS
READY AS WRITTEN
REQUIRES ANOTHER REVIEW PASS
```

If another pass is required, identify the blocking language or compatibility issue precisely.
