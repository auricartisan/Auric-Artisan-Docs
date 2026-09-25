---
title: Basic Color Tools — Getting started
description: Open Basic Color Tools, learn the parts of the screen, and make, check and export your first palette.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Getting started with Basic Color Tools

This guide takes you from opening the page to exporting a checked palette. It takes about five minutes.

## Open the page

1. Go to https://auricartisan.com/tool/basic-tools/ in a current desktop or mobile browser. JavaScript must be enabled.
2. Wait for the page to load. You see the title **Basic Color Tools**, a short description, and a row of labels: **4 Categories**, **7 Tools**, **Palette Remix · Color Battle**, **Sidebar + Panel Layout** and **In-page Floating Panels**.
3. Below the title is a row of three view buttons: **Workspace**, **Catalogue** and **Panels**. The page opens on **Workspace** the first time, and on the view you used last after that.

## A tour of the screen

### The view buttons

| View | What it shows |
| --- | --- |
| **Workspace** | A launcher list on the left and a stage on the right. Tools you open appear as panels on the stage. This is where you work. |
| **Catalogue** | A searchable grid of tool cards with a category filter, a level switch, favourites and a copy-link button. Use it to browse and filter. |
| **Panels** | A list of the panels that are open, each with its state, and a reminder of what the panel title-bar buttons do. |

### The Workspace view

- **Open a tool** (left column) lists every tool the catalogue currently shows, grouped by category: **Generate**, **Pick**, **Compose** and **Convert**. Each row has a small colour band, the tool name, an **Advanced** label on advanced tools, and the word **open** when that tool already has a panel.
- **Panels** (left column, below the list) shows how many panels are open out of five, as a number and a bar. It tells you how much room is left ("Room for 3 more.") or that you have reached the ceiling. Every open panel is listed with its state: **Floating**, **Docked** or **Maximised**. Select one to bring it back to the front.
- **The stage** (right) is where panels open. Before you open anything it shows **Nothing open yet.** and a short explanation. Panels stay inside the stage while you work in this view. On screens narrower than about 1,100 pixels the launcher column sits above the stage instead of beside it.

### A panel

Every tool opens in the same kind of window:

- A **title bar** with the tool's name and category, and four buttons: **Open another instance** (duplicate), **Minimize**, **Maximize or restore**, and **Close**.
- A **controls sidebar** on the left with the tool's inputs and export buttons.
- A **main area** on the right with the result, often split into tabs.
- A **resize handle** in the bottom-right corner.

On a narrow screen the sidebar and main area stack vertically inside the panel, and the panel body scrolls.

### Save to Library

A floating **Save to Library** button sits near the bottom-right corner of the page. It saves the result of the focused panel to your Library. See [Import, export and the Library](import-export-and-library.md).

## Your first palette

1. In **Open a tool**, select **Palette Studio**. A panel opens on the stage with five colour strips in the main area.
2. Select **Generate** in the sidebar. Five new colours replace the old ones. You can also press `Space` while the panel is focused and your cursor is not in a text box or list.
3. Open the **Harmony** list and choose **Analogous**. The palette regenerates as neighbouring hues.
4. Hover over the second colour strip. Small buttons appear at its top. Select the lock button. The strip is marked as locked.
5. Select **Generate** a few more times. The locked colour stays; the others change.
6. Select **+ Add** to add a sixth colour. A palette holds between two and nine colours.
7. Select the main area's **Contrast Matrix** tab. A table shows the WCAG contrast ratio of every pair of colours, colour-coded from fail to AAA.
8. Open the **CVD Preview** list in the sidebar and choose **Deuteranopia**. The strips now show how the palette may look to someone with deuteranopia. Your real colour values are unchanged; set the list back to **Normal vision** when you are done.
9. In the **Export** section, select **CSS**. The palette is copied to your clipboard as CSS custom properties, and a short **CSS copied** message appears.

Result: a palette you generated, locked and checked, copied as code:

```css
:root {
  --color-1: #3F6E8C;
  --color-2: #5B8A74;
  --color-3: #A3B86A;
  --color-4: #D9C27A;
  --color-5: #E89F6B;
  --color-6: #B5655C;
}
```

The colours above are only an example; yours will differ.

## Work with two tools at once

1. With Palette Studio open, select **Gradient Maker** in **Open a tool**. A second panel opens, slightly offset from the first.
2. Drag the Gradient Maker title bar to move the panel. Drag the corner handle to make it smaller.
3. Select anywhere on the Palette Studio panel. It comes to the front.
4. Select **Minimize** on the Gradient Maker title bar. The panel is hidden from the stage, and the **Panels** list on the left shows it as **Docked**. Its work is kept.
5. Select **Gradient Maker** in the **Panels** list (or select **Gradient Maker** again in **Open a tool**). It returns at its previous size and position, with your stops as you left them.

Result: two tools on screen, and you know how to arrange, dock and restore them. For more, read [Workspace and panels](workspace-and-panels.md).

## Next steps

- Learn each tool: [Panel tools](panel-tools/README.md).
- Open the site-wide Colour Tools from any page: [Colour Tools workbench](colour-tools/README.md).
- See every export format: [Import, export and the Library](import-export-and-library.md).

## Related

- [Basic Color Tools overview](../README.md)
- [Shortcuts](../others/shortcuts.md)
- [Troubleshooting](troubleshooting.md)
