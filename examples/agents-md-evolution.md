# AGENTS.md Evolution Example

This example shows how a simple `AGENTS.md` can evolve into a practical operating manual.

## Starting Point

Many projects begin with a generic instruction file:

- Be helpful
- Follow project style
- Run tests
- Do not break things

That is not enough for repeated work.

## Useful Sections To Add

### Identity

Define who the user is and where decision authority lives.

```text
The user makes product and strategy decisions.
The agent implements, verifies, and documents work.
```

### Startup Checks

Define what the agent reads before working.

Examples:

- Project instructions
- Memory or context files
- Today's task queue
- `.ready/` folder

### Work Rules

Make operating rules explicit:

- Output first
- Read before editing
- Test or verify before finishing
- Keep changes small
- Preserve user changes
- Do not delete without approval

### Tool Routing

Tell the agent which tool owns which type of work.

Example:

| Need | Route |
| --- | --- |
| Local web UI | Browser |
| Deck | Presentations |
| Spreadsheet | Spreadsheets |
| Video | Hyperframes |
| Long document | Documents |

### Project Focus

List what is active and what is paused.

This prevents the agent from chasing every interesting new tool.

### Editable Asset Rule

For visual work:

```text
Final image is not enough.
Keep the editable source.
```

For repeatable production, preserve:

- Final image
- Source file
- Data or copy
- Render command

## Example Final Principle

```text
Plugins are tools.
AGENTS.md is the system layer.
```

The goal is not to make the instruction file long.

The goal is to make repeated work easier to resume.
