---
title: Analyzer — Arrange the workspace
description: Open, move, resize, focus and close report panels, find sections with the Sections picker, and save layouts.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Arrange the workspace

The Analyzer shows its report as a workspace: each section is a panel in a grid, and you choose which panels are on screen and where. This lets you read a finding and the thing it is about side by side, for example the accessibility findings next to the contrast pairs and the fixes.

Both modes use the workspace. Simple mode offers 8 sections and no **Layouts** menu; Advanced offers all 22 sections and saved layouts.

## What opens by itself

- **Before your first run**, the workspace holds only the **Overview** panel, across the full width.
- **After a run**, the section of every check that ran is opened, if your mode can show it. The **Devices** section is never opened automatically.
- **The first time you use Advanced**, the default arrangement is **Overview** and **Contrast** side by side, with **Fixes** across the full width below. It replaces the single Overview panel when your first run finishes, but only if you have not already changed the arrangement.

Sections you closed during a run are not reopened for you.

## The panel title bar

Every panel has a title bar with a grip and four buttons:

| Control | What it does |
| --- | --- |
| Grip (the section icon and name) | Drag to move the panel. With the keyboard, focus it and press `Left` or `Right` to move it one place. |
| **Width** | Cycles the panel through a third of the row, half the row and the full row. |
| **Focus** | Shows only this panel, full width. Select it again ("Show the other panels again") to bring your arrangement back. |
| **Collapse** / **Expand** | Folds the panel to its title bar and back. The panel keeps its place. |
| **Close** | Removes the panel from the workspace. Its data is kept; open it again from the Sections picker. |

Panels are as tall as their content, and the grid packs them so a short panel beside a long one does not leave a gap.

## Open sections with the Sections picker

In Advanced mode select **Sections** in the strip. In either mode you can press `Ctrl` + `P` while the Analyzer is open.

> **Note:** While the Analyzer page is open, `Ctrl` + `P` opens the Sections picker instead of your browser's print dialog. To get the report on paper, use the exports in the **Report** section.

The picker is a dialog with a filter field ("Type to filter…") and every section your mode offers, in three groups:

| Group | Contains |
| --- | --- |
| **On screen** | Sections that are open now. Their tick box is ticked. |
| **Ready to open** | Sections the last run filled, or that are always available |
| **Not scanned** | Sections whose check was switched off for the last run. Their count reads "scan". |

Each row shows the section's finding count, taken from the same badge the section uses. A dash means the section has no count.

To use it:

- Select a row to open or close that section. The picker stays open, so you can open several in one visit.
- Type in the filter field to narrow the list.
- Press `Up` and `Down` to move between rows, following the rows as they are laid out on screen; `Left` and `Right` move across columns when the filter field is empty.
- Press `Enter` to open the highlighted section (or scroll to it if it is already open) and close the picker.
- Press `Space` to open or close the highlighted section and keep the picker open.
- Press `Esc`, or click outside the dialog, to close it.

The footer shows these keys and how many sections are on screen.

Choosing a section from **Not scanned** turns its check on. If there is already a report, the Analyzer runs the audit again so the section has something to show. In Simple mode this also switches you to Advanced, because Simple has no scan picker.

## Open a section from the progress rail

The steps in the run line also open sections: **3 Fix** shows Fixes, **4 Preview** shows Before / After, **5 Export** shows Report, and **1 Analyze** and **2 Issues** show the Overview. A section opened this way appears at the top of the results area, above the panels, rather than as a panel of its own.

## Layouts (Advanced)

Select **Layouts** in the strip to open the layout menu.

### Ready-made layouts

| Layout | What it puts on screen |
| --- | --- |
| **Accessibility review** | The engine's findings, the contrast that fails, and the fixes: A11y+ full width, then Contrast and Fixes side by side |
| **Colour and vision** | Every failing pair beside its palette, both under a filter: Contrast, Palette, Simulation, Before / After |
| **Speed and weight** | Vitals, what JavaScript wrote, and the media that costs the most: Performance full width, then Media and Deep |
| **Content and search** | Metadata and headings against the shape of the whole site: SEO and Project, then Site Map full width |
| **Everything, thin** | One narrow column of each, for a first look: Overview, Contrast, A11y+, SEO, Performance, Site Map |

The arrangement currently on screen is marked **on screen**.

### Save your own layout

1. Arrange the panels the way you want them.
2. Open **Layouts**.
3. Type a name in the **Name this arrangement** field (up to 40 characters).
4. Select **Save**.

Your layout now appears in the menu. Select it to apply it. Select the **×** beside a saved layout to forget it.

### Nothing is lost when you switch

When you apply a layout or select **Reset to the default layout**, the arrangement you are leaving is kept, unless it is already saved under a name. It appears under **Kept automatically** as the date and time, for example "12 Sep 14:05". Only the three newest automatic entries are kept; named layouts are never removed for you.

## What is remembered

- Each mode remembers its own arrangement, in this browser, between visits.
- Saved layouts are stored in this browser.
- A **Focus** view is temporary and is not remembered.

If the workspace cannot load in your browser, the Analyzer falls back to a row of tabs, one section at a time.
