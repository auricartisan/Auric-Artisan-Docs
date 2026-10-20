---
title: LUT Lab — Limits and accuracy
description: LUT Lab's 8-bit path, how its figures are measured, and what it does not hold.
product: Website › Tools › Image and file tools › LUT Lab
updated: 2026-09-25
---

# Limits and accuracy

## The 8-bit path

Every value in LUT Lab travels as an 8-bit integer, because it comes from and returns to a canvas. This is a real limit:

- A loaded LUT's output is rounded to 8 bits when applied.
- An exported `.cube` holds only the 256 values k ÷ 255 per channel, written to six decimals. The header says so.
- A 1D export longer than 256 entries would only repeat values; the tool writes at most 65.
- At sizes where N − 1 does not divide 255 (including 17, 33 and 65), grid points in an exported file sit up to half an 8-bit step from the exact grid. An 8-bit image is unaffected; a program reading at higher precision is not.

## What is measured, and how

| Figure | Method |
|---|---|
| **mean ΔE₀₀**, **95th percentile**, **largest** | CIEDE2000 between each pixel before and after, in CIELAB with a D65 white |
| **clipped** | Pixels with a channel moved to 0 or 255 from somewhere else |
| **the old test said** | Pixels with any output channel at 0 or 255; kept for comparison only |
| Hue circle | 72 colours at L* 60, C* 40 in CIELAB, every 5°; 13 are pulled inside sRGB first |
| Hue shift | Change of CIELAB hue angle, not HSL hue |
| Round trip | Values written and read back agree to the six decimals of the format |

The CIEDE2000 formula is checked against a second transcription of the standard and against published test data.

## Choices the tool makes

These are listed as **Stand-in** on the **Data** tab.

- **The five stylisations** are hand-tuned curves. None imitates a measured film stock or a photochemical process, whatever its name.
- **The tone-map exposure** defaults to 2×, a one-stop lift. An 8-bit sRGB picture has no record of the scene's true brightness.
- **The drawn scenes** exercise a transform evenly but are not photographs: no grain, flare or real sensor colour. Load your own picture for a real test.
- **The 8-bit path** itself.

## What the tool does not hold

| Not held | Why |
|---|---|
| ACEScct to ACEScg | Its output runs far above 1, which an 8-bit canvas cannot hold |
| 32-bit float export | There is no floating-point path to fill it |
| PQ (SMPTE ST 2084), BT.2020, ACES primaries | Not implemented; the tool works in sRGB only |
| LUT formats other than `.cube` | Only `.cube` is read and written |
| Input beyond 0 to 1 | Pictures are 8-bit sRGB; wider domains are only partly reachable |

## Limits

- Your picture is scaled to fit 480 × 270 for the analysis.
- Export sizes are 2 to 65, for 3D and 1D alike.
- A loaded file is applied at full strength only.
- Share links do not carry a loaded file or your picture.
- The tool does not store anything between visits.

## What it is not

LUT Lab is a place to read, test and write `.cube` files for 8-bit sRGB work. It is not a grading application, and it does not handle log, HDR or wide-gamut footage.
