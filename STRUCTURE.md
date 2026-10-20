# Repository structure

The repository separates editable documentation, published reading editions, structured catalogs and maintenance tools.

```text
Auric-Artisan-Docs/
|-- README.md                  Repository entry point
|-- CONTRIBUTING.md            Editing and validation workflow
|-- STRUCTURE.md               Folder conventions and migration map
|-- docs/                      Editable Markdown source
|   |-- getting-started/
|   |-- website/
|   |   |-- site-features/
|   |   |-- tools/
|   |   |-- kits/
|   |   |-- library/
|   |   |-- portfolio/
|   |   |-- search/
|   |   |-- account-and-billing/
|   |   |-- download-and-offline/
|   |   |-- advertise/
|   |   `-- company-and-legal/
|   |-- vscode-extensions/
|   |-- browser-extension/
|   |-- services/
|   |-- design-tool-plugins/
|   `-- help/
|-- exports/                   Published reading editions
|   |-- html/                  Offline website and search assets
|   |-- text/                  Plain-text pages and folder navigation
|   |-- pdf/                   Printable publications
|   |-- epub/                  Complete e-book
|   `-- word/                  Editable Word publications
|-- data/                      Catalogs generated from docs/
|   |-- json/                  Document index, folder tree, section text
|   `-- csv/                   Document and folder inventories
`-- scripts/                   Local checks and catalog generation
```

## Product folders

Each product or tool uses the same arrangement where applicable:

```text
product-name/
|-- README.md                  Overview, quick start and navigation
|-- guides/
|   |-- README.md              Guide contents
|   |-- getting-started.md
|   |-- task-name.md
|   |-- reference.md
|   |-- troubleshooting.md
|   `-- faq.md
`-- resources/
    |-- README.md              Supporting material contents
    |-- glossary.md
    |-- shortcuts.md
    |-- limits-and-accuracy.md
    |-- related.md
    |-- release-notes.md
    `-- privacy.md
```

Larger guides may group workflows or features into subfolders. General sections such as getting started and help can keep their documents directly in the section folder. The text and HTML editions follow the same product hierarchy, with their respective file extensions and additional `README.md` navigation files.

Use descriptive names rather than numbered folders. Keep product identifiers and topic filenames stable. Every documentation folder has a `README.md` entry point.

## Path changes made on 21 October 2026

| Previous location | Current location |
| --- | --- |
| `md/` | `docs/` |
| `txt/` | `exports/text/` |
| `other/html/` | `exports/html/` |
| `other/pdf/` | `exports/pdf/` |
| `other/epub/` | `exports/epub/` |
| `other/docx/` | `exports/word/` |
| `other/json/` | `data/json/` |
| `other/csv/` | `data/csv/` |
| Product-level `docs/` | `guides/` in source, text and HTML editions |
| Product-level `others/` | `resources/` in source, text and HTML editions |

For example, `md/browser-extension/docs/getting-started.md` is now `docs/browser-extension/guides/getting-started.md`.

Local navigation and offline search paths follow the new locations. PDF, EPUB and Word publications retain their original bytes and publication dates. The Markdown source includes later revisions than those snapshots; catalog refreshes always read the current source.

## Catalog path conventions

`path` in the document index, `doc` in the section index, and `folder` in the folder tree and CSV inventory are relative to `docs/`. The tree's root folder is `.`. The `editions` values in `docs-index.json` are relative to the repository root. The `md`, `txt` and `html` edition keys identify formats and remain stable regardless of their folder names.

The offline HTML search index uses URLs relative to `exports/html/`. It describes the published HTML edition, rather than unpublished Markdown revisions.

Local application state in `.auric-artisan/` stays outside the documentation hierarchy and is ignored by Git.
