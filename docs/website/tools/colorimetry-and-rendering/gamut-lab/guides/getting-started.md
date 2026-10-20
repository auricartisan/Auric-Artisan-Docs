---
title: Gamut Lab — Getting started
description: Open the Gamut Lab, learn its tabs and panels, and read the chromaticity diagram.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Getting started with the Gamut Lab

## Open the lab

Go to https://auricartisan.com/tool/general/gamut-and-rendering/gamut/. The heading is **Gamut Lab**. All calculations run in your browser.

## Key ideas

- The **chromaticity diagram** maps colour without brightness. Its curved edge, the **spectral locus**, is made of single wavelengths of light; the straight line closing it at the bottom joins deep violet and deep red (the purples). Every colour a person can see lies inside.
- An RGB space's **gamut** on the diagram is the triangle between its three primaries. A larger triangle holds more saturated colours.
- The **CIE 1931 xy** diagram is the classic one, but equal distances on it are not equal visual differences (it stretches greens). The **CIE 1976 u′v′** diagram is more even, so the lab quotes shares of the locus in u′v′.
- A triangle shows chromaticity only. **Gamut volume** in CIELAB also accounts for lightness, which is why the lab measures it separately.

## A tour of the screen

| Tab | What it is for |
| --- | --- |
| **Lab** | The diagram, the working space's primaries and matrices, a transfer curve, volume and slice panels |
| **Transfer** | Every distinct transfer curve, plotted, with its fidelity to its standard |
| **Compare** | Every space measured the same way: volume, ratio to sRGB and share of the locus |
| **Data** | The eight datasets the lab uses and their status |
| **Export** | Choose what to take and in which format, preview it, download or copy; import spaces; the library |
| **Reference** | Standards, formulas, citations and research notes with a filter |

### The Lab tab

The left panel holds: **Working color space**, **Diagram mode**, **Standard observer**, **Overlays**, **Vertex readout**, **Actions** (Reset view, Export PNG, Export SVG), **Primaries (xy)**, **White point XYZ**, **RGB ↔ XYZ matrices** (with **Solve from primaries** and the triangle area), **Transfer function**, **Volume comparison** and **Gamut slice**.

The right side shows four canvases: **Chromaticity diagram**, **EOTF / OETF curve**, **Gamut slice — Lab / OKLab** and **3-D gamut wireframe**.

## Read the diagram

1. The diagram opens with sRGB, Display P3 and Rec. 2020 drawn on CIE 1931 xy.
2. Choose another space under **Working color space**, for example **ACES 2065-1 (AP0)**. It is added to the diagram (up to five spaces are drawn; the oldest is dropped when you add a sixth). Its primaries and matrices fill the panel.
3. Notice AP0's blue primary lies below the diagram's edge: it is an imaginary colour, which lets the triangle enclose every real colour.
4. Click or drag on the diagram. A marker follows the pointer and **Vertex readout** shows x, y, a colour chip with its sRGB HEX, a CIELAB value, and a tick or cross for each drawn space.
5. Tick **Show all library spaces** to draw every space at once, including your own.
6. Choose **CIE 1976 u′v′** under **Diagram mode** to redraw everything on the more uniform diagram, or **3-D Wireframe (Lab)** to see each drawn space as a wireframe solid in CIELAB.
7. Select **Reset view** to return to CIE 1931 xy with the default overlays and no probe marker.

## Next steps

- [Compare colour spaces](compare-colour-spaces.md)
- [Define a custom colour space](define-a-custom-space.md)
- [Inspect transfer functions](inspect-transfer-functions.md)
