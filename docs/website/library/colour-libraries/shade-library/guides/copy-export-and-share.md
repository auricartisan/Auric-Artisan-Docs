---
title: Shade Library — Copy, export and share
description: Copy a shade scale as hex, token-named CSS, SCSS or Tailwind, download JSON, SVG or PNG, export design tokens, share a link, and export many scales.
product: Website › Library › Colour libraries › Shade Library
updated: 2026-09-25
---

# Copy, export and share

## One scale

Open the scale on **Inspect**. Use **Quick export**, or the **Selection** card on the **Export** tab (headed **Selection -** and the id). With nothing open, the **Export** tab says **No shade system selected. Click Inspect on any card in the Library tab to enable selection exports.**

Names in the output come from the scale's name with the hex codes removed, in lower case with dashes: **Material Like #FF724C #00001** becomes `material-like-00001`. Each variable ends in the token name.

### Copy formats

| Quick export | Export tab | What is copied | Message |
| --- | --- | --- | --- |
| **Copy HEX** | **HEX list** | All hex codes, comma-separated. | **HEX list copied** |
| **Copy CSS vars** | **CSS variables** | A CSS class holding one custom property per token. | **CSS variables copied** |
| **Copy SCSS** | **SCSS variables** | One Sass variable per token. | **SCSS copied** |
| **Copy Tailwind** | **Tailwind config** | A colour group keyed by token. | **Tailwind copied** |

For the first scale in the collection:

```css
.aa-shade-material-like-00001 {
  --material-like-00001-50: #fff0ec;
  --material-like-00001-100: #ffdfd7;
  --material-like-00001-300: #ff886b;
  --material-like-00001-500: #ff724c;
  --material-like-00001-700: #cd5531;
  --material-like-00001-900: #4b1200;
  --material-like-00001-950: #1e0400;
}
```

```text
$material-like-00001-50: #fff0ec;
$material-like-00001-100: #ffdfd7;
...
$material-like-00001-950: #1e0400;
```

```text
"material-like-00001": {
  "50": "#fff0ec",
  "100": "#ffdfd7",
  ...
  "950": "#1e0400"
}
```

> **Tip:** The CSS variables are declared on a class, not on `:root`. Either add that class to an element, or change the selector to `:root` after pasting. Rename the prefix to something meaningful in your project, such as `--brand-500`.

### Downloads

| Quick export | Export tab | File | Contents |
| --- | --- | --- | --- |
| **Download JSON** | **JSON** | `shade-000000.json` | Id, name, base, method, token names, each token's hex and contrast on white and black, and score, average lightness, average chroma and auto-AA count. |
| **Download SVG** | **SVG strip** | `shade-000000.svg` | A 1200 × 260 strip of the tokens; hovering a band shows its token and hex. |
| **Download PNG** | **PNG strip** | `shade-000000.png` | A 1600 × 420 strip. |

## Design tokens

Select **Design tokens…**. The dialog is titled with the scale's name. **Token prefix** starts as `color`, and every token keeps its step name: `color-50`, `color-100` … `color-950`. Choose **W3C Design Tokens**, **CSS Variables**, **SCSS**, **Tailwind Config**, **Style Dictionary**, **Material UI Theme**, **iOS (SwiftUI)** or **Android colors.xml**, then **Copy**, **Download**, or **Download all** for a ZIP such as `shade-shade-000000.zip`.

## Share a link

Select **Copy share link**. The **Share link** dialog offers **Copy**, **Share via…** where available, **Open in new tab** and **Close**. The link opens the scale on **Inspect**; if it cannot be found, the page says **Shared shade not in current library**.

## Many scales

The **Visible page** card on the **Export** tab exports every scale matching your search and filters (all 8,192 with none set). Its badge shows the number.

| Button | File | Contents |
| --- | --- | --- |
| **Download JSON (visible page)** | `shade-library-<count>-<date>.json` | Every scale in full. |
| **Download CSV (visible page)** | `…csv` | `id,name,base,method,tokens,score,avg_lightness,avg_chroma,auto_aa,colors`, with colours separated by vertical bars. |
| **Download CSS variables** | `…css` | One class per scale. |
| **Download SCSS variables** | `…scss` | Sass variables per scale. |
| **Download compact JSON** | `…json` | Id and hex codes per scale. |
| **Download .txt hex list** | `…txt` | One line per scale: its id, a colon and its hex codes. |
| **Download tailwind.config.js fragment** | `…txt` | One Tailwind colour group per scale, inside braces. |

If nothing matches, the bulk buttons do nothing.
