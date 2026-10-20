---
title: Neuroscience (Visual Pathway) — Limits and accuracy
description: What the Visual Pathway takes from published sources, what is its own, how precise its numbers are and what it is not.
product: Website › Tools › Perception and spectral › Neuroscience
updated: 2026-09-25
---

# Limits and accuracy

## What the tool is

An educational simulation of how early vision transforms a stimulus. It is not a physiological model fitted to measurements, not a diagnostic tool and not a vision test. Nothing it shows is a measurement of any real visual system.

## The data register, in plain terms

The **Data** tab lists nine entries. This is what each means for the numbers you see.

| Entry | Status | What it means for you |
|---|---|---|
| sRGB transfer and primaries | Verbatim | Screen colours are decoded and converted with the published IEC 61966-2-1 curve and matrices |
| Dichromacy projection | Verbatim | The three colour-vision simulations use the published Viénot, Brettel and Mollon (1999) matrices, applied in cone space |
| Cone transform | Computed | Cone signals come from the published Hunt-Pointer-Estévez matrix applied to XYZ; greys sit within about 2.2 × 10⁻⁴ of zero on the chromatic axes |
| Spectral sensitivity table | Stand-in | The cone curves in the figure are the tool's own, with L and M both peaking at 590 nm; they draw the figure and nothing else |
| Opponent axes | Stand-in | L − M, S − (L+M)/2 and L + M are useful axes but are not DKL; nothing is in cone-contrast units |
| Spatial sensitivity | Stand-in | The weighting curve is the tool's own log-Gaussian peaking at 4 c/deg; it has no threshold criterion and gives no detection probability |
| Cortical stage models | Stand-in | Retina, V1, V2 and V4 use standard forms with constants chosen by the tool, with sizes in pixels rather than degrees |
| Viewing geometry | Computed | Degrees per pixel and the Nyquist limit follow exactly from the distance and pitch you enter |
| Spike raster | Absent | The tool has no time axis and no firing model, so nothing may be reported as a spike train or a firing rate |

A figure that depends on a stand-in or absent entry is never labelled as a published value. The settings file and CSV carry `reportable: false` (or the line "reportable against a published table: false") until you install a published cone table.

## Precision

- Colours are handled as 8-bit sRGB values and computed in double precision.
- The maps are 256 × 256 pixels. The V1 bank runs at half resolution (128 × 128) and is enlarged back, so V1 and V2 maps are blockier than the retinal and LGN maps.
- Every map is stretched to its own range. Compare maps by their scale-bar numbers, not by their brightness.
- The grating's contrast is capped where sRGB cannot show it; **Contrast achieved** gives the value used.
- The geometry is only as accurate as the viewing distance and pixel pitch you enter. The page cannot measure your screen or your seat.
- Your screen is assumed to follow the sRGB standard. An uncalibrated or wide-gamut screen shows the stimulus differently.

## What it does not do

- It does not model the eye's optics, eccentricity, eye movements or time: every stage is a single static frame.
- It does not simulate anomalous trichromacy or a partial deficiency: **Colour vision** is full dichromacy.
- It does not load your own images.
- It does not report detection probabilities, thresholds, spike trains or firing rates.
- The **Pupil** control does not change any output in the current version.
