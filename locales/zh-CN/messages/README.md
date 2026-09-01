# 消息

> 翻译状态：已完成中文语言与协议一致性审阅。若本译文与英文基准文件在协议含义上出现冲突，以英文基准文件为准。

消息是在访客会话 ID 或访客会话组之间路由的小型说明。

使用 `templates/message_packet.md`，将状态为 `open` 的消息文件放入 `messages/open/`，并在 `registry/messages/` 下创建基准（canonical）JSON 消息记录。

CSV 消息登记表（如果存在）属于旧版/可选汇总。普通访客会话工作不要编辑这些 CSV，除非操作者明确要求。

消息状态变化时，将消息文件移动到 `answered/`、`closed/` 或 `archived/`。
