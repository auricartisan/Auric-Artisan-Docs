---
title: Color Library — Troubleshooting
description: Symptoms, causes and fixes for problems in the Color Library.
product: Website › Library › Colour libraries › Color Library
updated: 2026-09-25
---

# Troubleshooting

## "Could not load color atlas"

**Why:** The page downloads the atlas when it opens. The download failed — usually because the network connection dropped, a content blocker stopped it, or the site was opened from an old offline copy.

**What to do:** Check your connection, allow auricartisan.com in any content blocker, and reload the page.

## "Not a colour this reads."

**Why:** The text in **Start from a colour you already have** is not a colour format the page understands.

**What to do:**

- Check brackets and separators: `rgb(118 205 246)` or `rgb(118, 205, 246)`.
- Use one of the supported `color()` spaces: `srgb`, `srgb-linear` or `display-p3`.
- Replace a CSS variable such as `var(--brand)` with its actual value.
- Remove anything after the colour, such as a trailing semicolon or comment.

## My colour shows "outside sRGB"

**Why:** The colour you entered, for example a strong `oklch()` or `display-p3` value, cannot be shown on a standard sRGB screen. The page brings it to the nearest displayable colour before matching.

**What to do:** Nothing is wrong. The matches are for the nearest displayable version of your colour. If you need a colour inside sRGB, use one of the neighbours.

## "No colors match these filters"

**Why:** Your requirement chips, search words and filters together exclude every colour. For example, **Vivid** and **Muted** together always leave nothing, and **Neutral / Gray** with **Vivid** chroma does too.

**What to do:** Select **Reset** to clear the searches and filters, then turn off the highlighted requirement chips one at a time until colours return. The count on each chip shows what turning it off would give you.

## The WCAG filter "AA on white" shows no colours

**Why:** On the current page, this option can return no colours even though thousands of colours reach 4.5:1 on white.

**What to do:** Set **WCAG** back to **Any WCAG** and select the **Readable on white** requirement chip instead. It applies the same 4.5:1 threshold. **AAA on white**, **AA on black** and **AAA on black** work as described.

## CSV (flat) does not download

**Why:** On the current page, the **CSV (flat)** bulk export may produce no file.

**What to do:** Use **JSON (all metadata)** for the full set of fields, or **.txt (one hex per line)** for a plain list, and convert it in your spreadsheet or code.

## The Copy and Save buttons on The colour tab do nothing

**Why:** On the current page these two buttons may not respond.

**What to do:** To copy the colour, open the **Export** tab and use the **Copy formats** buttons under **Selection**. To save it, select the star on its tile in the grid.

## The nearest colours on The colour tab cannot be opened

**Why:** The five cells under **Nearest in the atlas** on **The colour** tab show values only.

**What to do:** Copy the hex code into **Start from a colour you already have**; the cells there open the colour when selected. Or search for the hex code in **Search by hex (#a6e223) or id…**.

## The Stats tab does not reflect my latest filter

**Why:** The histograms are drawn when the tab is opened.

**What to do:** Select the **Stats** tab again to redraw them.

## Searching for an id finds many colours

**Why:** Ids are matched as text, so `12` also matches `120`, `312`, `4812` and so on.

**What to do:** Scroll to the colour whose id you want, or add a second word such as part of its hex code.

## My saved colours have disappeared

**Why:** Saved colours are kept in this browser only. They are lost if you clear this site's data, use a private window, or switch browser or device.

**What to do:** Save them again. To keep a permanent copy, export them: filter the grid down to them and use **Export visible**, or keep them in your Library.

## Copy does not reach the clipboard

**Why:** Some browsers block clipboard access on pages that are not in focus, or when a permission is denied.

**What to do:** Click inside the page and try again. If your browser asks for clipboard permission, allow it.
