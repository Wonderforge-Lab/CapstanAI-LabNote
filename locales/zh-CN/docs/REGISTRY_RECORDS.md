# 登记库记录

基准登记库记录每条对应一个 JSON 文件。JSON 是其关联 Markdown 产物的结构化索引、状态、关系和溯源封套；不要求复制产物正文。

权威字段、状态、生命周期、溯源和兼容性规则见英文基准 [Registry Contract v1](../../../docs/registry/REGISTRY_CONTRACT_V1.md)。`registry/schemas/` 下的 JSON 模式和 `scripts/validate_repo.py` 会校验这些规则。

## 基准路径

工作包：

```text
registry/packets/<year>/<packet_id>.json
```

回复：

```text
registry/responses/<year>/<response_id>.json
```

访问记录：

```text
registry/visits/<year>/<visit_id>.json
```

访客会话：

```text
registry/visitors/<visitor_id>.json
```

消息：

```text
registry/messages/open/<message_id>.json
registry/messages/answered/<message_id>.json
registry/messages/closed/<message_id>.json
registry/messages/archived/<message_id>.json
```

通知：

```text
registry/notifications/open/<notification_id>.json
registry/notifications/delivered/<notification_id>.json
registry/notifications/closed/<notification_id>.json
```

标签：

```text
registry/tags/proposed/<tag_slug>.json
registry/tags/accepted/<tag_slug>.json
registry/tags/deprecated/<tag_slug>.json
```

状态决定消息、通知或标签的存储分区。请使用该合同中按记录类型划分的生命周期表；不要自行发明新的状态或目录。

## 访客会话规则

对于常规访客会话工作：

```text
创建一条基准 JSON 记录
按需要创建或更新其关联产物
验证该记录
在签退记录中提及它
不要编辑 CSV 登记表
```

使用 `templates/` 中的对应文件作为起始封套。`examples/contract_v1/` 下经过检查、可安全公开的记录/产物配对，展示了完整的工作包、回复、消息和访问记录。

## 标签

标签是受控词汇记录，不是自由文本。

- 由会话创建的标签从 `registry/tags/proposed/` 开始。
- 候选标签不得在同一变更集中变为已接受标签。
- 仅当具备所需的接受元数据和 `acceptance_basis: operator_supplied` 时，操作者提供的标签才可被直接接受。这属于控制平面更改，必须使用 `branch + PR`。
- 记录只能使用能解析到候选或已接受标签记录的标签。

## 生成的兼容视图

CSV 登记表和 `registry/INDEX.md` 是生成的、只读的兼容视图。它们不是基准记录，且不得手动编辑。

基准 JSON 发生变化时，请在本地使用 `scripts/generate_registry_views.py` 重新生成视图，并提交生成后的视图。CI 会检查已提交的视图是否与基准 JSON 记录一致。
