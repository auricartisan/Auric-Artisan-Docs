---
title: Portfolio Builder — Preview and check
description: Preview your portfolio at different widths and full screen, and use the Check pane to fix accessibility problems before publishing.
product: Website › Portfolio
updated: 2026-09-25
---

# Preview and check

## Preview widths

The **Live preview** bar has four width buttons:

| Button | Width | Use |
| --- | --- | --- |
| **Fit** (default) | The width of the preview column, at full size | Writing and editing. |
| **Desktop** | 1160 px | Checking the desktop layout. |
| **Tablet** | 800 px | Checking a tablet layout. |
| **Mobile** | 390 px | Checking a phone layout. |

The bar shows the current width (for example **Desktop · 1160px**) and the number of sections. Desktop, Tablet and Mobile may be scaled down to fit the column; Fit is the width to write at. The builder remembers your choice in this browser.

**Fullscreen preview** (the button at the right of the bar) enlarges the preview to fill the screen; select it again, or press `Escape`, to leave.

## Full preview in a new tab

Select **Preview** in the top bar (or the command **Open a full preview**). The finished page opens in a new tab, exactly as an exported HTML file would look. If nothing opens, the builder says **Allow pop-ups to preview.** — allow pop-ups for auricartisan.com.

## The Check pane

Open **Check**. It audits the page as it is actually rendered — the colours, sizes and text a visitor will get — against WCAG 2.2 AA.

### What it checks

| Finding | Severity | What it means | The fix it suggests |
| --- | --- | --- | --- |
| **Text below AA** | Blocking when well below; otherwise a warning | Normal text is under 4.5:1 against its background. | "Take a darker step from the same palette in Style, or change the paper." |
| **Large text below AA** | Blocking when well below; otherwise a warning | Large text (24 px, or about 19 px bold) is under 3:1. | "Deepen this colour, or set the text larger so the 3:1 threshold applies." |
| **A link with no text** | Blocking | A link with nothing readable inside it. | "Give it text, or an aria-label if it is deliberately an icon." |
| **A link that does not say where it goes** | Blocking | Link text such as "click here", "here", "read more", "more", "link", "this", "learn more" or "see more". | "Name the destination in the link itself." |
| **An image with no alt text** | Blocking | An image with no description for screen readers. | "Describe what the image shows, or set alt="" if it is decoration." |
| **Heading jumps from hN to hM** | Warning | A heading level is skipped, for example h2 to h4. | "Make this an h3, or add the level it skipped." |
| **A target smaller than 24px** | Warning | A link or button smaller than 24 × 24 pixels. | "Give it padding, or set a minimum height." |
| **A colour this check could not read** | Warning | Text in a colour format the check does not measure (for example from Raw HTML). | "Pick this colour from the Style pane, which works in sRGB and is graded." |

Each finding explains why it matters and names the section it is in. Contrast findings show the colour pair and ratio, for example "#9A8F7B on #FBFAF7 is 3.05:1".

### Using the pane

1. Read the summary: how many faults, in how many places, and how many would stop the page going online — or "None of them blocks publishing."
2. When there are several kinds, use the filter chips **All**, **Blocking** and **Contrast**.
3. Select a finding. The preview scrolls to it and outlines the element.
4. Fix it in the section card, the preview, or **Style**. The pane updates.

When everything passes, it says the pairs checked "against WCAG 2.2 AA. Nothing to fix." If the preview has not rendered yet, it says **The preview has not rendered yet.**

### Blocking findings stop publishing

While any **Blocking** finding remains, the **Publish** button is disabled and its tooltip says, for example, "2 things to fix in Check before this can go online". Warnings do not block publishing. Saving and exporting are never blocked.

While you work in **Content**, a dot on the **Check** tab tells you there is something to look at.

## Result

You have seen the page at every width, and it goes online without contrast, link, alt-text or heading problems.
