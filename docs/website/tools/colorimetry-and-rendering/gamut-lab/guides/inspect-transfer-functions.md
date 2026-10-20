---
title: Gamut Lab — Inspect transfer functions
description: Read each space's transfer curve, understand EOTF and OETF, and check which curves are exact to their standard.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Inspect transfer functions

## Key ideas

- A **transfer function** links stored values to light. The **OETF** (opto-electronic) encodes light into a signal; the **EOTF** (electro-optical) turns a signal back into light on a display.
- Most spaces use a **relative** curve: signal 0 to 1 becomes light 0 to 1 of the display's peak. **PQ** (SMPTE ST 2084) is **absolute**: a signal value means a specific luminance in cd/m² (nits), up to 10,000.
- **HLG** (hybrid log-gamma) is a relative HDR curve. Its full EOTF needs a display peak luminance and a surround; this lab draws the inverse OETF only, and marks it **Partial**.

## The ten distinct curves

| Curve | Used by | Fidelity |
| --- | --- | --- |
| IEC 61966-2-1 (sRGB piecewise) | sRGB, Display P3, Custom | Exact |
| ITU-R BT.2020-2 | Rec. 2020 | Exact (corrected) |
| ROMM / ISO 22028-2, γ 1.8 plus toe | ProPhoto RGB | Exact (corrected) |
| Adobe RGB (1998), γ 563/256 | Adobe RGB | Exact (corrected) |
| SMPTE ST 2084 (PQ) | Rec. 2100 PQ | Exact |
| ARIB STD-B67 — inverse OETF | Rec. 2100 HLG | Partial |
| Linear | ACES 2065-1 (AP0), ACEScg (AP1) | Exact |
| Gamma 2.6 | DCI-P3 | Exact |
| Gamma 2.2 | Adobe Wide Gamut, NTSC 1953 | Exact |
| Gamma 2.8 | PAL/SECAM | Exact |

"Corrected" marks a curve that an earlier version of the page did not run as its standard defines.

## The Transfer tab

1. Open the **Transfer** tab. The note gives the number of distinct curves across the spaces.
2. Under **Plot**, choose **Relative, 0 to 1** for the display-relative curves or **Absolute, cd/m²** for PQ, which has its own log-scale axis from 1 to 10,000 cd/m².
3. Under **Fidelity**, filter the rows: **All**, **Exact**, **Partial** or **Corrected** (each chip shows its count).
4. Read the legend under the plot; a dashed line is the linear reference.
5. Open a row to see the defining document, what the curve used to be (for corrected rows) and, for HLG, why it is partial.

## The Lab tab's transfer panel

1. On the **Lab** tab, find **Transfer function**.
2. Choose a preset: **sRGB**, **Display P3**, **Rec. 2020**, **PQ (ST 2084)**, **HLG**, **Adobe RGB (γ 563/256)** or **ProPhoto (ROMM)**.
3. The **EOTF / OETF curve** canvas plots it, the summary names the defining document, and an equation box shows the formula for the sRGB, PQ, HLG and linear curves. For the other presets the equation box shows a simplified power-law form; the Transfer tab and Reference › Formulas give the exact definitions.

## Result

You know which curve each space uses, whether it is relative or absolute, and whether the lab runs it exactly as its standard defines.
