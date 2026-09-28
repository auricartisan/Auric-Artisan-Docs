---
title: Colour Tools — Open the tools and work in their panels
description: Every way to open the 14 floating Colour Tools, the launcher and its working colour, ?ctool= links, and what every tool panel shares: the header band, tabs, controls, footer, Open in, docking and the phone sheet.
product: Website › Tools › Colour workspace
updated: 2026-09-27
---

# Open the Colour Tools and work in their panels

The Colour Tools are 14 colour tools that open in floating panels over the page you are on. You can check a contrast ratio, name a colour or audit a palette without leaving an article or a tool page: the panel opens on top, you work in it, and you close it when you are done.

This page covers what all 14 tools share: the ways to open them, the **Color Tools** launcher and its working colour, links that open a tool with its settings, and the panel every tool is drawn in. Each tool has its own page in this folder. For the page that gathers your working colour, your colour set and your recent work, see [Colour Tools dashboard](colour-tools-dashboard.md).

## Where the Colour Tools are available

The Colour Tools load on almost every page of the site, a moment after the page has loaded. The Basic Color Tools page (https://auricartisan.com/tool/basic-tools/) is their home page, and the dashboard is at https://auricartisan.com/tool/color-tools/.

A few pages do not load them. On those pages the right-click menu has no **Colour tools** group, and `Ctrl` + `Shift` + `C` takes you to the Basic Color Tools page instead of opening the launcher.

## Ways to open a tool

### From the right-click menu

Right-click anywhere on a page (outside a text field) to open the site's menu. The **Colour tools** row opens a submenu:

| Item | What it opens |
|---|---|
| **All colour tools…** | The launcher, at the place you right-clicked. The row shows the shortcut `Ctrl` + `⇧` + `C`. |
| **Contrast System**, **Accessibility Lab**, **Harmony Studio**, **Color Space Converter**, **Color Name Finder**, **Gradient Library**, **Color Library** | That tool. |

The other seven tools are one step away through **All colour tools…**. To use the browser's own menu instead, hold `Shift` while you right-click.

### Right-click a colour value

When you right-click a colour, the menu header changes to **Colour** and shows the hex code and its RGB value. The menu recognises a colour when you right-click selected text that is a hex code, a swatch the site marks with its colour, or a short piece of text that is only a hex code, such as `#D3AF37`. The colour section offers **Copy HEX**, **Copy RGB**, **Copy HSL**, **Copy OKLCH**, and four tools:

| Item | What it opens |
|---|---|
| **Check its contrast** | Contrast System, with the colour as the first text colour. |
| **Build harmonies** | Harmony Studio, with the colour. |
| **Find its name** | Color Name Finder, with the colour. |
| **Inspect in Colour Tools** | The Color Inspector, with the colour. |

The **Colour tools** row is there too. Every tool you open from it starts with the colour you right-clicked, and **All colour tools…** makes that colour the launcher's working colour.

### The keyboard shortcut

Press `Ctrl` + `Shift` + `C` to open the launcher. It opens where you last right-clicked, or near the top-left corner if you have not right-clicked yet.

If you have text selected that is exactly a hex code (3 or 6 digits, with or without `#`), that colour becomes the working colour, so the tool you pick next opens with it. Select `#1E40AF` in an article, press the shortcut, choose **Contrast System**, and the colour is ready to check.

### A link

Two kinds of link open a tool over any page of the site:

- **`?color=`** opens the Color Inspector on a colour, for example `https://auricartisan.com/?color=CEA1B5`. See [Color Inspector](colour-inspector.md) for its keys.
- **`?ctool=`** opens any of the 14 tools with its colours and settings, for example `https://auricartisan.com/?ctool=contrast&on=0F172A&fg=D3AF37,F5F0E6`. See [A `?ctool=` link](#a-ctool-link) below.

### From the dashboard and from other tools

- The [Colour Tools dashboard](colour-tools-dashboard.md) opens every tool, and reopens tools as you left them.
- Every tool except the Color Inspector has an **Open in another tool** button in its title bar that hands your colours to a related tool. The Inspector has an **Open in another tool** list in its **Read** section instead.
- The Design Engine can open Colour Tools with your system's primary colour. See [Design Engine](../../../design-engine/README.md).

## The working colour

The working colour is the colour every tool opens with when you start it from the launcher or the dashboard. It is shown in the coloured band at the top of the launcher and of the dashboard, with a plain-language name such as "Light soft amber", its hex code and its OKLCH value. Until you change it, it is the site's gold, `#D3AF37`.

The working colour changes when you:

- type a colour in the band's field, pick one from the screen, or select the dice in the launcher;
- choose an action for a colour you typed in the launcher's search (see [Search](#search));
- open the launcher with a colour: select a hex code and press `Ctrl` + `Shift` + `C`, or right-click a colour and choose **All colour tools…**;
- type a colour, or choose a colour of the working set, on the dashboard;
- work in a tool. A moment after you change a tool's main colour, that colour becomes the working colour: for example the selected text colour in Contrast System, **Colour 1** in Accessibility Lab, or the text colour in Type Readability Sim and Animation Contrast. The Color Inspector changes it too.

The working colour is kept in this browser on this device. It is a solid colour: transparency is not kept.

## The launcher

The launcher is a dark card titled **Color Tools**, with the number of tools (**14 tools**) beside the title, the shortcut keys and a close button (×). Below the header are the working colour, a search box and the list of tools.

### The working colour band

The band is painted in the working colour. It shows "Working colour · every tool opens with it", the colour's plain-language name, its hex code and OKLCH value, and a field where you can change it:

- **Type** a hex code (with or without `#`), a CSS colour name such as `rebeccapurple`, or a CSS colour function such as `rgb(206 161 181)`. The band follows as soon as the text is a complete colour. Text that is not a colour is outlined in red, and the band keeps the last colour.
- **Pick** a colour from anywhere on your screen with the pen-shaped button (in browsers that support it).
- **Roll** the dice ("Try a random, well-balanced colour") for a random colour of medium lightness and chroma.

### Search

The search box says "Search tools, or type a colour or a task" and has focus when the launcher opens. Press `/` to return to it from anywhere in the launcher.

- **Search by name or task.** The search matches tool names, the line under each name and a list of task words, so `print`, `apca`, `mood`, `video` or `pantone` finds the right tool. The heading says how many tools match, for example "2 tools match “apca”", and a row found by a task word says so ("matches “apca”"). Each row shows its group on the right.
- **Paste or type a colour.** When the search box holds a colour, the launcher offers actions for it under **Do something with #0F4C81**:

| Action | What it does |
|---|---|
| **Inspect #0F4C81** | Opens the Color Inspector with it. The line underneath gives its plain-language name. |
| **Check #0F4C81 as text on #F5F0E6** | Opens Contrast System with it as text on the house paper (`#F5F0E6`) or the house navy (`#0F172A`), whichever reads better. The line gives the ratio and says whether that is "readable as body text", "large text only" or "not readable as text". |
| **Find the name of #0F4C81** | Opens Color Name Finder with it. |
| **Build harmonies from #0F4C81** | Opens Harmony Studio with it. |
| **Make #0F4C81 the working colour** | Sets it as the working colour and clears the search. |

Each of the first four actions also makes the colour the working colour. Tools whose names contain what you typed are listed below the actions.

If nothing matches, the launcher says "No tool matches “zzz”. Try a task — contrast, print, gradient, name, mood — or paste a hex."

### Pick up where you left off

With the search box empty, the first section lists the last three tools you used, newest first, "Kept on this device". Each row shows a strip of the colours you were using, the tool's name, a line describing what you were doing (for example "Triadic from #D3AF37 · 3 colours") and how long ago: "Just now", "5 min ago", "2 h ago", "Yesterday", "3 days ago" or a date. Select a row to reopen the tool with the same colours, settings and tab.

Until you have used a tool, the section says "Tools you open show up here, with what you were doing in them." The Color Inspector is not listed here.

### The tool list

Below that, the 14 tools are listed in four groups. Each row has a small mark drawn in the working colour, the tool's name and a line on what it answers.

| Group | Tools |
|---|---|
| **Essentials** · Check and read | **Color Inspector** (Everything about one colour), **Accessibility Lab** (Audit a palette for readability), **Contrast System** (Is this text readable?), **Color Name Finder** (Name any colour), **Animation Contrast** (Text on moving backgrounds), **Type Readability Sim** (Is this type comfortable?) |
| **Explore** · Names and meaning | **Color Library** (Browse 1,055 named colours), **Color Psychology** (What a palette signals), **Pantone & Named Lookup** (Nearest Pantone, RAL, NCS) |
| **Design** · Make and prepare | **Harmony Studio** (Palettes from one colour), **Gradient Library** (Find, tune and check gradients), **CMYK Soft-Proof** (Preview a colour on press) |
| **Deep dive** · How colour works | **Color Formulation** (How it is built, and mixed), **Color Space Converter** (34 notations, one colour) |

Select a tool to open it with the working colour. Opening a tool closes the launcher.

### Keyboard

The footer repeats the keys: "Arrow keys move · Enter opens · Esc clears, then closes".

| Key | What it does |
|---|---|
| `↓` / `↑` in the search box | Moves the highlight through the rows, wrapping round at the ends. |
| `Enter` in the search box | Opens the highlighted row. |
| `Esc` in the search box | Clears the search. Press it again, with the box empty, to close the launcher. |
| `/` | Moves to the search box. |
| `Tab` / `Shift` + `Tab` | Moves between the fields, the rows, the footer links and the close button. |
| `Esc` elsewhere | Closes the launcher. |

Typing in the launcher never sets off the site's own keyboard shortcuts.

### Moving and closing

- **Move:** drag the launcher by its header.
- **Close:** select ×, press `Esc`, click anywhere outside the launcher, or open a tool.

The footer has two links: **All tools**, the site's full list of tools, and **Colour dashboard**, which opens the [Colour Tools dashboard](colour-tools-dashboard.md).

On a phone, the launcher rises from the bottom of the screen as a sheet, lists the tools in one column and leaves out the keyboard hints.

## A `?ctool=` link

Add `?ctool=` and a tool's id to the address of any page on the site, and that tool opens over the page. Further keys carry the tool's colours and settings, so a link can open a tool exactly as someone left it.

```text
https://auricartisan.com/?ctool=contrast&on=0F172A&fg=D3AF37,F5F0E6&ctab=fix
https://auricartisan.com/library/?ctool=name&color=goldenrod&ctab=neighbours
```

| Tool | Id |
|---|---|
| Color Inspector | `inspector` |
| Accessibility Lab | `a11y` |
| Contrast System | `contrast` |
| Color Name Finder | `name` |
| Animation Contrast | `anim` |
| Type Readability Sim | `type` |
| Color Library | `library` |
| Color Psychology | `psychology` |
| Pantone & Named Lookup | `named` |
| Harmony Studio | `harmony` |
| Gradient Library | `gradients` |
| CMYK Soft-Proof | `softproof` |
| Color Formulation | `formulation` |
| Color Space Converter | `spaces` |

- **`color`** (or `colour` or `hex`) is the tool's main colour. It accepts anything `?color=` accepts: a hex code without `#`, a CSS colour name, or a CSS colour function.
- **Other colour keys**, such as `on`, `fg` or `colors`, take hex codes of 3 or 6 digits without `#`. Separate several with commas.
- **`ctab`** opens the tool on one of its tabs.
- A value the tool cannot read is ignored, and the tool uses its default instead. An id that is not a tool does nothing.
- `?ctool=inspector` needs a `color`. For comparison colours in the Inspector, use a `?color=` link.

Every key for every tool is listed in [Other link options](../../../../../site-features/shareable-links/docs/other-link-options.md).

The easiest way to make one of these links is **Share link** in the tool's footer. The Color Inspector keeps the address bar in step with what you see; the other tools leave the address bar as it was, so use **Share link** to copy a link to what is on screen now.

## The panel

Every tool opens in the same kind of floating panel. The chrome is dark and neutral in both site themes, so the colours you are studying are the only colours on the panel.

From top to bottom a panel has:

1. **The title bar**: the tool's name, its link on wider panels, and the panel buttons.
2. **The header band**: the colours under study, painted, with one or two lines that sum up the result. Tools about one colour (Color Inspector, Color Name Finder, Color Space Converter, Color Formulation, Pantone & Named Lookup) show a large specimen with the colour field in it instead; on every tab but the first it folds to a strip.
3. **The tabs**: three or four sections (six in the Color Inspector).
4. **The controls rail** (the wider tools): the colours and settings, on the left. On a panel narrower than about 720 pixels, the rail moves above the results.
5. **The results** for the tab you are on. Each tab starts with one to three plain sentences that give the answer, then the detail.
6. **The footer**: a gold copy button, **Share link**, a save button and **Export**.

### The title bar

The title bar shows the tool's name and, when the panel is wider than about 620 pixels, the link that describes what you are looking at, for example `?ctool=contrast&on=0F172A&fg=D3AF37,F5F0E6,765A0B`. On a narrower panel the link is hidden; **Share link** still copies it.

| Button (tooltip) | What it does |
|---|---|
| Chain ("Link — sync controls with other linked panels") | Turns linking on or off for this panel. |
| Two squares ("Open another instance of this simulation") | Opens a second copy of this tool, offset slightly from the first. |
| Pin ("Pin — prevent auto-replacement when over the panel limit") | Keeps the panel open when the panel limit is reached. |
| Arrow out of a box ("Open in another tool") | Opens a menu of related tools. Not on the Color Inspector. |
| Split rectangle ("Dock to the right edge") | Docks the panel. See [Docking](#docking). |
| Dash ("Minimize to dock") | Hides the panel. Bring it back from its tab on the control bar. |
| Square ("Maximize / restore") | Fills the browser window, leaving a small margin. Select it again to go back. |
| Cross ("Close") | Closes the panel. |

**Linking.** When two or more panels are linked, changing a control in one changes the matching control in the others. This is most useful with two copies of the same tool.

### Open in another tool

**Open in another tool** drops a menu under the title bar. Each item names a tool and says what it will do with what you have now, for example, from Contrast System: **Accessibility Lab** — "Audit #0F172A and all 3 text colours as one set". Select an item to open that tool with those colours and settings. A line at the top of the results confirms it, for example "Opening Color Inspector with #1E40AF…".

If that tool is already open, its panel comes to the front and switches to what you handed over, instead of opening a second copy.

In the menu, `↑` and `↓` move between items, `Home` and `End` jump to the ends, and `Esc` closes the menu without closing the panel.

### Docking

**Dock to the right edge** pins the panel to the full height of the right edge of the window, so you can keep using the page beside it. Tools about one colour dock 560 pixels wide; the wider tools dock 880 pixels wide (never wider than the window). A docked panel cannot be dragged or resized, and docking a maximised panel restores it first.

Select the button again (its tooltip now says **Undock** and the tool's name) to put the panel back where it was. Each tool remembers whether you left it docked.

### The footer

| Button | What it does |
|---|---|
| Gold copy button | Copies the tool's main result. Its label says what: **Copy report** in Accessibility Lab, **Copy CSS** in Contrast System, **Copy name** in Color Name Finder, **Copy hex** in the Color Inspector, and so on. It shows **Copied** for a moment. |
| **Share link** | Copies the current page's address with `?ctool=`, the tool's settings and, unless you are on the first tab, `ctab` for the tab you are on. It shows **Link copied**. |
| Save (**Save audit**, **Save check**, **Save setting**, **Save colour** …) | Saves what you are looking at to your Library, with a name and a short summary. |
| **Export** | Opens a menu above the footer. Each item has a one-line preview. Select one to copy it (the item shows **Copied**) or download it (**Downloaded**). `↑`, `↓`, `Home`, `End` and `Esc` work as in the Open in menu. |

A short message at the bottom of the screen confirms each copy, download and save, for example "CSS copied" or "Saved to your library". If the Library is not available on the page, the message says "The library isn’t available on this page".

Each time you select the save button it saves what is on screen at that moment and says **Saved** for a moment. Change something and select it again to save the new state as well.

On a narrow panel, **Share link**, the save button and **Export** show as icons; screen readers still hear their names.

### Moving, resizing and focus

- The first time a tool opens, it appears at the right of the window: 880 by 860 pixels for the wider tools, 560 by 860 for tools about one colour (560 by 880 for the Color Inspector), or smaller if the window is smaller. After that, each tool reopens at the size and position you last gave it.
- Drag the title bar to move a panel. You cannot drag a maximised or docked panel.
- Double-click the title bar to maximise or restore.
- Drag the corner handle at the bottom right to resize. A panel is at least 520 by 420 pixels on a computer, and it always stays inside the browser window.
- Click anywhere in a panel to bring it to the front.
- `Esc` closes the panel that has focus, or leaves full-window view first if it is maximised. In a menu, `Esc` closes only the menu, and in Color Library's search it clears the search first.

While a tool loads, the panel shows its name and a progress bar. If a tool cannot open, the panel says "Couldn't open" with a short reason.

### How many panels can be open

Up to five panels can be open at once. If you open a sixth, the oldest panel that is not pinned closes to make room. If all five are pinned, the new tool does not open until you unpin or close one.

Opening a tool that is already open brings its panel to the front. When you open it with a colour, from the launcher, the dashboard, **Open in another tool** or a link, the open panel switches to that colour. Tools that hold a list of colours keep the list: Accessibility Lab puts the new colour in **Colour 1**, Contrast System in the selected text colour, and Color Psychology in **Colour 1**. A link that names a whole list replaces it. Use the two-squares button when you want two copies side by side.

### On a phone

On a screen up to 600 pixels wide, a tool opens as a sheet from the bottom of the screen, full width and up to nine-tenths of the screen high, instead of a window. The title bar keeps only **Open in another tool** and **Close** (the Color Inspector keeps only **Close**). The header band and tabs sit at the top, the controls come before the results, and the footer shows the gold copy button with its label and the other three as icons.

## The control bar

While at least one panel is open, a slim bar appears at the bottom-right of the window. Drag it by the dotted handle at its left end to move it; its position is remembered.

| Part (tooltip) | What it does |
|---|---|
| Grid ("Tile in a grid") | Tiles the panels to fill the window. |
| Split ("Split left and right") | Places the panels side by side at full height. |
| Split ("Split top and bottom") | Stacks the panels at full width. |
| Cascade ("Cascade with an offset") | Gives each panel the same size and staggers them. |
| Stack ("Stack them centred") | Centres every panel in the same place. |
| Panel tabs | Select a tab to bring that panel to the front, restoring it if minimised. Small icons show whether it is pinned, synced, minimised or maximised. |
| Count | How many panels are open out of five, for example `2/5`. |
| Three dots ("More panel actions") | **Sync all panels** (or **Unsync all panels**), **Minimize all**, **Restore all**, **Export a comparison PNG**, **Open the verification panel** and **Close all but pinned**, which asks "Close all unpinned floating panels?" first. |

The same bar serves the Vision Simulation panels. **Export a comparison PNG** and **Open the verification panel** are built for those: with Colour Tools panels, the PNG shows only each panel's name. On a phone the bar shows only the panel tabs, the count and the three dots.

## What all 14 tools share

- **Colour fields.** A swatch, a text box and, where the browser supports it, a pen-shaped button that picks a colour from anywhere on your screen. Some fields also have a dice button for a random colour. The text box accepts a hex code (3, 4, 6 or 8 digits, `#` optional), a CSS colour name or a CSS colour function, and the tool follows as soon as the text is a complete colour. Press `Enter` to also accept a fragment of a hex code, such as `CE`. Text that is not a colour is outlined in red, and the tool says "That isn’t a colour yet. Try a hex like D3AF37, a CSS name, or rgb()." When you leave the field, it goes back to the colour in use. Transparency in a colour you type is ignored.
- **Answers first.** Each tab opens with one to three sentences that give the result in words, then the numbers.
- **Live results.** There is no "calculate" button. Every change updates the panel at once, and a short line at the top of the results confirms actions such as adding, removing or swapping a colour.
- **Tap to copy.** Value tiles, format rows and names copy when you select them, and show **Copied** for a moment.
- **Tabs by keyboard.** With a tab focused, `←` and `→` move to the previous or next tab (wrapping round), and `Home` and `End` jump to the first and last.
- **One set of measures.** Every tool rounds WCAG ratios down to two decimals and cuts APCA Lc towards zero, so a value never reads as a level it misses: 4.497:1 shows as 4.49:1, and Lc −59.99 as Lc −59. The colour-vision simulations use the same model in every tool.
- **Kept on this device.** The working colour, what each tool was last doing, your recent activity and the working set are kept in this browser only; see [Colour Tools dashboard](colour-tools-dashboard.md). Each tool also remembers its size, position, pin and dock state.
- **Everything runs in your browser.** Colours, images and videos you use in the tools are not uploaded.

## Tips and limits

- To keep a tool's exact state, use **Share link** or the save button. Reopening a tool from the launcher starts it again from the working colour.
- The Color Inspector appears in **Pick up where you left off** and in the dashboard's recent activity like every other tool, and changes the working colour as you inspect.
- A `?ctool=` link for a video check in Animation Contrast carries the text region, not the video: add the video again after opening it.

## Related

- [Colour Tools documentation](README.md) — the contents of this folder
- [Colour Tools dashboard](colour-tools-dashboard.md) — the working colour, working set, sessions and recent activity
- [Other link options](../../../../../site-features/shareable-links/docs/other-link-options.md) — every `?ctool=` key
- [Basic Color Tools](../../README.md)
- The Essentials: [Color Inspector](colour-inspector.md), [Accessibility Lab](accessibility-lab.md), [Contrast System](contrast-system.md), [Color Name Finder](colour-name-finder.md), [Animation Contrast](animation-contrast.md), [Type Readability Sim](type-readability-sim.md)
- The other tools: [Color Library](colour-library.md), [Color Psychology](colour-psychology.md), [Pantone & Named Lookup](pantone-and-named-lookup.md), [Harmony Studio](harmony-studio.md), [Gradient Library](gradient-library.md), [CMYK Soft-Proof](cmyk-soft-proof.md), [Color Formulation](colour-formulation.md), [Color Space Converter](colour-space-converter.md)
- [Right-click menu](../../../../../site-features/context-menu/README.md)
