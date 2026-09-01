# AI 入口

本仓库包含一个 `CapstanAI - LabNote` 工作区。

> 翻译状态：已完成中文语言与协议一致性审阅。若本译文与英文基准文件在协议含义上出现冲突，以英文基准文件为准。
>
> 本文件是简体中文语言层的操作入口。工作流使用的仓库路径、机器标识、状态值和写入目标保持语言不变。

不要假定当前工作区是公开的、私有的、本地的、远程的，也不要假定它绑定到任何特定仓库名称。**写入之前，必须根据当前仓库和操作者（human operator）确认工作区环境。**

如果这是公共工作区或仅供参考的工作区，不得投递私密报告、凭证、私密聊天记录、私密访客会话记录或项目专用语料库。

如果这是私有工作区或其他受控工作区（controlled live workspace），可以按照下面的规则进行正常 LabNote 投递。

应根据预期的 LabNote 结构和入口文件来验证工作区，而不是依赖固定的仓库所有者或仓库名（slug）。如果预期结构缺失或存在实质性不一致，**停止并报告该不一致。**

**没有本次运行的访客会话标识（visitor handle），就不得写入。**

除非操作者针对本次运行明确确认，否则不要复用先前对话上下文中的访客会话标识、分支、存储位置或权限。

如果当前提示词中粘贴或上传了源报告/文档，应把这些材料视为本次任务的来源材料。

## 常规投递

在受控工作区中，常规投递可以直接写入该工作区的默认分支。

不要为普通投递创建任务分支。

以下情况**必须使用 `branch + PR`**：流程、政策、代码、仓库结构、清理、高风险/大体量导入、对大量现有文件的修改，或明确要求审阅的更改。

普通投递的简体中文操作说明请使用：

```text
locales/zh-CN/lobby/ROUTINE_DEPOSIT_QUICKSTART.md
```

其英文基准对应文件为：

```text
lobby/ROUTINE_DEPOSIT_QUICKSTART.md
```

## 阅读顺序

使用简体中文语言层时，按以下顺序阅读：

1. `locales/zh-CN/AI_ENTRYPOINT.md`
2. `locales/zh-CN/lobby/README_FIRST.md`
3. `locales/zh-CN/lobby/VISITOR_CHECKLIST.md`

需要打标签时，读取 `locales/zh-CN/lobby/TAGGING_PROTOCOL.md`。

需要投递文档时，读取 `locales/zh-CN/docs/DOCUMENT_DEPOSIT_POLICY.md`。

只有任务确实需要分支时，才读取 `locales/zh-CN/docs/BRANCH_HYGIENE.md`。
