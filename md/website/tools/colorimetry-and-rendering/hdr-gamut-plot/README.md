---
title: HDR Gamut Plot — Overview
description: What the HDR Gamut Plot does, who it is for, where to find it and how to take your first reading.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# HDR Gamut Plot

High dynamic range (HDR) video changes two things at once: it widens the **gamut** (more saturated colours, typically Rec. 2020 primaries) and extends the **luminance range** (from about 100 nits for standard video to as much as 10,000 nits). The HDR Gamut Plot puts both on screen.

It draws the three broadcast gamuts — Rec. 709/sRGB, Display P3 and Rec. 2020 — on a CIE 1931 xy or CIE 1976 u′v′ chromaticity diagram, and measures each as a share of the spectral locus. It plots the HDR transfer curves (PQ from SMPTE ST 2084 and HLG from BT.2100, with its system gamma) against standard gamma 2.2 and 2.4, on an axis in real cd/m². It draws the gamuts in two HDR perceptual spaces, ICtCp and Jzazbz, at a luminance you choose, and stacks their boundaries at eight luminance levels from 0.1 to 10,000 nits. You can also drop in an image to measure how much of each gamut its colours occupy.

The page is careful about what a nit is. A PNG or JPEG does not record absolute luminance, so the lab does not claim one from an image; where a luminance comes from the peak-brightness control rather than from a signal, it says so.

## Who it is for

- Video, streaming and games developers working with HDR10, HLG or wide-gamut content.
- Designers preparing assets for P3 and HDR displays.
- Students learning PQ, HLG, ICtCp and the difference between absolute and display-referred curves.

## Where to find it

- Address: https://auricartisan.com/tool/general/gamut-and-rendering/hdr-gamut-plot/
- In the tool collection (https://auricartisan.com/collections/) under **Gamut & Rendering**, as **HDR Gamut Plot**.

## Quick start

1. Open https://auricartisan.com/tool/general/gamut-and-rendering/hdr-gamut-plot/. The diagram shows the three gamuts on CIE 1931 xy.
2. Read **Gamut metrics**: each space's primaries, white, share of the locus and area.
3. Move the pointer over the diagram to read x, y, XYZ, L* and ICtCp values under it.
4. Press `A` to switch to the u′v′ diagram, then `A` again to switch back.
5. Open **Curves**, set **Peak brightness** to 1000 nits, and press `3` (PQ) and `4` (HLG) to compare the curves.
6. Open **Planes** to see the gamuts in ICtCp at the luminance set by **Signal level**.
7. Open **Export**, choose **The measurements** as **CSV**, and select the download button.

## What you can do

- Compare Rec. 709/sRGB, Display P3 and Rec. 2020 on xy or u′v′, with the spectral locus and line of purples.
- Read each gamut's area and share of the spectral locus in the plane on screen.
- Plot PQ, HLG, gamma 2.4 (BT.1886) and gamma 2.2 as absolute luminance against signal.
- Set peak brightness (100 to 10,000 nits) and HLG surround, and read HLG's system gamma.
- View the gamuts in ICtCp or Jzazbz at a chosen luminance, and as boundary rings at eight luminance levels.
- Measure how much of each gamut an image's colours occupy.
- Convert a list of HEX colours to CIELAB, ICtCp and Jzazbz.
- Export measurements (CSV, JSON, CSS), the curve (CSV), the diagram, curve plot and plane (PNG), or a link.

## In this folder

- [docs/](docs/README.md) — how to use the tool
  - [Getting started](docs/getting-started.md)
  - [Compare broadcast gamuts](docs/compare-broadcast-gamuts.md)
  - [Read HDR transfer curves](docs/read-hdr-curves.md)
  - [Explore ICtCp and Jzazbz planes](docs/explore-perceptual-planes.md)
  - [Reference](docs/reference.md)
  - [Troubleshooting](docs/troubleshooting.md)
  - [FAQ](docs/faq.md)
- [others/](others/README.md) — background and supporting pages
  - [Glossary](others/glossary.md)
  - [Shortcuts](others/shortcuts.md)
  - [Limits and accuracy](others/limits-and-accuracy.md)
  - [Related tools](others/related.md)
  - [Release notes](others/release-notes.md)
  - [Privacy](others/privacy.md)
