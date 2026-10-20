---
title: Industrial Dye Chemistry (Dye in Solution) — Reference
description: Every tab, control, readout, message and file format in Dye in Solution, with ranges and defaults.
product: Website › Tools › Perception and spectral › Industrial Dye Chemistry
updated: 2026-09-25
---

# Dye in Solution reference

Address: https://auricartisan.com/tool/general/spectral-tools/industrial-dye-chemistry/

## Tabs

| Tab | Contents |
|---|---|
| **Lab** | Bath, light and component controls; the spectrum plot; colour, absorbance and wavelength readouts; the lights row |
| **Method** | Four explanation views and the tolerance sweep |
| **Safety** | The withdrawn hazard gate and what stays |
| **Data** | The register of 18 tables and formulas, filterable by status; the tab label shows the count; measured-spectrum loader |
| **Export** | Spectrum CSV, bath JSON and link |
| **Reference** | Thirteen sources, filterable |

Links in the page text (for example **Method** or **Safety** in the note strip) switch to that tab.

## Lab tab — The bath

| Control | Range and step | Default |
|---|---|---|
| **pH** | 0–14, step 0.05 | 3.50 |
| **Path length** | 0.1–10 cm, step 0.1 | 1.0 cm |
| **Run the titration** | Steps pH from 0 to 14 by 0.2 every 90 ms; reads **Stop** while running | — |

## Lab tab — The light

| Control | Values | Default |
|---|---|---|
| Illuminant | **D65 — daylight, 6504 K**, **D50 — daylight, 5003 K**, **A — a blackbody at 2856 K**, **E — equal energy** | D65 |

## Lab tab — The components and the selected dye

| Control | What it does | Values or range | Default |
|---|---|---|---|
| Component buttons | Select a dye; show its swatch, pKa, concentration, band peaks and **Stand-in** or **Measured** | 1 to 4 dyes | Weak-acid indicator |
| Dye menu | The dye **Add** will add | Six presets | Weak-acid indicator |
| **Add** | Adds the dye in the menu and selects it | Up to 4 components | — |
| **Mute** | Toggles the selected dye out of and back into the bath | — | — |
| **Remove** | Deletes the selected dye | At least 1 remains | — |
| **pKa** | The selected dye's pKa | 0–14, step 0.1 | The preset's |
| **Concentration** | The selected dye's concentration | 0.5–200 µM, step 0.5 | The preset's |
| **Reset the bath** | Default bath, clears sweep and measured spectra | — | — |

Preset dyes, with pKa, default concentration, and acid and base λmax, ε and band width (Gaussian standard deviation):

| Dye | pKa | µM | Acid form | Base form |
|---|---|---|---|---|
| **Weak-acid indicator** | 3.5 | 34 | 508 nm, 26,000, 34 nm | 462 nm, 22,000, 30 nm |
| **Mid-range indicator** | 7.1 | 20 | 430 nm, 15,000, 30 nm | 615 nm, 34,000, 32 nm |
| **High-range indicator** | 9.4 | 25 | 400 nm, 900, 40 nm | 553 nm, 31,000, 30 nm |
| **Azo red, pH-stable** | 12.5 | 50 | 505 nm, 30,000, 36 nm | 512 nm, 29,000, 36 nm |
| **Anthraquinone blue, pH-stable** | 11.8 | 40 | 600 nm, 16,000, 26 nm | 606 nm, 16,500, 26 nm |
| **Yellow, pH-stable** | 12.0 | 60 | 428 nm, 21,000, 28 nm | 431 nm, 21,000, 28 nm |

## Lab tab — Spectrum plot

| Element | Description |
|---|---|
| **Acid form** `HA` | The selected dye's acid-form molar absorptivity, dashed |
| **Base form** `A⁻` | The base-form molar absorptivity, dashed |
| **What you measure** | Their weighted sum at the current pH, filled |
| **Isosbestic** | Green circle and label where the forms cross, when the crossing is clear |
| Axes | 380–780 nm; molar absorptivity in thousands (k) |
| Drop and click | Drop a spectrum file on the plot, or click it to choose one |

## Lab tab — Readouts

| Readout | Meaning | Format |
|---|---|---|
| **sRGB** | Un-adapted colour under the chosen light | Hex |
| **CIE L\*** | Lightness against the light's own white | One decimal |
| **a\*, b\*** | Opponent coordinates against the light's own white | One decimal each |
| **Base fraction** | Share of the selected dye in the base form | Three decimals |
| **Peak absorbance** | Highest bath absorbance | Three decimals |
| **λmax** | Wavelength of that peak | nm |
| **Beer–Lambert holds** | **yes, A x.xx** or **no — A x.xx is past 1** (highlighted) | — |
| **Isosbestic point** | **N nm**, **N nm (weak)** or **none in range** (last two highlighted) | — |
| **Dominant λ** | Dominant wavelength, or complementary with a `c` prefix | nm |
| **Excitation purity** | Distance from white towards the spectral edge | %, one decimal, or **—** |
| **Inside sRGB** | **yes** or **no** (highlighted) | — |
| **Observer** | Fixed | CIE 1931 2° |

## Lab tab — The same bath under every light

Swatches for **D65**, **D50**, **A** and **E**; the current light is labelled **— this bath** with its hex, the others show **ΔE₀₀** from it. An **F11** card reads **not held**.

## Method tab

| Control | Values or range | Default |
|---|---|---|
| **Method** | **The titration**, **Beer–Lambert**, **The light**, **What was resampled** | The titration |
| **Concentration** (sweep) | ±0–20%, step 0.5 | ±2.0% |
| **Path length** (sweep) | ±0–2 mm, step 0.01 | ±0.10 mm |
| **Molar absorptivity** (sweep) | ±0–30%, step 0.5 | ±5.0% |
| **Draws** | 100–2000, step 100 | 500 |
| **Run the sweep** | Runs the sweep; shows **Median**, **95th percentile** and **Worst draw** in ΔE₀₀ | — |

## Safety tab

Shows **GHS hazard assessment and PPE compliance gate**, marked **Withdrawn**, with a table of what an earlier version did and what GHS classification actually is, and **What stays, because it is true and needs no calculation**: gloves, eye protection and a lab coat for any dye work; the supplier's safety data sheet (section 2 for the GHS classification, section 8 for exposure controls and PPE); and disposing of dye liquor through your institution's waste stream.

## Data tab

| Control | What it does |
|---|---|
| **Status** | **All** (18), **Verbatim** (6), **Computed** (5), **Stand-in** (4), **Absent** (3) |
| Register row | Select, or press `Enter` or `Space`, to expand its note and **what it would take** |
| Form menu | **Into the acid form** or **Into the base form** |
| **Drop a spectrum** | Loads a measured spectrum; click or `Enter`/`Space` opens a file chooser |
| **Back to the drawn bands** | Shown after loading; restores drawn bands |

Entries: **CIE 1931 2° standard observer**, **CIE D-series eigenvector basis**, **sRGB primaries and transfer curve**, **CIEDE2000 colour difference**, **The Beer–Lambert law**, **Henderson–Hasselbalch** (Verbatim); **The two-species absorbance**, **The isosbestic point**, **Dominant wavelength and excitation purity**, **Colour inconstancy index**, **Special metamerism index, change of illuminant** (Computed); **The absorption band shape**, **The six dye presets**, **The default sweep tolerances**, **Kubelka-Munk on an opaque substrate** (Stand-in); **The CIE fluorescent illuminants (F-series)**, **Colourfastness and content testing**, **GHS classification and PPE compliance** (Absent). The metamerism index and Kubelka–Munk entries describe methods that have no control in the current interface.

## Export tab

| Control | What it does |
|---|---|
| **What to take** | Preview **The spectrum**, **The whole bath** or **A link to this** |
| **Download the spectrum** | Saves `dye-in-solution-spectrum.csv` (81 rows) |
| **Download the bath** | Saves `dye-in-solution-bath.json` |
| **Copy a link to this bath** | Copies a link |

## Reference tab

| Control | Values |
|---|---|
| **Reference** | **All** (13), **Runs** (6), **Partly** (1), **Not held** (6) |

## Messages

| Message | Meaning |
|---|---|
| **Titration complete** | The titration reached pH 14 |
| **Four components is the ceiling here** | A fifth dye was refused |
| **The bath needs at least one dye** | The last dye cannot be removed |
| **Bath reset** | Defaults restored |
| **Swept N draws in M ms** | The sweep finished |
| **N rows into the acid form — peak N nm, ε N** | A spectrum was loaded |
| **No two-column numeric rows in that file** | The file had no usable rows |
| **Not installed: fewer than eight rows** / **fewer than eight usable rows** | Too few rows |
| **Not installed: covers X to Y nm; at least 420 to 680 is needed …** | The file does not span 420–680 nm |
| **Back to the drawn bands** | Measured spectra cleared |
| **Link copied** | The link is on the clipboard |

## File formats

| File | Format | Contents |
|---|---|---|
| `dye-in-solution-spectrum.csv` | CSV with `#` header lines | `wavelength_nm,absorbance,transmittance,eps_acid,eps_base,observer_x,observer_y,observer_z` |
| `dye-in-solution-bath.json` | JSON | See [Export and share](export-and-share.md) |
| Measured spectrum (input) | `.csv`, `.tsv` or `.txt` | Two columns: wavelength (nm), molar absorptivity (M⁻¹ cm⁻¹); at least 8 rows spanning 420–680 nm |

## Link parameters

`ph`, `path` (cm), `ill` (`d65`, `d50`, `a`, `e`), `dyes` (`id:pKa:µM`, comma-separated; ids `weak-acid`, `mid-range`, `high-range`, `azo-red`, `anthraquinone-blue`, `yellow`).
