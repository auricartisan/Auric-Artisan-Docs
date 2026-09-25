---
title: Font Library — Troubleshooting
description: Fixes for common problems in the Font Library, from an empty page to downloads and shortcuts that do not behave.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Troubleshooting

## The page stays empty, or says the library is unavailable

The catalogue and the fonts load from the Font CDN. If it cannot be reached, after a few seconds the grid shows **Font library is temporarily unavailable** or **The live font engine didn’t load**, with the likely causes.

- Check that you are online.
- Turn off extensions that block scripts or requests for this site, and allow requests to fonts.auricartisan.com.
- Select **Retry**, or reload the page, once the connection is back.

## Some cards show a plain font instead of the family

The specimen appears once the family's font file has loaded; slow connections show a stand-in first. Cards marked **Installed** only appear in their own face if that font is installed on your device; see [Limits and accuracy](../others/limits-and-accuracy.md).

## Sorting by Accessibility score or Readability score shows A to Z

At the time of writing these two sort options do not take effect, and the grid stays in alphabetical order. **UI score** works. For accessible families, open **Collections** and use **Best Accessibility Fonts**, or open **Recommend** with **Accessibility priority** set to **Essential**. Each card's badge also shows its accessibility score.

## The Collections view is empty

The collections are hidden while a search, a filter chip, a category or the recommender is active on **Specimens**. Select **Clear all** under **Applied** (or **Reset all filters**) and close the recommender, then open **Collections** again.

## The Size slider stops changing the cards

Card specimens stay between 22 and 48 pixels. Settings outside that range make no further difference. Open a family for larger sizes; its specimen goes up to 400 pixels.

## Searching for a foundry finds nothing

The search covers family names, designers and categories, not foundries. Open a family's **About** tab to see its foundry.

## I cannot filter for my language

The **Scripts** filter offers the 18 most common scripts and blocks. For others, such as Arabic, Devanagari or Thai, search for the script name (many families carry it in their name, such as *Noto Sans Devanagari*), then check the family's **Charset** tab.

## The F and R keys do nothing

At the time of writing, pressing `F` (filters) or `R` (recommender) switches the panel twice, so nothing appears to change. Use the **Filters** and **Recommend** buttons, or press `?` and choose **Toggle filters** or **Find your font** from the command palette. Other shortcuts work normally; see [Shortcuts](../others/shortcuts.md).

## The Selected view shows names in a plain font

The **Selected** view lists names and categories; its sample word may appear in a stand-in font. Open a family, or use **Compare**, to see the families in their own faces.

## The weight chips in Use & Embed do not change the code

They are not connected to the snippets. Every snippet covers the whole family. Edit the code, or download the kit and keep only the files you need.

## Download kit is disabled or says Installed only

That family is listed from installed system fonts and is not served, so it cannot be downloaded or embedded from the CDN. Choose a family from the **Library** source.

## The ZIP is missing a file

If a font file could not be fetched, the ZIP holds `DOWNLOAD_NOTES.txt` naming it. Try again later. Large kits take a while to build; wait for the **Downloaded** message.

## My kit disappeared

The kit is kept in this browser on this device. It does not follow you to another browser or device, and clearing site data or using a private window empties it. Keep embed code or the ZIP for anything you need to keep.

## The panel covers the page on my tablet

On narrower screens the panel is a sheet from the bottom. Drag its grip down or tap the dimmed page to close it, or turn the device to landscape if it is wide enough for the docked layout.

## Related

- [FAQ](faq.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
- [Font CDN troubleshooting](../../../../../services/font-cdn/docs/troubleshooting.md)
