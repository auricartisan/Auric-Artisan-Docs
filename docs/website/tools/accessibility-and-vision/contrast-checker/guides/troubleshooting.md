---
title: Contrast Checker — Troubleshooting
description: Odd results in the Contrast Checker, why they happen, and what to do.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Troubleshooting the Contrast Checker

### The ratio looks wrong while I am typing

- **Why:** a half-typed value such as `#1A` cannot be read, so the checker grades pure black (for the text) or pure white (for the background) in its place.
- **What to do:** finish typing all three or six digits, or press `Tab` to leave the field. The field rewrites a valid value in full, and the ratio is then yours.

### My colour is not accepted

- **Why:** the fields take hex only. `rgb()`, `hsl()`, colour names and eight-digit hex with transparency are not accepted.
- **What to do:** convert the colour to six-digit hex first. For a semi-transparent colour, work out the colour it actually shows over its background, and test that.

### The ratio says 4.50:1 but body text AA says Fail

- **Why:** the display is rounded to two decimals; the badge uses the exact value, which is just under 4.5.
- **What to do:** treat it as failing and move the colour a little further.

### The ratio did not change when I swapped the colours

- **Why:** the ratio does not depend on which colour is the text. Only the preview, and which colour **Make it pass AA** moves, change.
- **What to do:** nothing; this is correct.

### Make it pass AA made my colour grey

- **Why:** it moves the text colour in a straight line towards black or white and stops at the first passing step, which removes saturation.
- **What to do:** use its result as a target and adjust your original colour towards it by hand. See [Make a pair pass](make-a-pair-pass.md).

### Make it pass AA went towards white on a mid-grey background

- **Why:** the direction follows relative luminance. Mid greys count as dark.
- **What to do:** darken the text yourself if you want the other direction.

### The Make it pass AA button is missing

- **Why:** it only appears when body text fails AA. If the pair already reaches 4.5:1 there is nothing to fix.
- **What to do:** for AAA (7:1), darken or lighten the text by hand.

### Copy link printed the address instead of copying it

- **Why:** your browser did not allow clipboard access, for example on an insecure connection or because you declined the permission.
- **What to do:** select the address in the status line and copy it by hand.

### Back does not return to my previous colours

- **Why:** the address is replaced, not added to history.
- **What to do:** copy a link whenever you want to keep a pair.

### The UI & graphics row passes but my control is still hard to see

- **Why:** the row compares the two colours you entered. A control's edge is judged against the colour actually next to it, which may not be the background you typed.
- **What to do:** enter the control's border colour and the colour directly behind the control.
