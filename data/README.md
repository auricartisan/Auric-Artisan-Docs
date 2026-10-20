# Documentation catalogs

Machine-readable catalogs generated from the current [Markdown source](../docs/README.md).

| Folder | Contents |
| --- | --- |
| [json/](json/README.md) | Document metadata and available editions, the folder tree, and full text split by section. |
| [csv/](csv/README.md) | Document and folder inventories for spreadsheets and audits. |

Document and folder paths are relative to `docs/`. Edition paths in the JSON document index are relative to the repository root. Catalogs cover the current source; the [reading editions](../exports/README.md) have their own publication dates.

Refresh both formats together:

```powershell
python scripts/rebuild_indexes.py
python scripts/check_repository.py
```

See [STRUCTURE.md](../STRUCTURE.md) for the path schema and [CONTRIBUTING.md](../CONTRIBUTING.md) for maintenance instructions.
