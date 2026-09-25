---
title: Auric Artisan Formatter — a code formatter for VS Code
description: What Auric Artisan Formatter does, who it is for, how to install it and where to find every guide.
product: VS Code extensions › Auric Artisan Formatter
updated: 2026-09-25
---

# Auric Artisan Formatter

Auric Artisan Formatter formats your code in VS Code. It rebuilds JavaScript, TypeScript, JSON, CSS, HTML, Markdown, YAML and more from a real parse, and tidies the indentation and spacing of hundreds of other languages with a conservative structural engine. Every result passes a *safety gate* before it reaches your file: the output is re-read and compared with the input, and if the formatter cannot prove the change keeps your code's meaning, it keeps your original text.

It is built for adopting a formatter without surprises. **Preview Formatting as a Diff** shows the result beside your source before anything changes. A **workspace scan** formats every file in memory when the window opens and tells you how many would change, without writing anything. **Formatter Studio** lets you try the 391 options against your own code, find the few that matter for a file, and copy only the ones you changed into a configuration file. The same engine runs from a command line for CI checks.

It reads existing Prettier configuration and `.editorconfig`, offers 13 presets (including one byte-compatible with Prettier 3), and has no runtime dependencies.

## Who it is for

- Developers who want consistent formatting with a preview before changes land.
- Teams adopting a formatter on an existing codebase who want to see the impact first and keep `git blame` useful.
- Teams moving from Prettier who want the same output on day one.
- Anyone working in less common languages that other formatters do not cover.

## Where to find it

- Marketplace ID: `auric-artisan.auric-artisan-formatter`
- Marketplace page: https://marketplace.visualstudio.com/items?itemName=auric-artisan.auric-artisan-formatter
- Install from a terminal:

  ```text
  code --install-extension auric-artisan.auric-artisan-formatter
  ```

- Requires VS Code 1.74 or newer. Version 0.1.0 at the time of writing. The interface is in English.

## Quick start

1. Install the extension.
2. Run **Auric Formatter: Toggle Format on Save**. It makes Auric the default formatter and turns on format on save.
3. Open a file and run **Auric Formatter: Preview Formatting as a Diff** (`Ctrl` + `Alt` + `Shift` + `F`). Review the read-only result beside your source.
4. Select **Apply formatting** in the editor title or the CodeLens, or **Discard preview**.
5. Open **Auric Formatter: Open Formatter Studio** (`Ctrl` + `Alt` + `Shift` + `P`) to tune options against your own file, then **Copy config**.
6. Paste the configuration into a `.auricformatrc` file at the root of your project.
7. Before formatting a whole existing repository, check the status bar count from the workspace scan, or run **Auric Formatter: Scan the Workspace Without Writing**.
8. Use **Show Files That Need Formatting** (`Ctrl` + `Alt` + `Shift` + `U`) to review and format files a folder at a time.

## What you can do

- Format a document, a selection or every file that needs it; format on save, or only the lines you changed.
- Preview formatting as a read-only document beside your source, with Apply, Discard, Refresh and Compare.
- Tune 391 options live in Formatter Studio, see the diff and an explanation of each decision, and copy only what you changed.
- Scan the workspace in memory, see which files would change and by how much, and format selected files explicitly.
- Check formatting without writing, reporting into the Problems panel, and run the same check in CI from the command line.
- Start from one of 13 presets, import Prettier settings, generate a configuration file.
- Configure per language and per file pattern, with `.editorconfig` and inline directives.
- See why a file was formatted as it was with **Explain Formatting Decisions**.
- Format 253 languages: 31 natively, the rest with the structural engine.

## In this folder

- [docs/](docs/README.md) — task guides and the full reference.
  - [Getting started](docs/getting-started.md)
  - [Format files and format on save](docs/format-and-format-on-save.md)
  - [Preview formatting as a diff](docs/preview-diff.md)
  - [Formatter Studio](docs/formatter-studio.md)
  - [Scan the workspace](docs/workspace-scan.md)
  - [Configuration](docs/configuration.md)
  - [Presets](docs/presets.md)
  - [The safety gate and formatting tiers](docs/safety-gate-and-tiers.md)
  - [Supported languages](docs/supported-languages.md)
  - [Command line and CI](docs/command-line.md)
  - [Reference: commands, keys and settings](docs/reference.md)
  - [Options reference](docs/options-reference.md)
  - [Troubleshooting](docs/troubleshooting.md)
  - [FAQ](docs/faq.md)
- [others/](others/README.md) — supporting material.
  - [Glossary](others/glossary.md)
  - [Shortcuts](others/shortcuts.md)
  - [Limits and accuracy](others/limits-and-accuracy.md)
  - [Privacy](others/privacy.md)
  - [Related](others/related.md)
  - [Release notes](others/release-notes.md)
