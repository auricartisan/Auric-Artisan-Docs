---
title: Info bars and notices — The clock strip
description: Show a live clock under the header and set its format, date, weekday, zone label and time zone from its own menu.
product: Website › Site features › Info bars and notices
updated: 2026-09-25
---

# The clock strip

The clock strip is a live clock under the header. It is **off by default**.

## Turn it on

1. Press `Ctrl` + `,` and select **Highlights**.
2. Switch on **Clock strip** ("Off by default. Turn this on for a live clock, date and timezone above every page.").

It appears under the header (and under the announcement bar, if shown) on every page.

## What it shows

- The flag of your time zone's country, or a globe for other zones.
- The zone's name, for example "India Standard Time" (it reads **Local time** for a moment while the clock starts). "(default)" is added when the site could not match your zone and used a close one.
- The time, ticking every second, for example `10:42:07 AM`.
- The date, the weekday, and the zone's abbreviation with its offset from UTC, for example "EDT · UTC-4" for New York in summer. Where the browser has no abbreviation for a zone, the offset is shown in both places.

Screen readers can read the time on demand; it is not announced every second.

## The Clock settings menu

Right-click anywhere on the clock strip to open **Clock settings**:

| Part | Options |
|---|---|
| Preview | The clock and date as they will look |
| **Format** | **12h**, **24h** |
| **Date** | **Long**, **D/M/Y**, **M/D/Y**, **ISO** |
| **Show** | **Seconds**, **Weekday**, **Zone** (each on or off) |
| **Time zone** | A search box ("Search time zone…") and a list: **Auto-detect**, then common cities with their offsets |
| **Reset** | Returns the clock to its defaults |
| **All settings →** | Opens Settings on the Clock section |

Each change applies at once to the strip and the preview.

### Pick a time zone

1. Right-click the strip.
2. Under **Time zone**, choose a city from the list, or type part of a city, zone or region name (for example `tokyo` or `Europe`). Up to 60 matches are listed; if none match, the list reads "No zones match."
3. Select a zone. The strip switches to it; the list marks your current choice.

Choose **Auto-detect** to follow your device's zone again.

### Reset

**Reset** returns the format to 12-hour, shows seconds, weekday and zone, sets the date to **Long**, and returns the zone to **Auto-detect**.

## How it relates to Settings › Clock

The clock strip and **Settings** › **Clock** share the same choices: 24-hour time, seconds, date format and time zone. A change in one shows in the other. The menu adds three choices that Settings does not have: the **ISO** date format, and the **Weekday** and **Zone** switches. Settings adds **Show date**, which hides the date line.

## Turn it off

Switch off **Clock strip** in Settings › Highlights.
