---
title: Material Lighting (Material Under Light) — Run a sensitivity sweep
description: Use the Metrics tab to see how far the colour moves when the reflectance curve is perturbed, and read why the CRI and TM-30 figures were withdrawn.
product: Website › Tools › Perception and spectral › Material Lighting
updated: 2026-09-25
---

# Run a sensitivity sweep

A reflectance curve is never known exactly: a spectrophotometer's reading carries error, and the presets are inventions. The sweep asks how much that matters for the colour.

## Run it

1. Set up the scene on the **Lab** tab.
2. Open the **Metrics** tab. Under **Sensitivity sweep**:

   | Control | Range and step | Default | Meaning |
   |---|---|---|---|
   | **Perturbation** | ±0.005–0.1, step 0.005 | ±0.02 | The size of the random change to the reflectance, in reflectance units |
   | **Correlation length** | 0–120 nm, step 5 | 40 nm | How far along the spectrum neighbouring changes move together; 0 shows **independent** |
   | **Draws** | 100–2000, step 100 | 500 | How many perturbed curves to try |

3. Select **Run the sweep**. A message reports how many draws took how long.

## Read the result

Under **How far the colour moves when the curve does** appear **Median**, **95th percentile** and **Worst draw**, each a ΔE₀₀ between the unperturbed colour and a perturbed one. The note gives the number of draws and the time, and the line under the figures restates the perturbation and correlation, adding, for a synthesised material, that this is the sensitivity of the model, not of any pigment.

For gold under D65 with the defaults, the median is typically about 0.5 and the 95th percentile about 1.2. The draws are random, so each run differs slightly.

## Why the perturbation is correlated

A real instrument's error does not jump independently from one wavelength to the next; it drifts over tens of nanometres. The sweep smooths its random noise over the **Correlation length** so neighbouring wavelengths move together. Independent noise (correlation length 0) largely cancels when the spectrum is summed into a colour, and gives a misleadingly small spread: for the default scene, roughly half the correlated value.

This is a sensitivity sweep, not a bootstrap: there is no observed data to resample, so the page perturbs the curve and says by how much.

The result is written into the exports until you run another sweep or reset the scene; it is not rerun when the scene changes.

## What used to print here

Below the sweep, **What used to print here** (marked **2 withdrawn**) explains two rendering figures an earlier version printed.

A **colour rendering index** (CRI, CIE 13.3) scores how faithfully a light source renders a specified set of measured test colours, compared with its reference light, on a scale up to 100. **TM-30** (IES TM-30-20) is a newer method with a fidelity score, Rf, and a gamut score, Rg, over 99 samples.

- **CIE colour rendering index** — marked **Withdrawn**. The earlier version compared every source with D65 regardless of its temperature, used invented test colours and the wrong colour space. A table reruns that old formula for D65, D50, D55, illuminant A and blackbodies at 2700 K and 2000 K, beside the value each ought to have (100, since each is its own reference) and the tool's current colour difference for skin.
- **TM-30 Rf and Rg** — marked **Withdrawn**. Both old numbers were simple functions of the same fourteen values, so they could never disagree. A table shows this over several sources.

Each panel ends with **What it would take** to hold the index properly. The tool now holds the reference-selection rule, but not the measured sample sets or the colour spaces the indices need, so it prints neither.

You should now know how sensitive your material's colour is to errors in its curve.
