---
title: Auric Accessibility — FAQ
description: Short answers about Auric Accessibility.
product: VS Code extensions › Auric Artisan Studio › Auric Accessibility
updated: 2026-09-25
---

# Auric Accessibility FAQ

### How many rules are there?

70+: the current package runs 72 static rules across 29 WCAG success criteria, plus the contrast checks. The Marketplace description gives the figure as 70 rules across 28 criteria. See [Rules](rules.md).

### Will a clean result make my site WCAG compliant?

No. Static checks cover only part of WCAG, and many criteria need a person to test with a keyboard, a screen reader, zoom and real content. Use the [manual checks](manual-evidence.md) for the rest. The score is for prioritising and tracking progress, not a certification.

### Which WCAG version does it check?

WCAG 2.2 by default. You can choose 2.0, 2.1 or the 3.0 draft (which adds APCA). See [Audit profiles and contrast](audit-profiles-and-contrast.md).

### Does it work with React, Vue, Svelte and Astro?

Yes. It reads JSX and TSX, Vue, Svelte and Astro files, understands framework attribute syntax and bound values, and does not judge components such as `<Button>` as native elements. It cannot see markup produced by JavaScript at runtime.

### Does it check plain JavaScript files?

Plain `.js` and `.ts` files get contrast checks for CSS-in-JS, not the markup rules; put JSX in `.jsx` or `.tsx` files to get both. Inspect works in all four.

### Why was a finding shown as a hint "Best practice"?

Six rules (`accesskey`, `autofocus`, `heading-skip`, `positive-tabindex`, `tiny-font`, `text-spacing-important`) and unreferenced duplicate IDs flag patterns worth fixing that do not by themselves fail WCAG. They are shown as hints and weigh half in the score.

### Can it fix problems automatically?

Only where a rewrite is safe and deterministic, for 13 rules such as adding `lang="en"` or removing `accesskey`. Judgement calls such as alt-text quality are only suggested. See [Apply fix](editor-linting.md#apply-fix).

### How do I ignore a false positive?

Use **Ignore here** in the hover, the **Ignore this WCAG … finding here** quick fix, or an `auric-disable-next-line <rule-id>` comment. See [Suppression and branding](../../docs/suppression-and-branding.md).

### Can I mark a brand colour so it does not hurt the score?

Yes, with `auric-brand-line` or **Mark Line as Intentional Branding (Toggle)**. Only colour findings can be classified; structural findings always count.

### Does it use axe-core?

No. It has its own engine. During development its results were checked against axe-core on rendered HTML; see [Limits and accuracy](../others/limits-and-accuracy.md).

### Can I run the same checks in CI?

Yes, with the bundled `auric-artisan` command-line scanner. See [The CI gate](../../docs/ci-gate.md).

### Does it send my code anywhere?

No. See [Privacy](../others/privacy.md).
