# Contributing to the documentation

Edit the Markdown documents in [docs/](docs/README.md). They are the source of truth for user-facing content. Use the product's existing terminology, keep instructions focused on real user tasks, and update the page's `updated` field when its product information changes.

## Choose the right location

- Product overview and quick start: the product's `README.md`.
- Setup, workflows, control reference, troubleshooting and FAQ: `guides/`.
- Glossary, shortcuts, limitations, release notes, privacy and related tools: `resources/`.
- General onboarding and help: `docs/getting-started/` and `docs/help/`.

Use lowercase, hyphen-separated names for folders and topic files. Keep `README.md` as each folder's entry point and list new documents in its navigation. Use relative links between documents so they work on GitHub and in a local checkout. Preserve heading names when possible because links may point to them.

See [STRUCTURE.md](STRUCTURE.md) for the full folder map and the previous-to-current path conventions.

## Refresh the catalogs

Python 3.10 or later is sufficient; no third-party packages are required. Run these commands from the repository root:

```powershell
python scripts/rebuild_indexes.py
python scripts/check_repository.py
```

The first command refreshes the JSON and CSV catalogs from the current Markdown source. Existing document IDs remain stable when their paths have not changed. Edition links are included only when the corresponding file exists.

The second command checks local Markdown, text and HTML file links, offline search destinations, source coverage in the catalogs, edition paths and folder entry points. It does not contact external websites or validate heading fragments. Use `--report` to save findings:

```powershell
python scripts/check_repository.py --report link-report.json
```

## Publish reading editions

The files in [exports/](exports/README.md) are published snapshots. Refreshing the catalogs does not rebuild the text, HTML, PDF, EPUB or Word editions. Regenerate those editions through the publishing process when publishing updated product content, then check their links again. Keep their publication dates accurate.

Keep the HTML stylesheet, scripts and search index with the HTML edition so it continues to open offline. Preserve UTF-8 with a byte-order mark and CRLF line endings in CSV files; [the index script](scripts/rebuild_indexes.py) writes these automatically. Other text files use UTF-8 and LF line endings, as defined in [.gitattributes](.gitattributes).
