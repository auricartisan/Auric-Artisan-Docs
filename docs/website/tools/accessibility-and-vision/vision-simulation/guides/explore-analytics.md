---
title: Vision Lab — Explore Analytics
description: See the whole collection of vision conditions by category and severity, and export the catalogue as JSON or CSV.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Explore Analytics

**Analytics** maps the collection of conditions: which categories they fall into, how severe they are estimated to be, and which are the most severe. It reflects the conditions currently showing, so it follows the Catalogue's **Level** and **Kind** filters.

## Views

Choose a view under **View**:

| View | What it shows |
| --- | --- |
| **Matrix** | A grid of categories against severity. Each cell counts how many conditions land there. |
| **Map** | A map of how the conditions relate to each other |
| **Statistics** | Figures for the collection |

## The matrix

- Rows are categories and columns are severity scores, running left to right. Each row ends with its count and mean severity, and the last row totals the columns.
- Colour shows how **many** conditions are in a cell, not how bad they are: the column already says that. A key shows the range of counts.
- Select a cell to list the conditions in it.

A note explains: "Severity is an estimated visual-impact score, not a clinical grade. It orders the collection; it does not rank anyone's sight."

## The collection

A summary of what is showing: how many conditions, how many categories, the mean severity, and how many are per-colour transforms and field effects. It notes that the 17 per-colour conditions are exactly the 17 the Catalogue calls basic.

**Most severe** lists the top conditions by severity score.

## Actions

| Button | What it does |
| --- | --- |
| **Open a random condition** | Opens a random condition as a panel (`R` does the same) |
| **Export JSON** | Downloads the catalogue as `vd-catalog-<date>.json` |
| **Export CSV** | Downloads severity data as `vd-severity-<date>.csv` (columns listed below) |
| **Keyboard shortcuts** | Shows the lab's keyboard shortcuts (`?` does the same) |

The CSV columns are slug, name, category, complexity, severity_score, description and prevalence.

A footer line says how many conditions are shown and their severity range, for example "17 of 78 shown · severity 3–9".
