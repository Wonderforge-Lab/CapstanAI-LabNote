# CapstanAI - LabNote 简体中文术语表

Status: **reviewed baseline for high-risk terms; wider glossary remains live**
Locale: `zh-CN`
Canonical source language: `en`

This glossary is the terminology gate for the first Simplified-Chinese localization of CapstanAI - LabNote.

The high-risk terms below have received an external Simplified-Chinese terminology review supplied through the human operator and a protocol-fidelity adjudication. They are now the stable baseline for broad translation. The wider glossary remains live: newly encountered terms may be added, but should be reviewed before widespread use.

A later change to a frozen high-risk term is allowed, but it is a controlled terminology revision and must trigger a consistency sweep across existing localized files.

Machine identifiers shown in backticks remain unchanged in localized files.

## First-use rule

Use the canonical English term in parentheses on first use **per file** for high-risk or cross-language project terms. Repeat it later only when a section is reasonably likely to be read independently or ambiguity could otherwise arise.

Example:

```text
访客会话（visitor）
工作包（packet）
登记库（registry）
```

## Core terms

| Canonical English | Reviewed Simplified Chinese | Handling | Protocol meaning / review note |
| --- | --- | --- | --- |
| CapstanAI | CapstanAI | keep brand | Ecosystem/product-family name. Do not translate the mark. |
| LabNote | LabNote | keep brand | Product/component name. A Chinese explanation may follow on first use. |
| WonderForge | WonderForge | keep brand | Maker/studio mark. Do not replace with a translated brand name. |
| workspace | 工作区 | translate | The current usable copy of LabNote, whether local or remote. |
| human operator / operator | 人类操作者 / 操作者 | translate | Use `人类操作者` where humanness must be explicit, normally on first use; `操作者` is the natural short form. |
| AI session / assistant session | AI 会话 / 助手会话 | translate | One bounded AI interaction/session participating in the workflow. |
| visitor | 访客会话 | frozen high-risk term | **Not a person.** A labelled AI-session identity used for routing and provenance. Do not shorten to `访客` where it could imply a human guest. |
| visitor handle | 访客会话标识 | frozen high-risk term | Current-run identifier supplied or explicitly confirmed by the human operator. No handle, no write. |
| visitor profile | 访客会话资料 | translate | Small generic record describing a visitor/session identity. |
| lobby | 入口区 | frozen high-risk term | Deterministic entry area for visiting AI sessions. Prefer this over `入口大厅`, which can evoke hotels, games, or chat lobbies. Retain `lobby` on first use. |
| packet | 工作包 | frozen high-risk term | A bounded LabNote artifact carrying context, task, evidence/source material or instructions between sessions. Not a network packet. |
| datadrop | 资料投递 | frozen high-risk term | Deposit of source/context material into the LabNote workflow. Broader than raw computer data. |
| datadrop packet | 资料投递工作包 | frozen high-risk term | Packet used to deliver context, evidence/source material and requested work to another session. |
| response packet | 回复工作包 | translate | Structured AI response tied to a source packet. |
| message packet | 消息工作包 | translate | Directed note between visitor/session IDs. |
| handoff | 交接 | translate | Transfer of enough context/status/provenance for another AI session to continue coherently. |
| registry | 登记库 | frozen high-risk term | Canonical structured record area under `registry/`, primarily JSON-per-record. `库` signals a digital collection without implying the Windows Registry. |
| registry record | 登记记录 | translate | One JSON-per-record workflow state record. |
| signoff | 签退记录 | frozen high-risk term | End-of-visit completion record. **Not necessarily approval or acceptance.** |
| review | 审阅 | translate | Human or AI inspection of a response/artifact before status changes. |
| review note | 审阅记录 | translate | Record explaining a review decision when the reason matters. |
| relay | 转递 | frozen high-risk term | Carrying a message or needed action onward between sessions/people. |
| human relay | 人工转递 | frozen high-risk term | Human operator carries a notification/message onward because the repository itself does not send notifications. `人工中转` may be idiomatic, but `人工转递` stays closer to the project action and avoids over-emphasising a logistics metaphor. |
| provenance | 溯源信息 | frozen high-risk term | Trace of where work came from, what source/session produced it, and how it moved through the workflow. |
| route / routing | 路由 / 路由规则 | translate | Deterministic choice of where a packet, message or action goes. |
| notification | 通知 | translate | Structured indication that something needs attention or relay. LabNote itself does not autonomously send notifications. |

## Governance and safety terms

| Canonical English | Reviewed Simplified Chinese | Handling | Protocol meaning / review note |
| --- | --- | --- | --- |
| human-in-the-loop | 人在回路（Human-in-the-loop, HITL） | frozen high-risk term | Mainland technical usage is established. Human review/approval remains part of the control loop. |
| human-held authority | 最终决定权由人类掌握 | translate with care | Final decision authority remains with the human operator. Prefer `决定权` over `权限`, which can sound like access rights. |
| bounded action | 受限操作 | translate with care | AI actions are constrained by allowed paths, targets, stop conditions and gates. |
| deterministic entry | 确定性入口 | translate | All AI sessions enter through the same defined route. |
| ask-gate | 询问节点（ask-gate） | frozen high-risk term | Point at which the AI must stop and ask the human operator rather than infer or continue. Do **not** reduce this to approval/confirmation: the missing human input may be information, permission, choice or confirmation. |
| stop condition | 停止条件 | translate | Explicit condition requiring the AI to stop rather than improvise. |
| fail closed | 默认拒绝（不明确即停止） | translate by meaning | When permissions/tool access/routing are unclear, stop rather than assume permission. Longer explanatory prose may use `不明确时默认停止并拒绝继续`. |
| controlled live workspace | 受控工作区 | frozen high-risk term | Private or otherwise controlled workspace appropriate for live deposits under operator-approved rules. The live/running sense is normally supplied by context. |
| public/reference-only workspace | 公共/仅供参考工作区 | translate | Public template/reference copy where private runtime material must not be deposited. |
| routine deposit | 常规投递 | translate | Ordinary packet, response, message, signoff or small record deposit under established rules. |
| deposit | 投递 | translate | Place a LabNote artifact into the appropriate workflow location. Not a financial deposit. |
| direct write | 直接写入 | translate | Write to the live workspace default branch without creating a task branch when rules permit. |
| branch + PR | 分支 + 拉取请求（PR） | translate explanation, keep Git term | Required route for policy, procedure, structure, code, cleanup, risky/bulky changes, many edits, or explicit review. |
| default branch | 默认分支 | translate | Repository default branch. |
| approval | 批准 | translate | Explicit human authorization where required. Do not confuse with the `accepted` workflow state unless context says so. |

## State and registry terms

Machine status values remain exactly as written in canonical records. Chinese text may explain them but must not replace them.

| Canonical English | Reviewed Simplified Chinese explanation | Machine value handling |
| --- | --- | --- |
| new | 新建 / 新提交 | keep `new` |
| in_review | 审阅中 | keep `in_review` |
| answered | 已回复 | keep `answered` |
| superseded | 已被后续版本取代 | keep `superseded` |
| archived | 已归档 | keep `archived` |
| pending_review | 待审阅 | keep `pending_review` |
| accepted | 已接受 | keep `accepted` |
| rejected | 已拒绝 | keep `rejected` |
| open | 未关闭 | keep `open`; deliberately avoid `待处理` because an open record does not always require action, and avoid `开放中` where it could imply public availability |
| acknowledged | 已确认收到 | keep `acknowledged` |
| in_progress | 处理中 | keep `in_progress` |
| blocked | 受阻 | keep `blocked` |
| closed | 已关闭 | keep `closed` |
| proposed | 候选 | keep `proposed` |
| deprecated | 已弃用 | keep `deprecated` |
| dormant | 休眠 | keep `dormant`; `暂停活跃` may be used in explanatory prose when temporary inactivity needs emphasis |
| retired | 已停用 | keep `retired`; avoid `退役` for software/session records |

## Registry v1 溯源术语

下列为基准字段名和枚举值。在任何语言层中都必须保持其字面形式不变；只翻译周围的说明文字。

| Canonical English | 审阅后的简体中文说明 | 处理 | 协议含义 / 审阅说明 |
| --- | --- | --- | --- |
| `content_origin` | 内容来源类别 | 保留字段名 | 声明记录内容本身来自何处的类别。 |
| `source_refs` | 来源引用 | 保留字段名 | 用于指明第三方、网络或混合来源材料的具体出处。 |
| `source_note` | 来源说明 | 保留字段名 | 当 `content_origin` 为 `unknown` 时，必须说明不确定性；不能替代应有的 `source_refs`。 |
| `derivative_of` | 派生来源 | 保留字段名 | 本产物所源自的上游工作包或回复记录。 |
| `provenance_coverage` | 溯源与派生信息覆盖程度 | 保留字段名 | 记录中来源及派生关系被表示的完整程度。 |
| `operator_authored` | 由操作者（人类）撰写 | 保留枚举值 | 内容由人类操作者撰写或创作。 |
| `third_party` | 由非操作者的外部第三方提供或撰写 | 保留枚举值 | 内容并非由操作者提供或撰写。 |
| `web` | 来源于网络 | 保留枚举值 | 内容来源于网络。 |
| `model_generated` | 由 AI/模型生成 | 保留枚举值 | 内容由 AI 或模型生成。 |
| `mixed` | 多来源混合 | 保留枚举值 | 内容具有不止一种来源。 |
| `unknown` | 来源无法确定；必须说明不确定性 | 保留枚举值 | 需要非空的 `source_note`，但不应为了满足字段而虚构来源引用。 |

## Tag terms

| Canonical English | Reviewed Simplified Chinese | Handling | Note |
| --- | --- | --- | --- |
| tag | 标签 | translate | Human-readable categorization concept. |
| tag slug | 标签标识符（slug） | translate explanation, keep slug | Stable machine-facing label such as `human-in-the-loop`. |
| accepted tag | 已接受标签 | translate | Canonical accepted tag state. |
| proposed tag | 候选标签 | translate | AI-generated tag awaiting acceptance. Machine status remains `proposed`. |
| deprecated tag | 已弃用标签 | translate | Retired tag state. |

Tag slugs remain language-invariant. For example:

```text
human-in-the-loop
provenance
workflow-testing
```

Do not create Chinese slugs for the same semantic tags.

## Storage and evidence terms

| Canonical English | Reviewed Simplified Chinese | Handling | Protocol meaning / review note |
| --- | --- | --- | --- |
| ledger | 工作台账（ledger） | frozen high-risk term | LabNote metaphor: structured record of work, not a warehouse. `工作` reduces the accounting/bureaucratic feel of `台账` while retaining the ledger distinction. |
| warehouse | 仓库 | translate | In the phrase "the ledger, not the warehouse": heavy source material generally belongs elsewhere. |
| storage policy | 存储策略 | translate | Rules governing what belongs in the workspace and where bulky/private material may live. |
| corpus | 语料库 | translate | Larger source corpus or project material. |
| manifest | 清单 | translate | Lightweight index/description of bulky material before full import. |
| review surrogate | 审阅替代稿 | translate with care | Markdown/text representation created for review when the canonical original is binary. It is not the canonical binary. |
| source material | 来源材料 | translate | Material supplied for the current task/packet. |
| evidence | 依据材料 / 证据 | translate by context | Use `依据材料` for neutral technical/research supporting material. Use `证据` where material genuinely has evidentiary character, including investigation/casework contexts. Do not globally replace with `佐证材料`, which can imply corroboration and may demote primary evidence. |
| checksum | 校验和 | translate | Machine integrity value; algorithms such as SHA256 remain unchanged. |

## Localization terms

| Canonical English | Reviewed Simplified Chinese | Handling | Note |
| --- | --- | --- | --- |
| localization | 本地化 | translate | Adaptation to a target language/locale while preserving the shared workflow substrate. |
| locale | 区域设置（locale） | translate with English on first use | Locale code such as `zh-CN`. |
| canonical | 基准（canonical） | frozen high-risk term with definition | Default localization term. In LabNote it means the authoritative project form, path, record or source, not merely a benchmark. Keep English on first use where that authority distinction matters. |
| canonical source language | 基准源语言 | translate | English source from which supported translations are maintained. |
| language layer | 语言层 | translate | Localized interaction/presentation layer over one invariant workflow substrate. |
| protocol parity | 协议一致性 | translate | Localized route must preserve operational decisions and control semantics. |
| behavioural parity | 行为一致性 | translate | Fresh sessions using different locales should make materially equivalent workflow decisions. |

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
content_origin
source_refs
source_note
derivative_of
provenance_coverage
registry/packets/
registry/responses/
registry/visits/
registry/messages/
registry/notifications/
registry/tags/
```

Likewise, enum/status values remain English machine values even when surrounding explanatory prose is Chinese.

## Frozen high-risk baseline

The following terms are now stable enough to gate broad translation:

```text
human operator / operator     -> 人类操作者 / 操作者
visitor                       -> 访客会话
visitor handle                -> 访客会话标识
lobby                         -> 入口区
packet                        -> 工作包
datadrop                      -> 资料投递
registry                      -> 登记库
signoff                       -> 签退记录
relay                         -> 转递
human relay                   -> 人工转递
provenance                    -> 溯源信息
ask-gate                      -> 询问节点
controlled live workspace     -> 受控工作区
ledger                        -> 工作台账
canonical                     -> 基准 (retain canonical on first use)
human-in-the-loop             -> 人在回路 (Human-in-the-loop, HITL)
```

A change to one of these terms later is a controlled terminology revision, not an informal wording tweak.

## Review provenance

The first external Simplified-Chinese terminology review was supplied to the project through the human operator on 2026-08-31. The review tested naturalness, technical clarity, mainland-China usage, cultural connotation and protocol fit. Its recommendations were then adjudicated against the English LabNote workflow semantics before this baseline was frozen.

See [`../../docs/localization/ZH_CN_VALIDATION.md`](../../docs/localization/ZH_CN_VALIDATION.md) for the durable validation summary.
