---
title: Harmony Studio — Palettes from one colour on the OKLCH wheel
description: Build a harmony palette from one base colour in eight schemes, walk it to a contrast target on your background, check it for every kind of colour vision, preview it in an interface and export it as tokens.
product: Website › Tools › Colour workspace
updated: 2026-09-27
---

# Harmony Studio

Harmony Studio builds a palette from one base colour by a classic harmony rule, such as complementary, triadic or square, and shows it on a colour wheel. It can then walk each colour's lightness until it reaches a contrast target on the background you choose, which turns a pleasing palette into one you can use for text and interface parts. It also checks whether the colours stay distinct for people with colour-vision deficiencies, previews them in a small interface, and exports them as design tokens named by role.

A **colour harmony** is a set of hues chosen by their position on the colour wheel: opposite each other, evenly spaced, or close together. Harmony Studio turns the hue in OKLCH, a perceptual colour model, so each new colour keeps the base colour's lightness and chroma.

Harmony Studio is in the launcher's **Design** group. It opens in a floating panel over the page you are on; for moving, docking and closing panels, see [Open the Colour Tools and work in their panels](launcher-and-panels.md).

## How to open it

- **Launcher:** press `Ctrl` + `Shift` + `C` (or right-click the page and choose **Colour tools** › **All colour tools…**), then select **Harmony Studio**.
- **Right-click menu:** **Colour tools** › **Harmony Studio**.
- **Right-click a colour:** when you right-click a hex code or a colour swatch on the site, choose **Build harmonies**.
- **From another Colour Tool:** it is in the **Open in another tool** menu of Color Psychology, Gradient Library, Color Formulation and Color Space Converter, and in the Color Inspector's **Open in another tool** list.
- **A link:** add `?ctool=harmony` to any page address, with the keys under [Links](#links).

Opened from the launcher or the [Colour Tools dashboard](colour-tools-dashboard.md), the base is the [working colour](launcher-and-panels.md#the-working-colour). With no colour at all, the base is `#D3AF37`. The background always starts as dark navy, `#0F172A`, unless a link sets it.

## Screen tour

The panel has the shared Colour Tools layout: the palette painted across the top, four tabs, a controls rail on the left, the selected tab on the right and a row of actions at the bottom. [Open the Colour Tools and work in their panels](launcher-and-panels.md) describes the parts every tool shares, including the title bar, **Open in another tool**, **Dock** and the bottom sheet on phones.

### The palette band

- **The lead block** is painted in the background colour. It says **On #0F172A**, names the palette, for example "Triadic from light soft amber", and counts the colours and how many are readable as body text on the background: "3 colours · 3 readable on #0F172A".
- **One block per colour**, with its role and hex. The base is always labelled **Base**; the others are named by their hue offset from it, such as **+120°** or **−30°**, or **Complement** for +180°. Monochromatic steps are named by their lightness, such as **L 44**.

If the base has almost no hue, the lead block says "A grey has no harmony".

### The controls rail

- **Base colour.** A colour field with a picker button (in browsers that support it) and a dice button. Under it, six house colours to start from: Auric gold `#D3AF37`, House navy `#1D2A3E`, Gold ink `#765A0B`, Rose `#CEA1B5`, Process blue `#0085CA` and Burnt orange `#C2410C`.
- **Background it sits on.** The colour the palette is checked and previewed on.
- **Scheme.** The harmony rule, with the number of colours beside each name. A note under the list describes the scheme.
- **Spread.** A slider from 10° to 60° in steps of 5°, shown for **Split-complementary**, **Analogous** and **Double split**.
- **Steps.** A slider from 3 to 9, shown for **Monochromatic**.
- **Mode.** Whether to adjust the colours for contrast, with a note under the list.
- **Also adjust the base.** When ticked, the base is walked to the target too. It is unavailable in **As generated**.

The colour fields accept a hex code (with or without `#`), a CSS colour name or a CSS colour function. The tool follows as you type whenever the text is a complete colour. If you press `Enter` on something that is not a colour, the field is outlined in red and a message says "That isn't a colour yet".

On a narrow panel or a phone, the rail moves above the results.

## Schemes

| Scheme | Hue offsets from the base | Colours | Note in the tool |
|---|---|---|---|
| **Complementary** | 0°, 180° | 2 | The hue opposite the base. Maximum tension; use one as the accent. |
| **Split-complementary** | 0°, 180° − spread, 180° + spread | 3 | The two hues either side of the complement. Softer than a straight complement. |
| **Analogous** | −spread, 0°, +spread | 3 | Neighbouring hues. Calm and cohesive; lean on lightness for contrast. |
| **Triadic** | 0°, 120°, 240° | 3 | Three hues 120° apart. Balanced and lively. |
| **Tetradic, rectangle** | 0°, 60°, 180°, 240° | 4 | Two complementary pairs, 60° apart. Rich; let one hue lead. |
| **Square** | 0°, 90°, 180°, 270° | 4 | Four hues 90° apart. The most even spread. |
| **Double split** | −spread, 0°, +spread, 180° − spread, 180° + spread | 5 | The base, its neighbours and their complements. Five hues. |
| **Monochromatic** | Same hue, lightness in even steps from 0.28 to 0.92 | 3 to 9 | One hue at several lightness steps. The base keeps its exact value. |

The spread is 30° unless you change it, so **Split-complementary** gives +150° and +210°, and **Analogous** gives −30° and +30°.

**Tetradic, rectangle** and **Square** are different shapes: the rectangle pairs hues 60° apart, the square spaces all four 90° apart.

The **Base** label always sits on your base colour. In **Analogous** and **Double split**, the colour 30° below the base comes first in the lists, and your base is the one labelled **Base**. In **Monochromatic**, your base replaces the step nearest its own lightness and keeps its exact value; the other steps take their lightness from the even spread.

When a turned colour would fall outside what a screen can show, its chroma is trimmed until it fits. The hue stays exact and only the vividness drops; the colour's note and the **Wheel** verdict say so.

## Modes

| Mode | Target on the background | Note in the tool |
|---|---|---|
| **As generated** | None | Colours exactly as the scheme makes them. |
| **Readable text · 4.5:1** | 4.5:1 | Walks each colour's OKLCH lightness until it reaches 4.5:1 on the background. Hue and chroma stay. |
| **UI parts · 3:1** | 3:1 | Enough for icons, borders, focus rings and large text. |
| **Strict text · 7:1** | 7:1 | The strict level for small body text. |

A contrast mode walks each colour lighter or darker, whichever is away from the background, until it reaches the target. The colour's note then says, for example, "Moved from #00C9E3 to reach 4.5:1; hue kept." When no lightness at that hue reaches the target on this background, the note says so and the colour is left as it was.

The base is kept as you set it unless you tick **Also adjust the base**.

## Wheel

**Wheel** is the tab that opens first.

- **The verdict.** The scheme and the hue of each colour on the OKLCH wheel, for example "Triadic from light soft amber: 3 colours at 92°, 212° and 332° on the OKLCH wheel." Then how many colours read as body text on the background, and the weakest. When some fall short, it suggests setting **Mode** to **Readable text**, or ticking **Also adjust the base** if the base is the weakest. A note appears when any colour lost chroma to stay on screen.
- **The OKLCH hue wheel.** A ring of hues with a dot for each colour, joined by a dashed outline, and the base in the centre with its hex. Dots sit at their OKLCH hue, the same hue the palette uses, so a triadic draws an even triangle. In **Monochromatic**, only the base's dot is shown.
- **The list.** Each colour with its role, hex, OKLCH lightness, chroma and hue, its contrast ratio on the background and a grade: **AAA** (7:1 or more), **AA** (4.5:1), **Large only** (3:1) or **Fail**.
- **The selected colour.** Select a dot or a list row to select that colour; the base is selected to start with. The card below shows its note, with **Copy hex**, **Make it the base** (the selected colour becomes the base and the harmony is rebuilt around it) and **Inspect** (opens it in the Color Inspector).

## Palette

- **The verdict** repeats how many colours read as body text, then says how distinct the colours stay: for example "Every pair stays distinct in normal vision (closest ΔE 44.9). Under achromatopsia, Base and +120° come within ΔE 1.4 — label them rather than rely on colour."
- **Each colour, on** the background. One card per colour with its swatch, a sample of "Aa" in the colour on the background, the ratio and grade, its OKLCH values, its note and a **Copy** button for its hex.
- **Closest pair under each kind of vision.** A table with a row each for **Normal vision**, **Protanopia**, **Deuteranopia**, **Tritanopia** and **Achromatopsia**. Each row shows the two colours as that reader sees them, which pair is closest, the ΔE2000 between them and a reading: **Distinct** (ΔE 10 or more), **Close — add labels** (5 to 10) or **Hard to tell apart** (under 5).

## Preview

**Preview** puts the palette into a small interface on the background: a kicker ("Autumn collection"), a heading ("Colour that holds together"), body text with a link, two buttons ("Shop the palette" and "Save for later"), a tag for each colour and a row of bars.

- The heading and link use the colour with the highest contrast on the background. The main button is filled with the base; the second button uses the colour after the base.
- The switch above the preview shows it as seen with **Normal**, **Protan**, **Deutan**, **Tritan** or **Achromat** vision.
- The verdict names which colours the heading and button use and, when two colours nearly merge for the chosen vision, which ones.

The bars only show how the colours sit side by side; they are not data.

## Tokens

**Tokens** shows the palette as code, one token per colour, named by role: `base`, `complement`, the hue offset (`hue-120`, `hue-minus-30`), or the lightness step in **Monochromatic** (`l44`).

Choose **CSS**, **SCSS**, **Tailwind**, **JSON** or **Tokens** (the Design Tokens Community Group format). The code appears below, with a **Copy** button for that format. In CSS, JSON and DTCG, each token carries its contrast ratio on the background, so the reason for every value travels with it.

## Walkthroughs

### Make an accent set that reads on a white page

1. Set **Base colour** to your brand colour, for example `#D3AF37`.
2. Set **Background it sits on** to `#FFFFFF`.
3. Leave **Scheme** on **Triadic** and set **Mode** to **Readable text · 4.5:1**.
4. Read the list on **Wheel**. The +120° colour moves from `#00C9E3` to `#008294` (4.54:1) and the +240° colour from `#E591DA` to `#A95AA0` (4.50:1). The base stays at 2.10:1, and its note says "The base is kept as you set it."
5. Tick **Also adjust the base** if the base must carry text too.

### Check a palette for colour-blind readers

1. Build your palette and open **Palette**.
2. Read **Closest pair under each kind of vision**. Any row marked **Hard to tell apart** or **Close — add labels** names the two colours at risk.
3. Open **Preview** and select that vision type to see the pair in use.

Where two colours come close, do not rely on colour alone: add a label, an icon or a pattern.

### Export the palette as design tokens

1. Open **Tokens** and choose **Tokens**.
2. Select **Copy**.

For the starting triadic, the CSS format reads:

```css
:root {
  --harmony-base: #d3af37;  /* Base, 8.46:1 on #0f172a */
  --harmony-hue-120: #00c9e3;  /* +120°, 8.89:1 on #0f172a */
  --harmony-hue-240: #e591da;  /* +240°, 7.98:1 on #0f172a */
}
```

## Controls

| Control | What it does | Values or range | Default |
|---|---|---|---|
| **Base colour** | The colour the harmony is built from. | Hex, CSS names, CSS colour functions | The colour you opened with, or `#D3AF37` |
| House colours | Start from one of six house colours. | 6 swatches | — |
| **Background it sits on** | The colour for contrast checks and the preview. | As above | `#0F172A` |
| **Scheme** | The harmony rule. | 8 schemes | **Triadic** |
| **Spread** | The angle for split, analogous and double-split schemes. | 10° to 60°, steps of 5° | 30° |
| **Steps** | The number of monochromatic steps. | 3 to 9 | 5 |
| **Mode** | The contrast target, if any. | **As generated**, **Readable text · 4.5:1**, **UI parts · 3:1**, **Strict text · 7:1** | **As generated** |
| **Also adjust the base** | Walks the base to the target too. | On or off | Off |
| Wheel dots and list rows | Select a colour. | — | The base |
| **Make it the base** | Rebuilds the harmony around the selected colour. | Unavailable on the base | — |
| **Inspect** | Opens the selected colour in the Color Inspector. | — | — |
| Vision switch (**Preview**) | Simulates a kind of colour vision. | **Normal**, **Protan**, **Deutan**, **Tritan**, **Achromat** | **Normal** |
| Format switch (**Tokens**) | Chooses the token format. | **CSS**, **SCSS**, **Tailwind**, **JSON**, **Tokens** | **CSS** |
| Tabs | Switch the view. | **Wheel**, **Palette**, **Preview**, **Tokens** | **Wheel** |

## Outputs and exports

The footer holds **Copy hex list**, **Share link**, **Save palette** and **Export**.

| Output | Format | What it contains |
|---|---|---|
| **Copy hex list** | Text | The colours in palette order, separated by commas, for example `#D3AF37, #00C9E3, #E591DA`. |
| **Share link** | A URL | This page with `?ctool=harmony`, the base, background, scheme, spread or steps, mode, and the tab you are on. |
| **Save palette** | A palette in your Library | Named, for example, "Triadic from #D3AF37", with the scheme, mode, base, background and colours. |
| **Hex list** | Text | The same as **Copy hex list**. |
| **CSS custom properties** | CSS | `--harmony-…` per colour, each with a comment giving its role and ratio on the background. |
| **SCSS variables** | SCSS | `$harmony-…` per colour. |
| **Tailwind config** | `tailwind.config.js` snippet | A `harmony` colour group with a key per role. |
| **JSON** | JSON | The scheme, mode, base, background and each colour's role, hex, OKLCH values, ratio and, when a mode moved it, the hex it came from (`adjustedFrom`). |
| **Design tokens (DTCG)** | JSON | A `harmony` group; each token has `$type: "color"`, `$value` and a `$description` with its role and ratio. |
| **PNG strip** | PNG download | A strip of the colours, 80 pixels wide per colour and 100 pixels tall, named after the scheme and base, for example `harmony-triadic-d3af37.png`. |

The **Open in another tool** menu offers **Color Inspector** (the selected colour), **Contrast System** (all the colours as text on the background), **Accessibility Lab** (the colours and the background as one set), **Gradient Library** (a blend from the base into the next colour), **Color Psychology** (the mood of the palette) and **Color Name Finder** (the selected colour).

## Links

| Key | What it sets | Values |
|---|---|---|
| `ctool` | Opens this tool. | `harmony` |
| `color` | The base colour. | A hex code without `#` |
| `on` (or `bg`) | The background. | A hex code without `#` |
| `scheme` | The scheme. | `complementary`, `split`, `analogous`, `triadic`, `tetradic`, `square`, `doublesplit`, `mono` |
| `spread` | The spread, for `split`, `analogous` and `doublesplit`. | 10 to 60 |
| `steps` | The steps, for `mono`. | 3 to 9 |
| `mode` | The contrast mode. | `aa` (4.5:1), `ui` (3:1), `aaa` (7:1); leave it out for **As generated** |
| `adjust` | Ticks **Also adjust the base**. | `1` |
| `ctab` | The tab to open on. | `wheel`, `palette`, `preview`, `tokens` |

For example, `?ctool=harmony&color=D3AF37&on=FFFFFF&scheme=triadic&mode=aa&ctab=palette` opens the white-page walkthrough above on **Palette**.

## Accuracy and limits

- **Hues are turned in OKLCH.** Turned colours keep the base's lightness and chroma unless a colour would leave the screen's range, when its chroma is trimmed.
- **Contrast is the WCAG 2 ratio**, rounded down, so a colour shown at 4.50:1 really reaches 4.5:1. A colour walked to 4.5:1 suits normal text on that background only.
- **A grey base has no harmony.** Below an OKLCH chroma of 0.02, every turn lands on the same grey; the verdict says so and suggests **Monochromatic**.
- **Vision simulations are approximations** of full-strength colour-vision deficiency, the same model as the other Colour Tools. Real colour vision varies, and milder forms are more common.
- **Harmony rules are conventions**, not a guarantee of a pleasing result.

## Related

- [Colour Tools documentation](README.md)
- [Open the Colour Tools and work in their panels](launcher-and-panels.md)
- [Colour Tools dashboard](colour-tools-dashboard.md)
- [Palette Studio](../panel-tools/palette-studio.md) — generated palettes with locking and many exports
- [Accessibility Lab](accessibility-lab.md) and [Contrast System](contrast-system.md) — deeper contrast checks
- [Color Psychology](colour-psychology.md) — what the palette tends to signal
- [Gradient Library](gradient-library.md)
- [Library Kit](../../../../../kits/library-kit/README.md) — where saved palettes go
