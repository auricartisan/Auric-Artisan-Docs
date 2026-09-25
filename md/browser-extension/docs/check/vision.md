---
title: Browser extension — Vision
description: See the live page through eight colour-vision deficiency and four low-vision simulations, compare side by side, and capture the result.
product: Browser extension › Check
updated: 2026-09-25
---

# Vision

Vision (the Vision simulator) filters the live page so you can see it the way people with different vision do. It helps you spot information carried by colour alone, low-contrast areas and layouts that depend on peripheral vision.

## Simulations

| Group | Simulation | What it shows |
|---|---|---|
| Colour blindness | **Protanopia** | No red-sensitive cones |
| | **Deuteranopia** | No green-sensitive cones, the most common form |
| | **Tritanopia** | No blue-sensitive cones, rare |
| | **Achromatopsia** | No colour vision |
| Weaker forms | **Protanomaly** | Weak red sensitivity |
| | **Deuteranomaly** | Weak green sensitivity |
| | **Tritanomaly** | Weak blue sensitivity |
| | **Achromatomaly** | Weak colour vision overall |
| Low vision | **Cataracts** | Blur with a yellowed, washed-out look |
| | **Low vision** | Strong blur with reduced brightness |
| | **Glaucoma** | Tunnel vision: the edges of the view darken |
| | **AMD** | Age-related macular degeneration: loss in the centre of the view |

## Use it

1. Open the page, then Check › **Vision**.
2. Choose a simulation. The page is filtered at once.
3. Drag **Strength** (0 to 100%, 100% by default) to weaken or strengthen the effect. Strength applies to the eight colour-vision simulations; the four low-vision ones have a fixed strength.
4. Choose another simulation to switch, or **Clear** to remove the filter.

The filter stays on while you move around a single-page site. Reloading the page removes it.

## Compare side by side

Choose **Side-by-side**. The page shows the original on the left and the filtered version on the right, labelled "Original / " and the simulation's name. Choose its **✕** to close it. With no simulation chosen, it compares deuteranopia.

## Capture

Choose **Capture** to download a PNG of the visible tab, named after the simulation (for example `aa-vision-deuteranopia-…png`).

## Other ways to start a simulation

- `Alt` + `Shift` + `V` toggles deuteranopia on the current tab.
- The browser's own right-click menu has **Simulate · Protanopia**, **Deuteranopia**, **Tritanopia**, **Achromatopsia** and **Clear vision filter** (while Settings › Right-click › **Items in the browser's menu** is on).
- The custom right-click menu has **Simulate colour vision**, with a preview of how four everyday colours look in each type, and **Side by side** (see [Right-click menu](../on-websites/right-click-menu.md)).

## Limits

Simulations are approximations based on published models. They show the kind of difficulty a person may have, not exactly what any individual sees. See [Limits and accuracy](../../others/limits-and-accuracy.md).

## Related pages

- [Contrast](contrast.md), whose colour-vision check gives ratios for protan, deutan and tritan vision
- [Picker](../colour/picker.md), whose Vision pane previews one colour
