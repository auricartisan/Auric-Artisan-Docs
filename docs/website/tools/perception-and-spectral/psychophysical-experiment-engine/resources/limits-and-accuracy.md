---
title: Psychophysical Experiment Engine — Limits and accuracy
description: What the Psychophysics Bench takes from published sources, what is its own, the limits of an uncalibrated screen, and what it does not show.
product: Website › Tools › Perception and spectral › Psychophysical Experiment Engine
updated: 2026-09-25
---

# Limits and accuracy

## What the bench is

An educational instrument for measuring a contrast detection threshold in a browser. It is not a calibrated laboratory system and not a clinical test. Results depend on your screen, your room and your attention as much as on your vision.

## The data register, in plain terms

| Entry | Status | What it means for you |
|---|---|---|
| sRGB transfer and primaries | Verbatim | Contrast is converted to screen values with the standard sRGB curve, which is a standard, not a measurement of your screen |
| Transformed up-down rules | Verbatim | 1-up / 2-down and 3-down / 1-up follow Levitt (1971), including averaging an even number of reversals |
| Extreme-proportion correction | Verbatim | The 1/2N rule of Macmillan and Kaplan (1985) for hit rates of 1 or false-alarm rates of 0 |
| Michelson contrast in luminance | Computed | Every contrast is placed symmetrically around the background's luminance, so the contrast asked for is the contrast drawn, unless capped |
| Viewing geometry | Computed | Degrees per pixel and the Nyquist limit follow exactly from the distance and pitch you enter |
| Signal-detection formulae | Computed | d′, criterion and β as in Macmillan and Creelman (2005), for yes/no only |
| Inverse normal CDF | Computed | An approximation accurate to 4.5 × 10⁻⁴; it caps any d′ at about 6.18 |
| Nonparametric bootstrap | Computed | A trial bootstrap; it gives intervals that are too narrow for adaptively sampled data |
| Bayesian adaptive staircase | Stand-in | The tool's own tracker, not QUEST; its slope and lapse rate are assumed |
| Psychometric function fit | Stand-in | A logistic with the task's guess rate and a fitted lapse rate; search and binning are the tool's own |
| Accelerated staircase | Stand-in | The tool's own; not PEST, and no stated target percentage |
| Weibull fit | Absent | No Weibull function is ever fitted to data |
| ROC curve and its area | Absent | A single yes/no criterion gives one point, not a curve |

Because the fit is a stand-in, exports carry `reportable: false`.

## Limits of a screen

- **No calibration.** The page assumes the sRGB curve. Real screens differ, and brightness, contrast and colour settings change the light that reaches you. A measured display calibration cannot be loaded in the current version.
- **8-bit steps.** Near threshold, a stripe pattern may differ from the background by only one or two screen code values, so the smallest contrasts the page can draw are coarse. The page does not dither.
- **Capped contrast.** A bright background cannot hold high contrast; the page caps it and says so.
- **Geometry you enter.** The frequency and envelope in degrees are only as accurate as the distance and pixel pitch you give, and assume you stay put.
- **Timing.** Durations are timed by the browser and shown on the screen's refresh; background load can delay them.

## What the bench does not show

In the current version no readout displays the psychometric fit, d′, criterion, β or bootstrap interval, although the register describes them. The threshold shown comes from the staircase itself: the reversal average or the Bayesian tracker's estimate.

## What it does not do

- Only two tasks run: two-interval forced choice and yes/no. m-alternative, same/different and odd-one-out are withdrawn.
- Constant stimuli tests only the starting contrast.
- At the time of writing, only the Lab tab opens, so exports cannot be made.
