---
title: Color Space Converter — One colour in 34 colour-space notations
description: Convert one colour into 34 notations across eight groups, from HEX and HSL to Lab, OKLCH, Display P3, Rec.2020, ACEScg, JzAzBz and YCbCr, with gamut badges, two diagrams, channel bars and a JSON export.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Color Space Converter

Color Space Converter writes one colour in every colour space you are likely to meet, from web notations to scientific and broadcast ones: 34 notations in eight groups. Each row has a copy button, wide-gamut rows show whether the colour fits the space, and two diagrams place the colour on the CIE 1931 chromaticity chart and on an OKLab slice. A third tab shows the main channels as bars.

A **colour space** is a system of numbers that describes colours. Different spaces suit different jobs: HEX and RGB for screens and code, CMYK for print, Lab and OKLab for measuring how different colours look, P3 and Rec.2020 for wide-gamut screens, YCbCr for video. A **gamut** is the range of colours a space or device can represent.

Color Space Converter is in the launcher's **Deep dive** group.

## Open it

Open the launcher and select **Color Space Converter**, or pick it from the right-click menu's **Colour tools** group. See [Open the Colour Tools](launcher-and-panels.md). It starts with the colour you opened with, or gold (#D3AF37).

## Screen tour

### Sidebar

- **Color**: a colour field.
- A large chip showing the colour and its HEX code.
- Key figures: **Luminance** (WCAG relative luminance), **OKLCh L**, **Chroma**, **Hue°**, **Saturation** (HSL) and **CCT** (estimated colour temperature with a label).
- **Copy All (JSON)**.

### Main area tabs

| Tab | What it shows |
| --- | --- |
| **All Spaces** | A search box (*Search 30 spaces…*), a count, and the 34 notations in eight groups. |
| **Diagrams** | **CIE 1931 xy Chromaticity** and **OKLab a–b Gamut Plane**, plus six figures. |
| **Channels** | Bars for the channels of eight spaces. |

## The notations

| Group | Rows |
| --- | --- |
| **Web / Device-RGB** | HEX, HEX (short), RGB, RGBA, RGB % |
| **Cylindrical / Perceptual Device** | HSL, HSV / HSB, HWB, HSI |
| **Print / Subtractive** | CMYK, Linear sRGB |
| **CIE Standard** | XYZ D65, XYZ D50, Lab (D65), LCh (D65), Lab (D50), LCh (D50) |
| **Perceptual Uniform** | OKLab, OKLCh, CIELuv, LChuv |
| **Wide Gamut** | Display P3, Linear P3, Adobe RGB 1998, Linear AdobeRGB, Rec.2020, Linear Rec.2020, ACEScg (AP1) |
| **Scientific / Appearance** | Hunter Lab, IPT, JzAzBz |
| **Video / Broadcast** | YCbCr BT.709, YUV, YIQ (NTSC) |

Each group heading shows how many spaces it holds. The wide-gamut rows carry a badge: **✓ In** when all three channels are between 0 and 1, **! Out** otherwise.

What some of these are:

- **HWB**: hue, whiteness and blackness, a CSS colour notation.
- **HSI**: hue, saturation and intensity, used in image processing.
- **Linear sRGB**: sRGB with the gamma curve removed, so values are proportional to light.
- **XYZ D65 / D50**: CIE tristimulus values for a daylight (D65) or print-standard (D50) white.
- **Lab and LCh (D65 and D50)**: CIELAB and its cylindrical form. CSS `lab()` and `lch()` are defined relative to D50, so use the D50 rows for CSS.
- **OKLab and OKLCh**: a modern perceptual space where equal steps look roughly equal; CSS supports `oklab()` and `oklch()`.
- **CIELuv and LChuv**: another CIE perceptual space, used for lighting and displays.
- **Display P3, Adobe RGB 1998, Rec.2020**: wider-gamut RGB spaces for modern screens, photography and HDR video. The encoded rows use CSS `color()` syntax, such as `color(display-p3 …)`.
- **ACEScg (AP1)**: a linear space used in film and visual-effects rendering.
- **Hunter Lab**: an older opponent-colour space still used in some industries.
- **IPT** and **JzAzBz**: perceptual spaces from colour science research; JzAzBz is designed to also cover high dynamic range.
- **YCbCr BT.709**, **YUV**, **YIQ (NTSC)**: luma and colour-difference encodings used in video.

## Tasks

### Copy a colour in a particular notation

1. Set **Color**.
2. On **All Spaces**, type part of a name or value in the search box, for example `p3` or `lab`. Only matching rows show, and the count reads *N matching spaces*.
3. Select the copy button on the row. **Copied** appears.

The copied text sometimes differs slightly from the displayed text: for example HSL is copied with commas (`hsl(46.2, 63.9%, 52.2%)`) and the degree signs shown in LCh rows are left out, so the copied value is valid in CSS or code.

Result: the notation you need on your clipboard.

### Export every notation at once

Select **Copy All (JSON)**. A JSON object with one key per notation (for example `"hex"`, `"oklch"`, `"p3"`, `"rec2020"`) is copied, and **All spaces copied as JSON** appears.

```json
{
  "hex": "#D3AF37",
  "hex-s": "#D3AF37",
  "rgb": "rgb(211, 175, 55)",
  "oklch": "oklch(0.7655 0.1385 91.6)",
  "p3": "color(display-p3 …)"
}
```

The real output has all 34 keys.

### See where a colour sits

1. Open **Diagrams**.
2. **CIE 1931 xy Chromaticity** shows the horseshoe of visible colours, the white point (D65) as a small white dot, and four gamut triangles: **sRGB**, **P3**, **a98-RGB** and **Rec.2020**. Your colour is a ringed dot with guide lines.
3. **OKLab a–b Gamut Plane** shows a slice through OKLab at your colour's lightness (given as *L = N%*). The coloured area is the part of the slice that sRGB can show; the grey area is outside sRGB. Your colour is the ringed dot.
4. Under the diagrams, read **xy chromaticity**, **Y (luminance)**, **Rel. luminance**, **CCT**, **Temp. kind** and **Hue category**.

Result: you can see how close the colour is to the edge of sRGB, and how much room the wider gamuts leave.

### Compare channels

Open **Channels** to see bars for **sRGB (gamma-encoded, 0–255)**, **Linear-light sRGB (0–1)**, **HSL**, **OKLab (perceptually uniform)**, **OKLCh (cylindrical)**, **CIE XYZ D65**, **Display P3 (encoded, 0–1)** and **YCbCr BT.709 (0–1)**. Each bar shows the value as a number and as a filled length.

## Controls

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| **Color** | The colour to convert | HEX, colour well, dice | #D3AF37, or the colour you opened with |
| **Copy All (JSON)** | Copies all notations as JSON | 34 keys | — |
| Tabs | Switch view | All Spaces, Diagrams, Channels | All Spaces |
| Search box | Filters rows by name or value | Free text | Empty |
| Row copy button | Copies one notation | — | — |

## Accuracy and limits

- Every conversion starts from an 8-bit sRGB colour, so values are only as precise as that input. A colour chosen here is always inside sRGB, so the wide-gamut badges read **✓ In**; the badges are useful for colours near the edges and as a reminder of what each space can hold.
- D65 values use the sRGB white point directly. D50 values use a standard chromatic adaptation from D65.
- **CCT** uses a common approximation for light sources. It is meaningful for near-white and near-neutral colours and rough for saturated ones; some colours show *Indeterminate*.
- The chromaticity diagram's fill colours are approximate and clipped to what your screen can show.
- The scientific spaces (IPT, JzAzBz, Hunter Lab) follow their published formulas with standard assumptions (for example an absolute luminance for JzAzBz). Use a colour-science library for research-grade work.

## Related

- [Colour Tools documentation](README.md)
- [Quick Converter](../panel-tools/quick-converter.md), the fourteen-notation converter in the workspace
- [Color Inspector](colour-inspector.md)
- [Color Science Lab](../../../colour-science-lab/README.md)
- [Oklab and Oklch](https://auricartisan.com/library/learn/articles/2026-06-02-oklab-oklch-perceptual-color-spaces) on Learn
- [Basic Color Tools](../../README.md)
