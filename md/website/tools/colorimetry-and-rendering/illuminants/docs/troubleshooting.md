---
title: Illuminants — Troubleshooting
description: What to do when a reading, chart, export or shortcut in the Standard Illuminants lab does not behave as expected.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Troubleshooting Illuminants

| Symptom | Why it happens | What to do |
| --- | --- | --- |
| Moving the CCT slider changed my illuminant to a blackbody | The CCT controls drive Blackbody mode, so touching them switches the source | Choose **Standard** under Source mode and pick the illuminant again, or select **Reset to D65** |
| The CCT box jumps back when I pick a standard illuminant | **Link to select** copies the illuminant's nominal CCT into the box | Untick **Link to select** to keep your own CCT value |
| The Illuminant comparison panel is empty | Comparison is off | Tick **Enable comparison** |
| CCT shows "n/a" or a validity warning | The light is too far from the blackbody curve (Duv beyond ±0.05) or outside 1,000–100,000 K, where CCT is not defined | Read Duv and x, y instead. See [Limits and accuracy](../others/limits-and-accuracy.md) |
| The dominant wavelength shows a dash | The light is almost the same colour as the D65 reference white, so there is no direction to measure | Expected. Purity will read close to 0% |
| The CRI of a fluorescent light looks wrong compared with a datasheet | The lab's test colour samples and fluorescent spectra are stand-ins, not the CIE tables | Treat CRI as indicative. Use a published or measured value for specifications |
| I want TM-30 Rf and Rg | The 99 colour evaluation samples are not held, so TM-30 is not computed | The Methods tab shows the card as switched off. Use IES software for TM-30 |
| The 1964 10° observer button is greyed out | Its colour matching functions are not held | Only the 1931 2° observer is available |
| The equal-energy E spectrum is a flat line | E has equal power at every wavelength by definition | Expected |
| Changing interval or interpolation does not change the Lab summary | Those settings apply to the Chromaticity, Uncertainty, Console and Methods views; the Lab tab always works at 5 nm | Read the changed figures on those tabs |
| Changing interval or interpolation changes nothing at all | The source tables are tabulated at 5 nm, so a finer grid adds no information; the Methods note says so | Expected. The deltas show as dashes |
| The Uncertainty results change slightly each run | Monte Carlo sampling is random | Use **20k** trials for a steadier result |
| Console CSV or JSON does nothing | No query has returned rows yet | Select **Run** first, then export |
| Console says "Nothing matched" | A name was misspelt, or a range used an unknown prefix | Use names such as `D65` or `F1..F12` |
| Pressing S, R, C or E does nothing | The Lab rail shows these keys as a hint, but they are not active in the current version | Use **Swap**, **Reset to D65**, **Enable comparison** and **Export SPD CSV** instead |
| **Copy white HEX** or **Copy** gives no toast and nothing is copied | The browser blocked clipboard access (permissions, or a page not opened over https) | Allow clipboard access, or select the share field and copy it manually |
| The share link opened without my surfaces or comparison | The link stores source, illuminant or CCT, and adaptation settings only | Re-tick the surfaces and comparison after opening |
| The full-screen chart will not close | — | Press `Esc`, select the close button, or click outside the chart |
| Charts look blurred after resizing the window | Some charts redraw only when their view changes | Switch tabs and back, or reload the page |
