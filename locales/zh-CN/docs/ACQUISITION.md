# 获取 CapstanAI LabNote

本指南只说明如何获得一个可以使用的 LabNote 工作区。工作区副本准备好之后，正常的 LabNote 使用流程从 `AI_ENTRYPOINT.md` 开始。

## 最简单的起始提示词

如果你已经在和一个 AI 对话，可以直接对它说：

```text
请帮我为这个项目设置 CapstanAI LabNote。先判断你目前具备哪些访问能力，再向我推荐最简单、最安全的方式。如果需要我运行任何终端命令，请先解释命令的作用。
```

AI 应先判断：它是否能够访问 GitHub、是否能自行运行终端命令、你是否能够运行终端命令，以及你希望工作区只保存在本地、只放在 GitHub，还是两边都要。

## 推荐方式

### 浏览器 AI（可使用终端）：本地 + GitHub

如果你既需要本地工作副本，也需要一个私有 GitHub 工作区，这是首选方式。

对于下面这套简单流程，目标私有仓库必须是**新建且为空**的。如果 GitHub 提示用 README、`.gitignore` 或许可证初始化仓库，请不要勾选这些选项。如果目标仓库已经包含提交或文件，请停止，让 AI 选择安全的替代方案，而不要通过强制推送覆盖现有内容。

浏览器 AI 应根据你的操作系统、shell、所选文件夹和目标私有仓库调整命令。典型的 Git 流程如下：

```bash
git clone https://github.com/Wonderforge-Lab/CapstanAI-LabNote.git MyProject-LabNote
cd MyProject-LabNote
git remote rename origin upstream
git remote add origin <YOUR-PRIVATE-REPO-URL>
git push -u origin main
```

在让你运行这些命令之前，AI 应先解释它们会：

- 把公开的 LabNote 仓库复制到一个新的本地文件夹；
- 将公开源仓库保留为 `upstream`；
- 把你的工作副本连接到你自己的仓库，并将其命名为 `origin`；
- 把初始 LabNote 工作区推送到你的仓库。

AI 还应确认：目标仓库确实是你打算使用的仓库；对于这套流程，它目前为空；并且适合执行这次推送。AI **不得猜测或编造**私有仓库 URL，也不得把强制推送当成绕过非空目标仓库的捷径。

### 浏览器 AI（无法使用终端）：仅 GitHub

使用 GitHub 的 **Use this template** 流程，创建一个新的私有仓库或其他受控仓库。

推荐步骤：

1. 在 GitHub 上打开 CapstanAI LabNote 的基准（canonical）仓库。
2. 选择 **Use this template**。
3. 选择 **Create a new repository**。
4. 给新仓库取一个与项目对应的名称。
5. 除非你有意创建公开工作区，否则选择 **Private**。
6. 创建仓库。
7. 让 AI 访问新的工作区，并从 `AI_ENTRYPOINT.md` 开始。

如果模板创建不可用或不合适，也可以使用 GitHub Import；但对于只使用 GitHub 的用户，模板方式仍是更简单的默认选择。

### 编程智能体或可使用终端的 AI

在操作者（human operator）批准并且权限允许的前提下，编程智能体通常可以自行完成克隆和仓库设置。

智能体仍应：

- 明确说明它正在复制哪个仓库；
- 明确说明预定的本地和/或远程目标位置；
- 未经明确批准，不覆盖非空目标；
- 创建私有 `origin` 时，把公开源仓库保留为 `upstream`；
- 如果仓库身份或权限不明确，停止并询问，而不是继续猜测。

### 仅本地工作区

在本地克隆 LabNote：

```bash
git clone https://github.com/Wonderforge-Lab/CapstanAI-LabNote.git MyProject-LabNote
cd MyProject-LabNote
git remote rename origin upstream
```

不需要私有远程仓库。使用 `upstream` 这个名称，只是为了清楚表明该远程地址指向公开源仓库，而不是你自己的项目仓库。

## 获取之后

无论 LabNote 是通过哪种方式获得的，下一步都一样：

1. 用将要使用该工作区的 AI 打开 `AI_ENTRYPOINT.md`。
2. 确认预期的 LabNote 结构存在。
3. 确认当前工作区属于私有/受控工作区，适合实际工作，还是公共/仅供参考工作区。
4. 按入口区（lobby）的阅读顺序继续。

第一次使用前，不应要求你先修改仓库名称，也不需要修改 LabNote 的身份文件。
