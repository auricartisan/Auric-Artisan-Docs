---
title: HDR Gamut Plot — Read HDR transfer curves
description: Compare PQ, HLG and gamma curves in cd/m², set peak brightness and HLG surround, and read what a signal value means in nits.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Read HDR transfer curves

## The four curves

| Curve | Defined by | Kind | What the output means |
| --- | --- | --- | --- |
| **PQ (ST.2084)** | SMPTE ST 2084 | Absolute | Signal 0 to 1 maps to 0 to 10,000 cd/m² on any display that can reach it. Signal 0.5 is about 92 cd/m² |
| **HLG (BT.2100)** | ARIB STD-B67, with the BT.2100 OOTF | Display-referred | Scene light is shaped by a system gamma that depends on the display's peak, then scaled to that peak |
| **Gamma 2.4 (BT.1886, zero black)** | ITU-R BT.1886 | Display-referred | signal^2.4 × peak |
| **Gamma 2.2 (SDR)** | Pure power law | Display-referred | signal^2.2 × peak |

**Absolute** means the curve states a luminance outright. **Display-referred** means it reaches a luminance only by way of the display's peak, which the **Peak brightness** control supplies.

## HLG system gamma

HLG applies an opto-optical transfer function (OOTF) with a system gamma that depends on the display peak L_W:

```text
γ = 1.2 + 0.42 × log10(L_W ÷ 1000)
```

At 1,000 nits γ is 1.2. The tool also offers two surround adjustments: **Dim surround** multiplies γ by 0.95 and **Bright surround** by 0.90. These two factors are this tool's own; they are not in BT.2100 or BT.2390. Choosing one marks the HLG reading **Adjusted**. **Reference dark** uses BT.2100's value unchanged. The system gamma is never set below 1.0.

## Steps

1. Open the **Curves** tab.
2. Set **Peak brightness** (100 to 10,000 nits in steps of 50; default 1,000). It scales the display-referred curves and sets HLG's system gamma. It does not scale PQ.
3. Choose a **Tone curve**: **Gamma 2.2 (SDR)**, **Gamma 2.4 (BT.1886, zero black)**, **PQ (ST.2084)** (default) or **HLG (BT.2100)**. Keys `1` to `4` select them in that order.
4. For HLG, choose an **HLG environment**: **Reference dark** (default), **Dim surround** or **Bright surround**. The line under it shows γsys, and a note says whether the reading is standard or adjusted.
5. Read **Tone curve output**: signal on the horizontal axis, cd/m² on a log vertical axis that extends to whatever the drawn curves need (up to 10,000 for PQ). The selected curve is gold; gamma 2.2 is drawn faintly for reference, and PQ too when another curve is selected.
6. Open the rows under the plot. Each is tagged **Absolute**, **Display-referred** or **Adjusted**. The PQ row lists its constants as the standard's exact fractions; the HLG row gives the system gamma at the current peak.
7. Set **Signal level** (0 to 1, default 0.5). It is used with the tone curve and peak to compute an absolute luminance for the Planes tab and the HEX conversion. The **I =** readout shows that luminance as an ICtCp intensity.

## The EOTF comparison chart

**EOTF Comparison — PQ vs HLG vs sRGB** plots all three on one log-nits axis: PQ over 0 to 10,000 cd/m², HLG at the 1,000-nit reference, and sRGB peaking near 100 nits. It is drawn when the page loads and does not follow the peak control.

## Export the curve

On the **Export** tab, choose **The curve** (CSV) to download the drawn curve sampled at 257 points as `signal,nits`, with a footer recording the curve, whether it is absolute, the peak (or that it was ignored for PQ) and, for HLG, the system gamma and surround. Choose **The curve plot** (PNG) for an image of the plot.

## Result

You can say exactly what luminance a signal value produces under each curve, and when that luminance depends on the display rather than on the signal.
