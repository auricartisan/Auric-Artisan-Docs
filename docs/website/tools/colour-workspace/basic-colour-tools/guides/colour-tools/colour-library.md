---
title: Color Library — Browse 1,055 named colours
description: Browse the 1,055 named colours by name, hex, family, readability or nearness to your working colour, open any colour in full detail with its contrast, notations, triadic harmony and similar colours, and add colours to your working set.
product: Website › Tools › Colour workspace
updated: 2026-09-27
---

# Color Library

Color Library lets you browse the dictionary of 1,055 named colours that the Colour Tools use. You can search by name or by hex code, filter by hue family and by whether a colour can carry body text on white or black, and sort by hue, lightness, name or nearness to your working colour. Open any colour for its full detail: key values, contrast on white and black, 20 notations, a triadic harmony with a name for each colour, and the 12 most similar names.

It shares its dictionary and its family rule with the [Color Name Finder](colour-name-finder.md), so a name's family is the same in both tools, and it shares the working set with the [Colour Tools dashboard](colour-tools-dashboard.md).

Color Library is in the **Explore** group of the Colour Tools. It opens in a floating panel; for the panel, its footer and its links, see [Open the Colour Tools and work in their panels](launcher-and-panels.md).

## Open it

- **Launcher:** press `Ctrl` + `Shift` + `C`, then select **Color Library**.
- **Right-click menu:** **Colour tools** › **Color Library**.
- **From another tool:** **Open in another tool** › **Color Library** in the Color Name Finder, which opens the colour's family sorted nearest first.
- **A link:** `?ctool=library`, for example `https://auricartisan.com/?ctool=library&fam=blue&sort=near&color=1E40AF`. See [Link keys](#link-keys).

The colour you open it with becomes the library's **Working colour**; with no colour, it is the site's gold, `#D3AF37`. The dictionary downloads the first time you open the tool, and the panel says "Loading 1,055 named colours…" until it arrives.

## Screen tour

### The header band

On **Browse** and **Families** the band describes the list you are looking at, for example "All 1,055 named colours" or, with the **Red** family chosen, "118 red colours", with the page and the sort ("Page 1 of 44 · sorted by hue"). Beside it, a stripe shows the current list in hue order, with a marker and a tag where your working colour falls.

On **Detail** the band is painted in the selected colour. It shows the family and hue, the name, the hex code and OKLCH value, and two samples of the colour as text: on white and on black, each with its ratio and grade.

### The controls rail

| Control | What it does |
|---|---|
| **Search names or hex** | Filters the list as you type. Part of a name finds every name containing it. A hex code such as `#DAA520` or `DAA520` ranks every colour by ΔE2000 from it instead. Three bare hex digits, such as `dda`, stay a text search, because they are also letters in names; type `#dda` to rank by colour. `Esc` clears the search. |
| **Family · one OKLCH rule** | **All** or one of ten families: **Red**, **Orange**, **Yellow**, **Green**, **Cyan**, **Blue**, **Violet**, **Pink**, **Brown**, **Neutral**. Each shows how many colours it has in the current search. |
| **Readable as body text** | **On white · 4.5:1** and **On black · 4.5:1**: keep only colours that reach 4.5:1 as text on that background. Each shows its count. |
| **Sort** | **Hue** (OKLCH hue from red round to pink, then neutrals light to dark), **Lightness, light to dark**, **Name, A to Z**, or **Nearest to working colour**. While you search by hex, the list is ranked by ΔE2000 instead. |
| **Working colour** | The colour the list is measured against for **Nearest to working colour**. A note gives its nearest name and ΔE. |
| **Working set** | The colours in your working set, as swatches. Select one to open it in **Detail** (or its nearest name, if it is not in the dictionary). **Copy 6 hex** copies them all; **Reset** puts the house colours back. |

On **Detail**, the search, family, readability and sort controls rest, with a note, "Back to browse to filter", and a **Back to browse** button.

Ticking both **On white** and **On black** leaves only mid-tones: a colour's ratios on white and on black always multiply to 21, so both reach 4.5:1 only between 4.50:1 and 4.67:1.

## The tabs

### Browse

The opening sentence describes the list and how many of its colours carry body text, for example "All 1,055 colours, sorted by hue. 369 of them carry body text on white and 700 on black (4.5:1)." When you search by hex, it names the nearest instead: "The nearest is Goldenrod (#DAA520), ΔE 0.0: imperceptible." A line under it counts the colours and says which are on this page.

The list shows 24 cards a page. Each card has the swatch, the name and a detail line: the hex code and family, the lightness when sorted by lightness, or the ΔE when ranked by colour. Select a card to open it in **Detail**.

Each card also has a **…** button (**More actions for …**) with a menu:

| Item | What it does |
|---|---|
| **Copy hex** | Copies the hex code. |
| **Download SVG** / **Download PNG** | Downloads a 512 × 512 swatch, named after the colour, for example `metallic-gold.png`. |
| **Open in Spaces** | Opens the Color Space Converter with the colour. |
| **Find name** | Opens the Color Name Finder with the colour. |
| **Open Accessibility** | Opens Accessibility Lab with the colour between white and black. |
| **Open Psychology** | Opens Color Psychology with the colour. |

In the menu, `↑`, `↓`, `Home` and `End` move, and `Esc` closes it.

Under the cards, **Previous** and **Next** turn the page, and you can type a page number. If nothing matches, the tab says so and offers **Clear filters**.

### Detail

One colour in full: the one you selected, or, until you select one, the name nearest your working colour.

The opening sentences place it and say where it reads as text, for example "Metallic Gold (#D4AF37) is in the Yellow family, at OKLCH lightness 0.77 and chroma 0.139." and "As text it belongs on black, at 9.98:1 (AAA); on white it reaches only 2.10:1, so keep it off white for text."

- **Moving through the list:** **Back to browse**, the previous and next arrows, and where it sits, for example "326 of 1,055 in the list". **Add to working set** adds it to your working set (it then reads **In working set**; select it again to take it out).
- **Key values · tap to copy:** **Name**, **Hex**, **Family**, **OKLCH**, **HSL**, and **Temperature · hue** (**Warm**, **Cool**, **Balanced**, or **None** for a neutral).
- **As text on white and black:** a card for each background with the ratio and grade (**AAA**, **AA**, **Large only** or **Fail**), the APCA Lc and its level, and what the colour can be used for there: "Any text, even small print.", "Body text and everything larger.", "Large text, icons and UI parts only." or "Decoration only, not text."
- **Every notation · tap to copy:** the same 20 notations as the Color Name Finder, from **HEX** to **Linear sRGB**, then the nearest **CSS keyword**, a **Custom property** named after the colour, and its **Name**. Each row is marked **CSS** or **Notation**.
- **Harmony · triadic, each with its nearest name:** the colour and the colours 120° and 240° round the OKLCH hue wheel at the same lightness, each matched to its nearest name, with its ΔE and **Open** to show that name here. A neutral turns onto itself, and the tool says so rather than invent a harmony.
- **12 similar colours · by ΔE2000:** the nearest other values, as cards with the same menu as **Browse**.

### Families

The ten families across the whole dictionary. The opening sentences give the largest and the smallest, for example "1,055 names in 10 families. Neutral is the largest, with 165; Cyan the smallest, with 41."

**Ten families · whole dictionary** has a row for each family: its count and share, a stripe of its colours in hue order, its lightness range, and **Browse**, which shows that family on **Browse**.

**The rule, in OKLCH** sets out how every name gets exactly one family:

- **Neutral:** chroma under 0.035, whatever the hue.
- **Brown:** hue 15° to 110° with lightness under 0.60 and chroma under 0.15, or chroma under 0.09 and lightness under 0.80.
- **Pink:** hue 330° to 15°, plus pale soft reds (lightness over 0.80, chroma under 0.10).
- **Red** 15° to 45°, **Orange** 45° to 80°, **Yellow** 80° to 120°, **Green** 120° to 175°, **Cyan** 175° to 225°, **Blue** 225° to 285°, **Violet** 285° to 330°.

**About the dictionary** says what the data holds: 1,058 entries, of which three are listed twice with the same name and value (Neon Blue, Neon Yellow and Neon Red) and appear once, leaving 1,055; 961 distinct hex values, so 83 values carry two or more names, such as Firebrick and Wildfire at `#B22222`.

## Walkthroughs

### Find a named colour

1. Type part of the name in **Search names or hex**, for example `teal`.
2. Narrow it with a **Family** if you need to.
3. Select a card to open it in **Detail**.

### Find the named colours nearest to yours

1. Type your hex code in **Search names or hex**, for example `#1E40AF`. The list is ranked by ΔE2000 from it.
2. Or set **Working colour** and choose **Nearest to working colour** in **Sort**, which keeps the ranking while you filter by family or readability.

### Find text colours for a white page

1. Tick **On white · 4.5:1**.
2. Pick a **Family**. Every card left can carry body text on white.

### Collect colours for a project

1. Open a colour in **Detail** and select **Add to working set**. The set holds up to eight colours.
2. Check the set together on the [Colour Tools dashboard](colour-tools-dashboard.md), or copy it with **Copy … hex** in the rail.

## Controls

| Control | Values or range | Default |
|---|---|---|
| **Search names or hex** | Text or a hex code | Empty |
| **Family** | **All** and 10 families | **All** |
| **Readable as body text** | **On white · 4.5:1**, **On black · 4.5:1** | Off |
| **Sort** | 4 orders | **Hue** |
| **Working colour** | Any colour | The colour you opened with, or `#D3AF37` |
| Page | 24 colours a page | 1 |

## Outputs and exports

| Output | Format | What it contains |
|---|---|---|
| Gold button on **Browse** and **Families** (**Copy 1,055 hex**) | Text | The hex codes of every colour in the current list, one per line. |
| Gold button on **Detail** (**Copy hex**) | Text | The selected colour's hex code. |
| **Hex · Metallic Gold** | Text | The selected colour's hex code. |
| **SVG swatch · 512 × 512** / **PNG swatch · 512 × 512** | File | A square of the selected colour, named after it. |
| **Add to working set** / **Remove from working set** | — | Adds or removes the selected colour. The set keeps two to eight colours. |
| **Current list · CSV** | CSV | `name,hex,family,oklch_l,oklch_c,oklch_h` for every colour in the current list. |
| **Current list · JSON** | JSON | A link to the current view, the count, and each colour's name, hex and family. |
| **Save colour** | A colour in your Library | The selected colour, named with its name and hex, with its family and its ratios on white and black. |
| **Share link** | URL | `?ctool=library` with the working colour and any search, family, sort, readability filter, page and selected colour. |

**Open in another tool** offers, for the selected colour: **Color Space Converter**, **Color Name Finder**, **Accessibility Lab** (against white and black), **Color Psychology**, **Pantone & Named Lookup** and **Color Inspector**.

## Link keys

| Key | What it sets | Values |
|---|---|---|
| `color` (or `colour`) | The working colour. | A colour |
| `q` | The search. | Text, or a hex code |
| `fam` | The family. | `red`, `orange`, `yellow`, `green`, `cyan`, `blue`, `violet`, `pink`, `brown`, `neutral` |
| `sort` | The sort. | `hue` (default), `light`, `name`, `near` |
| `read` | The readability filter. | `white`, `black`, `both` |
| `page` | The page. | 2 or more |
| `sel` | The colour shown in **Detail**. | Its name in lower case with hyphens, for example `metallic-gold` |
| `ctab` | The tab to open on. | `browse` (default), `detail`, `families` |

## Accuracy and limits

- **Terms.** *ΔE2000*: the CIEDE2000 colour difference; under about 1, two colours look the same side by side. *OKLCH*: a colour model whose lightness, chroma and hue change evenly to the eye. *APCA Lc*: a newer measure of perceived lightness contrast.
- **Names are names, not standards.** The dictionary gathers common colour names; the same value can carry several names. For print and paint systems, use [Pantone & Named Lookup](pantone-and-named-lookup.md).
- **Families follow one rule,** so a colour whose name says "pink" can sit in **Red**, and a dark "gold" in **Brown**.
- **Readability is WCAG body text only.** The filters and the **As text** cards use the 4.5:1 level on pure white and pure black. Check your real background in [Contrast System](contrast-system.md).
- **The harmony turns hue only.** Chroma is trimmed where sRGB cannot hold it, and each turned colour is matched to its nearest name, which may be some way off.
- **CMYK is a naive split,** not a press conversion.

## Related

- [Colour Tools documentation](README.md)
- [Open the Colour Tools and work in their panels](launcher-and-panels.md)
- [Colour Tools dashboard](colour-tools-dashboard.md) — the working set
- [Color Name Finder](colour-name-finder.md) — name any colour from the same dictionary
- [Pantone & Named Lookup](pantone-and-named-lookup.md)
- [Color Psychology](colour-psychology.md)
- [Basic Color Tools](../../README.md)
