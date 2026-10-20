---
title: Auric Artisan Live — run a backend or framework dev server
description: Let Auric Live run your project's backend or framework dev server (PHP, Python, Ruby, Go, Java, Node.js and more), or connect to one already running, and serve it through one address.
product: VS Code extensions › Auric Artisan Live
updated: 2026-09-25
---

# Run a backend or framework dev server

A *run target* is what actually serves your site. By default it is **Static files**: Auric Live serves the folder itself. For a project with a backend or a framework dev server, you can choose a different run target. Auric Live then starts that process, waits for it to be ready, and forwards requests to it, so you still use one address with the dashboard, request inspector, network simulation and phone QR code.

Auric Live does not install runtimes or packages. PHP, Python, Ruby, Go, Java, Node.js and the rest must already be installed and on your `PATH`, and the project's dependencies must already be installed.

Running a command needs a trusted workspace. In Restricted Mode only static files are served.

## Choose a run target

1. Run **Auric Live: Select Run Target…** (`Ctrl` + `Alt` + `J`), select the **Run target** row in the **Servers** view, or use the control panel's **03 / Runtime** section.
2. The list, titled **Run target — *folder name***, shows in this order:
   - your saved commands (from `auricLive.runProfiles`);
   - the detected framework dev server, if any;
   - detected language runtimes;
   - **Static files**, which is always available.

   Each entry shows its command and why it was detected, for example `manage.py is present`. The current target has a tick.
3. The list also offers **Add a custom command…**, **Edit saved commands…** and **Find a running backend…**.
4. Pick a target. If the server was not running, it starts.

What happens next depends on the kind of target:

| Kind | What Auric Live does |
| --- | --- |
| **Static files** | Serves the folder itself, with Auric live reload |
| **A server command** | Starts the command, forwards `/` to its port and waits while it starts |
| **PHP through CGI** | Runs `.php` files per request with `php-cgi`. See [Run PHP sites](php-and-cgi.md) |
| **An existing server (URL only)** | Forwards to a server you already run, without starting or stopping it |

With a server command, Auric live reload is switched off for that session so it does not compete with the framework's hot reload, and the developer dashboard is still added to pages.

**Auric Live: Show Detected Run Targets** writes every target it can offer for the folder, with the reason for each, to the output channel.

## What is detected

Detection is based on evidence in the folder: a file that exists, a dependency that is declared, an entry point that is present. It suggests a target; it does not guarantee every framework configuration works.

### JavaScript framework dev servers

Detected from `package.json` dependencies. The command uses your package manager, chosen from the lockfile: `pnpm run`, `yarn`, `bun run` or `npm run`. Auric Live prefers the script the project declares (`dev`, `start` or `serve`).

| Framework | Usual script | Usual port |
| --- | --- | --- |
| Next.js | `dev` | 3000 |
| Nuxt | `dev` | 3000 |
| SvelteKit | `dev` | 5173 |
| Astro | `dev` | 4321 |
| Remix | `dev` | 3000 |
| Angular | `start` | 4200 |
| Gatsby | `develop` | 8000 |
| Create React App | `start` | 3000 |
| Vue CLI | `serve` | 8080 |
| Eleventy | `start` | 8080 |
| Vite | `dev` | 5173 |
| Express | `start` | 3000 |
| Any project with a `dev`, `start` or `serve` script | that script | 3000 |

### Language runtimes

| Language | Target | Detected when | Command | Port |
| --- | --- | --- | --- | --- |
| PHP | Laravel | `artisan` is present | `php artisan serve --port=<port>` | 8000 |
| PHP | Symfony | `symfony.lock` is present | `symfony server:start --port=<port> --no-tls` | 8000 |
| PHP | PHP built-in server | `composer.json`, `index.php` or any `.php` file | `php -S 127.0.0.1:<port> -t <docroot>` (docroot `public` when `public/index.php` exists) | 8000 |
| PHP | PHP through CGI | the folder contains `.php` files | runs per request | — |
| Python | Django | `manage.py` is present | `python manage.py runserver <port>` | 8000 |
| Python | FastAPI | `fastapi` in `requirements.txt` or `pyproject.toml`, or `main.py` creates a FastAPI app | `uvicorn main:app --reload --port <port>` | 8000 |
| Python | Flask | `flask` declared, or `app.py` or `wsgi.py` creates a Flask app | `flask run --port <port>` | 5000 |
| Python | Python http.server | the folder contains `.py` files | `python -m http.server <port>` | 8000 |
| Ruby | Ruby on Rails | `bin/rails` is present | `ruby bin/rails server -p <port>` | 3000 |
| Ruby | Jekyll | `_config.yml` is present | `bundle exec jekyll serve --port <port>` | 4000 |
| Ruby | Sinatra | `sinatra` in the `Gemfile` | `ruby app.rb -p <port>` | 4567 |
| TypeScript | Deno | `deno.json` or `deno.jsonc` | `deno task start` | 8000 |
| TypeScript | Bun | a Bun lockfile | `bun run dev` | 3000 |
| JavaScript | Node entry point | `package.json` `main`, or `server.js`, `app.js`, `index.js`, `main.js`, `src/server.js`, `src/index.js` | `node <entry>` | 3000 |
| C# | ASP.NET Core | a `.csproj` or `.sln` file | `dotnet watch run --urls http://localhost:<port>` | 5000 |
| Java | Spring Boot (Maven) | `pom.xml` declares Spring Boot | `mvnw spring-boot:run` (or `mvn`) | 8080 |
| Java | Spring Boot (Gradle) | the Gradle build declares Spring Boot | `gradlew bootRun` (or `gradle`) | 8080 |
| Go | Go | `go.mod` is present | `go run .` | 8080 |
| Rust | Rust | `Cargo.toml` is present | `cargo run` | 8080 |
| Elixir | Phoenix | `mix.exs` declares Phoenix | `mix phx.server` | 4000 |
| Go | Hugo | `hugo.toml`, `hugo.yaml` or `config.toml` | `hugo server --port <port>` | 1313 |

Only one generic fallback is offered per language: a Django project is not also offered `python -m http.server`. For Maven and Gradle, the project's wrapper script (`mvnw`, `gradlew`) is used when it exists.

## The first-run suggestion

The first time you go live in a folder that is clearly not a plain static site, Auric Live says so once:

- For a framework: **This looks like a *Vite* project, which has its own dev server on port *5173*.** Choose **Start it and proxy**, **Write config** (saves a suggested setup to `auric.live.json`) or **Not now**.
- For PHP: **This looks like a PHP project.** Choose **Enable PHP** or **Not now**.

Serving a Vite or Next.js project as plain files shows an unbuilt page full of module errors; this prompt prevents that. Turn it off with `auricLive.suggestFrameworkSetup`. To skip the question and always start the detected dev server, set `auricLive.devServer.autoStart` to `true`.

## Framework dev server commands

| Command | What it does |
| --- | --- |
| **Auric Live: Start Framework Dev Server…** | Detect the framework, confirm the command (**Run: *command***), start it and forward to it |
| **Auric Live: Stop Framework Dev Server** | Stop it, and remove the forwarding it added |
| **Auric Live: Restart Framework Dev Server** | Restart it |
| **Auric Live: Show Dev Server Output** | Show its output (the **Auric Live: Run Target** output channel) |

When it starts: **Auric Live started *Next.js* and is forwarding to it. Requests wait while it compiles, and pages reload when it restarts.**

### Supervision

By default the dev server runs as a supervised process, which gives you three things:

- **Port adoption.** If the framework moves to another port because yours was taken, Auric Live reads the port it prints and forwards there (`auricLive.upstream.autoDetectPort`).
- **Restart on crash.** If it exits unexpectedly, it restarts with a growing delay (`auricLive.devServer.autoRestart`), up to `auricLive.devServer.maxRestarts` times (default 5). A clean exit is not restarted. After repeated failures you see **keeps failing** with **Show output** and **Try again**.
- **Reload on recovery.** Pages reload when the backend comes back (`auricLive.upstream.reloadOnRecover`).

If your command needs typed input, set `auricLive.devServer.useTerminal` to run it in a VS Code terminal instead. You lose port adoption, restart supervision and reload on recovery.

To override the detected command, set `auricLive.devServer.command`, for example `npm run dev -- --host`.

## Add your own command

1. Run **Auric Live: Add Custom Run Command…**, or choose **Add a custom command…** in the run-target list.
2. **Run command (1 of 3):** paste the command that starts your site, exactly as you would type it. Environment variables written in front of it are read and applied to the process, in any of these shell styles:

   ```text
   $env:API_MODE=mock; node server.js
   API_MODE=mock node server.js
   set API_MODE=mock && node server.js
   ```

   So a command copied from a PowerShell prompt also works when VS Code uses bash, and the other way round. A line that contains only assignments adds those variables to the currently selected run target.
3. **Run command (2 of 3):** give it a name.
4. **Run command (3 of 3):** enter the port it listens on, or leave it empty to read the port from the command's output when it starts.
5. Choose **Run it now** or **Not yet**.

The command is saved to `auricLive.runProfiles` in your workspace settings (per folder in a multi-root workspace), so it survives a restart. **Auric Live: Edit Saved Run Commands** opens that setting.

### Run profile fields

You can also write profiles by hand, in settings or in `auric.live.json`. A profile can be just a command string, or an object:

| Field | Meaning |
| --- | --- |
| `label` | Name shown in the list |
| `id` | Stable identifier; derived from the label if omitted |
| `description` | Extra text shown in the list |
| `command` | The command line; leading environment assignments are read |
| `env` | Environment variables as name–value pairs |
| `cwd` | Working directory, relative to the served root |
| `port` | Port the process listens on; `0` or omitted reads it from the output |
| `url` | An existing server to forward to (`http://` or `https://`, no embedded credentials). Without `command`, nothing is started |
| `kind` | `server`, `static` or `cgi` |
| `mount` | Path the target is forwarded under; default `/` |
| `healthPath` | An absolute path that must answer 200–399 before the target counts as ready |
| `autoStart` | `true` to apply this profile automatically on **Go Live** |
| `adoptPort` | `false` to stop Auric Live following the port the process prints |
| `shell` | A specific shell executable to run the command with |

### Connect to a backend you already run

A *URL-only* profile forwards to a server you started elsewhere. Auric Live never starts or stops it.

```json
{
  "runProfiles": [
    {
      "id": "existing-api",
      "label": "Existing API",
      "url": "http://localhost:8000",
      "mount": "/api",
      "healthPath": "/health",
      "autoStart": true
    }
  ]
}
```

## Find a running backend

**Auric Live: Find a Running Backend** scans the ports these tools usually use (or `auricLive.upstream.candidatePorts` if you set it), skipping Auric Live's own port.

- If something answers: **Something is listening on port *N*. Forward / to it?** Choose **Forward it**.
- If nothing answers: **Auric Live checked *N* common ports and nothing was listening.** Choose **Start the dev server** or **Show ports**.

The **Upstream not answering** row in the **Servers** view runs the same scan.

## Waiting for a backend

When a proxied backend refuses the connection, it is usually still compiling. With `auricLive.upstream.wait` on (the default), a request waits up to `auricLive.upstream.waitTimeoutMs` (default 25 seconds) instead of failing with 502. After that, the page shows a waiting screen that reloads itself until the backend answers. Auric Live checks a silent backend every `auricLive.upstream.pollIntervalMs` (default 400 ms), then less often once it is up.

Readiness is a TCP connection by default. Give a profile or proxy rule a `healthPath` to require an HTTP answer from 200 to 399 instead. Readiness checks do not follow redirects.

## Check prerequisites

**Auric Live: Diagnose Project and Runtime** opens a local report of the configuration, the run targets and whether each command's executable (and any configured shell) is found on your `PATH` or in the project. Credential fields are redacted. It inspects; it never runs or installs anything. The control panel's **03 / Runtime** section has **Run diagnostics** and shows the same readiness information.

When a run target is working, the **Servers** view shows **Dev server: *name*** as running with its port, **Upstream ready**, and the status bar shows the port without a warning background.
