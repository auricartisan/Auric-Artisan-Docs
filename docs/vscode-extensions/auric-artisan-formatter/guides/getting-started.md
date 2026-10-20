---
title: Auric Artisan Formatter — getting started
description: Install Auric Artisan Formatter, make it your formatter, learn where its controls are, and preview a first format.
product: VS Code extensions › Auric Artisan Formatter
updated: 2026-09-25
---

# Getting started with Auric Artisan Formatter

## Install

1. Check that VS Code is version 1.74 or newer (**Help** › **About**).
2. In the Extensions view (`Ctrl` + `Shift` + `X`), search for `@id:auric-artisan.auric-artisan-formatter` and select **Install**. Or run:

   ```text
   code --install-extension auric-artisan.auric-artisan-formatter
   ```

The extension starts when VS Code opens and offers formatting for every language it supports.

## Make it your formatter

VS Code uses one formatter per language. If you have several installed, it asks which to use every time. Tell it to use Auric:

- Run **Auric Formatter: Toggle Format on Save**. It sets `editor.defaultFormatter` to `auric-artisan.auric-artisan-formatter` and turns on `editor.formatOnSave`, in the workspace settings when a folder is open (otherwise in user settings). Run it again to turn format on save off.
- Or add the settings yourself:

  ```json
  {
    "editor.defaultFormatter": "auric-artisan.auric-artisan-formatter",
    "editor.formatOnSave": true
  }
  ```

To use it only for some languages, scope the settings:

```json
{
  "[typescript]": {
    "editor.defaultFormatter": "auric-artisan.auric-artisan-formatter",
    "editor.formatOnSave": true
  }
}
```

## The setup walkthrough

VS Code's **Welcome** page (**Help** › **Welcome**) includes **Set up Auric Artisan Formatter**, five steps with buttons:

1. **Choose a preset** — **Switch preset**.
2. **Try the Playground** — **Open Playground** (Formatter Studio).
3. **See what the whole repository would do** — **Show what needs formatting**.
4. **Turn on format on save** — **Toggle format on save**.
5. **Understand the safety gate** — **Explain this file**.

## The screen tour

### Status bar

Two items on the right:

| Item | Meaning | Select it to |
| --- | --- | --- |
| **Auric** with a tick | The last format ran; the tooltip names the tier (native or universal) and the time taken, or says the file was already formatted | Open the log |
| **Auric** with a shield, warning background | The safety gate reverted a change; your original text was kept | Open the log |
| **Auric** with a slash | The file was skipped (for example, it looks minified) | Open the log |
| **Auric** with an error, error background | Formatting failed | Open the log |
| ***N* unformatted**, warning background | The workspace scan found *N* files that would change; nothing has been written | Review them in Formatter Studio |
| **Auric** with a double tick | Every scanned file is already formatted | Open the list |
| **Auric *scanned*/*total***, spinning | The scan is running in memory | — |

The first item appears for languages Auric supports. Hide it with `auricFormatter.showStatusBar`.

### Formatter Studio and the Explorer sidebar

- **Auric Formatter: Open Formatter Studio** (`Ctrl` + `Alt` + `Shift` + `P`) opens the full studio as an editor tab.
- The **Auric Formatter** section in the Explorer is a compact version, with **Open full Studio**.

Both have two tabs: **01 Studio** (try options on your code) and **02 Workspace** (the scan results). See [Formatter Studio](formatter-studio.md).

### Editor menus

- **Editor title bar:** **Preview Formatting as a Diff** for supported files. While a preview is open: **Apply Formatting Preview**, **Compare Formatting Changes**, **Refresh Formatting Preview** and **Discard Formatting Preview**.
- **Editor context menu:** **Format Selection** when text is selected, otherwise **Preview Formatting as a Diff**.
- **Explorer context menu on a folder:** **Format Every File in the Workspace**.

## A first format with a preview

1. Open a JavaScript, TypeScript, CSS or JSON file.
2. Press `Ctrl` + `Alt` + `Shift` + `F` (**Preview Formatting as a Diff**).
3. A read-only tab, **Preview — *file name***, opens beside your source with the formatted result.
4. Use the CodeLens at the top: **Apply formatting**, **Compare changes**, **Discard preview** or **Full file · refresh preview**.
5. Choose **Apply formatting**, then confirm. Your source is updated and left unsaved; `Ctrl` + `Z` undoes it.

You now have a formatted file and have seen exactly what changed before it happened.

## Next steps

- [Format files and format on save](format-and-format-on-save.md)
- [Formatter Studio](formatter-studio.md)
- [Scan the workspace](workspace-scan.md)
- [Configuration](configuration.md)
