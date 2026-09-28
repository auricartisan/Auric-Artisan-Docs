---
title: Color Inspector — Everything about one colour
description: Use the Color Inspector to read one colour in every format, check it for contrast and colour-vision safety, build scales and harmonies, find its name and meaning, and export it as code.
product: Website › Tools › Colour workspace
updated: 2026-09-27
---

# Color Inspector

The Color Inspector takes one colour and shows you everything the site can work out about it. The colour itself fills the top of the panel, with a plain-language name such as "Light muted pink". Below it, a few sentences say what the colour is good for: whether it carries text on white or on black, and how it reads on the page you are looking at. Six sections hold the detail: contrast, colour vision, scales and harmonies, 43 notations, and names, meaning and science. An **Export** menu turns the colour into ready-to-paste code.

Use it when you meet a colour and want to know whether you can use it, and how. It is also the tool behind the site's `?color=` links: add `?color=` and a colour to any page address and the Inspector opens over that page.

The Inspector is one of the six **Essentials** in the Colour Tools. It opens in a floating panel; for moving, resizing and closing panels, see [Open the Colour Tools and work in their panels](launcher-and-panels.md).

## How to open it

- **Launcher:** right-click the page, choose **Colour tools** › **All colour tools…** (or press `Ctrl` + `Shift` + `C`), then select **Color Inspector** in the **Essentials** group. It opens on the launcher's working colour. You can also type a colour in the launcher's search and choose **Inspect …**.
- **Right-click a colour:** when you right-click a hex code or a colour swatch on the site, choose **Inspect in Colour Tools**. The Inspector opens with that colour.
- **Dashboard:** the **Color Inspector** card on the [Colour Tools dashboard](colour-tools-dashboard.md).
- **From another tool:** **Open in another tool** › **Color Inspector** in any other Colour Tool. If the Inspector is already open, it switches to that tool's colour instead of opening a second panel.
- **A link:** add `?color=` and a colour to any page address, for example `https://auricartisan.com/?color=CEA1B5`. See [A `?color=` link](#a-color-link) below.
- **A `?ctool=` link:** `?ctool=inspector&color=CEA1B5` also opens the Inspector, and `&ctab=` works with it. Without a `color`, `?ctool=inspector` opens on your working colour. `on=` adds a comparison colour, as it does on a `?color=` link.

Opened without a colour, the Inspector starts on the site's gold, `#D3AF37`.

If a link names something that is not a colour, such as `?color=xyz`, the Inspector still opens. It says it could not read the value, offers four colours to start from, and lists what `?color=` accepts. The sections stay disabled until you choose or type a colour.

### A `?color=` link

Add `?color=` and a colour to the address of any page on the site, and the Inspector opens over that page. For example:

```text
https://auricartisan.com/?color=CEA1B5
https://auricartisan.com/library/?color=1E40AF&on=FFFFFF&ctab=contrast
```

| Parameter | What it does | Accepted values |
|---|---|---|
| `color`, `colour` or `hex` | The colour to inspect. If you list several, the first is inspected and the rest appear as comparison colours. | See the forms below. Separate several colours with a comma, a semicolon or a vertical bar. |
| `on`, `bg`, `against` or `vs` | One or more comparison colours. They appear as extra rows in **Contrast** and in **Vision**'s **Confusion risk**. | Same forms as `color`. |
| `ctab` | The section to open on. | `read`, `contrast`, `vision`, `palette`, `formats`, `about`. Older names still work (see [Controls](#controls)). |

The colour can be written as:

- a hex code with 3, 4, 6 or 8 digits: `CEA`, `CEA1B5`, `CEA1B5CC` (the 4- and 8-digit forms carry transparency);
- `rgb()` or `rgba()`, `hsl()` or `hsla()`, `hwb()`, for example `rgb(206 161 181)`;
- three numbers separated by spaces, read as red, green and blue: `206+161+181`;
- a CSS colour name such as `rebeccapurple` or `tomato`;
- a fragment of a hex code. One digit is read as a grey (`C` becomes `#CCCCCC`), two digits are repeated (`CE` becomes `#CECECE`), five or seven digits are padded with the last digit, and anything longer than eight digits keeps the first six. The Inspector then shows a small tag saying which text it started from.

> **Important:** Leave out the `#`, or write it as `%23`. In an address, `#` starts the page fragment, so `?color=#CEA1B5` reaches the site without a colour.

In an address bar, a space can be typed as `+` or `%20`. When a value contains brackets, such as `rgb(206 161 181)`, separate several colours with `;` or `|`, because a comma is then read as part of the colour.

When the Inspector was opened by a link, it keeps the address bar in step as you change the colour or the section, so copying the page address shares the current read-out. If you open a second `?color=` link, or go back and forward between two, the open Inspector switches colour instead of opening another panel. An Inspector opened from the launcher or another tool leaves the address bar alone, and a colour handed over by another tool's **Open in another tool** does not change the address either.

## Screen tour

From top to bottom the panel has a title bar, the specimen, a strip of six sections, the selected section, and a row of actions.

### The title bar

The title bar shows **Color Inspector**. When you widen the panel beyond about 620 pixels, the link that describes what you are looking at appears beside the name, for example `?color=CEA1B5`; at the Inspector's usual width it is hidden, and **Share link** copies it.

Its buttons are the usual panel buttons for linking, duplicating, pinning, minimising, maximising and closing (see [Open the Colour Tools and work in their panels](launcher-and-panels.md#the-title-bar)), plus **Dock to the right edge**. Docking pins the panel, 560 pixels wide, to the full height of the right edge of the window, so you can keep using the page beside it; a docked panel cannot be dragged or resized. Select the button again (**Undock the inspector**) to return the panel to where it was. The Inspector remembers whether you left it docked. Unlike the other Colour Tools, the Inspector has no **Open in another tool** button in its title bar; its links to other tools are in **Read**.

The first time it opens, the panel is 560 pixels wide at the right of the window. After that it keeps whatever size and position you give it.

On a phone the Inspector opens as a sheet from the bottom of the screen instead of a window, with only a close button in its title bar.

### The specimen

The top of the panel is filled with the colour.

- **The name.** A plain-language description built from the colour's lightness, chroma and hue: "Light muted pink", "Vivid red", "Very dark greyish blue". Neutrals are named by lightness alone, from "Black" to "White".
- **The code line.** The hex code and the OKLCH value, for example `#CEA1B5 · oklch(0.756 0.059 350.2)`.
- **The ink tag.** Which of black or white reads better on the colour, and at what ratio, for example **Black ink · 9.38:1**. The name, code line and tags on the specimen are always written in that ink.
- **The colour field.** A box for the colour, with two buttons: the drop picks a colour from anywhere on your screen (only in browsers that support it), and the dice jumps to a random colour of medium saturation and lightness.

When the colour came from a link with transparency, the specimen shows it over a checkerboard with an **alpha** tag. When a link held a fragment the site had to interpret, such as `?color=CE`, a tag shows the text it started from, for example **from “CE”**.

On every section except **Read**, the specimen folds to a strip that shows only the name and the hex code, so the section has room.

#### Typing a colour

The box accepts a hex code (3, 4, 6 or 8 digits, `#` optional), a CSS colour name such as `rebeccapurple`, or a CSS colour function such as `rgb(206 161 181)`, `hsl(…)` or `oklch(…)`. The Inspector follows as you type whenever the text is a complete colour. Press `Enter` to also accept a fragment of a hex code, read the same way as in a link.

If you press `Enter` on something that is not a colour, the box is outlined in red and the colour does not change. Screen readers announce "That isn't a colour yet". When you leave the box, it goes back to the colour on screen.

### The sections

The six sections are **Read**, **Contrast**, **Vision**, **Palette**, **Formats** and **About**. With a section focused, `←` and `→` move to the previous or next one (wrapping round), and `Home` and `End` jump to the first and last. On a narrow panel the strip scrolls sideways, and a fade at the right edge shows there is more.

Almost every swatch in the sections is a button. Select one and the Inspector switches to that colour. The colour you were on becomes a comparison row in **Contrast**, labelled **Inspected before**, so you can compare against it and step back to it.

### Read

- **The verdict.** Up to three sentences:
  - which of black or white the colour pairs with, with both ratios, and what that means in use: for example "Pairs with black (9.38:1), not white (2.23:1): a fill or accent on light pages, and text only on dark ones";
  - how it reads on the page you opened it over, with that page's background and the ratio: "fine for body text", "enough for large text and icons only", or "too faint for text, but fine as a fill";
  - its dominant wavelength and excitation purity. Purples and magentas have no single wavelength, so they get a complementary wavelength instead. A colour with no hue says so, and that hue angle, dominant wavelength and colour temperature do not apply to it.
- **Key values.** Six cells: **HEX**, **RGB**, **HSL**, **OKLCH**, **CIELAB** and **LRV** (light reflectance value). Select a cell to copy its value; the cell shows **Copied** for a moment.
- **Where it reads as text.** Your colour as text on the page's background, on white and on black, each with its ratio and grade: **AAA** (7:1 or more), **AA** (4.5:1), **Large** (3:1, enough for large text and icons) or **Fail**.
- **Channels.** Bars for red, green and blue, for alpha when the colour is transparent, and for OKLCH lightness and chroma.
- **Open in another tool.** Eight buttons that open another Colour Tool with this colour: **Contrast System**, **Harmony Studio**, **Space Converter**, **Pantone & Named**, **Accessibility Lab**, **Formulation**, **CMYK Soft-Proof** and **Psychology**. If that tool is already open, its panel comes to the front and switches to this colour instead of opening a second copy.

### Contrast

**As text on each surface** is a table of your colour as text on:

- **This page**: the background of the page the Inspector opened over;
- **This page's text**: the page's own text colour, when it differs;
- **White** and **Black**;
- up to four comparison colours: **Compare · &on=** for colours given with `on=`, **Also in the link** for extra `?color=` colours, and **Inspected before** for colours you moved away from.

| Column | Meaning |
|---|---|
| **Ratio** | The WCAG 2 contrast ratio. |
| **Body** | Pass at 4.5:1 or more, the level for normal text. |
| **Large** | Pass at 3:1 or more, the level for large text, icons and other interface parts. |
| **AAA** | Pass at 7:1 or more. |
| **APCA** | The APCA lightness contrast (Lc) of your colour as text on that surface, and the use it supports: body text (Lc 75 or more), content text (60), headings (45), spot text (30), or no text. The Lc is shown as a whole number without its sign, cut towards zero, so a pair at Lc −59.99 reads **Lc 59** and not Lc 60. |

On a narrow panel the table scrolls sideways; you can scroll it with the keyboard once it has focus.

**Nearest colour that passes** offers up to three fixes, one each for text on this page, on white and on black, wherever your colour falls short of 4.5:1. Each fix keeps your colour's hue and chroma and changes only its lightness, just enough to reach 4.5:1, for example "Text on white: #8F7300 — 4.54:1 · same hue, lightness 0.77 → 0.57". Select **Use it** to inspect the fix. When the colour already passes everywhere, the section says so.

**As a surface** shows your colour behind black text and behind white text, with the ratio and grade of each.

### Vision

- **Four colour-vision deficiencies**, each at full strength: **Protanopia** (no red-sensitive cones), **Deuteranopia** (no green-sensitive cones), **Tritanopia** (no blue-sensitive cones, which is rare) and **Achromatopsia** (no colour at all). Each row shows your colour beside how it is seen, the simulated hex (select it to inspect that colour), and how far it moved: **Looks the same** (ΔE under 2), **Shifts slightly** (2 to 5), **Shifts noticeably** (5 to 10) or **Reads as a different colour** (over 10).
- **This page, as each sees it.** Five small tiles of your colour as text on this page's background: once for typical vision and once for each deficiency. This shows whether text in the colour stays readable against the page for each reader.
- **Confusion risk.** Shown only when there are comparison colours. For each one: the ΔE between it and your colour for typical vision, the vision type under which the two are closest, the ΔE there, and a verdict: **Distinct** (ΔE 10 or more), **Tight** (5 to 10) or **Confusable** (under 5).

### Palette

- **Tonal scale.** Eleven steps named 50 to 950, each at a fixed OKLCH lightness, with chroma eased off towards the ends and kept inside what a screen can show. Your colour itself sits at the step nearest its lightness, ringed, with its exact hex. The small number under each step is its contrast on white; 4.5 and above can carry body text.
- **Harmonies.** Five schemes, each turned in OKLCH so the companion colours keep your colour's lightness and chroma: **Complementary** (+180°), **Analogous** (−30° and +30°), **Triadic** (+120° and +240°), **Split complementary** (+150° and +210°) and **Square** (every 90°). Your colour is ringed in each. A colour with no hue has nothing to turn, and the section says so.
- **Tints, shades and tones.** Nine steps each from your colour towards white, towards black and towards mid grey, mixed in OKLCH.

### Formats

**Copy all as JSON** copies the full read-out. Below it are 43 notations in five groups; select any row to copy that value, and the row shows **Copied**.

| Group | Notations |
|---|---|
| **Web & CSS** (18) | HEX, HEX (short), RGB, RGBA, RGB %, HSL, HSLA, HSV, CMYK, CIE XYZ (D65), CIELAB (D65), CIELCh (D65), OKLab, OKLCH, HEX + alpha, RGB (modern), HWB, HSI |
| **Wide gamut** (5) | Display P3, Adobe RGB and Rec. 2020 (as CSS `color()` values), ACEScg (linear), Linear sRGB (as CSS `color(srgb-linear …)`) |
| **Perceptual & CIE** (9) | CIE xyY, CIE u′v′, CIELAB (D50), CIELCh (D50), CIELUV, LCh(uv), Hunter Lab, IPT, JzAzBz |
| **Video & broadcast** (3) | YCbCr, YUV, YIQ |
| **Code** (8) | Decimal, Android ARGB, UIColor, SwiftUI, Flutter, OpenGL vec4, .NET, CSS variable |

**Link to it from any page** reminds you of the three link parameters: `?color=` opens the Inspector on a colour, `&on=` adds a comparison colour, and `&ctab=` opens straight to a section.

### About

- **The name** again, with a sentence on its warmth, hue family, chroma and lightness.
- **Nearest named colour.** The nearest of 1,058 named colours, its ΔE2000 from yours and what that distance means, from "indistinguishable" (under ΔE 1) to "the nearest entry, but visibly different" (ΔE 10 or more), with **Inspect**. Eight more names follow.
- **Named systems.** The closest entry in each of five systems, with its ΔE: HTML/CSS, Pantone Solid C, RAL Classic, NCS and Crayola. Select a row to inspect that entry.
- **What it suggests.** For the colour's hue family at its lightness: emotion words, **Warmth** and **Energy** meters, personality traits, a sentence on brand fit, and cultural notes by region or tradition. Each region gives what the colour is associated with there and, where the data has them, what to be careful of and a **Ritual & mourning** line, for example "Weddings; funerals only when honouring martyrs" for red in China, or "Mourning" for red in South Africa. Check those lines before wedding, funeral or memorial work. Very light colours read softer and calmer; very dark ones read more serious and grounded.
- **Science.** Eight facts: the OKLCH hue angle and hue family; whether the colour is warm or cool by hue; the dominant (or complementary) wavelength; excitation purity; the correlated colour temperature, for near-white colours only; the light reflectance value; the chroma headroom (how much of the most chroma a screen can show at this lightness and hue the colour uses); and CIE x, y with u′v′.
- **Approximate reflectance.** A spectrum strip from 380 to 780 nm, masked to show roughly which light a surface of this colour would send back. Point at a band to see its wavelength and how much it reflects.
- **Same colour in other gamuts.** The colour's R, G and B values in sRGB, Display P3, Adobe RGB and Rec. 2020, with a note on the total ink of a simple CMYK split.

**About** downloads its names, systems and psychology data the first time you open it, and shows "Loading…" until they arrive.

### The actions

The row at the bottom of the panel holds **Copy hex**, **Share link**, **Save** and **Export**. On a narrow panel or a phone, the last three show as icons, still named for screen readers.

- **Copy hex** copies the hex code.
- **Share link** copies the current page address with `?color=` and, unless you are on **Read**, `&ctab=` for the section you are on.
- **Save** saves the colour to your Library.
- **Export** opens a menu. Select an item to copy it, or to download a swatch file. In the menu, `↑` and `↓` move between items, `Home` and `End` jump to the ends, and `Esc` closes it and returns you to the **Export** button.

After a copy or save, the control you used says **Copied**, **Link copied** or **Saved** for a moment, and a short message confirms what happened.

## Walkthroughs

### Check whether a brand colour can carry text

1. Open the Inspector with your colour, for example with `?color=D3AF37` on any page.
2. Read the verdict on **Read**. For `#D3AF37` it says "Pairs with black (9.95:1), not white (2.10:1): a fill or accent on light pages, and text only on dark ones".
3. Open **Contrast**. The **White** row shows 2.10:1 and **Fail** for body text; the **Black** row shows 9.95:1 and passes all three levels.
4. Under **Nearest colour that passes**, find **Text on white: #8F7300** and select **Use it**.

The Inspector switches to `#8F7300`, the same gold hue at a lower lightness, which reaches 4.54:1 on white. Your original gold is now the **Inspected before** row, so you can compare the two or go back.

### Check that two colours stay distinct for colour-blind readers

1. Open the Inspector with both colours in one link, for example `?color=D62728&on=2CA02C` for a red and a green.
2. Open **Vision**.
3. Read **Confusion risk**. For this pair the ΔE is about 72 for typical vision, but under **Deuteranopia** it falls to about 4.8, and the verdict is **Confusable**.

If the verdict is **Confusable** or **Tight**, do not rely on the colour difference alone: add a label, an icon or a pattern.

### Export a colour as design tokens

1. Set the colour you want in the colour field.
2. Select **Export**, then **Tailwind scale**.

The clipboard now holds a `tailwind.config.js` snippet with a `brand` scale from 50 to 950, the same steps as the **Tonal scale** in **Palette**. **CSS custom properties** for `#D3AF37` starts like this:

```css
:root {
  --brand: #d3af37;
  --brand-rgb: 211 175 55;
  --brand-oklch: oklch(0.766 0.138 91.6);
  --brand-ink: #000000;
  --brand-50: #fff5d7;
  --brand-100: #ffeaad;
  /* … through --brand-950 */
}
```

`#D3AF37` sits at step 300 of its own scale, so `--brand-300` is exactly `#d3af37`.

### Share exactly what you are looking at

1. Open the section you want the other person to see, for example **Vision**.
2. Select **Share link**.

The button says **Link copied**. The link opens the same page with the Inspector on the same colour and section.

## Controls

| Control | What it does | Values or range | Default |
|---|---|---|---|
| Colour field | Sets the colour. | Hex (3, 4, 6 or 8 digits), CSS names, CSS colour functions; fragments on `Enter` | `#D3AF37`, or the colour you opened with |
| Drop button | Picks a colour from your screen. | Supported browsers only | — |
| Dice button | Picks a random colour of medium saturation and lightness. | — | — |
| Section strip | Switches the section. | 6 sections | **Read**, or the `ctab` value |
| Key values cells | Copy one value each. | 6 cells | — |
| Swatches and fixes | Inspect that colour. | — | — |
| **Use it** | Inspects a fix from **Nearest colour that passes**. | Up to 3 fixes | — |
| Formats rows | Copy one notation. | 43 rows | — |
| **Copy all as JSON** | Copies the full read-out. | — | — |
| **Open in another tool** | Opens another Colour Tool with this colour. | 8 tools | — |
| **Copy hex** | Copies the hex code. | — | — |
| **Share link** | Copies a link to this page, colour and section. | — | — |
| **Save** | Saves the colour to your Library. | — | — |
| **Export** | Opens the export menu. | 9 items | — |
| **Dock to the right edge** (title bar) | Pins the panel, 560 pixels wide, to the right edge at full height. | On or off | Off, or as you last left it |

`ctab` accepts `read`, `contrast`, `vision`, `palette`, `formats` and `about`. Links made for the earlier ten-tab Inspector still work: `overview` opens **Read**, `harmony` and `scales` open **Palette**, `names`, `mind` and `science` open **About**, and `export` opens **Formats**.

## Outputs and exports

| Output | Format | Notes |
|---|---|---|
| **Copy hex** | Text, for example `#D3AF37` | — |
| **Share link** | A URL with `color`, and `ctab` unless you are on **Read** | Opens the Inspector on the same page, colour and section. |
| **Save** | A colour item in your Library | Named with the hex and the nearest named colour once **About** has loaded it, otherwise the plain-language name. |
| Key values, Formats rows | Text | One value each. |
| **CSS custom properties** | CSS | `--brand`, `--brand-rgb`, `--brand-oklch`, `--brand-ink`, `--brand-50` to `--brand-950`. |
| **SCSS variables** | SCSS | `$brand`, `$brand-ink`, `$brand-50` to `$brand-950`. |
| **Tailwind scale** | `tailwind.config.js` snippet | A `brand` colour scale 50 to 950. |
| **Design tokens, DTCG JSON** | JSON in the Design Tokens Community Group format | A `brand` group with 50 to 950, each `{ "$type": "color", "$value": … }`. |
| **SwiftUI** | Swift `Color` extension | `brand50` to `brand950`. |
| **Android colors.xml** | XML resources | `brand_50` to `brand_950`, as `#FFRRGGBB`. |
| **Full read-out, JSON** and **Copy all as JSON** | JSON | Hex, alpha, name, RGB, HSL, HSV, CMYK, CIELAB, CIELCh, OKLab, OKLCH, XYZ, CIE xy, luminance, light reflectance value, contrast on white and on black, colour temperature, dominant or complementary wavelength, excitation purity, nearest name and total ink. Values that do not apply to the colour are `null`, never a made-up number. |
| **Swatch, SVG** / **Swatch, PNG** | 512 × 512 file | Named after the hex code, for example `D3AF37.svg`. |

If you select **Save** on a page where the Library is not available, the message says "The library isn't available on this page".

## Accuracy and limits

- **Terms used on this page.** *WCAG contrast ratio*: the ratio between the relative luminance of two colours, from 1:1 to 21:1. WCAG 2 asks for 4.5:1 for normal text (AA), 3:1 for large text and interface parts, and 7:1 for AAA. *APCA Lc*: a newer measure of perceived lightness contrast. *ΔE2000*: the CIEDE2000 colour difference; under about 1, two colours look the same side by side. *OKLCH*: a colour model with lightness, chroma and hue that changes evenly to the eye. *Colour-vision deficiency*: reduced or missing sensitivity in one type of cone.
- **Ratios are rounded down, and Lc is cut towards zero.** The Inspector prints ratios to two decimals rounded down, so a pair at 4.497:1 shows 4.49:1 and fails, rather than showing 4.50:1. In the same way, an APCA value of Lc −59.99 shows as Lc 59, never as the Lc 60 it misses.
- **APCA is a guide.** WCAG 3, which may adopt APCA, is still a draft. The uses shown beside each Lc value are the published APCA guidance, not a conformance result. For a WCAG 2.2 audit, use the **Ratio**, **Body**, **Large** and **AAA** columns.
- **Vision simulations are approximations.** They model full-strength dichromacy (Machado, Oliveira and Fernandes, 2009), applied to linear light, the same model as the site's Vision tools. Real colour vision varies from person to person, and milder forms are more common than the full forms shown. Use the results to find risks, not to certify a design.
- **Colour temperature is for near-whites only.** A correlated colour temperature is only meaningful for a colour close to the colour of a heated body. The Inspector gives one only when the colour sits within 0.012 of that curve (Duv) and between 1,000 and 15,000 K. For every other colour it says whether the colour is warm or cool by hue, and gives no kelvin figure.
- **Colours with no hue.** Below an OKLCH chroma of 0.02 a colour is treated as neutral: it has no hue angle, no dominant wavelength and no harmonies.
- **Reflectance is a heuristic.** The curve explains the colour; it is not a spectrophotometer reading and cannot be used to match pigments.
- **CMYK is arithmetic.** The total-ink note uses a simple conversion, not an ICC profile. Soft-proof in [CMYK Soft-Proof](cmyk-soft-proof.md) before sending artwork to print.
- **Named-system matches are approximate.** Pantone, RAL and NCS entries are published sRGB approximations of printed swatches, so the Inspector always shows the ΔE distance rather than calling a match exact.
- **sRGB only.** Colours are handled as sRGB. Transparency from a link is shown and exported, but contrast is calculated on the solid colour.
- **Page sampling.** "This page" is the first solid background found from the page body upwards, and "This page's text" is the page's main text colour. They are not the colours behind a particular element.
- **Network.** **About** downloads its data from the site the first time you open it. If that fails, the section says "That data could not be loaded."

## Related

- [Colour Tools documentation](README.md)
- [Open the Colour Tools and work in their panels](launcher-and-panels.md) — the launcher, `?ctool=` links, panels and the control bar
- [Colour Tools dashboard](colour-tools-dashboard.md)
- [Contrast System](contrast-system.md) — deeper contrast work on several foregrounds
- [Accessibility Lab](accessibility-lab.md) — a whole palette against the standards and vision filters
- [Color Name Finder](colour-name-finder.md) — a quick name lookup
- [Harmony Studio](harmony-studio.md), [Pantone & Named Lookup](pantone-and-named-lookup.md), [Color Space Converter](colour-space-converter.md), [CMYK Soft-Proof](cmyk-soft-proof.md), [Color Psychology](colour-psychology.md)
- [Library Kit](../../../../../kits/library-kit/README.md) — where saved colours go
