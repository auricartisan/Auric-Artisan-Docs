---
title: Tone Mapping — Reference
description: Every control, readout, option and export in the Tone Mapping lab.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Tone Mapping reference

Address: https://auricartisan.com/tool/general/gamut-and-rendering/tone-mapping/

## Lab tab

### Source

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Source** | The frame to map | HDR test scene; Exposure gradient; ColorChecker patches; Uploaded image | HDR test scene |
| **Choose a file** | Picks an image (shown for Uploaded image) | Image files | "no file" |
| Source encoding | How the source values are decoded (step 1) | Linear (scene); sRGB; PQ (ST 2084); HLG (inverse OETF); Gamma 2.2; Gamma 2.4 | Linear (scene) |
| Source primaries | The source's RGB space | Rec.709; Display P3; Rec.2020; ACEScg AP1 | Rec.709 |
| Source white | The source's white point | D65; D60; D50 | D65 |

### Exposure and curve

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Exposure** | Multiplies by 2^EV before the curve (step 3) | −6 to +6 EV, step 0.1 | 0.0 EV |
| **Tone curve** | The operator (step 5) | None (clip); Reinhard; Uchimura / Gran Turismo; Hable filmic; Narkowicz fit; Log (soft); Custom 1D curve | Hable filmic |
| **Use the custom curve instead** | Uses the knee / mid / shoulder curve whatever is selected | On or off | Off |
| Custom curve knee, mid, shoulder | The three points of the custom curve | 0 to 1 each | 0.15, 0.5, 0.85 |
| **Low-level operator** | A per-channel function before the curve (step 4) | None; Add; Multiply; Soft clip; Power; Sigmoid; Exp; Log; Tanh | None |
| Parameters a, b | Values for the low-level operator | Numbers, step 0.1 | 0, 0 |

### Grade (steps 6–8)

| Field | Range | Default |
| --- | --- | --- |
| Contrast | 0 to 3 | 1 |
| Saturation | 0 to 3 | 1 |
| Lift | Any | 0 |
| Gamma | 0.1 to 4 | 1 |
| Gain | 0 to 4 | 1 |
| Temperature | Any | 0 |
| Tint | Any | 0 |
| Hue rotation | −180 to 180° | 0 |
| Vibrance | 0 to 3 | 1 |

The fields appear as one row in this order. See [Map a frame](map-a-frame.md) for what each does.

### Working → target (steps 2, 9–11)

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| Working space | The space the curve and grade run in | ACEScg AP1 (D60); Rec.709 (D65); Display P3 (D65); Rec.2020 (D65) | ACEScg AP1 (D60) |
| Target primaries | The display's RGB space | sRGB / Rec.709; Display P3; Rec.2020 | sRGB / Rec.709 |
| Target white | The display's white; Bradford adapts between whites | D65; D60; D50 | D65 |
| Gamut mapping | What happens to out-of-gamut colours | Soft compress; Clip; Preserve hue | Soft compress |
| Output OETF | How the result is encoded | sRGB; Gamma 2.2; Gamma 2.4; PQ; Linear | sRGB |
| **Mark out-of-gamut pixels** | Paints pixels that left the target gamut in magenta | On or off | Off |
| **Dither the 8-bit output** | Adds noise of up to half a code value | On or off | Off |
| **Display peak** | Display peak luminance | 80 to 4,000 nits, step 10 | 100 |
| **Source peak** | Source peak luminance | 100 to 10,000 nits, step 50 | 1,000 |

The two peaks change only the two retired operators, the false-colour map (display peak) and the false-colour note (source peak). The seven working curves do not depend on them.

### Presets

| Button | Sets |
| --- | --- |
| **SDR 100** | Hable filmic, sRGB / Rec.709 target, 100 nits, sRGB output, sRGB source |
| **P3 600** | Hable filmic, Display P3 target, 600 nits, sRGB output, sRGB source |
| **HDR 1000** | Narkowicz fit, Rec.2020 target, 1,000 nits, PQ output, linear source |
| **Reset** | Reloads the lab with defaults |

### Readouts

| Readout | What it shows |
| --- | --- |
| **The mapped frame** | The result, with its resolution |
| Frame chips | Working → target, curve and processing time; Scene-referred or Display-referred; Photographic or Display; "out of gamut" when any pixel left the target |
| **The curve, and where the scene sits on it** | The tone curve over a histogram of the scene |
| **Linear axis**, **Log axis**, **Film stops** | Fill the custom curve with presets (0.33 / 0.5 / 0.66; 0.05 / 0.35 / 0.7; 0.15 / 0.5 / 0.85) |
| Statistics | Mid-grey, curve; Scene white at; Working luma; Display peak |
| Behaviour label | A short description of the curve, such as Photographic or Filmic shoulder |
| Note | What mid-grey becomes, where white is reached, or why a curve clips |

## Operators tab

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Compare** | Rows shown | All nine; The seven that work | All nine |
| **Read out at** | Input columns | Mid-grey 0.18 (0.18, 1, 4, 12); Scene white (1, 4, 12, 32); Both (0.18, 1, 2, 4, 8, 16) | Mid-grey 0.18 |
| **Curve domain** | Chart range | 0 – 1; 0 – 12 | 0 – 12 |
| **Redraw the curves** | Redraws the chart | Button | — |

Table columns: Operator, one column per input, White at, Output strip, tag (runs, exceeds 1, not a curve).

## Scopes tab

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Show the exposure map** | Replaces the frame with false colour | On or off | Off |
| **Store A**, **Store B** | Stores the current frame | Buttons | — |
| **Split the viewport** | Shows A left and B right | On or off | Off |
| Split position | Where the split falls | 0 to 1, step 0.01 | 0.5 |
| **Time a pass** | Average of 20 full passes, in ms per frame | Button | — |
| **Time the curve** | Average of 5 full passes | Button | — |

Readouts: **Histogram — output, 256 bins**; **Waveform — output luma by column**; **Vectorscope — output chroma**; the false-colour key and note; **Controls that were read and never used**.

## Data tab

| Dataset | Status |
| --- | --- |
| sRGB, PQ and HLG transfer | Verbatim |
| Primaries and white points, 4 spaces | Verbatim |
| Bradford adaptation | Verbatim |
| Tone-mapping operators | Computed: seven of nine do what they are named for |
| Working-space luminance | Computed from each space's own matrix |
| Hue rotation | Computed |
| BT.2446 Method A and Method C | Absent: the names were held, the methods were not |
| Absolute scene luminance | Absent: the generated scenes carry none |

**Status** chips filter the list. **Install a table** ("Drop a CSV or JSON") does not load files in the current version.

## Export tab

| Control | What it does |
| --- | --- |
| **What to take** | The tone curve; The whole pipeline; A link to this view |
| **As** | .cube or CSV (curve); .cube (pipeline); URL (link) |
| **Input domain** | 0 – 1 or 0 – 12 for the curve export (default 0 – 1) |
| Download button | Names and saves the file; **Copy the link** for links |
| **Copy to clipboard** | Copies the payload |
| **Exactly what you will get** | Preview, bytes and lines |
| **What this file carries** | Which of the eleven steps the file includes |
| **Analyse a list**, **Analyse**, **Download the result** | Maps HEX colours; saves `tone-map-batch.csv` |

Link parameters: `op`, `exp`, `src` (source encoding), `peak` (display peak), `oetf`, `tp` (target primaries).

## Reference tab

| Control | What it does |
| --- | --- |
| **Standards**, **Formulas**, **Citations**, **Research notes** | Switch sections |
| **Filter** | Searches all four |

Standards include IEC 61966-2-1, SMPTE ST 2084, ARIB STD-B67 / BT.2100, BT.709, BT.2020, Academy S-2014-004 (ACEScg), BT.2446-1 (not implemented), BT.2408 and the Adobe Cube LUT Specification 1.0. Formulas give each operator, the transfer curves, working luminance, hue rotation, Bradford adaptation and the out-of-gamut test.

## Save to Library

The floating **Save to Library** button stores an image of the mapped frame in your Auric Artisan Library.
