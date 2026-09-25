---
title: Basic Color Tools — Import, export and the Library
description: Every way to bring colours and images into Basic Color Tools, every copy and download format, the palette share link, and saving to and reopening from your Library.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Import, export and the Library

Open panels in Basic Color Tools are not kept when you reload or leave the page. To keep your work, copy it, download it, or save it to your Auric Artisan Library. This guide lists every way in and out.

## Bringing colours and images in

| Into | How | Accepts |
| --- | --- | --- |
| Palette Studio | **From Image** | Any image file your browser can open. Colours are extracted on your device. |
| Palette Studio | Select a HEX label on a strip | Any colour, through the site colour picker. |
| Palette Remix | **Seed colors** box | HEX, `rgb()`, `rgba()`, `hsl()`, `hsla()`, `hsv()`, `oklch()`, separated by lines, spaces, commas, semicolons or vertical bars. |
| Color Battle | **Team A** and **Team B** boxes | Same as Palette Remix, up to nine colours per team. |
| Gradient Maker | Stop HEX boxes and colour wells | Three- or six-digit HEX, or the browser's picker. |
| Color Picker | HEX box, colour well, **Pick** eyedropper | HEX; any pixel on screen where the eyedropper is supported. |
| Quick Converter | Input box, colour well | HEX, `rgb()`, `rgba()`, `hsl()`, `hsla()`, `hsv()`, `oklch()`. |
| Collage Maker | **+ Add Images**, or select a cell | Image files from your device. |
| Any tool | Your Library | Saved palettes, gradients and colours reopen in the matching tool. See below. |

Colours you type in any of the text boxes are converted to sRGB HEX codes. Values outside the sRGB range are clipped.

## Copy and download formats

### Palette Studio

| Button | Kind | Output |
| --- | --- | --- |
| **Share** | Copy | A link with the HEX codes after `#palette=` |
| **CSS** | Copy | CSS custom properties `--color-1` … |
| **SCSS** | Copy | Sass variables `$color-1` … |
| **TW** | Copy | Tailwind `extend.colors` snippet with `palette-1` … |
| **JSON** | Copy | Array of colour objects with metrics |
| **SVG** | Download | `palette.svg`, 1200 × 240 |
| **PNG** | Download | `palette.png`, 1200 × 240 |
| **ASE** | Copy | Tab-separated text lines |

Examples:

```css
:root {
  --color-1: #D3AF37;
  --color-2: #1A1A2E;
}
```

```scss
$color-1: #D3AF37;
$color-2: #1A1A2E;
```

```text
extend: { colors: {
    "palette-1": "#D3AF37",
    "palette-2": "#1A1A2E"
} }
```

```json
[
  {
    "hex": "#D3AF37",
    "rgb": { "r": 211, "g": 175, "b": 55 },
    "oklch": { "L": 0.766, "C": 0.138, "H": 91.6 },
    "lab": { "L": 72.75, "a": 0.95, "b": 62.79 },
    "luminance": 0.448,
    "bestText": { "hex": "#000000", "ratio": 9.96, "label": "dark", "passes": true },
    "locked": false
  }
]
```

For role palettes each object also has `role`, `token`, `pairWith`, `target` and `note`. The real output carries more decimal places than shown here.

The **ASE** text looks like this, with tab characters between the parts:

```text
Color 1	#D3AF37	RGB(211, 175, 55)
Color 2	#1A1A2E	RGB(26, 26, 46)
```

It is plain text, not a binary Adobe Swatch Exchange file.

### Palette Remix

| Button | Kind | Output |
| --- | --- | --- |
| **CSS** | Copy | One `:root` block per set, `--remix-1-1` … |
| **JSON** | Copy | Array of the four sets with `name`, `note`, `hexes` |
| **All HEX** | Copy | Every HEX code, one per line |
| **Copy** (card) | Copy | One set's HEX codes, space-separated |
| Swatch | Copy | One HEX code |

### Gradient Maker

| Button | Kind | Output |
| --- | --- | --- |
| **Copy CSS** | Copy | `background: linear-gradient(…);` (or radial or conic) |
| **SVG** | Download | `gradient.svg`, 800 × 400 |
| **1600px** | Download | `gradient.png`, 1600 × 800 |
| **4K** | Download | `gradient.png`, 3840 × 1920 |
| **JSON** | Copy | The JSON shown on the **Export** tab |
| **Tailwind** | Copy | `backgroundImage: { 'gradient': '…' }` |

Open the **Export** tab after your last change before you copy JSON; see [Gradient Maker](panel-tools/gradient-maker.md).

### Color Picker and Quick Converter

Every row on the **Formats** tab (Color Picker) and the **Convert** tab (Quick Converter) has its own copy button. Quick Converter's **CSS oklch()**, **CSS oklab()** and **CSS lab()** rows are ready for stylesheets.

### Color Battle

| Button | Kind | Output |
| --- | --- | --- |
| **Copy winner** | Copy | The winning team's HEX codes, one per line (Team A in a draw) |
| **Copy report** | Copy | A short text report with the result and both scores |
| Swatch | Copy | One HEX code |

### Collage Maker

| Button | Kind | Output |
| --- | --- | --- |
| **Export PNG (4K)** | Download | `collage.png`, 3,840 pixels wide when the preview is at least 800 pixels wide |

### What "copied" looks like

Every copy button shows a short message such as **Copied**, **CSS copied** or **JSON copied** near the bottom of the page. If your browser blocks clipboard access, nothing is copied; see [Troubleshooting](troubleshooting.md).

## The palette share link

Palette Studio's **Share** button copies a link like this:

```text
https://auricartisan.com/tool/basic-tools/#palette=D3AF37-1A1A2E-F5DEB3-0F172A-FFFFFF
```

The HEX codes are listed after `#palette=`, without `#` signs and separated by hyphens. Opening the link opens Basic Color Tools, but the page does not rebuild the palette from it automatically. Use the link as a compact record: copy the codes and paste them into Palette Remix, Color Battle or Quick Converter.

The Catalogue's **Copy link** button copies the page address as it is in your browser.

## Save to Library

The **Save to Library** button floats near the bottom-right corner of the page. On narrow screens it shows only its icon.

1. Focus the panel you want to save by selecting it.
2. Select **Save to Library**.
3. A save window opens listing what will be saved. For each item you can edit the **Name** and **Description**. You can also choose a **Collection** (or leave it **Unfiled**) and add **Tags (comma-separated)** for all items.
4. Select **Save to Library** in the window, or press `Ctrl` + `Enter` (`Cmd` + `Enter` on a Mac). Select **Cancel** to close without saving.

Result: a message such as **Saved "Palette · 5 colors (analogous)"** appears, and the item is in your Library.

What each tool saves:

| Focused panel | Saved as |
| --- | --- |
| Palette Studio | One palette, with the harmony mode and CVD preview setting. |
| Palette Remix | Four palettes, one per remix set, named after the set. |
| Gradient Maker | One gradient, with its CSS, stops, type, angle, interpolation and easing. |
| Color Picker | One colour, with its formats and harmony colours. |
| Color Battle | Two palettes, **Team A** and **Team B**, each remembering both teams and the result. |
| Quick Converter | One colour, with every format. |
| Collage Maker | Nothing from the collage. Export the PNG instead. |
| No panel open, or only Collage Maker | A **Basic Tools workspace** bookmark that records your level setting. |

Save acts on the focused panel. Docked (minimised) panels are not saved. If there is nothing to save, a message says **Nothing to save yet — try creating something first.**

## Reopening saved items

You can reopen items from your Library in Basic Color Tools. The item opens in a fresh panel of the tool that suits it, replacing any panel of that tool that is already open:

| Saved item | Reopens in |
| --- | --- |
| A palette saved from Palette Studio | Palette Studio (**Loaded N colors from library**) |
| A remix set | Palette Remix, as seed colours (**Loaded remix from library**) |
| A gradient | Gradient Maker (**Loaded gradient from library**) |
| A colour saved from Color Picker | Color Picker (**Loaded color from library**) |
| A colour saved from Quick Converter | Quick Converter (**Loaded color from library**) |
| A Color Battle team | Color Battle, with both teams (**Loaded teams from library**) |
| A palette, gradient or colour saved from another tool | Palette Studio, Gradient Maker or Color Picker, by type |
| A saved analysis run from the URL Analyzer | Palette Studio, with the colours of the audited page |

Because a restore opens a fresh panel, any unsaved work in the replaced panel is lost.

For how to browse, organise and send items from the Library, see the [Library Kit](../../../../kits/library-kit/README.md).

## Related

- [Basic Color Tools overview](../README.md)
- [Panel tools](panel-tools/README.md)
- [Reference](reference.md)
- [Privacy](../others/privacy.md)
