---
title: Industrial Dye Chemistry (Dye in Solution) — Build a bath
description: Add, select, mute and remove dyes, set concentration and path length, and understand absorbance and the Beer–Lambert law.
product: Website › Tools › Perception and spectral › Industrial Dye Chemistry
updated: 2026-09-25
---

# Build a bath

## Absorbance in brief

A dye solution looks coloured because it absorbs some wavelengths of light more than others. **Transmittance** T is the fraction of light at a wavelength that gets through. **Absorbance** A is its negative base-10 logarithm, A = −log₁₀ T: an absorbance of 1 lets 10% through, 2 lets 1% through.

The **Beer–Lambert law** says absorbance is proportional to how much dye the light meets:

A = ε × c × l

- **ε** (epsilon), the **molar absorptivity**, is the dye's own strength at that wavelength, in litres per mole per centimetre (M⁻¹ cm⁻¹).
- **c** is the concentration in moles per litre. The page shows it in micromolar (µM, millionths of a mole per litre).
- **l** is the **path length**, the distance the light travels through the solution, in centimetres.

Absorbances of several dyes, and of the two forms of one dye, simply add. So doubling the concentration or the path length doubles the absorbance at every wavelength.

The law holds well only up to about A = 1. Above that, real solutions fall below the straight line, because dye molecules clump together and spectrophotometers have finite bandwidth. The page flags a bath whose absorbance exceeds 1 anywhere.

## The six preset dyes

Every preset stands for a **class** of dye and says which; none is a named commercial substance, and all their constants are the tool's own. Each has an acid form and a base form, each drawn as a Gaussian band.

| Dye | Stands for | pKa | Default concentration | Acid form: λmax, ε | Base form: λmax, ε |
|---|---|---|---|---|---|
| **Weak-acid indicator** | The methyl-orange family: a large shift, low in the pH range | 3.5 | 34 µM | 508 nm, 26,000 | 462 nm, 22,000 |
| **Mid-range indicator** | The bromothymol-blue family: the widest shift, near neutral | 7.1 | 20 µM | 430 nm, 15,000 | 615 nm, 34,000 |
| **High-range indicator** | The phenolphthalein family: one form barely absorbs | 9.4 | 25 µM | 400 nm, 900 | 553 nm, 31,000 |
| **Azo red, pH-stable** | A textile azo red whose colour does not move over the working range | 12.5 | 50 µM | 505 nm, 30,000 | 512 nm, 29,000 |
| **Anthraquinone blue, pH-stable** | A textile blue with a narrow band and little pH response | 11.8 | 40 µM | 600 nm, 16,000 | 606 nm, 16,500 |
| **Yellow, pH-stable** | A short-wavelength dye for mixing, flat across the range | 12.0 | 60 µM | 428 nm, 21,000 | 431 nm, 21,000 |

**λmax** is the wavelength at which a band absorbs most.

## Add, select, mute and remove components

The list under **The components** shows each dye in the bath as a button with a swatch (that dye alone in the current bath), its name, its pKa, concentration and the two band peaks, and a tag: **Stand-in** for drawn bands or **Measured** after you load a spectrum.

1. Pick a dye in the menu under the list and select **Add**. It joins the bath and becomes the selected dye. A bath holds at most four; a fifth shows **Four components is the ceiling here**.
2. Select a dye's button to make it the selected dye. The spectrum plot and **The selected dye** group switch to it.
3. Select **Mute** to take the selected dye out of the bath without deleting it; its button dims. Select **Mute** again to bring it back.
4. Select **Remove** to delete the selected dye. The bath keeps at least one; removing the last shows **The bath needs at least one dye**.

**Reset the bath** returns to the default single weak-acid indicator at pH 3.50, 1.0 cm and D65, and clears any sweep and measured spectra.

## Set concentration and path length

- **Concentration** (under **The selected dye**, 0.5–200 µM in steps of 0.5) sets the selected dye's concentration.
- **pKa** (0–14 in steps of 0.1) sets the selected dye's pKa; see [Run a titration](run-a-titration.md).
- **Path length** (under **The bath**, 0.1–10 cm in steps of 0.1, default 1.0 cm) applies to the whole bath. A standard spectrophotometer cell is 1 cm.

## Read the absorbance readouts

These describe the whole bath (every component that is not muted):

| Readout | Meaning |
|---|---|
| **Peak absorbance** | The highest absorbance at any of the 81 wavelengths, three decimals |
| **λmax** | The wavelength of that peak |
| **Beer–Lambert holds** | **yes, A 0.63** when the peak is at or below 1; **no — A 1.85 is past 1** when above, highlighted |

With the default dye at pH 3.5, raising **Concentration** above about 54 µM, or **Path length** above about 1.6 cm, pushes the peak past 1.

The spectrum plot is different: it shows the **selected** dye's two forms and their weighted sum as molar absorptivity (the vertical axis is in thousands of M⁻¹ cm⁻¹), not scaled by concentration or path. Use it to see the shape of a dye; use the readouts for the bath.

## Try it

1. Add the **Anthraquinone blue, pH-stable** to the default bath.
2. Watch the swatch move to a muted grey (`#ACA1A6`) as the blue dye absorbs the orange-red light the indicator lets through; the two dyes together absorb across most of the spectrum.
3. Select the blue dye's button and lower its **Concentration** until you like the shade.
4. Select **Mute** on it to compare the bath with and without it.

You should now have a mixture whose colour and absorbance you can adjust dye by dye.
