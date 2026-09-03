# 标签协议

优先使用现有的已接受标签。

已接受标签可在以下位置找到：

```text
registry/tags/accepted/*.json
```

候选标签应写入：

```text
registry/tags/proposed/<tag_slug>.json
```

如果操作者提供了一个当前尚未被接受的标签，仅可通过带有所需接受元数据和 `acceptance_basis: operator_supplied` 的 `branch + PR` 创建 `registry/tags/accepted/<tag_slug>.json`。不要将它作为直接常规投递的一部分创建。

AI 自行生成的标签**必须**作为 `proposed` 提交，**不得**直接标记为 `accepted`。

不要把私密或工作区专用的标签列表移入公共/仅供参考工作区。

不要创建近似重复的标签。

在工作包或签退记录中说明标签选择。
