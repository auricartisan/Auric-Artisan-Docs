---
title: Accessibility Checklist — Work through the checklist
description: Select checks, mark them Pass, Fail or N/A, filter the list, fold areas, read the meter, and use the one-check view on a phone.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Work through the checklist

## Select a check

- **With a mouse or touch:** select a row in the index.
- **With the keyboard:** focus a row, then press `Down` or `Up` to move to the next or previous visible check, and `Home` or `End` for the first or last. Only one row is in the `Tab` order at a time, so `Tab` moves out of the list rather than through every row.
- **From the pane:** select **Previous check** or **Next check**, or press `K` or `J`.
- **From the address:** open `#check-` plus the check's ID, for example `#check-f2`.

The pane's bar shows where the check sits in the full list of 50, for example "12 of 50", whatever filter is on. **Previous check** and **Next check** are disabled at either end of the visible list.

## Mark a check

| Button | Key | Meaning | State word |
| --- | --- | --- | --- |
| **Pass** | `Space` | The page meets this check | Passed |
| **Fail** | `F` | The page does not meet it: it is flagged | Failed |
| **N/A** | `N` | The check does not apply to this page | Not applicable |

- Selecting the active verdict again clears it back to **Not checked yet**.
- `Space` marks **Pass** only when focus is on a row, on the pane, or on the check title. Elsewhere `Space` presses the focused button as usual.
- A screen reader hears the new state word after every mark.

Each row shows its state as a shape as well as a colour:

| State | Symbol |
| --- | --- |
| Not checked yet | An empty ring |
| Passed | A gold disc with a tick; the row title is dimmed |
| Failed | A red disc with an exclamation mark |
| Not applicable | A dashed ring with a dash |

Marks are saved in this browser the moment you make them.

## Where the keys work

The single-key shortcuts (`J`, `K`, `Space`, `F`, `N`, `E`) only respond while focus is inside the index or the pane. They are ignored in text fields, when `Ctrl`, `Alt` or `Cmd` is held, and while the screenshot pen is open. This is deliberate: WCAG 2.1.4 asks that single-character shortcuts do not fire by accident, and the page follows its own advice.

| Key | Action |
| --- | --- |
| `E` | Open the check: on a phone, the one-check view; on a wide screen, focus moves to the pane title |
| `Esc` in the pane | On a phone, back to the list; on a wide screen, focus returns to the check's row |
| `J` from the pane | Next check; focus stays in the pane and the new title is announced |

See [Keyboard shortcuts](../others/shortcuts.md) for the full list.

## Filter the list

The filter buttons at the top of the index:

| Button | Shows | Count |
| --- | --- | --- |
| **All 50** | Every check (default) | 50 |
| **Required** | Level A and AA checks | 35 |
| **AAA** | Level AAA checks | 2 |
| **Practice** | Good-practice checks with no WCAG criterion of their own | 13 |
| **Open only** | A switch that hides checks marked Passed; it combines with any of the buttons above | — |

- **All 50**, **Required**, **AAA** and **Practice** are mutually exclusive.
- **Open only** keeps flagged, not-applicable and untouched checks.
- If the selected check is filtered out, the selection moves to the first visible check.
- `J`, `K`, the arrow keys and **Previous check** / **Next check** skip hidden rows.
- If nothing matches, the index says "Nothing matches these filters." Select **All 50** and switch off **Open only**.
- Filters are not remembered: a reload returns to **All 50**.

There is no text search, no filter by area, and no separate A or AA filter.

## Fold an area

Select an area header (for example "02 Keyboard & focus 0 / 7") to fold or unfold its rows. Folding is not a filter and does not change the meter, but keyboard navigation skips folded rows. Folds are not remembered; every area is open after a reload.

The header's tally is decided out of total, where decided means any mark, including N/A.

## Read the meter

The meter beside the tabs reads, for example, "12 passed · 3 flagged · 33 left … of 50".

- **left** is 50 minus passed, flagged and not-applicable checks. N/A has no bar segment of its own.
- The meter always counts all 50 checks. Filters never change it; the chip beside it says what the list is showing.
- Screen readers also hear a fuller sentence, for example "12 passed, 3 flagged, 33 not yet checked of 50. 2 of the flagged are A or AA.", or, with nothing flagged, how many **required** checks are left.

## On a phone: the one-check view

Below 1080 pixels wide, the index is the page and the pane is hidden.

1. Tap a row. The check opens full-screen, the address changes to `#check-` plus its ID, and focus moves to the title.
2. Read the check and mark it.
3. Use **Previous check** and **Next check** to move through checks without adding to your browser history.
4. Tap **All checks**, or use your browser's Back, to return to the list. The list scrolls to the row you came from and focuses it, and keeps it highlighted.

Turning the phone or widening the window past 1080 pixels closes the one-check view.

## Suggested order of work

1. Run the Analyzer on the page first, so the **AUTO** checks are already decided.
2. Filter to **Required** and work area by area.
3. Flag failures with **Fail** and attach a screenshot to each (see [Attach evidence](attach-evidence.md)).
4. Switch on **Open only** to see what is still to do.
5. Finish with the **Practice** checks, especially area 09, **Testing & proof**.
6. Export (see [Export your results](export-your-results.md)).
