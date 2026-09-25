---
title: Browser extension — Troubleshooting
description: Symptoms, causes and fixes for the Auric Artisan browser extension — page tools, the eyedropper, pickers, the right-click menu, shortcuts, audits and data.
product: Browser extension
updated: 2026-09-25
---

# Troubleshooting

Find your symptom, read why it happens, and try the fix. If nothing here helps, reload the page, then reload the extension from your browser's extensions page.

## Page tools

| Symptom | Why | What to do |
|---|---|---|
| The site chip says **No page**, or a page tool does nothing | Browsers do not let extensions run on their own pages (settings, new tab, `chrome://`, `about:`) or on the web stores | Open an ordinary web page |
| Page tools do nothing on a local file | Extensions cannot reach `file://` pages by default | In a Chromium browser: extensions page › Auric Artisan › **Details** › **Allow access to file URLs** |
| A tool worked on other tabs but not on one opened before you installed | The page was loaded before the extension existed | Reload the tab. The extension also tries to start itself there when you use a tool. |
| "Could not scan this page" or "No active tab" | The page is protected, still loading, or no normal tab is active | Wait for the page to load, click into it, and try again |
| Nothing is found inside an embedded frame | The extension runs in the top page only | Open the frame's own address in a tab |
| You limited the extension's site access | Page tools work only on sites you allowed | Allow the site from the extension's toolbar menu or details page |

## Eyedropper and colours

| Symptom | Why | What to do |
|---|---|---|
| **Pick from page** shows "This browser has no screen eyedropper" | Firefox, and some other browsers, do not offer the eyedropper feature | Use **Page palette**, which reads every colour the page uses |
| The right-click menu says "Eyedropper needs Chromium" | Same reason | As above |
| The picked colour is slightly different from the design file | The screen eyedropper reads rendered pixels, after colour management, scaling and anti-aliasing | Pick from a flat area, or read the CSS value with the inspector or Page palette |
| Image says "Could not read this image (cross-origin protected)" | The image's site does not allow its pixels to be read | Save the image and drop the file in, or use **Capture the visible tab** |
| "Can't capture this tab" | The tab is a browser page or cannot be captured | Try an ordinary page |

## Website pickers

| Symptom | Why | What to do |
|---|---|---|
| Pickers do not appear | The master switch, the type, or the site list stops them | In Settings › Pickers, check the master switch, the type's chip and **Never on**; then reload the page |
| Pickers never appear on auricartisan.com | By design: the site has its own pickers | — |
| A dropdown still looks like the site's own | It is probably a custom widget, not a real form control, or the site designed it | Pickers only enhance real controls. To override designed controls, turn off **Leave designed controls alone**. |
| A site's form behaves oddly with pickers on | A rare conflict with the site's own scripts | Add the site to **Never on** in Settings › Pickers |

## Right-click menu

| Symptom | Why | What to do |
|---|---|---|
| The custom menu does not appear | It is off, or the permission prompt was declined | Turn on Settings › Right-click › **Custom right-click menu** and accept the prompt |
| It does not appear on one site | The site is under **Never on**, opts out, or shows its own menu | With **Step aside** on, a site's own menu wins where it has one. Remove the site from **Never on** if you added it. |
| It replaced a site's own menu | **Step aside for a site's own menu** is off | Turn it on, or add the site to **Never on** |
| You need spellcheck or the dictionary | Only the browser's menu has them | **Shift** + right-click, or choose **Browser's own menu** and right-click again |
| Paste, Save or Reopen closed tab shows **Allow** | The optional permission is not granted | Settings › Right-click › **Permissions** › **Allow** |
| "Clipboard blocked — press Ctrl+V to paste." | The browser refused clipboard access for this page | Press `Ctrl` + `V` |
| Open link in private window fails | The extension is not allowed in private browsing | Allow it in private or incognito windows on the extension's details page |
| Items are missing from the browser's own menu | **Items in the browser's menu** is off | Turn it on in Settings › Right-click |

## Shortcuts

| Symptom | Why | What to do |
|---|---|---|
| A shortcut does nothing | Another extension or the browser uses the same keys | Reassign it: Settings › Shortcuts › **Change them in the browser** |
| Inspect or full-audit shortcuts do nothing | They have no key by default | Assign one on the browser's shortcuts page |
| A shortcut opened the wrong thing much later | It cannot: queued commands are dropped after 30 seconds | — |
| `Alt` + `Shift` + `C` or `E` did not open the popup | Some browsers do not let an extension open its popup by itself | Open the popup within 30 seconds; it goes straight to the tool |

## Inspector

| Symptom | Why | What to do |
|---|---|---|
| The inspector closed when I clicked | You went to another page, pressed Back or Forward, or the site changed route | Start it again. Before 1.0.2 it also closed on sites that rewrite their address on each click; update. |
| The card lost its element | The page removed the element | Pin another element |
| The ratio has "≈" in front | The text sits on an image or gradient | Check the lightest area under the text by eye |
| Live CSS changes stay on the page | Previews last until you reset | Choose **Reset** or **Stop**, or reload the page |

## Audit

| Symptom | Why | What to do |
|---|---|---|
| Few results on a large page | Scan limits were reached | Turn on Settings › Tools › **Deep page audit** |
| Some text is never checked | Text in frames, images or canvas cannot be measured, and some modern colour functions are skipped | Check those areas with Contrast and the inspector |
| Findings disappeared | Results live only while the extension is open | Export JSON or CSV before closing |
| Outlines vanished | They clear after 15 seconds | Choose **Outline on page** again |

## Data and appearance

| Symptom | Why | What to do |
|---|---|---|
| The popup is too small or too big | Popup size setting, or the browser's popup limits | Settings › Appearance › **Popup size**, or use the side panel |
| Something broke after changing settings | A setting combination you do not want | Settings › Data › **Reset all settings**. History, library and snippets are kept. |
| "Restore failed — invalid file" | The file is not an Auric Artisan backup, or it is damaged | Choose a file made by **Download a backup** |
| "Import failed" | The pasted text is not valid settings JSON | Copy the settings again with **Copy settings** |
| My colours are gone after reinstalling | Uninstalling deletes everything the extension stored | Restore from a backup if you made one |
| The toolbar badge shows a number | It counts the colours in your library | Remove colours from the library, or ignore it |
| The side panel button does nothing | Some browsers open side panels only from their own controls | Open it from the browser's side panel or sidebar menu |

## Related pages

- [FAQ](faq.md)
- [Permissions](permissions.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
