---
title: Perception and Vision — Limits and accuracy
description: What Perception Vision takes from published sources, what is its own, how precise it is and what it is not.
product: Website › Tools › Perception and spectral › Perception and Vision
updated: 2026-09-25
---

# Limits and accuracy

## What the tool is

An educational and design-review simulator. It shows how an image may reach a viewer with a different visual system. It is not a clinical or diagnostic instrument and nothing it prints is a measurement of anyone's vision.

## The data register, in plain terms

| Entry | Status | What it means for you |
|---|---|---|
| sRGB transfer and primaries | Verbatim | Colours are decoded and re-encoded with the published IEC 61966-2-1 curve and matrices |
| Hunt-Pointer-Estévez cone fundamentals | Verbatim | Cone signals come from the published matrix, applied to CIE XYZ as it is defined |
| Bradford chromatic adaptation | Verbatim | The D50 and A options relight the scene with the published Bradford transform and CIE chromaticities |
| Dichromacy projection | Computed | Protan, deutan and tritan use the published Viénot, Brettel and Mollon (1999) matrices; the severity blend is the tool's convention |
| One implementation, two renderers | Computed | GPU and CPU use one combined matrix and are checked against each other on 216 colours |
| The shader's matrix literals | Computed | The GPU receives its matrices in the correct orientation; the grey ramp confirms it |
| Rod spectral weighting | Stand-in | Scotopic and Mesopic use the tool's own rod weights (0.10, 0.59, 0.31), not the CIE scotopic curve; no scotopic luminance is reported |
| Lens, cataract, acuity and adaptation models | Stand-in | Their constants are the tool's own; they show the direction of an effect, not its clinical size |
| Contrast sensitivity function | Absent | There is no contrast-sensitivity simulation; nothing may be reported as a contrast-sensitivity result |

## What is and is not modelled

- **Colour vision deficiency.** Full dichromacy follows a published method. Partial severities are a linear blend towards it, not a model of anomalous trichromacy. The matrices describe a typical dichromat and are not individualised.
- **Night and twilight vision.** A rod signal from the tool's own weights; the mesopic setting is a crossfade, not CIE mesopic photometry.
- **Lens yellowing and cataract.** Direction from the ageing literature (Pokorny, Smith and Lutze 1987 for the lens); strengths are the tool's own.
- **Central loss.** A disc of reduced luminance, not a model of any particular disease.
- **Acuity.** A blur sized from the Snellen denominator with no viewing distance; it does not show what a person with that acuity sees at your screen distance.
- **Illuminant.** A chromatic adaptation of the image as authored under D65; it is not a spectral relighting.

## Precision

- Colours are 8-bit sRGB in and out and are computed in floating point.
- The GPU and CPU colour results agree within 2 code values on the 216-colour check when **GPU and CPU agree** reads **yes**. Blur-based effects use slightly different filters in the two renderers, so spatial simulations can look a little different between them.
- **Colours merged**, **Out of sRGB**, **Distinct colours left** and **Largest channel shift** are measured on a 64 × 48 reduced copy of the source.
- Your screen is assumed to be sRGB. What you see also depends on your own display and your own eyes.

## What the tool does not do

- It does not test vision, diagnose or measure a person.
- It does not model anomalous trichromacy physiologically, contrast sensitivity, eye movements, or the time course of adaptation.
- It does not use the camera on auricartisan.com at present.
- The **Install a table** area on the Data tab is not active.
