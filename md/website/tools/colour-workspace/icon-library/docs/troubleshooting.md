---
title: Icon Library — Troubleshooting
description: Fixes for common problems in the Icon Library, from an empty page to filters and exports that do not behave as expected.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Troubleshooting

## The page stays empty, or says the library is unavailable

The catalogue and the icons load from the Icon CDN. If it cannot be reached, after a few seconds the grid shows **Icon library is temporarily unavailable** or **The live icon engine didn’t load**, with the likely causes.

- Check that you are online.
- Turn off extensions that block scripts or requests for this site, and allow requests to icons.auricartisan.com.
- Select **Retry**, or reload the page, once the connection is back.

## Some tiles show a plain rounded square

That square stands in for an icon whose drawing could not be loaded. Scroll away and back, or reload the page. If it persists for a particular set and style, try another style.

## The Category filter says No categories for this set

Only Tabler and Remix icons have categories. Choose **All**, **Tabler** or **Remix**, or search by name instead.

## A keyword search finds only Tabler and Remix icons

Only those two sets carry keywords. For the other sets, search by the words in the icon's name, such as *bell*, *arrow* or *user*.

## Moving Stroke changes nothing

Stroke affects outline icons only: Tabler (Outline), Lucide, Feather and outline Heroicons. Filled sets such as Phosphor, Remix and Material have no stroke to change.

## The Featured collections are missing from the Sets view

They are hidden while a search, a set other than **All**, a filter or **Find your icon** is active. Select **Clear all** under **Applied**, close **Find your icon**, and open **Sets** again. The seven set cards are always shown.

## Removing a licence filter with × turns on a different licence

At the time of writing, the **×** on a licence chip under **Applied** can switch the wrong licence when more than one is listed. Select the chip itself in the **License** group instead, or use **Clear all**.

## Find your icon shows high match numbers for poor matches

The match figure only shows each result's place in the list, not how well it fits. Refine the **Brief**, or pick a **Set** or **Category**.

## The ZIP icons are not the size or colour I previewed

The ZIP holds the icons as they come from their sets. They use `currentColor`, so set the colour and size with CSS where you use them, or download single restyled icons with **Download .svg** in the icon panel.

## The header Download .svg ignores my colour

The **Download .svg** button at the top of the panel saves the icon in the grid's style as it comes from the set. Use **Download .svg** among the copy buttons for a file with your colour and stroke.

## A Material icon will not download as SVG

Material icons are served as a webfont. Use **Copy CDN tag** or the **Webfont @font-face** code, or choose a similar icon from another set.

## My kit disappeared

The kit is kept in this browser on this device. It does not follow you to another browser or device, and clearing site data or using a private window empties it.

## Related

- [FAQ](faq.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
- [Icon CDN troubleshooting](../../../../../services/icon-cdn/docs/troubleshooting.md)
