---
title: Material Lighting (Material Under Light) — Compare with the reference light
description: Read the measured colour temperature and its error band, understand how the reference light is chosen, and interpret the colour difference between a material under its source and under that reference.
product: Website › Tools › Perception and spectral › Material Lighting
updated: 2026-09-25
---

# Compare with the reference light

## Colour temperature

The **correlated colour temperature** (CCT) of a light is the temperature of the blackbody whose colour is closest to it, in kelvin. Low values (2700 K) are warm and orange; high values (6500 K and above) are cool and bluish.

**Measured temperature** gives the CCT the page computes back from the illuminant spectrum you chose, using McCamy's formula, rounded to 10 K, with its error band. The error bands were measured against blackbodies of known temperature:

| Temperature | Worst measured error |
|---|---|
| 1800–2500 K | ±18 K |
| 2500–4000 K | ±13 K |
| 4000–7000 K | ±11 K |
| 7000–10000 K | ±139 K |
| 10000–15000 K | ±1069 K |

Above 7000 K the readout is highlighted and adds **McCamy's fit is out of its range up here**. The reference chosen is a daylight either way.

## The reference rule

To judge how a light renders colours, the CIE compares it with a reference light of the same CCT (CIE 13.3, section 5.1):

- below 5000 K, a **blackbody** at that temperature;
- at or above 5000 K, a **CIE daylight** at that temperature.

**Reference for it** shows the choice (for example **daylight 6500 K** or **blackbody 2860 K**), and the note above the swatches gives the reason, for example **below 5000 K the reference is a Planckian radiator**. A light that is its own reference, such as D65 or a blackbody, compares with itself.

## The colour difference

**Against the reference the standard names** shows the material twice: **Under your source** (captioned with your illuminant) and **Under its reference** (captioned **D** or **BB** and the temperature). Between them is **ΔE₀₀**, the CIEDE2000 colour difference.

Each colour is taken against its own light's white, so what remains is how the **material** moved, not the fact that the two lights differ. That is why a source that is its own reference reads about zero: D65 about 0.01, a 2700 K blackbody about 0.002, illuminant A about 0.05. The small remainders come from the error in measuring the temperature.

Some examples with the preset materials and default surface:

| Scene | Reference | ΔE₀₀ |
|---|---|---|
| Gold under D65 | Daylight 6500 K | About 0.01 |
| Gold under E | Daylight 5460 K | About 2.0 |
| Gold under a 10000 K blackbody | Daylight 9860 K | About 3.1 |
| Skin under 4000 K daylight | Blackbody 4010 K | About 1.6 |
| Leaf under illuminant A | Blackbody 2860 K | About 0.05 |

This is a colour difference for **this one material**. It is not a rendering index and does not characterise the lamp: a rendering index needs a specified set of many measured samples, which the tool does not hold. The line under the swatches says so, and adds, for a synthesised material, that the difference is a property of the model rather than of a real pigment.

## Two white points

The page uses two white points on purpose, and the **Method** tab's **Two white points** view explains them:

| Readout | White point | Question it answers |
|---|---|---|
| The swatch and its hex | None: un-adapted | What does this material look like under this light? |
| L\*, a\*, b\* and every ΔE | The illuminant's own | How far did the material move? |

## Metamerism

Two materials with different reflectance spectra can produce the same colour under one light and different colours under another. This is **metamerism**, and it is why a spectral tool is needed to predict it: RGB values alone cannot tell you whether a match will hold. The tool shows one material at a time; to explore metamerism, note a material's L\*a\*b\* under two lights, then compare with another material (for example a measured file) under the same two lights.

## The Method tab's reference view

**Method** › **Choosing the reference** shows the rule as a table of D65, D50, illuminant A and a 2700 K blackbody against the reference each should get, the published and computed chromaticities of D50, D55, D65 and D75, and the colour-temperature error bands.

You should now be able to say how far a material's colour moves between a light and its reference, and what that number does and does not mean.
