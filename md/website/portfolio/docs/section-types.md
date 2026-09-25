---
title: Portfolio Builder — Section types
description: All 25 section types in the Portfolio Builder and every field and option each one has.
product: Website › Portfolio
updated: 2026-09-25
---

# Section types

The **Add a section** panel offers 25 types, in this order. Each entry lists the tile's hint and every field on the section's card. Fields marked "Markdown" accept the Markdown described in [Markdown and Raw HTML](markdown-and-raw-html.md).

## Text and structure

### Heading — "Section title"

| Field | Values | Default |
| --- | --- | --- |
| **Text** | Any text | Empty |
| **Size** | **H1**, **H2**, **H3** | H2 |
| **Align** | **Left**, **Center**, **Right** | Left |

### Text / Markdown — "Rich text with Markdown"

| Field | Values |
| --- | --- |
| **Markdown** | Markdown text. "Supports headings, bold/italic, links, images, lists, quotes, code." |

### Raw HTML — "Paste custom HTML (sanitised)"

| Field | Values |
| --- | --- |
| **HTML** | Your HTML, including `<style>`. "Styles, SVG and page structure all work. Scripts, iframes and forms are removed — your page is opened by strangers. A `<style>` block only reaches this section." |

### Two columns — "Side-by-side Markdown"

| Field | Values |
| --- | --- |
| **Left column (Markdown)** | Markdown |
| **Right column (Markdown)** | Markdown |

## Images and media

### Image — "A single image"

| Field | Values | Default |
| --- | --- | --- |
| **Image URL** | An `https://` address | Empty |
| **Or upload** (**Choose image**) | An image file from your device | — |
| **Alt text** | A description for screen readers | Empty |
| **Caption** | Text under the image | Empty |
| **Width** | **Full**, **Half**, **Small** | Full |
| **Links to** | An optional address the image opens | Empty |

Uploaded images are stored inside the portfolio itself, which makes it larger (see [Limits and accuracy](../others/limits-and-accuracy.md)).

### Gallery — "A grid of images"

| Field | Values | Default |
| --- | --- | --- |
| **Columns** | **2**, **3**, **4** | 3 |
| Image list | One address per row; ✕ removes a row | Empty |
| **+ Add image** | Adds an empty row | — |
| **Upload images** | Several files at once | — |

### Embed — "YouTube, Vimeo, CodePen, Figma…"

| Field | Values |
| --- | --- |
| **Embed URL** | A YouTube, Vimeo, CodePen, Figma, Spotify, SoundCloud, Google or CodeSandbox link. "Only trusted embed hosts are allowed." |

YouTube and Vimeo page links are converted to their player addresses automatically. Other links must be `https://` addresses on one of those services.

### Video (MP4) — "A self-hosted video URL"

| Field | Values |
| --- | --- |
| **MP4 URL** | An address of an MP4 or WebM video. Shown with player controls. |

## Actions and links

### Button — "A call-to-action link"

| Field | Values | Default |
| --- | --- | --- |
| **Label** | Button text | Empty |
| **URL** | `https://…` or `mailto:…` | Empty |
| **Style** | **Solid**, **Outline** | Solid |
| **Align** | **Left**, **Center**, **Right** | Left |

### Call to action — "A banner with a button"

| Field | Values |
| --- | --- |
| **Heading** | Banner heading |
| **Text** | A line of text |
| **Button label** | Button text |
| **Button URL** | `https://` or `mailto:` |

### Link list — "Social / contact links"

| Field | Values | Default |
| --- | --- | --- |
| **Title** | A heading for the list | Find me |
| Links | A label and an address per row; ✕ removes | One empty row |
| **+ Add link** | Adds a row | — |

Links without a label are not shown.

## Your work

### Work / Projects — "Showcase your library assets"

| Field | Values | Default |
| --- | --- | --- |
| **Title** | A heading | Selected work |
| **Show** | **All library assets**, **None (placeholder)** | All library assets |
| **Max** | **3**, **6**, **9**, **12** | 6 |

The card tells you how many assets it found in your Library. Each item in the section shows up to six colours of a saved palette as swatches labelled with their hex codes, the item's name and the tool it came from. Visitors can select a swatch to read it against the page, and copy the palette with **CSS** or **JSON**. When you publish or copy a snapshot link, the builder stores a copy of the items at that moment, so visitors see your work rather than anything in their own browser. With nothing saved, the section says **Your published work will appear here once you save assets in the Library.**

### Skills / Tags — "A row of tags"

| Field | Values | Default |
| --- | --- | --- |
| **Title** | A heading | Skills |
| **Tags (comma separated)** | For example `Colour, Type, Design systems` | Empty |

## Lists

These sections hold rows. Each row has its own fields, and the rows can be added, moved and removed in the card or in the preview.

### Stats — "A row of numbers / metrics"

| Field | Values |
| --- | --- |
| **Title** | Optional |
| **Metrics** | A value and a label per row (for example `50+` and `Projects`); **+ Add metric** |

### Feature list — "Icon + title + text cards"

| Field | Values | Default |
| --- | --- | --- |
| **Title** | Optional | Empty |
| **Columns** | **2**, **3** | 3 |
| **Features** | An icon, a title and a description per row; **+ Add feature** | Three empty rows |

### Steps — "A numbered process"

| Field | Values | Default |
| --- | --- | --- |
| **Title** | A heading | How it works |
| **Steps** | A title and a description per row; **+ Add step**. Steps are numbered automatically. | Two empty rows |

### Timeline — "A life — work, study, awards, projects"

| Field | Values | Default |
| --- | --- | --- |
| **Title** | A heading | Experience |
| **Layout** | **Rail**, **Compact**, **Cards** | Rail |
| **Group by** | **Nothing**, **Year**, **Decade** | Nothing |
| **Order** | **As listed**, **Newest first**, **Oldest first** | As listed |
| **Show at first** | **Everything**, **5, then fold**, **8, then fold**, **12, then fold** | Everything |
| **Label each entry with its kind** | On or off | On |
| **Entries** | Per row: date, title, subtitle, **Kind** (**No kind**, **Work**, **Education**, **Award**, **Project**, **Life**, **Travel**), **Still going**, link, description. **+ Add entry**; rows can be reordered. | One row |

Dates are free text, such as `2022 — Now` or `Summer 1998`; the builder reads the year out of them for sorting and grouping but always shows what you typed. Sorting uses the end year of a range; grouping uses its start year. Entries without a year keep their place. With a fold, the remaining entries sit under a "N earlier" line that visitors can open.

### FAQ / Accordion — "Expandable questions"

| Field | Values | Default |
| --- | --- | --- |
| **Title** | A heading | FAQ |
| **Questions** | A question and an answer (Markdown) per row; **+ Add question** | One row |

Each question opens and closes on the page.

## Quotes and notes

### Testimonial — "A quote with attribution"

| Field | Values |
| --- | --- |
| **Quote** | The testimonial |
| **Name** | Who said it |
| **Role / company** | Their role |

### Quote — "A pulled quote or testimonial"

| Field | Values |
| --- | --- |
| **Quote** | The quote |
| **Attribution** | Who said it |

### Callout — "A highlighted note"

| Field | Values | Default |
| --- | --- | --- |
| **Tone** | **Info**, **Success**, **Warning**, **Danger** | Info |
| **Icon** | Up to four characters, such as an emoji | A light-bulb emoji when empty |
| **Text (Markdown)** | The note | Empty |

## Data and code

### Table — "A simple data table"

| Field | Values |
| --- | --- |
| **Title** | Optional |
| **Headers (comma separated)** | For example `Plan, Price, Seats` |
| **Rows (comma per cell, one row per line)** | For example `Starter, $9, 1` on one line and `Pro, $29, 5` on the next |

Wide tables scroll sideways on narrow screens.

### Code — "A code snippet"

| Field | Values |
| --- | --- |
| **Language** | For example `js`, `css`, `html` |
| **Code** | The code, shown exactly as typed |

## Spacing

### Divider — "A horizontal rule"

No fields. "A simple horizontal divider."

### Spacer — "Vertical breathing room"

| Field | Values | Default |
| --- | --- | --- |
| **Size** | **Small**, **Medium**, **Large** | Medium |

## Empty sections

A section with nothing to show displays a short prompt in the preview, such as **Add an image URL or upload a file.**, **Add images to the gallery.**, **Add some metrics.**, **Add timeline entries.**, **Add questions.**, **Add features.**, **Add steps.**, **Add headers and rows.**, **Add an MP4/WebM video URL.** or **Paste a YouTube, Vimeo, CodePen, Figma or Spotify link.**
