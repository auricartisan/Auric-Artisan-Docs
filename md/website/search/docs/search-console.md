---
title: Search — Set up the Search Console
description: How to sign in to the Auric Artisan Search Console, add your site and prove you own it with a file, a meta tag or a DNS record.
product: Website › Search
updated: 2026-09-25
---

# Set up the Search Console

The Search Console at https://auricartisan.com/search/console/ shows what Auric Artisan's crawler found on a site you own, which searches put it in front of people, and, for every page that is not indexed, the reason why. It is free, for any site you own.

The console covers Auric Artisan's own web index only. What you do here changes what this index knows about your site. It has no effect on how you appear in Google, Bing or anywhere else.

## Before you start

- You need an Auric Artisan account. The account is needed only so that a site stays yours.
- You need to be able to change one of these for your site: a file on the web server, the home page's HTML, or the domain's DNS records.

## Sign in

1. Open https://auricartisan.com/search/console/.
2. If you are signed out, the page explains the console under **Your site, in the index**. Select **Sign in to start**, sign in, and come back.

## Add your site

1. Open **Your sites** in the console's side rail. With no sites yet, the page says **No properties yet. Add one below, then prove you own it.**
2. Under **Add another site**, type your domain in **Domain or URL prefix**, for example `example.com`.
3. Select **Add** or press `Enter`. The page says **Added. Prove you own it and the crawler will start.**

A domain covers every page on it, including subdomains. There is no limit on how many sites you keep.

The field also accepts a full address such as `https://example.com/docs/`. Check the name shown in the list after adding it: at present the console registers the whole domain, `example.com`.

Until you prove ownership, the site shows as pending, the other sections of the console are unavailable, and nothing is crawled.

## Prove you own it

The console opens a panel headed **Prove you own** your site. Choose one of three methods. Any one is enough.

| Method | Label | What you do |
| --- | --- | --- |
| **File on the site** | Quickest | Serve a text file at the address shown, containing the token. Easiest on a static site. |
| **Meta tag** | No deploy | Add the meta tag shown to the head of your home page. |
| **DNS TXT record** | Strongest | Add a TXT record on your domain with the value shown. Covers every subdomain and survives a redeploy. |

Each method shows exactly what to add, with a **Copy** button:

- File: an address of the form `https://example.com/auric-site-verification-TOKEN.txt`. The file must contain the token.
- Meta tag: a line of the form `<meta name="auric-site-verification" content="TOKEN">`, to go in the head of `https://example.com/`.
- DNS: a TXT record whose value begins `auric-site-verification=`.

Then:

1. Add the file, tag or record to your site.
2. Select **Check now**. All three methods are tried, in order, whichever one you set up.
3. If one works, the page says **Verified by** that method, and the console opens.
4. If none works yet, the page says **Not verified yet — here is what each check found.** Each method is listed with ✓ or ✕, where it looked, what went wrong, what it **expected** and what it **found instead**. Fix what it names and select **Check now** again.

A new DNS record can take an hour to become visible. If the DNS check fails straight after you add the record, wait and try again.

## After verification

- A green line reads **Ownership proven** by your method and date. Ownership is re-checked periodically, and you are told if the proof disappears.
- Keep the file, tag or record in place. Removing a meta tag later un-verifies the site.
- Your home page is queued for crawling straight away.
- The header shows when the site was last crawled and how many addresses are queued, for example **Crawled 3 hours ago • 42 queued for the next pass**.

## The console at a glance

The side rail has these sections. All but **Your sites** and **Portfolios** need a verified site.

| Section | What it shows |
| --- | --- |
| **Overview** | Indexed pages, impressions, clicks, average position, and why pages are not indexed. |
| **Performance** | Searches, pages, days, countries and devices, with impressions, clicks, click-through and position. |
| **Coverage** | Every address the crawler knows, grouped by what you can do about it. |
| **Pages** | Every address, by folder or as a list, with inspection. |
| **Links** | The site's rank; link reports are not collected yet. |
| **Submit** | Ask for a page or a sitemap to be crawled; the queue and your sitemaps. |
| **Your sites** | Every site on your account; adding and removing sites. |
| **Portfolios** | Your entries in the Portfolio Index. |

With more than one site, choose which one the console shows from the switcher in the header. Every section then shows that site.

At the top, **7d**, **28d** and **90d** set the period for every dated figure. The default is **28d**.

## Next steps

- [Read the console reports](console-reports.md)
- [Request a crawl](request-a-crawl.md)
- [Manage your sites](manage-your-sites.md)
- Listing a portfolio from the **Portfolios** section is covered in the Portfolio documentation: [List your portfolio](../../portfolio/docs/list-your-portfolio.md).
