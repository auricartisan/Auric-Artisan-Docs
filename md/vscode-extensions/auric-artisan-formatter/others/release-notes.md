---
title: Auric Artisan Formatter — release notes
description: What changed in each published version of Auric Artisan Formatter.
product: VS Code extensions › Auric Artisan Formatter
updated: 2026-09-25
---

# Release notes

Formatting output is treated as part of the extension's public behaviour: a change that makes an already-formatted file format differently is at least a minor version and is listed under "Formatting changes", so a team can decide when to take the diff.

## 0.1.0 (23 September 2026)

The first Marketplace release.

### Editor

- A native read-only formatting preview beside the source, with **Apply**, **Discard**, **Refresh** and **Compare Changes** in the editor title and CodeLens.
- Format document, selection and every pending file; format on save, optionally only changed lines; format as you type.
- A status bar item reporting the tier and any safety reversion.
- **Explain Formatting Decisions**, **Import Settings From Prettier**, **Generate a Configuration File**, **Switch Formatting Preset** and **Report a Formatting Problem**.
- A setup walkthrough on the Welcome page.

### Formatter Studio

- Formatter Studio and a matching Explorer sidebar, with searchable drop-downs, a filterable option rail (category, changed-only, affects-this-file and experimental filters), **Find what matters**, and live **Result**, **Diff** and **Explain** views.
- **Full document** and **Editor selection** scopes, a preview toggle, and explicit **Yes, apply** and **No, discard**. Apply is bound to the original document and refuses stale, discarded, scratch and truncated previews.
- A side-by-side or inline diff with change highlights, change navigation and expandable context.
- A validated JSON rules editor and **Copy config**, which exports only the options you changed.
- A command palette on `Ctrl` + `K`, full light, dark, high-contrast, forced-colours and reduced-motion support, and state that survives a reload.

### Workspace

- The in-memory workspace scan: the ***N* unformatted** status bar count and the **Workspace** tab, with sorting, filtering, **Format selected**, **Format all files** and per-file diffs. Nothing is written until you choose.
- Files are re-read and re-formatted at the moment they are written, and open unsaved files are written through the editor.
- Tracking of edits and file changes, with bounded rescans for new files; the preset or a configuration change re-runs the scan.
- **Check Formatting Without Writing (CI Mode)** reports line counts per file in Problems.
- New settings: `scanOnStartup`, `scanExclude`, `scanMaxFiles`, `confirmBeforeFormattingAll`.

### Engine

- A zero-dependency engine that measures width in display columns, so CJK text, emoji and combining marks break where a person expects.
- 391 options in 17 categories, each with a type, a validated default and a command-line flag.
- 13 presets, including `prettier`, byte-compatible with Prettier 3 at its defaults.
- Native formatting for 31 modes, including JavaScript and TypeScript, and a universal structural engine for 220 more languages.
- The five-check safety gate, aware of which changes your options allow.
- Tiered fallback: a failed parse falls back to safe whitespace formatting.
- Configuration compatibility with `.auricformatrc`, `package.json`, `.editorconfig` and Prettier configuration, with per-language and per-glob overrides and inline directives.
- The `auric-format` command line with the familiar `--check`, `--write`, `--list-different` and related flags, and typo suggestions.
- A plugin mechanism for additional languages, where a failing plugin disables itself.

### Not in this release

- A native JSX front end: `.jsx` and `.tsx` files containing JSX elements are formatted by the universal tier.
