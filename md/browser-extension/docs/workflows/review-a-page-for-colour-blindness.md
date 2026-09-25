---
title: Browser extension — Review a page for colour blindness
description: Check that a page does not rely on colour alone, using the vision simulations, side-by-side comparison and the contrast checker.
product: Browser extension › Workflows
updated: 2026-09-25
---

# Review a page for colour blindness

WCAG asks that colour is never the only way information is shown. This workflow helps you find places where it is: error states shown only in red, charts told apart only by hue, links distinguished only by colour.

## 1. Look through the common types

1. Open the page, then Check › **Vision**.
2. Choose **Deuteranopia**, the most common type. Look at status colours, charts, badges, links and form errors.
3. Repeat with **Protanopia**, **Tritanopia** and **Achromatopsia**.
4. Ask of each coloured element: can I still tell what it means?

`Alt` + `Shift` + `V` toggles deuteranopia at any time, which is handy while you scroll.

## 2. Compare side by side

1. Choose **Side-by-side**. The left half stays as it is and the right half is filtered.
2. Compare the two halves at the same place on the page.
3. Choose **✕** to close it.

## 3. Try the milder forms and low vision

1. Choose the **Weaker forms** (protanomaly, deuteranomaly, tritanomaly, achromatomaly). Use **Strength** to see how the effect grows.
2. Choose **Low vision**, **Cataracts**, **Glaucoma** and **AMD** to check that important content is not only at the edges or only in fine detail.

## 4. Record what you see

Choose **Capture** to download a PNG of the filtered tab for a report or a ticket.

## 5. Check the numbers

1. For a colour pair you are unsure of, open Contrast and set the two colours.
2. Read the **Colour-vision check**: the ratio for protan, deutan and tritan vision.
3. Run the **Audit** too: its `link-distinguishable` rule catches links in text that are identified by colour alone.

## 6. Clear the filter

Choose **Clear**, or press `Alt` + `Shift` + `V` again. Reloading the page also clears it.

**The result:** a list of places where colour carries meaning on its own, ready to fix with text, icons, patterns or stronger contrast.

## Related pages

- [Vision](../check/vision.md)
- [Contrast](../check/contrast.md)
- [Limits and accuracy](../../others/limits-and-accuracy.md)
