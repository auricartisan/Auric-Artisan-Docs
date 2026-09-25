---
title: Auric Icons: Drawn — Reference
description: Every command, keybinding, setting, view, category and library control in Auric Icons: Drawn 0.12.1.
product: VS Code extensions › Auric Icons: Drawn
updated: 2026-09-25
---

# Auric Icons: Drawn reference

This reference describes version 0.12.1 as published on the Visual Studio Marketplace.

## Commands

Category in the Command Palette: **Auric Icons: Drawn**.

| Command | ID | What it does |
| --- | --- | --- |
| Open Icon Library | `auricIconsDrawn.library.openExplorer` | Opens the **Icon Studio — Library** editor tab. |
| Search Icons | `auricIconsDrawn.library.searchIcons` | Choose an icon, then an action. |
| Insert SVG at Cursor | `auricIconsDrawn.library.insertSvg` | Choose an icon and insert it. |
| Smart Insert Icon (matches active language) | `auricIconsDrawn.library.smartInsert` | Choose an icon and insert with language-aware output. |
| Copy Icon As… (JSX, CSS, Markdown, Data URI, Image tag) | `auricIconsDrawn.library.copyAs` | Choose an icon and one of nine formats. |
| Insert from Likes | `auricIconsDrawn.library.showFavorites` | Choose a liked icon and insert. |
| Insert from Recent | `auricIconsDrawn.library.showRecents` | Choose a recent icon and insert. |
| Toggle Like for an Icon | `auricIconsDrawn.library.toggleFavorite` | Like or unlike an icon. |
| Clear Likes, Recents and Learned Recommendations | `auricIconsDrawn.library.resetPersonalization` | Confirm, then reset personalisation. |
| Copy SVG | `auricIconsDrawn.library.copySvg` | Choose an icon and copy raw SVG. |
| Save SVG As… | `auricIconsDrawn.library.saveSvg` | Choose an icon and save it as a file. |
| Open SVG Source | `auricIconsDrawn.library.openSource` | Choose an icon and open its SVG. |

These commands are hidden from the Command Palette while another extension hosts the shared library; from keybindings they forward to the host.

## Keybindings

| Keys (Windows and Linux) | Keys (macOS) | Command | When |
| --- | --- | --- | --- |
| `Ctrl` + `Alt` + `I` | `Cmd` + `Alt` + `I` | Smart Insert Icon | Editor focused and Drawn hosts the library |
| `Ctrl` + `Alt` + `R` | `Cmd` + `Alt` + `R` | Insert from Recent | Editor focused and Drawn hosts the library |

In the view: `/` focuses search, `Escape` clears it or closes a dropdown, arrow keys move between dropdown options.

## Settings

| Setting | Type | Values or range | Default | What it does |
| --- | --- | --- | --- | --- |
| `auricIconsDrawn.library.defaultVariant` | string | `auto`, `color`, `mono`, `outline`, `duotone` | `auto` | Variant for Command Palette actions; `auto` follows the file. |
| `auricIconsDrawn.library.pageSize` | number | 24 to 240 | 72 | Cards streamed per batch. |
| `auricIconsDrawn.library.smartInsert` | boolean | `true`, `false` | `true` | Language-aware output for Insert. |
| `auricIconsDrawn.library.recommendations.enabled` | boolean | `true`, `false` | `true` | Recommendations for the file you are editing. |
| `auricIconsDrawn.library.recommendations.limit` | number | 4 to 24 | 12 | Icons in the recommendation rail. |
| `auricIconsDrawn.library.showGuide` | boolean | `true`, `false` | `true` | Smart guide tips. |
| `auricIconsDrawn.library.density` | string | `comfortable`, `compact` | `comfortable` | Card size. |
| `auricIconsDrawn.library.hoverPreview` | boolean | `true`, `false` | `true` | Hover previews for icon IDs. |

## Views and menus

| Place | Contents |
| --- | --- |
| Activity Bar | **Auric Icons: Drawn** container with the **Icon Library** view (hidden while another extension hosts). |
| View title bar | **Open Icon Library**, **Smart Insert Icon**, **Insert from Likes**; **…** menu: **Clear Likes, Recents and Learned Recommendations**. |
| Editor tab | **Icon Studio — Library**. |

Drawn contributes no file icon theme.

## Library contents

| Item | Value |
| --- | --- |
| Icons | 480 |
| Style | Warm Drawn (shown as **Drawn** in the Style filter) |
| Variants | Color, Mono, Outline, Duotone |
| Categories | 30 |

Categories: Files and document types; Folders and organization; Coding and development; Artificial intelligence; Data and databases; Cloud and hosting; Cybersecurity; Communication; Social interaction; User accounts and profiles; Business and finance; E-commerce; Marketing; Analytics and reporting; Productivity; Project management; Calendar and scheduling; Education and learning; Science and laboratory; Healthcare and wellness; Food and cooking; Travel and transportation; Maps and navigation; Weather and environment; Nature and sustainability; Home and Furniture; Tools and Construction; Art and Design; Photography and Video; Music and Audio.

## Library controls

| Control | Options |
| --- | --- |
| Search | Free text, synonyms, fuzzy ranking. |
| Library | **All libraries** or one collection (only when merged). |
| Category | **All categories** or one of 30. |
| Style | **All styles** or **Drawn**. |
| Variant | **Auto**, **Color**, **Mono**, **Outline**, **Duotone**. |
| Preview surface | **Auto**, **Light**, **Dark**. |
| Chips | **All**, **✦ For you**, **♥ Likes**, **↺ Recent**. |
| Card buttons | Artwork (open source), heart, **Insert**, **Copy**, **Save**, **JSX**, **URI**, **Source**. |

## Limits

| Item | Limit |
| --- | --- |
| Recent icons | 60 |
| Liked icons | 500 |
| Quick Pick results | 200 with a search term; 400 without |
| Smart guide tips | Up to 4 |
