# Local First Agent Workflows

[中文说明](README.zh-CN.md)

Practical templates for solo builders who use coding agents to run local-first workflows.

This repository collects small, reproducible patterns for:

- Maintaining `AGENTS.md` as a local operating manual
- Turning repeated work into agent-ready task cards
- Keeping source files editable instead of shipping only final images
- Using `HTML/CSS + Playwright` for deterministic visual assets
- Routing work across coding, browser, document, spreadsheet, and video tools

The goal is simple: help independent builders keep their AI workflow understandable, editable, and low-maintenance.

## Why This Exists

Many AI workflows become hard to maintain because instructions live in chats, screenshots, and scattered notes.

This project keeps the important parts in files:

- What the agent should know
- Which tools should be used
- What should be avoided
- How outputs should be verified
- What source files must be preserved

## Included Templates

- [`templates/AGENTS.md`](templates/AGENTS.md): a practical agent operating manual
- [`templates/task-card.md`](templates/task-card.md): a task handoff template
- [`docs/codex-setup.md`](docs/codex-setup.md): a practical Codex setup workflow
- [`docs/codex-plugin-stack.md`](docs/codex-plugin-stack.md): a minimal plugin stack for solo builders
- [`docs/codex-plugin-audit-log.md`](docs/codex-plugin-audit-log.md): installed vs removed plugin audit notes
- [`docs/editable-assets.md`](docs/editable-assets.md): rules for editable visual deliverables
- [`examples/green-menu-agent-workflow.md`](examples/green-menu-agent-workflow.md): a real content pipeline example
- [`examples/product-image-workflow.md`](examples/product-image-workflow.md): a product image workflow example
- [`examples/codex-plugin-decision-record.md`](examples/codex-plugin-decision-record.md): a real plugin decision record
- [`examples/agents-md-evolution.md`](examples/agents-md-evolution.md): how AGENTS.md evolves into an operating manual
- [`examples/codex-for-oss-application.md`](examples/codex-for-oss-application.md): an open-source support application checklist

## Principles

1. Output first.
2. Keep workflows local-first when possible.
3. Prefer editable source files over one-off generated images.
4. Use fewer tools, but route them clearly.
5. Verify outputs before considering work done.

## Status

Early public version. The templates are extracted from real solo-builder workflows and will be refined as the workflow matures.

## Who This Is For

This project is for builders who:

- Work alone or in very small teams
- Use coding agents daily
- Need repeatable outputs, not one-off chat answers
- Care about local files, source control, and editable deliverables
- Want fewer tools and clearer routing

## Repository Map

```text
.
├── templates/
│   ├── AGENTS.md
│   └── task-card.md
├── examples/
│   ├── codex-for-oss-application.md
│   ├── codex-plugin-decision-record.md
│   ├── agents-md-evolution.md
│   ├── green-menu-agent-workflow.md
│   └── product-image-workflow.md
└── docs/
    ├── codex-plugin-audit-log.md
    ├── codex-plugin-stack.md
    ├── codex-setup.md
    ├── editable-assets.md
    └── tool-routing.md
```

## Maintainer Workflow

When adding a new workflow:

1. Write the task as a task card.
2. Define which tool owns each step.
3. Keep source files editable.
4. Add a verification step.
5. Document what should not be automated yet.

## License

MIT
