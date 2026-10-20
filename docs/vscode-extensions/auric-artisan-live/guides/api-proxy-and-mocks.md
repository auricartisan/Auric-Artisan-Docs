---
title: Auric Artisan Live — proxy an API, mock endpoints and a REST database
description: Forward API paths to a backend, answer endpoints that do not exist yet, and serve a full REST API from a JSON file with Auric Live.
product: VS Code extensions › Auric Artisan Live
updated: 2026-09-25
---

# Proxy an API, mock endpoints and a REST database

Auric Live can answer a request in several ways. For each request it tries, in order: a **mock route**, the **REST database**, a **proxy rule**, then **static files** (or a CGI handler). So you can forward a whole API to a real backend and still override one endpoint with a mock.

## Proxy an API path to a backend

A *proxy* forwards requests for a path to another server and passes the answer back. With `/api` proxied to your backend, the page and its API share one origin: no CORS workaround, no hard-coded backend address in your front-end code, and cookies behave as they will in production.

### Add a rule from VS Code

1. Run **Auric Live: Add API Proxy Route…**, or select the arrows button in the **Routes and Mocks** view title bar.
2. **Proxy route (1 of 2):** enter the path prefix to forward, for example `/api`. It must start with `/`.
3. **Proxy route (2 of 2):** enter where it should go, for example `http://localhost:3000`. It must start with `http://` or `https://`.
4. Auric Live says **Auric Live now forwards /api to http://localhost:3000. This lasts for the session.** Choose **Save to config file** to keep it in `auric.live.json`.

Rules added this way forward WebSockets and rewrite the `Host` header to the target.

### Write rules in the project file

The short form maps a prefix to a target:

```json
{
  "proxy": { "/api": "http://localhost:3000" }
}
```

The full form is a list of rules:

```json
{
  "proxy": [
    {
      "path": "/api",
      "target": "http://localhost:3000",
      "changeOrigin": true,
      "ws": true
    }
  ]
}
```

| Field | Default | Meaning |
| --- | --- | --- |
| `path` | — | Path prefix to forward (also accepted as `context`) |
| `target` | — | Backend address; must be `http://` or `https://` |
| `pathRewrite` | none | Rewrites as pattern–replacement pairs, for example `{ "^/api": "" }`; each pattern is a regular expression |
| `stripPrefix` | `false` | Remove the matched prefix before forwarding |
| `changeOrigin` | `true` | Send the target's host as the `Host` header |
| `secure` | `false` | Verify the target's HTTPS certificate |
| `ws` | `true` | Forward WebSocket connections |
| `headers` | none | Extra request headers to send to the target |
| `cookieDomainRewrite` | `true` | Rewrite cookie domains so cookies from the backend work on the Auric Live address |
| `healthPath` | none | An absolute path that must answer 200–399 before the target counts as ready |
| `timeoutMs` | `30000` | How long to wait for the target (100 to 600000) |

The **Routes and Mocks** view lists each rule as `/api →` with its target. Rules can also be set in the `auricLive.proxy` setting. Proxy rules need a trusted workspace.

While the backend starts, requests wait instead of failing. See "Waiting for a backend" in [Run a backend or framework dev server](run-targets-and-backends.md).

A few details that keep a proxied site working:

- When rules overlap, the longest matching prefix wins.
- A redirect from the backend is pulled back to the Auric Live address, so a login redirect does not send you to the backend's own port.
- Cookies lose their `Domain` and, over plain HTTP, their `Secure` flag, so the browser keeps the session cookie.
- HTML pages that come through the proxy get the Auric script injected like static pages, so the developer dashboard works on a proxied site too.

## Mock endpoints

A *mock route* is an endpoint Auric Live answers itself, with the status, headers, delay and body you declare. Use it to build a front end against an API that does not exist yet.

### Add one from VS Code

1. Run **Auric Live: Add Mock API Route…**, or select the beaker button in the **Routes and Mocks** view title bar.
2. **Mock route (1 of 3):** choose the method: `GET`, `POST`, `PUT`, `PATCH` or `DELETE`.
3. **Mock route (2 of 3):** enter the path. Named parameters (`:id`) and wildcards (`*`) are supported.
4. **Mock route (3 of 3):** enter the JSON body. It must be valid JSON.
5. Auric Live turns mocks on and says **Auric Live now answers *GET /api/example*.** Choose **Save to config file** to keep it.

The status is 201 for `POST` and 200 otherwise.

### Write routes in the project file

```json
{
  "mock": {
    "enabled": true,
    "delayMs": 0,
    "routes": [
      {
        "method": "GET",
        "path": "/api/health",
        "status": 200,
        "body": { "ok": true }
      },
      {
        "method": "POST",
        "path": "/api/session",
        "status": 201,
        "delayMs": 250,
        "body": { "id": "{{uuid}}", "user": "{{body.user}}", "issued": "{{now}}" }
      }
    ]
  }
}
```

A short form maps `"METHOD /path"` to a body: `{ "GET /api/users": [ … ] }`. Without a method, `GET` is assumed.

| Field | Default | Meaning |
| --- | --- | --- |
| `method` | `GET` | HTTP method, or `*` for any |
| `path` | — | Route pattern; must start with `/` |
| `status` | `200` | Status code, 100–599 |
| `headers` | none | Response headers |
| `body` | — | Response body (JSON or text) |
| `file` | — | A file to send as the body instead (needs a trusted workspace) |
| `delayMs` | `0` | Delay before answering, up to 60000; also accepted as `delay` |
| `id` | `route-N` | A name for the route |
| `description` | empty | Shown as the tooltip in the **Routes and Mocks** view |
| `disabled` | `false` | Keep the route but do not answer it |

A route needs at least a `body`, a `file` or a `status`.

### Route patterns

| Pattern | Matches |
| --- | --- |
| `/users/:id` | `/users/42`, captured as `params.id` |
| `/files/:name?` | `/files` and `/files/report`, with an optional segment |
| `/assets/*` | one path segment, captured as `params.0` |
| `/docs/**` | the rest of the path, including slashes |

A pattern without a wildcard matches only that exact path: `/api` does not answer `/api/users` unless you write `/api/**`. This keeps a mock from swallowing requests meant for the proxy.

### Placeholders in bodies

| Placeholder | Replaced with |
| --- | --- |
| `{{params.id}}` | A route parameter |
| `{{query.page}}` | A query-string value |
| `{{body.email}}` | A field of the parsed request body |
| `{{headers.origin}}` | A request header |
| `{{uuid}}` | A fresh random identifier |
| `{{now}}` | The current time in ISO 8601 |
| `{{timestamp}}` | The current time in milliseconds since 1970 |
| `{{method}}`, `{{path}}` | The request's method and path |
| `{{counter}}` | A number that goes up by one per response |
| `{{random}}` | A random number from 0 up to 1 |

A string that is exactly one placeholder keeps the value's type, so `"id": "{{counter}}"` gives a number. Placeholders are substitution only; no code runs.

### Turn mocks on and off

- **Auric Live: Toggle Mock API** switches mock answering on or off for the session.
- The control panel's **Overview** has **Answer mock routes**.
- `auricLive.mock.delayMs` adds latency to every mock and REST response, on top of each route's own delay.

## A full REST API from a JSON file

The *REST database* turns a JSON file into a working REST backend: lists, reads, creates, replaces, updates and deletes, with filtering, sorting, pagination and relationships. Forms submit, lists paginate and deleted rows stay deleted.

### Set it up

1. Run **Auric Live: Open Mock Database**, or choose **Open mock database** in the **Routes and Mocks** view's **…** menu.
2. If `db.json` does not exist, Auric Live offers **Create**. It writes a sample with `users`, `posts` and a `profile` object, and turns on mocks and the REST database for the session.
3. Edit the file. Each top-level key holding an array is a *collection*; a key holding an object is a single resource.

```json
{
  "users": [ { "id": 1, "name": "Ada Lovelace" } ],
  "posts": [ { "id": 1, "userId": 1, "title": "First post" } ],
  "profile": { "theme": "dark" }
}
```

To keep it on, put this in `auric.live.json`:

```json
{ "mock": { "enabled": true, "rest": { "enabled": true, "base": "/api", "database": "db.json" } } }
```

| Setting | Default | Meaning |
| --- | --- | --- |
| `auricLive.mock.rest.enabled` | `false` | Serve the REST database (mocks must also be enabled) |
| `auricLive.mock.rest.base` | `/api` | Prefix the collections are mounted under |
| `auricLive.mock.rest.database` | `db.json` | The file, relative to the served root |
| `auricLive.mock.rest.persist` | `false` | Write changes back to the file. Off, a restart returns to the original data |

Changes to unrelated settings keep the in-memory data. The **Routes and Mocks** view lists each collection with its record count.

### Routes

For a collection `users` under `/api`:

| Request | What it does |
| --- | --- |
| `GET /api/users` | List records |
| `GET /api/users/1` | Read one record |
| `POST /api/users` | Create a record |
| `PUT /api/users/1` | Replace a record |
| `PATCH /api/users/1` | Merge fields into a record |
| `DELETE /api/users/1` | Delete a record |

### Query options

| Query | Effect |
| --- | --- |
| `?_page=2&_limit=20` | Pagination, with `X-Total-Count` and `Link` headers |
| `?_start=10&_end=20` | Slice the list |
| `?_sort=name&_order=desc` | Sort; separate several keys with commas |
| `?_q=ada` | Search every field |
| `?status=active` | Exact match on a field |
| `?views_gte=100` | Operators: `_ne`, `_lt`, `_lte`, `_gt`, `_gte`, `_like`, `_in`, `_nin` |
| `?_embed=posts` | Include child records that point at this one |
| `?_expand=user` | Include the parent record this one points at |

Relationships follow the singular-name convention: a post with `userId` belongs to a user.

A path outside the base, or a collection the file does not contain, falls through to the proxy and then to static files.

When this is working, the **Routes and Mocks** view lists your proxy rules, mock routes with hit counts, and REST collections, and the **Requests** view shows `proxy`, `mock` or `rest` as the handler for each answered request.
