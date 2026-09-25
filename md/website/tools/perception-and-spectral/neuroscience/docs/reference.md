---
title: Neuroscience (Visual Pathway) — Reference
description: Every tab, control, readout, message and file format in the Visual Pathway, with ranges and defaults.
product: Website › Tools › Perception and spectral › Neuroscience
updated: 2026-09-25
---

# Visual Pathway reference

Address: https://auricartisan.com/tool/general/perception-and-neuroscience/neuroscience/

## Tabs

| Tab | Contents |
|---|---|
| **Lab** | Stimulus, geometry and stage controls; stimulus and map canvases; scale bar; cone figure; readouts; save and link buttons |
| **Pipeline** | The colour chain, the opponent-axis table of seven colours and the sensitivity table, with an earlier-version comparison |
| **Cells** | Previews of every stage over one stimulus, and the list of controls from an earlier version |
| **Data** | The register of nine datasets and transforms, filterable by status; the tab label shows the count (9); cone-table installer |
| **Export** | Colour list, CSV, clipboard, settings JSON and link |
| **Reference** | Standards, formulas, citations and research notes, with a search box |

Links in the page text (for example **Data** or **Cells** in a hint) switch to that tab.

## Lab tab — Stimulus

| Control | What it does | Values or range | Default |
|---|---|---|---|
| **Stimulus** | Chooses the source | **Grating**, **Test card** | Grating |
| **Base colour** | The colour the grating is built from (grating only) | Any colour from the picker | `#3A8CFF` |
| **Carrier** | What the grating modulates (grating only) | **Chromatic**, **Luminance** | Chromatic |

## Lab tab — Geometry, frequency and contrast

| Control | What it does | Range and step | Default |
|---|---|---|---|
| **Viewing distance** | Eye-to-screen distance used for every frequency | 20–200 cm, step 1 | 57 cm |
| **Pixel pitch** | Physical size of one pixel | 0.05–0.6 mm, step 0.001 | 0.248 mm |
| **Spatial frequency** | Grating frequency | 0.2–30 c/deg, step 0.1 | 4.0 c/deg |
| **Contrast** | Grating swing either side of its mean | 0–100%, step 1 | 25% |
| **Pupil** | Shown only; does not change any output in this version | 2–8 mm, step 0.1 | 3.0 mm |

## Lab tab — Stages

| Checkbox | Stage | Default |
|---|---|---|
| **Retina — centre-surround** | Difference-of-Gaussians on and off maps | On |
| **LGN — opponent channels** | L − M, S − (L+M)/2 and L + M maps | On |
| **V1 — Gabor bank** | Complex-cell energy and preferred orientation | On |
| **V2 — boundary signal** | Normalised gradient of V1 energy; needs V1 | On |
| **V4 — colour cell** | Projection onto a preferred colour direction | On |

## Lab tab — Show

| Control | Values | Default |
|---|---|---|
| Map menu | **Retina, on-centre**; **Retina, off-centre**; **LGN, L − M**; **LGN, S − (L+M)/2**; **LGN, L + M**; **V1, complex-cell energy**; **V1, preferred orientation**; **V2, boundary signal**; **V4, colour cell** | Retina, on-centre |
| Colourmap menu | **Viridis**, **Inferno**, **Grayscale** | Viridis |
| **Show the scale** | Shows or hides the scale bar | On |

## Lab tab — Stage settings

Shown only while the stage is on.

| Control | Range and step | Default | Unit |
|---|---|---|---|
| **Centre σ** (Retina) | 0.5–6, step 0.1 | 1.5 | pixels |
| **Surround σ** (Retina) | 1–14, step 0.1 | 4.0 | pixels |
| **Surround weight** (Retina) | 0–1.5, step 0.01 | 0.75 | none |
| **Gabor frequency** (V1) | 0.2–30, step 0.1 | 4.0 | c/deg |
| **Orientations** (V1) | 2–16, step 1 | 8 | count |
| **Kernel size** (V1) | 9–51, step 2 | 31 | pixels |
| **Envelope σ** (V1) | 1–16, step 0.1 | 6.0 | pixels |
| **V4 preferred direction** | **Red**, **Green**, **Blue**, **Yellow**, **Orange**, **Purple** | Red | — |

## Lab tab — Colour vision

| Control | Values | Default |
|---|---|---|
| **Colour vision** | **Typical**, **Protanopia**, **Deuteranopia**, **Tritanopia** (Viénot, Brettel and Mollon 1999, full strength) | Typical |

## Lab tab — Canvases, scale bar and figure

| Element | Description |
|---|---|
| **Stimulus** canvas | 256 × 256; the frame the stages see, after any colour vision simulation |
| Map canvas | 256 × 256; the selected map, named underneath, with **— stage off** when its stage is off |
| Header note | `256 × 256 · N° per pixel` at the stated geometry |
| Scale bar | Minimum, colour ramp, maximum and label: **response, this map's own range**; **flat — this stage found no variation in this stimulus**; or 0°–180° **preferred orientation** |
| Cone figure | L, M and S curves 390–730 nm with dashed lines at the published peaks (442, 541, 567 nm) and a note |

## Lab tab — Readouts

| Readout | Meaning | Format |
|---|---|---|
| **L − M peak gap** | Distance between the L and M peaks of the held cone table; highlighted below 5 nm | nm |
| **Published gap** | Fixed reference value | 25 nm |
| **Neutral off-axis** | Worst chromatic departure of a nine-step grey ramp; highlighted above 0.001 | Scientific notation |
| **Contrast achieved** | Contrast drawn after any sRGB cap; highlighted when capped | % |
| **Sensitivity at this frequency** | The tool's log-Gaussian weighting (peak 4 c/deg, 1.6 octaves) at the stimulus frequency | 0–1, three decimals |
| **The curve's peak** | Peak of that weighting | 4.0 c/deg |
| **Frame RMS contrast** | Root-mean-square spread of relative luminance over the stimulus frame | Four decimals |
| **Nyquist limit of the grid** | Half a cycle per pixel at the stated geometry | c/deg, one decimal |

## Lab tab — Notes and buttons

| Element | When it appears or what it does |
|---|---|
| **Above the pixel grid's Nyquist limit.** | Spatial frequency is above the Nyquist limit; the drawn grating is an alias |
| **The contrast you asked for does not fit in sRGB.** | The requested swing does not fit both phases; the contrast was reduced |
| **Save the map** | Saves the map canvas as `visual-pathway-<map>.png` |
| **Copy a link to this view** | Copies a link with the current settings |

## Pipeline tab

| Control | Values | Default |
|---|---|---|
| **Show** | **The chain**, **The opponent axes**, **The sensitivity curve** | The chain |
| **Against** | **What it was**, **Hide** | What it was |

Outputs: the chain of seven steps; a table of `#000000`, `#404040`, `#808080`, `#C0C0C0`, `#FFFFFF`, `#3A8CFF` and `#E03131` with **L − M** and **S − (L+M)/2** (plus **as shipped** columns with **What it was**); or a table of **Pupil** (2, 3, 5, 8 mm), **Peak, as shipped**, **Peak now** and **Published photopic peak**.

## Cells tab

| Control | Values | Default |
|---|---|---|
| **Show** | **Everything** (eight stage cards plus two withdrawn panels), **The five that run** | Everything |
| **Contrast** | **10%**, **25%**, **100%** | 25% |

Cards: **Stimulus**, **Retina — centre-surround**, **LGN — L − M**, **LGN — S − (L+M)/2**, **V1 — Gabor energy**, **V1 — hypercolumn**, **V2 — boundary signal**, **V4 — colour cell**; withdrawn: **Spike raster**, **Detection %**. Each card is 96 × 96 with a tag: **pass-through**, **units noted**, **space fixed**, **units fixed**, **runs**, **stand-in**, **inherits** or **withdrawn**. The list **Controls that were read and never used** has six rows marked **removed** or **wired up**.

## Data tab

| Control | What it does |
|---|---|
| **Status** | Filters the register: **All** (9), **Verbatim** (2), **Computed** (2), **Stand-in** (4), **Absent** (1) |
| Register row | Select (or press `Enter` or `Space`) to expand its note and **What it would take** |
| **Drop a CSV or JSON** | Installs a cone table: wavelength, L, M, S; see [Cones, opponent channels and the cone table](cones-and-opponent-channels.md) |

Register entries: **sRGB transfer and primaries** (Verbatim), **Dichromacy projection** (Verbatim), **Cone transform** (Computed), **Spectral sensitivity table** (Stand-in), **Opponent axes** (Stand-in), **Spatial sensitivity** (Stand-in), **Cortical stage models** (Stand-in), **Viewing geometry** (Computed), **Spike raster** (Absent).

## Export tab

| Control | What it does |
|---|---|
| **What to take** | **A list of colours**, **The active map** (saves the PNG), **The settings** (downloads the JSON), **A link to this view** (copies the link) |
| **Colours** | Hex colours, one per line; commas and semicolons also separate |
| **Run them** | Redraws the table (it also updates as you type) |
| **Download the CSV** | Saves `cones-opponent.csv` |
| **Copy to clipboard** | Copies a tab-separated table |
| **Download the settings** | Saves `visual-pathway-settings.json` |

Table columns: **Input**, **L**, **M**, **S**, **L − M**, **S − (L+M)/2**, **L + M**.

## Reference tab

| Control | Values |
|---|---|
| **Reference** | **Standards** (5), **Formulas** (12), **Citations** (13, default), **Research notes** (7) |
| **Filter** | Searches all four groups at once; shows **Nothing in the reference matches that.** when empty |

A ● before a citation marks one the current version corrected. Each entry carries a tag such as **runs**, **not held**, **re-named**, **form only**, **stand-in**, **context** or **measured**.

## Messages

| Message | Meaning |
|---|---|
| **Cone table installed — L peaks at N nm** | A dropped table was accepted |
| **Not installed: too few rows** | Fewer than eight rows |
| **Not installed: row N has fewer than 4 columns** / **row N is not numeric** | A malformed row |
| **Not installed: wavelengths must increase** | Rows out of order |
| **Not installed: L and M peak N nm apart, which is not a cone table** | L and M peaks closer than 5 nm |
| **CSV saved**, **PNG saved**, **Settings exported**, **Copied**, **Link copied** | The action succeeded |
| **Copy blocked** | The browser refused clipboard access |
| **No colours to write** / **No colours to copy** | The colour list is empty |

## File formats

| File | Format | Contents |
|---|---|---|
| `cones-opponent.csv` | CSV with `#` comment lines | Chain, cone table and peaks, axes, geometry, reportable flag; columns `Input,L,M,S,RG,BY,Lum` |
| Clipboard table | Tab-separated text | `Input`, `L`, `M`, `S`, `RG`, `BY`, `Lum`, four decimals |
| `visual-pathway-<map>.png` | PNG, 256 × 256 | The selected map without its scale bar |
| `visual-pathway-settings.json` | JSON | See [Export and share](export-and-share.md) |
| Cone table (input) | CSV or JSON | Four columns: wavelength (nm), L, M, S; at least eight rows, increasing wavelengths |

## Link parameters

`source`, `baseHex`, `carrier`, `cpd`, `contrast`, `distanceCm`, `pitchMm`, `nOrient`, `rfSize`, `gaborCpd`, `gaborSigma`, `dogCenter`, `dogSurround`, `dogWeight`, `v4Preset` (`red`, `green`, `blue`, `yellow`, `orange`, `purple`), `cvdType` (`none`, `protan`, `deutan`, `tritan`), `colormap` (`viridis`, `inferno`, `grayscale`), `viewMap` (`retina-on`, `retina-off`, `lgn-rg`, `lgn-by`, `lgn-lum`, `v1`, `v1-orient`, `v2`, `v4`).
