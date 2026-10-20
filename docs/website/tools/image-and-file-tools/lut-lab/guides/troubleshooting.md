---
title: LUT Lab — Troubleshooting
description: Symptoms you may meet in LUT Lab, why they happen, and what to do.
product: Website › Tools › Image and file tools › LUT Lab
updated: 2026-09-25
---

# Troubleshooting LUT Lab

## Loading a .cube

| Symptom | Why | What to do |
|---|---|---|
| **LUT_3D_SIZE N needs M rows; the file has K** | The file is shorter than its header says, often from a failed download | Download the file again |
| **no LUT_1D_SIZE or LUT_3D_SIZE keyword and no usable sample rows** | The file is not a `.cube`, or is empty of data | Check the file; convert other LUT formats to `.cube` first |
| **empty file** | The file has no content | Choose the right file |
| My `.3dl` or other LUT file is greyed out or will not load | Only `.cube` is supported | Convert it to `.cube` in another program |
| A note says rows beyond the declared number were ignored | The file has extra data rows | Check the file at its source; the declared table is used |
| A note says the file was read as a 1D or 3D table because no size keyword was found | The size keyword is missing | The guess is stated; fix the file at its source if it is wrong |
| **reachable** is below 100% | The file's domain is wider than 0 to 1, for example for HDR or log footage | Only part of the table affects 8-bit sRGB pictures; the file was made for different input |
| The result looks badly wrong, with red and blue swapped | The file was written by a program that orders rows blue fastest | Re-export it from its source with the standard order; LUT Lab reads red fastest, as the format requires |
| The result is far too flat or too contrasty | The LUT was made for a different input, such as log camera footage | Apply it only to the kind of input it was made for |

## Looks and controls

| Symptom | Why | What to do |
|---|---|---|
| The look menu and **Strength** are greyed out | A loaded file is being shown | Select **Back to the looks** or **Clear the file** |
| **Tone-map exposure** is greyed out | It applies only to **Reinhard tone-map** | Choose that look |
| **Strength** has no effect on my file | Loaded files are always applied at full strength | Blend in the program where you use the LUT |
| I went back to the looks and cannot show my file again | **Back to the looks** keeps the file but offers no way back | Drop the file again |

## Your picture

| Symptom | Why | What to do |
|---|---|---|
| **That image could not be read** | The browser could not decode the picture | Save it as PNG or JPEG and try again |
| My picture looks small | Pictures are scaled to fit 480 × 270 for the analysis | This is expected; the figures cover the whole picture |
| My picture disappeared | Selecting a drawn scene removes your picture | Drop it again |

## Exports

| Symptom | Why | What to do |
|---|---|---|
| A 1D export has lost the look's colour | A 1D curve keeps only what the transform does to greys | Export as **3D cube** |
| A resampled file differs slightly from the original | Resampling looks up each new grid point with interpolation and rounds to 8 bits | Keep the original; resample only when you need a different size |
| Another program reports banding or small errors | LUT Lab works in 8 bits, and the values in the file are one of 256 levels | Use the file for 8-bit work, or make high-precision LUTs in a tool with a floating-point pipeline |
| **The clipboard refused** | Clipboard access was blocked | Allow clipboard access for the site, or use **Save the .cube** |

## Share links

| Symptom | Why | What to do |
|---|---|---|
| The link opened without my `.cube` or picture | Links carry only the scene, look, strength, exposure, size and kind | Send the files separately |
| After opening a link, the **Kind** menu or **Size** slider looks different from the file preview | The export uses the linked kind and size; the controls may not move to match | Trust the size label and the file preview, or set **Kind** and **Size** again |

For help with the site in general, see [Help](../../../../../help/README.md).
