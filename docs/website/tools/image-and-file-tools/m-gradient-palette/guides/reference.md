---
title: M-Gradient Palette — Reference
description: Every tab, control, preset, readout, export format and message in the M-Gradient Palette.
product: Website › Tools › Image and file tools › M-Gradient Palette
updated: 2026-09-25
---

# M-Gradient Palette reference

Address: https://auricartisan.com/tool/general/tools/m-gradient-palette/

## Tabs

| Tab | Contents |
|---|---|
| **Ramp** | Ends, presets, routes, steps, easing, colour-vision view; the ramp, the step differences, figures and hue circle |
| **Spaces** | Thirty route and easing combinations measured; three ramps drawn with their least chromatic step |
| **Contrast** | Text colour; evidence table; every step checked by WCAG 2.2 and APCA; samples |
| **Data** | The 15 entries every figure rests on, filterable by status; the corrections list |
| **Export** | Six copy and save buttons, previews, the size table and the reading |
| **Reference** | Eight sources and the arithmetic table |

## Ramp tab — controls

| Control | What it does | Values | Default |
|---|---|---|---|
| Start swatch and hex box | The first colour | Any colour; hex as 3 or 6 digits, `#` optional | `#0B3D5C` |
| End swatch and hex box | The last colour | As above | `#F2B134` |
| **Swap the ends** | Exchanges start and end | — | — |
| **A starting point** | Sets both ends to a preset pair | 25 presets, listed below | Choose a pair… |
| **Interpolate in** | The route | OKLCH, short hue; OKLCH, long hue; sRGB; Linear RGB; HSL, short hue; HSL, long hue | OKLCH, short hue |
| **Steps** | Number of colours, ends included | 2 to 32 | 12 |
| **Easing** | Where the steps land | linear, ease-in, ease-out, ease-in-out, step | linear |
| **Show it as seen by** | Colour-vision view for the display | Normal vision, Protan, Deutan, Tritan | Normal vision |

## Presets

| Name | Start | End |
|---|---|---|
| Auric | `#3A2F10` | `#D3AF37` |
| Sunset | `#F56217` | `#0B486B` |
| Ocean | `#0B3D5C` | `#69D2E7` |
| Purple | `#41295A` | `#2F0743` |
| Cherry | `#EB3349` | `#F45C43` |
| Emerald | `#0F3443` | `#34E89E` |
| Lemon | `#CAC531` | `#F3F9A7` |
| Mango | `#FFE259` | `#FFA751` |
| Rosewater | `#E55D87` | `#5FC3E4` |
| Midnight | `#232526` | `#414345` |
| Cosmic | `#FF00CC` | `#333399` |
| Frozen | `#403B4A` | `#E7E9BB` |
| Mojito | `#1D976C` | `#93F9B9` |
| Sublime | `#FC5C7D` | `#6A82FB` |
| Peach | `#ED4264` | `#FFEDBC` |
| Aqua | `#136A8A` | `#267871` |
| Noon | `#00C9FF` | `#92FE9D` |
| Royal | `#141E30` | `#243B55` |
| Fire | `#CB2D3E` | `#EF473A` |
| Lavender | `#7F7FD5` | `#E8E8E8` |
| Deep space | `#000000` | `#434343` |
| Warm flame | `#FF9A9E` | `#FAD0C4` |
| Dusty | `#6D6027` | `#D3CBB8` |
| Heavy rain | `#CFD9DF` | `#E2EBF0` |
| Plum | `#DD5E89` | `#F7BB97` |

## Easing curves

| Easing | Position of step at fraction t along the ramp |
|---|---|
| linear | t |
| ease-in | t² |
| ease-out | t × (2 − t) |
| ease-in-out | 2t² for the first half; −1 + (4 − 2t) × t for the second |
| step | t rounded to the nearest quarter |

## Ramp tab — readouts

| Readout | Meaning |
|---|---|
| Note above the ramp | Steps, route and easing |
| **The ramp** | One button per step; select to copy the hex; gold underline when chroma was reduced |
| End labels | Hex of the first and last steps |
| **ΔE₀₀ between adjacent steps** | One bar per gap, with a mean line; stronger colours at 2 and 5 |
| **mean ΔE₀₀** | Average step difference |
| **evenness** | Standard deviation of the step differences; highlighted below 15% of the mean |
| **largest jump** | Largest step difference and where it is |
| **moved to fit sRGB** | Steps with reduced chroma; highlighted when above 0 |
| Hue circle | Steps in OKLCH hue (angle) and chroma (radius); spokes every 30°; amber outline for reduced steps |

Figures have two decimal places.

## Spaces tab

| Element | Contents |
|---|---|
| Note | Ends and step count |
| Route table | **Route**, **Easing**, **Mean ΔE₀₀**, **Min**, **Max**, **Evenness**, **What happens**; 30 rows |
| Footnote | The evenest row, and how much the mean and evenness vary |
| **The desaturated middle, drawn** | sRGB, Linear RGB and OKLCH, short hue at linear easing, each with evenness and **least chromatic step** |

## Contrast tab

| Element | Contents |
|---|---|
| **Text colour** | The colour checked against every step; default `#FFFFFF` |
| **Why two figures** | WCAG 2.2 is a ratio; APCA is perceptual and signed |
| Evidence table | Five fixed pairs: **Text on background**, **It printed**, **APCA gives**, **Out by** |
| **Your ramp, checked both ways** | **Step**, **WCAG 2**, **Rating**, **APCA Lc**, **Good for**, **The old figure** |
| Footnote | How far the old figure is off on this ramp, and steps it wrongly passed at Lc 60 |
| Samples | "The quick brown fox" on the first, middle and last steps |
| **WCAG 2.2 was already right** | Reference values: 21.00, 4.54, 7.00 |

WCAG ratings: **AAA** 7:1 and above, **AA** 4.5:1, **AA large** 3:1, **fail** below. APCA bands by absolute Lc: **any text** 90, **body text** 75, **large text** 60, **headlines only** 45, **non-text only** 30, **not for text** below.

## Data tab

Status buttons: **All** (15), **Measured** (4), **Computed** (6), **This tool's choice** (4), **Absent** (1). Select an entry to expand it.

| Status | Entries |
|---|---|
| **Measured** | ΔE₀₀ between adjacent steps, evenness, the route × easing table, steps moved to fit sRGB |
| **Computed** | OKLab and OKLCH, the sRGB transfer function, relative luminance, the WCAG 2 ratio, APCA Lc, CIELAB |
| **This tool's choice** | How out-of-gamut steps are brought back, the five easings, calling a ramp even, the 25 presets |
| **Absent** | Colour-vision deficiency below full severity |

**What was corrected, and what it printed** lists four corrections, each with **was** and **now**: the APCA scale factor, the colour-blindness citation, "six interpolation spaces", and "chromaticity paths".

## Export tab

| Button | Output |
|---|---|
| **Copy the CSS gradient** | `linear-gradient` in the route's space, from the two ends |
| **Copy the custom properties** | `--ramp-01` to `--ramp-NN`, one per step |
| **Copy the hex list** | One hex per line |
| **Copy the SVG** | 600 × 80 SVG with one stop per step |
| **Save the SVG** | `ramp.svg` |
| **Save the reading** | `ramp-reading.json` |

## Reference tab

| Source | Status |
|---|---|
| Ottosson (2020), OKLab | Runs |
| ISO/CIE 11664-6:2014, CIEDE2000 | Runs |
| IEC 61966-2-1:1999, sRGB | Runs |
| W3C WCAG 2.2, contrast minimum | Runs |
| APCA-W3 0.1.9 | Rebuilt |
| Machado, Oliveira and Fernandes (2009) | Runs |
| Brettel, Viénot and Mollon (1997) | Withdrawn |
| W3C CSS Color 4 and Images 4, interpolation in a named space | Runs |

**The arithmetic** gives the formulas for the hue route, gamut mapping, evenness, the WCAG 2 ratio, and APCA Lc for both polarities.

## Messages

| Message | When |
|---|---|
| **That is not a colour.** | A hex box holds an invalid value |
| Hex value followed by **copied** | A step was copied |
| **CSS gradient copied** / **Custom properties copied** / **SVG copied** | An export was copied |
| N **colours copied** | The hex list was copied |
| **Reading saved.** | The reading was saved |
| **The browser refused the clipboard.** | Clipboard access was blocked |
| **This browser will not take text from the clipboard.** | The browser cannot copy text |
