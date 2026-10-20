#!/usr/bin/env python3
"""Check local document links, offline search URLs and machine-readable indexes."""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class HTMLLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        self.links.extend(value for key, value in attrs if key in {"href", "src"} and value)


def document_links(path: Path):
    text = path.read_text(encoding="utf-8-sig")
    if path.suffix == ".html":
        parser = HTMLLinks()
        parser.feed(text)
        return parser.links
    if path.suffix == ".txt":
        return re.findall(r"\[([^\]\s]+\.(?:txt|md|html)(?:#[^\]\s]*)?)\]", text)
    # Fenced examples are not navigation links.
    text = re.sub(r"(?ms)^(`{3,}|~{3,}).*?^\1[^\n]*$", "", text)
    text = re.sub(r"(`+)[^`\n]*\1", "", text)
    inline = re.findall(r"!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)", text)
    definitions = re.findall(r"(?m)^\s{0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)", text)
    return [link.strip("<>") for link in inline + definitions]


def run(root: Path, verbose: bool = False):
    errors = []
    checked = 0
    roots = [root / name for name in ("docs", "exports", "data", "scripts")]
    files = [Path(directory) / name for folder in roots for directory, _, names in os.walk(folder) for name in names]
    files.extend(p for p in root.iterdir() if p.is_file())
    existing = {os.path.normcase(str(p)) for p in files}
    existing.update(os.path.normcase(str(parent)) for p in files for parent in p.parents if parent.is_relative_to(root))
    def exists(path):
        return os.path.normcase(str(path)) in existing

    for folder in roots:
        if not exists(folder / "README.md"):
            errors.append(f"{folder.relative_to(root)}: missing folder README.md")
    for position, path in enumerate(sorted(files)):
        if verbose and position % 250 == 0:
            print(f"Checking {position:,}/{len(files):,}: {path.relative_to(root)}", flush=True)
        if path.suffix not in {".md", ".txt", ".html"}:
            continue
        for link in document_links(path):
            parsed = urlsplit(unescape(link))
            if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith("/"):
                continue
            checked += 1
            target = Path(os.path.abspath(path.parent / unquote(parsed.path)))
            if not target.is_relative_to(root):
                errors.append(f"{path.relative_to(root)}: link leaves repository: {link}")
            elif os.path.normcase(str(target)) not in existing:
                errors.append(f"{path.relative_to(root)}: missing {link}")

    html = root / "exports/html"
    search = html / "assets/search-index.js"
    if search.exists():
        payload = search.read_text(encoding="utf-8").split("=", 1)[1].rstrip().removesuffix(";")
        for entry in json.loads(payload):
            checked += 1
            if not exists(html / entry["u"]):
                errors.append(f"{search.relative_to(root)}: missing {entry['u']}")

    data = root / "data"
    index = data / "json/docs-index.json"
    source = root / "docs"
    if index.exists():
        index_data = json.loads(index.read_text(encoding="utf-8"))
        entries = index_data["entries"]
        indexed = {entry["path"] for entry in entries}
        actual = {p.relative_to(source).as_posix() for p in files if p.suffix == ".md" and p.is_relative_to(source)}
        for missing in sorted(actual - indexed):
            errors.append(f"{index.relative_to(root)}: source document is not indexed: {missing}")
        for entry in entries:
            checked += 1
            if not exists(source / entry["path"]):
                errors.append(f"{index.relative_to(root)}: missing source {entry['path']}")
            for edition in entry.get("editions", {}).values():
                checked += 1
                if not exists(root / edition):
                    errors.append(f"{index.relative_to(root)}: missing edition {edition}")
        if index_data["documents"] != len(entries):
            errors.append(f"{index.relative_to(root)}: incorrect document count")
        if len(indexed) != len(entries):
            errors.append(f"{index.relative_to(root)}: duplicate source paths")

    tree_path = data / "json/tree.json"
    if tree_path.exists():
        tree_docs = set()

        def check_tree(node):
            folder = source / node["folder"]
            if not exists(folder):
                errors.append(f"{tree_path.relative_to(root)}: missing folder {node['folder']}")
            for doc in node["documents"]:
                target = folder / doc["file"]
                tree_docs.add(target.relative_to(source).as_posix())
                if not exists(target):
                    errors.append(f"{tree_path.relative_to(root)}: missing {target.relative_to(root)}")
            for child in node["folders"]:
                check_tree(child)

        check_tree(json.loads(tree_path.read_text(encoding="utf-8")))
        if index.exists() and tree_docs != indexed:
            errors.append(f"{tree_path.relative_to(root)}: documents differ from docs-index.json")

    sections_path = data / "json/sections.json"
    if sections_path.exists():
        sections = json.loads(sections_path.read_text(encoding="utf-8"))
        for doc in {section["doc"] for section in sections}:
            if not exists(source / doc):
                errors.append(f"{sections_path.relative_to(root)}: missing source {doc}")

    for name, column in (("docs-index.csv", "path"), ("folders.csv", "folder")):
        path = data / "csv" / name
        if path.exists():
            with path.open(encoding="utf-8-sig", newline="") as stream:
                rows = list(csv.DictReader(stream))
            for row in rows:
                checked += 1
                if not exists(source / row[column]):
                    errors.append(f"{path.relative_to(root)}: missing {row[column]}")
            if name == "docs-index.csv" and index.exists() and {row[column] for row in rows} != indexed:
                errors.append(f"{path.relative_to(root)}: documents differ from docs-index.json")

    for folder in (source, root / "exports/text", html):
        for directory, _, _ in os.walk(folder):
            path = Path(directory)
            if not exists(path / "README.md"):
                errors.append(f"{path.relative_to(root)}: missing folder README.md")
    return checked, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, help="Write all findings to a JSON file")
    parser.add_argument("--verbose", action="store_true", help="Show progress while checking")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    checked, errors = run(root, args.verbose)
    if args.report:
        args.report.write_text(json.dumps({"checked": checked, "errors": errors}, indent=2) + "\n", encoding="utf-8")
    print(f"Checked {checked:,} local links and index paths; {len(errors):,} issue(s).")
    for error in errors[:30]:
        print(error)
    if len(errors) > 30:
        print(f"... {len(errors) - 30:,} more issue(s); use --report to save the full list.")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
