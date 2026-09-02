# 登记库

> 本文件是仓库根目录 `registry/README.md` 的简体中文说明，不改变基准运行期路径 `registry/`。

仓库根目录 `registry/` 下的基准（canonical）记录采用每条记录一个 JSON 文件的方式。

CSV 文件和 `INDEX.md` 是生成的兼容视图。不要手动编辑它们；基准 JSON 发生变化时，在本地运行 `scripts/generate_registry_views.py`，然后提交生成后的视图。

CI 会检查已提交的视图是否与基准 JSON 记录一致。
