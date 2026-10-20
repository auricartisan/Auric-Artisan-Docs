---
title: ICC Profile Parser — Troubleshooting
description: Symptoms you may meet in the ICC Profile Parser, why they happen, and what to do.
product: Website › Tools › Image and file tools › ICC Profile Parser
updated: 2026-09-25
---

# Troubleshooting the ICC Profile Parser

## The file will not read

| Symptom | Why | What to do |
|---|---|---|
| **A profile is at least 132 bytes; this file is** N. | The file is too short to hold a header and tag count | Check you chose the right file; it may be empty or cut short by a failed download |
| **Bytes 36-39 are** … **not 'acsp' — this is not an ICC profile.** | The file does not carry the ICC signature | You may have dropped an image, a PDF or another format. Save the embedded profile out as a standalone `.icc` file first |
| My `.icc` file is greyed out in the file chooser | The chooser filters for `.icc` and `.icm` | Drag the file onto the **Drop a profile** box instead, or rename it with the right ending |
| **The reader could not get through this file:** … | Reading stopped part-way, usually because the file is damaged | Try the original source of the profile. The reason after the colon says where it failed |
| **That file could not be read** | The browser could not open the file | Check the file is not locked or still downloading, then try again |

## A panel is empty or missing

| Symptom | Why | What to do |
|---|---|---|
| No ranking table, diagram or tone curves | The profile has no RGB colorants (for example a CMYK, greyscale or LUT-only RGB profile) | This is expected. A CMYK profile with an A2B table shows a CIELAB hull instead |
| No gamut hull for a CMYK profile | Its A2B table is in a version 4 format, is incomplete, has more than 200,000 grid points, or is missing | The header, tags and findings are still read; the gamut cannot be drawn |
| The area cards show a dash | Area and coverage apply only to profiles with RGB colorants | — |
| I cannot see the profile's name | The page does not print the text of the description tag | The tag table shows whether `desc` is present; open the profile in another viewer to read the name |
| A tag's row says **could not be decoded** | Its data is damaged or shorter than its type needs | See the **Every tag payload could be decoded** finding for the reason |

## The figures look wrong

| Symptom | Why | What to do |
|---|---|---|
| The area figures seem to refer to another space | After loading, the comparison moves to the closest space, but the menu label may still show your earlier choice | Choose the space you want from **Compare against** |
| sRGB and Rec. 709 tie in the ranking | They share primaries and white; only the tone curve separates them | Read the aside under the verdict; a profile with no tone curve cannot be told apart |
| **area, u′v′** is over 100% | It is an area ratio; a larger gamut gives more than 100% | Use **covers of it** to see how much of the reference space is covered |
| **area, xy** differs from **area, u′v′** | The xy diagram is uneven; the u′v′ figure is the more meaningful | Quote the u′v′ figure, and name it |
| The verdict names a space that seems wrong | Closest means closest among six | Compare the first and second rows of the ranking; a large distance means none of the six is a good match |
| The caption says the primaries were recovered with an assumed white | The profile carries no `chad` tag, so the white it was adapted from is not recorded | Treat the gold triangle as a best estimate |

## Findings

| Symptom | Why | What to do |
|---|---|---|
| **The profile ID matches the bytes** raised as a warning | The file was changed after its ID was written, or the ID was written incorrectly | Get a fresh copy from the source of the profile |
| **A v4 profile carries a profile ID** raised | A version 4 profile has an all-zero ID | It is graded a warning, not an error; regenerate the profile if your workflow needs the ID |
| **Media white point is the PCS white** raised on a display profile | The white point tag holds the display's measured white instead of D50 | Common in older version 2 profiles; version 4 requires D50 here |
| **Declared size matches the file** raised as an error | The file was cut short or padded after writing | Get an undamaged copy |
| **A LUT tag holds the grid its header declares** | A table is shorter than its header says, often from a truncated download | Download the profile again |

## Clipboard and downloads

| Symptom | Why | What to do |
|---|---|---|
| **The clipboard refused** | Your browser blocked clipboard access | Allow clipboard access for the site, or use **Save the reading** |
| **Load a profile first** | Nothing is loaded | Drop a profile on the **Lab** tab first |

For help with the site in general, see [Help](../../../../../help/README.md).
