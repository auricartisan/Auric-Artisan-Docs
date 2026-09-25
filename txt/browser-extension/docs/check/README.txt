==============================================================================
CHECK TOOLS
==============================================================================
The tools in the Check space — Contrast, Vision, Audit and Findings — and the
rules the audit applies.
Area: Browser extension › Check   Updated: 2026-09-25

The Check space holds the accessibility tools. Contrast checks any colour pair
and fixes it. Vision shows the live page through twelve simulations. Audit
checks the current page against WCAG 2.2, and Findings gathers everything
wrong into one list.

FILES IN THIS FOLDER
====================

  Page:           Contrast [contrast.txt]
  What it covers: Check a pair in WCAG and APCA, read the verdict, and find
                  the nearest passing colour

  Page:           Vision [vision.txt]
  What it covers: Colour-vision and low-vision simulations on the live page,
                  side by side, and capture

  Page:           Audit [audit.txt]
  What it covers: Run an audit, read the contrast results, outline problems on
                  the page, and export

  Page:           Audit rules [audit-rules.txt]
  What it covers: The 80 rules of the accessibility engine, by category, with
                  their WCAG criteria

  Page:           Findings [all-findings.txt]
  What it covers: The pooled list of problems, by severity, with actions for
                  each

KEY IDEAS
=========

  - WCAG contrast ratio compares the relative luminance of two colours, from
    1:1 (no contrast) to 21:1 (black on white). WCAG 2.2 asks for 4.5:1 for
    body text and 3:1 for large text at level AA, and 7:1 and 4.5:1 at AAA.
  - APCA Lc (Accessible Perceptual Contrast Algorithm, lightness contrast) is
    the contrast method in the WCAG 3 drafts. It gives a signed score, where a
    higher absolute value reads more easily, and its guidance depends on font
    size and weight.
  - Large text means at least 24 px, or at least 18.66 px when bold.

The glossary [../../others/glossary.txt] defines these and other terms, and
Limits and accuracy [../../others/limits-and-accuracy.txt] explains what the
checks can and cannot tell you.
