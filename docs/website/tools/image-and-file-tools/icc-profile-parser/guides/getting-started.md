---
title: ICC Profile Parser — Getting started
description: Open the ICC Profile Parser, find your way around its tabs, and read a first profile.
product: Website › Tools › Image and file tools › ICC Profile Parser
updated: 2026-09-25
---

# Getting started with the ICC Profile Parser

## Open the tool

Go to https://auricartisan.com/tool/general/tools/icc-profile-parser/. The page opens on the **Lab** tab. Until you load a file, the main panel reads **Nothing loaded yet** and explains what the tool will and will not tell you.

A note under the heading explains what the numbers on the page are measurements of. It has no close button on purpose.

## Find a profile to read

An ICC profile is a file ending in `.icc` or `.icm` that describes how a device or colour space reproduces colour. Your computer already has some:

- **Windows:** `C:\Windows\System32\spool\drivers\color\`
- **macOS:** `/Library/ColorSync/Profiles/`, `~/Library/ColorSync/Profiles/` and `/System/Library/ColorSync/Profiles/`

Monitor calibration software, printer drivers and paper manufacturers also supply profiles.

The tool reads standalone profile files. A profile embedded inside a JPEG, PNG, TIFF or PDF must first be saved out as its own file by another application.

## The screen at a glance

| Tab | What it is for |
|---|---|
| **Lab** | Load a profile; read the header, verdict, diagrams, figures, findings and tag table |
| **Method** | How each figure is derived, in five sections |
| **Conformance** | The rules the check runs, filtered by severity, with the clause each one enforces |
| **Data** | Every figure and what it rests on; the tab shows the number of entries (20) |
| **Export** | What the JSON reading contains, and a preview of it |
| **Reference** | The published sources, marked by whether they run in the tool |

### The Lab tab

- **The left-hand panel** holds **The profile** (the drop box), **What the header says** (the header fields), **Compare against** (a menu of six reference spaces), and **Take it away** (four buttons: **Save the reading**, **Copy it**, **Tag table, CSV** and **Clear**).
- **The right-hand panel** shows, once a profile is loaded, **What this profile is**: the verdict, the ranking table **How close, and to what**, the chromaticity diagram and tone-curve plot, six figure cards, the **Findings** list and **The tag table**.

## Read a first profile

1. Drop a profile on the **Drop a profile** box, or select the box (or press `Enter` or `Space` while it has focus) to open a file chooser. The chooser offers `.icc` and `.icm` files.
2. A message confirms **Read** followed by the file name.
3. Read the verdict at the top of the right-hand panel. For a standard sRGB profile it reads "An sRGB profile, matrix/TRC, ICC v2.1.0", followed by how far its colorants sit from sRGB's primaries, how well its tone curve fits, and whether it is conformant.
4. In **What the header says**, check **version**, **class**, **data space**, **PCS** and **intent**. The **profile ID** line says **not carried**, **matches** or **does NOT match**.
5. Look at the cards under the diagrams. **conformance** reads **clean** when no rule raised anything, **no errors** when only warnings or notes were raised, or the number of errors.
6. Scroll to **Findings** to see any rule the profile does not meet, each with its severity and clause.
7. Scroll to **The tag table** to see every tag the file contains.
8. Select **Save the reading** to download the full reading as a JSON file.

You should now know what kind of profile it is, which colour space it describes, and whether anything in it breaks the specification.

## Next steps

- If the terms on the page are unfamiliar, read [Understand ICC profiles](understand-icc-profiles.md).
- To interpret the ranking, the diagram and the area figures, read [Identify a profile and read its gamut](identify-and-gamut.md).
- To understand a finding, read [Check conformance](check-conformance.md).
