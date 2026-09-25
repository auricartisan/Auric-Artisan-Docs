---
title: Color Science Lab — The Workbench
description: Resolve one colour into CIE XYZ, xyY, Lab, LCh, Oklab, Oklch, sRGB, HSL and CMYK under a chosen illuminant, standard observer and adaptation transform, and see its gamut and how it shifts under other lights.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# The Workbench

The Workbench takes one colour, the **specimen**, and computes it in nine notations at once, all from the same linear-light values. You can change the viewing conditions (the illuminant, the standard observer and the chromatic adaptation transform) and every row moves together. The page's own note under the board says: *Computed, not looked up.*

A few terms:

- **Illuminant**: a standard light defined by its white point, such as D65 (average daylight) or A (incandescent).
- **Standard observer**: the CIE's model of human colour matching over a 2° field (1931) or a 10° field (1964). Lab values depend on which one you use.
- **Chromatic adaptation transform**: a formula that predicts how a colour appears after the eye adapts to a different white. Bradford, CAT02 and CAT16 are three versions of the von Kries method.

## Layout

### Left: the controls

- **Specimen** (*sRGB in*): a large swatch, a HEX box, a colour well and eight preset swatches (#4F7FE0, #D3AF37, #2F6D3A, #C4562C, #8F3B22, #2B6F8F, #B0169A, #F0E6D2).
- **Observer** (*CIE standard*): **2° 1931** or **10° 1964**.
- **Illuminant** (*white point*): **D65**, **D50**, **D55**, **C**, **A**, **F2** and **F11**.
- **Adaptation** (*von Kries family*): **Bradford**, **CAT02** or **CAT16**. While the illuminant is D65, a note says no adaptation is applied: the transform only works once you move the white point.

### Centre: the results

**Resolved coordinates**, with a note naming the illuminant, observer and transform:

| Space | Coordinates | Note |
| --- | --- | --- |
| CIE XYZ | X, Y, Z | reference |
| CIE xyY | x, y, Y | chromaticity |
| `CIE L*a*b*` | L, a, b | illuminant and observer |
| CIE LCh | L, C, h | polar Lab |
| Oklab | L, a, b | perceptual |
| Oklch | L, C, h | polar Oklab |
| sRGB | R, G, B | display |
| HSL | H, S, L | cylindrical |
| CMYK | C, M, Y, K | naive, no profile |

**CIE 1931 chromaticity** plots the specimen on the xy diagram and gives x and y, with three figures: `CIE L*`, `C* ab` and **hue angle**.

### Right: gamut and other lights

- **Gamut** (*this colour*): **sRGB** (IEC 61966-2-1), **Display P3** (SMPTE RP 431-2), **Adobe RGB** (1998) and **Rec. 2020** (ITU-R BT.2020), each marked **inside** or with the ΔE of clipping. A HEX colour is always inside sRGB.
- **Under other light** (*ΔE00 vs the current illuminant*): every other illuminant with the ΔE 2000 shift the colour would undergo. Green below 3, amber 3 to 8, red above 8. Select a row to switch to that illuminant.

## How the numbers are computed

1. The specimen's sRGB values are decoded to linear light and converted to XYZ for D65 and the 1931 observer, where sRGB is defined.
2. If you choose another illuminant or the 10° observer, XYZ is adapted from D65 to that white with the chosen transform.
3. Lab and LCh are computed against the chosen white. Oklab and Oklch come straight from sRGB, as the Oklab definition specifies.

## Tasks

### Get print-condition Lab values

1. Enter your colour.
2. Select **D50** and **2° 1931**.
3. Choose the transform your workflow uses (Bradford is the common choice in ICC workflows).
4. Read the `CIE L*a*b*` row.

Result: Lab values relative to D50, as used in print.

### Check a colour's stability under shop lighting

1. Enter the colour.
2. Read **Under other light**. Large values under **A**, **F2** or **F11** mean the colour will look noticeably different under incandescent or fluorescent light.

Result: a quick risk check before choosing a surface or product colour.

## Controls

| Control | Values | Default |
| --- | --- | --- |
| Specimen HEX box | `#RRGGBB` (with `#`) | #4F7FE0, or your last specimen |
| Colour well | Any sRGB colour | Same |
| Preset swatches | 8 colours | — |
| **Observer** | 2° 1931, 10° 1964 | 2° 1931 |
| **Illuminant** | D65, D50, D55, C, A, F2, F11 | D65 |
| **Adaptation** | Bradford, CAT02, CAT16 | Bradford |
| **Under other light** row | Switches the illuminant | — |

## Related

- [Illuminants](illuminants.md)
- [Compare two colours](compare-two-colours.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
