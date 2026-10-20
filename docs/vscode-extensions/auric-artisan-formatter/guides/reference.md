---
title: Auric Artisan Formatter — reference
description: Every Auric Artisan Formatter command, keyboard shortcut, menu entry, status bar state, file and editor setting.
product: VS Code extensions › Auric Artisan Formatter
updated: 2026-09-25
---

# Reference: commands, keys and settings

This page covers Auric Artisan Formatter 0.1.0: 21 commands, 3 keyboard shortcuts, one Explorer view, a setup walkthrough, 11 editor settings and 391 formatting options (listed in the [options reference](options-reference.md)). Commands appear in the Command Palette with the **Auric Formatter:** prefix.

## Commands

| Command | ID | Keys | What it does |
| --- | --- | --- | --- |
| **Format Document** | `auricFormatter.formatDocument` | — | Format the active file with Auric |
| **Format Selection** | `auricFormatter.formatSelection` | — | Format the selected code (shown only with a selection) |
| **Format Every File in the Workspace** | `auricFormatter.formatWorkspace` | — | Write every file the scan found would change (asks first) |
| **Format Every File That Needs It** | `auricFormatter.formatAll` | — | The same, from the scan results (asks first) |
| **Scan the Workspace Without Writing** | `auricFormatter.scanWorkspace` | — | Format every file in memory and report; offers **Review them** or **Format them all** |
| **Show Files That Need Formatting** | `auricFormatter.showPending` | `Ctrl` + `Alt` + `Shift` + `U` | Open Formatter Studio on the **Workspace** tab |
| **Check Formatting Without Writing (CI Mode)** | `auricFormatter.checkWorkspace` | — | Scan and list unformatted files in the Problems panel |
| **Open Formatter Studio** | `auricFormatter.openPlayground` | `Ctrl` + `Alt` + `Shift` + `P` | Open Formatter Studio |
| **Preview Formatting as a Diff** | `auricFormatter.previewDiff` | `Ctrl` + `Alt` + `Shift` + `F` (editor focused) | Open a read-only formatted copy beside the source |
| **Apply Formatting Preview** | `auricFormatter.applyPreview` | — | Apply the open preview to its source, after confirmation |
| **Discard Formatting Preview** | `auricFormatter.discardPreview` | — | Close the preview without changes |
| **Refresh Formatting Preview** | `auricFormatter.refreshPreview` | — | Format the source again and update the preview |
| **Compare Formatting Changes** | `auricFormatter.comparePreview` | — | Open the diff between source and preview |
| **Explain Formatting Decisions for This File** | `auricFormatter.explainFormatting` | — | Open a report of language, parser, tier, option sources and warnings |
| **Switch Formatting Preset** | `auricFormatter.selectPreset` | — | Choose one of the 13 presets |
| **Generate a Configuration File** | `auricFormatter.generateConfig` | — | Write `.auricformatrc` with your preset and settings |
| **Import Settings From Prettier** | `auricFormatter.migrateFromPrettier` | — | Convert a Prettier configuration into an unsaved Auric one |
| **Toggle Format on Save** | `auricFormatter.toggleFormatOnSave` | — | Turn format on save on (and make Auric the default formatter) or off |
| **Show the Formatter Log** | `auricFormatter.showOutput` | — | Open the **Auric Artisan Formatter** output channel |
| **Report a Formatting Problem** | `auricFormatter.reportIssue` | — | Open a Markdown template with version, language, tier and explanation |
| **Clear the Configuration Cache** | `auricFormatter.clearCache` | — | Forget cached configuration so files are re-read |

On macOS, `Cmd` replaces `Ctrl` in the three shortcuts. **Format Every File That Needs It** and **Format Every File in the Workspace** have no shortcut on purpose.

## Where commands appear

- Editor title bar: **Preview Formatting as a Diff** (supported files)
- Editor title bar, in a preview: **Apply Formatting Preview**, **Compare Formatting Changes**, **Refresh Formatting Preview**, **Discard Formatting Preview**
- Preview CodeLens: **Apply formatting** (or **No formatting changes**, or **Source changed — refresh preview**), **Compare changes**, **Discard preview**, **Full file · refresh preview** / **Selection preview · refresh from source**
- Editor context menu: **Format Selection** with a selection; **Preview Formatting as a Diff** without
- Explorer context menu, on a folder: **Format Every File in the Workspace**
- Explorer: The **Auric Formatter** view
- Welcome page: The walkthrough **Set up Auric Artisan Formatter**

## Status bar

| Text | Meaning |
| --- | --- |
| **Auric** (brush icon) | Ready for this language |
| **Auric** with a tick | Formatted, or already formatted; the tooltip names the tier and the time |
| **Auric** with a shield | The safety gate kept your original text |
| **Auric** with a slash | Skipped, with the reason in the tooltip |
| **Auric** with an error | Formatting failed |
| **Auric *scanned*/*total*** (spinning) | Scanning in memory |
| **Auric writing…** | Writing formatted files |
| ***N* unformatted** | Files the scan found would change; select to review |
| **Auric** with a double tick | Every scanned file is formatted |

The first four open the log when selected.

## Editor settings

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricFormatter.preset` | string | `auric` | 13 presets (see [Presets](presets.md)) | The preset to start from; your own options and a configuration file's `preset` win |
| `auricFormatter.formatOnType` | boolean | `false` | — | Reformat the line and block as you type closing punctuation; needs `editor.formatOnType` |
| `auricFormatter.formatOnSaveMode` | string | `file` | `file`, `modifications` | Format the whole file on save, or only lines changed since the last commit |
| `auricFormatter.showStatusBar` | boolean | `true` | — | Show the status bar item for the tier and safety result |
| `auricFormatter.logLevel` | string | `warn` | `silent`, `error`, `warn`, `log`, `debug` | How much reaches the output channel |
| `auricFormatter.enabledLanguages` | array | `[]` | Language ids | Format only these languages; empty means all |
| `auricFormatter.disabledLanguages` | array | `[]` | Language ids | Never format these languages |
| `auricFormatter.scanOnStartup` | boolean | `true` | — | Scan the workspace in memory when the window opens |
| `auricFormatter.scanExclude` | array | `[]` | Globs | Globs the scan skips; empty uses the built-in list |
| `auricFormatter.scanMaxFiles` | integer | `4000` | 1 or more | Stop the scan after this many files |
| `auricFormatter.confirmBeforeFormattingAll` | boolean | `true` | — | Ask before writing more than one file |

All settings, including the 391 options, have resource scope: they can be set for the user, the workspace or a single folder.

## Files

| File | Role |
| --- | --- |
| `.auricformatrc` and its variants, `auric.format.json`, `package.json` (`auricFormatter` key) | Configuration; see [Configuration](configuration.md) |
| `.prettierrc` and variants, `package.json` (`prettier` key) | Read for compatibility |
| `.editorconfig` | Read for indentation, line endings, line length and final newline |
| `.auricformatignore`, `.prettierignore` | Files not to format |

Written by the extension:

| What | When |
| --- | --- |
| `.auricformatrc` | **Generate a Configuration File** |
| `editor.defaultFormatter`, `editor.formatOnSave` | **Toggle Format on Save** (workspace settings, or user settings with no folder open) |
| `auricFormatter.preset` | **Switch Formatting Preset** |
| Your source files | Format commands, **Apply**, format on save, **Format selected** / **Format all files** |

## Workspace trust and virtual workspaces

- In an untrusted workspace, configuration files are read but JavaScript configuration files and formatter plugins are not run.
- Virtual workspaces are supported.

## Setup walkthrough

**Set up Auric Artisan Formatter** on the Welcome page has five steps: **Choose a preset**, **Try the Playground**, **See what the whole repository would do**, **Turn on format on save** and **Understand the safety gate**.
