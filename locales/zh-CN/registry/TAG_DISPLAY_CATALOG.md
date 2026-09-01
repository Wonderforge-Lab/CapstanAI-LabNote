# 简体中文标签显示目录

> 翻译状态：已完成中文语言与协议一致性审阅。若本目录与英文基准标签记录在协议含义上出现冲突，以英文基准标签记录为准。

本文件只提供简体中文的标签显示名称和说明。

**基准标签仍是 `registry/tags/accepted/*.json` 中以英文 slug 标识的 JSON 记录。** 本目录不会创建中文 slug，也不会改变标签状态、作用域、创建者或其他机器字段。

| Canonical tag slug | 简体中文显示名 | 简体中文说明 |
| --- | --- | --- |
| `capstanai-labnote` | CapstanAI - LabNote | CapstanAI 多 AI 工作流生态中的公共 LabNote 模板组件。 |
| `example-project` | 示例项目 | 用于模板演示的可公开示例项目标签。 |
| `human-in-the-loop` | 人在回路（HITL） | 涉及人工审阅、批准或路由的工作。 |
| `provenance` | 溯源信息 | 涉及来源追踪、交接记录或决策轨迹的工作。 |
| `workflow-testing` | 工作流测试 | 用于测试 LabNote 工作流机制的可公开标签。 |

## 使用规则

- 在机器记录中继续使用 canonical tag slug，例如 `human-in-the-loop`。
- 中文显示名只用于人类可读界面、说明或本地化文档。
- 不要因为存在中文显示名而创建等义的中文 slug。
- 如果基准标签记录发生变化，本目录也应接受同步审阅。
