---
title: Ishihara Plate Generator — Troubleshooting
description: Common problems with the Ishihara Plate Generator, why they happen, and what to do.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Troubleshooting the Ishihara Plate Generator

### My plates disappeared

- **Why:** plates are kept only while the page is open. Reloading or leaving the page loses them.
- **What to do:** export plates you want to keep, or download the seeds file so you can rebuild them.

### I can see the figure clearly under Protan, Deutan or Tritan

- **Why:** the plate's colours still differ for that deficiency. Palettes and difficulty decide how well a figure hides.
- **What to do:** check **Concealment** in **Diagnostics**, choose a palette that targets that deficiency, raise the difficulty, or regenerate.

### I cannot see the figure even with normal preview

- **Why:** at **Hard** and **Extreme** the figure's colours are very close to the background's, and your screen, brightness and room light all affect what you see.
- **What to do:** lower the difficulty, raise **Color separation** in **Fine tuning**, or check the plate's **Separation** in **Diagnostics**.

### A plate is marked Review instead of Pass

- **Why:** its quality score is under 45, or its density, figure share or separation is out of range.
- **What to do:** see [Read the diagnostics](read-the-diagnostics.md) and regenerate with adjusted settings.

### "No plates to export"

- **Why:** the bench is empty.
- **What to do:** generate plates first. **Set 38** plates are shown in their own tab and are not on the bench.

### "ZIP library unavailable — downloading first plate as PNG"

- **Why:** the ZIP builder could not load, often because of a network problem or a content blocker.
- **What to do:** reload and try again, or download plates one at a time from their cards.

### Download every .svg saved only one file, or asked for permission

- **Why:** browsers limit or ask before a page saves several files in a row.
- **What to do:** allow multiple downloads for auricartisan.com, or use **Export every plate** for a single ZIP.

### "Copy failed"

- **Why:** the browser refused clipboard access.
- **What to do:** read the seed from the card, or download the seeds file.

### A rebuilt plate does not match the original

- **Why:** the seed only reproduces a plate with exactly the same type, content, palette, difficulty and fine-tuning settings.
- **What to do:** check every setting against the seeds file or the plate's JSON in the export ZIP.

### Colour space shows sRGB, not P3 HDR

- **Why:** your display or browser does not report wide-gamut support.
- **What to do:** nothing; plates are still generated and scored the same way.
