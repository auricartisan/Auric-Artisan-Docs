# CSV catalogs

Spreadsheet-ready inventories of the current [Markdown source](../../docs/README.md). Both files use UTF-8 with a byte-order mark and CRLF line endings, so spreadsheet applications open them with the right characters.

| File | What it contains |
| --- | --- |
| [docs-index.csv](docs-index.csv) | One row per document: area, path, title, summary, product, word count, updated. |
| [folders.csv](folders.csv) | One row per folder: area, path, title, summary and how many documents it holds. |

Document paths and folder paths are relative to `docs/`. The root folder is `.`. The folder inventory counts documents directly inside each folder, including its `README.md`.

Run `python scripts/rebuild_indexes.py` from the repository root to refresh these files together with the [JSON catalogs](../json/README.md). See [STRUCTURE.md](../../STRUCTURE.md) for path conventions and [data/](../README.md) for all catalogs.
