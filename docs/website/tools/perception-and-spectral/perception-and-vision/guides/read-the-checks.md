---
title: Perception and Vision — Read the checks
description: Understand the grey-ramp test, every readout under the frame, the renderer agreement check, and the Simulation and Modes tabs.
product: Website › Tools › Perception and spectral › Perception and Vision
updated: 2026-09-25
---

# Read the checks

The page does not ask you to trust its simulation. It shows checks you can read yourself. This guide explains each one.

## The grey ramp: the test that needs no reference

Under the frame, **The grey ramp, which is the test that needs no reference** shows nine grey steps from black to white, and under each step a number: how far apart the red, green and blue channels of that grey end up after the simulation, in 8-bit code values (0 to 255).

- For **Colour vision** the numbers must all be `0`. A dichromacy projection removes one colour axis and leaves the grey axis alone, so a person with a colour vision deficiency sees a grey as grey and white as white. A non-zero step is a defect and is shown in red. The note under the strip also shows what an earlier version of the page produced.
- For **Scotopic**, **Mesopic**, **Lens yellowing**, **Cataract** and **Light adaptation**, non-zero numbers are the effect itself: these simulations are meant to tint or shift neutrals. The note says so.
- For **Central loss** and **Acuity**, which depend on position rather than colour, the ramp measures only their colour part, which is none.
- For **None**, every number is zero.

The ramp leaves out the illuminant, because relighting a scene with illuminant A tints greys on purpose; including it would hide the signal the ramp exists to show.

## The readouts

| Readout | What it tells you |
|---|---|
| **Neutral drift** | The largest of the nine grey-ramp numbers; highlighted when it is above zero under Colour vision |
| **Colours merged** | The share of the frame's distinct colours that the simulation mapped onto a colour already taken by another, as a percentage |
| **Out of sRGB** | The share of the frame whose simulated colour fell outside what sRGB can show and had to be clipped |
| **GPU and CPU agree** | Whether the two renderers give the same answer on a grid of 216 colours: **yes** (within 2 code values), **N off**, **n/a — spatial** or **not run** |
| **Distinct colours left** | How many different colours remain after the simulation, out of how many before, for example **812 of 1540** |
| **Largest channel shift** | The biggest change in any channel of any pixel, in code values |
| **Frame luminance, mean** | The average relative luminance of what is on screen, from 0 to 1 |
| **min and max** | The darkest and lightest relative luminance on screen |

**Colours merged** is the figure a colour vision simulation is for: colours that were distinct and arrive at the same place are colours the simulated viewer cannot tell apart. The merged, out-of-sRGB, distinct and largest-shift figures are measured on a reduced copy of the source (64 × 48 pixels), so they describe the image's main colours rather than every pixel. They read **n/a** or **spatial mode** for **Cataract**, **Central loss** and **Acuity**, which change pixels according to their neighbours or position.

The luminance figures are read from the frame actually on screen, including the split and any adjustments.

The readouts refresh shortly after each change.

## Renderer agreement

The colour part of every simulation is one calculation that both renderers use. After each change the page draws 216 colours (six levels each of red, green and blue) on the GPU, reads them back, and compares them with the processor's answer. A gap of up to 2 code values counts as agreement and reads **yes**. The check covers colour only, so it reads **n/a — spatial** for Cataract, Central loss and Acuity, and **not run** when the GPU is unavailable. The settings file records the result.

## The Simulation tab

This tab follows a colour through the colour vision simulation.

**Show**

- **The chain** — the steps: **sRGB** (8-bit, encoded) → **linear** (the transfer curve) → **XYZ** → **LMS** (Hunt-Pointer-Estévez) → **project** (the 3×3 for the type) → **XYZ** → **linear** (and back to sRGB). The two XYZ steps are marked as ones an earlier version skipped.
- **The matrices** — four matrices to four decimals: **sRGB → XYZ**, **XYZ → LMS**, **project** for the type, and **the whole chain, in linear sRGB**, the single matrix both renderers use.

**Against**

- **What it was** (default) — the table adds **On screen** and **In the file** columns, the results an earlier version produced on screen and in its export, and **Apart**, the largest channel gap to the current result.
- **Hide** — current results only.

**Type** — **Protan**, **Deutan**, **Tritan** or **All three**.

The table runs seven colours (`#F59F00`, `#E03131`, `#C2255C`, `#1971C2`, `#2F9E44`, `#808080`, `#FFFFFF`) at severity 1.00 and shows each input and its result **Through XYZ** as swatches and hex. Under it, **The tell: a neutral must stay neutral** repeats the grey-ramp check for the chosen type.

## The Modes tab

This tab draws every simulation over the same source, as small previews computed on the processor.

- **Show**: **Everything** (all nine entries plus a card for the withdrawn **CSF overlay**) or **The eight that simulate**.
- **On**: **Test card**, **Grey ramp** or **Snellen chart**.
- **Severity**: **0.50** or **1.00** (default).

Each card gives the simulation's name, its source, a short explanation and a tag (**pass-through**, **space fixed**, **weights noted** or **runs**). The previews use fixed settings: adaptation level 0.35, age 70, cataract 0.60, scotoma radius 0.18 and acuity 20/90; the colour vision type follows the Lab. The CSF overlay card explains why a contrast-sensitivity mode was withdrawn. Below the grid, **Controls that were read and never used** lists six controls from an earlier version and whether each was removed or connected.

The previews are drawn when you first open the tab and when you press one of its buttons.

## The Data and Reference tabs

The **Data** tab lists nine entries with a status each: **Verbatim** (3), **Computed** (3), **Stand-in** (2) and **Absent** (1). Select a row, or press `Enter` or `Space` on it, to read its note and what it would take to hold it properly. The **Install a table** area on this tab (**Drop a CSV or JSON**) does not act on files in the current version.

The **Reference** tab groups its entries as **Standards** (7), **Formulas** (11), **Citations** (13, the default) and **Research notes** (9). **Filter** searches all four. A ● marks a citation the current version corrected.

You should now be able to tell, for any simulation, whether the page's own checks pass.
