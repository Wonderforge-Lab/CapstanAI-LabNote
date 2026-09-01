# 常规投递快速入门

在实际使用中的 CapstanAI - LabNote 受控工作区里，普通访客会话投递使用本文件。

常规投递（routine deposit）是指访客会话把普通工作包、回复、消息、签退记录，或小型辅助 Markdown/JSON 记录放入 LabNote 工作区。

> 翻译状态：已完成中文语言与协议一致性审阅。若本译文与英文基准文件在协议含义上出现冲突，以英文基准文件为准。

## 工作区环境

不要假定当前副本是公开的、私有的、本地的、远程的，也不要假定它绑定到任何特定仓库名称。

**写入之前，必须确认它是私有工作区或其他受控工作区。** 如果它是公共工作区或仅供参考工作区，不得投递私密运行期材料。

## 受控工作区的默认写入方式

受控工作区中的常规投递可以直接写入该工作区的默认分支。

不要为普通投递创建任务分支。

只有以下情况才使用 `branch + PR`：流程、政策、仓库结构、代码/脚本更改、清理、高风险/大体量导入、对大量现有文件的修改，或明确要求人工审阅的更改。

## 快速流程

1. 确认预期的 LabNote 结构存在，并判断当前工作区环境。
2. 确认本次运行的访客会话标识（visitor handle）。
3. 如果没有提供本次运行的访客会话标识，**停止并向操作者询问。**
4. 除非操作者明确指定其他分支，否则使用默认分支。
5. 读取 `locales/zh-CN/AI_ENTRYPOINT.md`。
6. 读取 `locales/zh-CN/lobby/README_FIRST.md`。
7. 读取 `locales/zh-CN/lobby/VISITOR_CHECKLIST.md`。
8. 如果访客会话尚未登记，则进行登记。
9. 只检查与当前任务相关的消息和通知。
10. 如果需要标签，读取 `locales/zh-CN/lobby/TAGGING_PROTOCOL.md`。
11. 如果要投递文档，读取 `locales/zh-CN/docs/DOCUMENT_DEPOSIT_POLICY.md`。
12. 对所提供材料进行足够检查，以推断合适的标签。
13. 将推断出的标签与登记库中已接受的标签进行匹配。
14. 对于操作者提供但当前缺少的标签，添加状态为 `accepted` 的 JSON 标签记录。
15. 对于 AI 自行生成的标签，只有确有帮助时才添加状态为 `proposed` 的 JSON 标签记录。
16. 创建工作包、回复、消息或签退记录文件。使用 `locales/zh-CN/templates/` 下已审阅的 Markdown 模板；机器字段和状态值保持英文基准形式。
17. 创建 JSON 登记库记录文件。JSON 模板和机器结构保持基准形式，不进行本地化。
18. 除非操作者明确要求，否则不要编辑 CSV。
19. 如果需要团队审阅或人工转递（human relay），在 `README_FIRST` 中添加通知。
20. 报告所创建的文件，然后**停止。**

## 基准命名规则

除非操作者提供了更合适的命名方式，否则使用以下格式：

```text
packet_id:
YYYYMMDD-<visitor_id>-<short-topic>

packet:
datadrops/shared/inbox/<packet_id>.md

packet record:
registry/packets/YYYY/<packet_id>.json

visit_id:
<packet_id>-visit

visit record:
registry/visits/YYYY/<visit_id>.json

signoff:
responses/signoffs/<packet_id>-signoff.md
```

## 给操作者的最简最终报告

以下字段标签保持语言不变，以便跨语言协作和结构一致性：

```text
visitor_id:
files created:
JSON registry records created:
messages checked:
notifications checked:
README_FIRST notice added:
relay/action needed:
signoff path:
stopped:
```
