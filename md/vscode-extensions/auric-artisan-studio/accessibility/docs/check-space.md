---
title: Auric Accessibility — The Check space: Findings and Preview
description: Filter every finding in the Studio's Findings tool, and preview failing contrast next to its accessible repair in the Preview tool.
product: VS Code extensions › Auric Artisan Studio › Auric Accessibility
updated: 2026-09-25
---

# The Check space: Findings and Preview

The Studio's **Check** space holds three tools. **Findings** and **Preview** come with Auric Accessibility; **Contrast** is the [Contrast Studio](../../docs/contrast-studio.md). Switch between them with the tab row under the space header.

## Findings

**Findings** lists every WCAG finding, failing contrast pair and colour-vision risk from the last scan. Its tab shows the total count.

Before a scan it says **No scan yet** and offers **Scan project**.

### Header actions

| Button | What it does |
| --- | --- |
| **Export WCAG** | Saves `wcag-report.md`, a Markdown summary by criterion with every finding. See [Exports and health records](../../docs/exports-and-records.md#studio-markdown-exports). |
| **Fix plan for an agent** (gold) | Generates the [remediation plan](../../docs/remediation-plan.md) |

### WCAG accessibility

A section titled **WCAG accessibility** with the number of issues and files. It shows:

- badges for the accessibility sub-score (`a11y 97`), counts by level (`A 3 · AA 1 · AAA 0`) and counts by WCAG version;
- a badge for every success criterion found, such as `1.1.1 ×4`; select one to show only that criterion, and again to clear it;
- impact filters: **All**, **Critical**, **Serious**, **Moderate** and **Minor**, each with its count;
- a search box, **Filter by text, file, SC…**, that matches the message, criterion title and number, file path, evidence and level;
- a count such as `12 of 40 shown`, and the list, up to 200 rows at a time.

Each row shows the criterion, its title, the message, and the file, line and level (or **best practice**). Hover a row for the fix; select it (or press `Enter`) to open the file at that line.

Press `/` to jump to the search box, and `Escape` to clear it.

### Failing contrast

Every failing pair, worst first (up to 200 rows), with the pair, its ratio, what it needs (for example `needs 4.5:1`, or `large text, needs 3:1`), `dark theme` when it applies, and its location. The section's subtitle shows your target and the large-text target.

### Color-vision risk

Pairs that pass for typical vision but weaken under colour-vision simulation (up to 80), shown as `2.9:1 → 1.8:1 CVD`. Collapsed at first.

### Branding

Pairs classified as intentional branding, each with a **♥ branding** badge, its ratio and kind. A note explains the classification and how many structural findings had a branding mark that was ignored. Collapsed at first.

### Confusable hues

Pairs of project colours that look different normally but merge under colour-vision simulation, with the colour difference before and after. Select one to copy both hex values. Collapsed at first.

Sections remember whether you left them open or closed.

## Preview

**Preview** draws the same content twice, with your original colours and with an accessible repair, so you can judge legibility on real text rather than a swatch.

### Controls

| Control | Values | What it does |
| --- | --- | --- |
| **Text**, **Background** | Any colour; **⇄** swaps them | The pair to preview |
| **WCAG target** | AA Large / UI · 3:1, AA body · 4.5:1, AAA · 7:1 | The ratio the repair aims for |
| **Fix by** | Recolor text, Recolor background | Which colour the repair changes |
| **Vision** | Typical vision, Protanopia, Deuteranopia, Tritanopia, Achromatopsia | Shows both surfaces through a colour-vision deficiency |

### Interactive pair

Two surfaces side by side, **Original** and **After WCAG**. Each has a heading, body text, a caption, a **Primary action** button and a sample link, and below it the WCAG ratio, APCA Lc and **AA**, **AAA** and **UI 3:1** badges. A strip shows what changed (`text #999999 → #767676`), the ratio before and after, and **✓ meets 4.5:1** or **best effort** when the hue cannot reach the target.

Buttons: **Copy** the repaired colour, **Insert fix** (replaces the editor selection with it) and **Open in Contrast →** (loads the repaired pair into the Contrast Studio).

The Original surface deliberately shows failing contrast, so it is hidden from screen readers; its numeric verdict below is read instead.

### Project failures

After a scan, every failing pair from the project appears as its own before-and-after, up to the first 24 (the first three open), each with **Open file:line**. Before a scan, the section offers **Scan project**.

Open Preview on a specific pair with **Open in Preview** in an Inspect card.

## Related

- [The Studio](../../docs/studio.md)
- [The Project Issues view](project-issues-view.md)
- [Contrast diagnostics](../../color/docs/contrast-diagnostics.md)
