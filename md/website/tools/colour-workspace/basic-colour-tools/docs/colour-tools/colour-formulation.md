---
title: Color Formulation — How a colour is built, and how to mix it
description: Read one colour as channels, follow it through the conversion pipeline with its real numbers, see an illustrative reflectance curve, and find the two artist pigments, in which ratio, that mix closest to it.
product: Website › Tools › Colour workspace
updated: 2026-09-27
---

# Color Formulation

Color Formulation takes one colour apart. It shows the numbers a screen stores for the colour and how much light each channel gives, follows the colour step by step from its hex code to OKLCH and back with every number filled in, draws an illustrative curve of the light a surface of that colour might reflect, and finds which two of thirteen artist pigments, mixed in which ratio, come closest to it.

Use it to understand a colour rather than only copy its code: to learn how sRGB, linear light and OKLab relate, to see why a colour looks the way it does, or to get a starting recipe for mixing a physical paint that matches a screen colour. The reflectance curve and the paint mix are models, not measurements, and the tool labels them so.

Color Formulation is in the launcher's **Deep dive** group. It opens in a floating panel over the page you are on; for moving, docking and closing panels, see [Open the Colour Tools and work in their panels](launcher-and-panels.md).

## How to open it

- **Launcher:** press `Ctrl` + `Shift` + `C` (or right-click the page and choose **Colour tools** › **All colour tools…**), then select **Color Formulation**.
- **From another Colour Tool:** it is in the **Open in another tool** menu of CMYK Soft-Proof and Color Space Converter, and in the Color Inspector's **Open in another tool** list as **Formulation**.
- **A link:** add `?ctool=formulation` to any page address, with the keys under [Links](#links).

Opened from the launcher or the [Colour Tools dashboard](colour-tools-dashboard.md), it takes the [working colour](launcher-and-panels.md#the-working-colour). With no colour at all, it starts on `#D3AF37`.

## Screen tour

This is a narrow tool: the colour fills the top of the panel, four tabs sit below it, and a row of actions runs along the bottom. [Open the Colour Tools and work in their panels](launcher-and-panels.md) describes the parts every tool shares, including the title bar, **Open in another tool**, **Dock** and the bottom sheet on phones.

### The header

- **Two tags** describe the colour: its tone, **Light tint** (OKLCH lightness above 72%), **Mid tone** or **Deep shade** (below 35%); and its chroma, **Vivid chroma** (above 0.20), **Moderate chroma** (above 0.09) or **Muted, near neutral**.
- **The name**, a plain-language description such as "Light soft amber".
- **The hex and OKLCH value**, for example "#D3AF37 · oklch(0.766 0.138 91.6)".
- **The colour field**, with a picker button that takes a colour from anywhere on your screen (only in browsers that support it) and a dice button that tries a random colour.

The field accepts a hex code (with or without `#`), a CSS colour name or a CSS colour function. The tool follows as you type whenever the text is a complete colour; press `Enter` to also accept a fragment of a hex code. If you press `Enter` on something that is not a colour, the field is outlined in red and a message says "That isn't a colour yet".

On every tab except **Channels**, the header folds to a strip with the name and hex so the tab has room.

## Channels

**Channels** is the tab that opens first.

- **The verdict.** Two sentences:
  - which channels lead, for example "Red and green lead (211, 175) with little blue (55): that mix of light is what reads as light soft amber.";
  - where the colour's luminance comes from, for example "Luminance Y 0.448 comes 68% from green, 31% from red and 1% from blue, because the eye weighs green light most."
- **Properties · tap to copy.** Six tiles: **OKLCH L** (as a percentage), **Chroma**, **Hue angle** ("none" for a neutral), **HSL sat.**, **Luminance** (WCAG relative luminance, 0 to 1) and **LRV** (light reflectance value, 0 to 100). Select a tile to copy its value.
- **Where luminance comes from.** A bar split into the red, green and blue shares of the luminance, with the total Y.
- **Five groups of bars**, each value at the end of its bar:

| Group | Bars | What it is |
|---|---|---|
| **sRGB · encoded, 0–255** | **Red**, **Green**, **Blue** | What the file stores. |
| **Linear light · 0–1** | **Red**, **Green**, **Blue** | What the screen emits. |
| **HSL** | **Hue**, **Saturation**, **Lightness** | Device hue, not perceptual. |
| **OKLab** | **L**, **a · red–green**, **b · yellow–blue** | Perceptual, with signed axes. |
| **OKLCH** | **L**, **Chroma**, **Hue** | OKLab in polar form. |

The OKLab **a** and **b** bars grow from a centre line: red or green along a, yellow or blue along b. The **Chroma** bar is drawn against 0.37, about the most any display gamut reaches.

## Pipeline

**Pipeline** follows the colour through six steps, with the numbers for this colour at every step.

- **The verdict** says the round trip returns the same hex, or a different one, and gives the largest error before rounding. The second sentence names the biggest change, which is usually decoding to linear light, and gives the OKLCH values you would edit.
- **The six steps.** Each has its name and space, its three values, the formula or intermediate numbers used, and a short note.

| Step | What it shows |
|---|---|
| **1 · Encoded sRGB** | The three whole numbers in the hex code as fractions of 255. Still gamma-compressed. |
| **2 · Linear light** | The same colour after the sRGB transfer curve is removed, proportional to the amount of light. The note names the channel that falls furthest. |
| **3 · CIE XYZ · D65** | Tristimulus values under the D65 white, with the chromaticity x and y. Y is the relative luminance that WCAG contrast is built on. |
| **4 · OKLab** | L, a and b, with the cone-like LMS values and their cube roots on the way. |
| **5 · OKLCH** | L, chroma and hue, with the formulas for C and h. For a neutral, the note says the hue carries no meaning. |
| **6 · Back to sRGB** | Every step inverted and encoded again, with the round-trip error and the ΔE2000 between the start and the end. |

- **The round trip.** A split swatch of the colour before and after, "#D3AF37 → #D3AF37", the largest error and the ΔE2000, and **Exact** or **Drifts**.

## Spectrum

**Spectrum** draws an illustrative reflectance curve: roughly which light, from 380 to 780 nm, a surface of this colour might send back.

- **The verdict** says where the curve is highest and lowest, for example "A surface of this colour would reflect most from 580 nm upward (yellow through red), about 55%, and least in the violet band, 26%. Taking away violet light is what leaves it looking light soft amber." A note gives the wavelength the hue maps to and repeats "Illustrative — not a measurement; a spectrophotometer gives the real curve."
- **Reflectance · 380–780 nm.** The curve, filled with the colour itself, with a label at its peak and a strip under it showing the approximate colour of each wavelength. The tag **Illustrative — not a measurement** sits beside the heading.
- **Hue to wavelength.** Four facts: **OKLCH hue**, **Mapped peak**, **Lobe width** and **Floor** (the lowest reflectance).
- **Peak reflectance · by band.** The mean reflectance in six bands, **Violet** (380–450 nm), **Blue** (450–495 nm), **Green** (495–570 nm), **Yellow** (570–590 nm), **Orange** (590–620 nm) and **Red** (620–780 nm), with the highest marked **Most** and the lowest **Least**.

How the curve is drawn:

- The hue is mapped to a wavelength: blues peak near 450 to 470 nm, greens near 520 to 550 nm and reds above 600 nm. Yellows through reds keep reflecting on the long side of the peak.
- Purples and magentas have no single wavelength, so their curve has two lobes, violet near 440 nm and red from 620 nm, and dips through the green.
- A neutral is drawn nearly flat, at about its luminance: it reflects every wavelength about equally, which is why it has no hue.
- The more chroma, the narrower and taller the lobe; the lighter the colour, the higher the floor.

## Paint mix

**Paint mix** finds the two pigments, from thirteen, that mix closest to your colour.

- **The verdict.** The closest pair and ratio, for example "Closest two-pigment mix from the 13 pigments: Cadmium Yellow with Yellow Ochre at 35 / 65, ΔE 2.6 — close." When no pair gets within ΔE 10, it says the colour sits outside what these pigments mix in twos. The second sentence gives the range of lightness the pair covers, from 95 / 5 to 5 / 95, against your colour's.
- **Must include.** **Any pigment · all 78 pairs**, or one pigment to find the best mix that uses it.
- **The recipe card.**
  - Its heading: **Best two-pigment mix**, **Best mix with** a pigment, or **Alternative** and a number, with **Back to the best mix** when you are looking at an alternative.
  - A split swatch of your colour and the mix, the ΔE with a reading, the two hex codes, and the mix's OKLCH lightness against yours.
  - The recipe in parts, for example "Mix 7 parts Cadmium Yellow with 13 parts Yellow Ochre (35 / 65 by volume)."
  - Each pigment with its colour, hex and share, and a bar split in proportion.
  - **Share of** the first pigment: a slider from 5 to 95 in steps of 5. When you move away from the best ratio, a note gives the best ratio and its ΔE, with a button to go back to it, for example **Use 35 / 65**.
- **Ratio sweep · 19 mixes.** Nineteen swatches from 95 / 5 to 5 / 95, with the best ratio underlined. Select one to use that ratio.
- **Six alternatives · tap to show one.** The next six pairs, each with a swatch of the mix beside your colour, the two pigments, the ratio, the ΔE and its reading. Select one to show it in the recipe card.

ΔE readings are the same as in every Colour Tool: **Imperceptible** (under 1), **Very close** (1 to 2), **Close match** (2 to 5), **Noticeable** (5 to 10) and **Distinct** (10 and above).

### The pigments

| Pigment | Colour used | Pigment | Colour used |
|---|---|---|---|
| Cadmium Red Light | `#E63A2E` | Phthalo Blue | `#0B3D7A` |
| Alizarin Crimson | `#A0182E` | Phthalo Green | `#0E7A4A` |
| Cadmium Yellow | `#FFD500` | Sap Green | `#3F6E2A` |
| Yellow Ochre | `#C5A050` | Dioxazine Purple | `#3B1B5C` |
| Burnt Sienna | `#8B3A1F` | Titanium White | `#FAF8F2` |
| Raw Umber | `#7B4F2E` | Mars Black | `#1A1A1A` |
| Ultramarine Blue | `#1E3A8A` | | |

The model tries every pair of two different pigments (78 pairs) at 19 ratios, from 95 / 5 to 5 / 95 in steps of 5, and ranks them by ΔE2000 from your colour. It mixes them with single-constant Kubelka–Munk, a standard model for how paints absorb and scatter light, applied to each linear-light channel, so the ratio really does move the lightness of the mix.

## Walkthroughs

### See how a colour is encoded

1. Type `D3AF37` into the field.
2. On **Channels**, compare **sRGB · encoded, 0–255** (211, 175, 55) with **Linear light · 0–1** (0.6514, 0.4287, 0.0382). Blue drops from about a fifth of its range to under 4%: decoding pulls dark values down hardest.
3. Open **Pipeline** and read the six steps. The round trip returns `#D3AF37` exactly.

### Find a paint mix

1. Enter the colour you want to mix, for example `#D3AF37`, and open **Paint mix**.
2. Read the recipe: "Mix 7 parts Cadmium Yellow with 13 parts Yellow Ochre (35 / 65 by volume)", which the model puts at `#CFAC11`, ΔE 2.6.
3. If you do not have one of the pigments, look through **Six alternatives**, or choose a pigment you do have under **Must include**. With **Titanium White**, the best mix is Yellow Ochre with Titanium White at 70 / 30, ΔE 5.3.
4. Select **Copy recipe** to take the recipe with you.

> **Tip:** Treat the recipe as a direction to start mixing in, then adjust by eye under the light where the work will be seen.

## Controls

| Control | What it does | Values or range | Default |
|---|---|---|---|
| Colour field | Sets the colour. | Hex, CSS names, CSS colour functions; fragments on `Enter` | The colour you opened with, or `#D3AF37` |
| Picker button | Picks a colour from your screen. | Supported browsers only | — |
| Dice button | Tries a random colour. | — | — |
| Property tiles | Copy one value each. | 6 tiles | — |
| **Must include** | Limits the mixes to pairs with one pigment. | Any, or 13 pigments | **Any pigment · all 78 pairs** |
| **Share of** … | Sets the ratio of the pair shown. | 5 to 95, steps of 5 | The best ratio |
| Ratio sweep swatches | Set the ratio. | 19 ratios | — |
| **Use** … | Returns to the best ratio for this pair. | — | — |
| Alternatives | Show another pair. | 6 alternatives | — |
| **Back to the best mix** | Returns to the best pair and ratio. | — | — |
| Tabs | Switch the view. | **Channels**, **Pipeline**, **Spectrum**, **Paint mix** | **Channels** |

## Outputs and exports

The footer holds **Copy recipe**, **Share link**, **Save** and **Export**. On a narrow panel or a phone, the last three show as icons.

| Output | Format | What it contains |
|---|---|---|
| **Copy recipe** / **Recipe text** | Text | The target, the recipe in parts, the resulting hex, the ΔE2000 and its reading, and a note on the model. For example: "Target #D3AF37: Mix 7 parts Cadmium Yellow with 13 parts Yellow Ochre (35 / 65 by volume). Result #CFAC11, ΔE2000 2.61 (close). Model: single-constant Kubelka–Munk in linear sRGB; pigment hexes stand in for reflectance." |
| **JSON** | JSON | The target and its OKLCH values; the mix shown (pigments, hexes, shares, result, ΔE2000 and model); the six alternatives; the pipeline values (encoded, linear, XYZ, OKLab, OKLCH, round trip and error); and the spectrum, marked `illustrative: true`, with the mapped peak and the band means. |
| **Pipeline values** | Text | One line per step, for example "2. Linear light: R 0.6514, G 0.4287, B 0.0382". |
| **Mix hex** | Text | The hex of the mix shown. |
| **Share link** | A URL | This page with `?ctool=formulation`, the colour, any **Must include** pigment, alternative and ratio, and the tab you are on. |
| **Save** | A colour in your Library | Named with the description and hex, for example "Light soft amber #D3AF37", with the recipe as its description and the mix's pigments, shares, result and ΔE2000. |

The recipe, JSON and mix hex follow what the **Paint mix** tab shows, including a pigment you chose, an alternative or a ratio you set.

The **Open in another tool** menu offers **Color Space Converter** (all 34 spaces), **CMYK Soft-Proof** (how the colour shifts in print), **Pantone & Named Lookup** (the nearest Pantone and RAL chips), **Color Inspector** and **Harmony Studio**, all with your colour.

## Links

| Key | What it sets | Values |
|---|---|---|
| `ctool` | Opens this tool. | `formulation` |
| `color` | The colour. | A hex code without `#` |
| `with` | The **Must include** pigment. | The pigment's name in lower case with hyphens, for example `titanium-white`, `yellow-ochre`, `ultramarine-blue` |
| `alt` | An alternative to show. | 1 to 6 |
| `ratio` | The share of the first pigment. | 5 to 95, in steps of 5 |
| `ctab` | The tab to open on. | `channels`, `pipeline`, `spectrum`, `mix` |

For example, `?ctool=formulation&color=D3AF37&with=titanium-white&ctab=mix` opens the paint mix for `#D3AF37` limited to mixes with Titanium White.

## Accuracy and limits

- **The conversions are standard.** sRGB to linear light uses the sRGB transfer curve, XYZ uses the D65 white, and OKLab and OKLCH follow Björn Ottosson's published definition. The numbers match other colour tools, within rounding.
- **The paint mix is a model, not a paint lab.** Each pigment's hex stands in for its reflectance. The model does not know a pigment's tinting strength, opacity, binder or ground, all of which change real results. Use the recipe as a starting point and mix by eye.
- **ΔE** is the CIEDE2000 difference between your colour and the modelled mix. Below about 2, most people see no difference side by side; above 5 the difference is clear.
- **The spectrum is illustrative, not a measurement.** It is drawn from the colour's hue, chroma and lightness to explain why the colour looks as it does. Do not use the curve or the band table as spectral data; measure a real surface with a spectrophotometer.
- **Surfaces can match on screen and differ in light.** Two paints that look the same under one light can separate under another (metamerism). No screen tool can predict that without real spectral data.

## Related

- [Colour Tools documentation](README.md)
- [Open the Colour Tools and work in their panels](launcher-and-panels.md)
- [Colour Tools dashboard](colour-tools-dashboard.md)
- [Color Space Converter](colour-space-converter.md) — the same colour in 34 notations, with its gamut
- [Color Inspector](colour-inspector.md)
- [CMYK Soft-Proof](cmyk-soft-proof.md) — how the colour might print
- [Perception and spectral tools](../../../../perception-and-spectral/README.md) — tools that work with real spectra, dyes and materials
- [Library Kit](../../../../../kits/library-kit/README.md) — where saved colours go
