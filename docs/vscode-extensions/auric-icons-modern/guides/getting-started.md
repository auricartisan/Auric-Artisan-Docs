---
title: Auric Icons: Modern — Getting started
description: Install Auric Icons: Modern, turn on its file icon theme, open the Icon Library and insert your first icon.
product: VS Code extensions › Auric Icons: Modern
updated: 2026-09-25
---

# Getting started with Auric Icons: Modern

## Before you begin

- You need Visual Studio Code 1.85 or later, or an editor that keeps VS Code's extension and icon theme features.
- Everything works offline. The extension has no telemetry and makes no network requests.

## 1. Install

Open the Extensions view (`Ctrl` + `Shift` + `X`), search for **Auric Icons: Modern** and select **Install**, or run:

```text
code --install-extension auric-artisan.auric-artisan-modern-icon
```

## 2. Turn on the file icon theme

1. Open the Command Palette (`Ctrl` + `Shift` + `P`).
2. Run **Preferences: File Icon Theme**.
3. Choose **Auric Icons: Modern**.

Or run **Auric Icons: Modern: Activate Icon Theme**. The Explorer now shows Modern file and folder icons. Folders use the Auric gold by default, and open folders have their own open artwork.

> **Note:** If you also have Auric Artisan File Icons installed, it offers a Modern style under the same theme ID. See [Troubleshooting](troubleshooting.md).

## 3. Personalise the theme

1. Run **Auric Icons: Modern: Configure…**.
2. Choose **Folder colour** and pick a colour, for example **Teal**.
3. VS Code shows "Auric Icons: Modern updated — … Reload to apply?". Select **Reload Window**.

See [Use the file icon theme](file-icon-theme.md) for every option.

## 4. Open the Icon Library

1. Select **Auric Icons: Modern** in the Activity Bar. The **Icon Library** view opens.
2. Or run **Auric Icons: Modern: Open Icon Library** to open the larger **Icon Studio — Library** editor tab.

If Auric Artisan Icon Studio, or another Auric collection that is acting as host, is installed, this view may be hidden. See [The merged Icon Studio](merged-icon-studio.md).

## 5. Insert your first icon

1. Open a file, such as a React component, and place the cursor.
2. In the Icon Library, type `chart` in **Search**.
3. Select **Insert** on a card. With smart insert on (the default), the icon arrives in a format that suits the file, such as a JSX element in React.

Or stay in the editor: press `Ctrl` + `Alt` + `I` (`Cmd` + `Alt` + `I` on macOS), type to search, and choose an icon.

## Result

Your Explorer uses the Modern icon theme in your colour, and you have inserted a Modern icon into your code.

## Next steps

- [Browse the Icon Library](icon-library.md)
- [Insert, copy and save icons](insert-copy-and-save.md)
