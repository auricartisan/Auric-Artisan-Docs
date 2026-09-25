---
title: Gamut Lab — Reference
description: Every control, readout, option and export in the Gamut Lab.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Gamut Lab reference

Address: https://auricartisan.com/tool/general/gamut-and-rendering/gamut/

## The 13 standard spaces

| Space | Red (x, y) | Green (x, y) | Blue (x, y) | White (x, y) | Transfer |
| --- | --- | --- | --- | --- | --- |
| sRGB / BT.709 | 0.64, 0.33 | 0.30, 0.60 | 0.15, 0.06 | 0.3127, 0.329 | sRGB |
| Display P3 | 0.68, 0.32 | 0.265, 0.69 | 0.15, 0.06 | 0.3127, 0.329 | sRGB |
| DCI-P3 | 0.68, 0.32 | 0.265, 0.69 | 0.15, 0.06 | 0.314, 0.351 | Gamma 2.6 |
| Rec. 2020 | 0.708, 0.292 | 0.17, 0.797 | 0.131, 0.046 | 0.3127, 0.329 | BT.2020 |
| Rec. 2100 PQ | as Rec. 2020 | as Rec. 2020 | as Rec. 2020 | 0.3127, 0.329 | PQ |
| Rec. 2100 HLG | as Rec. 2020 | as Rec. 2020 | as Rec. 2020 | 0.3127, 0.329 | HLG (inverse OETF) |
| Adobe RGB | 0.64, 0.33 | 0.21, 0.71 | 0.15, 0.06 | 0.3127, 0.329 | γ 563/256 |
| ProPhoto RGB | 0.7347, 0.2653 | 0.1596, 0.8404 | 0.0366, 0.0001 | 0.3457, 0.3585 | ROMM |
| Adobe Wide Gamut | 0.7347, 0.2653 | 0.1152, 0.8264 | 0.1566, 0.0177 | 0.3457, 0.3585 | Gamma 2.2 |
| ACES 2065-1 (AP0) | 0.7347, 0.2653 | 0.0, 1.0 | 0.0001, −0.077 | 0.32168, 0.33767 | Linear |
| ACEScg (AP1) | 0.713, 0.293 | 0.165, 0.83 | 0.128, 0.044 | 0.32168, 0.33767 | Linear |
| NTSC 1953 | 0.67, 0.33 | 0.21, 0.71 | 0.14, 0.08 | 0.31, 0.316 | Gamma 2.2 |
| PAL/SECAM | 0.64, 0.33 | 0.29, 0.60 | 0.15, 0.06 | 0.3127, 0.329 | Gamma 2.8 |

**Custom** is a 14th option whose primaries you enter.

## Lab tab

### Controls

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Working color space** | Chooses the space shown in the panel and adds it to the diagram (up to five drawn) | The 13 spaces and Custom | sRGB / BT.709 |
| **Diagram mode** | How the main canvas draws | CIE 1931 xy; CIE 1976 u′v′; 3-D Wireframe (Lab) | CIE 1931 xy |
| **Standard observer** | Shown with two options, but only the CIE 1931 2° observer is used | CIE 1931 2°; CIE 1964 10° | CIE 1931 2° |
| **Spectral locus** | Draws the locus | On or off | On |
| **Grid** | Draws the grid | On or off | On |
| **MacAdam ellipses** | Draws 24 illustrative ellipses (a stand-in, see Limits) | On or off | Off |
| **λ labels** | Labels wavelengths on the locus | On or off | On |
| **Show all library spaces** | Draws every space, including imported ones | On or off | Off |
| **WebGL chromaticity fill** | Fills the locus with approximate colours using WebGL 2 | On or off | Off |
| **Reset view** | Returns to CIE 1931 xy, default overlays, no probe | Button | — |
| **Export PNG** | Downloads the diagram as `gamut-<mode>.png` | Button | — |
| **Export SVG** | Downloads the diagram as `gamut-<mode>.svg` | Button | — |
| **Primaries (xy)** R, G, B, W | The working space's primaries and white; editable for Custom | Numbers, 4 decimals | From the space |
| **White point XYZ** | The white as X, Y, Z with Y = 1 | — | From the space |
| **Solve from primaries** | Builds the Custom space from the fields and derives its matrices | Button | — |
| **Transfer function** | Curve shown on the EOTF / OETF canvas | sRGB, Display P3, Rec. 2020, PQ (ST 2084), HLG, Adobe RGB (γ 563/256), ProPhoto (ROMM) | sRGB |
| **Volume comparison** first list | Reference space | sRGB, Display P3, Rec. 2020, ACEScg | sRGB |
| **Volume comparison** second list | Space to compare | Active space, sRGB, Display P3, Rec. 2020, ACEScg | Active space |
| **Compute volume** | Measures both volumes and their overlap | Button | — |
| **Gamut slice** mode | Slice space | Constant L* (CIELAB); Constant L (OKLab) | Constant L* |
| **Level** | Slice lightness | 0 to 100 | 50 |

### Readouts

| Readout | What it shows |
| --- | --- |
| **Chromaticity diagram** | Drawn spaces as triangles, the locus, overlays and the probe marker with its coordinates. Click or drag to probe |
| **Vertex readout** | x, y, Y, a chip with sRGB HEX, CIELAB (L*, a*, b*) and a tick or cross per drawn space |
| **RGB ↔ XYZ matrices** | RGB → XYZ, XYZ → RGB, Area (xy) and Area % sRGB |
| **EOTF / OETF curve** | The chosen transfer curve, its defining document and an equation |
| **Volume metrics** | Both volumes (Lab³) with spread and box, overlap of A and of B in u′v′, and Jaccard |
| **Gamut slice — Lab / OKLab** | Up to five drawn spaces outlined at the slice level |
| **3-D gamut wireframe** | Wireframes of the drawn spaces in CIELAB, at a fixed viewing angle |

## Transfer tab

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Plot** | Which curves and axis | Relative, 0 to 1; Absolute, cd/m² (PQ, log scale 1 to 10,000) | Relative |
| **Fidelity** | Filters the rows | All, Exact, Partial, Corrected (with counts) | All |

Rows give each distinct curve, the spaces that use it, a fidelity tag, the defining document and, where relevant, what it used to be or why it is partial.

## Compare tab

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Measure in** | The share column's plane | u′v′ share; xy share (legacy) | u′v′ share |
| **Samples** (n) | Halton samples per space | 5,000 to 200,000, step 5,000 | 40k |
| **Measure them all** | Measures every space | Button | — |

Table columns: Space, White, Lab volume ± spread, vs sRGB, share.

## Data tab

| Dataset | Status |
| --- | --- |
| Primaries and white points, 13 spaces | Verbatim |
| Transfer functions, 10 distinct curves | Computed |
| HLG opto-electronic transfer | Synthesised (stand-in): inverse OETF only |
| Colour matching functions, 2° | Verbatim |
| Spectral locus | Computed, 380–715 nm |
| RGB ↔ XYZ matrices | Computed |
| Gamut volume in CIELAB | Computed, Halton sampling |
| MacAdam ellipses | Synthesised (stand-in) |

**Status** chips filter the list. **Install a table** ("Drop a CSV or JSON") does not load files in the current version.

## Export tab

| Control | What it does |
| --- | --- |
| **What to take** | **This space**, **Every space**, **The comparison**, **The diagram**, **A link to this view** |
| **As** | Formats that fit the choice: JSON; JSON; CSV or JSON; SVG or PNG; Link |
| **Download** (names the file) or **Copy the link** | Saves the file, or copies the link |
| **Copy to clipboard** | Copies text payloads (hidden for PNG and link) |
| **Exactly what you will get** | Previews the payload and its size |
| **Bring one in**, **Add to the library** | Imports a space from JSON |
| Library table | Name, Type (Standard or Custom), White, Transfer, and **Load** / **Del** |

| Choice | File |
| --- | --- |
| This space, JSON | `gamut-lab-<space>.json` |
| Every space, JSON | `gamut-lab-spaces.json` |
| The comparison, CSV | `gamut-comparison.csv` with Name, Area (xy), Area % sRGB, Volume (Lab³), Transfer, White Point |
| The comparison, JSON | `gamut-comparison.json` with area, area %, volume, spread, box, u′v′ share, transfer and white per drawn space |
| The diagram, SVG | `gamut-diagram.svg` |
| The diagram, PNG | `gamut-diagram.png`, at the canvas size |
| A link to this view | A URL encoding the drawn spaces, diagram mode, overlays and other view settings |

The comparison covers only the spaces currently drawn on the diagram, not the whole library. A link longer than about 1,800 characters shows a warning that some clients truncate long links.

## Reference tab

| Control | What it does |
| --- | --- |
| **Standards**, **Formulas**, **Citations**, **Research notes** | Switch sections |
| **Filter** | Searches all four; `Esc` clears it |

Standards are grouped as display and broadcast, cinema and VFX, photography and print, legacy, and colorimetry foundations. Formulas cover xy and u′v′, matrix derivation, the sRGB, PQ and HLG curves, shoelace area, CIELAB volume and overlap. Citations list 22 references. Research notes include a computed table of each space's area in xy and u′v′, % of sRGB and % of the locus.

## Save to Library

The floating **Save to Library** button stores a snapshot of the diagram in your Auric Artisan Library.
