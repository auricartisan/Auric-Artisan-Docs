---
title: Industrial Dye Chemistry (Dye in Solution) — Use a measured spectrum
description: Replace a drawn dye band with a measured UV–Vis molar absorptivity spectrum, and go back to the drawn bands.
product: Website › Tools › Perception and spectral › Industrial Dye Chemistry
updated: 2026-09-25
---

# Use a measured spectrum

The preset dyes' bands are drawn as Gaussian curves around a stated λmax. Real absorption bands are asymmetric, with a longer tail towards the blue, and the tails matter most where dyes overlap in a mixture. If you have a UV–Vis scan of a real dye, you can load it into one form of a dye in the bath.

## Prepare the file

- A plain-text file: `.csv`, `.tsv` or `.txt`.
- Two columns per line: **wavelength in nm** and **molar absorptivity** (ε, in M⁻¹ cm⁻¹). Columns may be separated by commas, semicolons, tabs or spaces.
- At least eight numeric rows, covering at least **420 to 680 nm**. Lines that are not two numbers (headers, comments) are skipped. Negative values are read as 0.

If your instrument exported absorbance rather than molar absorptivity, divide each absorbance by the concentration (in mol/L) and path length (in cm) of the measured sample first.

## Load it

1. On the **Lab** tab, select the dye whose band you want to replace in **The components** list.
2. Open the **Data** tab. Under **Measure your own dye**, choose **Into the acid form** or **Into the base form**.
3. Drop the file on **Drop a spectrum**, or select the area (or press `Enter` or `Space` on it) to choose the file. You can also drop the file directly on the spectrum plot on the Lab tab, or click the plot to choose a file; it goes into the form chosen on the Data tab.
4. Read the message: for example **74 rows into the acid form — peak 506 nm, ε 25300**, or **Not installed:** with a reason.

## What changes

- The file is resampled onto the 5 nm grid from 380 to 780 nm by straight-line interpolation between your rows. Beyond the ends of your file, the first and last values are held flat.
- That form's λmax and ε become the peak of your curve.
- The dye's tag in the components list changes from **Stand-in** to **Measured**.
- On the **Data** tab, **The absorption band shape** entry changes to **Verbatim**, with your file name and the span it covered.
- The CSV header and JSON mark the band shape as **MEASURED** and the component's provenance as `measured`.
- **Back to the drawn bands** appears on the Data tab.

The dye's pKa and concentration are unchanged; the pH still sets how much of it is in each form. If you have scans of both forms, load both.

## Go back

Select **Back to the drawn bands**. The selected dye's bands return to its preset, and every measured curve in the bath is cleared. A message confirms **Back to the drawn bands**. **Reset the bath** also clears measured curves.

Measured spectra are not carried by links and are lost when you reload the page.

You should now have a dye in the bath whose band is your own measurement.
