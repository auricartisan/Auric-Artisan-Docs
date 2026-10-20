---
title: Settings panel — Reference
description: Every control in the Settings panel, with what it does, its values and its default, plus the settings file format and messages.
product: Website › Site features › Settings panel
updated: 2026-09-25
---

# Settings panel reference

All settings apply immediately, are kept in this browser, and are shared by every tab of the site you have open.

## Panel frame

| Control | What it does |
|---|---|
| Title **Your Settings** | Drag to move the panel. The position is remembered. |
| **Focus mode** | Kit-style focus button. Tooltip: "Keep Settings open through navigation and while opening other kits." |
| **Resize** | Switches between normal width and a wider panel (up to 980 px). The choice is remembered. |
| **Minimize** / **Restore** | Collapses the panel to its title bar. Select the bar or the button to restore. |
| **Close settings** (X) | Closes the panel. Focus returns to the control that opened it. |
| Section list | Appearance, Comfort, Highlights, Clock, Tooltips, Ads, Shortcuts, each with a control count |
| **Export** | Downloads `auric-settings.json` |
| **Import** | Loads a settings file |
| **Reset all** | Resets every setting after a confirmation (saved colours are kept) |
| `Ctrl` `,` hint | Reminder of the open and close shortcut |

## Appearance

| Control | What it does | Values | Default |
|---|---|---|---|
| **Preview** | Live sample of heading, accent chip, link, text and button | Read-only | — |
| **Accent on background** | WCAG contrast of the accent against the page background | Ratio and badge | — |
| **Text on accent** | WCAG contrast of the automatic text colour on the accent | Ratio and badge | — |
| Shade strip | Seven shades of the accent; selecting one makes it your accent | 7 swatches | — |
| **Accent color** | Site-wide highlight colour | Gold, Champagne, Rose Gold, Silver, Platinum Grey, Bronze, Copper, Brown, Maroon, Pink, Emerald, Sapphire, Amethyst | Gold |
| **Saved colors** | Your palette of kept accents; select to use, X to remove | Up to 18 | Empty |
| **Custom color** chip | Opens your browser's colour picker | Any sRGB colour | — |
| **+** (**Save this color**) | Adds the custom colour to Saved colors | — | — |
| **Eyedropper** | Samples any pixel on screen as the accent (supported browsers only) | — | — |
| **Theme** | Light, dark, or follow the device | **Light**, **Dark**, **System** | System |
| **Language** | Interface and article language | **English**, **हिन्दी** | English |
| **Text size** | Scales type across the site | **Small** 90%, **Default** 100%, **Large** 112%, **X-Large** 125% | Default |
| **Restore section defaults** | Resets accent, theme and text size | — | — |

Contrast badges: **AAA** 7:1 or more, **AA** 4.5:1 or more, **AA Large** 3:1 or more, **Fail** below 3:1.

## Comfort

| Control | What it does | Values | Default |
|---|---|---|---|
| **Reading mode** | Distraction-free layout with comfortable typography (`Alt` + `R`) | On, off | Off |
| **Reduce motion** | Minimises animations and transitions (`Alt` + `M`) | On, off | Off |
| **Reduce transparency** | Turns off blur and translucency | On, off | Off |
| **Boost contrast** | Stronger text and borders | On, off | Off |
| **Underline links** | Always underlines links in articles and prose | On, off | Off |
| **Custom cursor** | The ring and dot that follow your pointer | On, off | On |
| **Eye-rest reminders** | Reminders to rest your eyes on a schedule | On, off | Off |
| **Reminder interval** | Minutes between reminders | **20m**, **35m**, **45m**, **60m** | 20m |
| **Screen saver** | Ambient colour screen after inactivity | On, off | Off |
| **Start after** | Minutes of inactivity before the screen saver | **1m**, **5m**, **10m**, **20m**, **30m** | 10m |
| **Restore section defaults** | Resets all Comfort settings | — | — |

## Highlights

| Control | What it does | Values | Default |
|---|---|---|---|
| **Live demo chips** | Live / demo chips above demo sections | On, off | On |
| **Welcome bar** | Rotating welcome bar | Off; on (every page); homepage only | Homepage only |
| **Announcement bar** | Site announcements bar | Off; on (every page); homepage only | Homepage only |
| **Quick links bar** | Documentation, changelog, timeline, blog, learn cards | Off; on (every page); homepage only | Homepage only |
| **Clock strip** | Live clock, date and time zone above every page | On, off | Off |
| **Hero notice** | Notice banner on the homepage hero | On, off | On |
| **Restore section defaults** | Resets all Highlights settings | — | — |

"Homepage only" shows the switch as on. Switching it on after it has been off shows the bar on every page.

## Clock

| Control | What it does | Values | Default |
|---|---|---|---|
| **Live preview** | The clock drawn with your settings, updating each second | Read-only | — |
| **24-hour time** | 24-hour format instead of AM / PM (also used by the screen saver clock) | On, off | Off |
| **Show seconds** | Seconds on the live clock | On, off | On |
| **Show date** | Calendar date next to the clock | On, off | On |
| **Timezone** | Zone shown by the clock | **Auto-detect** or any listed zone | Auto-detect |
| **Date format** | How the date is written | **Long**, **DD/MM/YYYY**, **MM/DD/YYYY** | Long |
| **Restore section defaults** | Resets all Clock settings | — | — |

## Tooltips

| Control | What it does | Values | Default |
|---|---|---|---|
| **Live preview** | Sample tooltip reflecting the switches | Read-only | — |
| **Show tooltips** | Rich hover and focus tooltips across the site | On, off | On |
| **Detailed tooltips** | Preview image, metadata and tags | On, off | On |
| **Advanced tooltips** | Data section always expanded; off means press `Alt` to expand | On, off | Off |
| **Restore section defaults** | Resets all Tooltips settings | — | — |

## Ads

Shown only while the site is showing ads. The controls are locked for signed-out and free-plan visitors.

| Control | What it does | Values | Default |
|---|---|---|---|
| **Show ads** | Sponsored slots across the site | On, off | On |
| **Ad density** | In-content slots per page | **Standard**, **Reduced** | Standard |
| **Ads in panels & search** | Compact sponsored strip in kits, Spotlight and search results | On, off | On |
| **Restore section defaults** | Resets all Ads settings | — | — |

## Shortcuts

The Shortcuts section lists the panel's own keyboard shortcuts. It has no settings.

| Keys | Action |
|---|---|
| `Ctrl` + `,` | Open or close settings |
| `Alt` + `R` | Toggle reading mode |
| `Alt` + `T` | Switch theme (light, then dark, then system) |
| `Alt` + `+` | Increase text size |
| `Alt` + `-` | Decrease text size |
| `Alt` + `0` | Reset text size |
| `Alt` + `M` | Toggle reduced motion |
| `Esc` | Close the dialog |

The `Alt` shortcuts do nothing while you are typing in a text field. On a Mac, `Cmd` + `,` also opens the panel. The whole site's shortcuts are in [Keyboard shortcuts](../../keyboard-shortcuts/README.md).

## The settings file

**Export** writes a JSON file named `auric-settings.json`. It starts with two marker fields and then lists every setting:

```json
{
  "_aa": "auric-settings",
  "v": 1,
  "accent": "sapphire",
  "savedColors": ["#2e8b57"],
  "themeMode": "system",
  "textScale": 1.12,
  "reduceMotion": false,
  "customCursor": true,
  "eyeRest": true,
  "eyeRestInterval": 35,
  "time24": true,
  "clockTz": "",
  "dateFormat": "dmy"
}
```

The example is shortened. A real export also includes the remaining switches: `reduceTransparency`, `contrast`, `underlineLinks`, `reading`, `screenSaver`, `screenSaverDelay`, `showWelcome`, `showAnnouncements`, `showQuickLinks`, `showTimeStrip`, `showHeroNotice`, `showDemoBadges`, `showSeconds`, `showDate`, `tipEnabled`, `tipDetails`, `tipAdvanced`, `adsEnabled`, `adsDensity` and `adsInPanels`, plus `recentColors`, an older colour history that is only read to fill Saved colors once.

| Field | Accepted values |
|---|---|
| `accent` | A preset name (`gold`, `champagne`, `rose-gold`, `silver`, `platinum`, `bronze`, `copper`, `espresso`, `maroon`, `rose`, `emerald`, `sapphire`, `amethyst`) or a `#rrggbb` colour |
| `savedColors` | Up to 18 `#rrggbb` colours |
| `themeMode` | `light`, `dark`, `system` |
| `textScale` | `0.9`, `1`, `1.12`, `1.25` |
| `eyeRestInterval` | `20`, `35`, `45`, `60` |
| `screenSaverDelay` | `1`, `5`, `10`, `20`, `30` |
| `dateFormat` | `long`, `dmy`, `mdy` |
| `clockTz` | Empty for auto-detect, or a time zone name such as `Europe/London` |
| `showWelcome`, `showAnnouncements`, `showQuickLinks` | `true`, `false` or `"home"` |
| `adsDensity` | `standard`, `reduced` |
| Other switches | `true` or `false` |

The preset names in the file are fixed identifiers: `espresso` is the **Brown** swatch, `rose` is **Pink**, and `platinum` is **Platinum Grey**. The language is not part of the file; it is kept separately (see [Language](../../language/README.md)).

## Messages

| Message | When it appears |
|---|---|
| Settings exported | After **Export** |
| Couldn’t export settings | The browser refused the download |
| Settings imported | After a successful **Import** |
| That file isn’t valid settings | The chosen file is not valid JSON |
| Couldn’t read that file | The browser could not read the chosen file |
| Appearance / Comfort / Highlights / Clock restored to defaults | After that section's restore |
| Section restored to defaults | After the Tooltips or Ads restore |
| All settings reset to defaults | After a confirmed **Reset all** |
| Theme: Light / Dark / System | After `Alt` + `T` |
| Text size: Small / Default / Large / X-Large | After `Alt` + `+`, `Alt` + `-` or `Alt` + `0` |
| Reduced motion on / Reduced motion off | After `Alt` + `M` |
