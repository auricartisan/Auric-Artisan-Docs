---
title: HDR Gamut Plot — Reference
description: Every control, readout, option and export in the HDR Gamut Plot.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# HDR Gamut Plot reference

Address: https://auricartisan.com/tool/general/gamut-and-rendering/hdr-gamut-plot/

## Lab tab

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Working colour space** | Shown on the page, but in the current version it does not change the diagram or figures | sRGB / Rec.709 (BT.709); Display-P3 (D65); Rec.2020 (BT.2020) | Rec.2020 |
| **Overlay gamuts** | Shows or hides each triangle (also used by the Planes tab) | Rec.709 / sRGB, Display-P3, Rec.2020 | All on |
| **Spectral locus** | Draws the locus | On or off | On |
| **Line of purples** | Draws the straight edge of the locus | On or off | On |
| **ICtCp marker** | Shown, but draws nothing in the current version | On or off | Off |
| **Chromaticity axes** | The diagram's plane | CIE 1931 xy; CIE 1976 u′v′ | CIE 1931 xy |
| **Standard observer** | Shown, but the locus is always the CIE 1931 2° observer's | CIE 1931 2° (Standard); CIE 2015 10° (Revised) | CIE 1931 2° |
| **Drop a PNG or JPEG** | Opens a file picker and measures the image's gamut occupancy | Image files; reduced to at most 1,024 pixels a side | — |

| Readout | What it shows |
| --- | --- |
| **Gamut chromaticity diagram** | The triangles, locus, purples line and D65 marker; the axis name is shown over it |
| Hover line | Coordinates, XYZ at Y = 0.35, L*, and I, Ct, Cp at the PQ luminance of the Signal level |
| **Gamut metrics** | Space, Primaries, White, Share of locus, Area, in the plane on screen |
| Image results | Size analysed, pixels sampled, distinct chromaticities, occupancy of each gamut, and a note |

## Curves tab

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Peak brightness** | The display peak L_W: scales display-referred curves and sets HLG's system gamma; does not scale PQ | 100 to 10,000 nits, step 50 | 1000 |
| **Tone curve** | The curve drawn and used for the Signal level | Gamma 2.2 (SDR); Gamma 2.4 (BT.1886, zero black); PQ (ST.2084); HLG (BT.2100) | PQ |
| **HLG environment** | Surround factor for HLG's system gamma | Reference dark (×1); Dim surround (×0.95); Bright surround (×0.90) | Reference dark |
| **Signal level** | A signal value to convert to absolute luminance | 0 to 1, step 0.01 | 0.5 |

| Readout | What it shows |
| --- | --- |
| γsys | HLG system gamma at the current peak and surround |
| Surround note | Whether the HLG reading is BT.2100's own or adjusted |
| **I =** | The ICtCp intensity of the signal's absolute luminance |
| **Tone curve output** | Signal against cd/m² (log), with a peak label |
| Curve rows | One per curve, tagged Absolute, Display-referred or Adjusted, with its defining document and details |
| **EOTF Comparison — PQ vs HLG vs sRGB** | All three on one log-nits axis, drawn at page load |

## Planes tab

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Perceptual plane** | The space for the plane and rings | ICtCp (Ct–Cp); JzAzBz (Az–Bz) | ICtCp |
| **Tone mapping operator** | Shown, but does not change any plot in the current version | Reinhard; Hable (Filmic); ACES Filmic; Uchimura (Gran Turismo) | Reinhard |
| **Boundary rings** | Key to the eight ring levels | 0.1, 1, 10, 100, 500, 1k, 4k, 10k nits | — |

| Readout | What it shows |
| --- | --- |
| Plane | Gamut boundaries at the Signal level's absolute luminance |
| **Boundary rings by luminance** | Boundaries at the eight levels for each gamut switched on in the Lab |

## Data tab

| Dataset | Status |
| --- | --- |
| Primaries and white, 3 spaces | Verbatim |
| Spectral locus (65 xy pairs, 380–700 nm) | Verbatim |
| PQ transfer (ST 2084 constants as rationals) | Verbatim |
| ICtCp matrices (BT.2100) | Verbatim |
| HLG transfer (with the OOTF) | Computed |
| JzAzBz (Safdar et al. 2017, own quantiser) | Computed |
| Gamut area and share | Computed |
| Tone-mapping operators (four curves) | Computed |
| HLG surround factor | Synthesised (this tool's own) |
| Image luminance | Absent: 8-bit PNG and JPEG carry none |

**Status** chips filter the list. **Install a table** ("Drop a CSV or JSON") does not load files in the current version.

## Export tab

| Control | What it does |
| --- | --- |
| **What to take** | **The measurements**, **The curve**, **The diagram**, **The curve plot**, **The plane**, **A link to this view** |
| **As** | Only the formats that fit (below) |
| **Download** (names the file) | Saves it; for the link, copies it |
| **Copy to clipboard** | Copies text payloads |
| **Exactly what you will get** | Preview of the payload and its size |
| **Convert a list**, **Convert to ICtCp**, **Download the result** | HEX conversion; the last button copies the result as CSV |
| **The three spaces, side by side** | Bar chart and table of Area, Share of locus and White |

| Choice | Format | File |
| --- | --- | --- |
| The measurements | CSV | `hdr-gamut.csv`: Space, Plane, Red x, Red y, Green x, Green y, Blue x, Blue y, White x, White y, Area, Locus share %, plus a footer naming the locus area, plane and observer |
| The measurements | JSON | `hdr-gamut.json`: per space label, primaries, white point, plane, area and locus share, and a `_meta` block (axes, peak, curve, locus area, observer, locus points) |
| The measurements | CSS | `hdr-gamut.css`: custom properties such as `--gamut-rec2020-locus-share`, `--gamut-rec2020-area`, the R, G and B primaries, `--gamut-plane`, `--gamut-locus-area`, `--hdr-peak-nits` and `--hdr-curve-type` |
| The curve | CSV | `hdr-curve-<curve>.csv`: 257 rows of signal and nits, with a footer |
| The diagram | PNG | `hdr-gamut-diagram.png` |
| The curve plot | PNG | `hdr-tone-curve.png` |
| The plane | PNG | `hdr-perceptual-plane.png` |
| A link to this view | Link | A URL with `axes`, `peak`, `curve` and `mode` (the perceptual plane) |

## Reference tab

| Control | What it does |
| --- | --- |
| **Standards**, **Formulas**, **Citations**, **Research notes** | Switch sections |
| **Filter** | Searches all four; `Esc` clears it |

Standards: ITU-R BT.2020, BT.2100, SMPTE ST 2084, ARIB STD-B67, ICtCp, Jzazbz, BT.709 and sRGB, and Display P3. Formulas: PQ, HLG OETF and OOTF, ICtCp, Jzazbz, gamut area and locus share, four tone-mapping operators, and xy/u′v′ conversion. Citations: 17 references. Research notes explain why a file has no nits, occupancy against coverage, the single locus denominator, absolute against display-referred curves, the surround factor, the two quantisers, and what "ACES" means here.

## Save to Library

The floating **Save to Library** button stores a snapshot of the diagram in your Auric Artisan Library.
