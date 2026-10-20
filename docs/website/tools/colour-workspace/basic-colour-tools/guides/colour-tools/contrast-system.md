---
title: Contrast System — Is this text readable?
description: Check one background against up to five text colours with WCAG, signed APCA and ISO 9241-3 scores, read APCA size and weight guidance, find the nearest passing shade in both directions, and preview the pair in an interface.
product: Website › Tools › Colour workspace
updated: 2026-09-27
---

# Contrast System

Contrast System answers one question: is this text readable on this background? You set one background and up to five text colours. For each text colour it gives three scores (the WCAG 2 ratio, the signed APCA lightness contrast and the ISO 9241-3 modulation), says which sizes and weights the pair can carry, finds the nearest lighter and darker shade that passes, and draws a sample interface in your colours, as designed or as seen with a colour-vision deficiency.

Use it when you are choosing text colours for one surface. To check a whole palette against itself, use [Accessibility Lab](accessibility-lab.md).

Contrast System is one of the six **Essentials** in the Colour Tools. It opens in a floating panel; for the panel, its footer and its links, see [Open the Colour Tools and work in their panels](launcher-and-panels.md).

## Open it

- **Launcher:** press `Ctrl` + `Shift` + `C`, then select **Contrast System**. To check a particular colour, type it in the launcher's search and choose **Check … as text on …**.
- **Right-click menu:** **Colour tools** › **Contrast System**, or right-click a colour value and choose **Check its contrast**.
- **Dashboard:** the **Contrast System** card. See [Colour Tools dashboard](colour-tools-dashboard.md).
- **From another tool:** **Open in another tool** › **Contrast System** in Accessibility Lab, Type Readability Sim and Animation Contrast.
- **A link:** `?ctool=contrast`, for example `https://auricartisan.com/?ctool=contrast&on=0F172A&fg=D3AF37,F5F0E6`. See [Link keys](#link-keys).

It starts with the house navy background, `#0F172A`, and three text colours: the colour you opened it with (or the site's gold, `#D3AF37`), `#F5F0E6` and `#765A0B`.

## Screen tour

### The header band

The band is painted in the background colour, with each text colour as a large "Aa" above its ratio and hex code. Select an "Aa" to make that colour the **selected** one; the selected colour is outlined, and the **Size & weight**, **Fix** and footer actions follow it.

The band's lines describe the selected pair:

- the background and text size, for example "On #0F172A · body text";
- the pair in words, its ratio and grade, for example "Light soft amber on very dark greyish blue · 8.46:1 · AAA";
- the hex code, the APCA Lc and the modulation, for example "#D3AF37 · Lc −59 · M 0.96".

### The controls rail

- **Background**: the colour field for the surface.
- **Text colours**, with a count such as "3 of 5". Each has a label (**Text 1**, **Text 2** …, with "· selected" on the selected one), its ratio and Lc, a swatch you can select to make it the selected colour, a colour field, and a remove button (×) while there is more than one.
- **Add a text colour** adds a random colour and selects it. At five it reads **Five is the limit**.
- **Swap background and selected** exchanges the background with the selected text colour.
- **Text size**: **Small**, **Body** or **Large**. The size sets the WCAG and APCA levels on every tab.
- **Presets**: five ready-made pairs (see [Presets](#presets)).

| **Text size** | Means | WCAG needs | APCA needs |
|---|---|---|---|
| **Small** | Under 14 px | 4.5:1 (AAA 7:1) | Lc 90 |
| **Body** | 14 to 23 px | 4.5:1 (AAA 7:1) | Lc 75 |
| **Large** | At least 24 px, or 18.66 px bold | 3:1 (AAA 4.5:1) | Lc 60 |

## The tabs

### Scores

The opening sentences count the text colours that pass WCAG AA for the chosen size and name the weakest, for example "2 of 3 text colours pass WCAG AA for body text on #0F172A (4.5:1). Text 3 (#765A0B) reaches only 2.75:1 — Fix finds the nearest shade that passes." The second says whether APCA agrees: "APCA is stricter: 1 of 3 reach Lc 75 for body text." (or "in step", or "more lenient").

A card for each text colour shows a sample ("Aa" and a line of text in your colours, at the chosen size) and three scores:

| Score | What it shows |
|---|---|
| **WCAG 2.x** | The ratio, a **Body** pill (**AAA**, **AA**, **Large only** or **Fail**) and a **Large** pill (**AAA**, **AA** or **Fail**). |
| **APCA** | The signed Lc, its level (**Lc 75 body**, **Lc 60 large**, **Lc 45 headline**, **Lc 30 spot** or **Below 30**) and what the chosen size needs, for example "body text needs Lc 75", with "— met" when it is. |
| **ISO 9241-3** | The modulation M and its word: **Excellent**, **Good**, **Marginal** or **Poor**. |

Each card has **Copy #…** (the hex code), **Fix** (or **Fix · AAA** when the colour already passes AA), which selects the colour and opens **Fix**, and **Sizes**, which selects it and opens **Size & weight**.

### Size & weight

What the selected pair can carry, from APCA's published guidance (its "bronze" level). The opening sentence gives the pair's Lc and the smallest sizes it works at, for example "Text 1 on #0F172A is Lc −59. It carries text from 36 px at 400 and from 24 px at 700. Body columns need Lc 75: lighten the pair or go bigger."

Choose the pair to judge in the row of text colours at the top. Then:

- **APCA readability guidance (bronze)** lists six levels with **✓ meets** or **✗ below** for this pair:

| Level | Use |
|---|---|
| Lc 90 | Preferred for body text columns |
| Lc 75 | Body text · ≥ 18 px/400 or ≥ 14 px/700 |
| Lc 60 | Other content text · ≥ 24 px/400 or ≥ 16 px/700 |
| Lc 45 | Headlines · ≥ 36 px/400 or ≥ 24 px/700 |
| Lc 30 | Spot text, placeholders, disabled |
| Lc 15 | Non-text: icons, dividers, focus hints |

- **Size × weight** is a grid of sizes (12, 14, 16, 18, 24, 32 and 48 px) against weights (300 to 900). Each cell shows ✓ or ✗ and the Lc that size and weight need.
- **Smallest size that passes, as set** shows the text at the smallest size that works at weight 400 and at weight 700, for example "24 px and up", or "No size passes".

### Fix

The opening sentences give the selected pair's ratio and Lc, then the nearest AA and AAA shades, for example "The nearest AA is #9A7D38, lighter by L 0.120." Choose the text colour to fix in the row at the top.

- **Lightness sweep** draws two charts, **WCAG ratio** and **APCA |Lc|**, across every OKLCH lightness from 0 to 1 at the colour's own hue and chroma. The line is drawn in the colour at each lightness; a white ring marks your colour now, grey rings the nearest AA and AAA, and dashed lines the thresholds.
- **Nearest passing · searched lighter and darker** has a card for AA and one for AAA at the chosen size. Each card has a pill (**Passes now**, **Reachable** or **Unreachable**), a sentence, and a **Lighter** and a **Darker** line with the shade, its ratio, the lightness change and its ΔE from your colour, for example "#9A7D38 · 4.56:1 · L +0.120 · ΔE 13.6". Select **Use #…** to put that shade in place of the selected text colour. When a direction cannot reach the level, the line says "Nothing on this side reaches 4.5:1", and the sentence says which side can, for example "No darker brown reaches 4.5:1 — the lighter side does, at #9A7D38."
- **Alternatives along the sweep · tap to use** shows eight shades of the same hue from dark to light, each with its ratio and result. Select one to use it.

### Preview

A mock app screen in your colours: an app bar ("Studio dashboard"), a heading, body text with a link, small print at 11.5 px, **Primary**, **Secondary** and **Badge** buttons, a contrast figure, an email field, a small table and an alert. **Text 1** is the text; **Text 2** is the accent for the link, the buttons and the badge.

Choose how it is seen: **Normal**, **Protan**, **Deutan**, **Tritan**, **Achromat** or **Low vision**. The sentence says what holds, for example "As designed, Text 1 holds 8.46:1 on the background and the accent, Text 2, 15.71:1." Under a deficiency it names any text colour that drops below the AA level, or says "No text colour loses its AA result."

**Each text colour** lists every text colour on the background as seen that way, with its ratio, Lc and result.

## Presets

| Preset | Background | Text colours |
|---|---|---|
| **Dark UI** | `#0F172A` | `#FFFFFF`, `#D3AF37` |
| **Light UI** | `#F9FAFB` | `#111827`, `#1D4ED8` |
| **High contrast** | `#000000` | `#FFFFFF`, `#FFFF00` |
| **Brand gold** | `#1A1A2E` | `#D3AF37`, `#E8E8E8` |
| **Alert red** | `#FEF2F2` | `#991B1B`, `#B91C1C` |

## Walkthroughs

### Check your text colours on a background

1. Set **Background** to your surface colour.
2. Type your text colours into **Text 1**, **Text 2** and so on, or select **Add a text colour**.
3. Set **Text size** to the size you will use.
4. Read **Scores**. A green **Body** pill means the colour can carry body text; **Large only** means headings and big labels only.

### Fix a colour that fails

1. On **Scores**, select **Fix** on the failing colour's card.
2. Read **Nearest passing**. The shade with the smaller move is named in the sentence.
3. Select **Use #…**. The text colour changes, and every tab updates.

### Pick a size and weight

1. Select **Sizes** on a card, or open **Size & weight**.
2. Find the smallest size with a ✓ at the weight you plan to use, or read **Smallest size that passes, as set**.

## Controls

| Control | What it does | Values or range | Default |
|---|---|---|---|
| **Background** | Sets the surface. | Hex, CSS names, CSS colour functions | `#0F172A` |
| Text colour fields | Set each text colour. | 1 to 5 | The colour you opened with (or `#D3AF37`), `#F5F0E6`, `#765A0B` |
| Swatch beside a text colour, or its "Aa" in the band | Selects that colour. | — | Text 1 |
| Remove (×) | Removes that text colour. | At least 1 remains | — |
| **Add a text colour** | Adds a random colour and selects it. | Up to 5 | — |
| **Swap background and selected** | Exchanges the two. | — | — |
| **Text size** | Sets the WCAG and APCA levels. | **Small**, **Body**, **Large** | **Body** |
| Presets | Load a background and two text colours. | 5 presets | — |
| **Copy #…**, **Fix**, **Sizes** (Scores) | Copy, or select and jump to a tab. | — | — |
| **Use #…** and the alternatives (Fix) | Replace the selected text colour. | — | — |
| Vision (Preview) | Shows the preview as seen. | 6 views | **Normal** |

## Outputs and exports

| Output | Format | What it contains |
|---|---|---|
| **Copy CSS** (gold button) and **CSS variables** | CSS | `--contrast-bg` and `--contrast-text-1` to `--contrast-text-5`, each text colour with a comment giving its ratio, body result and Lc, for example `/* 8.46:1 AAA body · Lc −59 on --contrast-bg */`. |
| **JSON report** | JSON | The background, the text size, and for each text colour its hex, ratio, WCAG body and large results, APCA Lc and level, and ISO M and word. |
| **Markdown** | Markdown | "# Contrast report", the background and the levels for the size, and a table with Text, Hex, WCAG, Body, Large, APCA and ISO M. |
| **Save check** | A palette in your Library | Named "Contrast check · 3 on #0F172A", with how many pass. |
| **Share link** | URL | `?ctool=contrast` with `on`, `fg`, and `size` and `ctab` when they are not the defaults. |

**Open in another tool** offers **Accessibility Lab** (the background and all text colours as one set), **Type Readability Sim**, **Animation Contrast**, **Harmony Studio** and **Color Inspector**, each with the selected text colour.

## Link keys

| Key | What it sets | Values |
|---|---|---|
| `on` (or `bg`) | The background. | A hex code |
| `fg` | The text colours. | 1 to 5 hex codes, comma-separated |
| `color` | Text 1, with the default Text 2 and Text 3, when there is no `fg`. | A colour |
| `size` | The text size. | `small`, `body` (default), `large` |
| `ctab` | The tab to open on. | `scores` (default), `size`, `fix`, `preview` |

## Accuracy and limits

- **Terms.** *WCAG contrast ratio*: the ratio between two colours' relative luminance, from 1:1 to 21:1. *APCA Lc*: a newer measure of perceived lightness contrast, positive for dark text on light and negative for light text on dark. *Modulation M*: the ISO 9241-3 measure. *OKLCH*: a colour model whose lightness, chroma and hue change evenly to the eye. *ΔE2000*: the CIEDE2000 colour difference.
- **Ratios are rounded down, and Lc is cut towards zero,** so a pair never reads as a level it misses.
- **APCA is a guide.** WCAG 3, which may adopt APCA, is still a draft; for a WCAG 2.2 audit, use the WCAG scores.
- **Weights in the APCA grid.** APCA's bronze guidance defines levels at weights 400 and 700. The tool reads 500 and 600 as 400, 800 and 900 as 700, and holds weight 300 one level stricter, which is a house rule. Anything below the body minimums needs Lc 90.
- **Fixes change lightness only.** The hue and chroma are kept (chroma is trimmed where sRGB runs out), so a fix can look less saturated than you expect, and some hues cannot reach a level on some backgrounds at all.
- **When a colour already passes,** **Fix** still lists a shade a hair lighter or darker that also passes, and a direction that leads towards the background says "Nothing on this side reaches …" even though nearby shades on that side would still pass.
- **Vision simulations are approximations** of full-strength deficiencies (Machado, Oliveira and Fernandes, 2009, in linear light). **Low vision** also mixes each pair 15% towards its middle grey and blurs the card; it is a simple illustration, not a medical model.
- **Colours are solid sRGB.** Transparency is not taken into account.

## Related

- [Colour Tools documentation](README.md)
- [Open the Colour Tools and work in their panels](launcher-and-panels.md)
- [Accessibility Lab](accessibility-lab.md) — a whole palette, every pair
- [Type Readability Sim](type-readability-sim.md) — comfort at real sizes, fonts and viewing conditions
- [Animation Contrast](animation-contrast.md) — text over moving backgrounds
- [Color Inspector](colour-inspector.md) — one colour on this page, on white and on black
- [Accessibility and vision tools](../../../../accessibility-and-vision/README.md)
- [Basic Color Tools](../../README.md)
