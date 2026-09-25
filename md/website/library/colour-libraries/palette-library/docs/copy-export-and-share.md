---
title: Palette Library — Copy, export and share
description: Copy a palette as hex, CSS, SCSS or Tailwind, download it as JSON, ASE, SVG or PNG, export design tokens, share a link, and download many palettes at once.
product: Website › Library › Colour libraries › Palette Library
updated: 2026-09-25
---

# Copy, export and share

## Quick copies from the grid

- Select one swatch to copy that colour's hex code.
- Select **Copy** on a card to copy all five hex codes separated by commas, for example `#28ACE4, #715ED2, #F84461, #6F30E7, #BBC8BA`.

## Export one palette

Open the palette on the **Inspect** tab (see [Inspect a palette](inspect-a-palette.md)). You can then use either the **Quick export** row on **Inspect**, or the **Selection** card on the **Export** tab. They produce the same results.

If no palette is open, the **Export** tab says **No palette selected. Click Inspect on any card in the Library tab to enable selection exports.**

### Copy formats

The examples use palette `pal_0`. Variable names are built from the palette id and the colour's position, 1 to 5.

| Quick export | Export tab | What is copied |
| --- | --- | --- |
| **Copy HEX** | **HEX list** | The five hex codes, one per line. |
| **Copy CSS vars** | **CSS variables** | A `:root` block with one custom property per colour. |
| **Copy SCSS** | **SCSS variables** | Five Sass variables. |
| **Copy Tailwind** | **Tailwind config** | A colour object you can paste into `theme.extend.colors`. |

```css
:root {
  --pal_0-1: #28ACE4;
  --pal_0-2: #715ED2;
  --pal_0-3: #F84461;
  --pal_0-4: #6F30E7;
  --pal_0-5: #BBC8BA;
}
```

```text
$pal_0-1: #28ACE4;
$pal_0-2: #715ED2;
$pal_0-3: #F84461;
$pal_0-4: #6F30E7;
$pal_0-5: #BBC8BA;
```

```json
{
  "pal_0": {
    "c1": "#28ACE4",
    "c2": "#715ED2",
    "c3": "#F84461",
    "c4": "#6F30E7",
    "c5": "#BBC8BA"
  }
}
```

These are the real colours of `pal_0`, which is labelled `complementary`.

### Downloads

| Quick export | Export tab | File | Contents |
| --- | --- | --- | --- |
| **Download JSON** | **JSON** | `pal_0.json` | The id, each colour's hex, RGB, OKLCH and Lab, and the metadata: method, colour count, average ΔE, entropy and the full 5 × 5 contrast table. |
| **Download ASE** | **Adobe ASE** | `pal_0.ase` | An Adobe Swatch Exchange file with five RGB swatches named `pal_0_1` to `pal_0_5`. Opens in Adobe Illustrator, Photoshop, InDesign and other apps that read ASE. |
| **Download SVG** | **SVG strip** | `pal_0.svg` | A 600 × 220 strip of the five colours, each labelled with its hex code. |
| **Download PNG** | **PNG strip** | `pal_0.png` | An 800 × 320 image of the same strip. |

The page confirms each download with **Downloaded** and the file name.

### Open in Coolors

**Open in Coolors** (on **Inspect**, and under **External** on the **Export** tab) opens the palette on coolors.co in a new tab, with the five colours already loaded. Coolors is a separate website; what you do there is governed by its own terms.

## Export design tokens

Design tokens are named colour values in a format a design system or app platform understands.

1. On **Inspect**, select **Design tokens…**. A dialog opens, titled with the palette id.
2. In **Token prefix**, type the name your tokens should start with. The default is `brand`.
3. Select a format tab. The preview shows the file, with a line above it giving the number of tokens, the file name and the file's length, for example **5 tokens · tokens.css** and a character count.
4. Select **Copy** to copy the preview, **Download** to save that format, or **Download all** to save every format in one ZIP file.

| Format tab | File name |
| --- | --- |
| **W3C Design Tokens** | `tokens.json` |
| **CSS Variables** | `tokens.css` |
| **SCSS** | `tokens.scss` |
| **Tailwind Config** | `tailwind.config.js` |
| **Style Dictionary** | `style-dictionary.tokens.json` |
| **Material UI Theme** | `theme.ts` |
| **iOS (SwiftUI)** | `Colors.swift` |
| **Android colors.xml** | `colors.xml` |

**Download all** names the ZIP after the palette, for example `palette-pal-0.zip`. Close the dialog with ✕ or by selecting outside it.

## Share a link

1. On **Inspect**, select **Copy share link**. The **Share link** dialog opens, titled with the palette id.
2. The dialog explains: "Anyone with this link can open a copy. State is encoded in the URL — no account needed."
3. Select **Copy** (it changes to **Copied!**), **Share via…** (on devices that offer a system share sheet), or **Open in new tab**.
4. Select **Close** when you are done.

Anyone who opens the link lands on the Palette Library with the palette open on **Inspect**. The link carries the palette's id and colours; nothing is stored on a server. If the palette cannot be found, the page says **Shared palette not found in current dataset**.

## Export many palettes

The **Export** tab's second card is headed **Visible page** and carries a badge with a number of palettes. It exports the same sample the analysis tabs measure (see [Analyse the collection](analyse-the-collection.md)): with no filter, the first 2,000 palettes of the collection; with a filter, up to 2,000 matching palettes from the first 40,000 looked at.

| Group | Button | Contents |
| --- | --- | --- |
| **Bulk download** | **Download JSON (visible page)** | Every palette in full, with export time, source and count. |
| | **Download CSV (visible page)** | One row per palette: `palette_id,method,c1,c2,c3,c4,c5`. |
| | **Download CSS variables** | One `:root` block with five variables per palette. |
| | **Download SCSS variables** | Five Sass variables per palette. |
| | **Download compact JSON** | The count and each palette's id and five hex codes. |
| **Sample formats** | **Download .txt hex list** | Every hex code, one per line. |
| | **Download tailwind.config.js fragment** | A Tailwind configuration with one colour group per palette. |

Files are named `palette-page-` plus the number of palettes and the date, for example `palette-page-2000-2026-09-24.csv`. If the sample is empty, the page says **Nothing to export**.

> **Note:** "Visible page" means the measured sample, not only the cards on your screen. To export exactly one palette, use the **Selection** card instead.

## Result

The palette is on your clipboard, in a file your design tool or code can read, in a design-token format for your platform, or in a link someone else can open.
