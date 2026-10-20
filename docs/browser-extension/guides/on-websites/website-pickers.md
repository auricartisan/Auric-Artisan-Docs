---
title: Browser extension — Website pickers
description: Give a website's form controls Auric pickers — colour, select, multi-select, suggestions, dates, times, number, range, file, checkbox and radio — and control where they apply.
product: Browser extension › On websites
updated: 2026-09-25
---

# Website pickers

With the website pickers on, a page's own form controls open Auric panels instead of the browser's. The page's native control stays in place for form submission, and the site's code receives every value through the same `input` and `change` events it always does, so forms built with frameworks keep working.

## Turn them on

1. Open **Settings** › **Pickers**.
2. Turn on **Auric pickers on websites** ("Colour, date, select and ten more open Auric panels instead of the browser's own.").
3. Reload any page that was already open.

## Controls

Each type has its own chip under **Picker types**, all on by default. The heading shows how many are on, for example "13 of 13 on".

| Chip | Enhances | What you get |
|---|---|---|
| **Colour** | Colour inputs | The compact colour picker; see [Colour picker on pages](colour-picker-on-pages.md) |
| **Select** | Drop-down lists | A dropdown. Lists with more than 7 options open with a search field. |
| **Multi-select** | Lists that allow several choices | A dropdown with checkboxes, chips for what is chosen, an "N/M chosen" count, **Select all** and **Clear** |
| **Suggestions** | Text fields with a suggestion list | A searchable suggestion list |
| **Date** | Date fields | A calendar in your interface language |
| **Date & time** | Date-and-time fields | Calendar and time panels |
| **Month** | Month fields | A month panel |
| **Week** | Week fields | A week panel |
| **Time** | Time fields | A time panel |
| **Number** | Number fields | A stepper whose buttons switch off at the minimum and maximum |
| **Range** | Sliders | A slider with an editable value beside it |
| **File** | File fields | A themed button with the chosen file's name. The browser's own file dialog still opens. |
| **Checkbox & radio** | Checkboxes and radio buttons | Themed marks; the native control still handles the keyboard and the form |

## Search in long lists

Dropdowns with **more than 7 options** open with a search field:

- typing filters the list and underlines the matching text;
- groups keep their headings;
- when nothing matches, "No options match" offers to clear the search.

Shorter lists stay plain, and typing a letter jumps to the first match. In a multi-select with a search typed, **Select all** selects only the matches.

## Theme

- With the theme set to **Dark** or **Light** (Settings › Appearance), every picker uses that theme.
- On **System**, pickers match the page they are on: dark on a dark site, light on a light one.

Pickers also use your accent colour.

## Where pickers stay native

- **auricartisan.com**, always. The site ships its own pickers; it appears locked at the top of the **Never on** list.
- **Sites on the Never on list.** In Settings › Pickers › **Never on**, type a site such as `example.com` and choose **Add**. Subdomains are included, and a leading `www.` is ignored. Remove a site with its **✕**. The list holds up to 100 sites.
- **Types you switch off** under **Picker types**.
- **Controls the site designed**, while **Leave designed controls alone** is on (the default): "If a site already styles a control, it keeps its own." A control the site restyled, or hid behind its own widget, is left exactly as it is. Colour inputs are the exception: they are replaced unless hidden, disabled or read-only.
- **Controls the site opted out**; see [For site owners](for-site-owners.md).
- **Frames inside a page**, which the extension does not reach.

## Related pages

- [Colour picker on pages](colour-picker-on-pages.md)
- [Pickers settings](../settings/pickers.md)
- [Troubleshooting](../troubleshooting.md)
