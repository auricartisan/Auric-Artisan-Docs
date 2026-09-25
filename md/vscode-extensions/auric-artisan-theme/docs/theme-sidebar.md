---
title: Auric Artisan Theme — The Theme sidebar
description: Every part of the Auric Theme view in the Activity Bar, from the variant galleries to the contrast status and title-bar actions.
product: VS Code extensions › Auric Artisan Theme
updated: 2026-09-25
---

# The Theme sidebar

The extension adds an **Auric Theme** icon to the Activity Bar. It opens a compact view called **Theme** that covers the most common tasks without opening Theme Studio.

## Open the sidebar

Select the **Auric Theme** icon in the Activity Bar. If you do not see it, right-click the Activity Bar and make sure **Auric Theme** is ticked.

## Sections, top to bottom

| Section | What it does |
| --- | --- |
| Header | Shows the active theme name and a summary such as "3 dials changed · 1 slot override", or **Shipped defaults**. |
| Language | **Auto**, **EN** and **हिं** buttons switch the language of the sidebar and Theme Studio. |
| Active theme card | Shows the current theme with an **Open Theme Studio** button. |
| Metrics | **Built-in variants** and **Your changes**. |
| Variant | A searchable dropdown of all variants, and **Browse all swatches** for the family galleries. |
| Accent | Swatches for the named accents, plus **Custom** with a colour picker for any hex colour. |
| Look | A dropdown of the 11 looks. |
| Contrast | The worst pair, a **Pass** or **Fail** chip and its ratio. Select it to open the Audit tab. |
| Actions | **Reset** and **Export**, and a link to auricartisan.com. |

### Variant galleries

Expand **Browse all swatches** to see one collapsible group per family: Obsidian, Midnight, Parchment, Porcelain, Dusk, Forest and High contrast. Each group shows its variant count and a tile per accent. Each tile has a small colour strip showing the canvas, surface, accent, strings and keywords. The active variant has a tick.

- Select a tile to switch theme.
- Use the arrow keys to move between tiles in a group.
- The sidebar remembers which groups you expanded.

### Custom accent

Under **Accent**, open **Custom** and choose a colour in the picker. The theme switches the accent to **Custom** and uses your colour. Clearing the colour returns the accent to **Inherit**.

### Reset

Select **Reset** once: the button changes to **Reset everything?**. Select it again within four seconds to clear every dial and colour override and return to the shipped theme. If you wait, the button returns to normal.

### Export

The **Export** button prepares your customisation JSON. When Theme Studio is open, the JSON appears in the Share tab's Export box. To write a theme file, use **Export as Theme File…** in the title-bar **…** menu instead (see below).

## Title-bar actions

The view's title bar has two icons and a **…** menu.

| Location | Action |
| --- | --- |
| Icon | **Open Theme Studio** |
| Icon | **Show Contrast Report** |
| … menu | **Surprise Me**, **Save Current as Preset…**, **Load Preset…** |
| … menu | **Export as Theme File…**, **Copy Customisation to Clipboard**, **Apply Customisation from Clipboard** |
| … menu | **Reset Everything** (asks for confirmation in a dialog) |

## Result

You can switch variant, accent and look, check contrast and reach every sharing action from the sidebar, and open Theme Studio when you need the full controls.
