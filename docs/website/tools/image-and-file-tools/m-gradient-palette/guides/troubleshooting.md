---
title: M-Gradient Palette — Troubleshooting
description: Symptoms you may meet in the M-Gradient Palette, why they happen, and what to do.
product: Website › Tools › Image and file tools › M-Gradient Palette
updated: 2026-09-25
---

# Troubleshooting the M-Gradient Palette

## Building the ramp

| Symptom | Why | What to do |
|---|---|---|
| **That is not a colour.** and the hex box reverts | The value is not three or six hex digits | Type a value such as `F2B134` or `#abc`; eight-digit hex with alpha is not accepted |
| Some steps have a gold underline | Their chroma was reduced to fit sRGB | Expected with saturated ends in OKLCH. Choose less saturated ends, or accept the boundary colours |
| Neighbouring steps are identical | The **step** easing has only five positions | Choose another easing, or five steps |
| The middle of the ramp is grey or muddy | sRGB and linear RGB pass near grey between very different hues | Use **OKLCH, short hue**; see the **Spaces** tab |
| The ramp passes through unexpected hues | A long hue route, or HSL, goes round the colour wheel | Use a short hue route |
| One bar is much taller than the rest | A visible jump at that step | Try another route or easing; check **largest jump** |
| A preset gave a poor ramp | Presets make no claim to be good ramps | Adjust the ends, route or easing |

## The Spaces tab

| Symptom | Why | What to do |
|---|---|---|
| No row is marked the evenest | Two or more rows tie | Choose any of the tied rows |
| Choosing a row does nothing | The table is a comparison, not a control | Select that route and easing on the **Ramp** tab |

## Contrast

| Symptom | Why | What to do |
|---|---|---|
| APCA Lc is negative | The text is lighter than the step | Expected: the sign shows polarity; the **Good for** column uses the size |
| WCAG passes but APCA says **not for text**, or the reverse | The two measure different things | Treat both as evidence; choose steps that satisfy the standard you work to |
| The simulation changed the colours but not the contrast figures | Figures always use the true colours | Expected |

## Exports

| Symptom | Why | What to do |
|---|---|---|
| The CSS gradient looks different from the ramp | It carries only the two ends and the space, not steps or easing | Use the custom properties for exact steps |
| The CSS gradient looks like an sRGB blend in one browser | That browser does not support interpolation in a named space | Use the custom properties, or an SVG |
| The SVG's middle differs from the ramp | Between stops, the program showing the SVG blends in its own space | Add more steps so the stops are closer |
| **The browser refused the clipboard.** | Clipboard access was blocked | Allow clipboard access for the site, or use **Save the SVG** and **Save the reading** |
| **This browser will not take text from the clipboard.** | The browser cannot copy text | Use a current browser, or the save buttons |
| Pasted custom properties have no effect | They were pasted outside a CSS rule | Put them inside a rule such as `:root { … }` |

For help with the site in general, see [Help](../../../../../help/README.md).
