---
title: Auric Artisan File Icons — Getting started
description: Install File Icons, open File Icon Studio, tour its three tabs and activate a style in the Explorer.
product: VS Code extensions › Auric Artisan File Icons
updated: 2026-09-25
---

# Getting started with Auric Artisan File Icons

## Before you begin

- You need Visual Studio Code 1.85 or later. No other icon extension is needed.
- No account is needed. The extension does not contact a server and never runs code from your workspace.

## 1. Install

Open the Extensions view (`Ctrl` + `Shift` + `X`), search for **Auric Artisan File Icons** and select **Install**, or run:

```text
code --install-extension auric-artisan.auric-artisan-file-icon
```

For an official downloaded `.vsix` file, run **Extensions: Install from VSIX…** and choose the file.

## 2. Open File Icon Studio

- **Sidebar:** select **Auric File Icons** in the Activity Bar. The view is called **File Icon Studio**.
- **Editor tab:** run **Auric Artisan File Icons: Open File Icon Studio**, or select the **↗** button (**Open in editor tab**) in the sidebar.

Both have the same tools; the sidebar is compact.

## 3. Tour the Studio

| Area | Contents |
| --- | --- |
| Header | "Auric Artisan / File Icon Studio", an **auricartisan.com ↗** link, **↗** (sidebar only) and **⚙** (**All extension settings**). |
| Tabs | **Library**, **Appearance**, **Workspace**. |
| Target line | "Insert target · {file}" when a writable editor is open, otherwise "No editor target · open a writable file before inserting. Copy is always available." |

### Library

"Your files, with character." A search box, the **Artwork style**, **Show** and **Code format** pickers, an **Open folder artwork** check box, the **Use … in Explorer** button, a count badge and the icon grid.

### Appearance

"One palette. Three styles." The **Modern framework pack** picker and a form with **File color**, **Folder color**, **Saturation**, **Brightness**, **Opacity**, **Hide Explorer arrows**, **Apply appearance** and **Restore defaults…**.

### Workspace

"Connected to your project." Four panels: **Smart Explorer matches**, **Profiles**, **Insert from a code hover** and **Import existing file settings**.

The footer reads "Local artwork · no account · no telemetry" and shows which Auric Explorer style is active.

## 4. Activate a style

1. On **Library**, open **Artwork style** and choose **Facet**, **Playful** or **Modern**. Browsing a style only previews its artwork.
2. Select **Use Facet in Explorer** (the label follows your choice).
3. Your Explorer changes to that theme.

You can also run **Preferences: File Icon Theme** and choose **Auric Artisan File Icons: Facet**, **Auric Artisan File Icons: Playful** or **Auric Artisan File Icons: Modern**.

## 5. Try a colour

1. Open **Appearance**.
2. Set **Folder color** with the swatch or type a hex value such as `#D8A33C`.
3. Select **Apply appearance**. If VS Code asks, select **Reload**.

## Result

Your Explorer uses an Auric style in your colours. Next, see [Assign icons to files and folders](assign-icons.md) and [Insert icons into code](insert-icons-into-code.md).
