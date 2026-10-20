---
title: Illuminants — Reference
description: Every control, readout, option and export in the Standard Illuminants lab, tab by tab.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Illuminants reference

Address: https://auricartisan.com/tool/general/colorimetry/illuminants/

## Lab tab

### Controls

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| **Source mode** | Chooses between a tabulated standard illuminant and a Planckian (blackbody) spectrum | **Standard**, **Blackbody** | Standard |
| **Illuminant** | The standard illuminant to analyse | 18 choices, listed below | CIE D65 (6504 K) — Daylight, sRGB |
| **CCT** slider and number box | Colour temperature of the blackbody source. Moving either switches to Blackbody mode | 1,500 to 25,000 K in 50 K steps | 6500 |
| **Link to select** | When ticked, choosing a standard illuminant also sets the CCT field to that illuminant's nominal CCT | On or off | On |
| **Reset to D65** | Returns to Standard mode, D65 and 6500 K | Button | — |
| **Enable comparison** | Overlays a second illuminant on the SPD chart and fills the comparison table | On or off | Off |
| Comparison illuminant list | The second illuminant | CIE A, D50, D55, D65, D75, Equal-energy E, F2, F7, F11 | CIE A (2856 K) |
| **Surface reflectance samples** | Which surfaces appear under Surface appearance | White, Gray, Red, Green, Blue, Skin, Yellow, Cyan | White, Gray, Red, Green, Skin on |
| **Adapt from** | Source white point for the adaptation preview | D65, D50, D55, D75, A, E | D65 |
| **Swap** | Exchanges Adapt from and Adapt to | Button | — |
| **Adapt to** | Destination white point | D65, D50, D55, D75, A, E | D50 |
| Transform chips | The chromatic adaptation transform | Bradford, CAT16, CAT02, Von Kries, Sharp, XYZ scaling, None | Bradford |

### The 18 standard illuminants

| Choice in the list | Kind |
| --- | --- |
| CIE A (2856 K) — Incandescent | Tungsten, computed from Planck's law |
| CIE D50 (5003 K) — Daylight, ICC PCS | Daylight, reconstructed from the CIE daylight basis |
| CIE D55 (5503 K) — Daylight | Daylight |
| CIE D65 (6504 K) — Daylight, sRGB | Daylight |
| CIE D75 (7504 K) — North sky | Daylight |
| Equal-energy E (5455 K) | Equal power at every wavelength |
| F1 — Daylight fluorescent (6430 K) | Fluorescent, stand-in spectrum |
| F2 — Cool white fluorescent (4230 K) | Fluorescent, stand-in |
| F3 — White fluorescent (3450 K) | Fluorescent, stand-in |
| F4 — Warm white fluorescent (2940 K) | Fluorescent, stand-in |
| F5 — Daylight fluorescent (6350 K) | Fluorescent, stand-in |
| F6 — Lite white fluorescent (4150 K) | Fluorescent, stand-in |
| F7 — D65 simulator fluorescent (6500 K) | Broadband fluorescent, stand-in |
| F8 — D50 simulator fluorescent (5000 K) | Broadband fluorescent, stand-in |
| F9 — Cool white fluorescent (4150 K) | Broadband fluorescent, stand-in |
| F10 — Narrow-band 3-phosphor (5000 K) | Three-band fluorescent, stand-in |
| F11 — TL84 3-phosphor (4000 K) | Three-band fluorescent, stand-in |
| F12 — TL83 3-phosphor (3000 K) | Three-band fluorescent, stand-in |

The kelvin figures in the list are nominal labels. The lab computes its own CCT from each spectrum.

### Readouts

| Readout | What it shows |
| --- | --- |
| **Illuminant Summary** | A swatch of the white as sRGB, the name, the type and HEX, then **CCT**, **Duv**, **CIE x**, **CIE y**, **CRI Ra** and **XYZ** (Y normalised to 100) |
| **SPD** chart | Relative power from 380 to 780 nm at 5 nm. Gold is the selected light, blue the comparison. A faint rainbow fill marks the wavelength regions. Click to probe the nearest wavelength and its power |
| **CRI** chart | Bars for R1 to R14 and the Ra value (mean of R1 to R8). Reference: blackbody below 5,000 K, CIE daylight at or above. Computed on stand-in test samples |
| **Surface appearance** | For each ticked surface: its colour under D65, its colour under the selected light after adaptation to D65, both HEX values and the ΔE₀₀ between them |
| **Chromatic adaptation preview** | 24 fixed colours (top) and their adapted versions (bottom), with a caption naming source, destination and method |
| **Adaptation matrix details** | The transform's M matrix, the LMS scaling (destination ÷ source), and the source and destination white in LMS. With None selected it says no adaptation is applied |
| **Illuminant comparison** | With comparison on: CCT, CRI Ra and CIE x, y for both lights, and the **Metamerism Index (avg ΔE₀₀)** over the 14 test samples |

Surface samples: White Paint, Neutral Gray, Saturated Red, Leaf Green, Sky Blue, Skin-like, Yellow Paint and Cyan Ink. They are simple educational reflectance curves, not measured materials.

Each chart has a **Fullscreen** button; double-clicking the chart does the same.

## Chromaticity tab

| Control or readout | What it does | Values | Default |
| --- | --- | --- | --- |
| **Plane** | The chromaticity diagram to draw | **1931 xy**, **1976 u′v′**, **1960 uv** | 1931 xy |
| **Planckian locus** | Draws the blackbody curve from 1,500 to 25,000 K | On or off | On |
| **Isotemperature lines** | Short lines across the locus at 2000, 2856, 4000, 5000, 6500, 10000 and 20000 K (needs the Planckian locus on) | On or off | On |
| **Daylight locus** | Draws CIE daylight chromaticities from 4,000 to 25,000 K | On or off | Off |
| **sRGB / P3 / Rec.2020** | Draws the three RGB primary triangles | On or off | Off |
| Marks | A, D50, D65 and E in grey; the current light in gold, labelled | — | — |
| **Dominant wavelength** | **λ d** (a minus sign means complementary wavelength), **Purity**, **D uv** and **CCT** | — | — |

The dominant wavelength is measured from the D65 reference white against the spectral locus. When the light is almost the reference white (purity below 0.2%), λ d shows a dash because it has no defined direction. CCT shows "n/a" when it is not valid (see Methods).

MacAdam ellipses are not drawn. A note under the overlays explains that the measured ellipse parameters are not held.

## Uncertainty tab

| Control or readout | What it does | Values | Default |
| --- | --- | --- | --- |
| **Input budget** | Six editable error terms | See [Estimate measurement uncertainty](estimate-uncertainty.md) | Preset spectroradiometer budget |
| **Trials** | Number of Monte Carlo trials | **1k**, **4k**, **20k** | 4k |
| **Run the propagation** | Runs the simulation on the light selected in the Lab | Button | — |
| **Expanded uncertainty, k = 2** | Table of Quantity, Value, u, U (k=2) and Relative for x, y, CCT and Duv | — | "Not run yet." |
| **Contribution to u(CCT)** | Share of the CCT uncertainty from each term | — | — |
| **95% coverage region in u′v′** | Ellipse holding 95% of results; dashed ellipse at one standard deviation | — | — |

## Methods tab

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Observer** | The standard observer | **1931 2°**; **1964 10°** is shown but switched off because its tables are not held | 1931 2° |
| **Interval** | Wavelength step used for integration | **1 nm**, **5 nm**, **10 nm** | 5 nm |
| **Interpolation** | How the source table is resampled onto the working grid | **Sprague**, **Linear**, **PCHIP** | Sprague |

The interval and interpolation apply to the Chromaticity, Uncertainty and Console readings and to the tables on this tab. The Lab tab's own readouts are always computed at 5 nm.

Readouts:

- **What the pipeline is worth** — a table with the current pipeline's x, y, CCT and Duv, then the change caused by switching to 1 nm, to 5 nm, to linear and to PCHIP. A dash means no change. The note beneath explains that a 5 nm table resampled onto a finer grid adds no information.
- **CCT method** — the CCT and Duv by Ohno's method (named "Ohno 2014, triangular" or "Ohno 2014, parabolic" depending on how close the light is to the locus), with a validity note, and the older McCamy (1992) cubic for comparison, marked as having no validity test.
- **Rendition metrics** — three cards, all switched off: TM-30-18, CIE 13.3 and CIE S 026. Each lists the dataset it would need.

CCT validity notes: "in range" (Duv within ±0.02), "far from the locus" (Duv between ±0.02 and ±0.05), a note that CCT is not defined when Duv is beyond ±0.05, or "outside 1000–100000 K". A CCT is reported as valid only between 1,000 and 100,000 K and with Duv within ±0.05.

## Console tab

See [Query many illuminants at once](query-console.md) for the grammar.

| Control | What it does |
| --- | --- |
| **Query** box | The query text. `Ctrl` + `Enter` runs it |
| **Run** | Runs the query |
| **CSV** | Downloads `illuminants.csv` |
| **JSON** | Downloads `illuminants.json` |
| **Recipes** | Four ready-made queries; selecting one loads and runs it |
| **Results** table | One row per illuminant |
| **Horizontal axis**, **Vertical axis** | Columns to plot in the scatter chart |

## Data tab

The register lists every dataset the lab touches, with its source, the interval it is tabulated at, its status and why it matters. The summary counts datasets, verbatim, computed and not held.

| Status | Meaning |
| --- | --- |
| **Verbatim** | The published table, copied |
| **Computed** | Derived exactly from a defining formula or a verbatim table |
| **Synthesised** | A stand-in that is not the published data; never reported as a standard value |
| **Absent** | Not held; features that need it stay switched off |

| Dataset | Status |
| --- | --- |
| Colour matching functions, 2° (CIE 1931) | Verbatim |
| Colour matching functions, 10° (CIE 1964) | Absent |
| Daylight eigenvectors S0 S1 S2 | Verbatim |
| Illuminant A | Computed |
| Illuminants D50 D55 D65 D75 | Computed |
| Illuminant E | Computed |
| Planckian radiators | Computed |
| Fluorescent F1–F12 | Synthesised |
| Fluorescent FL3.1–FL3.15 | Absent |
| High pressure discharge HP1–HP5 | Absent |
| LED-B1–B5, BH1, RGB1, V1–V2 | Absent |
| Test colour samples 1–14 | Synthesised |
| Colour evaluation samples 1–99 | Absent |
| α-opic action spectra | Absent |
| MacAdam ellipses | Absent |

**Switched off, and why** lists the features that stay off: TM-30-18 Rf / Rg and the colour vector graphic; CIE 13.3 Ra and R1–R14 as standard values; melanopic EDI and the α-opic ratios; the CIE 1964 10° observer; F1–F12 as published illuminants; MacAdam ellipse overlays.

## Export tab

| Control | What it does | Output |
| --- | --- | --- |
| **Export SPD CSV** | Downloads the selected light's spectrum | `<name>-spd.csv` with columns `wavelength_nm` and `relative_power`, 380–780 nm at 5 nm |
| **Export JSON** | Downloads the light's data | `<name>.json` with the illuminant label, CCT, xy, XYZ, the CRI object (Ra and R1–R14) and the SPD |
| **Export SPD PNG** | Saves the SPD chart as an image | `<name>-spd.png` |
| **Copy white HEX** | Copies the sRGB HEX of the light's white to the clipboard | Text |
| **Share URL** field, **Generate**, **Copy** | Builds and copies a link to the current settings | A URL |
| **Generate comparison table** | Tables all 18 standard illuminants | Illum, CCT, x, y, CRI Ra and a white swatch |

`<name>` is the illuminant (for example `D65`) or, in Blackbody mode, `BB_<CCT>K`.

The share link stores the source mode, the illuminant (Standard mode) or the CCT (Blackbody mode), and the adaptation source, destination and method. It does not store the surface selection or the comparison settings.

## Reference tab

| Control | What it does |
| --- | --- |
| **Standards**, **Formulas**, **Citations**, **Research notes** | Switch between the four sections. Each shows a count |
| **Filter** | Searches all four sections at once and jumps to one with matches. `Esc` clears it |
| **Status** chips (Standards) | **All**, **Implemented**, **Stand-in**, **Cited only** |
| **Expand**, **Collapse** (Standards) | Open or close every row |
| **Where it is used** chips (Citations) | **All**, **Runs here**, **Data missing**, **Context only** |
| **Open in the data register** (inside a standard) | Jumps to the Data tab |

Each standard shows a badge read from the data register, the datasets it rests on, and any datasets it specifies that the lab does not hold. **Formulas** has eight sub-tabs: Planck Blackbody, CIE Daylight, SPD to XYZ, CRI Formula, TM-30 Overview, Bradford CAT, CCT Estimation and ΔE Formulas. These explain the background mathematics; where a formula (such as McCamy's CCT) is not what produces the readings, the Methods tab says which method does. **Citations** lists 22 sources, each marked Runs here, Data missing or Context only.

## Save to Library

The floating **Save to Library** button stores a preset of the current settings in your Auric Artisan Library, so you can reopen it later.
