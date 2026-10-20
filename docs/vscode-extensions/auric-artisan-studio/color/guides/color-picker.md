---
title: Auric Color — The colour pickers
description: Use Auric Color's three pickers (inline in the hover, the full panel beside the editor, and the docked sidebar view) to edit colours in your code.
product: VS Code extensions › Auric Artisan Studio › Auric Color
updated: 2026-09-25
---

# The colour pickers

Auric Color gives you three ways to edit a colour in your code. All three write the change straight into the file, in the colour's own format, as an edit you can undo.

| Picker | Where | Best for |
| --- | --- | --- |
| Inline hover picker | Inside the colour hover | Quick changes without leaving the code |
| Picker panel | A tab beside the editor | Precise editing, contrast checks, generating sets, rewriting every match |
| Color Picker view | Docked in the sidebar | Keeping a picker open while you move between colours |

## The inline hover picker

Point at a colour (or click it) and use the **Spectrum**, **Hue**, **Alpha**, **Shades**, **Fix**, **Brand** and **Recent** rows at the top of the hover. Each tile applies its colour and the hover reopens on the new value. **Type exact…** takes a typed value. See [Hover and swatches](hover-and-swatches.md#picker-rows).

## Open the picker panel

- Put the cursor on a colour (or select one) and press `Ctrl` + `Alt` + `C` (`Cmd` + `Alt` + `C` on macOS), or run **Auric Artisan: Pick / edit color**. It is also on the editor's right-click menu.
- Select **Spectrum picker** in a colour hover.
- Click a colour literal when `auricColor.colorPicker.clickAction` is `fullEditor`, or when the colour hover is turned off.
- Select **Open the color picker** on the Overview, or **Open full** in the docked view.
- Select a colour in the Command Center's **Recent colors**.

The panel opens beside your editor, titled **Auric Artisan — Color Picker**, with the heading **Color picker** and the line **Edit, convert, test contrast, and generate accessible color systems.**

If the cursor is not on a colour, the picker starts from Auric gold, `#D3AF37`, and the colour you apply is inserted at the cursor.

The first time you pick a colour while VS Code's own colour decorators are still on, Auric Color may ask **Auric Artisan can replace VS Code's native color picker with its own. Turn off the native color decorators?** with **Use Auric Artisan picker**, **Keep native** and **Don't ask again**. See [Picker modes](picker-modes.md).

## The docked Color Picker view

Expand **Color Picker** in the sidebar (collapsed by default). It is the same picker in a narrower layout. While it is visible and no picker panel is open:

- **Pick / edit color** and clicking a colour load that colour into the docked picker instead of opening a panel;
- applying a colour writes to that token, or inserts at the cursor if no colour was targeted.

The **↗** button at the top and **Open full** at the bottom open the picker panel.

## Picker controls

| Control | What it does |
| --- | --- |
| Spectrum | Drag, or use the arrow keys, to set saturation (across) and brightness (down) |
| Hue bar | Drag or use the arrow keys to set the hue |
| Opacity bar | Drag or use the arrow keys to set transparency |
| Preview | The current colour |
| **⊙** eyedropper | Picks a colour from anywhere on screen, where the system supports it; otherwise shows **Eyedropper unavailable here** |
| Format tabs | `hex`, `rgb`, `hsl`, `hsv`, `oklch`, `lch`: the input fields and the written format |
| **Copy** | Copies the current value |
| Value fields | Type values in the chosen format; the colour updates as you type |
| **Apply to all N matches in file** | Appears when the colour occurs more than once in the file; when ticked, every literal of the same colour is rewritten, each in its own format |
| **Best text** | Sets the colour to black or white, whichever reads better on it |
| **Done** (panel) or **Open full** (docked view) | Closes the panel, or opens the full panel |

The picker starts in the token's own format when it is one of the six. **HSV** is not a CSS format, so choosing it writes hex.

### Contrast section

Check the colour against a background:

- choose white or black with the chips, or type any background colour;
- read the ratio and APCA Lc, and the **AA**, **Large** and **AAA** badges (✓ or ✕);
- **Fix → AA** and **Fix → AAA** adjust the colour's lightness until it reaches 4.5:1 or 7:1 on that background, keeping its hue. A toast says **Nudged to passing**, or **Couldn't reach target** when no shade of that hue can get there.

### Generate section

Choose **Shade ramp** or a harmony (**Complementary**, **Split complement**, **Analogous**, **Triadic**, **Tetradic**, **Square**, **Double split**, **Monochromatic**) to see a set of colours based on the current one. Select a tile to apply it. **Copy** copies the set as CSS custom properties, for example `--shade-500: #4581FF;` or `--triadic-2: …;`, and **Insert** types them at the editor cursor.

### Accessibility section

Titled with the nearest colour name, for example **Accessibility · royalblue**. It shows the contrast on white and on black (coloured as pass, large-text pass or fail), APCA Lc on white and on black, relative luminance, and the colour difference to the named colour (**ΔE→name**).

### Brand and recent section

A search box (**Search 140+ named colors or a hex…**) that shows up to 28 matching CSS colour names, or the colour you typed; the nine brand swatches; and your recent picks in this picker (up to 14). Select any swatch to apply it.

Each section can be collapsed with its heading; the picker remembers which you collapsed.

## When changes are written

- Dragging writes when you release the pointer.
- Selecting a swatch, a tab or a fix writes immediately.
- Typing in a value field writes as the value becomes valid.
- Keyboard changes on the bars and spectrum write after a short pause (about 0.6 seconds).

Each write is a separate edit you can undo with `Ctrl` + `Z`. The picker never writes to a file outside your workspace or a file that is not open.

## Pickers inside the Studio

Colour fields in the Studio (for example the Contrast Studio's **Text** and **Background**, or the Palette's **Seed**) have their own swatch button that opens a pop-up version of the picker: spectrum, hue and opacity bars, eyedropper, formats, copy, accessibility figures, brand and recent swatches, **Best text** and **Done**. It edits the Studio field, not your code.

## Related

- [Picker modes](picker-modes.md)
- [Hover and swatches](hover-and-swatches.md)
- [Reference](reference.md)
