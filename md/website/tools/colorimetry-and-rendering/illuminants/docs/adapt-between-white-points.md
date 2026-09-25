---
title: Illuminants — Adapt colours between white points
description: Use the chromatic adaptation panel to move a 24-colour chart from one white point to another and read the transform matrix.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Adapt colours between white points

Colour-managed work often needs a colour expressed under one white point to be re-expressed under another. The classic case is ICC colour management, whose profile connection space uses D50, while sRGB and most screens use D65. A **chromatic adaptation transform (CAT)** does this by imitating how the eye rebalances its cone sensitivities to a new light.

## How a CAT works, briefly

1. Convert the colour's XYZ values into a cone-like space (L, M, S) with a 3 × 3 matrix M.
2. Scale each of L, M and S by the ratio of the destination white to the source white. This is the **von Kries** idea: each cone type adjusts its gain independently.
3. Convert back to XYZ with the inverse of M.

The transforms differ only in the matrix M. The lab offers:

| Choice | What it is |
| --- | --- |
| **Bradford** | The matrix from Lam (1985), the usual choice in ICC workflows. Default. |
| **CAT16** | The matrix from the CAM16 colour appearance model (Li et al., 2017). |
| **CAT02** | The matrix from CIECAM02 (CIE 159:2004). |
| **Von Kries** | The Hunt–Pointer–Estévez cone matrix, normalised to D65. |
| **Sharp** | A spectrally sharpened matrix (Finlayson and Süsstrunk, 2000). |
| **XYZ scaling** | Scales X, Y and Z directly. Kept as the simplest case to compare against; it is not a model of the eye. |
| **None** | No adaptation. The control turned off, so you can see the unadapted colours. |

## Steps

1. Open the **Lab** tab and find **Chromatic adaptation** in the left rail.
2. Under **Adapt from**, choose the white point the colours are currently expressed in. The choices are D65, D50, D55, D75, A and E. The default is D65.
3. Under **Adapt to**, choose the destination white point. The default is D50.
4. Select a transform chip: **Bradford**, **CAT16**, **CAT02**, **Von Kries**, **Sharp**, **XYZ scaling** or **None**.
5. Look at **Chromatic adaptation preview (24 patches)**. Each column has the original colour on top and the adapted colour below. The caption names the source, destination and method.
6. Read **Adaptation matrix details**:
   - the transform's **M matrix**;
   - **LMS scaling (dst/src)** — the three gains applied to L, M and S;
   - **Source white LMS** and **Dest white LMS** — the two whites in the cone-like space.
7. To reverse the direction, select **Swap** between the two lists.

## Reading the result

- Adapting D65 to D50 makes colours look slightly warmer on a D65 screen, because the preview is still displayed as sRGB. That is expected: the preview shows the adapted values, not what an adapted eye would see.
- Choosing A as the destination produces a strong orange cast for the same reason.
- If you choose **None**, the matrix panel says that no adaptation is applied, and the bottom row matches the top row.
- The 24 patches are a fixed set of 18 chromatic colours and a six-step grey scale, similar to a colour-checker chart. They are defined as sRGB values.

## Tips

- For ICC work, D65 to D50 with Bradford matches common practice.
- To see how much the choice of transform matters for a real image, use the [Chromatic Adaptation](../../chromatic-adaptation/README.md) lab, which applies eight transforms to a photograph and compares them.
- The adaptation settings (from, to and method) are saved in the share link on the **Export** tab.

## Result

You have a chart of 24 colours re-expressed from one white point to another, and the exact matrix and gains that did it.
