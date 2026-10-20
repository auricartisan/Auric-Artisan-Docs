---
title: LUT Lab — Load a .cube file
description: Load a 1D or 3D .cube file, read what the tool reports about it, and switch between the file and the built-in looks.
product: Website › Tools › Image and file tools › LUT Lab
updated: 2026-09-25
---

# Load a .cube file

## Load the file

1. On the **Lab** tab, drop a `.cube` file on **Drop a .cube**, or select the box to choose one. The chooser offers `.cube` and plain-text files.
2. A message confirms **Loaded** followed by the file name, and says how many notes there are if the tool found any.
3. The before and after pair now shows your file applied to the current scene. The label above the pair shows the file's title, or its name if it has none.

While a file is shown, the look menu and **Strength** are greyed out and the note under them reads **The pair is showing the loaded file. The looks are paused.** A loaded file is always applied at full strength.

## The file card

A card under the drop box describes the file.

| Line | Meaning | Example |
|---|---|---|
| Heading | The `TITLE` in the file, or the file name | Warm Film |
| **kind** | 1D or 3D | 3D |
| **size** | For 3D, N³ and the number of rows; for 1D, the number of rows | 33³ (35937 rows) |
| **domain** | The declared input range for red, green and blue | [0.000, 0.000, 0.000] – [1.000, 1.000, 1.000] |
| **reachable** | The share of the table that an 8-bit sRGB input can reach | 100.0% |

Under these lines is a list of notes. When there is nothing to report it reads **no discrepancies between the header and the body**.

## What the reader accepts

LUT Lab reads the `.cube` format as defined in the Adobe / IRIDAS Cube LUT Specification 1.0.

| Item | Handling |
|---|---|
| `TITLE "…"` | Read and shown as the file's name |
| `LUT_3D_SIZE N` | A 3D table of N × N × N rows, red index changing fastest |
| `LUT_1D_SIZE N` | A 1D table of N rows |
| `DOMAIN_MIN r g b`, `DOMAIN_MAX r g b` | The input range; 0 to 1 when absent |
| Lines starting with `#` | Comments, ignored |
| Blank lines | Ignored |
| Rows of three numbers | Table data |
| Any other keyword | Ignored |

Only `.cube` is supported. Other LUT formats, such as `.3dl`, need converting to `.cube` in another program first.

## Notes the tool may add

| Note | Meaning | What happens |
|---|---|---|
| The file carries N rows beyond the ones the header declares | Extra data rows | The extra rows are ignored |
| No `LUT_3D_SIZE` in the file, but the row count is a whole cube | The size keyword is missing | The file is read as a 3D table of that size |
| No size keyword, and the row count is not a cube | The size keyword is missing | The file is read as a 1D table with one row per line |
| The declared domain is wider than 0 to 1 | Part of the table is for inputs above 1 or below 0 | The reachable share is given; only that part can affect an 8-bit picture |

The specification requires a size keyword, so a file that needed a guess is worth fixing at its source.

## Files that cannot be read

| Message | Why |
|---|---|
| empty file | The file has no content |
| `LUT_3D_SIZE` N needs M rows; the file has K | The file is shorter than its header says |
| `LUT_1D_SIZE` N needs N rows; the file has K | As above, for a 1D file |
| no `LUT_1D_SIZE` or `LUT_3D_SIZE` keyword and no usable sample rows | Nothing in the file looks like a table |

When a file cannot be read, the card shows **status: not loaded** with the reason, and the pair keeps showing the look.

## How the file is applied

Each pixel of the scene is taken as 8-bit sRGB values, scaled to 0 to 1, placed within the file's domain, and looked up: with trilinear interpolation for a 3D table, or straight-line interpolation per channel for a 1D table. The result is rounded back to 8 bits. See [LUT concepts](lut-concepts.md).

## Switch between the file and the looks

- **Back to the looks** (shown while a file is applied) returns the pair to the built-in look and keeps the file loaded.
- Choosing a look from the menu, or **Show it on the pair** on the **Looks** tab, also switches back to the looks.
- **Clear the file** removes the file entirely and returns to the looks. The message reads **Cleared the loaded file**.

To apply the file again after going back to the looks, drop it again.

## Resample or convert the file

While a file is applied, the **Export** tab writes that file's transform. You can use this to save the same LUT at a different size, or as a 1D curve. See [Write a .cube file](write-a-cube-file.md) for what changes when you do.
