---
title: Tonal Steps — Reference
description: Every control, readout, option and export in Tonal Steps, Tints and Shades.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Tonal Steps reference

Address: https://auricartisan.com/tool/general/gamut-and-rendering/tonal-steps-tints-shades/

## Lab tab

### Controls

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| **Base colour** field and picker | The colour every step is built from | Six-digit HEX | #2563EB |
| **Random base** | Picks a random base colour | Button | — |
| **Ramp engine** | How the main ramp is built | HSL lightness; Equal luminance | HSL lightness |
| **Mix in** | Space for tints, shades, tones and key sets | sRGB linear; CIELAB; OKLab; HSL | OKLab |
| **Steps** | Number of ramp steps | 3 to 21 | 11 |
| **Easing γ** | Bends the Equal luminance targets and the neutral ladder | 0.4 to 2.6, step 0.05 | 1.0 |
| **Full ramp** | Adds the ramp to The other sets | On or off | On |
| **Tints — toward white** | Shows tints | On or off | Off |
| **Shades — toward black** | Shows shades | On or off | Off |
| **Tones — toward grey** | Shows tones | On or off | Off |
| **Neutral ladder** | Shows greys | On or off | Off |

In the current version, **sRGB linear** mixes the same way as OKLab.

### Readouts

| Readout | What it shows |
| --- | --- |
| Caption | Steps, engine and mixing space |
| Base note | The base HEX, whether it is one of the steps ("step n" or "not a step") and γ |
| Strip and step rows | Each step's swatch, HEX, OKLab L and contrast against white |
| **Base OKLab L**, **Largest step**, **Smallest step**, **Evenness** | Lightness and step-size statistics in OKLab L; evenness as ±% |
| **Where the steps fall** | OKLab L of each step |
| **Base colour** | HEX, RGB, HSL, L\*a\*b\*, LCh, OKLab L, Y (luminance), vs white and vs black with ratings |
| **The other sets** | The sets ticked under Also show, each titled with its count; tiles show HEX and contrast against black |

## Ramps tab

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Compare** | Which engines to show | Every engine; One at a time | Every engine |
| **Measure evenness in** | Measure for the evenness figure and step-size chart | OKLab L; CIELAB L\*; Relative Y | OKLab L |
| **Endpoints** | Which evenness figure leads | Include black; Interior only | Include black |
| **Key sets** | The key list for the design-scale ladder | 50–950; 50–900 | 50–950 |

| Readout | What it shows |
| --- | --- |
| Engine rows | Name, what it holds even, a "same ramp as" badge where two engines produce the same colours, the strip, evenness with and without the end steps |
| **Step sizes, as the chosen measure sees them** | Chart and statistics of the gaps between steps |
| **Where the ramp sits in chroma** | The ramp, tints, shades and tones on the OKLab a–b plane |
| **Design-scale key sets** | The ladder for the chosen key list |

## Contrast tab

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Against** | The colour every step is measured against | White; Black; The base | White |
| **Metric** | Shown, but the table always lists both measures in the current version | WCAG 2.2; APCA | WCAG 2.2 |
| **Superseded APCA** | Adds the former approximate figure and the difference | Show the difference; Hide | Hide |

| Readout | What it shows |
| --- | --- |
| Caption and note | "Every step against …" and "WCAG 2.2 ratio · APCA-W3 0.1.9 Lc · n steps" |
| Table | Step, WCAG, Rating (AAA, AA, AA large, Fail), APCA Lc, and optionally Superseded and Difference |
| **The ladder** | A chart of the steps' contrast |

## Data tab

| Dataset | Status |
| --- | --- |
| sRGB transfer and primaries (IEC 61966-2-1:1999) | Verbatim |
| WCAG 2.2 contrast | Verbatim |
| OKLab matrices (Ottosson 2020) | Verbatim |
| OKLab lightness | Computed from linear sRGB |
| CIELAB (CIE 015:2018, D65) | Computed |
| Ramp engines (two distinct) | Computed |
| APCA Lc (APCA-W3 0.1.9) | Computed |
| Tailwind and Material palettes | Absent: key names only |

**Status** chips filter the list. **Install a table** ("Drop a CSV or JSON") does not load files in the current version.

## Export tab

| Control | What it does |
| --- | --- |
| **What to take** | The ramp; The key set; The contrast table; A link to this view |
| **As** | CSS, SCSS, JSON, CSV or URL, as fits the choice |
| Download button | Names and saves the file; for a link, **Copy the link** |
| **Copy to clipboard** | Copies the payload |
| Link field | Read-only; always shows the current link |
| **Analyse a list**, **Analyse** | Table of Hex, L\*, a\*, b\*, OKL, Y, Tints, Shades |
| **Download the result** | Copies the analysis as CSV to the clipboard |
| **Exactly what you will get** | Preview, size in bytes and a footer explaining the provenance lines |

Link parameters: `hex`, `engine` (`hsl`, `luminance`, or `contrast`), `steps`, `gamma`, `mode` (`srgb`, `lab`, `oklab`, `hsl`).

## Reference tab

| Control | What it does |
| --- | --- |
| **Standards**, **Formulas**, **Citations**, **Research notes** | Switch sections |
| **Filter** | Searches all four |

Standards include IEC 61966-2-1:1999, ITU-R BT.709-6, CIE 015:2018, WCAG 2.2, APCA-W3 0.1.9, the WCAG 3.0 working draft, the Design Tokens Format Module and Ottosson (2020). Formulas list 11 formulas as written, from the sRGB curve to the evenness measure. Citations list 14 references, tagged runs, context or names only, with corrected ones marked. Research notes describe six fixes. **Where these colours sit on the 1931 diagram** plots the ramp on the CIE 1931 chromaticity diagram.

## Save to Library

The floating **Save to Library** button saves the colours shown on the page as a palette in your Auric Artisan Library. A palette or colour sent back from the Library to this tool sets the base colour.
