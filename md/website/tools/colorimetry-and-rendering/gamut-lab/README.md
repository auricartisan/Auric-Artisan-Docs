---
title: Gamut Lab — Overview
description: What the Gamut Lab does, who it is for, where to find it and how to compare your first colour spaces.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Gamut Lab

The Gamut Lab shows where an RGB colour space ends. Every RGB space is defined by three **primaries** (the reddest red, greenest green and bluest blue it can make), a **white point**, and a **transfer function** that turns stored values into light. Plot the primaries on a chromaticity diagram and they form a triangle: the space's **gamut**. The lab draws those triangles for 13 standard spaces — from sRGB and Display P3 to Rec. 2020, the HDR Rec. 2100 encodings, Adobe RGB, ProPhoto RGB, the ACES spaces and legacy television standards — plus any space you define yourself.

Beyond the diagram, it derives the RGB-to-XYZ matrices from the primaries, draws each space's transfer curve (and tells you whether that curve is exactly the one its standard defines), slices gamuts at constant lightness in CIELAB, and measures gamut volume in CIELAB and overlap in u′v′ with quasi-random sampling. You can keep your own spaces in a library in your browser, import and export them as JSON, and export the diagram as SVG or PNG.

The Gamut Lab defines and measures spaces. It does not map colours from one space into another; that is the job of [Gamut Mapping](../gamut-map/README.md).

## Who it is for

- Designers and developers choosing a working or output colour space.
- Video, VFX and HDR practitioners comparing Rec. 709, P3, Rec. 2020 and ACES.
- Display and camera engineers checking primaries and matrices for a custom space.
- Students learning chromaticity diagrams, transfer functions and gamut volume.

## Where to find it

- Address: https://auricartisan.com/tool/general/gamut-and-rendering/gamut/
- In the tool collection (https://auricartisan.com/collections/) under **Gamut & Rendering**, as **Gamut Explorer**. The page itself is titled **Gamut Lab**.

## Quick start

1. Open https://auricartisan.com/tool/general/gamut-and-rendering/gamut/. The diagram shows sRGB, Display P3 and Rec. 2020 on the CIE 1931 xy diagram.
2. Under **Working color space**, choose **Adobe RGB**. Its triangle is added and its primaries, white point and matrices appear in the panel.
3. Click inside the diagram. **Vertex readout** shows the x, y you clicked, a colour chip and which spaces contain that chromaticity.
4. Change **Diagram mode** to **CIE 1976 u′v′** to see a more evenly spaced diagram.
5. Open the **Compare** tab and select **Measure them all**.
6. Open **Transfer** to see every transfer curve and whether it is exact.
7. Open **Export**, choose **The diagram** and **SVG**, and select the download button.

## What you can do

- Draw 13 standard RGB spaces and your own on CIE 1931 xy or CIE 1976 u′v′ diagrams, or as 3-D wireframes in CIELAB.
- Read a space's primaries, white point and both RGB ↔ XYZ matrices, and solve the matrices for custom primaries.
- Probe any chromaticity for its colour, CIELAB value and gamut membership.
- Plot transfer curves (EOTF/OETF) and see which are exact, partial or corrected.
- Slice gamuts at constant CIELAB L* or at OKLab L.
- Measure gamut volume in CIELAB and overlap in u′v′ between two spaces, or measure all spaces at once.
- Keep, import and export custom spaces as JSON.
- Export the diagram (SVG, PNG), a space (JSON), all spaces (JSON), the comparison (CSV, JSON) or a link.

## In this folder

- [docs/](docs/README.md) — how to use the lab
  - [Getting started](docs/getting-started.md)
  - [Compare colour spaces](docs/compare-colour-spaces.md)
  - [Define a custom colour space](docs/define-a-custom-space.md)
  - [Inspect transfer functions](docs/inspect-transfer-functions.md)
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
