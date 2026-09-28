---
title: Accessibility Lab — Audit a palette for readability
description: Audit two to eight colours as a set under WCAG 2.2, APCA or ISO 9241-3, rank every pair with its nearest fix, see the palette under seven kinds of vision and check a sample interface.
product: Website › Tools › Colour workspace
updated: 2026-09-27
---

# Accessibility Lab

Accessibility Lab audits a palette of two to eight colours as one set. The first colour is the background; the others are the colours you set on it and on each other, such as text, links, buttons and icons. The lab checks every pair under the standard you choose, ranks them from best to worst, finds the nearest passing colour for each pair that fails, shows how the palette holds up under seven kinds of vision, and draws a small interface in your colours with a check for each element.

It measures contrast three ways:

- **WCAG 2.2**: the contrast ratio, from 1:1 to 21:1. WCAG 2.1 and 2.2 compute contrast the same way, so there is one option.
- **APCA**: the lightness contrast **Lc**, which depends on which colour is the text and which the background.
- **ISO 9241-3**: luminance modulation **M**, from 0 to 1.

Accessibility Lab is one of the six **Essentials** in the Colour Tools. It opens in a floating panel; for the panel, its footer and its links, see [Open the Colour Tools and work in their panels](launcher-and-panels.md).

## Open it

- **Launcher:** press `Ctrl` + `Shift` + `C` (or right-click the page and choose **Colour tools** › **All colour tools…**), then select **Accessibility Lab**.
- **Right-click menu:** **Colour tools** › **Accessibility Lab**.
- **Dashboard:** the **Accessibility Lab** card, or **Open the full audit in Accessibility Lab** under **Set health**, which brings the whole working set. See [Colour Tools dashboard](colour-tools-dashboard.md).
- **From another tool:** **Open in another tool** › **Accessibility Lab** in Contrast System, Type Readability Sim, Animation Contrast and Color Library.
- **A link:** `?ctool=a11y`, for example `https://auricartisan.com/?ctool=a11y&colors=FFFFFF,111111,1E40AF,DC2626`. See [Link keys](#link-keys).

Opened with a colour, the lab puts it in **Colour 1** on the house navy background: `#0F172A`, your colour, `#F5F0E6` and `#765A0B`. Opened with no colour, **Colour 1** is the site's gold, `#D3AF37`.

## Screen tour

### The header band

The band paints the palette: the background colour on the left with the audit's summary, then a block for each colour with its role and hex code.

- The kicker names the standard and the text size, for example "Audit · WCAG 2.2 · body".
- The title counts the colours and the pairs that pass, for example "4 colours · 3 of 6 pairs readable as body text".
- The last line says how many colours pass as text on the background, for example "On #0F172A · 2 of 3 pass as text".

### The controls rail

- **Colours · first is the background**, with a count such as "4 of 8". Each colour has a field: **Background**, **Colour 1**, **Colour 2** and so on. Every colour but the background has a remove button (×) while there are more than two colours.
- **Add a colour** adds a random colour at the end. At eight it reads **Eight is the limit**.
- **Randomize** gives every colour except the background a new random colour, keeping the count.
- **Presets**: four ready-made palettes (see [Presets](#presets)). The first colour of each becomes the background.
- **Standard**: **WCAG 2.2**, **APCA** or **ISO 9241-3**, with a note on how that standard reads.
- **Text**: **Body** or **Large**. Every tab uses the thresholds for the size you choose.

## Standards and levels

Each pair is read as the later colour (the text) on the earlier one (the surface), so the **Background** is always the surface.

| Standard | Value | Passes for body text | Passes for large text | Result words |
|---|---|---|---|---|
| **WCAG 2.2** | Ratio, for example `8.46:1` | 4.5:1 | 3:1 | Body: **AAA** (7:1), **AA** (4.5:1), **Large only** (3:1) or **Fail**. Large: **AAA** (4.5:1), **AA** (3:1) or **Fail**. |
| **APCA** | Signed Lc, for example `Lc −59` | Lc 75 | Lc 60 | **Lc 75 body**, **Lc 60 large**, **Lc 45 headline**, **Lc 30 spot** or **Below 30**. |
| **ISO 9241-3** | Modulation, for example `M 0.961` | M 0.5 | M 0.3 | **Excellent** (0.7), **Good** (0.5), **Marginal** (0.3) or **Poor**. |

The notes under **Standard** say:

- **WCAG 2.2:** "WCAG 2.1 and 2.2 compute contrast identically; 2.2 adds focus, target-size and help criteria, not a new formula. Body 4.5:1, large 3:1, AAA 7:1."
- **APCA:** "APCA Lc is signed: positive = dark text on light, negative = light text on dark. Body needs Lc 75, large text Lc 60."
- **ISO 9241-3:** "Modulation M = (Lmax − Lmin) / (Lmax + Lmin). Body needs M 0.5 (Good); 0.7 is Excellent. Large text accepts 0.3 here, a house reading — ISO has no large-text rule."

**Large** text means at least 24 pixels, or 18.66 pixels bold.

## The tabs

### Matrix

The opening sentences count the pairs that pass and name the strongest, then name the weakest pair and what it can carry, for example "The weakest, Colour 2 on Colour 1, reaches only 1.85:1 — decoration only." Under APCA they count "directed pairs" instead, because each pair is measured both ways round.

The matrix paints every pair as "Aa" in the text colour on the surface colour, with its value and a result pill. Rows are backgrounds and columns are text.

- Under **WCAG 2.2** and **ISO 9241-3**, swapping text and background gives the same number, so only the upper half of the grid is shown.
- Under **APCA** the whole grid is shown and signed: positive Lc for dark text on light, negative for light text on dark.

On a narrow panel the matrix scrolls sideways.

### Pairs

Every pair from best to worst, numbered. Each row shows the pair painted, its name and hex codes (for example "Colour 3 on Colour 1", `#765A0B on #D3AF37`), the value with its pill, and **Use for**: what the pair can carry at any size.

| Standard | **Use for** |
|---|---|
| WCAG 2.2 | **Body text** (4.5:1), **Large text, UI parts / icons (3:1)**, or **Decoration only** |
| APCA | **Body text** (Lc 75), **Large text** (Lc 60), **UI parts / icons** (Lc 30), or **Decoration only** |
| ISO 9241-3 | **Body text** (M 0.5), **Large text, UI parts** (M 0.3), or **Decoration only** |

Each pair that fails carries its fix: "Nearest passing text: #594200 reaches 4.51:1, lightness lowered, hue kept." Select **Use #594200** to put that colour in place of the text colour. The fix keeps the colour's hue and chroma in OKLCH and changes only its lightness, by the smallest step that passes. When no lightness of that hue can pass, the row says so: "No lightness at this hue reaches 4.5:1 on #0F172A. Change the hue or the background."

### Vision

The opening sentences compare normal vision with the hardest view, for example "2 of 3 colours pass on #0F172A in normal vision; under cataract none of them does.", then count the pairs that come close under any view.

**Each colour on the background** has a row for each of seven views. Each row shows every colour as "Aa" on the background, both simulated, with the value under the chosen standard; a cross marks a value that does not pass. The pill counts the colours that pass, for example "2 of 3 pass".

| View | What it shows |
|---|---|
| **Normal** · As designed | The colours as they are. |
| **Protan** · No long-wave cones | Protanopia. |
| **Deutan** · No mid-wave cones | Deuteranopia. |
| **Tritan** · No short-wave cones | Tritanopia. |
| **Achromat** · Lightness only | Achromatopsia: no colour at all. |
| **Low vision** · Blur, contrast −15% | Each pair mixed 15% towards its middle grey, and the sample blurred. |
| **Cataract** · Yellowed lens, glare veil | A yellowed lens (less blue, a little less green) and a veil of glare, 10% of the pair's average brightness, added to both colours; the sample is slightly blurred. White on navy drops from 15.71:1 to about 9.2:1. |

**Hard to tell apart · ΔE 2000 under 10** lists up to eight pairs of colours, under any view, that come close enough to be mistaken for each other, closest first: "Under cataract, Background (#0F172A) and Colour 3 (#765A0B) come within ΔE 9.7." The pill says **Hard to tell apart** under ΔE 5 and **Close — add labels** from 5 to 10. When a pair comes that close, label it rather than rely on colour. If no pair does, the tab says so.

### Preview

A small interface card drawn in **Background**, **Colour 1** and **Colour 2**: a **New** badge, a line of small print, the heading "Read me clearly", a paragraph with a link, a longer line of small print, a **Primary action** button and an **Outline** button.

Choose a view above the card, **Normal**, **Protan**, **Deutan**, **Tritan**, **Achromat**, **Low vision** or **Cataract**, to see the card that way. The opening sentence counts the elements that pass and names the first that fails, for example "In normal vision, 7 of 7 elements meet WCAG 2.2 at their own size."

**Checks** gives each element its value and pill, at its own size:

| Element | What is measured |
|---|---|
| **Heading** | Colour 1 on Background · 28 px, large |
| **Body text** | Colour 1 on Background · 15 px, body (24 px, large, with **Text** set to **Large**) |
| **Small print** | Colour 1 on Background · 12 px, body |
| **Link** | Colour 2 on Background · body |
| **Button label** | Its ink (black or white, whichever reads better) on Colour 2 · 14 px bold, body |
| **Button edge** | Colour 2 against Background · non-text |
| **Outline button** | Colour 1 border on Background · non-text |

The two non-text checks need 3:1, Lc 30 or M 0.3 and read **UI ok** or **Too faint**. With only two colours, Colour 1 also plays the link and the button, and the sentence suggests adding a third.

## Presets

| Preset | Colours |
|---|---|
| **Auric dark** | `#0F172A`, `#FFFFFF`, `#D3AF37` |
| **Brand blues** | `#1E40AF`, `#F9FAFB`, `#F59E0B`, `#10B981` |
| **Alert states** | `#111827`, `#F3F4F6`, `#EF4444`, `#3B82F6`, `#10B981` |
| **High contrast** | `#000000`, `#FFFFFF`, `#FF3B30`, `#34C759`, `#007AFF`, `#FFD60A` |

## Walkthroughs

### Audit a brand palette

1. Set **Background** to your page background, and **Colour 1** to your body text colour.
2. Select **Add a colour** for each other colour you use, such as links, buttons and accents, and type each one in.
3. Choose a **Standard**. **WCAG 2.2** is the usual baseline for legal and procurement checks.
4. Open **Pairs**. Pairs at the top are safe for body text; each failing pair shows its nearest fix.
5. Select **Use** on a fix you like. The palette, the matrix and the header band update at once.

### Check headings and large labels

1. Set **Text** to **Large**.
2. Read **Matrix** or **Pairs** again. Pairs that were **Large only** for body text now pass.

### Check a palette for colour-blind readers

1. Open **Vision**.
2. Read the pills down the right: any row with fewer passes than **Normal** loses readability for that reader.
3. Read **Hard to tell apart**. For each **Hard to tell apart** pair, add a label, an icon or a pattern.

## Controls

| Control | What it does | Values or range | Default |
|---|---|---|---|
| Colour fields | Set each colour. | 2 to 8 colours; hex, CSS names, CSS colour functions | `#0F172A`, the colour you opened with (or `#D3AF37`), `#F5F0E6`, `#765A0B` |
| Remove (×) | Removes that colour. | Not on the background; at least 2 remain | — |
| **Add a colour** | Adds a random colour. | Up to 8 | — |
| **Randomize** | New random colours for all but the background. | — | — |
| Presets | Load a palette. | 4 presets | — |
| **Standard** | Sets the measure on every tab. | **WCAG 2.2**, **APCA**, **ISO 9241-3** | **WCAG 2.2** |
| **Text** | Sets the thresholds on every tab. | **Body**, **Large** | **Body** |
| **Use #…** (Pairs) | Replaces the text colour with its nearest fix. | — | — |
| View (Preview) | Shows the card as seen. | 7 views | **Normal** |

## Outputs and exports

| Output | Format | What it contains |
|---|---|---|
| **Copy report** (gold button) and **Markdown report** | Markdown | "# Accessibility audit", the standard and text size, the colours with their roles, the number of pairs that pass, a table of every pair (rank, text on background, value, result, use for, nearest fix), and a **Colour vision** list of the pairs that come within ΔE 10. |
| **CSV matrix** | CSV | A grid with a row per background and a column per text colour, headed with each role and hex. Cells hold the value under the chosen standard: the ratio rounded down to two decimals, the signed Lc to one decimal, or M to three. |
| **JSON** | JSON | The standard, the text size, the colours with their roles, and every pair with its text, background, value, result, use and fix. |
| **CSS custom properties** | CSS | `--a11y-background`, `--a11y-colour-1` and so on, each with a comment giving its result on every earlier colour, for example `/* on background 18.88:1 AAA */`. |
| **Save audit** | A palette in your Library | Named "Accessibility audit · 4 colours", with how many pairs pass. |
| **Share link** | URL | `?ctool=a11y` with `colors`, and `std`, `size` and `ctab` when they are not the defaults. |

**Open in another tool** offers **Contrast System** (the text colours on your background), **Harmony Studio** (a harmony from Colour 1 on your background), **Type Readability Sim** (the weakest pair at real sizes), **Color Inspector** (Colour 1) and **Color Psychology** (the mood of the first six colours).

## Link keys

| Key | What it sets | Values |
|---|---|---|
| `colors` | The palette, background first. | 2 to 8 hex codes, comma-separated, for example `FFFFFF,111111,1E40AF` |
| `color` | Colour 1, with the default background and colours, when there is no `colors`. | A colour |
| `std` | The standard. | `wcag` (default), `apca`, `iso` |
| `size` | The text size. | `body` (default), `large` |
| `ctab` | The tab to open on. | `matrix` (default), `pairs`, `vision`, `preview` |

Older links with `std=wcag21` or `std=wcag22` open WCAG 2.2, and `std=wcag3` opens APCA.

## Accuracy and limits

- **Terms.** *WCAG contrast ratio*: the ratio between two colours' relative luminance. *APCA Lc*: a newer measure of perceived lightness contrast that depends on which colour is the text. *Modulation M*: the ISO 9241-3 measure, the difference between the two luminances over their sum. *ΔE2000*: the CIEDE2000 colour difference; under about 2, two colours look the same side by side.
- **Ratios are rounded down, and Lc is cut towards zero,** so a pair never shows a level it misses: Lc −59.6 shows as Lc −59, not Lc −60.
- **APCA is a guide.** WCAG 3, which may adopt APCA, is still a draft. For a WCAG 2.2 audit, use **WCAG 2.2**.
- **The ISO large-text threshold is a house reading.** ISO 9241-3 has no large-text rule; the lab accepts M 0.3 for large text, and says so.
- **Vision simulations are approximations.** The four colour-vision views model full-strength deficiencies (Machado, Oliveira and Fernandes, 2009) in linear light. Milder forms are more common. **Low vision** and **Cataract** are simple house simulations of reduced contrast, haze and blur, not medical models.
- **Contrast is not the whole of accessibility.** Size, weight, spacing, focus indicators and layout matter too. WCAG 2.2's new criteria (focus, target size, help) cannot be checked from colours.
- **Colours are solid sRGB.** Transparency is not taken into account.

## Related

- [Colour Tools documentation](README.md)
- [Open the Colour Tools and work in their panels](launcher-and-panels.md)
- [Contrast System](contrast-system.md) — several text colours on one background, with size guidance and fixes
- [Type Readability Sim](type-readability-sim.md) — reading comfort at real sizes and conditions
- [Colour Tools dashboard](colour-tools-dashboard.md) — a quick health check of your working set
- [Accessibility and vision tools](../../../../accessibility-and-vision/README.md)
- [Basic Color Tools](../../README.md)
