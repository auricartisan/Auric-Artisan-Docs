---
title: Gradient Library — Copy, export and share
description: Copy a gradient's CSS, download it as a CSS class, JSON, SVG, PNG or Tailwind token, export design tokens, share a link, and export whole filtered sets.
product: Website › Library › Colour libraries › Gradient Library
updated: 2026-09-25
---

# Copy, export and share

## One gradient

You can export the open gradient from three places: the **Inspect** tab, its **Quick Export** card, and the **Active Gradient** card on the **Export** tab. If no gradient is open, the **Export** tab says **Select a gradient to enable active exports.** and its buttons reply **Select a gradient first**.

The examples use the first gradient in the collection, **Aurora Simple #00001**. File names are made from the gradient's name in lower case with dashes, for example `aurora-simple-00001`.

| Button | Where | Output |
| --- | --- | --- |
| **Copy CSS** / **Copy CSS gradient** | Inspect, CSS card, Export | Copies the CSS value (**CSS copied**). |
| **Download CSS** / **Download CSS class** | CSS card, Export | `aurora-simple-00001.css`, a ready-made class. |
| **Download JSON** | Quick Export, Export | `aurora-simple-00001.json`: angle, type, stops (position, hex, OKLCH), name and all metadata. |
| **Download SVG** | CSS card, Export | `aurora-simple-00001.svg`, a 1440 × 900 image using an SVG linear gradient at the same angle. |
| **Download Tailwind** / **Download Tailwind token** | Quick Export, Export | `aurora-simple-00001.tailwind.txt`, one `"name": "css"` line for a Tailwind configuration (for example under `backgroundImage`). |
| **Download PNG** / **Download PNG preview** | Quick Export, Export | `aurora-simple-00001.png`, 1600 × 1000 pixels. |
| **Copy share link** | Quick Export, Export | Opens the **Share link** dialog. |
| **Design tokens…** | Quick Export, Export | Opens the design tokens dialog. |

The **Current CSS** card on the **Export** tab shows the open gradient's CSS.

### Examples

The CSS value:

```css
linear-gradient(0deg, #723c2d 0%, #7b3600 100%)
```

The CSS class:

```css
.aa-gradient-aurora-simple-00001 {
  background: linear-gradient(0deg, #723c2d 0%, #7b3600 100%);
}
```

The Tailwind token:

```text
"aurora-simple-00001": "linear-gradient(0deg, #723c2d 0%, #7b3600 100%)"
```

## Design tokens

1. Select **Design tokens…**. A dialog opens with the gradient's name as its title.
2. Set **Token prefix** (default `brand`).
3. Choose a format tab: **W3C Design Tokens**, **CSS Variables**, **SCSS**, **Tailwind Config**, **Style Dictionary**, **Material UI Theme**, **iOS (SwiftUI)** or **Android colors.xml**.
4. Select **Copy**, **Download**, or **Download all** for a ZIP of every format.

File names are `tokens.json`, `tokens.css`, `tokens.scss`, `tailwind.config.js`, `style-dictionary.tokens.json`, `theme.ts`, `Colors.swift` and `colors.xml`. Close with ✕, `Escape` or by selecting outside the dialog.

## Share a link

1. Select **Copy share link**. The **Share link** dialog opens, titled with the gradient's name.
2. Select **Copy** (it shows **Copied!**), **Share via…** where your device offers it, or **Open in new tab**.
3. Select **Close**.

Anyone opening the link sees the Gradient Library with that gradient open on **Inspect**. The link itself carries the gradient; nothing is uploaded. If the gradient cannot be found, the page says **Shared gradient not in current library**.

## Many gradients

The **Visible Set** card on the **Export** tab exports every gradient that matches your search and filters. Its badge shows how many.

| Button | File | Contents |
| --- | --- | --- |
| **JSON with metadata** | `gradient-library-<count>-<date>.json` | Export time, source, count and every gradient in full. |
| **Minified JSON** | `gradient-library-<count>-<date>.json` | Each gradient's name, CSS and stop hex codes, on one line. |
| **CSS classes** | `gradient-library-<count>-<date>.css` | One `.aa-gradient-…` class per gradient. |
| **CSV index** | `gradient-library-<count>-<date>.csv` | One row per gradient: id, name, type, angle, stops, scheme, method, complexity, interpolation, easing, score, complexity_score, banding and CSS. |
| **Tailwind tokens** | `gradient-library-<count>-<date>.txt` | An object of `"name": "css"` pairs. |

If nothing matches, the page says **Nothing to export**.

> **Tip:** Filter first. With no filter, a bulk export includes all 8,192 gradients.

## Result

The gradient is on your clipboard, in a file for your code, design tool or presentation, in design tokens for your platform, or in a link someone else can open.
