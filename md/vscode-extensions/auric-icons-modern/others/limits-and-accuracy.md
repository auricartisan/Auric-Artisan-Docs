---
title: Auric Icons: Modern — Limits and accuracy
description: What the Modern file icon theme and Icon Library can and cannot do.
product: VS Code extensions › Auric Icons: Modern
updated: 2026-09-25
---

# Limits and accuracy

## File icon theme

- Icon themes match file and folder names without path context. A name such as `settings.json` cannot be given a special icon for one folder only, which is why `.auric-artisan/settings.json` has no dedicated icon.
- Association keys are either `*.ext` or an exact name. Wildcards in the middle of a name and folder paths are not supported.
- Changes need a window reload to appear.
- Workspace detection checks only the top of local workspace folders; remote and virtual folders are skipped.
- Only one framework pack can be active.
- Colour is never the only cue: each icon also has a distinct shape, so icons stay distinguishable at low saturation.

## Icon Library

- The library is fixed to the installed version: 720 icons. New icons come with updates.
- Smart insert picks a format by language only, not by the exact cursor position. Check quotes and surrounding code.
- Recommendations are local rankings from the file you are editing and your likes and use, not an AI service.
- Hover previews recognise only Modern library IDs (a hyphenated name ending in four digits).
- There are no size, colour or stroke controls for output; icons are inserted as drawn. (Icon Studio and Icon Hub offer output controls.)

## Licence

Free to use for any purpose. Redistribution, republishing to any marketplace, resale and derivative releases are not permitted. Letterforms in some icons are outlines derived from Inter under the SIL Open Font Licence 1.1.
