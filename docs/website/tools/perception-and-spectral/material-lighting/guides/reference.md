---
title: Material Lighting (Material Under Light) — Reference
description: Every tab, control, readout, message and file format in Material Under Light, with ranges and defaults.
product: Website › Tools › Perception and spectral › Material Lighting
updated: 2026-09-25
---

# Material Under Light reference

Address: https://auricartisan.com/tool/general/spectral-tools/material-lighting/

## Tabs

| Tab | Contents |
|---|---|
| **Lab** | Light, material, surface and geometry controls; the spectrum plot; the sample sphere and lobe cards; readouts; the reference comparison |
| **Method** | Four explanation views |
| **Metrics** | The sensitivity sweep and the two withdrawn rendering indices |
| **Data** | The register of 17 tables and formulas, filterable by status; the tab label shows the count; reflectance loader |
| **Export** | Spectrum CSV, scene JSON and link |
| **Reference** | Fourteen sources, filterable |

Links in the page text (for example **Metrics** or **Data**) switch to that tab.

## Lab tab — The light

| Control | Values or range | Default |
|---|---|---|
| Illuminant | **D65 — daylight, 6504 K**, **D50 — daylight, 5003 K**, **D55 — daylight, 5503 K**, **D75 — daylight, 7504 K**, **A — a blackbody at 2856 K**, **E — equal energy**, **Blackbody at a temperature you choose**, **Daylight at a temperature you choose** | D65 |
| **Temperature** | 1800–10000 K, step 50; enabled only for the last two options; daylight is raised to at least 4000 K | 2700 K |

## Lab tab — The material and surface

| Control | Values or range | Default |
|---|---|---|
| Material | **White**, **Gray**, **Black**, **Red**, **Green**, **Blue**, **Yellow**, **Cyan**, **Magenta**, **Skin**, **Leaf**, **Ocean**, **Concrete**, **Wood**, **Sky**, **Gold**, **Copper**, **Silver**, **Ceramic**, **Rubber**; or one measured file | Gold |
| **Dielectric** / **Conductor** | Surface type | Dielectric |
| **Refractive index** | 1.00–3.00, step 0.01; disabled for Conductor | 1.50 |
| **Roughness** | 0.02–1.00, step 0.01 | 0.40 |

## Lab tab — The geometry

| Control | Range and step | Default |
|---|---|---|
| **Light from** | 0–89°, step 1 | 30° |
| **Seen from** | 0–89°, step 1 | 20° |
| **Between them** | 0–180°, step 1 | 0° |

## Lab tab — Buttons

| Button | What it does |
|---|---|
| **Save the spectrum** | Saves `material-under-light-spectrum.csv` |
| **Reset the scene** | Restores D65, 2700 K, Gold (if the presets are loaded), Dielectric, 1.50, GGX, 0.40, 30°, 20°, 0°, and clears the sweep |

## Lab tab — Lobe cards

| Card | Source |
|---|---|
| **GGX** (default) | Walter et al. 2007 |
| **Beckmann** | Beckmann & Spizzichino 1963 |
| **Ward** | Ward 1992 |
| **Ashikhmin-Shirley** | Ashikhmin & Shirley 2000 |
| **Oren-Nayar** | Oren & Nayar 1994 |

## Lab tab — Spectrum and sample

| Element | Description |
|---|---|
| Spectrum plot | **Illuminant** (dashed), **Reflectance** and **What leaves the surface** (filled), each scaled to its own maximum, 380–780 nm |
| Legend | The illuminant's name; the material with "synthesised" or the file name with "measured"; "their product, times the lobe" |
| Sample | A 232 × 232 sphere, seen head-on, lit from the **Light from** angle |
| Exposure note | **scaled so a white card here would read Y = 1** |
| **clipped to sRGB** | Shown when the swatch or the sphere had to be clipped |
| Drop and click | Drop a reflectance file on the plot, or click it to choose one |

## Lab tab — Readouts

| Readout | Meaning | Format |
|---|---|---|
| **sRGB** | Un-adapted colour at the chosen geometry | Hex |
| **CIE L\*** | Lightness against the light's own white | One decimal |
| **a\*, b\*** | Opponent coordinates against the light's own white | One decimal each |
| **Jz** | JzAzBz lightness | Four decimals |
| **Measured temperature** | CCT of the illuminant with its error band; highlighted above 7000 K | Nearest 10 K |
| **Reference for it** | **daylight N K** or **blackbody N K** | Nearest 10 K |
| **Reflectance** | **synthesised** (highlighted) or **measured —** and the file name | — |
| **Inside sRGB** | **yes**, **no** or **the highlight is not** (last two highlighted) | — |

## Lab tab — Against the reference the standard names

| Element | Description |
|---|---|
| **Under your source** | Swatch, captioned with the illuminant |
| ΔE₀₀ | CIEDE2000 difference between the two, two decimals |
| **Under its reference** | Swatch, captioned **D** or **BB** and the temperature |
| Note | The reason for the reference choice |

## Method tab

| Control | Values | Default |
|---|---|---|
| **Method** | **From spectrum to colour**, **Choosing the reference**, **The five lobes**, **Two white points** | From spectrum to colour |

## Metrics tab

| Control | Range and step | Default |
|---|---|---|
| **Perturbation** | ±0.005–0.1, step 0.005 | ±0.02 |
| **Correlation length** | 0–120 nm, step 5 (0 is **independent**) | 40 nm |
| **Draws** | 100–2000, step 100 | 500 |
| **Run the sweep** | Shows **Median**, **95th percentile** and **Worst draw** in ΔE₀₀ | — |

Below: **CIE colour rendering index** and **TM-30 Rf and Rg**, each marked **Withdrawn**, with tables and **What it would take**.

## Data tab

| Control | What it does |
|---|---|
| **Status** | **All** (17), **Verbatim** (8), **Computed** (5), **Stand-in** (2), **Absent** (2) |
| Register row | Select, or press `Enter` or `Space`, to expand its note and **what it would take** |
| **Drop a reflectance file** | Loads a measured reflectance; click or `Enter`/`Space` opens a file chooser |
| **Go back to the presets** | Shown after loading; restores the twenty presets |

Entries: **CIE 1931 2° standard observer**, **CIE D-series eigenvector basis**, **sRGB primaries and transfer curve**, **CIEDE2000 colour difference**, **JzAzBz**, **Planck's radiation law**, **GGX / Trowbridge-Reitz microfacet distribution**, **The other four reflectance lobes** (Verbatim); **Correlated colour temperature**, **The reference illuminant for a source**, **Rendering shift**, **Exposure normalisation**, **Illumination and view geometry** (Computed); **The twenty pigment reflectances**, **The sensitivity sweep** (Stand-in); **CIE colour rendering index (Ra)**, **IES TM-30 fidelity and gamut (Rf, Rg)** (Absent).

## Export tab

| Control | What it does |
|---|---|
| **What to take** | Preview **The spectrum**, **The whole scene** or **A link to this** |
| **Download the spectrum** | Saves `material-under-light-spectrum.csv` (81 rows) |
| **Download the scene** | Saves `material-under-light-scene.json` |
| **Copy a link to this scene** | Copies a link |

## Reference tab

| Control | Values |
|---|---|
| **Reference** | **All** (14), **Colorimetry** (6), **Reflectance** (6), **Not held** (2) |

## Messages

| Message | Meaning |
|---|---|
| **Scene reset** | Defaults restored |
| **Swept N perturbations in M ms** | The sweep finished |
| **N rows accepted — the register now says verbatim** (with **, read as percent** when applicable) | A reflectance file was loaded |
| **No two-column numeric rows in that file** | The file had no usable rows |
| **Not installed: fewer than eight rows** / **fewer than eight usable rows** | Too few rows |
| **Not installed: covers X to Y nm; at least 420 to 680 is needed …** | The file does not span 420–680 nm |
| **Back to the twenty synthesised presets** | The loaded file was removed |
| **Link copied** | The link is on the clipboard |

## File formats

| File | Format | Contents |
|---|---|---|
| `material-under-light-spectrum.csv` | CSV with `#` header lines | `wavelength_nm,illuminant_relative,reflectance,radiance_relative,observer_xbar,observer_ybar,observer_zbar` |
| `material-under-light-scene.json` | JSON | See [Export and share](export-and-share.md) |
| Reflectance (input) | `.csv`, `.tsv` or `.txt` | Two columns: wavelength (nm), reflectance (0–1 or percent); at least 8 rows spanning 420–680 nm |

## Link parameters

`illuminant`, `cct`, `material`, `ior`, `roughness`, `thetaL`, `thetaV`, `phi`, `lobe`, `metal`. Values are listed in [Export and share](export-and-share.md).
