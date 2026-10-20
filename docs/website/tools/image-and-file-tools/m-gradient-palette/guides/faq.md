---
title: M-Gradient Palette — FAQ
description: Short answers to common questions about the M-Gradient Palette.
product: Website › Tools › Image and file tools › M-Gradient Palette
updated: 2026-09-25
---

# M-Gradient Palette FAQ

## Which route should I use?

For even-looking steps, start with **OKLCH, short hue**, and confirm on the **Spaces** tab, which measures all six routes and five easings for your two colours.

## Why are there four spaces but six routes?

OKLCH and HSL have a hue angle, and each can go the short or the long way round the colour wheel. That is two routes in the same space, not two spaces.

## What does "evenness" mean?

The standard deviation of the colour differences between neighbouring steps. Lower means the steps look more equally spaced. It is a ranking, not a pass mark: the tool marks the evenest of the thirty combinations but sets no threshold for "even enough".

## Why did some steps get a gold underline?

Blending in OKLCH asked for a colour more colourful than sRGB can show. The tool reduced its chroma, keeping its lightness and hue, until it fitted.

## Can I have more than two colours in a ramp?

No. A ramp runs between two ends. For a multi-stop scale, build one ramp per section, or join exported steps yourself.

## Can I have more than 32 steps?

No. The **Steps** slider runs from 2 to 32.

## Is the CSS gradient the same as the steps?

No. The CSS gradient asks the browser to blend smoothly between the two ends in the chosen space. The custom properties and the hex list are the exact steps the tool measured.

## Why does the tool show two contrast figures?

WCAG 2.2 and APCA measure contrast differently and often disagree. Both are shown so you can see the disagreement.

## Why is the APCA figure negative?

APCA is signed. Negative means light text on a darker background; positive means dark text on a lighter background.

## Does the colour-vision view change the exports?

No. It changes only what is drawn on screen. All figures and exports use the true colours.

## Does it simulate mild colour blindness?

No. It simulates full protanopia, deuteranopia and tritanopia only.

## Is anything saved between visits?

No. The ramp and settings are not stored. Save the reading or copy the custom properties to keep them.
