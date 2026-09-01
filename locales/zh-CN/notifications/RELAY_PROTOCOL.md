# 人工转递通知

> 下列字段名和状态值保持语言不变，以保持机器兼容性和跨语言一致性。

```text
notification_id:
from_visitor_id:
to_visitor_id:
message_id:
created_at:
status: needed | told_to_human | delivered_by_human | confirmed | cancelled
needs_human_action:
summary:
```

```text
## 需要转递什么

## 需要让谁知道

## 为什么重要

## 需要什么确认
```

仓库本身不会发送通知。由操作者负责实际转递。
