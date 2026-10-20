---
title: Screen saver — Reading the screen
description: What each part of the screen saver shows, from the colour bands to the readout and clock.
product: Website › Site features › Screen saver
updated: 2026-09-25
---

# Reading the screen

## The colour bands

The whole screen is seven bands of one colour, from its darkest shade to its lightest. On a wide screen the bands run side by side; on a narrow or portrait screen they run top to bottom.

- The bands are steps of **lightness** in OKLCH: 0.22, 0.35, 0.48, 0.61, 0.74, 0.85 and 0.94. Each band shows its step number.
- The fourth band (0.61) is the colour's own step, marked as the sample.
- The darkest step is pure black for every colour.
- Colourfulness tapers towards both ends, because very dark and very light shades cannot hold a strong colour.
- Each step number sits on a small chip that keeps it readable on its band.

**OKLCH** describes a colour by its lightness (L), chroma or colourfulness (C) and hue (H), in a way that follows how people see colour. Stepping lightness in OKLCH gives even-looking shades.

## The readout

| Line | What it shows |
|---|---|
| **Colour atlas** and a number | The colour's number in the site's atlas of 8,192 colours, for example "6,400 / 8,192" |
| Name | The colour's name, for example Crocus Yellow |
| Hex | Its hex code |
| **oklch** | Its lightness, chroma and hue |
| **reads as** | The mood the atlas associates with it, for example calm or playful |
| **movement** | The art movement the atlas associates with it, for example Bauhaus or Art Deco |
| **on black** | Its WCAG contrast ratio against black |

## The rotation

- A new colour appears every twelve seconds, and a thin line shows the time until the next one.
- Each time the screen saver starts, it begins with a different colour.
- It pauses while the tab is hidden and resumes when you come back.

## The foot of the screen

- **Auric Artisan** on one side.
- A clock with the time and date. It uses 24-hour time if you chose **24-hour time** in Settings › Clock.
- **Move to return**, for the first minute.

## What is hidden

While the screen saver shows, the page utilities bar, the navigation dock, the right-edge menu line, the info bars and the clock strip are hidden. The pointer stays, since moving it is how you return.
