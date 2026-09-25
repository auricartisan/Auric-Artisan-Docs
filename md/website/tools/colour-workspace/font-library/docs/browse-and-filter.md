---
title: Font Library — Browse, search and filter
description: Preview your own text, set the specimen size, search, sort, pick a category, narrow with filter chips, and switch between grid and list.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Browse, search and filter

Everything here happens on the **Specimens** view. The grid shows 48 families at first and loads more as you scroll.

## Preview your own text

Type in *Type to preview every family…* above the grid. Every card shows your text in its own face. Clear the box to go back to each family's name.

Your text also starts the specimen in the family panel and appears in the **Styles** tab and in **Compare**.

## Specimen size

The **Size** row sets how large the card specimens are. Drag the slider, use **−** and **+** (2 pixels a step), or select **Reset to 40**. The slider snaps near 16, 24, 48, 72 and 96.

Cards keep their specimens between 22 and 48 pixels, so settings below 22 or above 48 make no further difference to the grid. For a bigger view, open the family: the specimen editor goes up to 400 pixels.

## Grid or list

**Grid** shows cards in columns; **List** shows one family per row, which suits long preview text.

## Search

Type in *Family, designer or foundry*. Results update as you type. The search looks for what you type anywhere in the family name, the designer's name or the category (for example *mono* or *serif*), ignoring capitals. Foundry names are not searched, despite the placeholder.

## Sort

| Option | Order |
| --- | --- |
| **Alphabetical** | A to Z (default) |
| **Accessibility score** | Intended to put the highest accessibility score first; see [Troubleshooting](troubleshooting.md) |
| **UI score** | Highest UI score first |
| **Readability score** | Intended to put the highest readability score first; see [Troubleshooting](troubleshooting.md) |
| **Most weights** | Families with the most weights first |
| **Most glyphs** | Families with the most characters first |
| **Variable first** | Variable fonts first, then A to Z |
| **Surprise me** | Random order |

**Shuffle**, beside the preview box, switches the sort to **Surprise me** and deals a new random order each time.

## Category

The **Category** chips pick one category at a time: **All** (2,213), **Serif** (1,172), **Sans Serif** (780), **Handwriting** (97), **Monospace** (83) or **Display** (81). Categories are detected automatically from the font files; see [Limits and accuracy](../others/limits-and-accuracy.md).

## Narrow it: the filter chips

**Filters** shows or hides the chip groups. Select a chip to turn it on; select it again to turn it off.

| Group | Chips | How several chips combine |
| --- | --- | --- |
| **Properties** | **⚡ Variable**, **𝘐 Italic**, **⌗ Monospace** | A family must match all |
| **Weights available** | 100 to 900 (hover for the name, such as SemiBold) | A family must have every weight chosen |
| **Features** | Ligatures, Small Caps, Oldstyle Figures, Tabular Figures, Fractions, Slashed Zero, Stylistic Sets, Swashes | A family must have every feature chosen |
| **Scripts** | The 18 most common scripts and Unicode blocks, such as Basic Latin, Cyrillic or Greek | A family must cover every one chosen |
| **Licence** | Open Font License, Unspecified, Apache 2.0, Creative Commons, MIT, Custom, with counts | Any of those chosen |
| **Source** | **Library** (served fonts) and **System** (listed, not served) | Either |

Tips:

- **Filter these options** at the top of the chip groups finds a chip by name across all groups, for example *tabular* or *Cyrillic*. It shows **No option matches that.** if nothing fits.
- Groups with more than ten chips show **+ n More**; select it to see the rest, and **Less** to fold them again.
- Select a group's heading to fold it; a number on the heading says how many of its chips are on. The page remembers which groups you folded.
- Chips can be reached with `Tab` and switched with `Enter` or `Space`.

## See and clear what is applied

When anything is switched on, **Applied** appears under the search box with a chip for each filter, the search and the category. Select **×** on a chip to remove just that one, or **Clear all** to remove everything.

**Reset all filters** at the foot of the rail also clears every chip, the category and the search.

The number of matching families appears beside the search tools and on the **Specimens** view button. If nothing matches, the grid reads **No fonts match these filters.**

## Related

- [Collections and the recommender](collections-and-recommender.md)
- [The specimen panel](specimen-panel.md)
- [Shortcuts](../others/shortcuts.md)
