# Green Menu Agent Workflow

This example describes a repeatable content pipeline for a vegan or healthy-food content account.

## Goal

Turn one recipe idea or video reference into a set of publishable content cards.

## Inputs

- Recipe title
- Ingredients
- Steps
- Nutrition or substitution notes
- Reference image or video
- Publishing platform requirements

## Tool Routing

| Step | Owner | Output |
| --- | --- | --- |
| Collect reference | Browser / research agent | Source links |
| Structure recipe | Coding or writing agent | JSON / Markdown |
| Render cards | HTML/CSS + Playwright | PNG cards |
| Review layout | Browser | Screenshot check |
| Polish copy | Writing agent | Final caption |

## Source Files

Keep:

- `recipe.json`
- `cards.html`
- `styles.css`
- rendered PNG files
- final caption Markdown

## Verification

Before publishing:

- Text fits inside cards
- Ingredients are readable
- Steps are ordered correctly
- Final images match platform size
- Source files can regenerate the output

## What Stays Manual

- Final taste judgment
- Platform publishing
- Brand positioning
- Whether the recipe fits the account strategy

## Why This Workflow Matters

The key asset is not a single image.  
The key asset is the template that can generate the next 100 images.
