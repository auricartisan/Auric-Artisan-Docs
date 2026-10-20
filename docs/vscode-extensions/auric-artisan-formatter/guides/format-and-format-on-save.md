---
title: Auric Artisan Formatter — format files and format on save
description: Format a document or selection, format on save (including only changed lines), format as you type, and choose which languages Auric formats.
product: VS Code extensions › Auric Artisan Formatter
updated: 2026-09-25
---

# Format files and format on save

## Format a document

- Run **Auric Formatter: Format Document**. It uses Auric for this format even if another formatter is your default.
- Or use VS Code's own **Format Document** (`Shift` + `Alt` + `F` on Windows) once Auric is your default formatter.

The status bar reports the result: the tier used, whether the file was already formatted, whether the safety gate kept your original text, or whether the file was skipped.

## Format a selection

1. Select the code.
2. Run **Auric Formatter: Format Selection**, or right-click and choose **Format Selection**. With nothing selected: **Select some code first.**

A selection may grow to a complete syntax unit (for example a whole statement or block) so the result stays valid.

## Format on save

1. Run **Auric Formatter: Toggle Format on Save**. The message says **Auric Formatter is now your default formatter and runs on save.**
2. Save a file. It is formatted first.

Running the command again turns format on save off (**Format on save is off.**).

### Only the lines you changed

Reformatting a whole file on its first save in a large codebase makes one huge diff and clutters `git blame`. Set:

```json
{ "auricFormatter.formatOnSaveMode": "modifications" }
```

Format on save then formats only the lines changed since the last commit, using Git. The default, `file`, formats the whole file. The `minimal-diff` preset is another way to keep changes small; see [Presets](presets.md).

### If another formatter is installed

VS Code does not guess between formatters; it asks on every save. Setting `editor.defaultFormatter` stops that. **Toggle Format on Save** sets it for you.

## Format as you type

Set `auricFormatter.formatOnType` to `true` and VS Code's `editor.formatOnType` to `true`. Typing a closing character (`;`, `}`, `)`, `]`) or a new line then reformats the current line and its enclosing block.

## Choose languages

| Setting | Default | Effect |
| --- | --- | --- |
| `auricFormatter.enabledLanguages` | `[]` | Format only these VS Code language ids; empty means every supported language |
| `auricFormatter.disabledLanguages` | `[]` | Never format these language ids, even when Auric is the default formatter |

For example, to leave Markdown alone:

```json
{ "auricFormatter.disabledLanguages": ["markdown"] }
```

## Format many files

| Command | What it does |
| --- | --- |
| **Format Every File That Needs It** | Writes every file the workspace scan found would change |
| **Format Every File in the Workspace** | The same; also on a folder's context menu in the Explorer. In this version it formats every pending file in the workspace, not only that folder |

Both ask **Format *N* files?** first (while `auricFormatter.confirmBeforeFormattingAll` is on): **This rewrites files on disk. Commit or stash your work first.** Each file is re-read and re-formatted at the moment it is written, so a file you edited since the scan is never overwritten with a stale result, and open files with unsaved changes are written through the editor. These commands have no default shortcut on purpose. See [Scan the workspace](workspace-scan.md) to review first and format a folder at a time.

## Files that are skipped

A file is left alone when:

- it is larger than `auricFormatter.maxFileSizeKb` (4096 KB by default; `0` removes the limit);
- it looks minified, unless `auricFormatter.formatMinified` is on;
- it is listed in `.auricformatignore` or `.prettierignore`;
- it contains an ignore-file directive, or `auricFormatter.requirePragma` is on and it has no `@format` pragma.

The status bar shows **Skipped** with the reason, such as **Skipped — looks minified** or **Skipped — larger than maxFileSizeKb**.

A parse that runs longer than `auricFormatter.parseTimeoutMs` (5000 ms by default) is abandoned.

When formatting works, the status bar shows **Auric** with a tick, and its tooltip names the tier that formatted the file.
