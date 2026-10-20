# Auric Artisan Docs

User documentation for [Auric Artisan](https://auricartisan.com): the website and its tools, seventeen VS Code extensions, the browser extension, design-tool plugins, the Font CDN, the Icon CDN and the public API.

The documentation explains screens, controls, settings and real workflows for designers, developers, accessibility specialists and students. The Markdown source contains **1,748 documents in 319 folders**.

## Start reading

- New to Auric Artisan? Start with [Getting started](docs/getting-started/README.md).
- Find a product in the [documentation contents](docs/README.md), [website tools](docs/website/tools/README.md) or [VS Code extensions](docs/vscode-extensions/README.md).
- Get answers in [Help](docs/help/README.md).
- Read offline by opening [exports/html/index.html](exports/html/index.html). Use [offline search](exports/html/search.html) to find a page.
- Choose a printable, e-book, Word or text edition in [Exports](exports/README.md).

## Repository layout

| Folder | Purpose |
| --- | --- |
| [docs/](docs/README.md) | Editable Markdown source, arranged by product and topic. |
| [exports/](exports/README.md) | Published HTML, plain-text, PDF, EPUB and Word editions. |
| [data/](data/README.md) | JSON and CSV catalogs generated from the current source. |
| [scripts/](scripts/README.md) | Local link checks and catalog generation. |

```text
docs/
|-- getting-started/
|-- website/                Tools, site features, kits, library and account guides
|-- vscode-extensions/
|-- browser-extension/
|-- services/
|-- design-tool-plugins/
`-- help/

exports/                    html/, text/, pdf/, epub/, word/
data/                       json/, csv/
scripts/                    check_repository.py, rebuild_indexes.py
```

Each product or tool has an overview in `README.md`, practical documentation in `guides/`, and supporting material in `resources/`. Every documentation folder has a `README.md` entry point. See [STRUCTURE.md](STRUCTURE.md) for the complete arrangement and the previous-to-current path map.

## Maintain the documentation

Edit the source in `docs/`, add navigation in its folder's `README.md`, then refresh the catalogs and check local links:

```powershell
python scripts/rebuild_indexes.py
python scripts/check_repository.py
```

Both scripts use the Python standard library and require Python 3.10 or later. See [CONTRIBUTING.md](CONTRIBUTING.md) for naming, editing and publishing instructions.

Reading editions are published snapshots and may lag the Markdown source. Their product content and publication dates are preserved; text and HTML navigation uses the current folder structure. The catalogs describe the current source and link to editions that exist.

Legal summaries help explain the policies; the official pages on auricartisan.com are authoritative. Questions and corrections: [Contact Auric Artisan](https://auricartisan.com/company/contact/).

© 2026 Auric Artisan. All rights reserved.
