---
title: Gamut Mapping — Reference
description: Every control, readout, option and export in the Gamut Mapping lab.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Gamut Mapping reference

Address: https://auricartisan.com/tool/general/colorimetry/gamut-map/

## The five colour spaces

| Space | White | Transfer curve used to decode HEX |
| --- | --- | --- |
| sRGB / Rec.709 | D65 | sRGB piecewise curve (IEC 61966-2-1) |
| Display P3 | D65 | sRGB piecewise curve |
| Rec. 2020 | D65 | BT.2020 curve |
| Adobe RGB | D65 | Power law 563/256 (about 2.2) |
| ProPhoto RGB | D50 | ROMM: power 1.8 with a linear toe |

The slice is drawn on the source space's white. A space with a different white is adapted onto it with the Bradford transform before its boundary is tested.

## Lab tab

### Controls

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| Base colour picker and HEX field | The colour to analyse, interpreted in the source space | Any six-digit HEX | #247DEB |
| **Random** | Picks a random base colour | Button | — |
| **Lightness Slice L\*** | The lightness of the a*b* slice | 5 to 95, step 1 | 65 |
| **Source** | The space colours come from | The five spaces | sRGB / Rec.709 |
| **Target** | The space colours go to | The five spaces | Display P3 |
| **Swap Source & Target** | Exchanges the two | Button | — |
| **Method** | The mapping method | Chroma compression, Clip in target RGB, Uniform RGB scale, Adapt white, then clip | Chroma compression |
| **Compression Strength** | How far chroma compression goes (used by chroma compression only) | 0 to 1, step 0.01 | 0.90 |
| **Resolution** | Sample grid for the slices | 60 to 512, step 20 | 120 × 120 |
| **Sampler** | How sample points are placed | Uniform grid; Stratified (2×2), randomly jittered; Halton (base 2/3), a low-discrepancy sequence | Uniform grid |
| **Adaptive edge refinement** | Shown but not applied in the current version | On or off | Off |
| **Mark out-of-gamut in source** | Draws the target's boundary on the source slice | On or off | On |
| **Show base colour on slice** | Rings the base colour on the source slice | On or off | On |
| **Hue tick lines** | Draws radial lines every 30° of hue | On or off | Off |
| **Gamut boundary outlines** | Outlines the source boundary on the source slice and the target boundary on the mapped slice | On or off | On |
| **Axes & labels** | Shown but not applied; axes are always drawn | On or off | On |
| ΔE Playground **A** | First colour (picker and HEX field) | Six-digit HEX | #735244 |
| ΔE Playground **B** | Second colour | Six-digit HEX | #3BB273 |
| ΔE formula menu | Shown but does not change the readout; all three formulas are always listed | ΔE₀₀, ΔE*₉₄, ΔE*₇₆ | ΔE₀₀ |

### Readouts

| Readout | What it shows |
| --- | --- |
| **Base Colour Info** | L*, a*, b*, C*, h°, and whether the colour is in the source and in the target (Yes or OOG) |
| **Source Slice** | Colours inside the source gamut at the chosen L*, painted in sRGB, a* and b* from −128 to +128. Click to probe |
| **Mapped to Target** | The source-gamut colours mapped into the target. In the current version this slice always uses chroma compression to the boundary, whatever the method and strength |
| Statistics line | L*, the source and target slice areas (in a*b* units), their ratio as a percentage, the method and the sampler with its resolution |
| Provenance line | The transfer curve, the white the Lab values are referenced to, and the method |
| **Probe Point** | L*, a*, b*, C*, h°, sRGB, HEX, and whether the point is in the source and the target |
| **Before / After (12 Test Colours)** | #FF0000, #00FF00, #0000FF, #FFFF00, #FF00FF, #00FFFF, #FF8800, #88FF00, #0088FF, #FF0088, #8800FF and #00FF88, before (left) and after (right) mapping with your method and strength |
| ΔE Playground result | ΔE₀₀ with its verbal band, ΔE*94 and ΔE*76 |

ΔE₀₀ verbal bands: below 1 Imperceptible; below 2 Barely perceptible; below 3.5 Noticeable; below 5 Significant; 5 and above Very different.

## Boundary tab

| Control or readout | What it does | Values | Default |
| --- | --- | --- | --- |
| **Spaces on the plot** | Toggles each space on the boundary tiles | Five chips | sRGB and Display P3 on |
| Boundary tiles | a*b* boundaries at L* 20, 40, 65, 80 and 90 on one shared scale | — | — |
| **Volume samples** (n) | Monte Carlo samples per space | 5,000 to 200,000, step 5,000 | 20k |
| **Measure the five** | Estimates every space's CIELAB volume | Button | — |
| Volume table | Space, White, Lab volume ± 1 SE, vs sRGB, Sample box | — | — |

## Methods tab

| Control or readout | What it does | Values | Default |
| --- | --- | --- | --- |
| **Compare on** | The colours the figures are computed on | The base colour; 12 probe colours | The base colour |
| Method rows | Name, what it does, tag "this tool", explanation, and mean ΔE₀₀, max ΔE₀₀ and out-of-gamut count | — | The Lab's method open |
| **Provenance** | Count of published intents (0) and this tool's methods (4) | — | — |

## Data tab

| Dataset | Status |
| --- | --- |
| Primaries, 5 RGB spaces | Verbatim |
| White points D65 and D50 | Verbatim |
| Transfer functions, 5 spaces | Computed |
| Bradford adaptation matrix | Verbatim |
| Gamut boundary, a*b* slice | Computed (360 hues per L*, 24 bisection steps) |
| ΔE₀₀, ΔE94, ΔE76 | Computed |
| Gamut volume in CIELAB | Computed (uniform Monte Carlo in a fitted box) |
| ICC perceptual and saturation tables | Absent |
| Reference gamut-mapping results | Absent |

**Status** chips filter the list (**All**, **Verbatim**, **Computed**, **Absent**). The **Install a table** area ("Drop a CSV, JSON or ICC profile") does not load files in the current version.

## Export tab

| Control | Output |
| --- | --- |
| **Source slice, PNG** | `gamut-map-gm-canvas-src.png` |
| **Mapped slice, PNG** | `gamut-map-gm-canvas-dst.png` |
| **Everything as JSON** | `gamut-map-config.json` with `sourceSpace`, `targetSpace`, `intent`, `strength`, `lStar`, `resolution`, `sampler`, `timestamp` |
| Link field, **Link**, **Copy** | A URL with `src`, `dst`, `int` (method), `l` (L*), `res`, `sam`, `str` and `hex` |
| **Map a list of colours at once**, **Run the list** | Table of Input, Output, OOG, ΔE₀₀ and Lab for up to 50 colours, with a summary |

Method values in the link: `compress`, `clip`, `scale`, `adapt-clip`. Sampler values: `grid`, `stratified`, `halton`. Space values: `sRGB`, `P3`, `Rec2020`, `AdobeRGB`, `ProPhoto`.

## Reference tab

| Control | What it does |
| --- | --- |
| **Standards**, **Formulas**, **Citations**, **Research notes** | Switch sections; each shows a count |
| **Filter** | Searches all four; `Esc` clears it |

Standards: IEC 61966-2-1 (sRGB), SMPTE ST 432-1 (Display P3), ITU-R BT.2020-2, Adobe RGB (1998), ProPhoto RGB (ROMM), ICC.1:2022 rendering intents, ISO 11664-6 (CIEDE2000) and CIE 15:2018, each with a badge read from the data register. Formulas: hard clip, chroma compression, uniform scaling, Bradford adaptation plus clip, boundary bisection, RGB–XYZ matrix derivation, ΔE formulas, and the Halton and stratified samplers. Some research notes use the older intent names and mention area comparisons that have moved to the Boundary tab; the Methods tab reflects the current methods.

## Save to Library

The floating **Save to Library** button stores a snapshot of the first slice image in your Library.
