---
title: Color Library — Copy and export
description: Copy one colour in six formats, download it as JSON, SVG or PNG, and download every matching colour in seven formats.
product: Website › Library › Colour libraries › Color Library
updated: 2026-09-25
---

# Copy and export

The **Export** tab has two parts: **Selection**, for the one colour you have open, and **Visible set**, for every colour that currently matches your chips, searches and filters. You can reach the tab directly, or select **Export visible** on the **Library** tab.

## Copy or download one colour

1. Open a colour (select its tile). See [Read a colour](read-a-colour.md).
2. Select the **Export** tab. The first card is headed **Selection ·** and the colour's hex code.
3. Under **Copy formats**, select a format. The text goes to your clipboard and a short message confirms it, such as **HEX copied**.
4. Under **Download**, select a file type. Your browser saves the file.

If no colour is open, the card reads **No color selected. Click any tile in the Library tab to enable selection exports.**

### Copy formats

Examples are for the atlas colour `#76CDF6`.

| Button | What is copied | Example |
| --- | --- | --- |
| **HEX** | The hex code in capitals. | `#76CDF6` |
| **RGB** | A CSS `rgb()` value with commas. | `rgb(118, 205, 246)` |
| **HSL** | A CSS `hsl()` value, whole numbers. | `hsl(199 88% 71%)` |
| **Lab** | A CSS `lab()` value, two decimals. | `lab(78.56% -15.21 -28.22)` |
| **OKLCH** | A CSS `oklch()` value. | `oklch(80.89% 0.102 230.17)` |
| **CSS variables** | A `:root` block with four custom properties. | See below |

The **CSS variables** button copies:

```css
:root {
  --color-hex: #76cdf6;
  --color-rgb: 118, 205, 246;
  --color-hsl: 199 88% 71%;
  --color-oklch: 80.89% 0.102 230.17;
}
```

### Downloads for one colour

| Button | File | Contents |
| --- | --- | --- |
| **JSON (full metadata)** | The hex code without `#`, for example `76cdf6.json` | The colour's complete record: every notation, metric, label and colour-blindness value. |
| **SVG** | For example `76cdf6.svg` | A 480 × 280 rectangle of the colour with its hex code written near the bottom in black or white, whichever reads better. |
| **PNG** | For example `76cdf6.png` | An 800 × 480 image of the same design. |

## Download every matching colour

1. On the **Library** tab, narrow the grid with the chips, searches and filters.
2. Select **Export visible**, or the **Export** tab.
3. Read the **Visible set** card's badge. It shows how many colours will be exported, for example **2,998 colors**.
4. Select a format under **Bulk download** or **Style formats**. Your browser saves the file.

Files are named `color-library-` followed by the number of colours and the date, for example `color-library-2998-2026-09-24.css`. The message **Downloaded** and the file name confirms each download. If nothing matches, the page says **Nothing to export**.

### Bulk formats

| Button | File type | Contents |
| --- | --- | --- |
| **JSON (all metadata)** | `.json` | The export time, a source note, the count, and a list of the colours with the fields the browser holds for them: id, hex, RGB, hue, lightness, chroma, luminance, contrast on white and black, and the five labels. |
| **JSON (compact: id + hex)** | `.json` | The count and a list of id and hex pairs. |
| **CSV (flat)** | `.csv` | Meant to hold one row per colour with a header row: id, hex, RGB, HSL, Lab, OKLCH, luminance, chroma and four labels. If no file arrives, see [Troubleshooting](troubleshooting.md). |
| **.txt (one hex per line)** | `.txt` | Hex codes in capitals, one per line. |

### Style formats

| Button | File type | Contents |
| --- | --- | --- |
| **CSS variables** | `.css` | A `:root` block with one custom property per colour, named by atlas id. |
| **SCSS variables** | `.scss` | One Sass variable per colour, named by atlas id. |
| **tailwind.config.js fragment** | `.js` | A Tailwind CSS configuration that adds each colour to `theme.extend.colors`, named `c` plus the atlas id. |

Examples, for a set containing colour 0:

```css
:root {
  --color-0: #76CDF6;
}
```

```text
$color-0: #76CDF6;
```

```js
module.exports = {
  theme: { extend: { colors: {
      "c0": "#76CDF6"
    } } }
};
```

> **Tip:** Variable names use the atlas id, not a descriptive name. After exporting, rename the variables you keep to names that mean something in your project, such as `--brand-accent`.

> **Note:** Exports are built in your browser from the data already loaded, so they work without a further download. A large set can take a moment.

## Result

You have the colour value on your clipboard, or a file on your computer that you can paste into a stylesheet, a Tailwind configuration, a spreadsheet or a design tool.
