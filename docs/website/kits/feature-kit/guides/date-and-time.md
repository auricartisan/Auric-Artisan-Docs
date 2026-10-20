---
title: Feature Kit — Date & Time
description: Use the Feature Kit's Date & Time tool to read a date in many formats, count days between dates, add or subtract time, and watch world clocks.
product: Website › Kits › Feature Kit
updated: 2026-09-25
---

# Work with dates and times

**Date & Time** is a small date workbench with four tabs: **Calendar**, **Difference**, **Add / Subtract** and **Timezones**. Dates are written in the format of the site's language, or of your browser if the site has no preference.

Open it with the **Date & Time** card on the Feature Kit menu, or press `5` on the menu.

## The calendar picker

All four tabs use the same calendar:

- The month and year sit at the top, with **‹** (previous month) on the left and **«** (previous year), **»** (next year) and **›** (next month) on the right.
- The week starts on Sunday: **Su Mo Tu We Th Fr Sa**.
- Today is marked. The selected day is highlighted. Weekends and days from the neighbouring months look different.
- **Clear** removes the selection. **Today** selects today and jumps to its month.

## Calendar tab: read a date in every format

1. Select the **Calendar** tab (it opens first).
2. Pick a day. Today is selected when you arrive.
3. Set the time of day in the **Time** box if it matters.

Under the calendar you see the date in ISO form with a relative description (**Today**, **Tomorrow**, **Yesterday**, **in 12 days**, **3 days ago**), then one row per format, each with a **Copy** button:

| Row | Example |
|---|---|
| **Full (culture)** | The full date and short time in your locale, for example Thursday 24 September 2026 at 14:05 |
| **Long date** | 24 September 2026 |
| **ISO 8601** | 2026-09-24T14:05 |
| **Unix (s)** | Seconds since 1 January 1970 UTC, for your local date and time |
| **Day of year** | 267 |
| **ISO week** | W39 · 2026 |
| **Weekday** | Thursday |

Selecting **Copy** copies that row's value; the button briefly shows a tick. If copying is blocked it shows **Failed**.

### Recent dates

Every day you pick is added to a **Recent** row of chips, newest first, up to 8. Each chip shows the month and day. Select a chip to jump back to that date. The list is kept in your browser.

If you select **Clear**, the details read **No date selected. Pick a day above.**

## Difference tab: count the time between two dates

1. Select **Difference**.
2. Select the **From** field and pick a date. It starts on today.
3. Select the **To** field and pick a date. It starts 30 days from today.

The result shows six figures:

| Figure | How it is worked out |
|---|---|
| **Days** | Calendar days from **From** to **To**. Negative if **To** is earlier |
| **Weeks** | Days divided by 7, to 2 decimal places |
| **Months (≈)** | Days divided by 30.437, to 2 decimal places |
| **Years (≈)** | Days divided by 365.25, to 3 decimal places |
| **Business days** | Days that are Monday to Friday, counting the **To** date but not the **From** date. Public holidays are not taken into account |
| **Hours** | Days multiplied by 24 |

If either field is empty, you see **Pick two dates.**

Each date field shows the chosen date written out in full. Select it to open its calendar; picking a day closes the calendar again.

## Add / Subtract tab: shift a date

1. Select **Add / Subtract**.
2. Pick the **Start date**. It starts on the date selected in the Calendar tab, or today.
3. Type a whole number in **Amount** (it starts at 30).
4. Choose a **Unit**: **days**, **weeks**, **months** or **years**.
5. Choose a **Direction**: **after (+)** or **before (−)**.

The result shows the new date in ISO form and written out in full, and updates as you change any field.

When you add months or years and the day does not exist in the target month, the date moves to that month's last day. For example, 31 January plus 1 month gives 28 or 29 February.

If the start date is empty, you see **Pick a date.**

## Timezones tab: world clocks

Select **Timezones** to see live clocks, updating every second, in 24-hour time with seconds and the local date for each place:

- UTC
- New York
- Los Angeles
- London
- Berlin
- Kolkata
- Tokyo
- Sydney

Daylight saving time is applied automatically for each place. The list of places is fixed. The clocks stop updating while you are in another Feature Kit tool and restart when you come back.

## Related

- [Developer Tools](developer-tools.md) — the **Epoch** tool converts Unix timestamps in both directions
- [Reference](reference.md)
