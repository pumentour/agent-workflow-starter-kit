# 本地优先的 Agent 工作流

给一人公司、独立开发者、小团队使用的 AI Agent 工作流模板。

这个仓库不是提示词合集。  
它关注的是：怎么把反复发生的工作沉淀成可复用、可验证、可维护的文件。

## 解决什么问题

很多 AI 工作流的问题不是不会问。  
而是每次都散在聊天里，过几天就断片。

这个仓库把关键内容文件化：

- Agent 应该知道什么
- 任务怎么交接
- 原始资料怎么进入 `raw/`
- 干净知识怎么沉淀到 `wiki/`
- 转换规则怎么放进 `instructions/`
- 用 `scripts/ingest.py` 跑最小 Wiki Layer
- 工具怎么路由
- 产物怎么验证
- 图文交付怎么保留源文件

## 当前包含

- [`templates/AGENTS.md`](templates/AGENTS.md)：Agent 工作手册模板
- [`templates/task-card.md`](templates/task-card.md)：任务卡模板
- [`docs/codex-setup.md`](docs/codex-setup.md)：Codex 搭建流程
- [`docs/codex-plugin-stack.md`](docs/codex-plugin-stack.md)：一人公司的 Codex 插件取舍
- [`docs/codex-plugin-audit-log.md`](docs/codex-plugin-audit-log.md)：Codex 插件安装/卸载审计
- [`docs/wiki-layer-workflow.md`](docs/wiki-layer-workflow.md)：raw/wiki/instructions 三层知识库工作流
- [`docs/editable-assets.md`](docs/editable-assets.md)：可编辑图文资产原则
- [`docs/tool-routing.md`](docs/tool-routing.md)：工具路由规则
- [`examples/green-menu-agent-workflow.md`](examples/green-menu-agent-workflow.md)：绿色菜单内容管线示例
- [`examples/product-image-workflow.md`](examples/product-image-workflow.md)：商品图工作流示例
- [`examples/codex-plugin-decision-record.md`](examples/codex-plugin-decision-record.md)：真实插件决策记录
- [`examples/agents-md-evolution.md`](examples/agents-md-evolution.md)：AGENTS.md 如何演进成工作手册
- [`examples/codex-for-oss-application.md`](examples/codex-for-oss-application.md)：Codex for OSS 申请清单

## 核心原则

1. 先输出结果。
2. 小步验证。
3. 保留源文件。
4. 少装工具，清晰路由。
5. 不把一次性聊天当系统。

## 适合谁

- 一人公司
- 独立开发者
- 内容创业者
- 本地优先 AI 工作流使用者
- 想让 Codex / Claude Code / Cursor 更懂项目的人

## 不适合谁

- 只想找万能提示词的人
- 不愿维护文件的人
- 需要大型团队权限系统的人

## 状态

早期版本。  
内容来自真实的一人公司 AI 工作流，会继续迭代。

## 快速生成 Wiki

```bash
python scripts/ingest.py
```

这个命令会读取 `raw/` 下的 Markdown，生成到 `wiki/`，并更新 `wiki/project-index.md`。

高级命令：

```bash
python scripts/wiki_layer.py scan
python scripts/wiki_layer.py ingest
python scripts/wiki_layer.py graph
python scripts/wiki_layer.py watch --interval 5
```

高级版会记录源文件哈希、保留人工修改、报告冲突，并生成 `wiki/_graph.md`。
