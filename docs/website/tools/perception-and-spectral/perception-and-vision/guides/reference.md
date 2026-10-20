---
title: Perception and Vision — Reference
description: Every tab, control, readout, message and file format in Perception Vision, with ranges and defaults.
product: Website › Tools › Perception and spectral › Perception and Vision
updated: 2026-09-25
---

# Perception and Vision reference

Address: https://auricartisan.com/tool/general/perception-and-neuroscience/perception-vision/

## Tabs

| Tab | Contents |
|---|---|
| **Lab** | Source, simulation, comparison, renderer, illuminant, adjustments and presets; the frame, grey-ramp check and readouts |
| **Simulation** | The colour vision chain, its matrices and a seven-colour table, with an earlier-version comparison |
| **Modes** | Previews of every simulation over one source, and the list of controls from an earlier version |
| **Data** | The register of nine datasets and transforms, filterable by status; the tab label shows the count (9) |
| **Export** | Colour list, CSV, clipboard, settings download and load, link |
| **Reference** | Standards, formulas, citations and research notes, with a search box |

## Lab tab — Source

| Control | Values | Default |
|---|---|---|
| **Source** | **Test card**, **Grey ramp only**, **Snellen chart**, **Uploaded image**, **Camera** | Test card |
| **Choose a file** | Opens a file chooser for images (shown for Uploaded image); images are fitted within 1200 × 900 | — |
| **Start or stop** | Switches the camera (shown for Camera); status **off**, **active** or **unavailable** | off |

## Lab tab — Simulation

| Control | Values or range | Default | Shown for |
|---|---|---|---|
| **Simulation** | **Colour vision**, **Scotopic**, **Mesopic**, **Lens yellowing**, **Cataract**, **Central loss**, **Light adaptation**, **Acuity**, **None** | Colour vision | Always |
| **Type** | **Protan**, **Deutan**, **Tritan** | Protan | Colour vision |
| **Daltonise instead of simulate** | On or off | Off | Colour vision |
| **Severity** | 0–1, step 0.01 | 1.00 | Always |
| **Adaptation level** | 0–1, step 0.01 | 0.50 | Mesopic, Light adaptation |
| **Age** | 20–80, step 1 | 40 | Lens yellowing |
| **Scotoma radius** | 0.02–0.45, step 0.01 | 0.15 | Central loss |
| **Cataract** | 0–1, step 0.01 | 0.50 | Cataract |
| **Acuity** | 20/20–20/200, step 5 | 20/20 | Acuity |

## Lab tab — Compare and renderer

| Control | Values or range | Default |
|---|---|---|
| **Compare** | **Split**, **Simulated only**, **Difference** (absolute difference × 4) | Split |
| **Divider** | 0–100%, step 1%; also set by dragging on the frame (Split only) | 50% |
| **Renderer** | **GPU**, **CPU**; GPU is disabled without WebGL2 | GPU |
| **Fixation cross** | Draws a cross and ring at the frame centre | Off |

## Lab tab — Before the eye

| Control | Values or range | Default |
|---|---|---|
| Illuminant | **D65 — as authored**, **D50**, **A — tungsten** | D65 |
| **Adaptation** | 0–1, step 0.01 (Bradford strength) | 1.00 |

## Lab tab — Adjustments

| Control | Range and step | Default |
|---|---|---|
| **Contrast** | −0.9 to 0.9, step 0.01 | 0.00 |
| **Gamma** | 0.4 to 2.6, step 0.01 | 1.00 |
| **Blur** | 0 to 8, step 0.1 | 0.0 |
| **Glare** | 0 to 1, step 0.01 | 0.00 |
| **Noise** | 0 to 0.08, step 0.001 | 0.000 |

## Lab tab — Presets

| Control | Values |
|---|---|
| **Presets** | **—**, **Protanopia**, **Mild deuteranomaly**, **Tritanopia**, **Low light with glare**, **Lens at 70**, **Cataract**, **Central loss**, **Acuity 20/80** (values in [Simulate a design or image](simulate-a-design.md)) |
| **Reset** | Returns every control to its default and stops the camera |

## Lab tab — Stage elements

| Element | Description |
|---|---|
| Caption | The simulation, type and severity, or **The frame, unchanged** |
| Renderer note | A dot (green when WebGL2 is available), **GPU** or **CPU**, and the frame size |
| Frame | The simulated view; in Split the halves are labelled **Original** and the simulation's name; the line under it names the method's source |
| **No WebGL2 here.** | Shown when the browser has no WebGL2; the CPU is used |
| Grey-ramp strip | Nine steps and the channel spread added to each, in code values |
| **Save the frame** | Downloads `perception-<simulation>-<severity × 100>.png` |
| **Copy a link to this view** | Copies a link to the current settings |

## Lab tab — Readouts

| Readout | Format |
|---|---|
| **Neutral drift** | Code values, 0–255 |
| **Colours merged** | Percentage, one decimal; **n/a** for spatial simulations |
| **Out of sRGB** | Percentage, one decimal; **n/a** for spatial simulations |
| **GPU and CPU agree** | **yes**, **N off**, **n/a — spatial** or **not run** |
| **Distinct colours left** | **N of M**, or **spatial mode** |
| **Largest channel shift** | Code values; **n/a** for spatial simulations |
| **Frame luminance, mean** | Relative luminance, four decimals |
| **min and max** | Relative luminance, four decimals |

Simulation identifiers used in file names and links: `none`, `cvd`, `scotopic`, `mesopic`, `age-yellowing`, `cataracts`, `macular-degeneration` (Central loss), `photopic-adaptation` (Light adaptation), `acuity`.

## Simulation tab

| Control | Values | Default |
|---|---|---|
| **Show** | **The chain**, **The matrices** | The chain |
| **Against** | **What it was**, **Hide** | What it was |
| **Type** | **Protan**, **Deutan**, **Tritan**, **All three** | Protan |

Table columns: **Input**, **Type**, **Through XYZ**, and with **What it was** also **On screen**, **In the file** and **Apart**.

## Modes tab

| Control | Values | Default |
|---|---|---|
| **Show** | **Everything**, **The eight that simulate** | Everything |
| **On** | **Test card**, **Grey ramp**, **Snellen chart** | Test card |
| **Severity** | **0.50**, **1.00** | 1.00 |

## Data tab

| Control | What it does |
|---|---|
| **Status** | **All** (9), **Verbatim** (3), **Computed** (3), **Stand-in** (2), **Absent** (1) |
| Register row | Select, or press `Enter` or `Space`, to expand the note and **What it would take** |
| **Drop a CSV or JSON** | Shown under **Install a table**; not active in the current version |

Entries: **sRGB transfer and primaries**, **Hunt-Pointer-Estévez cone fundamentals**, **Bradford chromatic adaptation** (Verbatim); **Dichromacy projection**, **One implementation, two renderers**, **The shader's matrix literals** (Computed); **Rod spectral weighting**, **Lens, cataract, acuity and adaptation models** (Stand-in); **Contrast sensitivity function** (Absent).

## Export tab

| Control | What it does |
|---|---|
| **What to take** | **A list of colours**, **The frame**, **The settings**, **A link to this view** |
| **Colours** | Hex colours, one per line; commas and semicolons also separate |
| **Run them** | Redraws the table (it also updates as you type) |
| **Download the CSV** | Saves `perception-<simulation>-<severity × 100>.csv` |
| **Copy to clipboard** | Copies a tab-separated table |
| **Download the settings** | Saves `perception-vision-settings.json` |
| **Load settings** | Applies a settings JSON file |

## Reference tab

| Control | Values |
|---|---|
| **Reference** | **Standards** (7), **Formulas** (11), **Citations** (13, default), **Research notes** (9) |
| **Filter** | Searches all four groups; shows **Nothing in the reference matches that.** when empty |

## Messages

| Message | Meaning |
|---|---|
| **Preset: …** | A preset was applied |
| **Reset** | All controls returned to defaults |
| **Camera: …** | The camera could not start; the source returned to the test card |
| **PNG saved**, **CSV saved**, **Settings exported**, **Settings imported**, **Copied**, **Link copied** | The action succeeded |
| **Import failed: …** | The settings file could not be read |
| **Copy blocked** | The browser refused clipboard access |
| **No colours to write** / **No colours to copy** | The colour list is empty |

## File formats

| File | Format | Contents |
|---|---|---|
| `perception-<simulation>-<severity>.png` | PNG | The frame at its own size, with the divider and fixation cross if shown |
| `perception-<simulation>-<severity>.csv` | CSV with `#` comment lines | `Input,Simulated,L,M,S,RG,BY,DeltaE00,InSRGB` |
| Clipboard table | Tab-separated text | `Input`, `Simulated`, `L`, `M`, `S`, `DeltaE00`, `InSRGB` |
| `perception-vision-settings.json` | JSON | See [Check a palette and export](check-a-palette-and-export.md) |

## Link parameters

`simMode`, `cvdType` (`protan`, `deutan`, `tritan`), `severity`, `contrast`, `gamma`, `blur`, `noise`, `bloom` (glare), `adaptLevel`, `age`, `scotomaR`, `cataractLvl`, `acuity`, `illum` (`D65`, `D50`, `A`), `adaptStrength`, `compare` (`split`, `sim`, `diff`), `source` (`sample`, `ramp`, `snellen`, `upload`, `camera`), `renderer` (`gpu`, `cpu`).
