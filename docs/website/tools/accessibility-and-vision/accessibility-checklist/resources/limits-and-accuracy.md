---
title: Accessibility Checklist — Limits and accuracy
description: What the Accessibility Checklist covers, where its wording and behaviour differ, and what it is not.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Limits and accuracy

## What it covers

- 50 checks: 37 tied to 33 distinct WCAG success criteria at Levels A, AA and AAA, and 13 good-practice checks.
- The masthead describes the checks as spanning "the whole of WCAG 2.2". In practice some criteria have no check of their own, including four added in WCAG 2.2: Dragging Movements (2.5.7), Consistent Help (3.2.6), Redundant Entry (3.3.7) and Accessible Authentication (Minimum) (3.3.8). The [Analyzer](../../analyzer/README.md) checks 2.5.7, 3.2.6 and 3.3.8 automatically.
- Two level tags differ from WCAG: check m2 (text in images, 1.4.5) and check f6 (legal and financial submissions, 3.3.4) are tagged Level A, but WCAG places both criteria at Level AA. Both are still counted as **Required**, so your work is unaffected; only the A and AA counts shift by two.
- Check d3 also asks for `lang` on foreign-language passages, which WCAG covers under 3.1.2 Language of Parts (AA), although the check cites only 3.1.1.

## AUTO, PARTLY and BY HAND

These labels describe what the Analyzer can decide. The checklist does not import Analyzer results. Two AUTO labels are really judgement calls: x1 (an automated pass in continuous integration) is a process check, and c6 (simulating colour-vision deficiencies) needs a person to look at the result.

## Where the wording and the behaviour differ

The current page describes a few things differently from how they work. The docs describe the behaviour.

| The page says | What happens |
| --- | --- |
| **Export the report**: "Self-contained HTML with the screenshots inline" | It opens the browser's print dialog; choose **Save as PDF** for a file |
| **Reset**: "Asks first, and says how much it is about to discard" | It clears everything at once, with no confirmation |
| **Passed**: "Listed by name" in the report | The Markdown gives a count; the printout leaves passed checks out |
| **Not applicable**: "Carried as you marked them" | The Markdown gives a count; the printout leaves them out |
| "The checks, your reasons and every screenshot" | There is no field for reasons; marks and screenshots are kept |
| **What a claim actually needs →** | The link does not switch to the Reference tab; select **Reference** yourself |
| Check c1's **Check a pair** link | Opens the tools collection page, not a contrast checker |

The Evidence count reads "1 screenshots pinned" when there is one screenshot; this is a wording slip, not an error.

## Legal information

The Reference tab is orientation, not legal advice. It was last reviewed on 11 September 2026. Dates in law and regulation move; always check the primary source.

## What it is not

- Not a conformance claim or certification. A worked checklist is evidence of a process.
- Not a replacement for testing with assistive technology and with disabled people; check x5 says so itself.
- Not shared or synced: it is one browser's record of one person's work.
