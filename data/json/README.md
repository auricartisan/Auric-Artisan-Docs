# JSON catalogs

Machine-readable indexes of the current [Markdown source](../../docs/README.md), for search tools, assistants and scripts.

| File | Contents |
| --- | --- |
| [docs-index.json](docs-index.json) | One entry per source document: stable ID, area, path, title, description, product, update date, word count, headings and available editions. |
| [tree.json](tree.json) | Folder tree with every folder's title, description and document list. |
| [sections.json](sections.json) | Document text split at level-two headings, including the introduction. |

`path`, `folder` and `doc` values are relative to `docs/`; the root folder is `.`. The document index's `editions` values are relative to the repository root. The `md`, `txt` and `html` edition keys identify formats. An edition is listed only when its file exists; existence does not imply its content is current with the source.

The index's `updated` value is the latest product-content date recorded by a source page. Run `python scripts/rebuild_indexes.py` from the repository root to refresh all JSON and CSV catalogs together. See [STRUCTURE.md](../../STRUCTURE.md) for the full path schema and [data/](../README.md) for other catalogs.
