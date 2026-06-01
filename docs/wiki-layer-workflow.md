# Wiki Layer Workflow

The Wiki Layer is a way to stop making language models reread the same raw files again and again.

Instead of treating raw files as the daily workspace, the model first turns them into a clean, linked, editable knowledge base.

## Core Idea

```text
raw files -> structured wiki -> agent works from wiki
```

The agent cleans and structures source material once.

After that, repeated work happens against the `wiki/` layer instead of repeatedly uploading the original files.

## Folder Structure

```text
project/
├── raw/
├── wiki/
└── instructions/
```

## raw/

Immutable source files.

Use this folder for:

- HTML pages
- PDFs
- Screenshots
- Notes
- Spreadsheets
- Transcripts
- Exported chats

Rule:

```text
Do not edit raw files manually.
```

They are the source of truth.

## wiki/

Clean Markdown files created from raw material.

Use this folder for:

- Clean summaries
- Structured notes
- Linked concepts
- Project pages
- Topic indexes
- Research digests

This becomes the primary workspace for the agent.

## instructions/

Rules for turning raw files into wiki pages.

Use this folder for:

- Templates
- Metadata rules
- Link rules
- Update rules
- Conflict handling rules

## Why This Matters

Without a wiki layer, the model wastes tokens:

- rereading the same files
- reprocessing messy documents
- losing relationships between files
- rebuilding context from scratch

With a wiki layer, the model works from structured knowledge.

Benefits:

- Lower repeated token cost
- Better retrieval
- Clearer links between ideas
- Easier human review
- Local-first knowledge storage

## Obsidian Fit

The `wiki/` folder works well with Obsidian because Markdown files can use internal links:

```text
[[Project_Index]]
[[AGENTS]]
[[Editable_Assets]]
```

This gives both the human and the agent a shared knowledge graph.

## Agent Prompt Pattern

```text
You are maintaining a local wiki layer.

Read files from raw/.
Create or update clean Markdown notes in wiki/.
Follow templates and linking rules in instructions/.
Do not modify raw files.
Prefer short summaries, explicit metadata, and internal links.
When a source conflicts with an existing wiki note, report the conflict before overwriting.
```

## Good Use Cases

Use a wiki layer when:

- You have more than 10 related documents
- The topic changes over time
- You repeatedly generate reports or content
- You need local privacy
- You want the agent to resume work without re-reading everything

## Relationship To AGENTS.md

`AGENTS.md` tells the agent how to behave.

The Wiki Layer gives the agent clean project knowledge to work from.

Together:

```text
AGENTS.md = operating rules
wiki/ = structured memory
raw/ = original evidence
instructions/ = transformation rules
```

## Minimal Starter

```text
my-project/
├── AGENTS.md
├── raw/
│   └── source-note.md
├── wiki/
│   └── project-index.md
└── instructions/
    └── wiki-rules.md
```

Start small.

Do not build a complex knowledge system before you have repeat work.

## Runnable Starter

This repository includes a small wiki builder:

```bash
python scripts/ingest.py
```

It reads `raw/*.md`, creates wiki pages, adds metadata, and updates `wiki/project-index.md`.

## Advanced Local Version

The advanced local tool is:

```bash
python scripts/wiki_layer.py ingest
```

It supports:

- recursive raw file scanning
- source hashing
- state tracking
- automatic related links
- graph generation
- conflict reporting
- watch mode
- preserving manual edits unless forced

Commands:

```bash
python scripts/wiki_layer.py scan
python scripts/wiki_layer.py ingest
python scripts/wiki_layer.py graph
python scripts/wiki_layer.py watch --interval 5
```

Generated support files:

- `wiki/_state.json`
- `wiki/_graph.md`
- `wiki/_conflicts.md`

This is still intentionally local-first and simple.

It is not trying to become a database before the workflow needs one.
