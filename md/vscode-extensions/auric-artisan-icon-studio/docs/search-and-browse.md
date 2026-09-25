---
title: Auric Artisan Icon Studio — Search and browse
description: Search 17,234 entries, switch between Library, For you, Likes and Recent, and refine by collection, category, style and skin tone.
product: VS Code extensions › Auric Artisan Icon Studio
updated: 2026-09-25
---

# Search and browse

## Search

1. Select **Search your library**, or press `/` anywhere in Icon Studio.
2. Type a name, tag or concept. The results update as you type.
3. Press `Escape` in the search box to clear it.

Search is synonym-aware and ranks results. For example, `delete` finds trash icons. Hindi search aliases are supported for many entries. The search also takes account of the icons you like and use.

## The four views

The chips at the top switch what the grid shows.

| View | Shows | Empty message |
| --- | --- | --- |
| **Library** | Every entry that matches your search and filters. | "No icons found. Try another word, or choose All collections." |
| **For you** | Up to 96 icons ranked for the file you are editing and your likes and use. Hidden when recommendations are turned off. | "No recommendations yet. Open a file, or like and use a few icons to teach Icon Studio your style." |
| **Likes** | Icons you liked with the heart button. | "No liked icons yet. Press the heart on any card to keep it here." |
| **Recent** | Icons you inserted, copied or saved, newest first (up to 60). | "No recent icons yet. Icons you insert, copy or save appear here." |

Search and filters apply inside every view.

## Refine the results

Expand **Refine library** (subtitle "Collection, category & style").

| Control | Options |
| --- | --- |
| **Collection** | **All collections**, or one collection. Each option shows its group and count, for example "Auric Artisan · Drawn (480)" or "Open source · Tabler (5,093)". |
| **Category** | **All categories**, or a category from the chosen collection. |
| **Style** | Appears when you choose one collection that has more than one style. **Default** uses the collection's default style. |
| **Skin tone** | Appears when **All collections** or **Emoji** is chosen: **Default tone**, **Light**, **Medium-light**, **Medium**, **Medium-dark**, **Dark**. It changes emoji that support tones. |

When you pick a single collection, a credit line under the heading shows the collection name, its licence and its author.

Select **Reset filters** to clear the search, collection, category, style and tone. You stay in the current view (Library, Likes and so on).

Dropdowns support the arrow keys, `Home`, `End`, `Enter`, `Escape` and `Tab`. Scroll a long menu with the mouse wheel.

## Collections and styles

| Collection | Entries | Styles |
| --- | --- | --- |
| Auric Modern | 720 | Color, Mono, Outline, Duotone |
| Auric Drawn | 480 | Color, Mono, Outline, Duotone |
| Auric Playful | 1,225 | Color, Outline, Filled, Small |
| Emoji | 1,914 | Default tone and five skin tones where supported |
| Phosphor | 1,512 | Thin, Light, Regular, Bold, Fill, Duotone |
| Tabler | 5,093 | Outline, Filled |
| Lucide | 1,714 | Regular |
| Remix | 1,689 | Line, Fill |
| Heroicons | 324 | 24 Outline, 24 Solid, 20 Solid, 16 Solid |
| Feather | 287 | Regular |
| Material | 2,276 | Outlined, Round, Sharp, Regular, Two-tone |

Counts are catalog entries, not style variants. Emoji look as your operating system draws them. Material icons are drawn from a bundled font, not SVG.

## Scrolling

The grid loads cards in batches (96 by default; see `auricIconStudio.pageSize`) and adds more as you scroll. A status line reads, for example, "192 of 1,512 loaded — scroll for more", then "All 1,512 loaded". The sidebar and editor tab remember your search, filters and view when you come back.

## Card size

Set `auricIconStudio.density` to `compact` for smaller cards or `comfortable` (default) for larger ones.

## Result

The grid shows exactly the icons you need, in the style you want to preview.
