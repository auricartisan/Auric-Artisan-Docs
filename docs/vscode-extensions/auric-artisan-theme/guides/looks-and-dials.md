---
title: Auric Artisan Theme — Looks and dials
description: Start from one of 11 looks, then tune the 37 theme dials on the Dials tab, with search, filters and resets.
product: VS Code extensions › Auric Artisan Theme
updated: 2026-09-25
---

# Looks and dials

The theme is generated from a small number of decisions called dials. A **dial** is one setting, such as the accent colour or how strongly panes separate. Change a dial and every colour that depends on it is recomputed, with the contrast guard applied on top. A **look** is a named combination of dial values that you can apply in one click.

Both are available in Theme Studio. Dials are also ordinary VS Code settings under `auricTheme.*`, so you can change them in the Settings editor or in `settings.json`.

## Apply a look

1. Open Theme Studio (`Ctrl` + `Alt` + `;`).
2. Select the **Looks** tab (or press `1`).
3. Under **The set**, select a look.

| Look | What it does |
| --- | --- |
| Signature | The theme exactly as shipped. Applying it clears every dial back to its default. |
| Gallery | Everything turned up: layered surfaces, gold edges, visible controls. Built for demos and projectors. |
| Atelier | Warm, soft and unhurried. Expressive italics, quiet chrome, pastel tokens. |
| Foundry | Monochrome tokens, flat chrome, no ornament. Lightness does all the work. |
| Bullion | One hue, top to bottom. |
| Nocturne | Deeper canvas, dimmer chrome, quieter comments. For working late. |
| Vitrine | Maximum colour separation: vivid tokens, rainbow brackets and guides. |
| Clarity | Accessibility first: maximum text contrast, strong control edges, AAA enforced everywhere. |
| Patina | Aged copper instead of gold, with a cool syntax set to match. |
| Ember | Hot orange accent over a warm syntax set. |
| Sapphire | The classic blue editor, built on Auric surfaces. |

A look is a starting point, not a lock. Everything on the Dials tab layers on top of it, so you can pick a look and keep adjusting. Selecting the same look again puts you back where that look began.

You can also run **Auric Theme: Choose Look…** from the Command Palette, or use the **Look** dropdown in the sidebar.

## Tune dials on the Dials tab

1. Select the **Dials** tab (or press `2`).
2. Dials are grouped into ten cards: **Look**, **Accent**, **Surfaces**, **Text**, **Syntax**, **Editor**, **Workbench**, **Terminal**, **Effects** and **Accessibility**.
3. Change a control. The editor updates while you drag a slider and again when you release it.

Controls come in four kinds:

- **Swatches** for the accent colour: 17 named accents plus **Custom…**.
- **Dropdowns** for choices. Long lists can be searched by typing.
- **Sliders** for numbers. Use the arrow keys for small steps, `Shift` for bigger steps, `Page Up` and `Page Down`, `Home` and `End`, or double-click to reset.
- **Switches** for on and off.

### Find a dial

- Type in **Search dials by name or setting…**. The search matches the dial label, its description and its setting ID, such as `editor.cursor`.
- Use the **Dial visibility** dropdown to switch between **All dials** and **Modified only**.
- A live count, such as "12 dials shown", sits beside the filters.

### See and undo changes

- A dot and a reset button appear beside every dial you have changed. Select the reset button to return that dial to its default.
- Each card has a reset button in its header that resets all dials in that group.
- The footer shows the number of dials and overrides you have changed.

## What each group controls

A summary follows. Every value and default is listed in the [reference](reference.md#theme-dials).

### Accent

- **Accent colour** re-keys the whole theme onto one hue. The rotation happens in OKLCH, so each accent keeps the same visual weight. **Inherit** keeps the variant's own accent.
- **Custom accent** is any hex colour, used only when Accent colour is **Custom**. On light themes it is darkened automatically until it clears your minimum contrast.
- **Accent intensity** (0 to 200) scales every accent-tinted wash, border and selection.
- **Accent the chrome** fills the status bar, activity bar, both, or all three bars with the accent. Labels are recomputed so they stay legible.

### Surfaces

- **Depth** (−4 to 4) sinks every surface towards black (or white on light themes) or lifts them.
- **Warmth** (−100 to 100) tints neutral surfaces towards amber or slate. Text and syntax are not affected.
- **Separation** sets how far apart the editor, sidebar, panel and bars sit tonally.
- **Borders** sets divider strength. Form-control edges are excluded: they always keep their 3:1 minimum.

### Text

- **Text contrast** moves the whole foreground ramp at once.
- **Comment emphasis** makes comments quieter or louder.

### Syntax

- **Syntax palette** reassigns token hues while keeping each role's lightness and chroma, so a palette swap cannot break the contrast audit. Nine palettes are available.
- **Saturation** (0 to 200): 0 gives greyscale tokens.
- **Italics** and **Bold** set how much of the code uses each style. If your font has no true italic, turn italics off.

### Editor

**Cursor**, **Cursor colour**, **Selection strength**, **Current line**, **Bracket pairs**, **Indent guides**, **Whitespace marks** (only visible when VS Code's `editor.renderWhitespace` is on), **Inlay hints** and **Sticky scroll**.

### Workbench

**Active tab** style, **Status bar**, **Activity bar**, **Title bar** (only visible with the custom title bar style), **Side bar** and **Dim unfocused**.

### Terminal

**ANSI palette** (five palettes; all 14 text-bearing ANSI colours stay contrast-audited) and **Terminal background**.

### Effects

**Shadows** and **Focus ring**. There is deliberately no "off" option for the focus ring.

### Accessibility

- **Enforce contrast** (on by default) pushes every colour the customiser produces along its OKLCH lightness until it clears the minimum.
- **Minimum contrast** (3 to 7, default 4.5): 4.5 is WCAG AA for body text; 7 is AAA. It applies to text and syntax, not decorative washes.
- **Audit on apply** (on by default) runs the full contrast audit every time customisations are applied and warns you about failures.

## Quick commands for common dials

| Command | What it does |
| --- | --- |
| **Auric Theme: Choose Accent Colour…** | Pick from the 17 named accents, each shown with its hex value and a hint. |
| **Auric Theme: Choose Look…** | Apply one of the 11 looks. |
| **Auric Theme: Choose Syntax Palette…** | Pick one of the 9 syntax palettes. |
| **Auric Theme: Toggle Italics** | Switch italics between **off** and **standard**. |
| **Auric Theme: Surprise Me** | Clears your dials, then picks a random accent, syntax palette, warmth, separation, bracket style and tab style from curated choices. |

## Edit dials as settings

Dials are standard settings, so you can also set them in `settings.json`:

```json
{
  "auricTheme.look": "signature",
  "auricTheme.accent.preset": "patina",
  "auricTheme.syntax.palette": "cool",
  "auricTheme.a11y.enforceContrast": true
}
```

The theme re-applies automatically when you save. In the Studio footer, **Settings** opens the Settings editor filtered to this extension.

## Result

Your chosen look is active, your dial changes are visible in the editor, and each changed dial is marked with a dot so you can reset it individually.
