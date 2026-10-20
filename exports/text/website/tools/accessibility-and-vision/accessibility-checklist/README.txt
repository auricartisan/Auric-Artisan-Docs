==============================================================================
ACCESSIBILITY CHECKLIST
==============================================================================
What the Accessibility Checklist is, who it is for, and how to start working
through its 50 WCAG 2.2 checks.
Area: Website › Tools › Accessibility and vision   Updated: 2026-09-25

The Accessibility Checklist is a free working checklist of 50 accessibility
checks, grouped into nine areas, from semantics and keyboard focus to forms,
media, colour, motion, ARIA, zoom and testing. Each check is explained in
full: what it means, who it affects, how to test it, what the fix looks like
in code, and what usually breaks it.

You work through it in the Inspector: a list of every check beside the
selected check in full. Mark each one Pass, Fail or N/A, attach annotated
screenshots as evidence, and watch a meter count what is left. When you are
done, print the findings or copy them as Markdown into your issue tracker.
Everything stays in your browser; there is no account and nothing is uploaded.

The page also carries a Reference of what the WCAG levels mean and what the
law asks for in 15 jurisdictions, India first, with links to the primary
sources.

WHO IT IS FOR
=============

  - Front-end developers, designers and accessibility testers preparing or
    running a manual review.
  - Teams who want evidence of a process to go with an automated audit.
  - Anyone who needs to know which accessibility law applies where, and to
    which WCAG version.

WHERE TO FIND IT
================

  - Address: https://auricartisan.com/resources/accessibility-checklist/
  - From any page: open the Learn menu in the site header and select
    Accessibility Compliance ("WCAG checks & guidance").
  - The old addresses https://auricartisan.com/accessibility-compliance/ and
    https://auricartisan.com/compliance forward here. See Accessibility
    Compliance [../accessibility-compliance/README.txt].
  - A single check: add `#check-` and the check's ID, for example
    `https://auricartisan.com/resources/accessibility-checklist/#check-k2`.

QUICK START
===========

  1. Open https://auricartisan.com/resources/accessibility-checklist/. The
     first check, "Landmarks wrap every region of the page", is selected.
  2. Optionally run the automated pass first: select Run the automated pass
     first → to open the Analyzer [../analyzer/README.txt] on your page.
  3. Read the check in the pane on the right (on a phone, tap a row to open
     it).
  4. Test your page as the How to test it block describes.
  5. Select Pass, Fail or N/A. With focus in the list or the pane, you can
     press `Space`, `F` or `N`.
  6. Press `J` to move to the next check, and repeat.
  7. For a failure, select Attach screenshot, add a screenshot and mark it up.
  8. Open the Export tab and select Copy as Markdown or Export the report.

WHAT YOU CAN DO
===============

  - Read 50 checks, each tied to a WCAG 2.2 success criterion or marked as
    good practice, with a code example for most.
  - See which checks the Analyzer can decide for you (AUTO), narrow down
    (PARTLY), or cannot judge (BY HAND).
  - Mark each check Pass, Fail or N/A, and clear a mark by pressing it again.
  - Filter to Required (Level A and AA), AAA or Practice checks, or hide
    passed checks with Open only.
  - Attach any number of screenshots to a check and annotate them with a pen,
    highlighter, arrows, boxes, redaction and numbered callouts.
  - Print the flagged findings, or copy them as Markdown for Jira, Linear or
    GitHub.
  - Look up the accessibility law for India, the United States, the European
    Union, the United Kingdom, Canada, Australia, Japan and eight more
    countries.
  - Work entirely from the keyboard.

IN THIS FOLDER
==============

  - guides/ [guides/README.txt] — how to use the checklist
    - Getting started [guides/getting-started.txt] — the screen tour and your
      first check
    - Work through the checklist [guides/work-through-the-checklist.txt] —
      selecting, marking, filtering and the meter
    - Attach evidence [guides/attach-evidence.txt] — screenshots and the
      annotation pen
    - Export your results [guides/export-your-results.txt] — print, Markdown and
      reset
    - The 50 checks [guides/the-50-checks.txt] — every check by area, with its
      criterion and who can decide it
    - Laws by jurisdiction [guides/laws-by-jurisdiction.txt] — the Reference tab
    - Reference [guides/reference.txt] — every control, label and message
    - Troubleshooting [guides/troubleshooting.txt]
    - FAQ [guides/faq.txt]
  - resources/ [resources/README.txt] — supporting material
    - Glossary [resources/glossary.txt]
    - Keyboard shortcuts [resources/shortcuts.txt]
    - Limits and accuracy [resources/limits-and-accuracy.txt]
    - Related tools and reading [resources/related.txt]
    - Privacy [resources/privacy.txt]
