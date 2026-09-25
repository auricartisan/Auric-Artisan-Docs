# Auric Artisan Docs

The complete user documentation for **Auric Artisan**: the website at https://auricartisan.com and every tool on it, the seventeen VS Code extensions, the browser extension, and the services — the Font CDN, the Icon CDN and the public API.

It is written for the people who **use** the products — designers, developers, accessibility specialists, students — not for the people who build them. It explains every screen, control, command and setting, walks through real tasks step by step, states what each tool measures and how precisely, and says what to do when something does not behave as expected.

Updated 25 September 2026 · 1,747 documents · about 927,000 words · 319 folders.

## Three editions of the same content

| Folder | Format | Open it with |
| --- | --- | --- |
| [md/](md/README.md) | **Markdown** — the source edition. Renders on GitHub with working links. | GitHub, any Markdown viewer or editor |
| [txt/](txt/README.md) | **Plain text** — 78 columns, no formatting, one `.txt` per document. | Any text editor, terminal or screen reader |
| [other/](other/README.md) | **HTML, PDF, EPUB, Word, JSON and CSV**, all generated from `md/`. | See below |

Inside [other/](other/README.md):

| Folder | What you get |
| --- | --- |
| [other/html/](other/html/README.md) | A browsable offline website with navigation and search. Open `other/html/index.html` in any browser — no server or internet needed. Follows your light or dark setting. |
| [other/pdf/](other/pdf/README.md) | A4 PDFs with a cover, clickable contents, bookmarks and page numbers — one per area, with the website split into its ten sections. |
| [other/epub/](other/epub/README.md) | The whole documentation as one EPUB 3 e-book for phones, tablets and e-readers. |
| [other/docx/](other/docx/README.md) | Editable Word documents, one per area. |
| [other/json/](other/json/README.md) | Machine-readable indexes and the full text split by section, for search tools and assistants. |
| [other/csv/](other/csv/README.md) | Spreadsheet lists of every document and folder. |

The three editions mirror each other folder for folder, and **every folder in every edition has a `README.md`** that says what the folder covers and lists what is inside it.

## What is covered

```text
md/
├── getting-started/          What Auric Artisan is, where to start, accounts, privacy, language, offline use
├── website/
│   ├── site-features/        19 features on every page: settings, theme, language, right-click menu, search, …
│   ├── tools/                31 tools in five groups
│   │   ├── accessibility-and-vision/     Analyzer, Contrast Checker, Checklist, Vision Lab, Ishihara, …
│   │   ├── colour-workspace/             Basic Color Tools, Color Science Lab, Design Engine, Font and Icon Library, …
│   │   ├── colorimetry-and-rendering/    Illuminants, Chromatic Adaptation, Gamut Map, Gamut Lab, HDR, Tone Mapping, …
│   │   ├── perception-and-spectral/      Visual Pathway, Perception, Psychophysics, Dye in Solution, Material Under Light
│   │   └── image-and-file-tools/         Collage Maker, ICC Profile Parser, Image Picker, LUT Lab, M-Gradient, SVG Recolour
│   ├── kits/                 Feature, Menu, Advanced, Status and Library kits, and website updates
│   ├── library/              Six colour libraries, Collections, Learn (113 articles), documentation, blog, changelog
│   ├── portfolio/            The Portfolio Builder and the public portfolio directory
│   ├── search/               Web search and the Search Console
│   ├── account-and-billing/  Accounts, dashboard, security, plans, tokens, payments, invoices, API keys, deletion
│   ├── download-and-offline/ Installing the site as an app and using it offline
│   ├── advertise/            Advertising on Auric Artisan
│   └── company-and-legal/    Plain-language summaries of company pages and every legal policy
├── vscode-extensions/        All 17 extensions, each with docs/ and others/
│   ├── install-and-setup/
│   ├── auric-artisan-studio/ Full Pack, Color, Accessibility (70+ WCAG rules), Code Health
│   ├── auric-artisan-theme/  54 themes and the Theme Studio
│   ├── …icons, emoji, Icon Studio, Icon Hub, File Icons…
│   └── …Live, File System, Font Hub, Formatter
├── browser-extension/        Install, surfaces, colour, contrast, vision, audit (80 rules), code, saved items, settings
├── services/                 Font CDN, Icon CDN, public REST API
├── design-tool-plugins/      Status of the design-tool and launcher plugins
└── help/                     FAQ, glossary, troubleshooting, accessibility, privacy, support
```

Every product and tool folder follows the same pattern:

- `README.md` — what it is, who it is for, where to find it, a quick start, what you can do.
- `docs/` — getting started, one guide per task, a complete reference, troubleshooting, FAQ.
- `others/` — glossary, shortcuts, limits and accuracy, related tools, release notes, privacy.

## How to read these docs

- **New to Auric Artisan?** Start at [md/getting-started/](md/getting-started/README.md).
- **Looking for one tool?** The [tools catalogue](md/website/tools/README.md) and the [VS Code extensions list](md/vscode-extensions/README.md) link to every one.
- **Offline or on paper?** Use the HTML site or the PDFs in [other/](other/README.md).
- **Searching?** Open `other/html/search.html`, or search the repository on GitHub.

## Notes

- The docs describe each product as users have it on the date above. Where a product's own screens disagree with each other, the docs describe what the product actually does and say so.
- Legal summaries are there to help you understand the policies; the official pages on auricartisan.com are authoritative.
- Questions or corrections: https://auricartisan.com/company/contact/

© 2026 Auric Artisan. All rights reserved.
