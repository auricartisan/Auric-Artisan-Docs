---
title: Auric Color — Hover and swatches
description: Every part of Auric Color's colour hover and inline swatches, which colour formats are detected, and which languages are supported.
product: VS Code extensions › Auric Artisan Studio › Auric Color
updated: 2026-09-25
---

# Hover and swatches

Auric Color finds colour literals in your code, draws a swatch before each one, and shows a detailed hover when you point at one.

## Supported languages

The hover, swatches and pickers work in these VS Code languages. Some of them need a language extension installed so VS Code recognises the file type.

| Group | Languages |
| --- | --- |
| Stylesheets | CSS, SCSS, Sass, Less, PostCSS, Stylus |
| Web and markup | HTML, Vue, Svelte, Astro, PHP, XML, Markdown |
| JavaScript family | JavaScript, TypeScript, JavaScript React (JSX), TypeScript React (TSX), CoffeeScript |
| Data and config | JSON, JSON with Comments, JSON5, HJSON, YAML, TOML, INI, Properties |
| Templates | Handlebars, Pug, Jade, EJS, Twig, Razor, Blade |
| Systems and apps | C, C++, C#, Objective-C, Objective-C++, Go, Rust, Java, Kotlin, Swift, Dart, Scala, Groovy, F#, Visual Basic |
| Scripting | Python, Ruby, Lua, R, Julia, Perl, Shell script, PowerShell |
| Functional and others | Haskell, Elixir, Erlang, Clojure, Solidity, GraphQL, SQL, Dockerfile, Makefile |

## Detected colour formats

| Format | Examples |
| --- | --- |
| Hex, 3, 4, 6 or 8 digits | `#abc`, `#abcd`, `#1d4ed8`, `#1d4ed880` |
| `rgb()` and `rgba()` | `rgb(29 78 216)`, `rgba(29, 78, 216, 0.5)` |
| `hsl()` and `hsla()` | `hsl(221 76% 48%)` |
| `hwb()` | `hwb(221 11% 15%)` |
| `lab()` and `lch()` | `lab(35 21 -71)`, `lch(35 74 287)` |
| `oklab()` and `oklch()` | `oklch(0.49 0.22 264)` |
| `color()` | `color(display-p3 0.2 0.3 0.85)` |
| CSS named colours (148) | `rebeccapurple`, `tomato` |

Not detected as colours: integer literals such as `0xFF00FF`, custom property names such as `var(--brand)`, and `color-mix()` as a whole (the colours inside it are detected individually).

## Swatches

In the default Auric mode, a small square in the colour appears before every colour literal, and the literal gets a faint tinted outline. Swatches appear when:

- the picker mode is **Auric** (`auricColor.colorPicker.mode` is `auric`);
- `auricColor.colorPicker.nativeHoverPicker` is off;
- `auricColor.colorPicker.swatches` is on (the default).

Swatches are not drawn in files larger than 1 MB, and at most 5,000 colours per file are decorated.

**Clicking** a colour literal (with a single cursor and no selection) does what `auricColor.colorPicker.clickAction` says: show the hover picker (default), open the full picker panel, or nothing. See [The colour pickers](color-picker.md).

## The colour hover

Point at a colour literal to open the hover. In Auric Color alone, pointing anywhere else on a line that contains a colour shows the hover for the first colour on that line. With Auric Accessibility installed, pointing at an element or rule that is not a colour shows the Inspect card instead.

> **Note:** When the line has an Auric finding (for example a contrast failure), the hover shows the finding's card instead of the colour card. To see the colour card on such a line, use the full picker (`Ctrl` + `Alt` + `C`).

The hover has these parts, top to bottom.

### Header

A swatch, the hex value, the original text when it differs (for example `oklch(0.49 0.22 264)`), and the nearest CSS colour name. The name is marked `≈` when it is only close, for example `≈ royalblue`.

### Actions

| Link | What it does |
| --- | --- |
| **Type exact…** | Asks for an exact value (hex, `rgb()`, `hsl()`, `oklch()`, `lch()` or a CSS colour name) and writes it back in the token's format. An invalid value shows **Not a recognized color value.** |
| **Spectrum picker** | Opens the full picker for this colour. |
| **Picker mode** | Runs **Choose Color Picker Mode**. |

### Picker rows

Every tile applies its colour to the token immediately, in the token's own format, and the hover reopens on the new value.

| Row | Tiles |
| --- | --- |
| **Spectrum** | 7 rows of 18 tiles: saturation across, brightness down, at the colour's hue. The tile nearest the current colour has a ring. |
| **Hue** | 24 tiles around the colour wheel. |
| **Alpha** | 12 tiles from fully opaque down to 8% opacity. Hex tokens become 8-digit hex; `rgb()` and `hsl()` get an alpha value. |
| **Shades** | The colour's 11-step OKLCH shade scale, 50 to 950. |
| **Fix** | Versions of the colour that reach AA (4.5:1) and AAA (7:1) on white, and AA and AAA on black, keeping the hue. |
| **Brand** | Nine fixed brand swatches. |
| **Recent** | Up to 12 colours you applied recently. |

When VS Code's native picker is shown inside the hover (`colorPicker.nativeHoverPicker` on), the Spectrum, Hue and Alpha rows are left out because VS Code's sliders appear above the hover. In **VS Code native picker** mode, the hover shows only **Shades** and **Brand**.

### Values

- `RGB` red, green and blue from 0 to 255;
- `HSL` hue in degrees, saturation and lightness in percent;
- `OKLCH` lightness, chroma and hue;
- `A` alpha, when the colour is translucent;
- `P3` the same colour as `color(display-p3 …)`, marked *(wide gamut)*.

When the literal is outside the sRGB range (for example a vivid `oklch()` or `color(display-p3 …)`), a warning explains that it is shown, and its contrast measured, as the gamut-mapped sRGB colour a standard screen paints.

### Contrast

The colour's contrast on white and on black, each with a pass or fail icon, the ratio and the level (**AAA**, **AA**, **AA Large** or **Fail**), and **text → white** or **text → black**, whichever reads better on this colour as a background.

### Colour vision

The colour next to how it appears with protanopia, deuteranopia and tritanopia (*protan · deutan · tritan*).

### Open in Studio

Links that open the colour in a Studio tool: **Shades**, **Palette**, **Vision** and **Brand**.

## Turn the hover off

Set `auricColor.hover.enabled` to `false`. Clicking a colour then opens the full picker panel instead of the hover. Contrast and issue hovers are not affected.

## Recent colours

Colours you apply from the hover tiles, **Type exact…** and the pickers are added to your recent colours (up to 12, newest first). They appear in the hover's **Recent** row, the Overview, the Command Center and the pickers.

## Related

- [The colour pickers](color-picker.md)
- [Picker modes](picker-modes.md)
- [Contrast diagnostics](contrast-diagnostics.md)
