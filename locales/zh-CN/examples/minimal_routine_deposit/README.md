# 简体中文最小常规投递示例

> 示例状态：已完成端到端协议一致性与中文审阅。

本目录展示一个虚构、可公开的简体中文常规投递示例。

示例访客会话标识：`zhcn-example`

示例工作包：`20260901-zhcn-example-routine-test`

本示例用于验证以下行为：

- 使用简体中文 Markdown 工作包模板；
- Markdown 标题和正文可以使用中文；
- 字段名和状态值保持英文机器形式；
- 运行期工作包仍写入基准路径 `datadrops/shared/inbox/`；
- 工作包登记记录仍采用基准 JSON-per-record 结构；
- 访问记录仍采用基准 JSON-per-record 结构；
- 签退记录使用简体中文人类可读章节；
- 不编辑 CSV 登记表；
- 普通受控工作区常规投递不创建任务分支。

本地化语言层不会创建 `locales/zh-CN/datadrops/`、`locales/zh-CN/registry/` 或其他平行运行期存储树。

## 关于英文最小示例

英文 `examples/minimal_routine_deposit/` 中的 Markdown 示例早于当前 Markdown 模板，部分头部字段和签退章节仍使用旧形态。本简体中文兼容性示例以**当前基准模板和规则**为准，不把旧示例形态复制进新的语言层。

JSON 记录结构仍与当前基准 JSON 模板保持兼容。
