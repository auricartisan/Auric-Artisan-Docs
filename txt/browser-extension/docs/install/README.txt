==============================================================================
INSTALL THE EXTENSION
==============================================================================
Which browsers the extension supports and how to install it on each one, from
a store or from a ZIP package.
Area: Browser extension › Install   Updated: 2026-09-25

The Auric Artisan extension is one product with two store listings: the Chrome
Web Store, which serves every Chromium-based browser, and Firefox Add-ons.
Installing from a store is one click, survives restarts and updates itself.
The product page, https://auricartisan.com/extension, also offers the packages
as ZIP files, for anyone who prefers to load the extension from a folder they
can read first.

SUPPORTED BROWSERS
==================

  Browser:      Google Chrome
  Support:      Full, with the side panel
  Install from: Chrome Web Store [chrome-and-chromium.txt]

  Browser:      Brave, Vivaldi
  Support:      Full, with the side panel
  Install from: Chrome Web Store [chrome-and-chromium.txt]

  Browser:      Arc
  Support:      Installs from the Chrome listing
  Install from: Chrome Web Store [chrome-and-chromium.txt]

  Browser:      Microsoft Edge
  Support:      Full, with the side panel
  Install from: Chrome Web Store or the Edge ZIP [edge.txt]

  Browser:      Opera
  Support:      Full, with the side panel
  Install from: Chrome Web Store or the Opera ZIP [opera.txt]

  Browser:      Firefox 115 and later
  Support:      Full, with the sidebar. The screen eyedropper is not
                available.
  Install from: Firefox Add-ons [firefox.txt]

  Browser:      Safari on macOS
  Support:      Not published. You can convert the Chromium package yourself.
                There is no side panel.
  Install from: Convert with Xcode [safari.txt]

The extension is built on Manifest V3, the current extension format in
Chromium browsers and Firefox. The Chrome, Edge and Opera ZIPs are identical
copies of the same Chromium package, named for their stores. The Firefox
package is a separate build.

WHAT THE BROWSER ASKS WHEN YOU INSTALL
======================================

Every browser shows a permission prompt before it installs the extension. It
says that Auric Artisan can read and change your data on all websites. That is
the host access the tools need to work on whatever page you use them on. A
small script loads on each page and waits until you start a tool, and every
feature that changes a page is off until you turn it on. Permissions
[../permissions.txt] explains each permission.

FILES IN THIS FOLDER
====================

  Page:           Chrome and Chromium browsers [chrome-and-chromium.txt]
  What it covers: Chrome, Brave, Vivaldi and Arc from the Chrome Web Store

  Page:           Microsoft Edge [edge.txt]
  What it covers: Edge from the Chrome Web Store, or from the Edge ZIP

  Page:           Opera [opera.txt]
  What it covers: Opera from the Chrome Web Store, or from the Opera ZIP

  Page:           Firefox [firefox.txt]
  What it covers: Firefox from Firefox Add-ons, and the temporary add-on route

  Page:           Safari [safari.txt]
  What it covers: Converting the Chromium package with Xcode on macOS

  Page:           Load from a ZIP [load-from-a-zip.txt]
  What it covers: Loading an unpacked copy in any Chromium browser or Firefox

  Page:           Update and remove [update-and-remove.txt]
  What it covers: Keeping the extension current, reloading a ZIP copy, and
                  uninstalling
