---
title: Tonal Steps — Release notes
description: User-facing changes to Tonal Steps, Tints and Shades.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Tonal Steps release notes

## Current version (2026 workbench rebuild)

- Tabs are now **Lab**, **Ramps**, **Contrast**, **Data**, **Export** and **Reference**.
- OKLab now receives linear sRGB, as its definition requires. OKLab lightness values, the lightness chart and the OKLab mixing mode changed for every tone except black, white and the primaries.
- The Lab offers two ramp engines instead of three: the equal-contrast engine produced the same colours as equal luminance (and ran in reverse). The Ramps tab shows all three side by side.
- The equal-luminance engine's end steps are exactly white and black.
- The APCA column now runs APCA-W3 0.1.9 as published. The Contrast tab can show the former approximate figure and the difference.
- The "Tailwind 50–950" and "Material 50–900" scales are now presented as key sets that borrow the names only.
- New evenness measures in OKLab L, CIELAB L* and relative luminance.
- Exports now carry a header recording the base, engine, mixing space, steps and gamma, and a footer recording the OKLab input, WCAG and APCA versions.
- The share link control works and the link field always shows the current link.

## May 2026

The Tonal Steps, Tints and Shades User Guide was published in the site's Documentation library, describing the earlier version.
