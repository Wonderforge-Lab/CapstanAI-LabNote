# 审阅工作流

CapstanAI - LabNote 从设计上就是人在回路（Human-in-the-loop, HITL）的系统。

助手会话可以起草、批评、总结或提出方案。由操作者决定哪些内容被接受、拒绝、归档或继续路由到下一步。

典型流程：

```text
packet -> response -> review note -> registry update
```

即：工作包 -> 回复 -> 审阅记录 -> 登记库更新。

当决策理由本身很重要时，使用 `templates/review_note.md`。如果某个回复仍处于待处理状态，不要把它当作已经接受的工作成果。
