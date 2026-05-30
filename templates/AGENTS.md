# AGENTS.md Template

## Identity

The user is a solo builder.  
The agent implements, verifies, and documents work.  
The user keeps final decision authority.

## Startup

Before working:

1. Read local project instructions.
2. Check active task files.
3. Inspect existing code or documents before editing.
4. Verify whether the request needs implementation, analysis, or a draft.

## Work Rules

- Output first.
- Read before editing.
- Keep changes small and reversible.
- Use existing project scripts before adding new tooling.
- Preserve user changes.
- Do not delete files without explicit approval.

## Tool Routing

- Browser: verify local web UI and rendered outputs.
- Presentations: create slide decks.
- Spreadsheets: analyze tabular data.
- Documents: write reports and SOPs.
- Video tools: create motion or video assets.

## Visual Asset Rule

Do not ship only final PNG files when the user needs repeatable production.

For posters, product images, and content cards, preserve:

- Final exported image
- Editable source file
- Data or copy source
- Rendering script or command

Prefer deterministic templates such as `HTML/CSS + Playwright` when layout accuracy matters.

## Delivery Format

When done, report:

1. What changed
2. What was verified
3. What remains
