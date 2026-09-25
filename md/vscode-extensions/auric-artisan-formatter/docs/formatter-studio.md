---
title: Auric Artisan Formatter — Formatter Studio
description: Use Formatter Studio and the Explorer sidebar to try options on your own code, see the diff and the reasons, and export a configuration.
product: VS Code extensions › Auric Artisan Formatter
updated: 2026-09-25
---

# Formatter Studio

Formatter Studio (the setup walkthrough calls it the Playground) puts your code on one side, the formatted result on the other, and every option that applies in between. Change an option and the result updates as you type. Nothing you do in Studio touches your file until you explicitly apply it.

## Open it

- **Auric Formatter: Open Formatter Studio** — `Ctrl` + `Alt` + `Shift` + `P` (`Cmd` + `Alt` + `Shift` + `P` on macOS). Opens as an editor tab with the active editor's content loaded.
- The **Auric Formatter** section in the Explorer — a compact version of the same tools, with **Open full Studio**.
- **Show Files That Need Formatting** (`Ctrl` + `Alt` + `Shift` + `U`) opens Studio on its **Workspace** tab.

The panel follows your VS Code theme (light, dark and high contrast), respects reduced motion, and remembers its state when you reload.

## The layout

### Top bar

| Control | What it does |
| --- | --- |
| Brand line | The number of options and languages, and the version |
| **auricartisan.com ↗** | Open the Auric Artisan website |
| **Lang** | The language to format the input as; searchable, grouped into **Native printers** and **Universal engine** |
| **Preset** | The preset to start from; searchable, each with a description |
| **Commands** | The Studio command palette (also `Ctrl` + `K`) |
| Layout button | Show or hide the options rail |

### Tabs and actions

| Control | What it does |
| --- | --- |
| **01 Studio** | Try options on your code |
| **02 Workspace** | The workspace scan results, with a count badge. See [Scan the workspace](workspace-scan.md) |
| **Explain** | Explain how this file would be formatted and which layer set each option |
| **Copy config** | Copy the options you changed, with the preset, as `.auricformatrc` content |
| **Yes, apply** | Apply the reviewed preview to its original document, after confirmation |
| **No, discard** | Discard the preview; no file changes |

### Workflow row

| Control | What it does |
| --- | --- |
| **Preview beside editor** | Open the native read-only preview for the source, using the saved project rules. See [Preview formatting as a diff](preview-diff.md) |
| **Formatting scope** | **Full document**, or **Editor selection** (select code in VS Code first; the range may expand to a balanced syntax unit) |
| **Formatting preview** | On: show the formatted result, diff or explanation. Off: show the original |
| **Reload editor** | Load the active editor's content again |
| **Open full Studio** | In the sidebar only: open the full Studio tab |

### Custom rules

**Custom rules · JSON configuration** is a collapsible editor where you type options as a JSON object, for example:

```json
{ "printWidth": 100, "singleQuote": true }
```

- **Validate & preview rules** checks every name and value against the option catalogue (an unknown name is refused with **Unsupported rule**) and previews the result.
- **Load current rules** fills the editor with the options currently set in Studio.

No code runs from the rules editor; it only accepts catalogue options.

## The Studio tab

### Input

Your source code. It opens with the active editor's content; **Paste code here, or open a file and reopen the Playground.** when empty. The pane has **Clear the input** and **Reload from the active editor**.

### Options

The options rail lists every option that applies to the chosen language.

- **Search** the options by name or by what they do.
- **Group** filters by category: Global, Common, JavaScript, TypeScript, CSS, HTML, Markdown, YAML, JSON, GraphQL, Universal, Alignment, Sorting, Comments, Blank Lines, Safety, Experimental.
- Filter chips: **Changed** (only options you moved off the preset), **Affects this file** (after **Find what matters**) and **Experimental** (include options still settling).
- **Find what matters** formats the file once per option and reports the few that actually change *this* file. It can take a moment: **Probing every option against this file…**.
- **Reset every option to the preset default.**
- Each option can be opened in VS Code Settings with **Open this option in Settings**.

### Output

Choose the view:

| View | Shows |
| --- | --- |
| **Result** | The formatted file |
| **Diff** | Only what changes, with added and removed lines counted |
| **Explain** | Which language and parser were chosen, the formatting tier, timing, which configuration layer set each option, changed options and safety warnings |

In **Diff**: **Inline** or **Side by side**, **Show unchanged lines** (or collapse them), **Show more diff lines** for long diffs, and **Previous change** and **Next change**. The output can be copied, and soft wrap toggled from the command palette.

The status line at the bottom shows what Studio is doing, such as **Formatting…** or **Ready**, and warnings such as a safety revert.

## Apply the result to your file

1. Load the file with **Reload editor** (or open Studio from it).
2. Tune the options and review the **Diff**.
3. Choose **Yes, apply**.
4. Confirm **Apply reviewed formatting to *file*?** — **Only this document is edited. Changes remain unsaved and can be undone.**

Apply only works on the document the preview came from, and only if it has not changed since: otherwise **The file changed since this preview. Reload from the editor and review again.** Scratch text you typed yourself, and previews that were truncated, can be copied but not applied.

## Save your configuration

1. Choose **Copy config**. Studio copies JSON with your preset and only the options you changed, not all 391: **Configuration copied — paste it into .auricformatrc.**
2. Create `.auricformatrc` at the root of your project and paste.

See [Configuration](configuration.md) for where the file can live and how it combines with other settings.

## The Studio command palette

Press `Ctrl` + `K` (or select **Commands**) and type:

| Command | What it does |
| --- | --- |
| **Format every file that needs it** | Write every pending file to disk (asks first) |
| **Scan the workspace** | Format every file in memory again |
| **Show the workspace** / **Show the playground** | Switch tabs |
| **Find the options that change this file** | Run **Find what matters** |
| **Explain this file** | Show the explanation |
| **Show the diff** / **Show the result** | Switch the output view |
| **Copy the options as a config file** | Same as **Copy config** |
| **Apply the output to the editor** | Same as **Yes, apply** |
| **Reset every option** | Back to the preset defaults |
| **Toggle the options rail** | Show or hide the rail |
| **Toggle soft wrap** | Wrap long lines in the panes |
| **Open the formatter log** | Show the output channel |
| **Open the formatter settings** | Open VS Code Settings |

## Limits

- Studio previews are limited to 200,000 characters: **Preview is limited to 200,000 characters. Use editor formatting for larger files.** Larger files can still be formatted in the editor, up to `auricFormatter.maxFileSizeKb`.
- Native printers and the universal engine are labelled separately. Supporting a language does not mean every option applies to it.

When you are happy with a result, **Copy config** gives you a configuration that reproduces it for the whole project.
