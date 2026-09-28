---
title: Gradient Library — Find, tune, check and export gradients
description: Search 512 gradients by name, colour word or hex, edit any of them as a linear, radial or conic gradient blended in sRGB, OKLab or OKLCH, check text contrast across the width, and export CSS, Tailwind, SVG, JSON or PNG.
product: Website › Tools › Colour workspace
updated: 2026-09-27
---

# Gradient Library

The Gradient Library is a collection of 512 ready-made gradients that you can search, tune, check and export. You can find a gradient by name, by a colour word such as "blue", or by a hex code, which ranks every gradient by how close its nearest stop is. You can then change its type, angle, stops and blend, see where a blend turns muddy, check whether white or black text stays readable across it, and export it as CSS, a CSS variable, a Tailwind class, SVG, JSON or a PNG. You can also build a new gradient from any colour.

Gradient Library is in the launcher's **Design** group. It opens in a floating panel over the page you are on; for moving, docking and closing panels, see [Open the Colour Tools and work in their panels](launcher-and-panels.md).

For a full-page gradient editor, see [Gradient Maker](../panel-tools/gradient-maker.md). For the site's gradient collections, see [Colour libraries](../../../../../library/colour-libraries/README.md).

## How to open it

- **Launcher:** press `Ctrl` + `Shift` + `C` (or right-click the page and choose **Colour tools** › **All colour tools…**), then select **Gradient Library**.
- **Right-click menu:** **Colour tools** › **Gradient Library**.
- **From another Colour Tool:** Harmony Studio's **Open in another tool** menu opens it with a blend from the base into the next colour; Color Space Converter's opens it with a two-stop gradient blended in OKLCH.
- **A link:** add `?ctool=gradients` to any page address, with the keys under [Links](#links).

When you open it from the launcher or the [Colour Tools dashboard](colour-tools-dashboard.md), the [working colour](launcher-and-panels.md#the-working-colour) goes into the search box: every gradient is ranked by its nearest stop to that colour, and the closest one becomes the current gradient. Opened with no colour, the current gradient is **Trio Complement #065**.

If the Gradient Library is already open and you open it again with a colour, it searches for that colour and switches to the closest gradient. A gradient you have edited is never replaced this way: the search updates and your edit stays open.

The gradients download the first time you open the tool. Until they arrive, the tabs say "Loading the gradient library…".

## Screen tour

The panel has the shared Colour Tools layout: the current gradient painted across the top, four tabs, a controls rail on the left, the selected tab on the right and a row of actions at the bottom. [Open the Colour Tools and work in their panels](launcher-and-panels.md) describes the parts every tool shares, including the title bar, **Open in another tool**, **Dock** and the bottom sheet on phones.

### The gradient band

The current gradient fills the top of the panel, drawn as it is set in **Edit**.

- **A card** gives its type, angle, blend, number of stops and scheme, for example "Linear · 90° · OKLab · 3 stops · Complement", then its name and its stops with their positions, for example "#005449 0% · #E64887 33% · #FFCCED 100%".
- **A working-colour tag** shows the working colour and how far it is from the gradient's nearest stop, for example "Working #D3AF37 · nearest stop ΔE 46.4".
- **A tag for each stop** sits along the bottom edge at the stop's position.

### The controls rail

- **Search by name or colour.** A search box with the hint "Sunset, blue or #D3AF37". The note under it changes with what you type (see [Browse](#browse)).
- **Scheme.** **All schemes** or one of the seven schemes, each with its number of gradients.
- **Stops.** **Any**, **2**, **3** or **4**.
- A note: "Search and filters work on Browse; changing one opens it."
- **Working colour.** A colour field, with a picker button in browsers that support it.
- **Recipe.** How to build a gradient from the working colour: **Tint ramp · dark to light**, **Analogous · ±35°** or **Complement · across the wheel**. A note says what the recipe will make.
- **Start from** the working colour, for example **Start from #D3AF37**, builds that gradient and opens **Edit**.

On a narrow panel or a phone, the rail moves above the results.

## Browse

**Browse** is the tab that opens first.

- **The verdict** says what you are looking at:
  - with no search or filter: "The library holds 512 gradients in 7 schemes, with 2 to 4 stops.";
  - with filters: for example "18 of the 512 are 3-stop Sunset gradients.";
  - with words: for example "224 of the 512 gradients match “blue”, by name or by a blue stop.";
  - with a hex: for example "Ranked by the nearest stop to #D3AF37: the closest is Quad Mix Complement #099, whose stop #D8AA31 sits ΔE 3.0 away (close)."
- A note says the cards are drawn in the blend chosen in **Edit**.
- **Cards**, twelve to a page. Each shows the gradient, its name, and its number of stops, scheme and angle; after a hex search, also the distance of its nearest stop. The current gradient's card is marked. Select a card to make it the current gradient.
- **The pager.** **Previous**, a **Page** box you can type into, the page count and the number of gradients, and **Next**.

When nothing matches, the tab says so and offers **Clear search and filters**.

### How search works

| You type | What happens |
|---|---|
| A hex code: six digits with or without `#`, or three digits with `#` | Every gradient that fits the filters is ranked by ΔE2000 from that colour to its nearest stop. |
| A colour word | Gradients whose name contains the word, or with a stop of that colour. The words understood are pink, red, orange, amber, yellow, green, cyan, teal, blue, violet, purple, magenta, brown, wine, grey, gray, black and white. |
| Any other text | Gradients whose name contains it. |

With several words, a gradient must match every one of them.

### The collection

| Scheme | Gradients |
|---|---|
| Analogous | 76 |
| Complement | 76 |
| Triadic | 72 |
| Tetradic | 72 |
| WarmCool | 72 |
| Sunset | 72 |
| Mono | 72 |

By stops, 128 gradients have two, 128 have three and 256 have four. Names follow the pattern *Duo Analogous #001*, *Trio Complement #065* or *Quad Mix Complement #099*.

## Edit

**Edit** changes the current gradient. Changing the type, angle or stops of a library gradient renames it with **· edited**, for example "Trio Complement #065 · edited". Changing the blend does not.

- **The verdict** finds the pair of neighbouring stops whose plain sRGB blend loses the most colour at its midpoint, and compares the three blends there, for example "Between #005449 and #E64887 a plain sRGB blend goes grey: its midpoint drops to C 0.062, 54% below the ends. OKLab keeps C 0.065 (53% dip); OKLCH keeps C 0.106 by turning the hue 180° through soft brown." A second sentence says whether the blend you are using is the cleanest of the three, or which would keep more colour.
- **Type.** **Linear**, **Radial** or **Conic**.
- **Interpolation.** The blend: **sRGB** (what browsers do with plain hex stops; complementary stops pass through grey), **OKLab** (even lightness steps and less mud) or **OKLCH** (keeps chroma by travelling round the hue wheel the shorter way). The blend also changes how the cards on **Browse** are drawn.
- **Angle.** 0° to 360° in steps of 5°. For **Conic** it is the **Start angle**; **Radial** does not use it.
- **Stops**, with a count such as "3 of 6". Each stop has a colour field, a position slider from 0% to 100% and a **×** that removes it (a gradient keeps at least two stops).
- **Add stop** puts a stop in the widest gap, coloured as the blend already is there, so the gradient looks the same until you change it. Up to six stops.
- **Reverse** flips the gradient.
- **Back to** the library gradient (for example **Back to Trio Complement #065**) undoes every edit and returns to the last library gradient you had. It reads **Reset**, unavailable, while there is nothing to undo.
- **Same stops, three blends.** The gradient drawn in **sRGB**, **OKLab** and **OKLCH**, each with its worst dip; the one in use is marked.
- **Chroma along the gradient · OKLCH C.** A chart of how vivid the gradient is from 0% to 100% in each blend: dashed for sRGB, solid for OKLab, dotted for OKLCH, with the blend in use drawn brightest and thin lines at the stops.
- **Muddy-midpoint check · midpoint chroma vs the ends.** One row per pair of neighbouring stops, with the midpoint colour and its chroma dip in each blend, and a reading for the blend in use: **Holds colour** (dip under 10%), **Dulls a little** (10% to 25%), **Turns muddy** (25% to 45%) or **Goes grey** (45% or more). Near-grey stops read **Grey ends**.

The dip is how far the midpoint's OKLCH chroma falls below the average of its two stops.

### Build a gradient from a colour

Under **Working colour**, choose a **Recipe** and select **Start from**:

| Recipe | What it builds |
|---|---|
| **Tint ramp · dark to light** | Three stops at the colour's hue: darker, the colour itself in the middle, then lighter. |
| **Analogous · ±35°** | Neighbouring hues 35° either side of the colour, slightly darker and lighter, with the colour in the middle. |
| **Complement · across the wheel** | Two stops: the colour, then the hue opposite it on the OKLCH wheel at the same lightness. |

The new gradient is linear at 135° and is named, for example, "From #D3AF37 · analogous". Until you edit it, it follows the working colour and the recipe: change either and the gradient is rebuilt. A colour with almost no hue gives greys, and the note suggests the tint ramp instead.

## Check

**Check** tests white and black text across the gradient.

- **The verdict** says, for the chosen line and size, where each ink passes, for example "On the middle line at 4.5:1, white text passes at 25% of the width, failing from 25% to 100%; black text passes at 75%, failing from 0% to 25%." The second sentence recommends an ink that passes everywhere, or, when neither does, the lightest scrim (a translucent black or white layer behind the text) that would let each ink pass, for example "A 46% black scrim lets white text pass everywhere; a 22% white scrim does the same for black."
- **Text line.** **Top**, **Middle** or **Bottom** of the banner.
- **Text size.** **Body · 4.5:1** or **Large · 3:1**.
- **The banner.** The gradient drawn at 1200 × 400 with "White text" and "Black text" samples and a dashed line where the text sits.
- **One section per ink**, **White text · ratio at 20 points** and **Black text · ratio at 20 points**, each with a reading: **Passes everywhere**, **Fails everywhere** or **Passes** and a percentage. Bars show the ratio at 20 points along the line against the target, a strip shows the ink over each point, the failing stretches are marked, and a sentence gives the lowest (or best) ratio and where it is. Point at a bar to see its position, colour and ratio.

## Export

- **The verdict** describes the gradient and what each format does with the blend, for example "Linear gradient, 3 stops, blended in OKLab. The CSS says “in oklab” and carries a baked fallback; SVG and PNG bake the blend into 17 stops because they only blend in sRGB."
- **Format switch.** **CSS**, **Variable**, **Tailwind**, **SVG** or **JSON**, with the code below and a **Copy** button for that format.
- **Download PNG** and **Download SVG** save a 1280 × 320 image.
- A note on how the SVG matches the CSS for the gradient's type.
- **Stops · tap to copy.** One tile per stop with its position, hex and OKLCH values. Select a tile to copy its hex.

## Walkthroughs

### Find gradients that suit a brand colour

1. Type your colour into the search box, for example `#D3AF37`.
2. Read the verdict: it names the gradient whose stop is closest.
3. Narrow the list with **Scheme** or **Stops** if you like; the ranking stays.
4. Select a card to make it the current gradient.

### Stop a gradient going muddy

1. Choose a gradient whose ends are far apart on the colour wheel, such as **Trio Complement #065**.
2. Open **Edit** and read the verdict and the **Muddy-midpoint check**. In sRGB the first pair **Goes grey**.
3. Under **Interpolation**, select **OKLCH**. The reading for that pair becomes **Dulls a little**, and the band shows the new blend.

### Put a headline on a gradient

1. Open **Check**, choose the **Text line** where your headline sits and the **Text size**.
2. If one ink **Passes everywhere**, use it. If not, add the scrim the verdict suggests behind the text, or use large text.

### Export the gradient for a stylesheet

1. Open **Export** with **CSS** selected, or select **Copy CSS** in the footer.

For **Trio Complement #065** blended in OKLab, the CSS reads:

```css
.trio-complement-065 {
  /* Fallback for browsers without “in oklab”: the same blend baked into 17 stops. */
  background-image: linear-gradient(90deg, #005449 0%, #385750 4.2%, … #FFCCED 100%);
  background-image: linear-gradient(90deg in oklab, #005449 0%, #E64887 33.3%, #FFCCED 100%);
}
```

Browsers that understand `in oklab` use the second line; others keep the first, which draws the same blend.

## Controls

| Control | What it does | Values or range | Default |
|---|---|---|---|
| **Search by name or colour** | Filters or ranks **Browse**. | Free text, colour words or a hex | Empty, or the colour you opened with |
| **Scheme** | Filters **Browse**. | **All schemes** and 7 schemes | **All schemes** |
| **Stops** | Filters **Browse**. | **Any**, **2**, **3**, **4** | **Any** |
| **Working colour** | The colour for recipes and the nearest-stop tag. | Hex, CSS names, CSS colour functions | The working colour, or `#D3AF37` |
| **Recipe** | The gradient **Start from** builds. | 3 recipes | **Analogous · ±35°** |
| **Start from** | Builds a gradient from the working colour. | — | — |
| Cards | Make a gradient current. | 12 per page | — |
| Pager | Moves between pages. | **Previous**, **Page**, **Next** | Page 1 |
| **Type** | Linear, radial or conic. | 3 types | **Linear** |
| **Interpolation** | The blend. | **sRGB**, **OKLab**, **OKLCH** | **OKLab** |
| **Angle** / **Start angle** | The direction or start of the gradient. | 0° to 360°, steps of 5° | The gradient's own angle |
| Stop colour and position | Change one stop. | Any colour; 0% to 100% | — |
| **Add stop**, **Reverse**, **×** | Add, flip or remove stops. | 2 to 6 stops | — |
| **Back to** … / **Reset** | Returns to the last library gradient, without edits. | — | — |
| **Text line** | Where **Check** samples. | **Top**, **Middle**, **Bottom** | **Middle** |
| **Text size** | The target on **Check**. | **Body · 4.5:1**, **Large · 3:1** | **Body · 4.5:1** |
| Format switch | The code shown on **Export**. | **CSS**, **Variable**, **Tailwind**, **SVG**, **JSON** | **CSS** |
| Tabs | Switch the view. | **Browse**, **Edit**, **Check**, **Export** | **Browse** |

## Outputs and exports

The footer holds **Copy CSS**, **Share link**, **Save gradient** and **Export**.

| Output | Format | What it contains |
|---|---|---|
| **Copy CSS** / **CSS** | CSS rule | A class named after the gradient with `background-image`. For OKLab and OKLCH it has two lines: a fallback with the blend baked into extra stops, then the gradient with `in oklab` or `in oklch`. |
| **CSS variable** | CSS | `--gradient-` plus the name on `:root`, and an example `.hero` rule that uses it. |
| **Tailwind arbitrary value** | Text | A `bg-[…]` class with the gradient, for example `bg-[linear-gradient(90deg_in_oklab,#005449_0%,#E64887_33.3%,#FFCCED_100%)]`. |
| **SVG markup · angle-correct** | SVG text | A 1280 × 320 SVG. A linear gradient follows its angle exactly as CSS does; a radial one is the same ellipse; a conic one is drawn as 120 wedges of 3°, because SVG has no conic gradient. OKLab and OKLCH blends are baked into extra stops. |
| **JSON** | JSON | The name, type, angle (not for radial), interpolation, stops (hex and position from 0 to 1) and the CSS. |
| **PNG · 1280 × 320** / **Download PNG** | PNG download | The gradient as an image, named after the gradient, for example `trio-complement-065.png`. |
| **SVG file** / **Download SVG** | SVG download | The same SVG as a file, for example `trio-complement-065.svg`. |
| **Share link** | A URL | This page with `?ctool=gradients` and the gradient: its library name, or its stops, type and angle once edited, plus the blend, the search, the working colour and the tab. |
| **Save gradient** | An item in your Library | Named after the gradient, with its type, angle, blend, stops and CSS. |

The **Open in another tool** menu offers **Color Inspector**, **Harmony Studio** and **Color Name Finder** (each with the first stop), **Contrast System** (white and black text on the first stop), **Accessibility Lab** (the stops as one palette) and **Animation Contrast** (the stops as a looping animation, with text checked over it).

## Links

| Key | What it sets | Values |
|---|---|---|
| `ctool` | Opens this tool. | `gradients` |
| `g` | A library gradient. | Its name in lower case with hyphens, for example `trio-complement-065` |
| `stops` | A gradient by its stops, instead of `g`. | Two to six hex codes without `#`, separated by commas. Add `@` and a position to place a stop, for example `005449@0,E64887@33.3,FFCCED@100`; without positions the stops are spread evenly. |
| `kind` | The type. | `linear`, `radial`, `conic` |
| `angle` | The angle. | Degrees |
| `space` | The blend. | `srgb`, `oklab`, `oklch` |
| `q` | The search text. | Up to 60 characters |
| `color` | The working colour. | A hex code without `#` |
| `ctab` | The tab to open on. | `browse`, `edit`, `check`, `export` |

A gradient shared by its stops opens as "Shared gradient". If `g` names a gradient the library does not have, the tool says so and shows the default.

## Accuracy and limits

- **Browsers blend in sRGB by default.** OKLab and OKLCH blends need a browser that understands `in oklab` or `in oklch`; the CSS export carries a baked fallback for the others. SVG and PNG always bake the blend into extra stops.
- **The library gradients are starting points.** They were generated from colour-scheme rules and are not checked for text contrast. Use **Check** before you put text on one.
- **Check samples one line.** It tests 20 points along the chosen line of a 1200 × 400 banner. Text elsewhere, or on a different shape, meets different colours.
- **Ratios are WCAG 2**, rounded down. A scrim suggestion assumes a flat translucent layer behind the whole line.
- **Network.** The library downloads from the site the first time you open the tool. If it cannot load, the tool says so and you can still build a gradient from the working colour.

## Related

- [Colour Tools documentation](README.md)
- [Open the Colour Tools and work in their panels](launcher-and-panels.md)
- [Colour Tools dashboard](colour-tools-dashboard.md)
- [Gradient Maker](../panel-tools/gradient-maker.md)
- [Animation Contrast](animation-contrast.md) — text over a moving gradient
- [Contrast System](contrast-system.md)
- [Harmony Studio](harmony-studio.md)
- [Library Kit](../../../../../kits/library-kit/README.md) — where saved gradients go
