---
title: Color Library — Find a colour's nearest neighbours
description: Paste a colour in any CSS format and read the five catalogued colours closest to it, with their distance and contrast.
product: Website › Library › Colour libraries › Color Library
updated: 2026-09-25
---

# Find a colour's nearest neighbours

The **Start from a colour you already have** section answers the question most people arrive with: "I have this colour — what is it, and what can it do?" It finds the five atlas colours closest to yours and shows what each of them carries.

## Steps

1. Select the field under **Start from a colour you already have**. It starts with `#D3AF37`.
2. Replace the value with your colour. You can type or paste it in any of these forms:
   - hex, with or without `#`, in 3, 4, 6 or 8 digits: `#76cdf6`, `76cdf6`, `#abc`;
   - `rgb()` or `rgba()`: `rgb(118 205 246)`, `rgb(118, 205, 246)`;
   - `hsl()` or `hsla()`: `hsl(199 88% 71%)`;
   - `hwb()`: `hwb(199 46% 4%)`;
   - `lab()` and `lch()`: `lab(78.6 -15.2 -28.2)`, `lch(78.6 32 241)`;
   - `oklab()` and `oklch()`: `oklab(0.81 -0.07 -0.08)`, `oklch(0.81 0.1 230)`;
   - `color()` in the `srgb`, `srgb-linear` or `display-p3` space: `color(display-p3 0.5 0.8 0.95)`;
   - any of the 148 CSS colour names, such as `rebeccapurple`;
   - three bare numbers read as RGB: `118 205 246`.
3. Select **Find its neighbours**, or stop typing for a moment. The swatch beside the field changes to your colour and the results update.
4. Read the results (described below).
5. To learn more about one of the matches, select its cell. The **The colour** tab opens with that colour's full record.

**Result:** six cells in a row — your colour first, then the five nearest atlas colours in order of distance — and a sentence about the neighbourhood.

## Reading the results

### The heading line

**Nearest in the atlas** is followed by a note such as **Read as oklch. Distance is ΔE in CIE Lab; under 2.3 is a difference most eyes will not see.**

- **Read as** names the format the page recognised: `hex`, `named`, `rgb`, `hsl`, `hwb`, `lab`, `lch`, `oklab`, `oklch`, `color(srgb)`, `color(srgb-linear)` or `display-p3`. Check it if the result surprises you.
- If your colour lies outside the sRGB range a screen can show (for example a very saturated `oklch()` or `display-p3` value), the note adds **outside sRGB, brought to the edge of it**. The page moved your colour to the nearest displayable colour before matching, and it tells you so rather than doing it silently.

### The cells

| Cell | What it shows |
|---|---|
| First cell | Your colour's hex code, the note **your colour**, and its contrast **On white** and **On black** |
| Next five cells | An atlas colour's hex code, its distance from yours (for example **ΔE 3.41 — a close match**), and its contrast **On white** and **On black** |

Contrast ratios of 4.5:1 or more are marked as passing; lower values are marked as failing. 4.5:1 is the WCAG AA threshold for normal-size text.

The word after each ΔE value describes the size of the difference:

| ΔE | Word shown |
|---|---|
| Under 2.3 | **indistinguishable** |
| 2.3 to under 5 | **a close match** |
| 5 to under 10 | **visibly different** |
| 10 or more | **a different colour** |

ΔE is the straight-line distance between two colours in CIE Lab (the CIE76 formula). A value around 2.3 is often quoted as a just-noticeable difference.

### The sentence under the cells

The page averages the five neighbours' contrast and writes one of three sentences:

- **Colours around this one average N:1 on white — it is a colour you can write in on a light page.** The neighbourhood averages at least 4.5:1 on white.
- **Colours around this one average N:1 on white and N:1 on black. This is a colour to draw with on a light page, and to write in on a dark one.** It fails on white but averages at least 4.5:1 on black.
- **Colours around this one clear neither white nor black as body text. It is decoration wherever it lands.**

## If the field does not accept your colour

When the text is not a colour the page can read, the results are replaced by: **Not a colour this reads. It takes #76cdf6, rgb(118 205 246), hsl(199 88% 71%), hwb(199 46% 4%), lab(78.6 -15.2 -28.2), lch(78.6 32 241) and the rest of the CSS colour formats.** An empty field shows nothing.

Common causes are a missing closing bracket, a `color()` space other than the three listed above, or a CSS variable such as `var(--brand)`. See [Troubleshooting](troubleshooting.md).

> **Note:** Transparency is ignored. A colour with an alpha value, such as `#76cdf680` or `rgb(118 205 246 / 50%)`, is matched as the solid colour.

> **Tip:** Hues in `hsl()`, `hwb()`, `lch()` and `oklch()` can be written in degrees, `rad`, `grad` or `turn`. Percentages work wherever CSS allows them.
