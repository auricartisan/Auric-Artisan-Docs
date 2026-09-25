---
title: M-Gradient Palette — Limits and accuracy
description: What the M-Gradient Palette measures, how precisely, the choices it makes, and what it does not hold.
product: Website › Tools › Image and file tools › M-Gradient Palette
updated: 2026-09-25
---

# Limits and accuracy

## What is measured, and how precisely

| Figure | Method | Accuracy |
|---|---|---|
| ΔE₀₀ per step | CIEDE2000 (ISO/CIE 11664-6:2014) between neighbouring steps, via CIELAB with a D65 white | Agrees with the 34 published test pairs of Sharma, Wu and Dalal (2005) to within 0.000042 |
| Evenness | Standard deviation of the step differences | Exact from the above |
| OKLab and OKLCH | Ottosson's published matrices | Checked against the article's own reference values |
| sRGB conversions | The piecewise sRGB transfer function, both directions | Exact |
| WCAG 2 ratio | (L₁ + 0.05) ÷ (L₂ + 0.05) from relative luminance | Exact: 21.00, 4.54 for `#767676`, 7.00 for `#595959` on white |
| APCA Lc | APCA-W3 0.1.9 with all its constants | Black on white 106.04 |
| Colour-vision view | Machado, Oliveira and Fernandes (2009), severity 1.0, in linear light | Full dichromacy only |
| Gamut mapping | Chroma halved towards the boundary 20 times, lightness and hue held | Far finer than one 8-bit step |

Every step is rounded to an 8-bit hex colour before it is measured, so the figures describe the colours you export.

## Choices the tool makes

These are listed as **This tool's choice** on the **Data** tab.

- **How out-of-gamut steps are brought back:** by reducing chroma, not by clipping channels. A different method gives a visibly different ramp.
- **The five easings** are CSS animation curves, not a colour standard.
- **Calling a ramp even:** there is no published threshold for evenness, so the tool ranks rows and marks the evenest rather than passing or failing them.
- **The 25 presets** are pairs someone liked; they carry no claim to be good ramps.

## What the tool does not hold

- **Colour-vision deficiency below full severity.** The simulation shows complete loss of one cone type only. Milder forms are more common and are not shown.

## Limits

- Two ends only; 2 to 32 steps.
- Only the OKLCH routes can go outside sRGB; the other routes always stay inside it.
- The CSS gradient export carries the ends and the space only, and depends on browser support.
- The APCA figure is a guide to legibility, and the Lc bands are APCA's own guidance, not a conformance level.
- Nothing is stored between visits.

## What it is not

The tool measures how evenly spaced and how legible a ramp is. It does not judge whether the colours suit your brand, and it does not test your final layout; check text in context at its real size.
