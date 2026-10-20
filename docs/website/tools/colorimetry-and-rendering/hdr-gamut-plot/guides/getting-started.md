---
title: HDR Gamut Plot — Getting started
description: Open the HDR Gamut Plot, learn its tabs, and read the chromaticity diagram.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Getting started with the HDR Gamut Plot

## Open the tool

Go to https://auricartisan.com/tool/general/gamut-and-rendering/hdr-gamut-plot/. The heading is **HDR Gamut Plot**. Everything runs in your browser.

## Key ideas

- **Gamut** — the range of chromaticities a space can make, drawn as a triangle on a chromaticity diagram. HDR video usually uses the wide **Rec. 2020** gamut.
- **Luminance** — how much light, in candelas per square metre (cd/m², also called nits). Standard video is mastered around 100 nits; HDR can reach 1,000 to 10,000.
- **Transfer function** — the curve from signal (0 to 1) to light. **PQ** gives an absolute luminance for every signal value. **HLG** and the gamma curves are display-referred: their output depends on the display's peak.
- **ICtCp** and **Jzazbz** — colour spaces designed for HDR, in which equal steps are closer to equal visible differences across a wide luminance range.

## A tour of the screen

A note at the top reminds you that a nit is a measurement, not a setting.

| Tab | What it is for |
| --- | --- |
| **Lab** | The chromaticity diagram, overlays, gamut metrics and plotting an image |
| **Curves** | Tone curves from signal to cd/m², peak brightness, HLG surround and signal level |
| **Planes** | The gamuts in ICtCp or Jzazbz, and boundary rings at eight luminances |
| **Data** | The ten datasets the tool uses and their status |
| **Export** | Measurements, curves and images to download or copy, HEX conversion, and a side-by-side comparison of the three spaces |
| **Reference** | Standards, formulas, citations and research notes with a filter |

### The Lab tab

The left panel holds **Working colour space**, **Overlay gamuts**, **Advanced overlays**, **Chromaticity axes**, **Standard observer**, **Plot an image on it** and a shortcut hint. The right side shows the **Gamut chromaticity diagram**, a hover readout, and the **Gamut metrics** table.

## Read the diagram

1. The diagram shows three triangles: Rec.709/sRGB, Display-P3 and Rec.2020, with R, G and B labels at the corners and the D65 white point marked.
2. Move the pointer over it. The line under the diagram shows the coordinates (x, y or u′, v′), the XYZ of that chromaticity at a fixed Y of 0.35, its L*, and its I, Ct and Cp at the luminance that the Curves tab's **Signal level** represents on the PQ curve.
3. Untick a gamut under **Overlay gamuts** to hide it.
4. Under **Advanced overlays**, untick **Spectral locus** or **Line of purples** to hide the edge of the diagram.
5. Change **Chromaticity axes** to **CIE 1976 u′v′** (or press `A`). The label over the diagram changes and the metrics are recomputed in u′v′.
6. Read **Gamut metrics**: primaries, white, **Share of locus** (the triangle's area as a percentage of the spectral locus area in the same plane) and **Area**.

## Next steps

- [Compare broadcast gamuts](compare-broadcast-gamuts.md)
- [Read HDR transfer curves](read-hdr-curves.md)
- [Explore ICtCp and Jzazbz planes](explore-perceptual-planes.md)
