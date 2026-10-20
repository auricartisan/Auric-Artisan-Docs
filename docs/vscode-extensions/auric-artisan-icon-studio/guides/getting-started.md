---
title: Auric Artisan Icon Studio — Getting started
description: Install Icon Studio, open it in the sidebar or an editor tab, tour the screen and insert your first icon.
product: VS Code extensions › Auric Artisan Icon Studio
updated: 2026-09-25
---

# Getting started with Icon Studio

## Before you begin

- You need Visual Studio Code 1.85 or later.
- Icon Studio works offline and in untrusted and virtual workspaces. Files are only written when you save an icon through a save dialog.
- All collections are bundled. You do not need the individual Auric collection extensions.

## 1. Install

Open the Extensions view (`Ctrl` + `Shift` + `X`), search for **Auric Artisan Icon Studio** and select **Install**, or run:

```text
code --install-extension auric-artisan.auric-artisan-icon-studio
```

## 2. Open Icon Studio

- **Sidebar:** select **Icon Studio** in the Activity Bar. The view is compact and starts with the filters collapsed, leaving room for artwork.
- **Editor tab:** run **Auric Icon Studio: Open Icon Studio**, or select the **↗** button (**Open Icon Studio in an editor tab**) in the sidebar header. The tab opens beside your editor with the filters expanded.

Opening the editor tab again brings the existing tab forward and focuses the search box.

## 3. Tour the screen

| Area | What it contains |
| --- | --- |
| Header | The Auric Artisan mark, "Icon Studio / Creative workspace", an **Offline library** badge and, in the sidebar, the **↗** button. |
| View chips | **Library**, **For you**, **Likes** and **Recent**. Likes and Recent show a count. |
| Introduction | "Small details. Distinct character." |
| Search | **Search your library** with a `/` hint. The placeholder shows the number of entries. |
| Refine library | Collapsible: **Collection**, **Category**, and when relevant **Style** and **Skin tone**. |
| Finder footer | "Choose a card to insert. Copy or As… for more formats." and **Reset filters**. |
| Results | **Explore the collection**, a count such as "Showing 96 of 17,234 icons", and the card grid. |
| Footer | "Local artwork · No account · No telemetry". |

Each card shows the artwork, a heart button, a collection badge, the name, the category, three main buttons (**Insert**, **Copy**, **As…**) and three quick format buttons.

## 4. Insert your first icon

1. Open a writable file, for example a `.tsx` component, and place the cursor where the icon should go.
2. In Icon Studio, press `/` to focus the search and type `rocket`.
3. Select **Insert** on a card, or select the artwork itself.
4. The icon is inserted at every cursor. In a React file it arrives as a JSX element; in CSS as a background; in Markdown as an image.
5. A short status message confirms, for example "Rocket inserted as JSX."

If no editor is open, Icon Studio copies the output instead and tells you: "copied — open an editor to insert it."

## 5. Keep useful icons close

- Select the heart on a card to add it to **Likes**. Select it again to remove it.
- Every icon you insert, copy or save is added to **Recent**.
- **For you** ranks icons for the file you are editing and the icons you like and use.

## Result

You have inserted an icon in the right format for your file, and Icon Studio has started learning which icons you use.

## Next steps

- [Search and browse](search-and-browse.md)
- [Insert, copy and save](insert-copy-and-save.md)
- [Commands and keybindings](commands-and-keybindings.md)
