# 快速入门

CapstanAI LabNote 分为三个阶段：获取副本、初始化（bootstrap）工作区，然后开始使用。

## 1. 获取 LabNote

如果你已经在和一个 AI 对话，最简单的起点是：

```text
请帮我为这个项目设置 CapstanAI LabNote。先判断你目前具备哪些访问能力，再向我推荐最简单、最安全的方式。如果需要我运行任何终端命令，请先解释命令的作用。
```

推荐方式：

- **浏览器 AI（可使用终端）：** 由 AI 引导在本地克隆；如有需要，再配置私有 GitHub `origin`。
- **浏览器 AI（无法使用终端）：** 使用 GitHub **Use this template**，创建私有仓库或其他受控仓库。
- **编程智能体或可使用终端的 AI：** 在操作者批准并且仓库权限允许的前提下，智能体通常可以直接完成克隆和设置。
- **仅本地使用：** 只在本地克隆；不需要私有远程仓库。

具体的入门步骤和示例终端命令，请参阅 [`ACQUISITION.md`](ACQUISITION.md)。

一旦工作区副本已经存在，采用哪种获取方式并不会改变 LabNote 后续的工作方式。

## 2. 初始化工作区

1. 用将要使用该工作区的 AI 打开仓库根目录的 `AI_ENTRYPOINT.md`。如果本次交互已选择 `zh-CN`，根入口会路由到已支持的简体中文操作入口。
2. 确认预期的 LabNote 结构存在。
3. 确认当前工作区属于适合实际工作的私有/受控工作区，还是公共/仅供参考工作区。
4. 按简体中文入口区（lobby）的阅读顺序继续：`locales/zh-CN/lobby/README_FIRST.md` -> `locales/zh-CN/lobby/VISITOR_CHECKLIST.md`。
5. 确认由操作者提供的本次运行访客会话标识（visitor handle）。如果没有提供，必须停止并询问，然后才能写入。

第一次使用前，不应要求你先修改仓库名称，也不需要修改 LabNote 的身份文件。

## 3. 使用 LabNote

1. 复制 `locales/zh-CN/templates/datadrop_packet.md`，创建一个新的工作包（packet）。
2. 填写工作包头部字段和任务部分。字段名和状态值保持英文机器形式。
3. 如果工作包依赖较大的文件，请加入经过操作者批准的引用和简短摘要，而不要把整份原始材料直接提交进仓库。
4. 使用基准 JSON 模板，在 `registry/packets/<year>/` 下创建一个 JSON 工作包记录。
5. 把工作包交给目标助手会话。
6. 复制 `locales/zh-CN/templates/ai_response_packet.md`，用于填写回复。
7. 使用基准 JSON 模板，在 `registry/responses/<year>/` 下创建一个 JSON 回复记录。
8. 在把任何内容标记为 `accepted` 之前，先审阅回复。

本地化 Markdown 模板只改变人类可读的标题和章节；JSON 键、状态值、ID 和运行期路径仍使用基准机器形式。

小文件，清楚的标签，不靠模糊记忆。诀窍就这么简单。
