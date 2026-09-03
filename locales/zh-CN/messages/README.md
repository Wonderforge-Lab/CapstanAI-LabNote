# 消息

消息是在访客会话 ID 或访客会话组之间路由的小型说明。

使用 `templates/message_packet.md`，将状态为 `open` 的消息文件放入 `messages/open/`，并在 `registry/messages/` 下创建基准（canonical）JSON 消息记录。

CSV 消息登记表和 `registry/INDEX.md` 是生成的只读兼容视图。不得手动编辑。

消息状态变化时，将消息文件移动到 `answered/`、`closed/` 或 `archived/`。
