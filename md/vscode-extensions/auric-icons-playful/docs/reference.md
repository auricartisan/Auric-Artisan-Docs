---
title: Auric Icons: Playful — Reference
description: Every command, keybinding, setting, view, category and library control in Auric Icons: Playful 0.12.1.
product: VS Code extensions › Auric Icons: Playful
updated: 2026-09-25
---

# Auric Icons: Playful reference

This reference describes version 0.12.1 as published on the Visual Studio Marketplace.

## Commands

Category in the Command Palette: **Auric Icons: Playful**.

| Command | ID | What it does |
| --- | --- | --- |
| Open Icon Library | `auricIconsPlayful.library.openExplorer` | Opens the **Icon Studio — Library** editor tab. |
| Search Icons | `auricIconsPlayful.library.searchIcons` | Choose an icon, then an action. |
| Insert SVG at Cursor | `auricIconsPlayful.library.insertSvg` | Choose an icon and insert it. |
| Smart Insert Icon (matches active language) | `auricIconsPlayful.library.smartInsert` | Choose an icon and insert with language-aware output. |
| Copy Icon As… (JSX, CSS, Markdown, Data URI, Image tag) | `auricIconsPlayful.library.copyAs` | Choose an icon and one of nine formats. |
| Insert from Likes | `auricIconsPlayful.library.showFavorites` | Choose a liked icon and insert. |
| Insert from Recent | `auricIconsPlayful.library.showRecents` | Choose a recent icon and insert. |
| Toggle Like for an Icon | `auricIconsPlayful.library.toggleFavorite` | Like or unlike an icon. |
| Clear Likes, Recents and Learned Recommendations | `auricIconsPlayful.library.resetPersonalization` | Confirm, then reset personalisation. |
| Copy SVG | `auricIconsPlayful.library.copySvg` | Choose an icon and copy raw SVG. |
| Save SVG As… | `auricIconsPlayful.library.saveSvg` | Choose an icon and save it as a file. |
| Open SVG Source | `auricIconsPlayful.library.openSource` | Choose an icon and open its SVG. |

These commands are hidden from the Command Palette while another extension hosts the shared library; from keybindings they forward to the host.

## Keybindings

| Keys (Windows and Linux) | Keys (macOS) | Command | When |
| --- | --- | --- | --- |
| `Ctrl` + `Alt` + `I` | `Cmd` + `Alt` + `I` | Smart Insert Icon | Editor focused and Playful hosts the library |
| `Ctrl` + `Alt` + `R` | `Cmd` + `Alt` + `R` | Insert from Recent | Editor focused and Playful hosts the library |

In the view: `/` focuses search, `Escape` clears it or closes a dropdown, arrow keys move between dropdown options.

## Settings

| Setting | Type | Values or range | Default | What it does |
| --- | --- | --- | --- | --- |
| `auricIconsPlayful.library.defaultVariant` | string | `auto`, `color`, `outline`, `filled`, `small` | `auto` | Variant for Command Palette actions; `auto` follows the file. |
| `auricIconsPlayful.library.pageSize` | number | 24 to 240 | 72 | Cards streamed per batch. |
| `auricIconsPlayful.library.smartInsert` | boolean | `true`, `false` | `true` | Language-aware output for Insert. |
| `auricIconsPlayful.library.recommendations.enabled` | boolean | `true`, `false` | `true` | Recommendations for the file you are editing. |
| `auricIconsPlayful.library.recommendations.limit` | number | 4 to 24 | 12 | Icons in the recommendation rail. |
| `auricIconsPlayful.library.showGuide` | boolean | `true`, `false` | `true` | Smart guide tips. |
| `auricIconsPlayful.library.density` | string | `comfortable`, `compact` | `comfortable` | Card size. |
| `auricIconsPlayful.library.hoverPreview` | boolean | `true`, `false` | `true` | Hover previews for icon IDs. |

## Views and menus

| Place | Contents |
| --- | --- |
| Activity Bar | **Auric Icons: Playful** container with the **Icon Library** view (hidden while another extension hosts). |
| View title bar | **Open Icon Library**, **Smart Insert Icon**, **Insert from Likes**; **…** menu: **Clear Likes, Recents and Learned Recommendations**. |
| Editor tab | **Icon Studio — Library**. |

Playful contributes no file icon theme.

## Library contents

| Item | Value |
| --- | --- |
| Icons | 1,225 |
| Variants | Color, Outline, Filled, Small |
| Categories | 24 |

Categories: Lifestyle; Accessibility; Accounts; Actions; Admin Panel; Artificial Intelligence; Blog and Publishing; Business; Calendar and Time; Communication; Dashboard; Developer and Technology; Devices and Hardware; Navigation; E-commerce; Files; Folders; Form Elements; Location and Travel; Media; Reactions; Security and Privacy; Settings; Status.

## Library controls

| Control | Options |
| --- | --- |
| Search | Free text, synonyms, fuzzy ranking. |
| Library | **All libraries** or one collection (only when merged). |
| Category | **All categories** or one of 24. |
| Style | **All styles** or **Playful**. |
| Variant | **Auto**, **Color**, **Outline**, **Filled**, **Small**. |
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
