---
title: Type Readability Sim — Predict reading comfort for text on a colour
description: Combine text and background colours with font style, size, weight, letter-spacing and a viewing condition to get an APCA reading, a comfort score, size and weight sweeps, and recommendations.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Type Readability Sim

A contrast ratio on its own does not tell you whether text will be comfortable to read. The same colour pair can be easy at 24 pixels and bold, and hard at 12 pixels and light. Viewing conditions matter too: blur from low vision or glare on a screen eats into the margin.

Type Readability Sim puts these together. You choose a text colour, a background, a font style, size, weight and letter-spacing, and a viewing condition. It reports the APCA contrast and the minimum the APCA guidance asks for at that size and weight, a comfort score from 0 to 100, the WCAG ratio, a live preview, two sweeps across sizes and weights, and practical recommendations.

Type Readability Sim is in the launcher's **Essentials** group.

## Open it

Open the launcher and select **Type Readability Sim**. See [Open the Colour Tools](launcher-and-panels.md). The text starts white (#FFFFFF). The background starts as the colour you opened the tool with, or a deep navy (#1A1A2E).

## Screen tour

### Sidebar

- **Text** and **Background**: colour fields.
- **Font**: one of five font styles.
- **Size** (shows the current value, for example **Size · 16px**), **Weight** and **Letter-spacing** sliders.
- **Viewing condition**.
- **Sample content**.

### Main area

1. **Reading comfort** (*Composite estimate*): three meters.
   - **Comfort**: a score out of 100 with a bar and a label.
   - **APCA Lc**: the absolute Lc value, *Needs N for this size/weight*, and **Passes tier** or **Below tier**.
   - **WCAG 2.x**: the ratio, the levels for body and large text, and **Passes** or **Fails**.
2. **Live preview**: your sample text drawn with all your settings, under the chosen viewing condition. The heading shows the font style, size and weight.
3. **Size sweep**: *The quick brown fox* at 12, 14, 16, 18, 24 and 32 pixels in your weight, each marked **OK** or **fail**.
4. **Weight sweep**: the same text at your size in weights 300 to 800, each marked **OK** or **fail**.
5. **Recommendations** (*Strongest fix first*): up to four suggestions, or a note that the pair passes all checks.

## Options

### Font

| Option | Font stack used |
| --- | --- |
| **System sans (Inter-like)** | Your system's interface sans-serif |
| **Humanist (Georgia-like)** | Georgia or a similar serif |
| **Monospace (JetBrains-like)** | JetBrains Mono or your system monospace |
| **Display thin** | Bodoni Moda, Didot or a similar high-contrast serif |
| **Rounded (Quicksand-like)** | Quicksand, Avenir Next, Nunito or your system sans |

The preview uses fonts installed on your device; if a named font is not available, your browser falls back to a similar one. Each style also changes the comfort score slightly: the thin display style scores lower, the humanist style a little lower, and monospace a little higher.

### Viewing condition

| Option | Effect on the preview | Effect on the score |
| --- | --- | --- |
| **Normal vision · indoor** | None | None |
| **Low vision 20/40 (blur 0.6px)** | 0.6-pixel blur | −12 |
| **Low vision 20/80 (blur 1.8px)** | 1.8-pixel blur | −28 |
| **Bright glare (10% white veil)** | A 10 % white veil | −8 |
| **Tired eyes (blur 0.3px + 5% veil)** | 0.3-pixel blur and a 5 % white veil | −4 |

### Sample content

| Option | Text |
| --- | --- |
| **Body paragraph** | The quick brown fox jumps over the lazy dog, letters and digits |
| **UI label / button** | Save changes, Continue, Cancel, Sign out |
| **Long-form (4 sentences)** | A short passage about readability, long enough to feel fatigue |
| **Tabular / numeric** | A row of revenue and percentage figures |

## How the numbers work

- **APCA Lc** is the Accessible Perceptual Contrast Algorithm's lightness contrast; only its size matters here.
- **Needs** is the minimum Lc from the APCA size and weight table (the same table as the [Contrast System](contrast-system.md) APCA Guide), blended between the nearest sizes and weights. When a size and weight is not usable at any contrast, it shows **—**.
- **Comfort** starts at 50, adds 0.9 points for every Lc above the requirement (and subtracts below it), adds a little for larger sizes and heavier weights, subtracts the viewing-condition penalty, adjusts for the font style, and is kept between 0 and 100.

| Comfort score | Label |
| --- | --- |
| 85 and above | **Effortless** |
| 65 to 84 | **Comfortable** |
| 50 to 64 | **Legible** |
| 35 to 49 | **Strained** |
| Below 35 | **Unreadable** |

The comfort score is the tool's own heuristic, tuned to APCA. It is not a published standard.

## Tasks

### Check whether small text is comfortable

1. Set **Text** and **Background** to your colours.
2. Set **Size** to your caption size, for example 12 pixels, and **Weight** to its weight.
3. Read **Comfort** and the **APCA Lc** meter.
4. Look at **Size sweep** to see from which size the pair passes.

Result: you know whether the text is comfortable at that size, and the smallest size that passes.

### Test under reduced vision

1. Change **Viewing condition** to **Low vision 20/40 (blur 0.6px)**, then **Low vision 20/80 (blur 1.8px)**.
2. Watch the preview blur and the **Comfort** score drop.
3. If the score falls to **Strained** or below, read **Recommendations**.

Result: an idea of how much safety margin the pair has.

### Follow a recommendation

The recommendations can include:

- *Raise contrast by ~N Lc — current pair fails the size/weight tier.*
- *Bump size to N px — passes at current weight.* (the next table size that passes)
- *Bump weight to N — passes at current size.* (the next weight that passes)
- *Try text color #HEX — would pass current size/weight.* (the text colour's OKLCH lightness moved away from the background until it passes)
- *Under reduced vision, padding contrast above the minimum tier improves reading speed.* (shown for any viewing condition other than normal when the margin is under 15 Lc)

Apply a suggestion by changing the slider or typing the suggested colour into **Text**.

Result: the meters turn to **Passes tier** and the comfort label improves.

## Controls

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| **Text** | Text colour | HEX, colour well, dice | #FFFFFF |
| **Background** | Background colour | HEX, colour well, dice | The colour you opened with, or #1A1A2E |
| **Font** | Font style | 5 styles | System sans (Inter-like) |
| **Size** | Font size | 10 to 48 px, step 1 | 16 px |
| **Weight** | Font weight | 100 to 900, step 100 | 500 |
| **Letter-spacing** | Tracking | −0.05 em to 0.20 em, step 0.01 | 0.00 em |
| **Viewing condition** | Simulated condition | 5 options | Normal vision · indoor |
| **Sample content** | Preview text | 4 options | Body paragraph |

Letter-spacing changes the preview only; it does not change the scores.

## Outputs and exports

The tool has no export. Copy colours from the colour fields.

## Accuracy and limits

- The APCA values use a simplified form of a draft method, and the size and weight table is guidance, not a standard.
- The comfort score is a design heuristic, not a measurement of reading speed or a clinical test.
- Blur and veil effects are illustrations of low vision and glare; real vision loss varies a great deal.
- Fonts render with what is installed on your device, so the preview can differ from the font you plan to use.

## Related

- [Colour Tools documentation](README.md)
- [Contrast System](contrast-system.md)
- [Accessibility Lab](accessibility-lab.md)
- [Font Library](../../../font-library/README.md) to choose a real typeface
- [Basic Color Tools](../../README.md)
