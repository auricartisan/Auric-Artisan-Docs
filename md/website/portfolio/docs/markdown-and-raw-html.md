---
title: Portfolio Builder — Markdown and Raw HTML
description: The Markdown the Portfolio Builder understands, and what a Raw HTML section keeps and removes.
product: Website › Portfolio
updated: 2026-09-25
---

# Markdown and Raw HTML

## Markdown

Markdown is a simple way to format text with ordinary characters: `**bold**`, `# Heading`, `- item`. The **Text / Markdown**, **Two columns**, **Callout** and FAQ answer fields accept it.

| You type | You get |
| --- | --- |
| `# Heading` to `###### Heading` | Headings, levels 1 to 6 |
| `**bold**`, `*italic*` | Bold, italic |
| `[label](https://example.com)` | A link |
| `[label](https://example.com "Title")` | A link with a title |
| `<https://example.com>` or a bare `https://example.com` | A link |
| `![alt text](https://example.com/pic.png)` | An image |
| `` `code` `` | Inline code |
| A line of three or more `-`, `*` or `_` | A horizontal rule |
| `> quoted` | A block quote (quotes can contain other Markdown) |
| `- item` or `1. item`, indented for sub-items | Lists, including nested lists |
| `- [ ] task`, `- [x] done` | Task lists, shown as ticked or unticked boxes that visitors cannot change |
| A pipe table with a `---` row, and `:---:` for alignment | A table; wide tables scroll sideways |
| Three backticks, optionally followed by a language | A code block |

Tips:

- Links and images need full `https://` addresses. An address with spaces can be wrapped in angle brackets: `<https://example.com/my file.png>`.
- Images from other websites load on your published page as long as they are served over `https://`.
- A line break inside a paragraph is kept as a line break.

## Raw HTML

The **Raw HTML** section lets you paste your own markup and styles. Because your published page is opened by strangers, the builder cleans the HTML first.

### Kept

- Page structure: `div`, `span`, `section`, `article`, `header`, `footer`, `main`, `nav`, `aside`, `figure`, `details` and `summary`, headings, paragraphs, lists, tables, `hr`.
- Text markup: `strong`, `em`, `code`, `pre`, `blockquote`, `mark`, `small`, `sub`, `sup`, `abbr`, `time`, `kbd` and similar.
- Media: `img`, `picture`, `source`, `video`, `audio`, `track`; also `progress` and `meter`.
- Inline SVG for icons and diagrams: shapes, paths, text, gradients, masks and clip paths.
- Attributes: `class`, `id`, `style`, `role`, `aria-*`, `data-*`, `title`, `lang` and each element's usual attributes (such as `href`, `src`, `alt`).
- `<style>` blocks. The CSS is rewritten so it only affects this one section: it cannot restyle other sections or the site around your page. `@import` is allowed only for Google Fonts.

### Removed

- `<script>` and every event attribute such as `onclick`.
- `<iframe>`, `<object>`, `<embed>`. Use the **Embed** section for videos and prototypes.
- Forms and form controls: `form`, `input`, `button`, `textarea`, `select` and so on.
- `link`, `meta` and `base` elements.
- `javascript:` addresses anywhere, including inside CSS.
- `position: fixed` and `position: sticky`, so a section cannot cover the site's own header.
- SVG features that can fetch or run things, such as `use`, `foreignObject`, `image` and animation elements.

The section's help text sums it up: "Styles, SVG and page structure all work. Scripts, iframes and forms are removed — your page is opened by strangers. A `<style>` block only reaches this section."

### Example

```html
<style>
  .intro { padding: 32px; background: linear-gradient(135deg, #1d2a3e, #3f6fd1); color: #fff; border-radius: 16px; }
  .intro h2 { margin: 0 0 8px; }
</style>
<div class="intro">
  <h2>Hello</h2>
  <p>I design colour systems for small brands.</p>
</div>
```

> **Tip:** For a full-bleed design drawn entirely in Raw HTML, choose the **No background** paper in **Style** so no sheet or padding shows around it.
