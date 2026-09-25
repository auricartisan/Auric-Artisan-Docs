---
title: ICC Profile Parser — Export a reading
description: Save or copy the full JSON reading of a profile, save its tag table as CSV, and see what each export contains.
product: Website › Tools › Image and file tools › ICC Profile Parser
updated: 2026-09-25
---

# Export a reading

A reading is the tool's full account of a profile as a JSON file: the header with the clause behind each field, the tag table, the identification, the gamut figures and every conformance finding. Every derived figure carries the clause or the method it came from, so someone else can check it without opening this page.

## Save the reading

1. Load a profile on the **Lab** tab.
2. Under **Take it away**, select **Save the reading**.
3. Your browser downloads a file named after the profile, for example `srgb-color-space-profile-reading.json` for `sRGB Color Space Profile.icm`. The name is the file name in lower case, with the `.icc` or `.icm` ending removed and anything other than letters and digits turned into hyphens.

If no profile is loaded, the message reads **Load a profile first** and nothing is saved.

## Copy the reading

Select **Copy it** to place the same JSON on the clipboard, ready to paste into a ticket or a message. The message reads **Copied the reading**, or **The clipboard refused** if your browser blocks clipboard access.

## Save the tag table as CSV

Select **Tag table, CSV** to download a spreadsheet-ready list of every tag, named like the reading but ending `-tags.csv`.

```text
signature,type,offset,size,aligned,in_bounds,shares_with
desc,desc,240,108,yes,yes,
A2B0,mft2,576,41094,yes,yes,A2B2
```

| Column | Meaning |
|---|---|
| `signature` | The tag's four-character signature |
| `type` | The four-character type at the start of its data |
| `offset` | Where the data starts, in bytes from the start of the file |
| `size` | The length of the data in bytes |
| `aligned` | `yes` if the offset is a multiple of 4 |
| `in_bounds` | `yes` if the data lies inside the file |
| `shares_with` | Other tags pointing at the same data, separated by spaces |

The rows in the example are illustrative.

## Clear

**Clear** removes the loaded profile from the page and returns the **Lab** tab to **Nothing loaded yet**. The message reads **Cleared**.

## Preview the reading on the Export tab

The **Export** tab shows what the reading will contain before you save it.

- On the left, **What to take** lists the parts: the reading as JSON, the header with clauses, the tag table, and the conformance rules and findings, followed by the **size** of the reading in KB and its **file name**.
- On the right, **What the reading says about itself** explains the provenance, and **The reading, as it will be written** shows the JSON. Long readings are cut after 58 lines, with a count of the lines not shown; the saved file is always complete.

## What the reading contains

| Section | Contents |
|---|---|
| `tool`, `specification`, `generated` | The tool name, the specification (ISO 15076-1:2010), and the date and time of the reading |
| `file` | The file name and its size in bytes |
| `header` | Version, device class, data space, PCS, rendering intent, PCS illuminant, creation date and profile ID, each with its clause |
| `tags` | Every tag: signature, type, offset, size, alignment, whether it is in bounds, and any tags it shares data with |
| `identity` | For RGB profiles with colorants: the closest space, primaries distance, curve fit, adaptation, and the full ranking |
| `gamut` | For RGB profiles: the space compared against, stored colorants, recovered primaries, area ratios in u′v′ and xy, and coverage |
| `gamut` (no colorants) | For profiles walked from an A2B table: the table, grid points, a*b* hull area, lightness range and encoding |
| `conformance` | Number of rules, number passed, whether conformant, and every finding with severity, clause, title and detail |
| `register`, `registerCounts` | The status and source of every entry on the **Data** tab |

For a file that could not be read, the reading holds the file details and the error message.

The `profileId` entry holds the stored ID, the recomputed ID, and `matches`: `true`, `false`, or `null` when the profile carries no ID. The `identity` entry records that the white point does not contribute to the comparison. The `gamut` and `conformance` entries each carry a short note explaining their figures.

The reading uses the space currently chosen under **Compare against** for the gamut figures. Choose the space you want before saving.
