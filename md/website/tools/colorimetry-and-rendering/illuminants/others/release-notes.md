---
title: Illuminants — Release notes
description: User-facing changes to the Standard Illuminants lab.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Illuminants release notes

## September 2026 — the workbench rebuild

The lab was rebuilt around a new colorimetric core and a new layout.

- New tabs: **Chromaticity**, **Uncertainty**, **Methods**, **Console** and **Data** join Lab, Export and Reference.
- CCT and Duv are now computed with Ohno's method, with a signed Duv and a validity check. The older McCamy figure is shown only on the Methods tab for comparison.
- The daylight illuminants are rebuilt from the published daylight basis at its tabulated interval, and Illuminant A is computed as defined (2848 K with the 1931 constant, measuring 2856 K).
- Chromatic adaptation now offers Bradford, CAT16, CAT02, Von Kries, Sharp, XYZ scaling and None, with the matrix shown.
- A provenance line under results names the dataset, observer and interval.
- A data register marks each dataset verbatim, computed, stand-in or absent. Fluorescent spectra and CRI test samples are labelled as stand-ins; TM-30 is shown as not computed rather than estimated.
- The Standards, Formulas, References and Research tabs became one **Reference** view with a search filter and status chips; the citation list grew to 22 entries, each marked Runs here, Data missing or Context only.

## May 2026

The Illuminants User Guide was published in the site's Documentation library, describing the earlier version of the lab (Lab, Actions, Standards, Formulas, References and Research tabs).
