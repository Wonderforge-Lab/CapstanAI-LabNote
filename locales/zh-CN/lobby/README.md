# 入口区

> 翻译状态：已完成中文语言与协议一致性审阅。若本译文与英文基准文件在协议含义上出现冲突，以英文基准文件为准。

> 当前访客会话工作流从 `../AI_ENTRYPOINT.md` 开始，然后依次读取 `README_FIRST.md`、`VISITOR_CHECKLIST.md`；普通投递还要读取 `ROUTINE_DEPOSIT_QUICKSTART.md`。
> 写入之前必须确认当前工作区环境。公共/仅供参考工作区不得接收私密运行期数据。

每个助手会话在处理 LabNote 工作之前，都先通过入口区进行检查。

1. 读取 `../AI_ENTRYPOINT.md`。
2. 读取 `README_FIRST.md`。
3. 读取 `VISITOR_CHECKLIST.md`。
4. 普通投递按照 `ROUTINE_DEPOSIT_QUICKSTART.md` 执行。
5. 在仓库根目录的基准 `registry/` 路径下创建 JSON 登记记录。
6. 除非操作者明确要求，否则不要编辑 CSV 汇总文件。

入口区留下的是工作轨迹，不是登录系统。
