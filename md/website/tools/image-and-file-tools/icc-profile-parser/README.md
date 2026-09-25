---
title: ICC Profile Parser — Overview
description: What the ICC Profile Parser does, who it is for, where to find it and how to read a first profile.
product: Website › Tools › Image and file tools › ICC Profile Parser
updated: 2026-09-25
---

# ICC Profile Parser

The ICC Profile Parser (the page is titled **ICC Profile Reading**) opens a colour profile file, `.icc` or `.icm`, and tells you what it says. An ICC profile is a small file, defined by the International Color Consortium, that describes how a device or colour space reproduces colour, so that software can convert colours between devices. The tool reads the profile's header at the byte positions the ICC specification (ICC.1:2010, also published as ISO 15076-1:2010) sets out, lists every tag in the file, and runs a conformance check in which every finding names the clause of the specification it enforces.

For RGB display-style profiles, it recovers the primaries behind the stored colorants, draws them on a CIE 1931 chromaticity diagram, plots the tone curves, and identifies which of six well-known colour spaces the profile matches most closely: sRGB, Rec. 709, Display P3, Adobe RGB (1998), Rec. 2020 or ProPhoto RGB. It reports gamut area and coverage against the space you choose, using the more even CIE 1976 u′v′ diagram. For press and other profiles with no colorants, it walks the profile's lookup table to draw the gamut in CIELAB instead.

The file is read in the page and never sent anywhere. You can save the whole reading as JSON, copy it, or save the tag table as CSV.

## Who it is for

- Designers and photographers checking what a monitor, camera or printer profile actually contains.
- Colour-management and prepress staff triaging a profile that an application rejects.
- Developers who need the header fields, the tag table and a clause-by-clause verdict to paste into a ticket.
- Students learning how ICC profiles are put together.

## Where to find it

Open https://auricartisan.com/tool/general/tools/icc-profile-parser/ in a current browser. It is listed as **ICC Parser** on the Collections page at https://auricartisan.com/collections/. Nothing needs installing.

## Quick start

1. Open the tool. The **Lab** tab is selected.
2. Drop an `.icc` or `.icm` file on the **Drop a profile** box, or select the box to choose one.
3. Read the verdict under **What this profile is**, for example "An sRGB profile, matrix/TRC, ICC v2.1.0".
4. Check **What the header says** on the left for the version, class, data space, connection space and more.
5. Look at the **conformance** card and the **Findings** list for anything that breaks the specification.
6. Select **Save the reading** to download the full reading as JSON.

## What you can do

- Read every header field: size, version, device class, data colour space and channel count, connection space, rendering intent, CMM, platform, creation date, tag count and profile ID.
- See every tag with its type, offset and size, and which tags share one data element.
- Recompute the profile ID and see whether it matches the bytes.
- Identify the closest of six reference colour spaces, with primaries distance, tone-curve fit and the adaptation the profile was built with.
- Compare gamut area and coverage against any of the six spaces in CIE 1976 u′v′, with the CIE 1931 xy figure alongside.
- Plot stored colorants, recovered primaries and the reference space on a chromaticity diagram, and the tone curves against the reference transfer function.
- Draw the CIELAB a*b* gamut of a CMYK or other LUT-based profile from its A2B table.
- Run 23 conformance rules, each graded error, warning or note and citing its clause.
- Export the reading as JSON and the tag table as CSV.

## In this folder

- [docs/](docs/README.md) — how to use the tool.
  - [Getting started](docs/getting-started.md) — open it, the screen tour, the first profile.
  - [Understand ICC profiles](docs/understand-icc-profiles.md) — classes, tags, the connection space, versions, intents and curves.
  - [Identify a profile and read its gamut](docs/identify-and-gamut.md) — the verdict, the ranking, the diagram, area and coverage, tone curves.
  - [Check conformance](docs/check-conformance.md) — findings, severities, clauses and the rule list.
  - [Export a reading](docs/export-a-reading.md) — JSON, clipboard and the tag table CSV.
  - [Reference](docs/reference.md) — every field, tag, value, rule and file format.
  - [Troubleshooting](docs/troubleshooting.md) — symptoms, causes and fixes.
  - [FAQ](docs/faq.md) — short answers to common questions.
- [others/](others/README.md) — background material.
  - [Glossary](others/glossary.md) — terms used in this tool.
  - [Limits and accuracy](others/limits-and-accuracy.md) — what it can and cannot read, and how precise it is.
  - [Related](others/related.md) — related tools and Learn articles.
  - [Release notes](others/release-notes.md) — user-facing history.
  - [Privacy](others/privacy.md) — what stays in your browser.
