---
title: Colour Tools dashboard — Your working colour, set and recent work
description: The Colour Tools dashboard gives six instant answers about your working colour, checks a working set of up to eight colours together, reopens tools as you left them, lists all 14 tools and shows what you copied, exported and saved, all kept on your device.
product: Website › Tools › Colour workspace
updated: 2026-09-27
---

# Colour Tools dashboard

The Colour Tools dashboard is one page that gathers what you do in the floating Colour Tools. It shows your working colour with six instant answers about it, checks a small set of colours together, lists each tool as you last left it, and keeps a short history of what you copied, exported, saved and fixed.

Nothing on the dashboard comes from a server. It reads what the Colour Tools have kept in this browser, on this device, and it never sends it anywhere. Another browser, another device or a private window starts empty.

## Open it

- Go to https://auricartisan.com/tool/color-tools/.
- In the Colour Tools launcher, select **Colour dashboard** in the footer. See [Open the Colour Tools and work in their panels](launcher-and-panels.md).

The page needs JavaScript. Without it, it shows a short note and a link to **All tools**.

## Screen tour

The top of the page has the kicker "Your tools & recent activity", the title **Color Tools**, a filter box and **Open the launcher** (with its shortcut, `Ctrl` `Shift` `C`). Below that, on a wide screen:

- **Left column:** the working colour with **Straight to an answer**, the **Working set**, **Pick up where you left off** and **All colour tools**.
- **Right column:** **Set health** and **Recent activity**.

On a narrower screen the two columns stack, and on a phone **Open the launcher** is hidden.

Tools you open from the dashboard float over it like on any other page, and the dashboard updates as you use them, including in other tabs.

## The working colour

The large swatch is painted in the working colour: the colour every tool opens with when you start it from the launcher or the dashboard. It shows "Working colour · every tool opens with it", a plain-language name such as "Light soft amber", the hex code and the OKLCH value.

To change it:

- type in the field: a hex code (with or without `#`), a CSS colour name or a CSS colour function. The page follows as soon as the text is a complete colour; text that is not a colour is outlined in red;
- pick a colour from anywhere on your screen with the pen-shaped button (in browsers that support it);
- select a colour of the working set (see below).

The working colour is shared with the launcher and follows your work in the tools. See [The working colour](launcher-and-panels.md#the-working-colour).

### Straight to an answer

Six cards answer a question about the working colour at a glance. Select a card to open its tool with the working colour.

| Card | What it shows | Opens |
|---|---|---|
| **Color Inspector** | The OKLCH lightness, chroma and hue, for example `L 0.77 · C 0.138 · h 92°`. | The Color Inspector. |
| **Contrast System** | The ratio of the colour as text on the house navy (`#0F172A`) or the house paper (`#F5F0E6`), whichever reads better, and its grade: **AAA**, **AA**, **large only** or **fails**. For example `8.46:1 on #0F172A · AAA`. | Contrast System, on that background. |
| **Color Name Finder** | The nearest of the dictionary's names and how far it is, for example `Nearest name: Metallic Gold · ΔE 0.3`. It says "Finding the nearest name…" while the names load. | Color Name Finder. |
| **Harmony Studio** | A triadic scheme: the colour and the two colours 120° and 240° round the OKLCH hue wheel. | Harmony Studio. |
| **Accessibility Lab** | How the colour looks with deuteranopia (no green-sensitive cones) and how far it moves, for example `Deuteranopia sees #CBB73E · ΔE 4.8`. | Accessibility Lab. |
| **Color Space Converter** | The colour as a CSS Display P3 value, `color(display-p3 …)`. | Color Space Converter. |

## Working set

The working set is a short list of the colours you are working with, from two to eight. "Pick one to make it the working colour; the checks on this page cover the whole set."

Until you change it, the set is the house palette: **Paper** `#F5F0E6`, **Sheet** `#FCF9F2`, **Ink** `#2F2B24`, **House navy** `#1D2A3E`, **Auric gold** `#D3AF37` and **Gold ink** `#765A0B`.

| Control | What it does |
|---|---|
| A swatch | Makes that colour the working colour. The swatch that matches the working colour is outlined. |
| **Add #D3AF37** | Adds the working colour to the set, named with its plain-language name. It reads **In the set** when the colour is already there and **Set is full (8)** when the set holds eight. |
| **Remove** | Takes that colour out of the set. Shown only while the set has more than two colours. |
| **Reset to house palette** | Puts the six house colours back. |

The same working set appears in the Color Library's controls, where **Add to working set** adds the colour you are viewing. See [Color Library](colour-library.md).

## Set health

**Set health** checks every pair of colours in the working set. Its pill counts the pairs that can carry body text, for example **8 / 15 readable**.

- **The summary** says how many pairs reach 4.5:1, names the strongest pair and its ratio, and names the weakest pair that fails even for large text (under 3:1). When a lightness change of the darker colour can fix that pair, it names the nearest readable version, for example "… is the nearest readable house navy."
- **The matrix.** Rows are backgrounds and columns are text. Each cell is painted as that pair and shows its WCAG ratio (one decimal below 10, whole numbers above). The ratio is the same either way round, so each pair is drawn once. A dashed cell fails even for large text.
- **Closest pair by vision type.** For protanopia, deuteranopia, tritanopia and achromatopsia, the two colours of the set that come closest when simulated, with their ΔE2000 and a verdict: **Hard to tell apart** (under 5), **Close — add labels** (5 to 10) or **Distinct** (10 or more).
- **Open the full audit in Accessibility Lab** opens [Accessibility Lab](accessibility-lab.md) with the whole set, the first colour as the background.

## Pick up where you left off

"Each tool reopens as you left it." The dashboard lists up to eight tools you have used, newest first. Each card shows a strip of the colours you were using, the tool's name, how long ago, a line on what you were doing (for example "#D3AF37 on #0F172A · 8.46:1 · body text") and **Resume**. Select a card to reopen the tool with the same colours, settings and tab.

Until you use a tool, the section says "Tools you open show up here, with what you were doing in them — reopen any of them exactly as you left it." The Color Inspector is not listed.

## All colour tools

All 14 tools in their four groups, **Essentials**, **Explore**, **Design** and **Deep dive**, "each opens as a floating panel on any page". Each row shows the tool's mark drawn in the working colour, its name, and either when you last used it ("Used 5 min ago") or the line on what it answers. Select a row to open the tool with the working colour.

The filter box at the top of the page ("Filter tools by name or task — contrast, print, names…") narrows this list as you type. It matches tool names, what they answer, their task words and group names. The heading then says how many match, for example "2 of 14 match “apca”", and a group with no match says "No match here."

## Recent activity

The last twelve things you did in the Colour Tools, newest first: copies, exports, downloads, saves to your Library, colours added to the working set, and fixes you applied, such as a **Use** button in Accessibility Lab or Contrast System, or a recommendation in Type Readability Sim. Each line says what happened, in which tool and how long ago, with a swatch of the colour involved.

Until there is something to show, it says "Copies, exports, saves and fixes from any colour tool show up here." The footer says "Kept on this device only". **Clear history** empties the list.

Copies and exports in the Color Inspector are not recorded here.

## Walkthroughs

### Check a brand palette at a glance

1. Remove the house colours you do not need, then set the working colour to each of your brand colours in turn and select **Add** after each one.
2. Read **Set health**. The pill and the summary say how many pairs can carry body text, and which pair fails worst.
3. Look down **Closest pair by vision type**. A **Hard to tell apart** pair needs a label, an icon or a pattern as well as its colour.
4. Select **Open the full audit in Accessibility Lab** for every pair ranked, with fixes.

### Carry on from yesterday

1. Open the dashboard.
2. Under **Pick up where you left off**, find the tool by its colour strip and its line, and select it.

The tool opens over the dashboard with the colours, settings and tab you left it on.

## Accuracy and limits

- **Terms.** *WCAG ratio*: the contrast between two colours' relative luminance, from 1:1 to 21:1; 4.5:1 is the level for body text and 3:1 for large text. *ΔE2000*: the CIEDE2000 colour difference; under about 2, two colours look the same side by side.
- **This device only.** Everything is kept in this browser's storage. Clearing the site's data, a private window, or a browser that blocks storage empties the dashboard, and it then shows the house palette and empty lists.
- **What is kept.** One entry per tool (the dashboard shows the latest eight), the last 40 activities (it shows twelve), the working colour and the working set.
- **Set health is a quick check.** It measures WCAG ratios only, for body text. Use [Accessibility Lab](accessibility-lab.md) for APCA, ISO 9241-3, large text and fixes.
- **Vision simulations are approximations** of full-strength colour-vision deficiencies. Milder forms are more common.

## Related

- [Open the Colour Tools and work in their panels](launcher-and-panels.md) — the launcher, the working colour and the panels
- [Accessibility Lab](accessibility-lab.md) — the full audit of a set
- [Color Library](colour-library.md) — add named colours to the working set
- [Colour Tools documentation](README.md)
- [Basic Color Tools](../../README.md)
