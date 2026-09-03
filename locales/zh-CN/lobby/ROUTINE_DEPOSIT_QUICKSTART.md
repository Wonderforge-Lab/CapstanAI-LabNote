# 常规投递快速入门

在实际使用中的 CapstanAI - LabNote 工作区里，普通访客会话投递使用本文件。

常规投递（routine deposit）是指访客会话把普通工作包、回复、消息、签退记录，或小型辅助 Markdown/JSON 记录放入 LabNote 工作区。

## 工作区环境

不要假定当前副本是公开的、私有的、本地的、远程的，也不要假定它绑定到任何特定仓库名称。

写入之前，确认它是私有或其他受控的实际工作区。如果它是公共工作区或仅供参考工作区，不得投递私密运行期材料。

## 实际工作区的默认写入方式

受控实际工作区中的常规投递可以直接写入该工作区的默认分支。

不要为普通投递创建任务分支。

只有以下情况使用 `branch + PR`：流程、政策、仓库结构、代码/脚本更改、清理、高风险/大体量导入、对大量现有文件的修改，或明确要求人工审阅的更改。

## 快速流程

1. 确认预期的 LabNote 结构存在，并判断当前工作区环境。
2. 确认本次运行的访客会话标识（visitor handle）。
3. 如果没有提供本次运行的访客会话标识，停止并向人类操作者询问。
4. 除非操作者明确指定其他分支，否则使用默认分支。
5. 如果缺少访客会话登记记录，则进行登记。
6. 只检查相关的消息和通知。
7. 如果需要标签，读取 `locales/zh-CN/lobby/TAGGING_PROTOCOL.md`。
8. 如果要投递文档，读取 `locales/zh-CN/docs/DOCUMENT_DEPOSIT_POLICY.md`。
9. 对所提供材料进行足够检查，以推断标签。
10. 将推断出的标签与已接受的登记库标签进行匹配。
11. 不要在此次直接投递中创建已接受标签记录。对于操作者提供但当前缺少的标签，使用带有所需接受元数据的 `branch + PR`，或询问操作者是否将其记录为候选标签。
12. 仅在确有帮助时，将 AI 生成的标签添加为候选 JSON 记录。
13. 创建工作包、回复、消息或签退记录文件。
14. 创建 JSON 登记库记录文件。
15. 不要手动编辑生成的 CSV 或 `registry/INDEX.md` 视图。
16. 如果需要团队审阅或转递，在 `README_FIRST` 中添加通知。
17. 报告所创建的文件，然后停止。

入口文件、入口区前门和访客会话检查表是本快速入门的前提；本文件不重复它们。

## 基准命名

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
