---
title: Perception and Vision — Release notes
description: User-facing history of the Perception Vision tool.
product: Website › Tools › Perception and spectral › Perception and Vision
updated: 2026-09-25
---

# Release notes

The site-wide history is at https://auricartisan.com/library/changelog/. The entries below cover what changed for users of this tool.

## September 2026 — rebuilt

The page was rebuilt with six tabs (**Lab**, **Simulation**, **Modes**, **Data**, **Export**, **Reference**). The **Simulation** tab can show the results an earlier version produced on screen and in its export beside the current ones.

Changed:

- The colour vision simulation now converts through CIE XYZ into cone signals before projecting, as the published method defines, and the screen and the export use the same calculation. Colours in earlier exports and screenshots can differ widely from current results; white now stays white under every type.
- Uploaded images are no longer drawn upside down.
- The readouts refresh after every change.
- The hero now counts eight simulations; **None** is listed but not counted.

Added:

- A CPU renderer, used automatically when WebGL2 is not available, and a check that the GPU and CPU agree.
- The grey-ramp strip, **Neutral drift**, **Colours merged**, **Distinct colours left**, **Out of sRGB** and **Largest channel shift**.
- The **Grey ramp only** and **Snellen chart** sources.
- **Load settings**, and the chain, matrix, illuminant and renderer check in the settings file and CSV header.

Connected (these controls previously did nothing): **Blur**, **Glare**, the illuminant with its **Adaptation** strength, and **Fixation cross**.

Removed: the CSF overlay simulation and the test overlay checkbox.

## May 2026

- The Perception & Vision User Guide was published in the site documentation.
