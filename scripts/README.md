# Maintenance scripts

Run these scripts from the repository root with Python 3.10 or later. They use only the Python standard library.

| Script | Purpose |
| --- | --- |
| [rebuild_indexes.py](rebuild_indexes.py) | Rebuild JSON and CSV catalogs from all current Markdown source pages. Preserve existing IDs, extract metadata and sections, and record available edition paths. |
| [check_repository.py](check_repository.py) | Check local document links, offline search URLs, catalog coverage, edition paths and folder entry points. Exit with a nonzero status when an issue is found. |

```powershell
python scripts/rebuild_indexes.py
python scripts/check_repository.py
```

To show check progress, add `--verbose`. To save all findings, add `--report link-report.json`. Checks run offline and do not validate external URLs or heading fragments.

These scripts maintain catalogs and validate the repository. They do not regenerate reading editions. See [CONTRIBUTING.md](../CONTRIBUTING.md) for the editing and publishing workflow and [STRUCTURE.md](../STRUCTURE.md) for catalog path conventions.
