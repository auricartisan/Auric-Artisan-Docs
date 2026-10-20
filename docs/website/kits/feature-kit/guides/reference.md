---
title: Feature Kit — Reference
description: Every control, tab, field, option and message in the Feature Kit, with what it does and its default.
product: Website › Kits › Feature Kit
updated: 2026-09-25
---

# Feature Kit reference

Every control in the Feature Kit, grouped by where it appears. Defaults are given where the kit sets one.

## Launcher

| Control | What it does | Default |
|---|---|---|
| **Feature** launcher (nine-dot icon) | Opens the kit on its menu; closes it when open (without Focus mode) | Closed |
| `Ctrl` + `Shift` + `K` | Same as the launcher, from anywhere on the page | — |
| Launcher tooltip | "Calculator, converter, graph tools, and feedback." | — |

## Title bar

| Control | What it does | Values or range | Default |
|---|---|---|---|
| **Back** | Returns to the menu from a tool | Shown only inside a tool | — |
| Title | Shows **Feature Kit** or the open tool's name; drag it to move the kit | — | Bottom-left corner |
| **Graph** | Shows or hides the graph area | Calculator only; gold when on | Off |
| **History** | Shows or hides past calculations | Calculator only; gold when on | Off |
| **Focus mode** | Keeps the kit open across pages and other kits, and stops dimming the page | On or off; remembered | Off |
| **Theme** | Switches the kit between light and dark | Light or dark; remembered | Follows the site |
| **Resize** | Normal (560 px wide) or full size (up to 640 px wide, 900 px tall) | Remembered | Normal |
| **Minimize** | Shrinks the kit to a small round icon; select the icon to reopen at the menu | — | — |
| **Close** | Closes the kit, hides the graph and history, and turns Focus mode off | — | — |

## Menu

| Card | Key | Opens |
|---|---|---|
| **Scientific Calculator** | `1` | [Calculator](calculator.md) |
| **Unit Converter** | `2` | [Unit Converter](unit-converter.md) |
| **Feedback** | `3` | [Feedback](feedback.md) |
| **Notes** | `4` | [Notes](notes.md) |
| **Date & Time** | `5` | [Date & Time](date-and-time.md) |
| **Developer Tools** | `6` | [Developer Tools](developer-tools.md) |

The hint line under the cards reads **1 – 6 Open · Ctrl ⇧ K Toggle** (**⌘** on a Mac).

## Calculator

### Display and entry

| Control | What it does | Default |
|---|---|---|
| Expression line | Shows the expression being entered | Empty |
| Result line | Shows the live result or an error; select it to copy the result | `0` |
| **RAD** / **DEG** | Angle unit for trigonometric functions and the graph; not remembered | **RAD** |
| Expression bar | Type a full expression and press `Enter` | Empty |
| **ƒx** | Shows or hides the function reference chips | Hidden |
| Variables strip | Chips for each defined variable and function, plus **Clear** | Hidden until something is defined |
| **Basic**, **Scientific**, **Programmer** tabs | Switch keypad; which tabs appear depends on the Advanced Kit mode | **Basic** (or **Scientific** in Advanced mode) |

### Memory row

| Key | What it does |
|---|---|
| **MC** | Memory clear (to 0) |
| **MR** | Memory recall: adds the memory value to the expression |
| **M+** | Adds the result line's number to memory |
| **M−** | Subtracts the result line's number from memory |

### Basic keypad keys

**C** (clear), **(**, **)**, **÷**, **×**, **−**, **+**, **0** to **9**, **.**, **=**.

### Scientific keypad keys

| Key | Inserts |
|---|---|
| **d/dx** | `diff(` |
| **∫** | `integral(` |
| **solve** | `solve(` |
| **Σ** | `sum(` |
| **Π** | `product(` |
| **nCr** | `nCr(` |
| **gcd**, **lcm** | `gcd(`, `lcm(` |
| **x̄** | `mean(` |
| **σ** | `stdev(` |
| **sin**, **cos**, **tan** | `sin(`, `cos(`, `tan(` |
| **sin⁻¹**, **cos⁻¹**, **tan⁻¹** | `asin(`, `acos(`, `atan(` |
| **π**, **e**, **φ** | The constant |
| **^** | Power |
| **ln**, **log**, **log₂** | `ln(`, `log(`, `log2(` |
| **√**, **∛** | `sqrt(`, `cbrt(` |
| **exp** | `exp(` |
| Absolute value key (a bar either side of x) | `abs(` |
| **n!** | Factorial sign |
| **%** | Remainder operator |
| **⌫** | Deletes the last character |
| **C** | Clears the expression |
| **Ans** | The previous result |
| Digits, brackets, operators, **.**, **=** | As labelled |

### Programmer keypad keys

| Key | Inserts |
|---|---|
| **AND** | `&` |
| **OR** | The bitwise OR operator |
| **XOR** | `xor(` |
| **NOT** | `not(` |
| **<<**, **>>** | Bit shifts |
| **0x**, **0b** | Hexadecimal and binary prefixes |
| **A** to **F** | Hexadecimal digits |
| **⌫** | Deletes the last character |
| **AC** | Clears the expression |
| Digits, **+**, **−**, **×**, **.**, **=** | As labelled |

### Function reference chips (ƒx)

| Group | Chip | Inserts |
|---|---|---|
| Calculus | **diff(x², at)** | `diff(` |
| Calculus | **diff2** | `diff2(` |
| Calculus | **∫ integral(f, a, b)** | `integral(` |
| Calculus | **solve(f, guess)** | `solve(` |
| Calculus | **Σ sum(f, n, 1, 99)** | `sum(` |
| Calculus | **Π product** | `product(` |
| Statistics | **mean**, **median**, **stdev**, **variance**, **geomean**, **rms** | The function name and `(` |
| Numbers | **gcd**, **lcm**, **isprime**, **nextprime**, **fib**, **nCr**, **nPr** | The function name and `(` |
| Numbers | **roundto(x, digits)**, **nthroot(x, n)**, **logb(x, base)** | `roundto(`, `nthroot(`, `logb(` |
| Define | **x = 5** | `x = ` |
| Define | **f(x) = x^2** | `f(x) = ` |
| Define | **ans** | `ans` |
| Constants | **π**, **e**, **φ**, **τ** | `pi`, `e`, `phi`, `tau` |
| Constants | **c (light)**, **G**, **g₀**, **Nᴀ**, **kʙ** | `c`, `G`, `g0`, `NA`, `kB` |

### Graph area

| Control | What it does | Default |
|---|---|---|
| **y =** box | Expression in `x` to plot; redraws as you type | `sin(x)` |
| Graph canvas | Drag to pan; scroll or pinch to zoom | Centred on the origin, 50 px per unit |
| **Zoom in** | Zooms in one step | — |
| **Zoom out** | Zooms out one step | — |
| **Reset view** | Returns to the starting view | — |

Zoom range: 5 to 5,000 pixels per unit.

### History area

| Control | What it does |
|---|---|
| Entry | Loads that expression and result into the display |
| Bin icon on an entry | **Delete** — removes that calculation |
| Bin icon in the heading | **Clear history** — deletes every calculation, without confirmation |

Up to 100 calculations are kept in your browser. Empty history reads **No calculations yet**.

## Unit Converter

| Control | What it does | Default |
|---|---|---|
| **Search units...** | Narrows the category pills to those with a matching unit name or symbol | Empty |
| Category pills | Choose one of 70 categories | **Length** |
| **From** value box | The number to convert (**Enter value**) | Empty |
| **From** unit list | The unit you have | First unit of the category |
| Swap button | Exchanges the **From** and **To** units | — |
| **To** result | The converted value; select it to copy | — |
| Result sentence | For example `37 celsius = 98.6 fahrenheit` | — |
| **To** unit list | The unit you want | Second unit of the category |
| Unit count | **1344 units available** | — |

## Feedback

| Control | What it does |
|---|---|
| Five faces | **Terrible**, **Bad**, **Okay**, **Good**, **Amazing** (rating 1 to 5) |
| **Tell us more (optional)...** | Comment box, shown after you choose a face |
| **Submit** | Sends quick feedback; disabled until you choose a face |
| **Give Detailed Feedback** | Starts the multi-question form |
| **Not now** | Leaves without sending |
| **← Back**, **Skip**, **Next →** | Move through the detailed form; **Next →** becomes **Submit** on the last question |
| **Done** | Returns to the menu after sending |
| **Try again** or **Check account** | Retries a failed submission |
| **Open form**, **Later** | Buttons on the occasional feedback prompt |

## Notes

| Control | What it does |
|---|---|
| Note tabs | Switch note; each is named after the note's first line |
| **+** (**New note**) | Adds an empty note |
| **Edit** / **Preview** | Switch between editing and formatted preview |
| **Copy** | Copies the note's Markdown |
| **Export** | Downloads the note as a `.md` file |
| **Delete** | Deletes the note without confirmation (empties it if it is the only note) |
| Status line | **Saving…**, **Saved ·** time, **Copied** or **Copy failed** |

## Date & Time

| Tab | Controls |
|---|---|
| **Calendar** | Calendar picker, **Time** box, format rows with **Copy** (**Full (culture)**, **Long date**, **ISO 8601**, **Unix (s)**, **Day of year**, **ISO week**, **Weekday**), **Recent** chips |
| **Difference** | **From** and **To** date fields; results **Days**, **Weeks**, **Months (≈)**, **Years (≈)**, **Business days**, **Hours** |
| **Add / Subtract** | **Start date**, **Amount** (default 30), **Unit** (**days**, **weeks**, **months**, **years**), **Direction** (**after (+)**, **before (−)**) |
| **Timezones** | Live clocks for UTC, New York, Los Angeles, London, Berlin, Kolkata, Tokyo, Sydney |

Calendar picker controls: **‹** previous month, **«** previous year, **»** next year, **›** next month, **Clear**, **Today**.

## Developer Tools

| Tab | Inputs | Buttons |
|---|---|---|
| **JSON** | JSON text | **Format**, **Minify**, **Sort keys**, **→ TypeScript**, **Stats**, **Escape**, **Copy** |
| **Base64** | Text or Base64 | **Encode**, **URL-safe**, **Decode**, **→ Hex**, **Copy** |
| **URL** | URL or text | **Parse**, **Encode**, **Decode**, **Copy** |
| **Hash** | Text; **HMAC key** | **Hash all**, **HMAC-SHA256**, **Copy** |
| **UUID** | **Paste a UUID to inspect…** | **v4**, **v4 ×10**, **v7**, **v7 ×10**, **NIL**, **Copy** |
| **JWT** | Token | **Decode**, **Copy** |
| **Epoch** | Seconds, milliseconds or a date | **Convert**, **Now**, **Copy** |
| **Regex** | Pattern, flags (default `g`), test string, replacement | **Test**, **Copy** |
| **Cron** | Five-field expression (default `*/15 9-17 * * MON-FRI`) | **Explain** and four preset buttons |
| **Text** | Text | **camelCase**, **PascalCase**, **snake_case**, **kebab-case**, **slug**, **Title Case**, **UPPER**, **lower**, **reverse**, **sort lines**, **dedupe lines**, **trim lines**, **Copy** |
| **HTML** | HTML or text | **Encode**, **Decode**, **Strip tags**, **Copy** |

## Messages

| Message | Where | Meaning |
|---|---|---|
| **Copied!** | Calculator, converter | The value is on your clipboard |
| **Copy failed** | Calculator, converter, notes, developer tools | The browser blocked clipboard access |
| **Loading units — Preparing the converter.** | Converter | The unit list is downloading |
| **Units could not be loaded.** | Converter | The download failed; select **Try again** |
| **No matches** | Converter search | No unit name or symbol contains your search |
| **No calculations yet** | History | The history is empty |
| **Date & Time failed to load** (or another tool's name) | Any tool card | The tool could not be downloaded; reload the page |
| **Could not send yet** | Feedback | See [Feedback](feedback.md) |

Calculator error messages are listed in [Troubleshooting](troubleshooting.md).
