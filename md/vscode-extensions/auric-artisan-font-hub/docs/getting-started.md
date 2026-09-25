---
title: Auric Artisan Font Hub — getting started
description: Install Auric Artisan Font Hub, learn the sidebar and studio layout, and add a first font to a page.
product: VS Code extensions › Auric Artisan Font Hub
updated: 2026-09-25
---

# Getting started with Auric Artisan Font Hub

## Install

1. Check that VS Code is version 1.85 or newer (**Help** › **About**).
2. In the Extensions view (`Ctrl` + `Shift` + `X`), search for `@id:auric-artisan.auric-artisan-font-hub` and select **Install**. Or run:

   ```text
   code --install-extension auric-artisan.auric-artisan-font-hub
   ```

3. If the older **Font Library** extension is installed, disable or uninstall it first. See [Moving from Font Library](moving-from-font-library.md).

Font Hub works in untrusted and virtual workspaces. It only writes files when you choose an explicit save or insert.

## Two ways to open it

- **Sidebar.** Select **Auric Font Hub** in the Activity Bar. The **Font Hub** view is a compact version of the studio.
- **Studio.** Run **Auric Artisan Font Hub: Open Font Hub** (`Ctrl` + `Alt` + `F`), select **Open studio ↗** in the sidebar, or select the **Fonts** item in the status bar. The studio opens as an editor tab with more room.

Both share the same layout, controls, favourites and selection. The sidebar's title bar has **Open Font Hub**, **Focus Font Search** and **Refresh Font Catalog from Auric CDN**.

Opening Font Hub creates no files in your project.

## The screen tour

From top to bottom:

| Area | What it contains |
| --- | --- |
| Header | The Auric Artisan mark; **auricartisan.com ↗**; **Open studio ↗** (in the sidebar); **↻** refresh the catalogue; **↗** open the web library; **⚙** Font Hub settings |
| Introduction | The catalogue status, such as **Offline catalog ready** |
| **Your font delivery** card | The CDN address `fonts.auricartisan.com` and **Check CDN health** |
| **CDN & insertion help** | A collapsible explanation, the last check's status and **Run a live check** |
| Guide | **01 Discover · 02 Compare · 03 Use**, with a hint to try **Preview**. Dismiss it with **×** |
| Controls | **Search**, **Category**, **Sort**, **Preview text**, **Size** (18–96 px) and **More filters** |
| Advanced filters | **Properties**, **Weights**, **OpenType**, **Scripts**, **License**, **Source** and **Reset filters** |
| Scopes | **All**, **For you**, **Favorites**, **Recent**, **Variable**, **Selected** |
| **Find your font** | The recommender: design intent, industry, colour palette, options and **Rank fonts** |
| Density | Compact, comfortable and showcase cards |
| **Collections & recommendations** | Featured collections and recommended families (collapsible) |
| Results | The font cards, with **Show more** to load the next batch |
| Footer | The version, a licence reminder and **CDN diagnostics** |

### A font card

Each card shows the category, a favourite heart and a select button, the family name set in its own font with your preview text, the designer, whether it is variable and how many weights it has, and three scores out of 100: **A11y** (accessibility), **Read** (readability) and **UI** (UI and product). At the bottom are **Add to code** and **Preview**.

Select the family name to open its details. See [Font details](font-details.md).

### The selection tray

When you select families, a **Selected** button appears. It opens the **Selected families** tray with **Copy embed**, **Insert**, **Compare** and **Download**.

## A first task: add a font to an HTML page

1. Open an HTML file that has a `<head>` in the editor.
2. In Font Hub, search for `Inter`.
3. On the Inter card, choose **Preview**.
4. VS Code opens a diff titled **Font Hub: Inter — proposed changes**. The right side adds a stylesheet link and a small class rule inside `<head>`.
5. In the notification **Inter: add CDN setup to *file*? Existing content stays unchanged.**, choose **Apply**.
6. The file now contains the setup and is left unsaved; `Ctrl` + `Z` undoes it.
7. Use the class in your markup:

   ```html
   <p class="auric-font-inter">A considered choice of type.</p>
   ```

8. Save and open the page in a browser. The paragraph uses Inter.

## Keyboard

| Keys | Where | What they do |
| --- | --- | --- |
| `Ctrl` + `Alt` + `F` | VS Code | Open Font Hub |
| `Ctrl` + `Alt` + `T` | VS Code | Quick Pick Font |
| `/` or `Ctrl` + `K` | Font Hub | Focus the search box |
| `Escape` | Font Hub | Close the comparison, details or tray; otherwise clear the search |
| Arrow keys | Font cards | Move between cards |

On macOS, `Cmd` replaces `Ctrl`.

## Next steps

- [Find and compare fonts](find-and-compare-fonts.md)
- [Add a font to your code](add-fonts-to-code.md)
- [Check CDN and browser delivery](cdn-and-browser-delivery.md)
