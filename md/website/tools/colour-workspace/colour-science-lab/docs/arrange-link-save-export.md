---
title: Color Science Lab — Arrange, link, save and export panels
description: Move, resize, pin, dock and link Color Science Lab panels, arrange them with the Color Control centre, export a combined image, and save panels to your Library.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Arrange, link, save and export panels

## Panel windows

Lab panels float over the whole page, whichever view you are on. Each opens at 1120 by 720 pixels (or smaller to fit your window), offset slightly from the last one.

### Title-bar buttons

| Button | Tooltip | What it does |
| --- | --- | --- |
| Link | **Link shared controls** | Links this panel. Linked panels copy each other's control changes (see below). |
| Duplicate | **Open another instance** | Opens another copy of the tool with its own settings. |
| Pin | **Keep panel open** | Protects the panel from being closed automatically or by **Close unpinned** and **Close all**. |
| **−** | **Minimize** | Hides the panel and adds it to the dock. |
| **□** | **Maximize or restore** | Fills the window; select again to restore. |
| **×** | **Close** | Closes the panel. |

- Drag the title bar to move; double-click it to maximise or restore.
- Drag the bottom-right corner to resize. The minimum is 520 by 420 pixels, or the window size if smaller.
- Select a panel to bring it to the front.
- With the keyboard focus inside a panel, `Escape` restores a maximised panel, or closes the panel otherwise.
- Selecting a tool that is already open brings its panel forward instead of opening a second one.

### The five-panel limit

Up to five panels can be open. Opening a sixth closes the oldest panel that is not pinned. If all five are pinned, the new tool does not open until you unpin or close one.

### The dock

Minimised panels appear as items in a dock. Select an item to restore the panel; select its **×** to close it.

## Linking panels

Link two or more panels with their link buttons (or **Link all** / **Sync all**). When you change a control in a linked panel, the same control in every other linked panel changes too: sample and compare colours, model, colour space, theory, white points, strength, colour temperature and the two check boxes. Use it to run one colour through several tools at once, for example Bradford Adaptation, CAT Matrix Comparison and White Point Reference Atlas.

## The Open Panels list

Choose **Open Panels** in the Catalogue's domain list. A toolbar offers **⊞ Tile**, **⫷ Cascade**, **▤ Stack**, **🔗 Link all** (or **Unlink all**), **📤 Export image** and **✕ Close unpinned**. Below it, a card per panel shows its domain, name, whether it is active or *Minimized in dock*, its level and **Linked** or **Pinned** tags. Select a card to bring the panel forward.

## The Color Control centre

When at least one panel is open, a floating **Color Control** box appears, with the number of open panels. Drag it by its header; collapse or expand it with the arrow button.

| Button | What it does |
| --- | --- |
| **Grid** | Tiles the panels: one fills the window, two to four in two columns, five in three columns. |
| **Split H** | Places the panels side by side at full height. |
| **Split V** | Stacks the panels at full width. |
| **Cascade** | Gives each panel the default size and staggers them. |
| **Stack** | Centres every panel in the same place. |
| **Sync all** | Links every panel, or unlinks them if all are linked. |
| **Minimize** / **Restore** | Docks or restores every panel. |
| **Export** | Downloads the combined image (below). |
| **Close all** | Closes every panel that is not pinned. |

The layouts apply to panels that are neither minimised nor maximised. Below the buttons, each panel is listed with its domain and **Sync**, **Keep** (pin), **Min** or **Open**, **Max**, **Copy** (duplicate) and **Close**. Select a panel's name to bring it forward.

## Export a combined image

**Export image** (Open Panels) or **Export** (Color Control) downloads one PNG, `color-science-lab-` followed by the date and time, with each open panel's experiment canvas in a grid, labelled with its name.

## Save to and restore from the Library

With a panel focused, select the floating **Save to Library** button. The panel is saved as a preset with a picture of its canvas, its colours and every control value. With no panel open, it saves a *Color Science Lab — workspace* bookmark instead.

Opening a saved preset from your Library opens a fresh copy of that tool (closing any open copy) and re-applies the saved controls once the panel has drawn. See the [Library Kit](../../../../kits/library-kit/README.md).

Panels themselves are not kept when you reload the page.

## Related

- [The Catalogue and its panels](catalogue-and-panels.md)
- [Shortcuts](../others/shortcuts.md)
- [Troubleshooting](troubleshooting.md)
