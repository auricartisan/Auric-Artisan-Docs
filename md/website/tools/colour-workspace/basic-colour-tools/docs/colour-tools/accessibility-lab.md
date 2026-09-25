---
title: Accessibility Lab — Check a set of colours against contrast standards and vision filters
description: Compare two to six colours under WCAG 2.1, WCAG 2.2, APCA or ISO 9241-3, preview text in them, and see every colour through seven vision filters.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Accessibility Lab

Accessibility Lab checks a small set of colours, from two to six, as a group. The first colour is the background; the others are foreground colours such as text, buttons and icons. The lab shows a contrast matrix for every pair under the standard you choose, a live text sample in your first two colours, and a grid showing each colour through seven vision filters with its contrast against the background.

It supports four ways of measuring contrast:

- **WCAG 2.1** and **WCAG 2.2**: the luminance contrast ratio, from 1:1 to 21:1. Both versions use the same formula.
- **WCAG 3 (APCA)**: the Accessible Perceptual Contrast Algorithm, reported as **Lc** (lightness contrast). It takes into account which colour is the text and which is the background.
- **ISO 9241-3**: luminance modulation, a measure from an older ergonomics standard for display text.

Accessibility Lab is in the launcher's **Essentials** group.

## Open it

Open the launcher and select **Accessibility Lab**, or pick it from the right-click menu's **Colour tools** group. See [Open the Colour Tools](launcher-and-panels.md). It starts with a dark navy background (#0F172A) and one foreground: the colour you opened it with, or gold (#D3AF37).

## Screen tour

### Sidebar

- **Standard**: WCAG 2.1, WCAG 2.2, WCAG 3 (APCA) or ISO 9241-3.
- **Large text mode**: a check box that applies the large-text thresholds.
- **Colors (first = background)**: one colour field per colour, labelled **Background**, **Color 1**, **Color 2** and so on, with **+ Color**, **- Color** and **Randomize** buttons.
- **Presets**: four ready-made colour sets.
- **Preview CVD filter**: a vision filter applied to the live preview only.
- **Standard info**: a short explanation of the chosen standard.

### Main area

- **Contrast matrix**: every colour against every other colour, labelled with the standard's name.
- **Live preview**: a heading (**Read me clearly**), a paragraph, a line of small print and two buttons (**Outlined** and **Primary**), drawn in the background colour and **Color 1**.
- **Color-vision deficiency grid** (*All 7 filters × all colors*): one row per filter, one column per colour.

## Tasks

### Check a brand palette

1. Set **Background** to your page background colour.
2. Set **Color 1** to your body text colour. Select **+ Color** and add your link, button and accent colours (up to six colours in total).
3. Choose a **Standard**. **WCAG 2.1** is the usual legal and procurement baseline.
4. Read the matrix row or column for **BG**. Each cell shows the value, a bar and a level pill: green for a pass, amber for a borderline result, red for a fail.

Result: you can see which of your colours are readable on your background, and which pairs of foreground colours also contrast with each other.

### Check large text or headings

1. Tick **Large text mode**.
2. The matrix levels switch to the large-text thresholds, and the live preview's text grows from 14 to 18 pixels.

Result: levels for text that is at least 18 point regular or 14 point bold (about 24 and 19 CSS pixels).

### Compare standards

1. Keep the same colours and switch **Standard** between **WCAG 2.1** and **WCAG 3 (APCA)**.
2. Read **Standard info** for what each value means.

Result: you see where the two models agree and where APCA is stricter or more lenient, for example with dark backgrounds or very light text.

### See the colours through vision filters

1. Read the **Color-vision deficiency grid**. Each row shows all your colours as simulated for one filter. Under each foreground swatch is its WCAG 2.1 contrast ratio against the simulated background, coloured green (AA or AAA), amber or red (fail).
2. To see real text, choose a filter in **Preview CVD filter**. The live preview is redrawn through it.

Result: you can spot colours that lose contrast or merge for people with a colour-vision deficiency.

## Standards and levels

| Standard | Value shown | Normal text | Large text |
| --- | --- | --- | --- |
| **WCAG 2.1** / **WCAG 2.2** | Ratio, for example `7.21:1` | **AAA** at 7:1, **AA** at 4.5:1, otherwise **Fail** | **AAA** at 4.5:1, **AA** at 3:1, otherwise **Fail** |
| **WCAG 3 (APCA)** | `Lc` value, for example `Lc -86.4` | **AAA** at 90, **AA** at 75, **Body** at 60, otherwise **Fail** | **AAA** at 75, **AA** at 60, **Body** at 45, otherwise **Fail** |
| **ISO 9241-3** | Modulation, for example `M 0.912` | **Excellent** at 0.7, **Good** at 0.5, **Marginal** at 0.3, otherwise **Poor** | Same |

APCA thresholds apply to the size of the Lc value, whether it is positive or negative. A negative Lc means light text on a dark background; a positive Lc means dark text on a light background. In the matrix, the row colour is treated as the background and the column colour as the text.

The **Standard info** text for each:

- **WCAG 2.1**: body text needs 4.5:1 (AA) or 7:1 (AAA); large text (18 pt regular or 14 pt bold and up) needs 3:1 for AA.
- **WCAG 2.2**: the same ratio as 2.1; version 2.2 adds criteria for focus visibility, target size and consistent help, which a colour tool cannot check.
- **WCAG 3 (APCA)**: Lc runs from about −108 to +106; body text needs an absolute Lc of 75 (AA) or 90 (AAA).
- **ISO 9241-3**: M = (Lmax − Lmin) / (Lmax + Lmin); at least 0.5 is recommended for legible display text under office lighting.

## Vision filters

| Filter | What it simulates |
| --- | --- |
| **Normal vision** | No change. |
| **Deuteranopia** | Missing green-sensitive cones (the most common red-green deficiency). |
| **Protanopia** | Missing red-sensitive cones; reds also look darker. |
| **Tritanopia** | Missing blue-sensitive cones (rare). |
| **Achromatopsia** | No colour vision; greyscale. |
| **Low vision** | Blur with reduced saturation. Live preview only. |
| **Cataract haze** | A yellowish haze with slight blur. Live preview only. |

In the grid, the **Low vision** and **Cataract haze** rows show the colours unchanged, because those two filters are blur effects that apply to a picture, not to single colour values. Use **Preview CVD filter** to see them.

## Presets

| Preset | Colours |
| --- | --- |
| **Auric dark** | #0F172A, #FFFFFF, #D3AF37 |
| **Brand blues** | #1E40AF, #F9FAFB, #F59E0B, #10B981 |
| **Alert states** | #111827, #F3F4F6, #EF4444, #3B82F6, #10B981 |
| **High contrast** | #000000, #FFFFFF, #FF3B30, #34C759, #007AFF, #FFD60A |

The first colour of each preset becomes the background.

## Controls

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| **Standard** | Contrast measure for the matrix | WCAG 2.1, WCAG 2.2, WCAG 3 (APCA), ISO 9241-3 | WCAG 2.1 |
| **Large text mode** | Large-text thresholds; bigger preview text | On or off | Off |
| Colour fields | Background and foreground colours | 2 to 6 colours; HEX or colour well; dice for random | #0F172A and #D3AF37 |
| **+ Color** | Adds a random colour | Up to 6 | — |
| **- Color** | Removes the last colour | At least 2 remain | — |
| **Randomize** | Keeps the count, resets the background to #0F172A and randomises the others | — | — |
| Preset buttons | Load a preset set | 4 presets | — |
| **Preview CVD filter** | Filter for the live preview | Normal vision, Deuteranopia, Protanopia, Tritanopia, Achromatopsia, Low vision, Cataract haze | Normal vision |

## Outputs and exports

The lab is for checking; it has no export. To copy values, open a colour in the [Color Inspector](colour-inspector.md), or use [Contrast System](contrast-system.md) for copyable reports.

## Accuracy and limits

- WCAG ratios use the standard sRGB relative-luminance formula.
- The APCA figure follows a simplified form of the published algorithm. APCA is still a draft for WCAG 3, and its thresholds may change.
- ISO 9241-3 values are computed from relative luminance, not measured screen luminance.
- The colour-vision filters use simple 3 × 3 matrices for complete deficiencies. Milder, more common forms change colours less. The low-vision and cataract filters are illustrations, not medical models.
- Contrast is only one part of accessibility. Font size, weight, spacing and layout matter too.

## Related

- [Colour Tools documentation](README.md)
- [Contrast System](contrast-system.md) for deeper contrast work and readability
- [Type Readability Sim](type-readability-sim.md)
- [Accessibility and vision tools](../../../../accessibility-and-vision/README.md)
- [Basic Color Tools](../../README.md)
