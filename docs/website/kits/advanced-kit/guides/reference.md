---
title: Advanced Kit — Reference
description: Every control, card, button and message in the Advanced Kit.
product: Website › Kits › Advanced Kit
updated: 2026-09-25
---

# Advanced Kit reference

## Launcher

| Control | What it does | Default |
|---|---|---|
| **Advanced** launcher (slider icon) | Opens or closes the kit. Announces itself as **Open Advanced Kit** or **Close Advanced Kit** | Closed |
| `Ctrl` + `Shift` + `A` | Same as the launcher | — |
| Tooltip | "Choose Basic, Advanced, or Everything tool visibility." | — |

## Title bar

| Control | What it does | Values | Default |
|---|---|---|---|
| **Advanced Kit** title | Drag the title bar to move the kit | — | Bottom-left corner |
| **Focus mode** | Keeps the kit open across pages and when other kits open | On or off; remembered | Off |
| **Theme** | Switches the kit between light and dark | Light or dark; remembered | Follows the site |
| **Resize** | Normal (480 px wide) or expanded (up to 720 px wide) | Remembered | Normal |
| **Minimize** | Collapses the kit to its title bar | — | — |
| **Close** | Closes the kit ("Close the Advanced Kit panel.") | — | — |

## Body

| Element | What it shows or does |
|---|---|
| **Tool visibility** | Heading, with "Choose which tools stay visible by default." |
| **Current mode** badge | **Basic**, **Advanced**, **Everything** or **Custom** |
| Mode summary | Illustration, title and description for the current mode, and switch buttons |
| **Default visibility** cards | Four selectable cards; a tick marks the current one. The **Basic** card is tagged **Recommended**. Each card's tooltip repeats its description |
| **Choose your tools** | The Custom checklist; shown only in Custom mode |
| Quick cards | Example tools for the current mode |

### Mode cards

| Card | Description | Value stored |
|---|---|---|
| **Basic** | Beginner-friendly tools stay visible while deeper scientific tools are hidden. | Default for new visitors |
| **Advanced** | Scientific, diagnostic, and power-user tools stay visible while simple tools are hidden. | — |
| **Everything** | Every tool stays available, including removed or not-yet-used cards. | — |
| **Custom** | Turn individual tools on or off — your picks apply across the whole site. | — |

### Mode summary

| Mode | Title | Buttons |
|---|---|---|
| Basic | Advanced tools are hidden | **Switch to Advanced** |
| Advanced | Advanced tools are on | **Show everything** |
| Everything | Everything is available | **Use Basic**, **Use Advanced** |
| Custom | Your custom tool set is active | **Show everything** |

### Custom checklist

| Control | What it does |
|---|---|
| **Enable all** | Ticks every tool |
| **Disable all** | Unticks every tool |
| **Reset** | Forgets your custom choices; every tool is ticked |
| **Filter tools…** | Hides rows whose name does not contain your text |
| Category headings | Group the rows; hidden when none of their rows match the filter |
| Tool checkboxes | Ticked shows the tool while Custom mode is on; unticked hides it |

### Quick cards

| Card | Opens | Shown in |
|---|---|---|
| **Analyze URLs** — "Audit color, contrast, accessibility, SEO, and page structure." | https://auricartisan.com/tool/analyzer/ | Every mode |
| **Image Color Picker** — "Pull colors and build palettes from any image." | https://auricartisan.com/tool/general/tools/image-picker/ | Basic, Everything, Custom |
| **Generate Ishihara Plates** — "Create vision-screening plates and teaching examples." | https://auricartisan.com/tool/ishihara-plate-generation/ | Advanced, Everything, Custom |

## Messages

| Message | When |
|---|---|
| **Loading tools…** | The Custom checklist is being built |
| **No tools found.** | The tool list could not be loaded |

## Keyboard

| Key | What it does |
|---|---|
| `Ctrl` + `Shift` + `A` | Opens or closes the kit |
| `Esc` | Closes the kit |
| `Tab` | Moves between cards, buttons and checkboxes |
| `Enter` or `Space` | Selects the focused card or toggles the focused checkbox |
