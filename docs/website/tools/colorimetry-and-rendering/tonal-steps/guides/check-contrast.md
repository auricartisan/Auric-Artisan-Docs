---
title: Tonal Steps — Check contrast
description: Read every ramp step's WCAG 2.2 ratio and rating and its APCA-W3 Lc against white, black or the base colour.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Check contrast

## Two measures

- **WCAG 2.2 contrast ratio** — (L1 + 0.05) ÷ (L2 + 0.05), lighter over darker, where L is relative luminance. Thresholds: 3:1 for large text (AA large), 4.5:1 for normal text (AA), 7:1 for enhanced (AAA).
- **APCA Lc** (APCA-W3 0.1.9) — a perceptual contrast value that treats dark-on-light and light-on-dark differently. It is signed: the sign tells you which way round the pair is. APCA is a working draft of what WCAG 3 may adopt, not a ratified requirement.

## Steps

1. Build your ramp on the **Lab** tab.
2. Open the **Contrast** tab.
3. Under **Against**, choose **White** (default), **Black** or **The base** (your base colour). The caption changes to "Every step against white", and so on.
4. Read the table:

| Column | Meaning |
| --- | --- |
| **Step** | The step's swatch and HEX |
| **WCAG** | The ratio, for example 4.63:1 |
| **Rating** | **AAA** (7 and above), **AA** (4.5 and above), **AA large** (3 and above) or **Fail** |
| **APCA Lc** | The signed Lc, to one decimal |

5. Under **Superseded APCA**, choose **Show the difference** to add two columns: **Superseded** (the approximate figure an earlier version of the page computed) and **Difference**. Differences of 1 Lc or more are highlighted. Choose **Hide** to remove them (the default).
6. Look at **The ladder** for a chart of the steps' contrast.

The **Metric** choice (**WCAG 2.2** or **APCA**) does not change the table in the current version; both figures are always shown.

## Reading the result

- Pick text and background steps whose WCAG rating meets your target (AA for body text is the usual minimum).
- For APCA, larger absolute Lc means more contrast. Common reference levels are Lc 45, 60, 75 and 90, used by APCA guidance for progressively smaller or thinner text.
- The difference column shows why the correction mattered: under 0.3 Lc through the mid-range, 8 at black against white, and up to 20 against black.

## Tips

- Each step row on the Lab tab already shows its ratio against white; the Contrast tab adds black, the base and APCA.
- The contrast table export on the Export tab lists every step's WCAG ratio and APCA Lc against both white and black, whichever **Against** you chose here.
- For checking a single text and background pair in depth, use the [Contrast Checker](../../../accessibility-and-vision/contrast-checker/README.md).

## Result

You know which steps of your ramp pass WCAG AA or AAA, and their APCA Lc, against white, black or your base colour.
