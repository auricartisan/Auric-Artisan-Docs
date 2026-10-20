---
title: ICC Profile Parser — Reference
description: Every tab, control, header field, value table, tag type, readout, rule and export format in the ICC Profile Parser.
product: Website › Tools › Image and file tools › ICC Profile Parser
updated: 2026-09-25
---

# ICC Profile Parser reference

Address: https://auricartisan.com/tool/general/tools/icc-profile-parser/

## Tabs

| Tab | Contents |
|---|---|
| **Lab** | The drop box, header fields, **Compare against**, export buttons, and the full reading of the loaded profile |
| **Method** | Five sections explaining how each figure is derived |
| **Conformance** | All 23 rules, filterable by severity, with clauses and the two withdrawn checks |
| **Data** | The 20 entries that every figure rests on, filterable by status |
| **Export** | The contents, size and file name of the reading, and a preview |
| **Reference** | The nine published sources, filterable by whether they run in the tool |

## Lab tab — controls

| Control | What it does | Values |
|---|---|---|
| **Drop a profile** | Loads a profile by drag and drop, or opens a chooser when selected or when `Enter` or `Space` is pressed | `.icc`, `.icm` or `application/vnd.iccprofile` in the chooser |
| **Compare against** | Chooses the reference space for the diagram, the tone curve plot and the area cards | sRGB, Rec. 709, Display P3, Adobe RGB (1998), Rec. 2020, ProPhoto RGB |
| **Save the reading** | Downloads the reading as JSON | — |
| **Copy it** | Copies the reading to the clipboard | — |
| **Tag table, CSV** | Downloads the tag table as CSV | — |
| **Clear** | Removes the loaded profile | — |

Only one profile is loaded at a time. Loading another replaces it.

## Lab tab — What the header says

| Field | Shows | Example |
|---|---|---|
| **file** | The file name | `display.icc` |
| **size** | The size declared in the header, in bytes | 3,048 bytes |
| **version** | Major.minor.bug-fix, from bytes 8 and 9 | 2.1.0 |
| **class** | Four-character code and class name | mntr · display |
| **data space** | Data colour space and channel count | RGB · 3 ch |
| **PCS** | Profile connection space | nCIEXYZ |
| **intent** | Rendering intent number and name | 0 · perceptual |
| **CMM** | Preferred colour management module signature, or none declared | — |
| **platform** | Primary platform | Microsoft |
| **created** | Creation date and time, or **not a valid date** | 2024-03-18 09:30:00 |
| **tags** | Number of tags | 17 |
| **profile ID** | **not carried**, **matches** or **does NOT match** | not carried |

If the file cannot be read, the panel shows the file name and **status: unreadable**. Example values are illustrative.

## Value tables

### Device classes

| Code | Shown as |
|---|---|
| `scnr` | Input |
| `mntr` | Display |
| `prtr` | Output |
| `link` | DeviceLink |
| `spac` | ColorSpace |
| `abst` | Abstract |
| `nmcl` | NamedColor |

### Data colour spaces and the PCS

| Code | Shown as | Channels |
|---|---|---|
| `XYZ ` | nCIEXYZ | 3 |
| `Lab ` | CIELAB | 3 |
| `Luv ` | CIELUV | 3 |
| `YCbr` | YCbCr | 3 |
| `Yxy ` | CIEYxy | 3 |
| `RGB ` | RGB | 3 |
| `GRAY` | Grayscale | 1 |
| `HSV ` | HSV | 3 |
| `HLS ` | HLS | 3 |
| `CMYK` | CMYK | 4 |
| `CMY ` | CMY | 3 |
| `2CLR` to `FCLR` | 2 colour to 15 colour | 2 to 15 |

### Rendering intents

| Value | Shown as |
|---|---|
| 0 | Perceptual |
| 1 | Media-relative colorimetric |
| 2 | Saturation |
| 3 | ICC-absolute colorimetric |

### Platforms

| Code | Shown as |
|---|---|
| `APPL` | Apple |
| `MSFT` | Microsoft |
| `SGI ` | Silicon Graphics |
| `SUNW` | Sun Microsystems |
| All zeros | none declared |

## Tag types the tool reads

| Type | What it is | How the tool uses it |
|---|---|---|
| `text` | Plain text | Read |
| `desc` | Version 2 description text | Read |
| `mluc` | Multi-language text (version 4) | Read, every language record |
| `XYZ ` | One or more XYZ values | Colorants and white point |
| `curv` | Tone curve: identity, gamma or table | Tone curves and curve fit |
| `para` | Parametric tone curve, five function types | Tone curves and curve fit |
| `sf32` | Signed fixed-point array | The `chad` matrix |
| `sig ` | A signature | Read |
| `mft1` | lut8 table | Gamut hull for profiles without colorants; completeness check |
| `mft2` | lut16 table | As above |
| `mpet` | Multi-process elements (version 4) | Structure only: element count and types; not evaluated |
| `ncl2` | Named colour list | Structure only: count and up to 64 names; no colour resolved |

Any other type is listed in the tag table with its type code and is not decoded. The page does not print the text of description or copyright tags.

## Lab tab — the reading

| Element | Shown when | Contents |
|---|---|---|
| Verdict | A profile is loaded | Heading, distances, gamut source, conformance sentence, optional aside |
| **How close, and to what** | The profile has RGB colorants | Ranking of six spaces: **Space**, **Primaries Δu′v′**, **Curve fit**, **White**, **Verdict** |
| Chromaticity diagram | The profile has RGB colorants | CIE 1931 xy, 2° observer: stored colorants, primaries, reference space, white point |
| Gamut hull | No colorants, with a readable A2B table | CIELAB a*b* hull, rings every 20 |
| **Tone response** | The profile has RGB colorants | Red, green, blue and grey curves against the reference transfer function |
| Figure cards | A profile is loaded | **version**, **conformance**, **tags**, **area, u′v′**, **covers of it**, **area, xy** |
| **Findings** | A profile is loaded | One row per finding, or **All 23 rules hold** |
| **The tag table** | A profile is loaded | **Tag**, **Type**, **Offset**, **Size**, **Anything notable** |

The note beside **Findings** gives the tag count and how many tags share an element. The **Anything notable** column shows one of: **outside the file**, **could not be decoded**, **shares this element with** another tag, **not 4-byte aligned**, or a dash.

## Reference spaces

| Space | Defined by | White | Transfer function used for the curve fit |
|---|---|---|---|
| sRGB | IEC 61966-2-1:1999 | D65 | Piecewise sRGB curve |
| Rec. 709 | ITU-R BT.709-6 | D65 | 2.4 power |
| Display P3 | SMPTE RP 431-2 primaries, sRGB transfer | D65 | Piecewise sRGB curve |
| Adobe RGB (1998) | Adobe RGB (1998) Color Image Encoding | D65 | Power of 563/256 |
| Rec. 2020 | ITU-R BT.2020-2 | D65 | BT.2020 curve |
| ProPhoto RGB | ISO 22028-2:2013 (ROMM RGB) | D50 | 1.8 power with a linear toe |

sRGB and Rec. 709 share their primaries and white, so only the tone curve can tell them apart.

## Conformance rules

The 23 rules, with their severities and clauses, are listed in [Check conformance](check-conformance.md). Summary: 11 errors, 8 warnings, 4 notes; 2 rules are house preferences with no clause.

## Method tab

| Section | Contents |
|---|---|
| **The header** | Bytes 8 to 11 of the loaded profile (or an example), and how the version is read |
| **Colorant vs primary** | sRGB's stored colorants against its primaries, and the two adaptation hypotheses |
| **Identification** | Why a raw white-point term cannot be part of the score, and the order of the comparison |
| **Gamut area** | Each reference space as a percentage of sRGB in xy and u′v′, and its coverage of sRGB |
| **A profile with no colorants** | How an A2B table becomes a CIELAB hull, with figures when such a profile is loaded |

## Conformance tab

| Element | Contents |
|---|---|
| **Rules** buttons | **All** (23), **Errors** (11), **Warnings** (8), **Notes** (4) |
| Rail note | How many rules are shown, and how many cite no clause |
| **Withdrawn** | Two checks removed because they fired on correct files |
| **The rules that stayed, and what each cites** | Every rule with severity and clause, or **house preference** |
| **What the old validator got right** | The checks carried across unchanged |

## Data tab

Status buttons: **All** (20), **Verbatim** (8), **Computed** (7), **Stand-in** (2), **Absent** (3). Select an entry to expand it; stand-in and absent entries add **what it would take**.

| Status | Meaning | Entries |
|---|---|---|
| **Verbatim** | A published table, clause or definition carried unaltered | Header, tag table rules, required tags, CIE 1931 observer, sRGB, the other spaces, Bradford, MD5 |
| **Computed** | Derived here by stated arithmetic | Primaries, adaptation method, identification, area and coverage, curve fit, profile ID, CLUT gamut |
| **Stand-in** | The tool's own choice in place of something published | The list of six spaces; the severity each rule carries |
| **Absent** | Named but not held | Evaluating `mpet` pipelines; resolving named colours; any measurement of the device |

## Reference tab

Status buttons: **All** (9), **Runs** (7), **Partly** (1), **Not held** (1).

| Source | Status |
|---|---|
| ISO 15076-1:2010 / ICC.1:2010 | Runs |
| IEC 61966-2-1:1999 (sRGB) | Runs |
| CIE 015:2018, Colorimetry | Runs |
| Lam (1985), the Bradford matrix | Runs |
| ITU-R BT.709-6, SMPTE RP 431-2:2011, Adobe RGB (1998), ITU-R BT.2020-2, ISO 22028-2:2013 | Runs |
| CIE 142-2001 (CIEDE2000) | Runs |
| RFC 1321 (MD5) | Runs |
| ICC.1:2010 §10.14, multiProcessElementsType | Partly |
| ICC.1:2010 §10.17, namedColor2Type | Not held |

## Export formats

| File | Name | Contents |
|---|---|---|
| Reading | *profile-name*`-reading.json` | Header with clauses, tags, identity, gamut, conformance, register |
| Tag table | *profile-name*`-tags.csv` | `signature,type,offset,size,aligned,in_bounds,shares_with` |

See [Export a reading](export-a-reading.md) for the fields.

## Messages

| Message | When |
|---|---|
| **Read** followed by the file name | A profile was read |
| **A profile is at least 132 bytes; this file is** N. | The file is too short to be a profile |
| **Bytes 36-39 are** "…", **not 'acsp' — this is not an ICC profile.** | The file lacks the profile signature |
| **The reader could not get through this file:** followed by a reason | Reading stopped unexpectedly |
| **That file could not be read** | The browser could not read the file |
| **Load a profile first** | An export was requested with nothing loaded |
| **Saved the reading** / **Copied the reading** / **Saved the tag table** | An export succeeded |
| **The clipboard refused** | Clipboard access was blocked |
| **Cleared** | **Clear** was selected |

When a file cannot be read, the verdict area turns red and reads **This file could not be read**, followed by the reason.
