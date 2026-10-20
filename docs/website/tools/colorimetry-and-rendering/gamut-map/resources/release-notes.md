---
title: Gamut Mapping — Release notes
description: User-facing changes to the Gamut Mapping lab.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Gamut Mapping release notes

## Current version (2026 workbench rebuild)

- Tabs are now **Lab**, **Boundary**, **Methods**, **Data**, **Export** and **Reference**.
- The four methods are renamed for what they do: **Chroma compression**, **Clip in target RGB**, **Uniform RGB scale** and **Adapt white, then clip**. They were previously labelled with ICC intent names, two of which were on the wrong method.
- Every space now decodes HEX values with its own transfer curve, and ProPhoto RGB uses its own D50 white, adapted onto the Lab plane.
- **Compression Strength** now affects the result of chroma compression.
- Gamut volume moved to the new **Boundary** tab, measured in a box fitted to each space and reported with a standard error. The xy-area percentage was removed.
- The new **Methods** tab compares the four methods on the base colour or 12 fixed probe colours.
- The new **Data** tab lists the nine datasets and their status.
- The Export tab offers PNG slices, a settings JSON, a link to the exact state and a 50-colour batch.

## May 2026

The Gamut Map User Guide was published in the site's Documentation library, describing the earlier version.
