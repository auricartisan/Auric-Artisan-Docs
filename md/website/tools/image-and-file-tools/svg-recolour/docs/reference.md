---
title: SVG Recolour — Reference
description: Every tab, control, paint property, colour form, readout, export format and message in SVG Recolour.
product: Website › Tools › Image and file tools › SVG Recolour
updated: 2026-09-25
---

# SVG Recolour reference

Address: https://auricartisan.com/tool/general/tools/svg-recolor/

## Tabs

| Tab | Contents |
|---|---|
| **Recolour** | Loading, write style, vision preview, harmonies; before and after previews, the colour list and figures |
| **Mapping** | Every colour's use, target and written count; worked examples of swaps and counts |
| **Check** | Text colour; WCAG 2.2 and APCA per colour; closest pairs; the artwork under three dichromacies |
| **Data** | The 15 entries every figure rests on, filterable by status; six corrections |
| **Export** | Four save and copy buttons, the size table, custom properties and the report |
| **Reference** | Nine sources and a six-step description of how the tool works |

## Recolour tab — The file

| Control | What it does | Accepts |
|---|---|---|
| **Drop an SVG** | Loads a dropped file, or opens a chooser when selected or when `Enter` or `Space` is pressed | `.svg`, `image/svg+xml` |
| **Load the sample** | Loads a built-in sample and puts its markup in the paste box | — |
| Paste box | SVG markup | Text |
| **Read the markup** | Loads the markup in the paste box | Well-formed SVG |

The sample loads automatically when the page opens.

## Recolour tab — Options

| Control | Values | Default |
|---|---|---|
| **Write colours as** | **Write hex**, **Keep the source form** | Write hex |
| **Show it as seen by** | **Normal vision**, **Protan**, **Deutan**, **Tritan** | Normal vision |
| **Recolour from a harmony** | complementary, analogous, triadic, tetradic, split complementary | — |
| **Put every colour back** | Resets every target to its original | — |

## Paint properties searched

`fill`, `stroke`, `stop-color`, `flood-color`, `lighting-color`, `color`, `solid-color`, `text-decoration-color`, in presentation attributes, style attributes and `<style>` elements.

## Colour forms

| Form | Read | Written with **Keep the source form** |
|---|---|---|
| `#RRGGBB` | Yes | Hex, keeping capitals if the original used them |
| `#RGB` | Yes | Six-digit hex |
| `#RRGGBBAA`, `#RGBA` | Yes | Six-digit hex; the alpha is lost |
| `rgb()`, `rgba()` | Yes, comma or space separated | `rgb(r, g, b)`, or `rgba(r, g, b, a)` keeping the alpha |
| `hsl()`, `hsla()` | Yes | `hsl(h, s%, l%)`, or `hsla(…)` keeping the alpha |
| 148 CSS names | Yes | The CSS name if the new colour has one, otherwise hex |
| `none`, `transparent` | Listed, left alone | — |
| `currentColor`, `inherit`, `initial`, `unset`, `revert`, `context-fill`, `context-stroke` | Listed, left alone | — |
| `url(…)` | Listed, left alone | — |
| Other functions, `var()` | Not recognised | — |

With **Write hex**, every changed colour is written as lower-case six-digit hex.

## Active content removed from the previews

`script`, `foreignObject` and `handler` elements; attributes whose names begin with `on`; `href` and `xlink:href` values beginning with `javascript:`, including when whitespace or control characters are hidden inside the word. The exported file is not stripped.

## Recolour tab — Readouts

| Readout | Meaning |
|---|---|
| Stripped notice | What active content was removed from the previews |
| Note above the previews | Elements, occurrences and colours, or **nothing loaded** |
| **As it came** | The original, on a chequerboard |
| **After** heading | Occurrences written out of those that can be written |
| Colour list row | Current swatch, hex, name, places; target swatch, hex, **unchanged** or **written in** N **places**; written count |
| Greyed row | Keyword, **left alone**, reason, **not held** |
| **elements** | Elements in the document, root included |
| **occurrences** | Places a colour value is written |
| **colours** | Distinct changeable colours |
| **left alone** | Values with no colour to change |
| **written** | Occurrences the export carries as changed |
| **closest pair** | Smallest CIEDE2000 difference under the three simulations; highlighted below 8 |

Reasons for greyed rows: **resolves from outside this file** (`currentColor`), **no paint** (`none`), **a reference, not a colour** (others).

## Harmonies

| Harmony | Angles from the base colour's OKLCH hue |
|---|---|
| complementary | 0°, 180° |
| analogous | 0°, −30°, +30° |
| triadic | 0°, 120°, 240° |
| tetradic | 0°, 90°, 180°, 270° |
| split complementary | 0°, 150°, 210° |

The base is the first colour in the list. Lightness and chroma are kept; the pattern repeats with a further 12° turn when there are more colours than angles.

## Mapping tab

| Element | Contents |
|---|---|
| Note | Number of occurrences |
| Table | Swatch, **In the file**, **Used**, **Becomes**, **Written**, **Where, and what happened** |
| Footnote | Written, unchanged and skipped counts, which add up to the total |
| **Two colours trading places** | Three measured cases: a swap, a named colour, a shorthand |
| **What the count used to mean** | Six measured cases of the earlier count against the real one |

## Check tab

| Element | Contents |
|---|---|
| **Text laid over the artwork** | The text colour; default `#FFFFFF` |
| **What can be read on it** | **Colour**, **WCAG**, **Rating**, **APCA Lc**, **Good for**, **It used to say** |
| **The Lc that was always zero** | Four pairs: **It printed** against **APCA gives** |
| **The two colours hardest to tell apart** | **Seen as**, **The two closest colours**, **ΔE₀₀ between them**, **What that means** |
| **The artwork under three dichromacies** | Four previews with **closest two** |

WCAG ratings: **AAA** 7:1, **AA** 4.5:1, **AA large** 3:1, **fail** below. APCA bands by absolute Lc: **any text** 90, **body text** 75, **large text** 60, **headlines only** 45, **non-text only** 30, **not for text** below. Closeness: **close to indistinguishable** below 5, **tells apart with effort** below 12, **clearly different** otherwise.

## Data tab

Status buttons: **All** (15), **Measured** (3), **Computed** (7), **This tool's choice** (3), **Absent** (2). Select an entry to expand it.

| Status | Entries |
|---|---|
| **Measured** | Where each colour is used, occurrences written back, colours that cannot be written |
| **Computed** | Reading a colour value, ΔE₀₀, WCAG ratio, APCA Lc, OKLab and OKLCH, the sRGB transfer function, colour-vision simulation |
| **This tool's choice** | When two colours count as the same, the harmony angles, the colour names |
| **Absent** | What `currentColor` resolves to; colour inside embedded raster images |

**What was corrected, and what it printed** lists six corrections with **was** and **now**. Colours are grouped only when they are exactly the same colour; there is no control for merging near-identical colours.

## Export tab

| Button | Output |
|---|---|
| **Save the recoloured SVG** | `recoloured.svg` |
| **Copy the markup** | The recoloured SVG markup |
| **Copy the custom properties** | `--colour-01: #RRGGBB;  /* name */` lines |
| **Save the report** | `recolour-report.json` |

## Reference tab

| Source | Status |
|---|---|
| W3C SVG 1.1 and SVG 2, paint and presentation attributes | Runs |
| W3C CSS Color 4, colour syntax and named colours | Runs |
| ISO/CIE 11664-6:2014, CIEDE2000 | Runs |
| IEC 61966-2-1:1999, sRGB | Runs |
| W3C WCAG 2.2, contrast minimum | Runs |
| APCA-W3 0.1.9 | Rebuilt |
| Ottosson (2020), OKLab | Runs |
| Machado, Oliveira and Fernandes (2009) | Runs |
| Brettel, Viénot and Mollon (1997) | Withdrawn |

**How it works** lists six steps: Parse, Strip, Walk, Resolve, Plan and Write.

## Messages

| Message | When |
|---|---|
| **Loaded** file name / **Loaded the pasted markup.** | A file or markup was loaded |
| **A sample with a hex, an rgb(), a name, a shorthand, a stylesheet and a currentColor.** | The sample was loaded |
| **That file will not parse as SVG, so nothing was changed.** | The markup is not well-formed |
| **Paste some SVG markup first.** | **Read the markup** with an empty box |
| **Load an SVG first.** | A harmony with nothing loaded |
| **A** harmony **palette from** hex. | A harmony was applied |
| **Every colour back to what it was.** | **Put every colour back** |
| **Saved ·** N **occurrences written** | The SVG was saved |
| **Nothing loaded.** | Save or copy with nothing loaded |
| **Markup copied** / **Custom properties copied** | A copy succeeded |
| **Report saved.** | The report was saved |
| **The browser refused the clipboard.** | Clipboard access was blocked |
| **This browser will not take text from the clipboard.** | The browser cannot copy text |
