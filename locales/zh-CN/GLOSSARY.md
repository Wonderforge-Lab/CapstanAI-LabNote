# CapstanAI - LabNote 简体中文术语表

Status: **provisional - requires Chinese-language nuance and cultural review**
Locale: `zh-CN`
Canonical source language: `en`

This glossary is the terminology gate for the first Simplified-Chinese localization of CapstanAI - LabNote.

The Chinese renderings below are working proposals, not final canonical translations. Reviewers should challenge wording, register, ambiguity and cultural fit freely while preserving the protocol meaning in the final column.

Machine identifiers shown in backticks remain unchanged in localized files.

## Core terms

| Canonical English | Proposed Simplified Chinese | Handling | Protocol meaning / review note |
| --- | --- | --- | --- |
| CapstanAI | CapstanAI | keep brand | Ecosystem/product-family name. Do not translate the mark. |
| LabNote | LabNote | keep brand | Product/component name. A Chinese explanation may follow on first use. |
| WonderForge | WonderForge | keep brand | Maker/studio mark. Do not replace with a translated brand name. |
| workspace | 工作区 | translate | The current usable copy of LabNote, whether local or remote. |
| human operator / operator | 人工操作者 / 操作者 | translate | The human who holds authority over the current LabNote workflow. Review whether a more natural term conveys authority without sounding mechanical. |
| AI session / assistant session | AI 会话 / 助手会话 | translate | One bounded AI interaction/session participating in the workflow. |
| visitor | 访客会话 | translate with care | **Not a person.** A labelled AI-session identity used for routing and provenance. The Chinese term must not imply an external human guest. |
| visitor handle | 访客会话标识 | translate with care | Current-run identifier supplied or explicitly confirmed by the human operator. No handle, no write. |
| visitor profile | 访客会话资料 | translate | Small generic record describing a visitor/session identity. |
| lobby | 入口大厅 | translate with care | Deterministic entry area for visiting AI sessions. The project uses a room/lobby metaphor, but the Chinese term must still signal workflow entry rather than a social chat room. |
| packet | 工作包 | translate with care | A bounded LabNote artifact carrying context, task, evidence or instructions between sessions. Not a network packet. Review whether `工作包`, `资料包`, or another term is clearest. |
| datadrop | 资料投递 | translate with care | Deposit of source/context material into the LabNote workflow. Broader than raw computer data. |
| datadrop packet | 资料投递工作包 | translate with care | Packet used to deliver context, evidence, source material and requested work to another session. |
| response packet | 回复工作包 | translate with care | Structured AI response tied to a source packet. |
| message packet | 消息工作包 | translate with care | Directed note between visitor/session IDs. |
| handoff | 交接 | translate | Transfer of enough context/status/provenance for another AI session to continue coherently. |
| registry | 登记簿 | translate with care | Canonical collection of small structured records under `registry/`. Avoid Windows Registry connotations if possible. |
| registry record | 登记记录 | translate | One JSON-per-record workflow state record. |
| signoff | 签退记录 | translate with care | End-of-visit completion record. **Not necessarily approval or acceptance.** The term should signal that a session is leaving a trace before stopping. |
| review | 审阅 | translate | Human or AI inspection of a response/artifact before status changes. |
| review note | 审阅记录 | translate | Record explaining a review decision when the reason matters. |
| relay | 转递 | translate | Carrying a message or needed action onward between sessions/people. |
| human relay | 人工转递 | translate with care | Human operator carries a notification/message because the repository itself does not send notifications. |
| provenance | 溯源信息 | translate with care | Trace of where work came from, what source/session produced it, and how it moved through the workflow. |
| route / routing | 路由 / 路由规则 | translate | Deterministic choice of where a packet, message or action goes. Technical `路由` is acceptable if natural for the target audience. |
| notification | 通知 | translate | Structured indication that something needs attention or relay. LabNote itself does not autonomously send notifications. |

## Governance and safety terms

| Canonical English | Proposed Simplified Chinese | Handling | Protocol meaning / review note |
| --- | --- | --- | --- |
| human-in-the-loop | 人在回路（Human-in-the-loop, HITL） | translate + retain English on first use | Human review/approval remains part of the control loop. Confirm preferred mainland technical usage. |
| human-held authority | 人类持有最终权限 | translate with care | Final authority remains with the human operator. Wording must not suggest AI co-equality in final approval. |
| bounded action | 有界操作 | translate with care | AI actions are constrained by allowed paths, targets, stop conditions and gates. Review whether `受限操作` is more natural without losing the formal sense. |
| deterministic entry | 确定性入口 | translate | All AI sessions enter through the same defined route. |
| ask-gate | 询问门控 | translate with care | Point at which the AI must stop and ask the human rather than infer/continue. This is a project control term, not a generic conversational question. |
| stop condition | 停止条件 | translate | Explicit condition requiring the AI to stop rather than improvise. |
| fail closed | 不明确时默认停止并拒绝继续 | translate by meaning | When permissions/tool access/routing are unclear, stop rather than assume permission. Avoid a literal translation that sounds like software crash behaviour. |
| controlled live workspace | 受控运行工作区 | translate with care | Private or otherwise controlled workspace appropriate for live deposits under operator-approved rules. Review whether `受控工作区` is sufficient. |
| public/reference-only workspace | 公共/仅供参考工作区 | translate | Public template/reference copy where private runtime material must not be deposited. |
| routine deposit | 常规投递 | translate | Ordinary packet, response, message, signoff or small record deposit under established rules. |
| deposit | 投递 | translate | Place a LabNote artifact into the appropriate workflow location. Not financial deposit. |
| direct write | 直接写入 | translate | Write to the live workspace default branch without creating a task branch when rules permit. |
| branch + PR | 分支 + 拉取请求（PR） | translate explanation, keep Git term | Required route for policy, procedure, structure, code, cleanup, risky/bulky changes, many edits, or explicit review. |
| default branch | 默认分支 | translate | Repository default branch. |
| approval | 批准 | translate | Explicit human authorization where required. Do not confuse with `accepted` workflow state unless context says so. |

## State and registry terms

Machine status values remain exactly as written in canonical records. Chinese text may explain them but must not replace them.

| Canonical English | Proposed Simplified Chinese explanation | Machine value handling |
| --- | --- | --- |
| new | 新建 / 新提交 | keep `new` |
| in_review | 审阅中 | keep `in_review` |
| answered | 已回复 | keep `answered` |
| superseded | 已被后续版本取代 | keep `superseded` |
| archived | 已归档 | keep `archived` |
| pending_review | 待审阅 | keep `pending_review` |
| accepted | 已接受 | keep `accepted` |
| rejected | 已拒绝 | keep `rejected` |
| open | 未关闭 / 待处理 | keep `open` |
| acknowledged | 已确认收到 | keep `acknowledged` |
| in_progress | 处理中 | keep `in_progress` |
| blocked | 受阻 | keep `blocked` |
| closed | 已关闭 | keep `closed` |
| proposed | 候选 / 待审议 | keep `proposed` |
| deprecated | 已弃用 | keep `deprecated` |
| dormant | 暂停活跃 / 休眠 | keep `dormant`; review natural wording for session identity |
| retired | 已退役 / 已停用 | keep `retired`; review register |

## Tag terms

| Canonical English | Proposed Simplified Chinese | Handling | Note |
| --- | --- | --- | --- |
| tag | 标签 | translate | Human-readable categorization concept. |
| tag slug | 标签标识符 | translate explanation, keep slug | Stable machine-facing label such as `human-in-the-loop`. |
| accepted tag | 已接受标签 | translate | Canonical accepted tag state. |
| proposed tag | 候选标签 | translate with care | AI-generated tag awaiting acceptance. Machine status remains `proposed`. |
| deprecated tag | 已弃用标签 | translate | Retired tag state. |

Tag slugs remain language-invariant. For example:

```text
human-in-the-loop
provenance
workflow-testing
```

Do not create Chinese slugs for the same semantic tags.

## Storage and evidence terms

| Canonical English | Proposed Simplified Chinese | Handling | Protocol meaning / review note |
| --- | --- | --- | --- |
| ledger | 台账 / 记录簿 | translate with care | LabNote metaphor: structured record of work, not a warehouse. Review which term best fits software/research context. |
| warehouse | 仓库 | translate | In the phrase "the ledger, not the warehouse": heavy source material generally belongs elsewhere. |
| storage policy | 存储策略 | translate | Rules governing what belongs in the workspace and where bulky/private material may live. |
| corpus | 语料库 | translate | Larger source corpus or project material. |
| manifest | 清单 | translate | Lightweight index/description of bulky material before full import. |
| review surrogate | 审阅替代稿 | translate with care | Markdown/text representation created for review when the canonical original is binary. It is not the canonical binary. |
| source material | 来源材料 | translate | Material supplied for the current task/packet. |
| evidence | 证据 | translate | Evidence/source material associated with the task. Context may require a less legalistic term for ordinary technical work. |
| checksum | 校验和 | translate | Machine integrity value; algorithms such as SHA256 remain unchanged. |

## Localization terms

| Canonical English | Proposed Simplified Chinese | Handling | Note |
| --- | --- | --- | --- |
| localization | 本地化 | translate | Adaptation to a target language/locale while preserving the shared workflow substrate. |
| locale | 区域语言设置 / locale | translate with English on first use | Locale code such as `zh-CN`. Review preferred developer-facing terminology. |
| canonical | 规范 / 规范性 | translate by context | Means the authoritative workflow form, path, record or source. Avoid wording that sounds legally binding where it is merely project-canonical. |
| canonical source language | 规范源语言 | translate | English source from which supported translations are maintained. |
| language layer | 语言层 | translate | Localized interaction/presentation layer over one invariant workflow substrate. |
| protocol parity | 协议等价性 | translate | Localized route must preserve operational decisions and control semantics. |
| behavioural parity | 行为等价性 | translate | Fresh sessions using different locales should make materially equivalent workflow decisions. |

## Canonical identifiers that must not be translated

Examples include:

```text
packet_id
source_session
target_session
visitor_id
response_id
message_id
notification_id
status
created_at
response_expected
needs_human_relay
registry/packets/
registry/responses/
registry/visits/
registry/messages/
registry/notifications/
registry/tags/
```

Likewise, enum/status values remain English machine values even when surrounding explanatory prose is Chinese.

## Review questions for Chinese-language reviewers

Please review the proposed terms above for the following, without changing the underlying protocol meaning unless a genuine ambiguity in the English source is discovered:

1. Does the term sound natural to a Simplified-Chinese technical user?
2. Does it accidentally imply a human person where LabNote means an AI session?
3. Does it carry unwanted gaming, Windows, networking, legal, bureaucratic or financial connotations?
4. Would a different mainland-China technical term be more conventional?
5. Is the register too formal, too colloquial, or too literal?
6. Does the term preserve the distinction between approval, acceptance, signoff, review and relay?
7. Does the translation preserve human authority and stop/ask semantics?
8. Which English project terms should remain in parentheses on first use to help cross-language collaboration?

## Current high-risk terms

The following should receive special review before broad translation begins:

```text
visitor / visitor handle
lobby
packet / datadrop packet
registry
signoff
relay / human relay
provenance
ask-gate
controlled live workspace
ledger
canonical
```

These terms carry more workflow meaning than their everyday English equivalents suggest.
