# 通知

> 翻译状态：已完成中文语言与协议一致性审阅。若本译文与英文基准文件在协议含义上出现冲突，以英文基准文件为准。

通知用于记录需要操作者进行人工转递（human relay）的请求。

当某条消息需要在彼此无法直接看到对方内容的会话之间传递时，使用通知。

从 `templates/notification_request.md` 创建通知文件，把它放入 `notifications/open/`，并在 `registry/notifications/` 下创建基准 JSON 通知记录。

CSV 通知登记表（如果存在）属于旧版/可选汇总。普通访客会话工作不要编辑这些 CSV，除非操作者明确要求。
