#!/usr/bin/env python3
"""Rebuild JSON and CSV catalogs from docs/ using only the Python standard library."""

from __future__ import annotations

import csv
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs"
DATA = ROOT / "data"


def read_document(path):
    text = path.read_text(encoding="utf-8")
    metadata = {}
    body = text
    if text.startswith("---\n"):
        header, body = text[4:].split("\n---\n", 1)
        for line in header.splitlines():
            key, separator, value = line.partition(":")
            if separator:
                metadata[key.strip()] = value.strip().strip('"')
    title = metadata.get("title") or next(iter(re.findall(r"(?m)^# (.+)$", body)), path.stem)
    return metadata, title, body


def plain_text(text):
    text = re.sub(r"!?\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"(?m)^#{1,6}\s+", "", text)
    text = re.sub(r"[`*_~]", "", text)
    return " ".join(text.split())


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def write_csv(path, columns, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, extrasaction="ignore", lineterminator="\r\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    if not SOURCE.is_dir():
        raise SystemExit("The docs/ source directory is missing.")
    index_path = DATA / "json/docs-index.json"
    previous = json.loads(index_path.read_text(encoding="utf-8")) if index_path.exists() else {"entries": []}
    identifiers = {entry["path"]: entry["id"] for entry in previous["entries"]}
    used = set(identifiers.values())
    entries = []
    sections = []
    documents = {}
    source_files = [Path(directory) / name for directory, _, names in os.walk(SOURCE) for name in names if name.endswith(".md")]
    edition_files = {Path(directory) / name for edition in ("text", "html") for directory, _, names in os.walk(ROOT / "exports" / edition) for name in names}
    for path in sorted(source_files, key=lambda p: (p.relative_to(SOURCE).as_posix() != "README.md", p.relative_to(SOURCE).as_posix())):
        relative = path.relative_to(SOURCE).as_posix()
        metadata, title, body = read_document(path)
        identifier = identifiers.get(relative)
        if identifier is None:
            sequence = len(used)
            while f"doc-{sequence}" in used:
                sequence += 1
            identifier = f"doc-{sequence}"
            used.add(identifier)
        editions = {"md": path.relative_to(ROOT).as_posix()}
        for key, directory, suffix in (("txt", "exports/text", ".txt"), ("html", "exports/html", ".html")):
            candidate = ROOT / directory / Path(relative).with_suffix(suffix)
            if candidate in edition_files:
                editions[key] = candidate.relative_to(ROOT).as_posix()
        entry = {
            "id": identifier,
            "area": relative.split("/", 1)[0],
            "path": relative,
            "title": title,
            "description": metadata.get("description", ""),
            "product": metadata.get("product", "Auric Artisan"),
            "updated": metadata.get("updated", ""),
            "words": len(plain_text(body).split()),
            "sections": re.findall(r"(?m)^## (.+)$", body),
            "editions": editions,
        }
        entries.append(entry)
        documents[relative] = entry
        parts = re.split(r"(?m)^## (.+)\n", body)
        intro = re.sub(r"(?m)^# .+\n", "", parts[0], count=1)
        sections.append({"doc": relative, "title": title, "heading": "", "text": plain_text(intro)})
        for position in range(1, len(parts), 2):
            sections.append({"doc": relative, "title": title, "heading": parts[position], "text": plain_text(parts[position + 1])})

    folder_rows = []

    def make_tree(folder):
        relative = folder.relative_to(SOURCE).as_posix()
        overview = documents.get((folder / "README.md").relative_to(SOURCE).as_posix(), {})
        direct = [documents[p.relative_to(SOURCE).as_posix()] for p in sorted(folder.glob("*.md"), key=lambda p: (p.name != "README.md", p.name))]
        node = {
            "folder": relative,
            "title": overview.get("title", folder.name),
            "description": overview.get("description", ""),
            "documents": [{"file": Path(e["path"]).name, "title": e["title"], "description": e["description"]} for e in direct],
            "folders": [make_tree(p) for p in sorted(folder.iterdir()) if p.is_dir()],
        }
        folder_rows.append({"area": relative.split("/", 1)[0], "folder": relative, "title": node["title"], "description": node["description"], "documents": len(direct)})
        return node

    tree = make_tree(SOURCE)
    index = {
        "title": "Auric Artisan user documentation",
        "updated": max(entry["updated"] for entry in entries),
        "documents": len(entries),
        "words": sum(entry["words"] for entry in entries),
        "path_base": "docs/",
        "edition_path_base": "repository root",
        "entries": entries,
    }
    write_json(index_path, index)
    write_json(DATA / "json/tree.json", tree)
    write_json(DATA / "json/sections.json", sections)
    write_csv(DATA / "csv/docs-index.csv", ["area", "path", "title", "description", "product", "words", "updated"], entries)
    write_csv(DATA / "csv/folders.csv", ["area", "folder", "title", "description", "documents"], sorted(folder_rows, key=lambda row: row["folder"]))
    print(f"Indexed {len(entries):,} source documents, {len(folder_rows):,} folders and {len(sections):,} sections.")


if __name__ == "__main__":
    main()
