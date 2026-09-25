---
title: Contrast System — Analyse and fix text contrast
description: Check up to five foreground colours on one background under WCAG 2.x, APCA and ISO 9241-3, read an APCA font-size table, sweep lightness on a contrast curve, fix colours to AA or AAA, and preview them in a realistic interface.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Contrast System

Contrast System is the workbench's in-depth contrast tool. You set one background and up to five foreground colours. For each pair it reports three measures side by side, suggests the nearest colour that passes, shows which font sizes and weights the pair can carry under APCA, and draws the pair in a realistic interface sample.

The three measures:

- **WCAG 2.x contrast ratio**: the luminance ratio used by WCAG 2.0, 2.1 and 2.2, from 1:1 to 21:1. 4.5:1 is AA for normal text, 7:1 is AAA, 3:1 is AA for large text.
- **APCA Lc** (shown as **WCAG 3 APCA**): the Accessible Perceptual Contrast Algorithm, proposed for WCAG 3. **Lc** (lightness contrast) runs from about −108 to +106. A negative value means light text on a dark background, a positive value dark text on a light background. Readability depends on its size and on the font's size and weight.
- **ISO 9241-3 modulation (M)**: (Lmax − Lmin) / (Lmax + Lmin), from 0 to 1, from the ergonomics standard for display text.

Contrast System is in the launcher's **Essentials** group.

## Open it

Open the launcher and select **Contrast System**, pick it from the right-click menu's **Colour tools** group, or right-click a colour value and select **Check its contrast**. See [Open the Colour Tools](launcher-and-panels.md). It starts with a dark navy background (#0F172A) and one foreground: the colour you opened it with, or gold (#D3AF37).

## Screen tour

### Sidebar

- **Background**: one colour field.
- **Foreground colors**: one colour field per foreground, labelled **FG 1**, **FG 2** and so on, with **+ Add**, **− Remove** and **Swap BG↔FG1**.
- **Text size**: **Normal**, **Large** or **Small**. Changes the scale of the **Preview** tab.
- **Preview filter**: a vision filter for the **Preview** tab.
- **Quick presets**: five background-and-foreground sets.
- A summary with one line per foreground: its WCAG ratio (coloured green, amber or red) and its APCA Lc.

### Main area tabs

| Tab | What it shows |
| --- | --- |
| **Analysis** | One card per foreground with all three measures and fix buttons. |
| **APCA Guide** | The Lc value for one pair, a plain-language verdict, and a font size and weight table. |
| **Curve** | How the contrast ratio changes as the foreground gets lighter or darker, with suggested alternatives and the nearest AA and AAA colours. |
| **Preview** | A realistic interface drawn in your colours, with a stats card per foreground. |

## The Analysis tab

Each card shows:

- A header with the background swatch, a small **Aa — FG 1 on BG** sample, both HEX codes and the foreground swatch.
- **WCAG 2.x**: a bar, the ratio (for example `7.21:1`) and two level pills, **norm** and **large**.
- **WCAG 3 APCA**: a bar, the Lc value with its sign (for example `Lc −86.4`) and two level pills, **body** and **large**.
- **ISO 9241**: a bar, the modulation (for example `M 0.912`) and a level pill.
- Four buttons: copy the foreground HEX code, **→ Fix to AA**, **→ Fix to AAA** and **Curve**.

Pills are green for a pass, amber for a borderline result and red for a fail. The levels:

| Measure | Levels |
| --- | --- |
| WCAG 2.x, normal | **AAA** 7:1, **AA** 4.5:1, else **Fail** |
| WCAG 2.x, large | **AAA** 4.5:1, **AA** 3:1, else **Fail** |
| APCA, body | **AAA** Lc 90, **AA** Lc 75, **Body** Lc 60, else **Fail** |
| APCA, large | **AAA** Lc 75, **AA** Lc 60, **Body** Lc 45, else **Fail** |
| ISO 9241-3 | **Excellent** 0.7, **Good** 0.5, **Marginal** 0.3, else **Poor** |

APCA levels use the size of Lc, whichever its sign.

## Tasks

### Check your text colours on a background

1. Set **Background** to your surface colour.
2. Set **FG 1** to your body text colour. Select **+ Add** for headings, links and muted text (up to five foregrounds).
3. Read each card on **Analysis**. Look at the **norm** pill for body text and the **large** pill for headings.

Result: every text colour rated under three measures at once.

### Fix a colour that fails

1. On a failing card, select **→ Fix to AA** (4.5:1) or **→ Fix to AAA** (7:1).
2. The foreground changes to the nearest passing colour and **Fixed to AA** or **Fixed to AAA** appears.

The fix keeps the colour's hue and chroma and moves only its OKLCH lightness, in small steps: lighter on a dark background, darker on a light one. It stops at the first step that passes. If no lightness can reach the target (for example 7:1 on a mid-grey background), it stops at the lightest or darkest version it tried, which may still fail; the card shows the result.

Result: a foreground that looks like the original but meets the ratio.

### Pick a size and weight with the APCA guide

1. Open **APCA Guide**. Choose a pair with the **FG** buttons next to **Pair:**.
2. Read the large Lc value and the verdict under it:

| Lc (absolute) | Verdict shown |
| --- | --- |
| 90 or more | AAA — suitable for all body text, small and large. |
| 75 to 90 | AA — passes body text at regular weights and sizes. |
| 60 to 75 | Fluent — readable for mid-size and larger text. |
| 45 to 60 | Spot — suitable for short labels and larger UI text only. |
| 30 to 45 | Non-text / large decorative elements only. |
| Under 30 | Insufficient — fails all text readability thresholds. |

3. Read the table. Rows are font sizes (10, 12, 14, 16, 18, 24, 32 and 48 pixels); columns are font weights (100 to 900). Each cell shows:
   - **✓**: passes with room to spare (or the combination needs no minimum);
   - **✓~**: passes with a small margin (less than 15 Lc above the minimum);
   - **✗**: fails; hover to see the Lc needed;
   - **—**: that size and weight is not usable at any contrast.

Result: you know the smallest and thinnest type the pair can support, for example "16 px needs weight 400 or more".

### Explore lighter and darker alternatives

1. Open **Curve**, or select **Curve** on an analysis card. Choose a pair next to **Pair:**.
2. Read the chart **WCAG contrast ratio curve — FG lightness sweep**. The line shows the contrast ratio (vertical axis, up to 21) for every OKLCH lightness of the foreground (horizontal axis, dark to light), keeping its hue and chroma. Dashed lines mark **7:1 AAA**, **4.5:1 AA** and **3:1 Lg**. A ringed dot marks the current foreground.
3. Under the chart, read the three current figures (**WCAG 2.x**, **APCA Lc**, **ISO mod**) with their levels.
4. Under **Alternatives**, eight chips show the foreground at eight lightness levels with their ratio and level. Select one to use it.
5. Below, two cards show **Nearest AA (4.5:1)** and **Nearest AAA (7:1)**, each with a preview, its HEX code and ratio. Select **Use this color** to apply it.

Result: the same colour family at a lightness that works, chosen by eye.

### Preview the pair in an interface

1. Open **Preview**.
2. The sample draws a small product interface in the background colour, with **FG 1** as the text colour and **FG 2** as the accent: a header (**Panel Preview**, the active filter and the FG 1 ratio), a heading (*The quick brown fox*), body text, 11-pixel small print, **Primary** and **Secondary** buttons, an **FG 2 link**, a **Badge**, a dashboard card with APCA Lc and ISO figures, a form with an email field and a status list, a table of levels (**Normal text**, **Large text**, **APCA body**) and three alert states.
3. A strip at the bottom shows *Aa* under **Normal**, **Deuteranopia**, **Protanopia**, **Tritanopia** and **Achromatopsia**.
4. Change **Text size** to **Small** or **Large** to scale the sample, and **Preview filter** to see it through a vision filter.
5. Under the sample, one stats card per foreground shows its ratio, APCA Lc and level, ISO modulation and level, and a WCAG pill.

Result: you judge the colours in context, not only as numbers.

## Quick presets

| Preset | Background | Foregrounds |
| --- | --- | --- |
| **Dark UI** | #0F172A | #FFFFFF, #D3AF37 |
| **Light UI** | #F9FAFB | #111827, #1D4ED8 |
| **High contrast** | #000000 | #FFFFFF, #FFFF00 |
| **Brand gold** | #1A1A2E | #D3AF37, #E8E8E8 |
| **Alert red** | #FEF2F2 | #991B1B, #B91C1C |

## Controls

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| **Background** | Background colour | HEX, colour well, dice | #0F172A |
| **FG 1** … **FG 5** | Foreground colours | 1 to 5 | #D3AF37, or the colour you opened with |
| **+ Add** | Adds a random foreground | Up to 5 | — |
| **− Remove** | Removes the last foreground | At least 1 remains | — |
| **Swap BG↔FG1** | Exchanges the background and FG 1 | — | — |
| **Text size** | Scale of the Preview sample | Normal, Large, Small | Normal |
| **Preview filter** | Vision filter on the Preview sample | Normal vision, Deuteranopia, Protanopia, Tritanopia, Achromatopsia, Low vision | Normal vision |
| Quick presets | Load a preset | 5 presets | — |
| Copy HEX (card) | Copies the foreground HEX | — | — |
| **→ Fix to AA** / **→ Fix to AAA** | Adjusts lightness to 4.5:1 or 7:1 | — | — |
| **Curve** (card) | Opens the Curve tab for that pair | — | — |
| **Pair:** buttons | Choose the foreground for APCA Guide and Curve | FG 1 to FG 5 | FG 1 |
| Alternative chips | Apply one of eight lightness variants | OKLCH L 0.05 to 0.95 | — |
| **Use this color** | Apply the nearest AA or AAA colour | — | — |

## Outputs and exports

- Copy a foreground's HEX code from its analysis card.
- Fixed and suggested colours replace the foreground, so you can copy them from the colour field.
- There is no file export. For code output, open the colour in the [Color Inspector](colour-inspector.md).

## Accuracy and limits

- WCAG ratios use the standard sRGB relative-luminance formula.
- The APCA value follows a simplified form of the published algorithm, and the size and weight table is based on the APCA bridge guidance for WCAG 3. APCA is still a draft; treat its results as guidance.
- ISO 9241-3 modulation is computed from relative luminance, not measured on a screen.
- The fix and the curve change only OKLCH lightness. Colours outside the sRGB range are clipped, which can shift them slightly.
- Vision filters are simple simulations; see [Accessibility Lab](accessibility-lab.md) for their limits.

## Related

- [Colour Tools documentation](README.md)
- [Accessibility Lab](accessibility-lab.md) for a whole palette at once
- [Type Readability Sim](type-readability-sim.md)
- [Animation Contrast](animation-contrast.md) for text over moving backgrounds
- [Contrast Checker and other accessibility tools](../../../../accessibility-and-vision/README.md)
- [Basic Color Tools](../../README.md)
