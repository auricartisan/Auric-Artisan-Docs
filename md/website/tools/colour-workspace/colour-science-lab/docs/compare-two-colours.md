---
title: Color Science Lab — Compare two colours
description: Measure the difference between a reference and a candidate colour with ΔE 2000, ΔE 1994, ΔE 1976 and Oklab distance, and see whether the gap is lightness, chroma or hue.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Compare two colours

The **Compare** view measures how different two colours are. It is useful for checking a match (a print against a screen colour, a paint against a brand colour, a new token against an old one) and for understanding why two colours look different.

**ΔE** (delta E) is a number for colour difference. Several formulas exist; newer ones follow human perception more closely.

## Layout

Two cards side by side:

- **Reference** (**A**) and **Candidate** (**B**), each with a large swatch, a HEX box, a colour well, and a table of **CIE XYZ**, **CIE Lab**, **CIE LCh** and **Oklab** coordinates.

The Reference starts as the Workbench specimen; the Candidate starts as #5A86D8.

Below them, four verdicts:

| Verdict | Meaning |
| --- | --- |
| **ΔE 2000** | The current CIE standard (CIEDE2000). Its note says whether the difference is below the just-noticeable threshold (under 1), noticeable only side by side (1 to 2), perceptible at a glance but acceptable side by side (2 to 5), or two different colours (5 and above). |
| **ΔE 1976** | The original straight-line Lab distance. It overstates differences in blues, which is why it was replaced. |
| **ΔE 1994** | The step between the two: it weights chroma by its own size. |
| **Oklab distance** | Plain distance in Oklab, a space designed to make that distance meaningful. |

Each figure is green (small), amber or red (large).

**Where the difference sits** splits the gap into **Δ lightness**, **Δ chroma** and **Δ hue angle**, and a sentence says which dominates: lightness (match L first), chroma (same hue, different saturation) or hue (genuinely different colours).

## Tasks

### Check whether a match is close enough

1. Enter the target in **Reference** and the sample in **Candidate** (HEX with `#`, or the colour well).
2. Read **ΔE 2000**. Under 1 is effectively identical; under 2 is usually acceptable for close work; above 5 is a clear mismatch.
3. Read **Where the difference sits** to know what to adjust.

Result: a measured, explained difference.

## Controls

| Control | Values | Default |
| --- | --- | --- |
| **Reference** HEX box and colour well | `#RRGGBB` | The Workbench specimen |
| **Candidate** HEX box and colour well | `#RRGGBB` | #5A86D8 |

Lab values here use D65 and the 2° observer.

## Related

- [The Workbench](workbench.md)
- [Quick Converter's Compare tab](../../basic-colour-tools/docs/panel-tools/quick-converter.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
