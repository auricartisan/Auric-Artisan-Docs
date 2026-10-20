---
title: Industrial Dye Chemistry (Dye in Solution) — Release notes
description: User-facing history of the Dye in Solution tool.
product: Website › Tools › Perception and spectral › Industrial Dye Chemistry
updated: 2026-09-25
---

# Release notes

The site-wide history is at https://auricartisan.com/library/changelog/. The entries below cover what changed for users of this tool.

## September 2026 — rebuilt as Dye in Solution

The page was rebuilt with six tabs (**Lab**, **Method**, **Safety**, **Data**, **Export**, **Reference**).

Changed:

- Each dye is now two forms (acid and base) weighted by pH, so the pH control changes every dye's colour through its pKa, and a titration shows an isosbestic point. Earlier, most presets did not respond to pH at all.
- The colour is computed under a named light source, and L\*a\*b\* is taken against that light's own white. Earlier there was no light source.
- The spectrum is sampled at 5 nm from 380 to 780 nm, the grid the CIE observer is published on.
- The preset list is now six dye classes with the tool's own constants, instead of named commercial dyes with unsourced values.
- **Dominant λ** is now a true dominant wavelength with excitation purity, rather than the wavelength of peak transmittance.

Added: the illuminant menu (D65, D50, A, E) and the lights row with colour inconstancy; the **Beer–Lambert holds** check; **Base fraction** and **Isosbestic point**; the tolerance sweep; loading measured spectra; the **Data** register; header lines stating the method in every export.

Removed:

- The confidence interval that resampled the recipe, replaced by the tolerance sweep.
- The GHS hazard levels and the tick-box gate on exports; the **Safety** tab explains why.

## Earlier

- An Industrial Dye Chemistry User Guide for the previous version was published in the site documentation in May 2026; it is now marked as superseded.
