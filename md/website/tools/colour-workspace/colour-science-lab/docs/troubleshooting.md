---
title: Color Science Lab — Troubleshooting
description: Symptoms you may meet in the Color Science Lab, why they happen, and what to do.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Troubleshooting the Color Science Lab

### Typing a HEX code on the Workbench does nothing

- **Why:** the Workbench, Compare and the gamut tools accept a full `#RRGGBB` code, with the `#`.
- **What to do:** type all six digits with the `#`, or use the colour well or a preset.

### A panel did not open

- **Why:** five panels are open and all are pinned.
- **What to do:** unpin or close one, then open the tool again.

### A panel closed by itself when I opened another tool

- **Why:** at five panels, opening another closes the oldest unpinned panel.
- **What to do:** pin panels you want to keep.

### A panel closed when I pressed Escape

- **Why:** `Escape` inside a panel closes it (or restores it first if it is maximised).
- **What to do:** select outside the panel before pressing `Escape` for other reasons.

### Pressing a letter changed the Catalogue or tiled my panels

- **Why:** single-letter shortcuts (`/`, `?`, `F`, `A`, `C`, `R`, `T`, `1` to `5`) work anywhere on the page when the cursor is not in a text box.
- **What to do:** click into a text box before typing, or see [Shortcuts](../others/shortcuts.md).

### Linked panels do not follow each other

- **Why:** only panels whose link button is on share changes.
- **What to do:** turn on linking in each panel, or use **Sync all**.

### The search seems slow to respond

- **Why:** the search waits a moment after you stop typing.
- **What to do:** pause briefly after typing.

### The Workbench and a panel give different Lab values for the same colour

- **Why:** the Workbench uses the illuminant and observer you selected with a chosen adaptation; a panel reports Lab against its source or target white.
- **What to do:** set the same white on both (for example D65 on the Workbench and D65 as the panel's source white).

### A canvas looks blurry or too small after resizing

- **Why:** the canvases redraw at the panel's size.
- **What to do:** resize or maximise the panel once more to redraw.

### The exported image is missing a panel's latest state

- **Why:** the export uses each panel's experiment canvas as last drawn; minimised panels are not redrawn.
- **What to do:** restore all panels and let them redraw before exporting.

### A restored Library preset shows old values at first

- **Why:** saved controls are applied just after the panel draws.
- **What to do:** wait a moment; if values still look wrong, check that the preset was saved from a focused panel.

### Everything disappeared after a reload

- **Why:** panels are not saved across reloads.
- **What to do:** save important panels to your Library, or export an image.

## Related

- [FAQ](faq.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
- [Help centre](../../../../../help/README.md)
