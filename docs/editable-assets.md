# Editable Asset Workflow

AI-generated visuals are useful, but one-off images are hard to operate as a business asset.

For repeatable production, keep the editable source.

## Minimum Deliverables

For each visual asset, preserve:

- Final PNG or JPG
- Editable source file
- Input copy
- Image references
- Render command or script

## Recommended Stack

Use `HTML/CSS + Playwright` when the asset needs:

- Precise layout
- Repeatable rendering
- Batch generation
- Easy text replacement
- Client-side edits

## Why Not Only Prompting

Prompt-only image generation is useful for exploration.  
It is weak for stable production.

Common failure points:

- Text errors
- Inconsistent layout
- Hard-to-edit details
- No reusable template
- Expensive revision loop

## Operating Rule

If an asset may be reused, sold, revised, or localized, keep the source.
