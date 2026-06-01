# Codex Plugin Decision Record

This is a real-world decision record for choosing a Codex plugin stack.

It is written as a reusable example, not as a private machine log.

## Input Signal

A public post recommended these Codex-related tools:

1. Presentations
2. Spreadsheets
3. Windsor AI
4. Hyperframes
5. Remotion
6. BioRender
7. Kama
8. Figma

The post also emphasized maintaining `AGENTS.md` as a long-term local memory and operating manual.

## Initial Interpretation

The useful insight was not "install everything."

The useful insight was:

```text
Plugins are tools.
AGENTS.md is the system layer.
```

## First Decision

Keep the core stack small:

- Browser
- Presentations
- Spreadsheets
- Hyperframes
- Documents

## Temporary Install Test

The remaining available plugins were tested:

- Figma
- Remotion
- BioRender
- Windsor AI
- Canva

Kama did not appear as a matching installable plugin in the available marketplace snapshot.

## Final Decision

After review, the extra plugins were removed.

| Plugin | Decision |
| --- | --- |
| Figma | Remove until design collaboration is needed |
| Remotion | Remove because Hyperframes already covers current video needs |
| BioRender | Remove because scientific diagrams are not a current workflow |
| Windsor AI | Remove until marketing data exists |
| Canva | Remove because external Canva is enough |

## Final Stack

```text
Browser
Documents
Presentations
Spreadsheets
Hyperframes
```

## AGENTS.md Updates

The operating manual was updated with:

- Plugin priority
- Plugin routing
- Project focus
- Source-file-first visual asset rule
- Editable deliverables rule

## Key Lesson

A plugin stack should match the workflow.

It should not mirror a recommendation list.

## Source-File Rule

For posters, product images, and content cards:

- Do not ship only PNG files.
- Keep editable source files.
- Prefer deterministic templates such as `HTML/CSS + Playwright` when layout matters.

This matters more than adding another design plugin.
