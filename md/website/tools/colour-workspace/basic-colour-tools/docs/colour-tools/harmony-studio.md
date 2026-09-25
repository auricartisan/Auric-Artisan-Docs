---
title: Harmony Studio — Build a harmony palette that works on your background
description: Generate eight kinds of colour harmony from one base colour, optionally adjust every swatch to meet a contrast target on your background, preview them and export HEX, CSS, JSON or PNG.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Harmony Studio

Harmony Studio builds a palette from one base colour using a classic colour-harmony pattern, such as complementary, triadic or square, and shows it on a colour wheel. It can then adjust each colour so that it reaches a contrast target against a background you choose, which turns a pretty palette into one you can use for text and interface elements.

A **colour harmony** is a set of hues chosen by their position on the colour wheel: opposite each other (complementary), evenly spaced (triadic, square), or close together (analogous). Harmony Studio rotates hue in OKLCH, a perceptual colour space, so the colours keep the base colour's lightness and chroma.

Harmony Studio is in the launcher's **Design** group.

## Open it

Open the launcher and select **Harmony Studio**, pick it from the right-click menu's **Colour tools** group, or right-click a colour value and select **Build harmonies**. See [Open the Colour Tools](launcher-and-panels.md). The base colour starts as the colour you opened with, or gold (#D3AF37); the background starts as dark navy (#0F172A).

## Screen tour

### Sidebar

- **Base color** and **Background**: colour fields.
- **Scheme**: the harmony pattern.
- **Mode**: how the colours are adjusted for contrast.
- **Mono count**: a slider for the number of colours in the **Monochromatic** scheme.
- **Export**: **Copy HEX list**, **Copy CSS variables**, **Copy JSON** and **Download PNG**.

### Main area

1. **Harmony wheel**, with a summary such as *3 colors · Standard (math)*: a hue ring with a dot for each colour joined by a dashed outline, the base colour ringed in gold and shown as a disc in the centre. Beside it, a legend lists each colour's HEX code, OKLCH hue, lightness and chroma, and its contrast ratio against the background; the first is marked **Base**.
2. **Palette**: a card per colour with a swatch, HEX code, a level pill (**AAA**, **AA**, **AA Lg** or **Fail**) for its contrast against the background, the ratio, and its OKLCH lightness and chroma.
3. **Preview on background**: the background with a **Sample Heading** in the first colour, body text in the second colour, up to five buttons (**Btn 1** to **Btn 5**) filled with the palette colours, and a tag for each colour.

## Schemes

| Scheme | Hue offsets from the base | Colours |
| --- | --- | --- |
| **Complementary** | 0°, 180° | 2 |
| **Split-Complement** | 0°, 150°, 210° | 3 |
| **Analogous** | −30°, 0°, +30° | 3 |
| **Triadic** | 0°, 120°, 240° | 3 |
| **Tetradic** | 0°, 90°, 180°, 270° | 4 |
| **Square** | 0°, 90°, 180°, 270° | 4 |
| **Monochromatic** | Same hue, lightness from dark to light | 3 to 9 (**Mono count**) |
| **Double Split** | 0°, +30°, −30°, 150°, 210° | 5 |

**Tetradic** and **Square** produce the same four hues in this tool. In **Analogous** the list starts with the hue 30° below your base colour, so the first card, the gold-ringed dot and the **Base** label in the legend show that colour; your base colour is the second one.

## Modes

| Mode | What it does |
| --- | --- |
| **Standard (math)** | Uses the harmony colours as calculated. |
| **WCAG 4.5:1 (AA)** | Adjusts each colour until it reaches 4.5:1 against the background. |
| **Soft 3.5:1** | Adjusts each colour to 3.5:1, a gentler target that keeps more colour. |
| **High-contrast 7:1 (AAA)** | Adjusts each colour to 7:1. |

The adjustment changes only lightness: each colour is made lighter if it is already lighter than the background, or darker if it is darker, in small steps until it meets the target. If a colour cannot reach the target within the steps allowed, it keeps the closest result, and its card shows the real level.

## Tasks

### Make an accessible accent set for a dark interface

1. Set **Background** to your dark surface colour.
2. Set **Base color** to your brand colour.
3. Choose a **Scheme**, for example **Split-Complement**.
4. Set **Mode** to **WCAG 4.5:1 (AA)**.
5. Check the **Palette** cards: each should show **AA** or **AAA**.
6. Look at **Preview on background** to judge the colours together.

Result: a set of related colours, each readable as text on your background.

### Build a monochromatic ramp

1. Choose **Monochromatic**.
2. Move **Mono count** to the number of steps you need, from 3 to 9.

The ramp keeps the base colour's hue and chroma and spreads OKLCH lightness from dark (0.18) to light (0.88).

Result: a tonal ramp you can use for surfaces, borders and text.

### Export the palette

- **Copy HEX list**: comma-separated codes in palette order, starting with the base colour. Message: **HEX list copied**.
- **Copy CSS variables**: one line per colour, `--color-1: #D3AF37;` and so on. Message: **CSS variables copied**.
- **Copy JSON**: the scheme, mode, base, background and palette. Message: **JSON copied**.
- **Download PNG**: downloads `harmony-palette.png`, a strip 80 pixels wide per colour and 100 pixels tall, with HEX labels.

Example JSON:

```json
{
  "scheme": "triadic",
  "mode": "standard",
  "base": "#D3AF37",
  "background": "#0F172A",
  "palette": ["#D3AF37", "#…", "#…"]
}
```

### Send a colour to another tool

1. Right-click a palette card. The site's colour menu opens with copy options and **Check its contrast**, **Build harmonies**, **Find its name** and **Inspect in Colour Tools**.
2. For Harmony Studio's own menu, hold `Shift` while you right-click the card. It offers **Copy HEX**, **Open in Color Spaces**, **Open in Accessibility**, **Find name** and **Open in Psychology**. `Esc` or a click elsewhere closes it.

Result: the colour opens in the chosen tool as its starting colour.

## Controls

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| **Base color** | The colour the harmony is built from | HEX, colour well, dice | #D3AF37, or the colour you opened with |
| **Background** | Colour for contrast checks and preview | HEX, colour well, dice | #0F172A |
| **Scheme** | Harmony pattern | 8 schemes | Triadic |
| **Mode** | Contrast adjustment | Standard (math), WCAG 4.5:1 (AA), Soft 3.5:1, High-contrast 7:1 (AAA) | Standard (math) |
| **Mono count** | Colours in Monochromatic | 3 to 9 | 5 |
| **Copy HEX list** | Copies codes, comma-separated | — | — |
| **Copy CSS variables** | Copies `--color-N` lines | — | — |
| **Copy JSON** | Copies the full state | — | — |
| **Download PNG** | Downloads `harmony-palette.png` | — | — |
| Palette card, `Shift` + right-click | Opens the tool's colour menu | 5 actions | — |

## Accuracy and limits

- Hues are rotated in OKLCH. The wheel places the dots by their HSL hue, so their positions on the ring can look slightly uneven even when the OKLCH offsets are exact.
- Rotated colours outside the sRGB range are clipped, which can change their lightness or chroma a little.
- Contrast uses the WCAG 2.x ratio. A colour adjusted to 4.5:1 is suitable for normal text on that background only.
- Harmony rules are conventions, not guarantees of a pleasing result.

## Related

- [Colour Tools documentation](README.md)
- [Palette Studio](../panel-tools/palette-studio.md) for generated palettes with locking and many exports
- [Accessibility Lab](accessibility-lab.md)
- [Color Space Converter](colour-space-converter.md)
- [Color Theory and Harmony](https://auricartisan.com/library/learn/articles/2026-06-04-color-theory-and-harmony) on Learn
- [Basic Color Tools](../../README.md)
