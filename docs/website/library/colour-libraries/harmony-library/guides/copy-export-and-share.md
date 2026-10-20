---
title: Harmony Library — Copy, export and share
description: Copy a harmony as hex, CSS, SCSS or Tailwind with role-named variables, download JSON, ASE, SVG or PNG, export design tokens, share a link, and export many harmonies.
product: Website › Library › Colour libraries › Harmony Library
updated: 2026-09-25
---

# Copy, export and share

## Quick copies from the grid

- Select a swatch to copy its hex code.
- Select **Copy** on a card to copy all its hex codes, separated by commas.

## One harmony

Open the harmony on **Inspect**. Use its **Quick export** row, or the **Selection** card on the **Export** tab (headed **Selection ·** with the id and scheme). With nothing open, the **Export** tab says **No harmony selected. Click Inspect on any card in the Library tab to enable selection exports.**

### Copy formats

Variables are named after the harmony's id and each colour's role, which makes them easy to read. The examples use `har_0`, a complementary harmony.

| Quick export | Export tab | What is copied |
| --- | --- | --- |
| **Copy HEX** | **HEX list** | Hex codes, one per line. |
| **Copy CSS vars** | **CSS variables** | A `:root` block. |
| **Copy SCSS** | **SCSS variables** | Sass variables. |
| **Copy Tailwind** | **Tailwind config** | A colour object keyed by role. |

```css
:root {
  --har_0-base: #D17671;
  --har_0-complement: #71CCD1;
}
```

```text
$har_0-base: #D17671;
$har_0-complement: #71CCD1;
```

```json
{
  "har_0": {
    "base": "#D17671",
    "complement": "#71CCD1"
  }
}
```

### Downloads

| Quick export | Export tab | File | Contents |
| --- | --- | --- | --- |
| **Download JSON** | **JSON** | `har_0.json` | Id, method, family, base (hue, saturation, lightness, hex), every colour (role, hex, RGB, HSL, OKLCH, Lab) and metadata including canonical angles, description, adherence and the contrast table. |
| **Download ASE** | **Adobe ASE** | `har_0.ase` | An Adobe Swatch Exchange file with one RGB swatch per colour. |
| **Download SVG** | **SVG strip** | `har_0.svg` | A strip of the colours with hex labels. |
| **Download PNG** | **PNG strip** | `har_0.png` | The same strip as an image. |

**Open in Coolors** (on **Inspect**, and under **External** on the **Export** tab) opens the harmony's colours on coolors.co in a new tab.

## Design tokens

Select **Design tokens…**. The dialog is titled with the harmony's id, and **Token prefix** starts as the harmony's method name in lower case with dashes (for example `split-complementary`). Choose a format — **W3C Design Tokens**, **CSS Variables**, **SCSS**, **Tailwind Config**, **Style Dictionary**, **Material UI Theme**, **iOS (SwiftUI)** or **Android colors.xml** — then **Copy**, **Download**, or **Download all** for a ZIP named, for example, `harmony-har-0.zip`.

## Share a link

Select **Copy share link**. The **Share link** dialog (titled **Harmony** and the id) offers **Copy**, **Share via…** where available, **Open in new tab** and **Close**. The link opens the Harmony Library with the harmony on **Inspect**. If it cannot be found, the page says **Shared harmony not found in current dataset**.

## Many harmonies

The **Visible page** card on the **Export** tab exports every harmony that matches your search and filters — all 8,192 with no filter. Its badge shows the number.

| Group | Button | Contents |
| --- | --- | --- |
| **Bulk download** | **Download JSON (visible page)** | Every harmony in full. |
| | **Download CSV (visible page)** | `harmony_id,method,family,color_count,base_hex,colors` with colours separated by spaces. |
| | **Download CSS variables** | One `:root` block, role-named variables per harmony. |
| | **Download SCSS variables** | Role-named Sass variables. |
| | **Download compact JSON** | Id, method and hex codes per harmony. |
| **Sample formats** | **Download .txt hex list** | Every hex code, one per line. |
| | **Download tailwind.config.js fragment** | A Tailwind configuration with one colour group per harmony. |

Files are named `harmony-page-<count>-<date>.<ext>`. With nothing matching, the page says **Nothing to export**.

## Result

The harmony is on your clipboard, in a file, in design tokens for your platform, or in a link — with variable names that say what each colour does.
