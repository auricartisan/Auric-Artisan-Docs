---
title: Tone Mapping — Compare operators
description: Compare all nine operators by what they return for chosen inputs, where they reach white, and how their curves look.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Compare operators

## The nine operators

| Operator | Source | Formula or shape | Offered in the Lab |
| --- | --- | --- | --- |
| None (clip) | — | Clamps to 0–1 | Yes |
| Reinhard | Reinhard et al. 2002 | L ÷ (1 + L); approaches 1 but never reaches it | Yes |
| Uchimura / Gran Turismo | Uchimura 2017 | A toe, a linear section and a shoulder blended together | Yes |
| Hable filmic | Hable 2010 (Uncharted 2) | A filmic curve with six constants, exposure bias 2.0, white point 11.2 | Yes |
| Narkowicz fit | Narkowicz 2016 | (x(2.51x + 0.03)) ÷ (x(2.43x + 0.59) + 0.14), clamped. Approximates the look of ACES; it is not the Academy's transform | Yes |
| Log (soft) | This tool | log2(1 + v) ÷ log2(11) | Yes |
| Custom 1D curve | This tool | Knee, mid and shoulder | Yes |
| Gamma-domain scale | This tool; formerly labelled "BT.2446 Method A" | Y × k^2.4, a constant multiplication (about 0.004 at the default peaks) that turns mid-grey nearly black | No |
| Scaled Reinhard | This tool; formerly labelled "BT.2446 Method C" | reinhard(Y × r) ÷ r, which can never exceed 1 ÷ r (0.1 at the default ratio of 10) | No |

The last two are not tone curves and do not implement ITU-R BT.2446. They are shown so that old links still open and so you can see what they did.

## Steps

1. Set the **Display peak** and **Source peak** on the Lab tab. They only affect the two retired operators.
2. Open the **Operators** tab.
3. Under **Compare**, choose **All nine** or **The seven that work**.
4. Under **Read out at**, choose the inputs:
   - **Mid-grey 0.18** — 0.18, 1, 4 and 12;
   - **Scene white** — 1, 4, 12 and 32;
   - **Both** — 0.18, 1, 2, 4, 8 and 16.
5. Read the table:

| Column | Meaning |
| --- | --- |
| Operator | The name, and its source (or "was: …" for a retired operator) |
| One column per input | The output value; values above 1 are highlighted |
| White at | The input where the curve reaches display white, or "never" |
| Output | A grey strip of the operator's output across the domain, as a display would show it |
| Tag | **runs**, **exceeds 1** (the curve passes 1.0, so it clips at the end of the pipeline) or **not a curve** |

6. Under **Curve domain**, choose **0 – 1** or **0 – 12** (default) for the chart. Scene values run past 1, so the wider domain shows how each curve treats highlights.
7. Read the chart: every operator on one pair of axes, with a dashed line at display white and a line at mid-grey 0.18. Retired operators are dashed and labelled in red. Select **Redraw the curves** if the chart looks out of date.

## Reading the result

- Mid-grey is where a tone map is judged. An operator that moves 0.18 a long way has changed the picture's exposure, not just its highlights.
- A curve that reaches white at a modest input (Narkowicz fit, None) clips everything above it. A curve that never reaches white (Reinhard) keeps compressing highlights but never shows pure white.
- The table's notes under the chart explain what the two retired operators computed and what the real BT.2446 methods involve.

## Result

You can see, for the same inputs, how each curve treats mid-grey, white and highlights, and which ones are not really tone curves.
