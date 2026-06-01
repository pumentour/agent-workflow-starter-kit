# Codex Setup Workflow

This document describes a practical Codex setup for solo builders.

It is not a maximal setup.  
It is a low-noise setup that keeps Codex useful without turning the toolchain into the project.

## Setup Goals

- Keep Codex as the implementation engine.
- Keep project knowledge in files, not only chats.
- Use a small plugin stack.
- Verify local outputs before calling work done.
- Preserve editable source files.

## Step 1: Create A Local Operating Manual

Create an `AGENTS.md` file in the project root.

It should define:

- Who the user is
- What the agent should do
- What the agent should not do
- Startup checks
- Tool routing
- Delivery format
- Permission boundaries

Use [`templates/AGENTS.md`](../templates/AGENTS.md) as a starting point.

## Step 2: Keep A Small Plugin Stack

Start with only the tools that directly support the work.

For many solo-builder projects, this is enough:

- Browser
- Documents
- Presentations
- Spreadsheets
- Hyperframes or another video workflow

Avoid installing tools just because they are trending.

## Step 3: Define Routing Before Work Starts

Every task should answer:

1. What is the final artifact?
2. Which source file must remain editable?
3. Which tool owns the work?
4. Which tool verifies the output?
5. What stays manual?

This prevents tool hopping.

## Step 4: Preserve Editable Sources

For visual or content assets, do not keep only exports.

Keep:

- Source copy
- Data files
- Layout source
- Render scripts or commands
- Final exports

For layout-heavy assets, `HTML/CSS + Playwright` is often more reliable than prompt-only generation.

## Step 5: Verify Outputs

Verification should be explicit.

Examples:

- Run tests for code changes.
- Use a browser screenshot for web UI.
- Open exported files.
- Check text overflow in images.
- Confirm generated assets can be reproduced from source.

## Step 6: Keep The Human Decision Boundary

The agent can implement, test, and draft.

The user should still decide:

- Whether to publish
- Whether to spend money
- Whether to change strategy
- Whether to expose personal or business information
- Whether to submit account-level applications

## Anti-Patterns

- Installing every recommended plugin
- Treating chats as documentation
- Shipping only PNGs with no source files
- Letting a workflow become more complex than the business
- Automating steps that still need taste or judgment
