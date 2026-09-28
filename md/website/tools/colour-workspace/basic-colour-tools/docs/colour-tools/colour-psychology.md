---
title: Color Psychology — What a palette tends to signal
description: Read the mood, warmth and energy of one to six colours, what each colour tends to suggest, cultural notes by region and what every pair of colours says, then copy it all as a brief.
product: Website › Tools › Colour workspace
updated: 2026-09-27
---

# Color Psychology

Color Psychology reads what a palette of one to six colours tends to signal. It works out how warm and how energetic the palette feels, which emotions and personality traits its colours share, what each colour's family is associated with, what the colours can mean in different regions and traditions, and what each pair of colours says together, including whether the pair can carry text.

Everything it shows is an association, not a fact, and the tool says so on every screen. Use it to prepare a brief, to start a design review, or to find questions to test with the people you are designing for.

Color Psychology is in the launcher's **Explore** group. It opens in a floating panel over the page you are on; for moving, docking and closing panels, see [Open the Colour Tools and work in their panels](launcher-and-panels.md).

## How to open it

- **Launcher:** press `Ctrl` + `Shift` + `C` (or right-click the page and choose **Colour tools** › **All colour tools…**), then select **Color Psychology**.
- **From another Colour Tool:** Harmony Studio's **Open in another tool** menu has **Color Psychology**, which opens it with the whole harmony as the palette.
- **A link:** add `?ctool=psychology` to any page address, with the keys under [Links](#links).

Opened from the launcher or the [Colour Tools dashboard](colour-tools-dashboard.md), it takes the [working colour](launcher-and-panels.md#the-working-colour) as **Colour 1**. The two other starting colours, house navy `#1D2A3E` and paper `#F5F0E6`, keep their places, so the palette always has pairs to read. With no colour at all, the palette is `#D3AF37`, `#1D2A3E` and `#F5F0E6`.

If Color Psychology is already open and you open it again with a colour, that colour becomes **Colour 1** and the rest of your palette stays as it was. A link that names a whole palette replaces it.

## Screen tour

The panel has the shared Colour Tools layout: the palette painted across the top, four tabs, a controls rail on the left, the selected tab on the right and a row of actions at the bottom. [Open the Colour Tools and work in their panels](launcher-and-panels.md) describes the parts every tool shares, including the title bar, **Open in another tool**, **Dock** and the bottom sheet on phones.

### The palette band

The top of the panel shows every colour in the palette.

- **Colour 1** fills the widest block. Its small heading gives its role, family and hex, for example **Colour 1 · Yellow · #D3AF37**. Below it is the reading of the whole palette, such as "Balanced, moderate-energy palette — honest, upbeat", and a line with the number of colours, the palette's warmth and its energy, for example "3 colours · warmth +5 · energy +25".
- Every other colour has its own block with its role, its family and its hex. A family followed by **· deep** or **· pale** means the colour is dark or light enough to shift its reading (see [How a colour is read](#how-a-colour-is-read)).

The reading always has the same shape: **Warm**, **Cool** or **Balanced**; then *high-energy*, *calm* or *moderate-energy*; then the two personality traits the palette leans on most.

### The controls rail

- **Colours**, with a count such as **3 of 6**. One colour field per colour, labelled **Colour 1** to **Colour 6**. Each field has a swatch, a text box, a dice button that tries a random colour and, when there is more than one colour, a **×** button that removes it.
- **Add colour** adds a random colour at the end. It is unavailable at six colours.
- **Random** replaces every colour at once. A note explains the range it picks from: pleasant colours in OKLCH, with lightness 0.55 to 0.80, chroma 0.09 to 0.17 and any hue.
- **Cultural notes from** chooses the region or tradition shown on **Culture**: **All regions**, or one of 17 regions. The note under the list says how many of the 17 have notes on your palette.
- A reminder: "Associations, not facts. What a colour signals shifts with culture, context and personal history, so treat every reading here as a prompt to test with real people, not a rule."

A colour field accepts a hex code (with or without `#`), a CSS colour name or a CSS colour function such as `rgb(206 161 181)`. The tool follows as you type whenever the text is a complete colour. If you press `Enter` on something that is not a colour, the field is outlined in red and a message says "That isn't a colour yet".

On a narrow panel or a phone, the rail moves above the results.

## Mood

**Mood** reads the palette as a whole.

- **The verdict.** Up to three sentences:
  - how warm and how energetic the palette is, for example "The palette leans neither warm nor cool (warmth +5) with moderate energy (+25).";
  - which colour pulls it warmest and liveliest and which cools and calms it, for example "Colour 1 (Yellow) pulls it warmest and liveliest; Colour 2 (Blue, deep) cools and calms it.";
  - which words two or more colours share: "the threads that tie the palette together". With one colour, this line says that counts appear once there are two or more colours.
- **Warmth** and **Energy** meters. Each runs from −100 to +100: **Cool −100** to **+100 Warm**, and **Calm −100** to **+100 Vivid**. A dot marks each colour, a white bar marks the palette mean, and dashed lines mark −30 and +30. The value and a reading sit above each meter, and a sentence below explains the reading.
- **Emotions · how many colours carry each.** Up to ten emotion words, each with a count such as "2 of 3". Words shared by two or more colours are highlighted and come first.
- **Personality traits · shared ones first.** Up to fourteen trait words, counted the same way.
- **What each colour adds to the mean.** A table with each colour's family, warmth and energy, and a **Palette mean** row at the bottom.

| Mean | Warmth reading | Energy reading |
|---|---|---|
| Above +30 | **Warm**: "the palette reads inviting and close" | **High energy**: "it stimulates and asks for attention" |
| −30 to +30 | **Balanced**: "neither warmth nor coolness dominates" | **Moderate energy**: "it holds attention without shouting" |
| Below −30 | **Cool**: "the palette reads calm and considered" | **Low energy**: "it settles and recedes" |

Both meters use the same ±30 threshold.

## Colours

**Colours** gives one card per colour.

- **The verdict** names the families in the palette, for example "3 colours from 3 families: Yellow, Blue and White.", and then says which colours are deep, pale or neutral, and what that does to their reading.
- **Each card** shows:
  - the role and hex, and the family in large type;
  - a plain-language description with the OKLCH values, for example "Light soft amber · OKLCH 0.77 0.138 92°";
  - **Warmth** and **Energy** tags with the colour's own numbers (the numbers the meters average);
  - a note on lightness, for example "Mid lightness (L 0.77): the Yellow reading applies as it is.";
  - **Emotion**, **Personality** and **Brand fit**;
  - **Copy reading**, which copies the card as one line of text.

### How a colour is read

The tool puts each colour into one family by its OKLCH hue, chroma and lightness:

| Family | OKLCH hue |
|---|---|
| **Red** | 12° to 42° |
| **Orange** | 42° to 78° |
| **Yellow** | 78° to 118° |
| **Lime** | 118° to 138° |
| **Green** | 138° to 175° |
| **Teal** or **Cyan** | 175° to 235° (Teal when darker, Cyan when lighter) |
| **Blue** | 235° to 285° |
| **Purple** | 285° to 318° |
| **Magenta** | 318° to 345° (dark magentas count as Purple) |
| **Pink** | 345° round to 12° (dark pinks count as Red, very light reds as Pink) |

A colour with OKLCH chroma under 0.03 is a neutral, named **Black**, **Grey** or **White** by its lightness. Very dark colours also count as **Black**.

Lightness then shifts the family's reading:

- **Pale** (OKLCH lightness 0.86 or more): "Soft" and "Calming" lead the emotions, energy falls by 40, and the traits gain "gentle" and "airy".
- **Deep** (lightness 0.36 or less): "Serious" and "Grounded" lead the emotions, energy falls by 30, warmth is scaled to 70%, and the traits gain "intense" and "deep".
- **Neutrals** take no shift: their family already is a lightness.

Two colours in the same family, at the same lightness band, get the same reading.

## Culture

**Culture** lists what the palette's families can mean by region or tradition.

- **The verdict** says how many of the 17 regions have notes on the palette's families. The second sentence lists every **ritual or mourning** note by family and region, for example "White in Western, China, India and Japan", and advises checking them before wedding, funeral or memorial work.
- **One table per family**, headed with its swatches and the colours in it, for example **Yellow · Colour 1**. The columns are **Region**, **Positive**, **Caution** and **Ritual & mourning**. A dash means the data has no note there.

Mourning, funerals, weddings and other rites always sit in **Ritual & mourning**, never in **Positive** or **Caution**.

The regions are Africa, Buddhism, China, Egypt, Hindu, India, Ireland, Islam, Japan, Korea, Middle East, Native American, Netherlands, South Africa, Thailand, Tibetan and Western. The data mixes countries with traditions and lists them as it has them. Which regions appear depends on the family: most families have a Western note, and some have only that one.

Choose a region under **Cultural notes from** to show only that region. The verdict then says how many of the palette's families have a note there, and names any that do not.

## Pairings

**Pairings** reads every pair of colours in the palette: three pairs for three colours, fifteen for six.

- **The verdict** counts the pairs that can carry body text, those for large text and interface parts only, and those for decoration only, and names the strongest and weakest pair with their contrast ratios.
- **Each pair** shows:
  - two samples, each colour as text on the other;
  - the families, for example **Yellow + Blue**, and the two colours;
  - the WCAG contrast ratio and a grade: **AAA** (7:1 or more), **AA** (4.5:1), **Large only** (3:1) or **Fail**;
  - a sentence on what the pair tends to say, built from its temperature, how far apart the hues are, the lightness step between the colours and each colour's leading trait. For example: "Warm against cool; near-complementary hues 167° apart, though the muted one keeps the tension low. A strong light–dark step (ΔL 0.48) makes the pair read crisp and decisive. Upbeat meets reliable.";
  - what the pair can be used for: "Carries body text either way round, even small print (AAA).", "Carries body text either way round (AA).", "Large text, icons and UI parts only, not body copy." or "Decoration only: too close in lightness to carry text."

With one colour, **Pairings** asks you to add another.

## Walkthroughs

### Write a mood brief for a brand palette

1. Open Color Psychology and type your main brand colour into **Colour 1**.
2. Type your other colours into **Colour 2** and **Colour 3**, and select **Add colour** for each further one, up to six.
3. Read **Mood**: the reading in the band, the two meters and the shared words.
4. Select **Copy brief**.

The clipboard now holds a Markdown brief with the palette, its reading, its warmth and energy, a line per colour, every pairing and the cultural notes. It ends with the reminder that these are associations, not facts.

### Check a palette for one market

1. Enter your palette.
2. Under **Cultural notes from**, choose the region, for example **Japan**.
3. Open **Culture**. Read the **Caution** and **Ritual & mourning** columns for each family.

If the verdict says the data has no note there for a family, choose **All regions** to see the notes it does have, and check with people who know that market.

### Find which colours can carry text

1. Enter the palette and open **Pairings**.
2. Read the verdict: for the starting palette it says "3 pairs: 2 can carry body text and 1 is decoration only."

Keep the pairs marked **Decoration only** for fills, borders or illustration, never for text.

## Controls

| Control | What it does | Values or range | Default |
|---|---|---|---|
| **Colour 1** to **Colour 6** | Set each colour. | Hex, CSS names, CSS colour functions | `#D3AF37`, `#1D2A3E`, `#F5F0E6`, or the colour you opened with as Colour 1 |
| Dice button | Tries a random colour in that field. | Pleasant OKLCH range | — |
| **×** button | Removes that colour. | At least 1 remains | — |
| **Add colour** | Adds a random colour. | Up to 6 colours | — |
| **Random** | Replaces every colour with a random one. | — | — |
| **Cultural notes from** | Filters **Culture** and the brief's culture section. | **All regions** or one of 17 | **All regions** |
| Tabs | Switch the view. | **Mood**, **Colours**, **Culture**, **Pairings** | **Mood** |
| **Copy reading** | Copies one colour's card as text. | — | — |

## Outputs and exports

The footer holds **Copy brief**, **Share link**, **Save palette** and **Export**.

| Output | Format | What it contains |
|---|---|---|
| **Copy brief** | Markdown | The same text as **Export** › **Markdown brief**. |
| **Share link** | A URL | This page with `?ctool=psychology`, your colours, the region, and the tab you are on. |
| **Save palette** | A palette in your Library | Named with the palette's reading, with its colours, warmth, energy, reading and region. |
| **Markdown brief** | Markdown | A heading, the palette, the reading, warmth and energy, one line per colour (family, emotion, personality, brand fit), every pairing with its ratio and sentence, the cultural notes for the chosen region, and the closing reminder. |
| **JSON** | JSON | `palette`, `reading`, `mood` (warmth, energy and their readings), `colours` (hex, family, lightness shift, OKLCH, warmth, energy, emotion, traits, brand fit), `pairings` (the two colours, ratio and sentence) and `culture` (the region and every note). |
| **Hex list** | Text | The colours, separated by commas. |
| **Copy reading** | Text | One colour: role, hex, family, emotion, personality and brand fit. |

The **Open in another tool** menu in the title bar offers **Harmony Studio** (a harmony from Colour 1), **Accessibility Lab** (all your colours as one set, or Colour 1 against white and black), **Contrast System** (the strongest pair, as text on its background), **Color Library** (named colours in Colour 1's family), **Color Name Finder** and **Color Inspector** (both with Colour 1).

## Links

A link opens Color Psychology over any page with the palette you shared. **Share link** builds it for you.

| Key | What it sets | Values |
|---|---|---|
| `ctool` | Opens this tool. | `psychology` |
| `colors` | The palette. | One to six hex codes without `#`, separated by commas, for example `D3AF37,1D2A3E,F5F0E6` |
| `color` | Colour 1 when there is no `colors` key. The house navy and paper fill Colours 2 and 3. | A hex code without `#` |
| `region` | The region for **Culture**. | The region's name in lower case with hyphens, for example `japan`, `middle-east`, `native-american` |
| `ctab` | The tab to open on. | `mood`, `colours`, `culture`, `pairings` |

For example, `?ctool=psychology&colors=D3AF37,1D2A3E,F5F0E6&region=japan&ctab=culture` opens the starting palette on **Culture**, showing Japan.

## Accuracy and limits

- **Associations, not facts.** The readings summarise common design and marketing associations. They vary between people, generations, industries and contexts, and they change over time. Test them with the people you are designing for.
- **One reading per family.** Every colour in a family gets that family's reading, adjusted only for pale and deep colours. Two quite different blues at mid lightness read the same.
- **Warmth and energy are the data's numbers.** They are scores for the family, not measurements of the colour, and the tool gives no colour temperature in kelvin.
- **Cultural notes are short summaries, not research.** The data covers 17 regions and traditions, unevenly. A missing note does not mean a colour is neutral there.
- **Pair contrast is WCAG 2.** The ratio is the same whichever colour is the text, and the grade applies to text; the samples show both ways round.

## Related

- [Colour Tools documentation](README.md)
- [Open the Colour Tools and work in their panels](launcher-and-panels.md)
- [Colour Tools dashboard](colour-tools-dashboard.md)
- [Harmony Studio](harmony-studio.md) — build the palette you read here
- [Accessibility Lab](accessibility-lab.md) and [Contrast System](contrast-system.md) — check the pairs that carry text
- [Color Library](colour-library.md)
- [Personalization Generator](../../../personalisation-generator/README.md)
- [Library Kit](../../../../../kits/library-kit/README.md) — where saved palettes go
