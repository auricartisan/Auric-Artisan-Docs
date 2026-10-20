---
title: Illuminants — Query many illuminants at once
description: Use the Console tab's query language to tabulate, sort, plot and export readings for many illuminants.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Query many illuminants at once

The **Console** tab answers questions such as "which of these lights is furthest from the Planckian locus?" in one table. You type a short query; the lab computes every requested column with the same engine the other tabs use, so a console row and a Lab reading cannot disagree. The query is parsed, never run as code.

## Steps

1. Open the **Console** tab. The **Query** box already holds an example.
2. Edit the query, or select one of the **Recipes** to load a ready-made one.
3. Select **Run**, or press `Ctrl` + `Enter` in the query box.
4. Read the **Results** table. Its heading shows the number of rows. The status line beside the buttons shows rows, time taken and the interval and interpolation used.
5. Under **Any two columns, plotted**, choose a **Horizontal axis** and a **Vertical axis**. The scatter plot labels each point with the illuminant name.
6. Select **CSV** or **JSON** to download the results.

## The grammar

A query is a few lines, each starting with a keyword. Anything after `//` on a line is a comment.

| Line | What it does | Example |
| --- | --- | --- |
| `select` | The illuminants to include, separated by commas or spaces. Names are case-insensitive. A range such as `F1..F12` expands to every name in between. | `select A, D50, D65, F1..F12` |
| `with` | Pipeline settings as `name=value` pairs. | `with interval=1nm, interpolation=sprague` |
| `report` | The columns to show, in order. | `report x, y, CCT, Duv` |
| `order by` | Sort by one reported column, `asc` (default) or `desc`. | `order by Duv desc` |
| `limit` | Keep only the first n rows after sorting. | `limit 8` |

### Names you can select

A, D50, D55, D65, D75, E and F1 to F12.

### Settings for `with`

| Setting | Values | Notes |
| --- | --- | --- |
| `interval` | `1nm`, `5nm`, `10nm` | Any other value falls back to the interval set on the Methods tab. |
| `interpolation` | `linear`, `sprague`, `pchip` | Any other value falls back to the Methods tab setting. |
| `observer` | `2deg` | Accepted for readability. Only the CIE 1931 2° observer is held. |

### Columns for `report`

| Column | Shown as | Meaning | Decimals |
| --- | --- | --- | --- |
| `x`, `y` | x, y | CIE 1931 chromaticity | 5 |
| `u`, `v` | u′, v′ | CIE 1976 chromaticity | 5 |
| `cct` | CCT | Correlated colour temperature (Ohno); blank when not valid | 0 |
| `duv` (also `d_uv`) | Duv | Signed distance from the Planckian locus | 5 |
| `efficacy` (also `eff`) | lm/W | Luminous efficacy of radiation | 1 |
| `entropy` | Entropy | A measure of how spread out the spectrum is | 3 |
| `peak` | Peak nm | Wavelength of the highest power | 0 |

If you leave out `report`, the table shows x, y, CCT and Duv.

## The recipes

| Recipe | What it asks |
| --- | --- |
| **The whole catalogue by CCT** | All 18 illuminants at 5 nm: x, y, CCT, Duv and efficacy, sorted by CCT |
| **Which sources are furthest off the locus** | CCT, Duv and entropy, sorted by Duv descending, top 8 |
| **Luminous efficacy against spectral spread** | Efficacy, entropy and peak, sorted by efficacy descending |
| **The D series at 1 nm** | D50, D55, D65 and D75 at 1 nm with Sprague interpolation |

## Stand-in rows

Fluorescent illuminants F1 to F12 are built from stand-in spectra, not the CIE tables. Their rows carry a **stand-in** tag in the table, "(stand-in)" after the name in the CSV, and `"synthetic": true` in the JSON. Do not quote them as CIE values.

## The export files

- **CSV** downloads `illuminants.csv`. The first line is a comment recording the observer, interval and interpolation; then a header row (`source` and your columns) and one row per illuminant.
- **JSON** downloads `illuminants.json` with the generation time, the pipeline settings, the column list and one entry per row (name, synthetic flag and values).

The buttons do nothing until a query has returned rows.

## Result

You have a sorted table of readings for the lights you chose, a scatter plot of any two columns, and a file you can open in a spreadsheet.
