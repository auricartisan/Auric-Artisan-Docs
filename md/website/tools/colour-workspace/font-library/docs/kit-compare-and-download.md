---
title: Font Library — Your kit, compare and download
description: Select families into Your kit, see them in the Selected view, compare up to four side by side, copy combined embed code, and download self-hosting kits.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Your kit, compare and download

Families you select gather in **Your kit**. The kit is kept in your browser on this device, so it is still there next time, and a second tab of the page sees the same kit.

## Select families

Any of these adds a family to your kit:

- the star (**☆**) on a card, which turns to **★**;
- **＋ Select** in the family panel, which turns to **✓ Selected**;
- **＋ Select both** on the **Pairings** tab, which adds the open family and its partner.

Select the star or the button again to remove the family.

## The Your kit tray

Once something is selected, a **Your kit** button with a count appears in the bottom-right corner. Select it to open the tray: **Your kit** with the count and *Kept in this browser*, a list of families (each with **✕** to remove it), and four buttons:

| Button | What it does | Needs |
| --- | --- | --- |
| **Embed** | Shows combined embed code for the whole kit | 1 family |
| **Download** | Downloads one ZIP of self-hosting kits | 1 family |
| **Compare** | Opens a side-by-side comparison | 2 families |
| **Clear** | Empties the kit | always available |

**Hide** closes the tray.

**Download selected** at the foot of the rail does the same as **Download**, and shows the count, for example **Download selected (3)**.

## The Selected view

The **Selected** view at the top lists your kit as cards with each family's name and category. With nothing selected it reads *Nothing selected yet. Star a family on the Specimens view and it lands here, ready to download as one kit.*

## Compare

Select **Compare** in the tray (or press `C` with two or more families selected). The panel shows up to four families, the first four in your kit, side by side:

| Row | Shows |
| --- | --- |
| **Specimen** | Your preview text, or *Quick brown fox 0123* |
| **Category**, **Designer**, **Weights** | From the catalogue |
| **Variable** | The axis tags, or No |
| **x-height** | In em |
| **Glyphs** | Number of characters |
| **OpenType** | Number of features |
| **Accessibility**, **UI / Product**, **Readability**, **Developer**, **Editorial** | The five scores, colour-coded |
| **License** | The licence name |

Select a family's name at the top of its column to open it. With fewer than two families, the message reads **Select at least 2 families to compare**.

## Combined embed code

**Embed** in the tray shows **Your selection**, *n families ready to embed*, with one block of code:

- a `<link>` to each family's stylesheet;
- or, instead, a single loader `<script>` whose `data-families` lists every family, separated by `|`;
- a `<style>` block with a CSS variable for each family, such as `--font-lora`.

**Copy all** copies the lot; the message reads **Copied combined embed**.

## Download a self-hosting kit

**Download kit** in the family panel (or on the **Styles** tab) downloads one family; **Download** in the tray, or **Download selected**, downloads your whole kit. While it builds, the message reads **Preparing download kit...**, then **Downloaded** and the file name.

| Download | File name |
| --- | --- |
| One family | *Family-name*-font-kit.zip |
| Several families | auric-font-selection-kit.zip |

Inside, each family has its own folder with:

- `fonts/`: the font files;
- `css/`: a stylesheet of `@font-face` rules pointing at those files, and a CSS variable for the family;
- `demo.html`: a page showing the family, which works straight from the folder;
- `README.txt`: the family, category, designer, licence, file list and three steps to use it;
- `LICENSE.txt`: the licence text, when the catalogue has it.

If a file could not be fetched, a `DOWNLOAD_NOTES.txt` at the top of the ZIP says which. Families marked **Installed** are left out, because they are not served; if every family in the request is one of them, the message reads **Only bundled library fonts can be downloaded**.

The ZIP is assembled in your browser from files on the Font CDN. To self-host, keep the folders together and link the stylesheet from your page. More detail is in [Font CDN: self-host a family](../../../../../services/font-cdn/docs/self-host-a-family.md).

## Related

- [Develop and embed](develop-and-embed.md)
- [Privacy](../others/privacy.md)
- [Troubleshooting](troubleshooting.md)
