---
title: Auric Color — Reference
description: Every command, keybinding, setting, view, menu entry and theme colour Auric Color contributes.
product: VS Code extensions › Auric Artisan Studio › Auric Color
updated: 2026-09-25
---

# Auric Color reference

Facts for Auric Color 0.1.0 (`auric-artisan.auric-color`). It needs VS Code 1.74 or newer and starts when VS Code finishes loading. Categories: Visualization, Programming Languages, Other.

## Keybindings

| Keys (Windows, Linux) | Keys (macOS) | Command | Active when |
| --- | --- | --- | --- |
| `Ctrl` + `Alt` + `.` | `Cmd` + `Alt` + `.` | Workstation: Command Center | Auric Color is not suppressed by a Workstation host |
| `Ctrl` + `Alt` + `C` | `Cmd` + `Alt` + `C` | Pick / edit color | The editor has focus |

## Commands

All titles appear in the Command Palette after `Auric Artisan:`.

| Title | Command ID | What it does |
| --- | --- | --- |
| Open Color Studio | `auricColor.openStudio` | Opens the Studio on Color › Palette, or the Workstation host's Studio |
| Workstation: Command Center | `auricColor.commandCenter` | Opens the Command Center list |
| Open Rulebook & Knowledge Database | `auricColor.openKnowledgeBase` | Searches the brand rulebook, policies, articles, glossary and sources |
| Build Workspace Knowledge Database (JSON + Markdown) | `auricColor.writeKnowledgeDatabase` | Writes `knowledge.json`, `rulebook.md` and an overrides template |
| Open Unified Icon Studio | `auricColor.openIconStudio` | Opens the combined Auric icon library |
| Generate Accessible Palette | `auricColor.generatePalette` | Opens the Palette tool seeded with the selected colour (or `#2563EB`) |
| Check Contrast of Selection | `auricColor.checkContrast` | Opens the Contrast Studio with the selected colour as text (or `#1A1A1A`) |
| Fix All Contrast Issues in File | `auricColor.fixAllContrast` | Previews and applies fixes for every fixable failing pair, as one edit |
| Pick / edit color | `auricColor.pickColor` | Opens the picker on the colour at the cursor, or to insert a new one |
| Choose Color Picker Mode | `auricColor.chooseColorPickerMode` | Chooses Auric picker or VS Code native picker |
| Disable native color picker (use Auric Artisan) | `auricColor.disableNativeColorPicker` | Auric picker on, VS Code's decorators and hover sliders off |
| Restore native color picker (use VS Code's) | `auricColor.restoreNativeColorPicker` | VS Code's picker and decorators back on |
| Refresh Contrast Diagnostics | `auricColor.refreshDiagnostics` | Re-checks every open file |
| Change Accent Color (Theme the Studio) | `auricColor.chooseAccent` | Chooses the Studio's accent colour |
| Mark Line as Intentional Branding (Toggle) | `auricColor.markBranding` | Adds or removes `auric-brand-line` on the current lines |

See [Picker modes](picker-modes.md), [Contrast diagnostics](contrast-diagnostics.md) and [Appearance](../../docs/appearance.md) for details.

## Views

| View | ID | Notes |
| --- | --- | --- |
| Overview | `auricColorHome` | In the **Auric Color** Activity Bar container; the colour workbench layout |
| Color Picker | `auricColorPickerView` | Collapsed by default; the docked picker |

Both are hidden while another Studio extension hosts the Workstation.

## Editor right-click menu

| Entry | Shown when |
| --- | --- |
| Pick / edit color | Always |
| Generate Accessible Palette | Text is selected |
| Check Contrast of Selection | Text is selected |
| Choose Color Picker Mode | Always |
| Mark Line as Intentional Branding (Toggle) | HTML, Vue, Svelte, Astro, PHP, XML, Handlebars, JavaScript, TypeScript, JSX, TSX, CSS, SCSS, Less, Sass, PostCSS, Stylus and Markdown files |

## Settings

Auric Color has 16 settings. Change them in **File › Preferences › Settings** (search `auricColor`), in `settings.json`, or for some of them in Studio › Settings.

| Setting | Type | Default | What it does |
| --- | --- | --- | --- |
| `auricColor.appearance.accent` | string | `gold` | The Studio's accent: a preset ID or a hex such as `#2563EB` (see below). Stored in user settings. |
| `auricColor.hover.enabled` | boolean | `true` | Shows the colour hover (values, contrast, colour-vision preview, inline picker). |
| `auricColor.colorPicker.mode` | `auric` or `decorators` | `auric` | Auric's hover-first picker, or VS Code's native picker with Auric's tools on top. |
| `auricColor.colorPicker.nativeHoverPicker` | boolean | `false` | In Auric mode, shows VS Code's draggable picker inside the hover, with Auric's content beneath. VS Code's decorators stay on. |
| `auricColor.colorPicker.swatches` | boolean | `true` | Draws Auric's swatch before every colour literal (when VS Code's decorators are off). |
| `auricColor.colorPicker.clickAction` | `inlinePicker`, `fullEditor`, `off` | `inlinePicker` | What clicking a colour literal does in Auric mode. |
| `auricColor.colorPicker.autoOpen` | boolean | `false` | Legacy: when `true` and `clickAction` has never been set, clicking opens the picker panel. |
| `auricColor.colorPicker.inlineSwatches` | boolean | `false` | Contributes VS Code's native inline swatches and picker for colour literals. Set together with `mode` by **Choose Color Picker Mode**. |
| `auricColor.contrast.enabled` | boolean | `true` | Flags text and background pairs below the target. |
| `auricColor.contrast.standard` | `wcag2`, `apca`, `both` | `wcag2` | The contrast model for diagnostics. |
| `auricColor.contrast.apcaThreshold` | number, 15–106 | `60` | Minimum APCA Lc when APCA is used (90 ≈ AAA, 75 body, 60 large or medium, 45 large bold, 30 non-text UI). |
| `auricColor.contrast.threshold` | number, 1–21 | `4.5` | Minimum WCAG 2.x ratio (4.5 AA body, 7 AAA, 3 AA large and UI). |
| `auricColor.contrast.severity` | `error`, `warning`, `information`, `hint` | `warning` | Problems severity for failing contrast. |
| `auricColor.contrast.flagCvdRisk` | boolean | `true` | Adds a hint when a passing pair relies on hue and weakens under colour-vision deficiency. |
| `auricColor.contrast.checkPageBackground` | boolean | `true` | Grades colour-only rules against the page background, as softer "verify the real background" hints. |
| `auricColor.branding.enabled` | boolean | `true` | Honours `auric-brand-…` marks in the editor, moving marked colour findings to the Branding group. |

Accent presets: `gold`, `champagne`, `rose-gold`, `silver`, `platinum`, `bronze`, `copper`, `espresso`, `maroon`, `rose`, `emerald`, `sapphire`, `amethyst`. See [Appearance](../../docs/appearance.md). The page background for `contrast.checkPageBackground` is the one declared on `body`, `html` or `:root` in the same file.

When Auric Accessibility is installed, it owns contrast diagnostics and the Studio's contrast settings, and reads its own `auricA11y.contrast.*` keys instead of these.

## Theme colours

| Colour ID | Dark | Light | High contrast | High contrast light |
| --- | --- | --- | --- | --- |
| `auricColor.branding.foreground` | `#F06595` | `#C2255C` | `#FF80AB` | `#A61E4D` |
| `auricColor.branding.background` | `#F0659522` | `#C2255C1A` | transparent | transparent |
| `auricColor.branding.border` | `#F0659580` | `#C2255C80` | `#FF80AB` | `#A61E4D` |
| `auricColor.branding.icon` | `#F06595` | `#C2255C` | `#FF80AB` | `#A61E4D` |

## Studio spaces

When Auric Color is the host or runs alone: **Color** (Palette, Shades, Vision), **Check** (Contrast), **Brand** and **Settings** (Appearance, Contrast, Color picker).

## Diagnostics

| Code | Meaning |
| --- | --- |
| `low-contrast` | WCAG 2.x contrast below target |
| `apca-low` | APCA below target |
| `cvd-risk` | Colour-vision risk |
| `branding:contrast`, `branding:apca`, `branding:cvd` | Classified as intentional branding |

## Export files

| File | From |
| --- | --- |
| `palette.css`, `palette.json`, `palette.tailwind.js` | Palette tool |
| `shades.css`, `shades.tailwind.js` | Shades tool |
| `brand-tokens.css`, `brand-tokens.json` | Brand tool |

## Related

- [Studio reference](../../docs/reference.md), including shared settings.
- [Shortcuts](../others/shortcuts.md)
