# Simplified-Chinese Session / Connector / Relay Review Brief

Target locale: `zh-CN`

Review targets:

- `docs/visitor_lobby_model.md`
- `docs/CONNECTOR_SAFE_WORDING.md`
- `docs/CONNECTOR_LIMITATIONS.md`
- `notifications/RELAY_PROTOCOL.md`

Status: language and protocol-parity review before these Chinese operational companions are marked reviewed.

## Review goal

Please review these four files as one operational cluster covering visitor/session identity, connector-safe wording, connector limitations, and human relay notifications.

Natural Chinese matters, but semantic and behavioural parity with the English canonical source is primary.

Do not redesign the protocol merely to make terminology more familiar.

## 1. Visitor lobby model

The most important semantic constraint is:

```text
A visitor is not a person. It is a labelled session identity used for routing and provenance.
```

Current Chinese:

```text
访客会话（visitor）不是一个人。它是一个带标签的会话身份，用于路由和溯源信息（provenance）。
```

Please verify that this cannot reasonably be read as a human guest identity.

Also verify that visitors:

- use the current-run visitor handle supplied or explicitly confirmed by the human operator,
- register a visitor profile only if needed,
- check messages on entry,
- perform the requested work,
- record created or answered messages,
- sign off before leaving,
- do not invent a visitor handle,
- do not silently reuse a handle from previous conversation context,
- keep visitor profiles under `lobby/visitors/` small and generic.

Please check consistency with the frozen glossary terms:

- visitor -> `访客会话`
- visitor handle -> `访客会话标识`
- visitor profile -> `访客会话资料`
- lobby -> `入口区`
- provenance -> `溯源信息`
- signoff -> `签退记录`

## 2. Connector-safe wording

This file is not a general ban on metaphor or project language.

It says that repository-facing files written through connectors should prefer clear technical language where metaphor-heavy wording could be misread by connector safety filters.

Please verify that the Chinese preserves that narrow compatibility purpose.

Review the proposed Chinese explanations for:

```text
early-stage model -> 早期阶段模型
small experimental model -> 小型实验模型
supervised guardrail stack -> 受监督的护栏栈
local teacher model -> 本地教师模型
resident agent -> 常驻智能体
deterministic scaffold -> 确定性框架
review layer -> 审阅层
safety wrapper -> 安全封装层
```

The English terms remain visible intentionally for cross-language technical reference.

Please flag any Chinese term that is technically unnatural, misleading, or carries a stronger safety/research connotation than the English.

## 3. Connector limitations

Please verify these source semantics precisely:

- different AI sessions may have different tool access,
- some can read/write files directly,
- some can only suggest patches,
- some cannot safely handle archives or large imports,
- when tool access is unclear, LabNote should **fail closed**,
- connector strengths and weaknesses remain descriptive rather than guaranteed capabilities,
- awkward full archive/corpus imports default to manifest/index unless operator-approved and safely supported,
- ordinary registry work prefers JSON-per-record over shared CSV,
- unclear registry format/path means stop and report rather than inventing a format,
- unsafe connector operations result in a clear signoff/report rather than improvisation,
- a stopped run with a clear explanation counts as successful safety behaviour.

Stress-test the Chinese:

```text
当工具访问能力不明确时，CapstanAI - LabNote 应默认拒绝（fail closed），而不是猜测工具能力。
```

Please confirm that `默认拒绝` communicates the operational meaning of fail-closed clearly enough. If a better mainland technical phrasing exists, propose it, but do not weaken the stop/refuse behaviour.

Also review:

```text
宁可停止，不要临场发挥
```

for naturalness and technical register.

## 4. Human relay notification

Machine-facing field names and status values intentionally remain unchanged:

```text
notification_id:
from_visitor_id:
to_visitor_id:
message_id:
created_at:
status: needed | told_to_human | delivered_by_human | confirmed | cancelled
needs_human_action:
summary:
```

Only human-facing Markdown section headings are localized.

Please verify that:

- `人工转递通知` naturally expresses Human Relay Notification,
- the translated section headings preserve the original meaning,
- none of the status values or field names are translated,
- the final sentence preserves the critical system boundary:

```text
The repository does not send notifications. The human operator does.
```

Current Chinese:

```text
仓库本身不会发送通知。由操作者负责实际转递。
```

Please verify that this does not imply an automated notification service exists elsewhere. The intended meaning is that a human performs the relay.

## Machine/path invariance

Do not translate or alter:

- `lobby/visitors/`,
- notification field names,
- notification status values,
- repository paths,
- machine IDs.

## Cross-file consistency

Please compare for consistency around:

- visitor/session identity,
- human operator,
- human relay,
- fail closed,
- stop/report behaviour,
- connector capability uncertainty,
- provenance,
- signoff,
- machine-readable fields.

## Review format

Please return two parts.

### Part A - overall assessment

Cover:

1. naturalness,
2. developer/agent-facing register,
3. protocol parity,
4. visitor-identity clarity,
5. connector fail-closed parity,
6. relay/human-boundary parity,
7. machine/path invariance,
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

Explicitly flag any recommendation that would alter source behaviour.

## Final verdict

End with one of:

```text
READY AFTER LISTED EDITS
READY AS WRITTEN
REQUIRES ANOTHER REVIEW PASS
```

If another pass is needed, identify the blocking protocol issue precisely.
