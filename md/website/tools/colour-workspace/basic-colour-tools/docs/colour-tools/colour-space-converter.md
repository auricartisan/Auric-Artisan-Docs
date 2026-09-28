---
title: Color Space Converter — One colour in 34 notations
description: Write one colour in 34 notations across eight groups, each marked CSS or notation, see it on the CIE 1931 diagram with its gamut membership and chroma headroom in P3 and Rec.2020, and export every value as JSON, CSS or Markdown.
product: Website › Tools › Colour workspace
updated: 2026-09-27
---

# Color Space Converter

Color Space Converter writes one colour in every notation you are likely to meet: 34 of them, from HEX and HSL through CIELAB, OKLCH, Display P3 and Rec.2020 to video and colour-science spaces. Each row says whether it is **CSS** you can paste into a stylesheet as it is, or a **Notation** for design tools, video and colour science, and each row copies exactly the text it shows. A second tab places the colour on the CIE 1931 chromaticity diagram and shows how much more chroma the wider P3 and Rec.2020 gamuts would allow at its lightness and hue.

A **colour space** is a system of numbers that describes colours. Different spaces suit different jobs: HEX and RGB for screens and code, CMYK for print, Lab and OKLab for measuring how different colours look, P3 and Rec.2020 for wide-gamut screens, YCbCr for video. A **gamut** is the range of colours a space or device can represent.

Color Space Converter is in the launcher's **Deep dive** group. It opens in a floating panel over the page you are on; for moving, docking and closing panels, see [Open the Colour Tools and work in their panels](launcher-and-panels.md).

## How to open it

- **Launcher:** press `Ctrl` + `Shift` + `C` (or right-click the page and choose **Colour tools** › **All colour tools…**), then select **Color Space Converter**.
- **Right-click menu:** **Colour tools** › **Color Space Converter**.
- **From another Colour Tool:** it is in the **Open in another tool** menu of CMYK Soft-Proof and Color Formulation, and in the Color Inspector's **Open in another tool** list as **Space Converter**.
- **A link:** add `?ctool=spaces` to any page address, with the keys under [Links](#links).

Opened from the launcher or the [Colour Tools dashboard](colour-tools-dashboard.md), it takes the [working colour](launcher-and-panels.md#the-working-colour). With no colour at all, it starts on `#D3AF37`.

## Screen tour

This is a narrow tool: the colour fills the top of the panel, three tabs sit below it, and a row of actions runs along the bottom. [Open the Colour Tools and work in their panels](launcher-and-panels.md) describes the parts every tool shares, including the title bar, **Open in another tool**, **Dock** and the bottom sheet on phones.

### The header

- **Two tags:** **34 spaces** and **18 paste as CSS**.
- **The name**, a plain-language description such as "Light soft amber".
- **The hex and OKLCH value**, for example "#D3AF37 · oklch(0.766 0.138 91.6)".
- **The colour field**, with a picker button that takes a colour from anywhere on your screen (only in browsers that support it) and a dice button that tries a random colour.

The field accepts a hex code (with or without `#`), a CSS colour name or a CSS colour function. The tool follows as you type whenever the text is a complete colour; press `Enter` to also accept a fragment of a hex code. If you press `Enter` on something that is not a colour, the field is outlined in red and a message says "That isn't a colour yet".

On **Gamut** and **Channels**, the header folds to a strip with the name and hex so the tab has room.

## Spaces

**Spaces** is the tab that opens first.

- **The verdict.** "34 ways to write #D3AF37: 18 are CSS you can paste, 16 are notations for design tools, video and colour science. Each row copies exactly what it shows." A note explains that CSS `lab()` and `lch()` are D50, so the D65 Lab and LCh rows sit beside them as notation, and says whether the colour fits inside every wide gamut listed.
- **Search 34 spaces.** A search box with the hint "lab, p3, video, css…". It matches a row's name, value, group, kind and note. A **×** clears it.
- **All · 34**, **CSS · 18**, **Notation · 16.** Show every row, or only one kind.
- **A count**, for example "34 spaces · 18 CSS · 16 notation", or "1 of 34 shown for “p3” · css only" while you filter.
- **Eight groups of rows.** Each row shows its name, its value, a note where one helps, a **CSS** badge or **Notation** tag, and **Copy**. Select a row to copy exactly the value shown.

When nothing matches, the tab says so and suggests trying lab, p3, video or css.

### The 34 notations

| Group | Rows (kind) |
|---|---|
| **Web** (6) | **HEX**, **HEX · short**, **RGB**, **RGBA · legacy**, **RGB %**, **Linear sRGB** (all CSS) |
| **Cylindrical** (4) | **HSL** (CSS), **HSV / HSB** (notation), **HWB** (CSS), **HSI** (notation) |
| **CIE** (6) | **XYZ · D65**, **XYZ · D50**, **Lab · D50**, **LCH · D50** (CSS); **Lab · D65**, **LCh · D65** (notation) |
| **Perceptual** (4) | **OKLab**, **OKLCH** (CSS); **CIELuv · D65**, **LChuv · D65** (notation) |
| **Wide gamut** (7) | **Display P3**, **Adobe RGB**, **Rec.2020** (CSS `color()` values); **Linear P3**, **Linear Adobe RGB**, **Linear Rec.2020**, **ACEScg · AP1** (notation) |
| **Print** (1) | **CMYK · naive** (CSS `device-cmyk()`) |
| **Video** (3) | **YCbCr · BT.709**, **YUV · BT.601**, **YIQ · NTSC** (notation) |
| **Scientific** (3) | **Hunter Lab · D65**, **IPT**, **JzAzBz** (notation) |

Notes on some rows:

- **HEX · short** shows the 3-digit form when the colour has one; otherwise it repeats the full hex and says there is no 3-digit form.
- **RGBA · legacy** uses the comma syntax, still valid CSS.
- **Linear sRGB** is light before gamma encoding, the start of every conversion below it.
- **XYZ · D50** is adapted from D65 with the Bradford method, as CSS does.
- **Lab · D50** and **LCH · D50** are what CSS `lab()` and `lch()` mean. The **Lab · D65** and **LCh · D65** rows are written as notation because, pasted into `lab()`, they would be read as D50.
- **Display P3**, **Adobe RGB** and **Rec.2020** each say whether the colour is inside that gamut: every unclamped value within 0 to 1.
- **ACEScg · AP1** is linear, on the ACES white, adapted from D65.
- **CMYK · naive** uses CSS Color 5 syntax, with no profile, and browsers do not render it yet.
- **YCbCr · BT.709** is full range 0 to 1, and the note gives the 8-bit studio-range values too.
- **IPT** follows Ebner and Fairchild (1998) on D65; **JzAzBz** follows Safdar (2017) with its pre-adaptation, for an SDR white of 203 cd/m².

## Gamut

- **The verdict.** Whether the colour fits every larger gamut, for example "#D3AF37 is an sRGB colour, so it sits inside every larger gamut: Display P3, Adobe RGB, Rec.2020 and ACEScg." Then how much chroma each gamut allows at the colour's lightness and hue, and how much of sRGB's room the colour uses: "At L 0.77 and hue 92°, sRGB allows chroma up to 0.157, P3 0.181 and Rec.2020 0.185. This colour uses 88% of what sRGB allows."
- **CIE 1931 xy · four gamuts.** The horseshoe of visible colours with wavelengths marked, the triangles of **sRGB**, **Display P3**, **Adobe RGB** and **Rec.2020**, the D65 white point and your colour. A dashed line runs from D65 through the colour to the edge: where it lands is the dominant wavelength, and how far along it the colour sits is its purity. Six facts sit under the diagram:
  - **xy**, the chromaticity coordinates;
  - **Y · luminance**;
  - **Dominant λ**, in nanometres. Purples take a complementary wavelength, marked **c**, for example "c 563 nm". White has none;
  - **Purity**, as a percentage;
  - **CCT**, the correlated colour temperature, for example "≈ 6510 K". It is given only within Duv ±0.02 of the curve of heated bodies; otherwise the cell says "n/a" with the Duv;
  - **Described as**, the plain-language name.
- **Chroma headroom.** A slice through OKLab at the colour's lightness: every sRGB colour at that lightness is filled in, and P3 and Rec.2020 are dashed outlines. Beside it, bars for **sRGB**, **Display P3** and **Rec.2020** give the most chroma each allows at this lightness and hue, with the gain over sRGB, for example "+16%". A white tick marks your colour.
- **Probe · push chroma at this lightness and hue.** A **Probe chroma** slider from 0 to 0.40 in steps of 0.005, starting at your colour's chroma. A sentence and five tags say whether the probe is **Inside** or **Outside** **sRGB**, **Display P3**, **Adobe RGB**, **Rec.2020** and **ACEScg**. A card shows the probe as an `oklch()` value with **Copy CSS**. When the probe is outside sRGB, its swatch shows it brought back into sRGB by reducing chroma.
- **Membership · linear values, unclamped.** A table for **sRGB**, **Display P3**, **Adobe RGB (1998)**, **Rec.2020** and **ACEScg · AP1**, with the linear values, the encoded values and **Inside** or **Outside**. A check line shows that white maps to exactly 1, 1, 1 in each.

## Channels

- **The verdict.** The colour in OKLCH, 8-bit sRGB and linear light, for example "Perceptually it is L 0.766, C 0.138 at 91.6°: light soft amber. In 8-bit sRGB that is 211, 175, 55; in linear light the same colour is 0.651, 0.429, 0.038." Then its luminance, light reflectance value and contrast on black and on white, and which text reads on it best.
- **Key values · tap to copy.** Six tiles: **Luminance**, **OKLCH L**, **Chroma**, **Hue**, **HSL sat.** and **LRV**.
- **Eight groups of bars:** **sRGB · encoded** (0–255), **Linear sRGB** (0–1, light), **HSL** (device hue), **OKLab** (signed a, b), **OKLCH** (chroma against 0.37), **XYZ · D65** (against the white), **Display P3 · encoded** (0–1) and **YCbCr · BT.709** (full range).

Signed channels, OKLab a and b, grow from a centre line; Cb and Cr are centred at 0.5, the point of no colour.

## Walkthroughs

### Copy a colour in the notation you need

1. Type your colour into the field.
2. On **Spaces**, type part of a name into the search, for example `p3` or `lab`.
3. Select the row. It shows **Copied** for a moment.

The copied text is exactly what the row shows, so `hsl(46.2 63.9% 52.2%)` pastes into CSS as it is.

### Paste CSS lab() correctly

1. Select **CSS · 18** to see only the CSS rows.
2. Copy **Lab · D50** for CSS `lab()`, not **Lab · D65**.

The D65 values are right for tools that expect D65, such as many colour-science references; CSS reads `lab()` as D50.

### See how much more vivid a colour could be on a wide-gamut screen

1. Open **Gamut** and read **Chroma headroom**. For `#D3AF37`, sRGB allows chroma up to 0.157 at its lightness and hue, P3 up to 0.181 (+16%) and Rec.2020 up to 0.185 (+18%).
2. Move **Probe chroma** to 0.170. The sentence reads "At C 0.170 the probe leaves sRGB and Adobe RGB but stays inside Display P3, Rec.2020 and ACEScg."
3. Select **Copy CSS** to take the `oklch()` value for a P3 screen.

## Controls

| Control | What it does | Values or range | Default |
|---|---|---|---|
| Colour field | Sets the colour. | Hex, CSS names, CSS colour functions; fragments on `Enter` | The colour you opened with, or `#D3AF37` |
| Picker button | Picks a colour from your screen. | Supported browsers only | — |
| Dice button | Tries a random colour. | — | — |
| **Search 34 spaces** | Filters the rows. | Up to 40 characters | Empty |
| **All** / **CSS** / **Notation** | Shows every row or one kind. | 3 choices | **All** |
| Rows | Copy one value. | 34 rows | — |
| **Probe chroma** | Tests more or less chroma at this lightness and hue. | 0 to 0.40, steps of 0.005 | The colour's chroma |
| **Copy CSS** (probe) | Copies the probe as `oklch()`. | — | — |
| Key value tiles | Copy one value each. | 6 tiles | — |
| Tabs | Switch the view. | **Spaces**, **Gamut**, **Channels** | **Spaces** |

## Outputs and exports

The footer holds **Copy all as JSON**, **Share link**, **Save** and **Export**. On a narrow panel or a phone, the last three show as icons.

| Output | Format | What it contains |
|---|---|---|
| **Copy all as JSON** / **All 34 as JSON** | JSON | One key per row with the value exactly as shown, for example `"hex": "#D3AF37"`, `"oklch": "oklch(0.7655 0.1385 91.55)"`, `"display-p3": "color(display-p3 0.8047 0.6916 0.3074)"`. |
| **CSS-only set · 17 properties** | CSS | A `:root` block with one `--colour-…` custom property per CSS row. The `device-cmyk()` row is left out because browsers do not render it yet. |
| **Markdown table** | Markdown | Every row with the columns **Space**, **Value** and **Kind**. |
| **OKLCH value** | Text | The `oklch()` value. |
| **Share link** | A URL | This page with `?ctool=spaces`, the colour, any search or kind filter, the probe, and the tab you are on. |
| **Save** | A colour in your Library | Named with the description and hex, for example "Light soft amber #D3AF37", with all 34 values. |

The **Open in another tool** menu offers **Color Inspector**, **Color Formulation** (how the colour is built and how to mix it), **CMYK Soft-Proof**, **Gradient Library** (a gradient from your colour to a lighter or darker partner, blended in OKLCH), **Harmony Studio** and **Pantone & Named Lookup**, all with your colour.

## Links

| Key | What it sets | Values |
|---|---|---|
| `ctool` | Opens this tool. | `spaces` |
| `color` | The colour. | A hex code without `#` |
| `q` | The search on **Spaces**. | Up to 40 characters |
| `only` | Shows one kind of row. | `css`, `notation` |
| `probe` | The probe chroma on **Gamut**. | 0 to 0.4 |
| `ctab` | The tab to open on. | `spaces`, `gamut`, `channels` |

For example, `?ctool=spaces&color=D3AF37&q=lab&only=css` opens with only the CSS rows that mention lab: **Lab · D50** and **OKLab**.

## Accuracy and limits

- **Every conversion starts from an 8-bit sRGB colour**, so values are only as precise as that input. A colour set here is always inside sRGB, and therefore inside every wider gamut listed; the membership tests matter most for the probe.
- **Wide-gamut values are unclamped.** Membership is tested on the linear values before any clipping, and white maps to exactly 1, 1, 1 in each space.
- **D50 values** are adapted from D65 with the Bradford method, as CSS does.
- **Colour temperature is for near-whites only.** It is given only within Duv ±0.02 of the curve of heated bodies, between 1,000 and 15,000 K.
- **The scientific spaces** (Hunter Lab, IPT, JzAzBz) follow their published formulas with standard assumptions, such as an SDR white of 203 cd/m² for JzAzBz. Use a colour-science library for research-grade work.
- **CMYK here is naive.** It has no press profile. To see how a colour might print, use [CMYK Soft-Proof](cmyk-soft-proof.md).
- **Diagram colours are approximate** and limited to what your screen can show.

## Related

- [Colour Tools documentation](README.md)
- [Open the Colour Tools and work in their panels](launcher-and-panels.md)
- [Colour Tools dashboard](colour-tools-dashboard.md)
- [Quick Converter](../panel-tools/quick-converter.md) — the fourteen-notation converter in the workspace
- [Color Inspector](colour-inspector.md) — its **Formats** section has 43 notations
- [Color Formulation](colour-formulation.md) — the same colour step by step through the conversion pipeline
- [Color Science Lab](../../../colour-science-lab/README.md)
- [Library Kit](../../../../../kits/library-kit/README.md) — where saved colours go
