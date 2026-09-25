---
title: Portfolio — Reference
description: Every control, option, command, message and limit in the Portfolio Builder, the published page and the Portfolio Index.
product: Website › Portfolio
updated: 2026-09-25
---

# Portfolio reference

## Top bar (https://auricartisan.com/portfolio/)

| Control | What it does |
| --- | --- |
| **Your portfolio**, address, **Not published** | Shows your published address and state. |
| Command field (`Ctrl K`) | "Add a section, change the look, publish…" — opens the list of builder commands. |
| Section count, **Saved** / **Saved to your account** | Document size and save state. |
| Undo / Redo | Step back / forward. Disabled when there is nothing to undo or redo. |
| **Templates** | Opens **Start from a template**. |
| **Preview** | Opens the finished page in a new tab. |
| **Export** | **Download HTML**, **Download PDF**, **Export JSON**, **Import JSON…**, **Copy snapshot link**, **"Made with Auric Artisan" credit** switch. |
| **Publish** | Opens the publish dialog; disabled while **Check** has blocking findings. |

## Mode tabs

| Tab | Contents |
| --- | --- |
| **Content** | Header panel, section cards, **Add a section**. |
| **Style** | **Typeface**, **Paper**, **Rhythm**, **Accent, from your library**, **Reset to defaults**. |
| **Check** | Accessibility findings; a dot marks findings while you are elsewhere. |

## Header panel

| Control | Limit | Default |
| --- | --- | --- |
| **Use the built-in header** | On / off | On |
| **Name** | 80 characters | Follows profile |
| **Headline / tagline** | 120 characters | Empty |
| **Email** + **Show** | 120 characters | Follows profile; **Show** off |
| **Location** + **Show** | 80 characters | Follows profile; **Show** on |
| **Website** + **Show** | 200 characters | Follows profile; **Show** on |
| **Avatar** (image address) + **Show** | 500 characters | Follows profile; **Show** on |
| Avatar picker | Double-click the avatar | — |
| **Accent** | Colour picker | `#8A6D16` theme default |

## Section card controls

Drag handle, expand/collapse, **Hidden** badge, **Hide from portfolio** / **Show in portfolio**, **Move up**, **Move down**, **More actions** (**Move to top**, **Move to bottom**, **Duplicate**, **Delete**).

Bulk bar: **Collapse all** / **Expand all**; **Bulk actions ▾**: **Expand all**, **Collapse all**, **Show all sections**, **Hide all sections**, **Reverse order**, **Clear all sections**.

## Section types (25)

Heading, Text / Markdown, Raw HTML, Two columns, Image, Gallery, Button, Call to action, Link list, Work / Projects, Stats, Feature list, Steps, Timeline, Skills / Tags, Testimonial, Quote, Callout, FAQ / Accordion, Table, Embed, Video (MP4), Code, Divider, Spacer. Fields: see [Section types](section-types.md).

## Style options

| Option | Values | Default |
| --- | --- | --- |
| **Typeface** | **Fraunces**, **Newsreader**, **Space Grotesk**, **Manrope** | Fraunces |
| **Paper** | **Cream**, **White**, **Sand**, **Ink**, **No background** | Cream |
| **Rhythm** | **Tight**, **Even**, **Airy** | Even |
| **Accent** | A colour from your saved palettes, graded against the paper | `#8A6D16` |

## Preview

| Control | Values | Default |
| --- | --- | --- |
| Width | **Fit**, **Desktop** (1160 px), **Tablet** (800 px), **Mobile** (390 px) | Fit |
| **Fullscreen preview** | On / off | Off |

## Check findings

| Finding | Severity |
| --- | --- |
| **Text below AA** (under 4.5:1) | Blocking when well below, else warning |
| **Large text below AA** (under 3:1) | Blocking when well below, else warning |
| **A link with no text** | Blocking |
| **A link that does not say where it goes** | Blocking |
| **An image with no alt text** | Blocking |
| **Heading jumps from hN to hM** | Warning |
| **A target smaller than 24px** | Warning |
| **A colour this check could not read** | Warning |

Filters: **All**, **Blocking**, **Contrast**.

## Publish dialog

| Control | What it does | Default |
| --- | --- | --- |
| **Public at an address** / **Only people I send the link to** | Visibility. | Public at an address |
| **Your address** | `auricartisan.com/p/` + 2 to 31 lower-case letters, numbers and hyphens; checked for availability. | Empty |
| **Or take** | Suggested addresses. | — |
| **What a shared link shows** | Share-card preview. | — |
| **Ready to go** | Address, sections, name, headline checklist. | — |
| **Publish** / **Copy the link** | Publishes, or copies a snapshot link in private mode. | — |
| **Copy**, **Open**, **QR code** | For the live address. | — |
| **Publish these changes** | Updates the live page. | — |
| **Reach** | View count since publishing. | — |
| **Let search engines list it** | Search engine listing. | On |
| **List it in the Portfolio Index** | Directory listing; needs search listing on. | On |
| **Allow a PDF download** | PDF button for visitors. | On |
| **Show the view count** | View count on the page. | On |
| **Unpublish** → **Yes, take it down** | Takes the page down; frees the address. | — |
| **Close** | Closes the dialog. | — |

## Commands (command field)

| Group | Commands |
| --- | --- |
| Sections | **Add a … section** for every type; **Start from a template** |
| Editing | **Undo**, **Redo**, **Edit the content**, **Turn the built-in header on** / **off**, **Set the name in the header**, **Set the headline**, **Set the header email**, **Set the header location**, **Set the header website**, **Set the header avatar** |
| Theme | **Change the look**; one command per typeface, paper and rhythm, such as **Paper — Ink** |
| Preview | **Preview: fit the column**, **Preview: check it at desktop**, **Preview: check it at tablet**, **Preview: check it on a phone**, **Preview full screen** |
| Export | **Download it as HTML**, **Download it as PDF**, **Export the document as JSON**, **Import a portfolio from JSON**, **Copy a snapshot link** |
| Publishing | **Publish this portfolio**, **Open a full preview**, **Check the page** |

Commands that cannot run at the moment are not offered.

## Limits

| Limit | Value |
| --- | --- |
| Address length | 2 to 31 characters |
| Published portfolio size | Half a megabyte ("Link images rather than embedding them.") |
| Timeline fold | After 5, 8 or 12 entries, or never |
| Gallery columns | 2, 3 or 4 |
| Feature columns | 2 or 3 |
| Work / Projects items | 3, 6, 9 or 12 |
| Callout icon | Up to 4 characters |

## Messages

| Message | When |
| --- | --- |
| **Added a … section.**, **Section duplicated.**, **Section removed — Ctrl+Z to undo.** | Section actions. |
| **All sections cleared — Ctrl+Z to undo.** and other bulk messages | Bulk actions. |
| **… template applied.** | Template chosen. |
| **HTML downloaded.**, **Portfolio JSON exported.**, **Portfolio imported.** | Export and import. |
| **That file is not a valid portfolio export.** | Import failed. |
| **Allow pop-ups to preview.**, **Allow pop-ups to print.** | Pop-ups blocked. |
| **Public link copied** | Snapshot link copied. |
| **Avatar updated.**, **Turn the built-in header on first.**, **That picture is too large even shrunk. Try a smaller one.**, **That file could not be read as a picture.** | Avatar. |
| **Loaded your portfolio from your account.**, **Loaded the newer draft from your account.** | Draft sync. |
| **Pick something short — this is the whole address.**, **Lower case letters, numbers and hyphens, 2 to 31 characters.**, **Checking…**, **Could not check that just now.** | Address field. |
| **Published at …**, **Could not publish.**, **Unpublished. The address no longer shows anything.** | Publishing. |
| **That portfolio is larger than half a megabyte. Link images rather than embedding them.** | Publish too large. |

## Portfolio Index (https://auricartisan.com/portfolios/)

| Control | Values |
| --- | --- |
| Search | Words, `"phrases"`, `-exclusions`, hex colours, `tag:`, `in:`, `made:here`, `made:elsewhere`, `is:verified` |
| Source | **All**, **Made here**, **Elsewhere** |
| **Filters** | **Verified only**, **Colour** (9 families), **Craft**, **Location** |
| Sort | **Best match**, **Recently updated**, **Newest**, **Name, A to Z**, **Most viewed** |
| View | Grid, List |
| Paging | 24 at a time; **Show N more of M** |
| Keys | `/` focuses search; `Escape` clears it |
