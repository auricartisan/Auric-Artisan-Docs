---
title: Contrast Checker — FAQ
description: Short answers to common questions about the Contrast Checker and colour contrast.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Contrast Checker FAQ

## What contrast ratio do I actually need?

4.5:1 for body text and 3:1 for large text is WCAG 2.1 Level AA, the level most laws and contracts reference. AAA asks for 7:1 and 4.5:1. Interface components and meaningful graphics need 3:1 against what sits next to them.

## What counts as large text?

At least 18.66 pixels in bold, or 24 pixels otherwise. A large heading in a light weight can still fall under the body-text requirement.

## Does passing the ratio mean the text is readable?

No. The WCAG 2.1 formula ignores font weight, size beyond the large-text threshold, and the way light text on dark backgrounds appears to spread. A pass is a floor, not a verdict. Check the preview as well as the number.

## Do disabled controls and logos have to pass?

No. WCAG 2.1 exempts inactive controls, pure decoration, text that is part of a logo, and text in a picture of something else. Everything a person has to read or operate is in scope.

## Does the checker show APCA?

No. The page's title mentions APCA, but the tool itself calculates only the WCAG 2.1 ratio. For APCA Lc values beside the ratio, audit a page with the [Analyzer](../../analyzer/README.md); its A11y+ panel shows them. The REST API endpoint named in the page's API hint also covers APCA.

## Can I check a colour with transparency?

Not directly. Work out the solid colour it shows over its background and test that.

## Can I check many pairs at once?

Not here. It checks one pair at a time. The [Analyzer](../../analyzer/README.md) checks every pair on a live page.

## Is anything uploaded or saved?

No. The maths runs in your browser and nothing is stored. The pair lives only in the page address.

## Do I need an account?

No. The tool is free and needs no sign-in.

## Can I use it with a keyboard and a screen reader?

Yes. Every control is reachable with `Tab`, the ratio is announced when it changes, and the result of each button is announced too. See the [Reference](reference.md).
