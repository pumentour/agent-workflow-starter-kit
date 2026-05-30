# Product Image Workflow

This example describes a low-maintenance workflow for AI-assisted product image production.

## Goal

Create product image variants while keeping the source editable for future revisions.

## Inputs

- Product photo
- Selling point
- Target platform
- Required size
- Brand colors
- Copywriting

## Recommended Stack

- Product image source: original photo
- Layout source: HTML/CSS
- Rendering: Playwright
- Batch data: JSON or CSV
- Output: PNG / JPG

## Deliverables

Each delivery should include:

- Final exported image
- Editable HTML/CSS source
- Copy/data file
- Render command

## Revision Rule

If the client asks to change copy, price, color, or layout:

1. Edit the source file.
2. Re-render.
3. Do not regenerate from scratch unless the concept changes.

## Verification

- Product remains visible
- Text is readable
- Layout fits platform ratio
- No important content is cropped
- Source can reproduce the final output

## Business Note

Editable templates are more valuable than one-off generated images.

They reduce revision cost and make small-batch production possible.
