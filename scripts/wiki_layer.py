#!/usr/bin/env python3
"""
Local Wiki Layer builder.

Commands:
    python scripts/wiki_layer.py ingest
    python scripts/wiki_layer.py scan
    python scripts/wiki_layer.py graph
    python scripts/wiki_layer.py watch
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RAW = "raw"
DEFAULT_WIKI = "wiki"
STATE_NAME = "_state.json"
GRAPH_NAME = "_graph.md"
CONFLICTS_NAME = "_conflicts.md"


STOPWORDS = {
    "the",
    "and",
    "for",
    "with",
    "from",
    "this",
    "that",
    "into",
    "your",
    "you",
    "are",
    "can",
    "not",
    "but",
    "use",
    "using",
    "workflow",
    "workflows",
    "agent",
    "agents",
    "local",
    "first",
}


@dataclass
class SourceDoc:
    source: Path
    rel_source: str
    title: str
    slug: str
    text: str
    source_hash: str
    summary: str
    tags: list[str]
    output: Path


def utc_date() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "untitled"


def title_from_text(path: Path, text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").replace("_", " ").title()


def strip_title(text: str) -> str:
    lines = text.strip().splitlines()
    if lines and lines[0].startswith("# "):
        return "\n".join(lines[1:]).strip()
    return text.strip()


def first_paragraph(text: str) -> str:
    cleaned: list[str] = []
    in_code = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not stripped:
            if cleaned:
                break
            continue
        if stripped.startswith("#") or stripped.startswith(("-", "*", "|")):
            continue
        cleaned.append(stripped)
    return " ".join(cleaned)[:240] or "No summary available."


def tokens(text: str) -> list[str]:
    return re.findall(r"[A-Za-z][A-Za-z0-9-]{2,}", text.lower())


def extract_tags(text: str, limit: int = 8) -> list[str]:
    counts: dict[str, int] = {}
    for token in tokens(text):
        if token in STOPWORDS:
            continue
        counts[token] = counts.get(token, 0) + 1
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return [word for word, _ in ranked[:limit]]


def load_state(wiki_dir: Path) -> dict[str, Any]:
    state_path = wiki_dir / STATE_NAME
    if not state_path.exists():
        return {"version": 1, "sources": {}}
    return json.loads(read_text(state_path))


def save_state(wiki_dir: Path, state: dict[str, Any]) -> None:
    state["updated_at"] = utc_timestamp()
    write_text(wiki_dir / STATE_NAME, json.dumps(state, ensure_ascii=False, indent=2) + "\n")


def find_sources(raw_dir: Path) -> list[Path]:
    patterns = ("*.md", "*.txt")
    files: list[Path] = []
    for pattern in patterns:
        files.extend(raw_dir.rglob(pattern))
    return sorted(path for path in files if path.name.lower() != "readme.md")


def unique_slug(base: str, used: set[str]) -> str:
    slug = base
    index = 2
    while slug in used:
        slug = f"{base}-{index}"
        index += 1
    used.add(slug)
    return slug


def build_docs(raw_dir: Path, wiki_dir: Path) -> list[SourceDoc]:
    docs: list[SourceDoc] = []
    used: set[str] = set()
    for source in find_sources(raw_dir):
        text = read_text(source)
        title = title_from_text(source, text)
        slug = unique_slug(slugify(title), used)
        docs.append(
            SourceDoc(
                source=source,
                rel_source=rel(source),
                title=title,
                slug=slug,
                text=text,
                source_hash=sha256_text(text),
                summary=first_paragraph(text),
                tags=extract_tags(text),
                output=wiki_dir / f"{slug}.md",
            )
        )
    return docs


def relation_score(left: SourceDoc, right: SourceDoc) -> int:
    if left.slug == right.slug:
        return 0
    left_terms = set(left.tags) | set(tokens(left.title))
    right_terms = set(right.tags) | set(tokens(right.title))
    return len(left_terms & right_terms)


def related_links(doc: SourceDoc, docs: list[SourceDoc]) -> list[str]:
    scored = [(relation_score(doc, other), other) for other in docs if other.slug != doc.slug]
    scored = sorted(scored, key=lambda item: (-item[0], item[1].title.lower()))
    return [f"[[{other.slug}]]" for score, other in scored if score > 0][:6]


def render_doc(doc: SourceDoc, docs: list[SourceDoc]) -> str:
    related = related_links(doc, docs)
    related_block = "\n".join(f"- {link}" for link in related) or "- None yet"
    tags = ", ".join(doc.tags) if doc.tags else "local-first"
    body = strip_title(doc.text)
    return f"""# {doc.title}

## Metadata

- Source: `{doc.rel_source}`
- Source hash: `{doc.source_hash[:12]}`
- Updated: {utc_date()}
- Tags: {tags}
- Generated by: `scripts/wiki_layer.py`

## Summary

{doc.summary}

## Key Notes

{body}

## Related

{related_block}
"""


def is_generated_page(text: str) -> bool:
    return "Generated by: `scripts/wiki_layer.py`" in text or "- Source: `raw/" in text


def render_index(docs: list[SourceDoc]) -> str:
    rows = "\n".join(f"- [[{doc.slug}]] - {doc.summary}" for doc in sorted(docs, key=lambda item: item.title.lower()))
    rows = rows or "- No generated pages yet"
    return f"""# Project Index

## Metadata

- Updated: {utc_date()}
- Generated by: `scripts/wiki_layer.py`

## Generated Pages

{rows}

## Manual Index

- [[Codex_Setup]]
- [[Plugin_Audit]]
- [[Editable_Assets]]
- [[Tool_Routing]]
- [[Wiki_Layer]]
"""


def render_graph(docs: list[SourceDoc]) -> str:
    lines = [
        "# Wiki Graph",
        "",
        "## Metadata",
        "",
        f"- Updated: {utc_date()}",
        "- Generated by: `scripts/wiki_layer.py`",
        "",
        "## Edges",
        "",
    ]
    edges: list[str] = []
    for doc in docs:
        for link in related_links(doc, docs):
            edges.append(f"- [[{doc.slug}]] -> {link}")
    lines.extend(edges or ["- No edges yet"])
    lines.extend(["", "## Mermaid", "", "```mermaid", "graph TD"])
    if edges:
        for edge in edges:
            left, right = edge[2:].split(" -> ")
            left_id = left.strip("[]").replace("-", "_")
            right_id = right.strip("[]").replace("-", "_")
            lines.append(f"  {left_id}[{left.strip('[]')}] --> {right_id}[{right.strip('[]')}]")
    lines.append("```")
    return "\n".join(lines) + "\n"


def output_hash(path: Path) -> str | None:
    if not path.exists():
        return None
    return sha256_text(read_text(path))


def ingest(raw_dir: Path, wiki_dir: Path, force: bool = False) -> int:
    raw_dir.mkdir(parents=True, exist_ok=True)
    wiki_dir.mkdir(parents=True, exist_ok=True)
    state = load_state(wiki_dir)
    sources_state: dict[str, Any] = state.setdefault("sources", {})
    docs = build_docs(raw_dir, wiki_dir)
    conflicts: list[str] = []
    written = 0
    preserved = 0

    for doc in docs:
        rendered = render_doc(doc, docs)
        previous = sources_state.get(doc.rel_source)
        existing_text = read_text(doc.output) if doc.output.exists() else ""
        existing_hash = sha256_text(existing_text) if existing_text else None
        previous_output_hash = previous.get("output_hash") if previous else None
        previous_source_hash = previous.get("source_hash") if previous else None
        manual_edit = bool(previous_output_hash and existing_hash and existing_hash != previous_output_hash)
        source_changed = bool(previous_source_hash and previous_source_hash != doc.source_hash)

        if doc.output.exists() and not previous and not is_generated_page(existing_text) and not force:
            conflicts.append(f"- `{doc.rel_source}` maps to existing manual page `{rel(doc.output)}`")
            preserved += 1
            continue

        if manual_edit and source_changed and not force:
            conflicts.append(f"- `{doc.rel_source}` changed, but `{rel(doc.output)}` also has manual edits")
            preserved += 1
            continue

        if manual_edit and not source_changed and not force:
            preserved += 1
            continue

        write_text(doc.output, rendered)
        new_hash = sha256_text(rendered)
        sources_state[doc.rel_source] = {
            "title": doc.title,
            "slug": doc.slug,
            "output": rel(doc.output),
            "source_hash": doc.source_hash,
            "output_hash": new_hash,
            "updated_at": utc_timestamp(),
        }
        written += 1

    write_text(wiki_dir / "project-index.md", render_index(docs))
    write_text(wiki_dir / GRAPH_NAME, render_graph(docs))
    if conflicts:
        conflict_text = "# Wiki Conflicts\n\n" + "\n".join(conflicts) + "\n"
    else:
        conflict_text = "# Wiki Conflicts\n\nNo conflicts.\n"
    write_text(wiki_dir / CONFLICTS_NAME, conflict_text)
    save_state(wiki_dir, state)

    print(f"Sources: {len(docs)}")
    print(f"Written: {written}")
    print(f"Preserved: {preserved}")
    print(f"Conflicts: {len(conflicts)}")
    return 1 if conflicts else 0


def scan(raw_dir: Path, wiki_dir: Path) -> int:
    state = load_state(wiki_dir)
    known = state.get("sources", {})
    docs = build_docs(raw_dir, wiki_dir)
    print(f"Raw sources: {len(docs)}")
    for doc in docs:
        previous = known.get(doc.rel_source)
        status = "new"
        if previous and previous.get("source_hash") == doc.source_hash:
            status = "unchanged"
        elif previous:
            status = "changed"
        print(f"- {status}: {doc.rel_source} -> wiki/{doc.slug}.md")
    return 0


def graph(raw_dir: Path, wiki_dir: Path) -> int:
    docs = build_docs(raw_dir, wiki_dir)
    write_text(wiki_dir / GRAPH_NAME, render_graph(docs))
    print(f"Generated {wiki_dir.joinpath(GRAPH_NAME).relative_to(ROOT)}")
    return 0


def watch(raw_dir: Path, wiki_dir: Path, interval: int, force: bool) -> int:
    print(f"Watching {raw_dir.relative_to(ROOT)} every {interval}s. Press Ctrl+C to stop.")
    last_signature = ""
    try:
        while True:
            sources = find_sources(raw_dir)
            signature = "|".join(f"{rel(path)}:{path.stat().st_mtime_ns}" for path in sources)
            if signature != last_signature:
                ingest(raw_dir, wiki_dir, force=force)
                last_signature = signature
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Stopped.")
        return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Maintain a local raw/wiki/instructions knowledge layer.")
    parser.add_argument("command", nargs="?", default="ingest", choices=["ingest", "scan", "graph", "watch"])
    parser.add_argument("--raw", default=DEFAULT_RAW, help="Raw source directory")
    parser.add_argument("--wiki", default=DEFAULT_WIKI, help="Wiki output directory")
    parser.add_argument("--force", action="store_true", help="Overwrite generated pages even when conflicts exist")
    parser.add_argument("--interval", type=int, default=5, help="Watch interval in seconds")
    args = parser.parse_args()

    raw_dir = (ROOT / args.raw).resolve()
    wiki_dir = (ROOT / args.wiki).resolve()

    if args.command == "scan":
        return scan(raw_dir, wiki_dir)
    if args.command == "graph":
        return graph(raw_dir, wiki_dir)
    if args.command == "watch":
        return watch(raw_dir, wiki_dir, args.interval, args.force)
    return ingest(raw_dir, wiki_dir, args.force)


if __name__ == "__main__":
    raise SystemExit(main())
