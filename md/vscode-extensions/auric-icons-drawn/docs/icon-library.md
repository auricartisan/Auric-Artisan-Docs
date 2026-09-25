---
title: Auric Icons: Drawn — Browse the Icon Library
description: Search the 480 Warm Drawn icons, filter by category, switch variants and preview surfaces, and use the smart guide and recommendations.
product: VS Code extensions › Auric Icons: Drawn
updated: 2026-09-25
---

# Browse the Icon Library

The Drawn library holds 480 hand-drawn icons in 30 categories. Each icon is available in **Color**, **Mono**, **Outline** and **Duotone**.

## Open the library

- **Sidebar:** select **Auric Icons: Drawn** in the Activity Bar.
- **Editor tab:** run **Auric Icons: Drawn: Open Icon Library**, select the **↗** button (**Open full explorer**), or the open-preview icon in the view's title bar. The tab is called **Icon Studio — Library**.

## The screen

| Area | What it does |
| --- | --- |
| Header | "Icon Studio", **Icon Library**, a count line such as "480 icons · 72 loaded", and **↗**. |
| Smart guide | Up to four dismissible tips, such as "Markdown detected" or "Like icons you reuse". Turn off with `auricIconsDrawn.library.showGuide`. |
| Search | Placeholder "Search 480 icons — try “empty state” or “auth”". |
| Library | Only shown when several collections are merged. |
| Category | **All categories** or one of 30. |
| Style | **All styles** or **Drawn** (plus other collections' styles when merged). |
| Variant | **Auto**, **Color**, **Mono**, **Outline**, **Duotone**. |
| Preview surface | **Auto**, **Light**, **Dark**. |
| Chips | **All**, **✦ For you**, **♥ Likes** (count), **↺ Recent** (count). |
| Recommended rail | **✦ Recommended for this file**, with **Refresh**. |
| Grid | Cards that load as you scroll. |

## Search

Search by concept, description, tag or synonym; results are ranked as you type and personalised by what you like and use. For example, `delete` finds trash icons. Press `/` to focus search and `Escape` to clear it.

## Variants and Auto

**Auto** follows the file you are editing and shows the resolved variant, for example "Auto · mono".

| Editing in | Auto variant |
| --- | --- |
| JavaScript, TypeScript, React JSX and TSX | Outline |
| HTML, PHP, Handlebars, Vue, Svelte, Astro, Markdown, MDX, XML, SVG | Color |
| CSS, SCSS, Less, JSON, YAML, Python | Mono |
| Anything else | Color |

Command Palette actions use `auricIconsDrawn.library.defaultVariant` (`auto`, `color`, `mono`, `outline`, `duotone`).

## Preview surface

**Light** and **Dark** place every card on a light or dark backdrop; **Auto** follows your VS Code theme. The choice is remembered.

## The views

| Chip | Shows |
| --- | --- |
| **All** | Every icon that matches the search and filters. |
| **✦ For you** | Icons recommended for the file you are editing and your likes and use. |
| **♥ Likes** | Liked icons. |
| **↺ Recent** | Icons you inserted, copied, saved or opened, newest first (up to 60). |

## Recommendations

The **✦ Recommended for this file** rail shows icons that match the file you are editing or your habits, each with a reason: **Matches this file**, **In your likes**, **Used recently**, **Fits your style** or **Popular in your catalog**. Selecting a rail card inserts it; **Refresh** recomputes the rail.

| Setting | Default | Effect |
| --- | --- | --- |
| `auricIconsDrawn.library.recommendations.enabled` | true | Show recommendations. |
| `auricIconsDrawn.library.recommendations.limit` | 12 | Icons in the rail (4 to 24). |

## Cards

| Control | Action |
| --- | --- |
| Artwork | Opens the SVG source in an editor tab. |
| Heart | Adds to or removes from **Likes**. |
| **Insert** | Inserts into the editor. |
| **Copy** | Copies raw SVG. |
| **Save** | Saves an `.svg` file through a dialog. |
| **JSX** | Copies a JSX element. |
| **URI** | Copies a data URI. |
| **Source** | Opens the SVG source. |

## Density and batch size

| Setting | Values | Default |
| --- | --- | --- |
| `auricIconsDrawn.library.density` | `comfortable`, `compact` | `comfortable` |
| `auricIconsDrawn.library.pageSize` | 24 to 240 | 72 |

## Result

You can find any Drawn icon quickly, preview it in the right variant and background, and act on it from its card.
