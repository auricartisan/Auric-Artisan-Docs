---
title: Illuminants — Estimate measurement uncertainty
description: Propagate a spectroradiometer uncertainty budget into x, y, CCT and Duv with the Monte Carlo view.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Estimate measurement uncertainty

A measured spectrum is never exact. The wavelength scale may be slightly off, the instrument's slit blurs sharp peaks, and the detector adds noise. The **Uncertainty** tab asks how much those errors move the numbers you would report: x, y, CCT and Duv.

It uses the **Monte Carlo method** described in JCGM 101:2008 (Supplement 1 to the Guide to the Expression of Uncertainty in Measurement): it perturbs the spectrum thousands of times at random, according to the error sizes you give, and measures the spread of the results.

## The input budget

The budget is preset for a typical array spectroradiometer. It is a starting point, not your instrument: every value is editable. Hover over a label to see what the term models and whether it is treated as a normal or a rectangular distribution.

| Term | Unit | Preset | Distribution | What it models |
| --- | --- | --- | --- | --- |
| Wavelength scale | nm | 0.20 | Normal | A shift of the whole wavelength axis. Dominates on a spiky source. |
| Bandwidth (FWHM) | nm | 5.0 | Rectangular | The finite slit width, modelled as a triangular blur. |
| Stray light | relative | 0.0001 | Rectangular | A flat pedestal added across the range. |
| Non-linearity | % | 0.10 | Rectangular | A gain error that depends on signal level. |
| Detector noise | % | 0.05 | Normal | Independent noise at each wavelength. |
| Reference lamp | % | 0.80 | Normal | The calibration scale. Largely cancels in chromaticity. |

For a normal term the value is one standard uncertainty. For a rectangular term the value is the half-width of the range, so its standard uncertainty is the value divided by √3.

## Steps

1. On the **Lab** tab, choose the illuminant you want to study. The Uncertainty tab always works on the light currently selected in the Lab.
2. Open the **Uncertainty** tab.
3. Edit any budget value. Negative or non-numeric entries are reset to 0.
4. Under **Trials**, choose **1k**, **4k** (the default) or **20k**. More trials give a steadier estimate and take longer.
5. Select **Run the propagation**. The button shows "Running…" and then returns.
6. Read **Expanded uncertainty, k = 2**. For each of x, y, CCT and Duv the table shows:
   - **Value** — the reading itself;
   - **u** — the standard uncertainty;
   - **U (k=2)** — the expanded uncertainty, twice u, which covers about 95% of cases for a normal distribution;
   - **Relative** — U as a percentage of the value. Figures over 5% are highlighted.
7. Read **Contribution to u(CCT)**. Each bar shows the share of the CCT uncertainty caused by one budget term. Bars above 40% are highlighted.
8. Look at **95% coverage region in u′v′**. The solid ellipse is the region that holds 95% of the simulated chromaticities; the dashed ellipse is one standard deviation. The centre coordinates are printed in the corner.
9. The line under the results records the number of trials, how long the run took, the observer and the interval.

## Reading the result

- For a smooth source such as D65 or a blackbody, the wavelength and bandwidth terms usually matter little. For a spiky source they can dominate.
- The reference lamp term mostly changes absolute level, which cancels when you compute chromaticity, so its share of the CCT uncertainty is small.
- The inputs are treated as uncorrelated. The page says so under the results.
- The contribution bars come from a shorter run (about a sixth of the trials, never fewer than 200), so they can move slightly between runs.

## Tips

- The interval and interpolation set on the **Methods** tab also apply here.
- Monte Carlo results vary a little each time. If two runs differ more than you are comfortable with, use **20k** trials.

## Result

You have expanded uncertainties for x, y, CCT and Duv, a ranking of which error source matters most, and a picture of the 95% region in u′v′.
