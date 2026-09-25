---
title: Vision Lab — Use the Workbench
description: Take one condition apart in the Workbench: choose a specimen, set the base colour, severity and model, and read what collapses.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Use the Workbench

The Workbench shows one condition at a time, in three columns: the source on the left, the stage in the middle, and the list of conditions on the right. It opens with **Deuteranopia** selected, or with the condition named in the page address.

## The source column

### Specimen

What the stage shows:

| Specimen | What you see |
| --- | --- |
| **Interface** | A small interface mock-up: a header with a **Get started** button, and a "Palette health" card |
| **Palette** | The ten reference swatches as a strip |
| **Image** | Your own image: drop it on the stage, or select **Choose an image** |

With the **Image** specimen, the stage says "Drop an image on the stage" and "Whatever you drop stays on your machine — the pipeline runs in this tab and nothing is uploaded." To open a condition's floating panel, see [Browse the Catalogue and panels](browse-the-catalogue-and-panels.md).

### Base colour

Type a hex colour into the field (up to seven characters, such as `#E53E3E`). Next to it, "under condition →" shows the colour it becomes. Under the field, ten swatches (the reference strip) each have a **Use** button that makes that swatch the base colour.

### Severity

A slider from 0 to 100%, with marks for **Normal**, the condition's clinical default (for example **Clinical default 100%**) and **Full**. The figure above it says how strongly the condition is expressed, for example "100% · full expression".

Selecting a condition resets the slider to that condition's clinical default. As the page puts it: "Severity is a dial on the model, not a milder diagnosis."

### Model

For the colour-vision conditions, choose how the simulation is calculated: **Brettel**, **Viénot** or **Machado**. The note beside the heading describes the method, for example "projection in LMS" (LMS being the three cone types). See [Limits and accuracy](../others/limits-and-accuracy.md) for how the models differ.

### Stage

- **Split** shows the reference and the simulation side by side.
- **Simulated only** shows just the simulation.

## The stage

The heading names what you are looking at, for example "COLOUR TRANSFORM · Deuteranopia · 100%". Under the stage are two readouts.

### What collapses

Pairs of reference colours that were comfortably apart (CIEDE2000 of 12 or more) and land within 8 under this condition, ranked by how far they fell. The heading says how many, for example "2 of 45 reference pairs fall under ΔE2000 8", and each pair shows its distance before and after, such as "24 → 1.5".

The ten reference swatches make 45 pairs. A pair that collapses is two colours that a person with this condition can no longer tell apart.

### Measured · base colour

| Measure | Meaning |
| --- | --- |
| **ΔE76** | How far the base colour moved, as a simple distance in Lab colour space |
| **ΔE2000** | How far it moved, with the CIEDE2000 formula, which follows perceived difference more closely |
| **pairs lost / 45** | How many reference pairs collapsed |
| **button label / fill** | The contrast ratio of the mock-up's button label against its fill, under the condition |

ΔE (delta E) is a measure of colour difference: around 1 is barely noticeable, and larger numbers mean more obvious differences.

## The conditions column

- **Search 78 conditions** filters the list by name.
- Filter buttons: **All 78**, **Colour** (the 17 per-colour transforms), **Field** (the 61 field effects) and **Basic only**.
- The selected condition is described at the top: its severity score in a ring, its name and category, a one-line description (for example "Green-cone absent. A per-colour transform: every pixel has an answer."), and chips for its kind, its prevalence and its level.
- Below, every condition is listed by category, with its severity score. Field conditions are marked **FIELD**.

Select a condition to put it on the stage.

## The action rail

| Button | What it does |
| --- | --- |
| **Open the full panel** | Opens this condition as a floating panel with every advanced control |
| **Compare this** | Sends the condition to the **Compare** sheet |
| **Copy link to this view** | Copies a link that reopens the Workbench on this condition, severity and model |

The rail also notes "78 conditions · 11 categories" and "Brettel 1997 · Viénot 1999 · Machado 2009, in linear light".

## What is remembered

The Workbench remembers your condition, severity, model, specimen and base colour in this browser, and a link with `?vw=` restores a condition directly. See [Links, saving and exports](links-saving-and-exports.md).
