---
title: Auric Color — Colour vision
description: Preview colours and your project palette under colour-vision deficiencies, and understand colour-vision risk and confusable hues.
product: VS Code extensions › Auric Artisan Studio › Auric Color
updated: 2026-09-25
---

# Colour vision

Colour-vision deficiency (CVD), often called colour blindness, makes some colours hard to tell apart. Colours that look clearly different to you can look alike to someone with a CVD. Auric Color shows you how your colours look and warns when a design relies on hue alone.

## The simulations

| Type | What it means |
| --- | --- |
| Protanopia | No red cones (about 1% of men) |
| Protanomaly | Weak red |
| Deuteranopia | No green cones (about 1% of men) |
| Deuteranomaly | Weak green; the most common form, about 5% |
| Tritanopia | No blue cones; rare |
| Tritanomaly | Weak blue |
| Achromatopsia | Total colour blindness |
| Achromatomaly | Partial colour blindness |

Simulations use the Brettel 1997 method in linear light, which keeps white white and does not brighten reds. They are previews for design decisions, not a diagnosis or a medical measurement.

## The Vision tool

Open the Studio's **Color › Vision**, select **Vision** in a colour hover's **Open in Studio** row or on the Overview, or choose **Open Studio: Vision** in the Command Center.

- **Color-vision simulation:** enter a colour to see it as a swatch next to all eight simulations. Hover a swatch for its simulated hex; select it to copy.
- **Project palette under color-blindness** (after a project scan): your 16 most used colours in four rows, for typical vision, protanopia, deuteranopia and tritanopia. Hover a cell to see the original and simulated hex.

## Colour vision elsewhere

| Where | What you see |
| --- | --- |
| Colour hover | The colour next to its protanopia, deuteranopia and tritanopia versions |
| Contrast diagnostics | A hint when a pair passes normally but its contrast falls below the target under protanopia, deuteranopia or tritanopia |
| Colour-vision risk hovers | The pair drawn for typical vision, protan, deutan and tritan, with each ratio |
| Palette and Brand tools | A **Preview as** or vision dropdown that shows every swatch or surface as seen with a CVD |
| Preview tool (Auric Accessibility) | A **Vision** dropdown for the before-and-after surfaces |
| Project scan | **Confusable colors** (Project Issues) and **Confusable hues** (Studio Findings) |

### Colour-vision risk

A pair is a colour-vision risk when it meets its contrast target for typical vision, but its worst ratio under protanopia, deuteranopia or tritanopia falls below the target. Such pairs are shown as hints (`[WCAG 1.4.1]`, Use of Color) and reduce the contrast sub-score by up to 10 points. The fix is to increase the difference in lightness, or to add a cue that is not colour, such as an icon, text or underline.

Turn the hints off with `auricColor.contrast.flagCvdRisk` (or `auricA11y.contrast.flagCvdRisk`).

### Confusable hues

After a project scan, the Studio compares your most used chromatic colours in pairs. A pair is **confusable** when the two look clearly different to typical vision (colour difference of at least 12) but become hard to tell apart under protanopia, deuteranopia or tritanopia (difference below 9). Up to 12 such pairs are listed, most confusable first, with both colour differences and the simulation that merges them. Use stronger lightness contrast, shape, text or icons to tell those states apart.

## Related

- [Contrast diagnostics](contrast-diagnostics.md)
- [Palettes and shades](palettes-and-shades.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
