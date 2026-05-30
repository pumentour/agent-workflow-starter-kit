# Tool Routing

Clear routing prevents tool sprawl.

Use fewer tools, but give each tool a clear job.

## Default Routing

| Need | Tool Type | Output |
| --- | --- | --- |
| Code changes | Coding agent | Patch, tests, summary |
| Web UI checks | Browser automation | Screenshot, interaction result |
| Slide deck | Presentation workflow | PPTX or slide images |
| Spreadsheet analysis | Spreadsheet workflow | Workbook, charts, summary |
| Long document | Document workflow | DOCX or Markdown |
| Video / motion | Video workflow | Rendered video and source |

## Routing Rule

Before starting a task, answer:

1. What is the final artifact?
2. Which source file must remain editable?
3. Which tool owns verification?
4. What should stay manual?

## Anti-Pattern

Do not install a new tool because a single post recommended it.

Install or enable a tool only when:

- The task repeats
- The output quality improves
- The workflow becomes easier to verify
- The maintenance cost stays low

## Example

For a content card workflow:

- Data source: Markdown or JSON
- Layout source: HTML/CSS
- Renderer: Playwright
- Final output: PNG
- Verification: screenshot review
- Editable source: keep HTML/CSS and data file
