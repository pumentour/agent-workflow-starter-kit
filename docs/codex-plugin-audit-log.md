# Codex Plugin Audit Log

This document records a practical plugin audit for a solo-builder Codex setup.

The goal is not to install every useful-looking plugin.  
The goal is to keep the system focused.

## Current Core Plugins

These plugins are installed and enabled.

| Plugin | Status | Why It Stays |
| --- | --- | --- |
| Browser | Installed | Verify local web pages, dashboards, screenshots, and rendered HTML |
| Documents | Installed | Create reports, SOPs, and long-form deliverables |
| Presentations | Installed | Create decks, product explainers, and course materials |
| Spreadsheets | Installed | Analyze products, competitors, finances, and growth data |
| Hyperframes | Installed | Create videos, motion assets, and website-to-video workflows |

## Plugins Tested Then Removed

These plugins were installable, but removed after review.

| Plugin | Final Status | Reason |
| --- | --- | --- |
| Remotion | Removed | Overlaps with Hyperframes for current needs |
| BioRender | Removed | Scientific illustration is not a current business line |
| Figma | Removed | Design collaboration is not needed for a solo workflow yet |
| Windsor AI | Removed | Useful only after real marketing or ad data exists |
| Canva | Removed | External Canva usage is enough; no need to add it to Codex |

## Plugin Mentioned But Not Installed

| Tool | Decision |
| --- | --- |
| Kama | No matching Codex plugin was found in the available marketplace snapshot |

## Decision Rule

Install a plugin only when it satisfies at least one condition:

- The task repeats often.
- The plugin improves output quality.
- The plugin makes verification easier.
- The plugin removes a real bottleneck.

Remove or delay a plugin when:

- It overlaps with an existing tool.
- It adds cognitive load.
- It depends on data you do not have yet.
- It solves a future problem instead of a current one.

## Minimal Stack Outcome

The final stack is intentionally small:

```text
Browser + Documents + Presentations + Spreadsheets + Hyperframes
```

This covers the main output types:

- Web checks
- Documents
- Slides
- Tables
- Video

For a solo builder, fewer tools often means faster execution.
