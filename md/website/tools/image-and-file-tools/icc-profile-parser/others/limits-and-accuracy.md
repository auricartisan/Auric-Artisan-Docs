---
title: ICC Profile Parser — Limits and accuracy
description: What the ICC Profile Parser can and cannot read, how precise its figures are, and what it is not.
product: Website › Tools › Image and file tools › ICC Profile Parser
updated: 2026-09-25
---

# Limits and accuracy

## What it reads

- Standalone profile files of ICC version 2 and version 4, at the byte positions ICC.1:2010 (ISO 15076-1:2010) gives.
- The whole header, the full tag table, and the tag types listed in the [Reference](../docs/reference.md): text, descriptions, multi-language text, XYZ values, tone curves in every form, the `chad` matrix, signatures, and lut8 and lut16 tables.
- A tag that cannot be decoded is reported as a finding, and the rest of the profile is still read.

## What it cannot read

| Item | What happens |
|---|---|
| Profiles embedded in images or PDFs | Not read. Save the profile out as its own file first |
| Version 4 `mAB `, `mBA ` tables | Listed in the tag table but not decoded; no gamut hull is drawn from them |
| `mpet` (multi-process elements) | Its structure is read; the pipeline is not run, so its behaviour is not measured |
| `ncl2` named colours | Not resolved to colours and not listed on the page |
| Private tags such as `vcgt` | Listed with their type, not decoded |
| Description and copyright text | Read, but not printed on the page or in the reading |

## How the figures are found, and how precise they are

| Figure | Method | Notes |
|---|---|---|
| Header fields | Read directly at the published offsets | Exact |
| Profile ID match | MD5 recomputed with the flags, intent and ID fields zeroed | Exact |
| Primaries | Colorants un-adapted with the profile's `chad` tag, or with Bradford from an assumed white | Exact with `chad`; an estimate without, and the caption says so |
| **Primaries Δu′v′** | Largest per-primary distance in CIE 1976 u′v′, after adapting the reference into the PCS | Two adaptation methods tried; the closer is reported |
| **Curve fit** | Peak difference from the reference transfer function over 257 samples | Uses the red curve, or the grey curve for greyscale |
| **area, u′v′** and **area, xy** | Triangle area ratios | Area, not coverage |
| **covers of it** | Polygon intersection in u′v′ | At most 100% |
| CIELAB hull | Every grid point of the A2B1 (or A2B0) table converted to CIELAB, then its outline | Up to 200,000 grid points |
| Spectral locus | CIE 1931 2° observer, 380 to 700 nm at 5 nm | Taken from CIE 015:2018 data |

## Choices the tool makes

These are listed as **Stand-in** on the **Data** tab.

- **The six reference spaces.** Identification means closest among sRGB, Rec. 709, Display P3, Adobe RGB (1998), Rec. 2020 and ProPhoto RGB. Each definition is taken from its own publication; the choice of list is the tool's.
- **Severity.** The grade of each rule (error, warning or note) is the tool's judgement. Each rule states its clause so you can apply your own.

## What it is not

- **Not a device measurement.** Everything on the page is a reading of a file. Whether the display, printer or press still behaves as the profile says is a question for a measuring instrument and the device. A profile that is internally perfect can describe a monitor that has drifted since calibration.
- **Not an official validator.** The conformance check cites the specification clause by clause, but it is not the International Color Consortium's own validation tool.
- **Not a profile editor or converter.** It does not change profiles or convert colours through them.
