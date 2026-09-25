---
title: Gamut Mapping — Overview
description: What the Gamut Mapping lab does, who it is for, where to find it and how to map your first colour.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Gamut Mapping

A **gamut** is the set of colours a colour space or device can hold. When a colour moves from a wide space (such as Display P3 or ProPhoto RGB) into a narrower one (such as sRGB), some colours will not fit. **Gamut mapping** decides what they become.

The Gamut Mapping lab shows this as a horizontal slice through CIELAB at a lightness you choose: the source gamut on one side, the colours mapped into the target on the other, with each space's boundary outlined. It supports five RGB spaces (sRGB, Display P3, Rec. 2020, Adobe RGB and ProPhoto RGB), each decoded with its own transfer curve and white point, and four mapping methods named for what they do: chroma compression, clipping in the target RGB, uniform RGB scaling, and adapting the white point before clipping.

Around the slice you can probe any point, map a base colour or a list of colours, measure every space's volume in CIELAB with a stated standard error, compare the four methods on a fixed set of probe colours, and compare colour differences with three ΔE formulas. The lab is explicit that none of its methods is an ICC rendering intent: ICC perceptual and saturation intents are lookup tables built into profiles, not algorithms.

## Who it is for

- Designers and brand teams checking what a wide-gamut colour becomes on standard screens or in sRGB files.
- Developers working with CSS Color 4 (Display P3, Rec. 2020) who want to see what clipping does.
- Photographers comparing ProPhoto, Adobe RGB and sRGB.
- Students learning how gamut boundaries change shape with lightness.

## Where to find it

- Address: https://auricartisan.com/tool/general/colorimetry/gamut-map/
- In the tool collection (https://auricartisan.com/collections/) under **Colorimetry**, as **Gamut Mapping**.

## Quick start

1. Open https://auricartisan.com/tool/general/colorimetry/gamut-map/.
2. Under **Colour Spaces**, set **Source** to **Display P3** and **Target** to **sRGB / Rec.709** (or select **Swap Source & Target** from the defaults).
3. Type a vivid P3 colour such as `#00FF00` in the base colour HEX field. The **Base Colour Info** panel says whether it is inside each space.
4. Move **Lightness Slice L\*** to find the lightness where the source and target boundaries differ most.
5. Under **Method**, try each of the four options and watch the **Before / After (12 Test Colours)** strip change.
6. Click inside the **Source Slice** to probe a point.
7. Open **Export** and paste a list of HEX colours into **Map a list of colours at once**, then select **Run the list**.

## What you can do

- Draw CIELAB a*b* slices of five RGB spaces at any L* from 5 to 95.
- Map colours with four methods and a compression strength.
- Probe any slice point for L*a*b*, C*h°, sRGB, HEX and gamut membership.
- Compare ΔE₀₀, ΔE*94 and ΔE*76 between two colours.
- See the boundary of up to five spaces at five lightness levels on one scale.
- Measure each space's CIELAB volume by Monte Carlo sampling, with a standard error.
- Compare the four methods on the base colour or on 12 fixed probe colours.
- Export the slices as PNG, the settings as JSON, a link to the exact state, and a mapped colour list.

## In this folder

- [docs/](docs/README.md) — how to use the lab
  - [Getting started](docs/getting-started.md)
  - [Map a colour into a smaller gamut](docs/map-a-colour.md)
  - [Compare spaces and methods](docs/compare-spaces-and-methods.md)
  - [Map a list of colours](docs/map-a-colour-list.md)
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
