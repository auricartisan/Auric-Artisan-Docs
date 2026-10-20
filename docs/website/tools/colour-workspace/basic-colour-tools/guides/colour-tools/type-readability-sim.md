---
title: Type Readability Sim — Is this type comfortable?
description: Score how comfortable text will be to read from its colours, font, size, weight, letter-spacing and line height under five viewing conditions, with every factor shown, size and weight sweeps, and one-click recommendations.
product: Website › Tools › Colour workspace
updated: 2026-09-27
---

# Type Readability Sim

Type Readability Sim asks whether text will be comfortable to read, not only whether it passes a contrast rule. You set a text colour and a background, a font, a size, a weight, letter-spacing and line height, a viewing condition and the kind of text. The tool gives a comfort score from 0 to 100 and shows every factor's share of it, sweeps sizes and weights, shows the same text under five viewing conditions, and suggests single changes that would help, each one click away.

The comfort score is a house heuristic, not a standard, and the tool labels it that way. The contrast levels behind it come from APCA's published guidance, and the WCAG 2 ratio is shown alongside.

Type Readability Sim is one of the six **Essentials** in the Colour Tools. It opens in a floating panel; for the panel, its footer and its links, see [Open the Colour Tools and work in their panels](launcher-and-panels.md).

## Open it

- **Launcher:** press `Ctrl` + `Shift` + `C`, then select **Type Readability Sim**.
- **From another tool:** **Open in another tool** › **Type Readability Sim** in Contrast System, Accessibility Lab (the weakest pair) and Animation Contrast (the worst moment).
- **A link:** `?ctool=type`, for example `https://auricartisan.com/?ctool=type&color=D3AF37&on=0F172A&px=18`. See [Link keys](#link-keys).

The colour you open it with becomes the **text** colour. It starts on the house navy background, `#0F172A`, in Sans — Manrope at 16 px, weight 500, letter-spacing 0.00 em, line height 1.50, **Normal indoor**, with a **Body paragraph**. Opened with no colour, the text is the site's gold, `#D3AF37`.

## Screen tour

### The header band

The band is a live specimen: the sample text set in your font, size, weight and letter-spacing, in your text colour on your background. Above it are the font, size, weight and condition (for example "MANROPE · 16 PX · 500 · NORMAL INDOOR") and the score (for example "COMFORT 38 · STRAINED"). Below it: the colours, the APCA Lc with the level it needs, and the WCAG ratio, for example "#D3AF37 on #0F172A · Lc −59 (needs 90) · 8.46:1".

### The controls rail

| Control | What it does | Range |
|---|---|---|
| **Text colour** | The colour of the text. Has a dice button for a random colour. | Any colour |
| **Background** | The surface. Its swap button (**Swap text and background**) exchanges the two. | Any colour |
| **Font** | The typeface, with a note on how it reads. | See below |
| **Size** | The text size. | 10 to 48 px |
| **Weight** | The stroke weight. Fixed at 200 with **Display thin**. | 100 to 900, in steps of 100 |
| **Letter-spacing** | The tracking. | −0.05 to 0.20 em |
| **Line height** | The leading. It counts only for multi-line samples. | 1.10 to 2.00 |
| **Viewing condition** | The situation the text is read in. | See below |
| **Sample content** | The kind of text, which changes the level it needs. | See below |

**Font** offers faces the site really has, or says when it falls back:

| Option | Note |
|---|---|
| **Sans — Manrope** | The neutral reference. Manrope covers weights 200 to 800, so 100 and 900 draw at the nearest cut. |
| **Serif — Fraunces** | A contrasty serif; its fine hairlines thin out under 16 px. |
| **Mono — Courier New** | The site's monospace. Even widths break word shapes in prose; ideal for figures. |
| **Display thin — Manrope 200** | A display cut at weight 200. Strokes are thin, so comfort drops; the weight is fixed. |
| **Rounded — system rounded** | The system's rounded face where one exists (Apple devices, or Arial Rounded where installed); elsewhere the system sans. |

**Viewing condition**:

| Option | How it is shown | Note |
|---|---|---|
| **Normal indoor** | No change | Office light, rested eyes, typical acuity. |
| **Low vision 20/40** | Blur 0.6 px | Mild blur, the driving-licence limit in many places. |
| **Low vision 20/80** | Blur 1.8 px | Strong blur; fine detail and thin strokes disappear. |
| **Bright glare** | 10% white veil | A white veil over the screen, mixed into both colours before Lc is measured. |
| **Tired eyes** | Blur 0.3 px + 5% veil | End-of-day reading. |

**Sample content**:

| Option | What it changes |
|---|---|
| **Body paragraph** | A two-line paragraph, read as body text. |
| **UI label** | A short interface label ("Account settings"): one level below body text, never below Lc 45. |
| **Button** | A button label ("Save changes"): one level below body text, never below Lc 45. |
| **Long-form reading** | One level stricter than body text, up to Lc 90. |
| **Tabular numbers** | Figures that must be read exactly: body-text levels, with tabular numerals. |

## How the level is set

Each size and weight needs a minimum APCA Lc, from APCA's published "bronze" guidance: Lc 75 for body text from 18 px at 400 or 14 px at 700, Lc 60 from 24 px at 400 or 16 px at 700, Lc 45 from 36 px at 400 or 24 px at 700, and Lc 90 below the body minimums. The guidance defines weights 400 and 700 only, so the tool reads 500 and 600 as 400, 800 and 900 as 700, and holds lighter weights one level stricter (a house rule). The **Sample content** then moves the level one step, as described above.

## The tabs

### Verdict

The opening sentences give the score and its word, the pair in words with its Lc and the level it needs, the biggest cost and the biggest help, and the WCAG result for the actual size, for example "Comfort 38/100 — strained. Light soft amber on very dark greyish blue at 16 px/500 reaches Lc −59; this size, weight and content need Lc 90."

- **The score** from 0 to 100, with its word and "House heuristic, not a standard", on a scale marked 0 Unreadable, 35, 50, 65 and 85 Effortless:

| Score | Word |
|---|---|
| 85 and over | **Effortless** |
| 65 to 84 | **Comfortable** |
| 50 to 64 | **Legible** |
| 35 to 49 | **Strained** |
| Under 35 | **Unreadable** |

- **Key values · tap to copy**: **APCA** (the Lc, and whether it meets its level or what the condition leaves), **Needs** (the Lc this size, weight and content need), **WCAG 2.x** (the ratio, and whether it passes 4.5:1 for normal-size text or 3:1 for large text), and **Margin** (how far the Lc is above or below its level: "Comfortable headroom" at 15 or more, "Thin headroom", or "Short of the level").
- **Factor breakdown · from a base of 60**: seven factors, each with a sentence, a bar and a signed number of points, and the sum (clamped to 0 to 100).

| Factor | How it counts |
|---|---|
| **Contrast margin** | 0.8 points for each Lc above or below the level needed, from −40 to +20. |
| **Size** | 0.8 points per pixel away from a 16 px reference, from −8 to +10. |
| **Weight** | Thin strokes under 400 cost points; 400 to 700 helps a little; heavier weights start to close the letters' counters. |
| **Font** | Display thin −8; Mono −4 in prose (+1 with **Tabular numbers**); Rounded −1; Serif −3 under 16 px. |
| **Letter-spacing** | Negative tracking crowds the letters; beyond 0.05 em words start to fall apart; beyond ±0.12 em there is a further cost. |
| **Line height** | For paragraphs, under 1.4 or over 1.7 costs points. A single line is not affected. |
| **Condition** | What a glare or tiredness veil takes off the contrast, plus a fixed cost for blur. |

- **Strongest fix**: the recommendation that would help most, with a button to apply it.

### Sweeps

The opening sentence counts the size and weight combinations that reach their level for this kind of text, and gives the smallest size at 400 and at 700, for example "6 of 48 size and weight combinations reach their level for a body paragraph at Lc 59. No size at 400, from 24 px at 700."

- **Size × weight**: a grid of sizes (12, 14, 16, 18, 20, 24, 28 and 32 px) against weights (300 to 800). Each cell shows ✓ or ✗ and the Lc needed; your current setting is marked.
- **Size ladder**: the sample at each of those sizes at your weight, each with its result.
- **Weight ladder**: the sample at each weight at your size.

The measure is the Lc under the current viewing condition.

### Conditions

The sample under all five viewing conditions at once, each with its Lc, score and word. The opening sentence counts the conditions that keep the pair at its level and names the hardest, for example "0 of 5 conditions keep the pair at its APCA level. The hardest is low vision 20/80, at 14/100 (unreadable)." Select a row to make it the viewing condition.

### Recommendations

Single changes that would help, strongest first. Each shows an "Aa" preview, what to do, why, and the score before and after (for example "38 → 84"), with **Apply**:

- **Use N px**: the next size up at which the pair meets its level;
- **Use weight N**: the next weight up at which it does (not offered with **Display thin**);
- **Lighten text to #…** or **Darken text to #…**: the nearest text colour of the same hue and chroma that reaches the level under the current condition;
- **Use Sans — Manrope** (or **Use Sans — Manrope 400**): offered for **Display thin**, and for **Mono** in prose;
- **Set letter-spacing to 0.00 em** or **0.02 em**: offered for negative or very wide tracking;
- **Set line height to 1.5**: offered for paragraphs set tighter than 1.4 or looser than 1.7.

The first three are offered only when the pair misses its level or scores under 65. Each is scored by running the same heuristic with only that one change. If nothing needs changing, the tab says so and suggests trying **Low vision 20/80** to see whether the margin holds.

## Walkthroughs

### Check whether small text is comfortable

1. Set your text colour and background, the **Font** and the **Size** you plan to use.
2. Set **Sample content** to match: **UI label** for labels, **Body paragraph** for running text.
3. Read the score on **Verdict** and the biggest cost in the second sentence.

### Test under harder conditions

1. Open **Conditions**.
2. Compare the rows. A pair that is comfortable indoors can become strained in glare or with blurred vision.
3. Select the hardest row to make it the condition, then open **Recommendations** to see what would hold up there.

### Follow a recommendation

1. Open **Recommendations**.
2. Select **Apply** on the change you want. The rail, the specimen and the score update, and a line confirms the new score.

## Controls

| Control | Values or range | Default |
|---|---|---|
| **Text colour** | Any colour | The colour you opened with, or `#D3AF37` |
| **Background** | Any colour | `#0F172A` |
| **Font** | 5 options | **Sans — Manrope** |
| **Size** | 10 to 48 px | 16 px |
| **Weight** | 100 to 900 | 500 |
| **Letter-spacing** | −0.05 to 0.20 em | 0.00 em |
| **Line height** | 1.10 to 2.00 | 1.50 |
| **Viewing condition** | 5 options | **Normal indoor** |
| **Sample content** | 5 options | **Body paragraph** |

## Outputs and exports

| Output | Format | What it contains |
|---|---|---|
| **Copy CSS** (gold button) and **CSS for the type** | CSS | A `.readable-text` rule with the font family, size, weight, letter-spacing, line height, colour and background (and tabular numerals for **Tabular numbers**), and a comment with the Lc, the level needed, the ratio and "comfort 38/100, house heuristic". |
| **JSON report** | JSON | The colours, font, size, weight, letter-spacing, line height, condition and sample; the APCA Lc clean and under the condition; the level needed; the WCAG ratio, threshold and result; the score and its word; "method": "house heuristic, not a standard"; each factor's points; and the recommendations. |
| **Save setting** | A palette in your Library | Named "Type setting · Manrope 16 px/500", with the colours, score and condition. |
| **Share link** | URL | `?ctool=type` with `color` and `on`, and any setting that is not the default. |

**Open in another tool** offers **Contrast System** (score the pair and find the nearest AA shade), **Accessibility Lab** (the pair under seven kinds of vision), **Animation Contrast**, **Harmony Studio** and **Color Inspector**, each with the text colour.

## Link keys

| Key | What it sets | Values |
|---|---|---|
| `color` | The text colour. | A colour |
| `on` (or `bg`) | The background. | A hex code |
| `font` | The font. | `sans` (default), `serif`, `mono`, `thin`, `rounded` |
| `px` | The size. | 10 to 48 |
| `weight` | The weight. | 100 to 900 |
| `track` | The letter-spacing, in em. | −0.05 to 0.2 |
| `lh` | The line height. | 1.1 to 2 |
| `cond` | The viewing condition. | `normal` (default), `v2040`, `v2080`, `glare`, `tired` |
| `sample` | The sample content. | `body` (default), `ui`, `button`, `long`, `data` |
| `ctab` | The tab to open on. | `verdict` (default), `sweeps`, `conditions`, `recs` |

Settings left at their defaults are left out of shared links, so links stay short.

## Accuracy and limits

- **The comfort score is a house heuristic.** It weighs contrast, size, weight, font, spacing and viewing condition to help you compare settings. It is not a standard or a measurement of real readers.
- **APCA is a guide.** The levels follow APCA's published bronze guidance, which WCAG 3 may adopt; WCAG 3 is still a draft. For a WCAG 2.2 check, use the **WCAG 2.x** value.
- **Weights 500, 600, 800 and 900** are read as 400 or 700, and lighter weights one level stricter; that last rule is the tool's own.
- **Conditions are simulations.** Blur is shown with a CSS blur, and glare and tiredness as a white veil mixed into both colours. They illustrate the effect; they are not medical models of vision.
- **Fonts depend on your device.** **Rounded — system rounded** draws the system's rounded face only where one exists. Manrope has no 100 or 900 cut, so those weights draw at the nearest one.
- **Lc is cut towards zero** and ratios rounded down, so a value never shows a level it misses. On **Conditions**, the Lc is shown without its sign.

## Related

- [Colour Tools documentation](README.md)
- [Open the Colour Tools and work in their panels](launcher-and-panels.md)
- [Contrast System](contrast-system.md) — scores and fixes for several text colours
- [Accessibility Lab](accessibility-lab.md) — a whole palette under seven kinds of vision
- [Font Library](../../../font-library/README.md) — choose a real typeface
- [Basic Color Tools](../../README.md)
