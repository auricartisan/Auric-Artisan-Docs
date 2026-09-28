---
title: Shareable links — Other link options
description: Add ?lang=, ?color=, ?ctool= or #split= to an address to open a page in a language, inspect a colour, open a Colour Tool with its settings, or restore a split view.
product: Website › Site features › Shareable links
updated: 2026-09-27
---

# Other link options

## Open a page in Hindi or English: `?lang=`

Add `?lang=hi` to any page address to open it in Hindi, or `?lang=en` for English. The browser that opens the link remembers the choice for later visits.

```text
https://auricartisan.com/library/learn/?lang=hi
```

If the address already contains `?`, use `&lang=hi`. See [Language](../../language/README.md).

## Inspect a colour over any page: `?color=`

Add `?color=` and a colour to any page address, and a floating colour inspector opens over that page with a full reading of the colour.

```text
https://auricartisan.com/?color=CEA1B5
https://auricartisan.com/library/palette/?colour=%23d3af37&on=ffffff
```

- **Parameter names:** `color`, `colour` or `hex` for the colour; `on`, `bg`, `against` or `vs` for a background to compare it with; `ctab` for the section to open on (`read`, `contrast`, `vision`, `palette`, `formats` or `about`).
- **Colour formats:** hex with or without `#` (3, 4, 6 or 8 digits; `#` must be written `%23` in an address), a CSS colour name such as `rebeccapurple`, or a CSS colour function such as `oklch(…)`, `lab(…)` or `rgb(…)`.
- **Short or partial hex** still works: `?color=CEA` is read as a colour.
- **Several colours:** separate them with `|` or `;` (or `,` when no colour function is used).
- The inspector reports contrast against the page it opens on, and against any colour you add with `on=`.
- A value the site cannot read still opens the inspector, which says so and offers colours to start from.

The inspector is one of the Colour Tools; see [Color Inspector](../../../tools/colour-workspace/basic-colour-tools/docs/colour-tools/colour-inspector.md).

## Open a Colour Tool with its settings: `?ctool=`

Add `?ctool=` and a tool's id to any page address, and that Colour Tool opens over the page. More keys carry the tool's colours and settings, so the link opens the tool exactly as it was shared. The **Share link** button in every tool's footer makes these links for you.

```text
https://auricartisan.com/?ctool=contrast&on=0F172A&fg=D3AF37,F5F0E6&ctab=fix
https://auricartisan.com/library/?ctool=a11y&colors=FFFFFF,111111,1E40AF,DC2626&std=apca
https://auricartisan.com/?ctool=name&color=goldenrod
```

### Rules for every tool

- **`ctool`** names the tool (see the table below). It is not case-sensitive. An id that is not a tool does nothing.
- **`color`** (or `colour` or `hex`) is the tool's main colour. It accepts every form `?color=` accepts: hex without `#`, a CSS colour name or a CSS colour function.
- **Other colour keys** (`on`, `fg`, `colors`, `stops` and so on) take hex codes of 3 or 6 digits, without `#`. Separate several with commas.
- **`ctab`** opens the tool on a tab. Each tool's first tab is the default.
- **Anything a tool cannot read is ignored,** and the tool uses its default for it.
- The tool does not rewrite the address bar as you work (the Color Inspector is the exception). Use **Share link** to copy a link to what is on screen.

### Keys for each tool

| Tool | `ctool` | Keys | `ctab` |
|---|---|---|---|
| Color Inspector | `inspector` | `color` (required). For comparison colours, use a `?color=` link with `on=`. | `read`, `contrast`, `vision`, `palette`, `formats`, `about` |
| Accessibility Lab | `a11y` | `colors`: 2 to 8 colours, background first. `color`: Colour 1, when there is no `colors`. `std`: `wcag` (default), `apca`, `iso`. `size`: `body` (default), `large`. | `matrix`, `pairs`, `vision`, `preview` |
| Contrast System | `contrast` | `on` (or `bg`): the background. `fg`: 1 to 5 text colours. `color`: Text 1, when there is no `fg`. `size`: `small`, `body` (default), `large`. | `scores`, `size`, `fix`, `preview` |
| Color Name Finder | `name` | `color`: also accepts a name from the dictionary, such as `goldenrod`. | `names`, `neighbours`, `formats` |
| Animation Contrast | `anim` | `color`: the text colour. `th`: `aa` (default), `large`, `aaa`, `lc75`, `lc60`. `src`: `keyframes` (default), `css`, `video`. `stops`: 2 to 8 of `hex@percent`, for example `0F172A@0,F97316@100`. `ease`: `linear`, `ease`, `ease-in`, `ease-out`, `ease-in-out` (default), `steps(4)`. `dur`: 1 to 20 seconds. `blend`: `srgb` (default), `oklab`. `region`: the video's text region as `left,top,width,height` in percent. | `timeline`, `moment`, `fix` |
| Type Readability Sim | `type` | `color`: the text colour. `on` (or `bg`): the background. `font`: `sans` (default), `serif`, `mono`, `thin`, `rounded`. `px`: 10 to 48. `weight`: 100 to 900. `track`: letter-spacing, −0.05 to 0.2 em. `lh`: line height, 1.1 to 2. `cond`: `normal` (default), `v2040`, `v2080`, `glare`, `tired`. `sample`: `body` (default), `ui`, `button`, `long`, `data`. | `verdict`, `sweeps`, `conditions`, `recs` |
| Color Library | `library` | `color`: the working colour. `q`: a search. `fam`: `red`, `orange`, `yellow`, `green`, `cyan`, `blue`, `violet`, `pink`, `brown`, `neutral`. `sort`: `hue` (default), `light`, `name`, `near`. `read`: `white`, `black`, `both`. `page`: a page number. `sel`: the colour shown in Detail, by name in lower case with hyphens, for example `metallic-gold`. | `browse`, `detail`, `families` |
| Color Psychology | `psychology` | `colors`: 1 to 6 colours. `color`: the main colour, when there is no `colors`. `region`: a region for the cultural notes, in lower case with hyphens, for example `china`, `south-africa` or `native-american`. | `mood`, `colours`, `culture`, `pairings` |
| Pantone & Named Lookup | `named` | `color`. `sys`: `all` (default), `css`, `pantone`, `ral`, `ncs`, `crayola`. `chip`: the chip to compare, by name in lower case with hyphens. | `matches`, `compare`, `formats` |
| Harmony Studio | `harmony` | `color`: the base colour. `on` (or `bg`): the background. `scheme`: `complementary`, `split`, `analogous`, `triadic` (default), `tetradic`, `square`, `doublesplit`, `mono`. `spread`: 10 to 60 degrees, for `split`, `analogous` and `doublesplit`. `steps`: 3 to 9, for `mono`. `mode`: a contrast target, `aa`, `ui` or `aaa` (none by default). `adjust=1`: also adjust the base colour to the target. | `wheel`, `palette`, `preview`, `tokens` |
| Gradient Library | `gradients` | `color`: the working colour. `g`: a gradient from the library, by name in lower case with hyphens. `stops`: 2 to 6 colours, each optionally `@percent`, instead of `g`. `kind`: `linear`, `radial`, `conic`. `angle`: degrees. `space`: `srgb`, `oklab` (default), `oklch`. `q`: a search. | `browse`, `edit`, `check`, `export` |
| CMYK Soft-Proof | `softproof` | `color` (default `0085CA`). `press`: `fogra39` (default), `gracol`, `swop`, `fogra52`, `news`, `rag`. `gcr`: `ucr`, `light`, `medium` (default), `heavy`. `comp=0`: turn off dot-gain compensation. | `proof`, `separation`, `chart`, `notes` |
| Color Formulation | `formulation` | `color`. `with`: a pigment the mix must use, for example `cadmium-red-light`, `yellow-ochre`, `ultramarine-blue` or `titanium-white`. `alt`: 1 to 6, the next-best pigment pairs. `ratio`: the first pigment's share, 5 to 95 in steps of 5. | `channels`, `pipeline`, `spectrum`, `mix` |
| Color Space Converter | `spaces` | `color`. `q`: filter the notations, for example `lab` or `p3`. `only`: `css` or `notation`. `probe`: a chroma for the gamut probe, 0 to 0.4. | `spaces`, `gamut`, `channels` |

Older values from earlier versions of the tools still work, for example `std=wcag21` in Accessibility Lab and `th=apca` in Animation Contrast.

A link to an Animation Contrast video check carries the text region, not the video; the person who opens it adds the video again.

For how each tool uses these settings, see [Open the Colour Tools and work in their panels](../../../tools/colour-workspace/basic-colour-tools/docs/colour-tools/launcher-and-panels.md) and the guide for each tool in the same folder.

## Restore a split view: `#split=`

While split view is open, the address holds `#split=` and a description of both panes. Opening that address restores the split. See [Split view › Share a split](../../split-view/docs/share-a-split.md).

## Search: `/search/?q=`

The full search page accepts a query in its address, for example `https://auricartisan.com/search/?q=gamut`. Spotlight's **View all results** uses it. See [Search](../../../search/README.md).
