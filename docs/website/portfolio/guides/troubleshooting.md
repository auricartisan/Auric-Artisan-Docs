---
title: Portfolio — Troubleshooting
description: Symptoms, causes and fixes for problems with the Portfolio Builder, publishing and the Portfolio Index.
product: Website › Portfolio
updated: 2026-09-25
---

# Troubleshooting

## The builder shows "Sign in to build your portfolio"

**Why:** Building needs an account.

**What to do:** Select **Sign In**, then return to https://auricartisan.com/portfolio/.

## Publish is greyed out

**Why:** The **Check** pane has one or more blocking findings. The button's tooltip says how many.

**What to do:** Open **Check**, select each **Blocking** finding and fix it. See [Preview and check](preview-and-check.md).

## In the publish dialog, Publish stays disabled

**Why:** The address is not valid or not available yet.

**What to do:** Use 2 to 31 lower-case letters, numbers and hyphens, wait for the availability check, or pick one of the **Or take** suggestions. If it says **Could not check that just now.**, try again in a moment.

## "That portfolio is larger than half a megabyte."

**Why:** Uploaded images (in Image and Gallery sections, or a large avatar) are stored inside the portfolio and make it too big to publish.

**What to do:** Host the images elsewhere and paste their `https://` addresses instead of uploading them.

## Images do not show on the page

**Why:** The address is not `https://`, points to a page rather than an image, or the image host does not allow other sites to show it.

**What to do:** Use a direct `https://` link to the image file, or upload it (keeping the size limit in mind). Add alt text so the Check pane does not flag it.

## My Raw HTML looks different, or parts are missing

**Why:** The builder removes scripts, iframes, forms, event attributes, `javascript:` addresses and fixed or sticky positioning, and limits each `<style>` block to its own section.

**What to do:** See [Markdown and Raw HTML](markdown-and-raw-html.md). Use the **Embed** section for videos and prototypes.

## An embed says "Paste a YouTube, Vimeo, CodePen, Figma or Spotify link."

**Why:** Only trusted hosts are allowed: YouTube, Vimeo, CodePen, Spotify, SoundCloud, Figma, Google and CodeSandbox, over `https://`.

**What to do:** Use a share link from one of those services.

## The Work / Projects section is empty

**Why:** It shows palettes and other items saved in your Library, in this browser. With nothing saved, it says **Your published work will appear here once you save assets in the Library.**

**What to do:** Save palettes from the colour tools or libraries, then reload the builder.

## Undo with Ctrl+Z does nothing

**Why:** Keyboard undo does not respond while you are typing in a field, and may not respond on the builder page at all.

**What to do:** Use the Undo and Redo buttons in the top bar, or the **Undo** and **Redo** commands.

## "Allow pop-ups to preview." or "Allow pop-ups to print."

**Why:** **Preview** and **Download PDF** open a new tab, which your browser blocked.

**What to do:** Allow pop-ups for auricartisan.com.

## The exported PDF has no background colours

**Why:** Browsers can drop backgrounds when printing.

**What to do:** Turn on the print dialog's background graphics option.

## I cannot switch off the credit line

**Why:** Watermark-free exports are part of paid plans.

**What to do:** Keep the credit, or see [Account and billing](../../account-and-billing/README.md). It never appears on your published page.

## A snapshot link does not open

**Why:** The link was cut short when pasted, or the browser is very old.

**What to do:** Copy a fresh link, or publish at an address instead, which has a short link.

## My portfolio is not in the Portfolio Index

**Why:** It was published less than fifteen minutes ago, **List it in the Portfolio Index** or **Let search engines list it** is off, or (for an external portfolio) it is waiting for review.

**What to do:** Check the switches in the publish dialog, or its status in the Search Console's **Portfolios** tab. See [List your portfolio](list-your-portfolio.md).

## "The portfolio index could not be reached"

**Why:** The directory could not load.

**What to do:** Try again later. Builder portfolios are still available at their own addresses.

## My draft is different on another device

**Why:** Drafts sync to your account only when you are signed in. The newer copy wins, but a draft you are actively editing is not replaced.

**What to do:** Sign in on both devices, and reload the builder on the second one.
