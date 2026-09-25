---
title: Personalization Generator — Troubleshooting
description: Fixes for common problems in the Personalization Generator, from lost results to unreadable palettes.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Troubleshooting

## My results disappeared after a reload

Results are kept only while the page is open. On every visit a quick new sweep runs, using your saved pool and settings. Before you leave, copy what you need, select **Download JSON** in **Export**, or **Save** the results you want to your Library. See [Export, save and share](export-and-save.md).

## The brief box is empty after a reload, but the results still follow my old brief

The brief is remembered, but the box in the left column starts empty. The remembered text is still used, and it shows in **Tune** under **Preference note**. Edit or clear it there, or type a new brief.

## Changing the brief does not change much

The brief is matched word by word against the names of built-in reference palettes; it is not read as a sentence. Words that appear in no name have no effect. Use a few distinctive words, and steer with the pool, style chips and **Use case** for bigger changes. See [Tune the sweep](tune-the-sweep.md).

## Every palette looks like my pool

Preference, closeness to your pool, carries the largest share of the score.

- Select **Jitter** once or twice in **Pool**.
- Raise **Diversity** in **Tune**.
- Remove near-duplicates from the pool.
- Use **+24 random** or **Build** to widen the pool.

## The palettes have no readable text pair

- Make sure **Contrast** (**UI contrast bonus (4.5:1)**) is on.
- Raise **Accessibility** in **Tune**.
- Add a very dark and a very light colour, or select **+ Grayscale** in **Quick seeds**.

Contrast is a weight, not a filter, so a palette with weak contrast can still be kept if the rest of its score is high. Check **The leader, checked** in the right column after each sweep.

## Generate does nothing

A sweep is already running; **Generate** reads **Generating…** until it ends. Wait, or select **Stop**. If **Endless** is on, each new sweep starts on its own; select **Endless** again to turn it off.

## A big sweep is slow

Sweeps of several thousand candidates take longer, especially on older devices. Lower **Search depth**, or select **Stop** at any time; the best of what the sweep has already found is kept.

## Endless mode shows the same kind of palette over and over

Endless merges each sweep into the list and keeps only the 96 best, so strong early palettes stay at the top. Change the pool or styles and run a normal sweep with **Generate** to start afresh.

## The Studio shows colours that are not in the palette

The **Test** overrides from an earlier palette are still set: a new sweep or a reload keeps them. Open **Test** and select **Reset**, or choose a palette from **Available Palettes**, which clears them.

## The check boxes in the left column disagree with Tune

The left-column boxes pick up changes made in **Tune** only after a reload. The Tune settings are the ones in force. Use one place for the filters, or reload the page to bring the two into line.

## This run shows old numbers

**This run** refreshes when you change a setting in the left column. After moving a slider in **Tune**, it can show the previous value until you next touch the left column. The Tune slider value is the one in force.

## The fonts in Typography or the Studio look wrong

The page does not download the named fonts. If a font is not installed on your device, the browser uses the next one in the stack, often a system sans or serif. Install the font, or read the three faces listed on each card.

## Save says Already saved

That card from the same sweep is already in your Library. Run a new sweep to save a new copy, or open your Library to find the saved item.

## Save says Save failed

The Library could not store the item. Reload the page and try again. If it keeps failing, see the [Library Kit](../../../../kits/library-kit/README.md).

## Loading a preset lost my colours

Loading a preset replaces the pool. There is no undo. Add your colours back with **Add**, or from a palette you saved to your Library.

## Related

- [FAQ](faq.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
- [Help centre](../../../../../help/README.md)
