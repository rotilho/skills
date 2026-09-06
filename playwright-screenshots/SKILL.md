---
name: "playwright-screenshots"
version: "1.0.1"
description: "Use when a task needs browser screenshots, visual verification, page smoke tests, or headless browser capture after browsermcp is unavailable or unnecessary. Prefer Playwright for localhost, static files, generated pages, and unauthenticated pages; note when a live user browser session is required instead."
license: "MIT"
compatibility: "codex"
metadata:
  audience: "agent"
  workflow: "browser-verification"
---

# Playwright Screenshots

## When to use

Use this skill when the user asks to:
- take or verify a screenshot of a webpage or local app
- check a UI visually without relying on browsermcp
- run a headless browser smoke test
- confirm that Playwright can open a page, render it, and save an image

Do not use this skill when the task requires the user's already-open browser state, Chrome extensions, active tabs, or existing logged-in cookies. In that case, say that a browser bridge or exported auth state is required.

## Workflow

1. Reuse the project's installed Playwright or browser tooling when available. Otherwise, check Node and npm before using `npx`:

```bash
node --version
npm --version
```

2. Capture the requested page. For project pages, use the running dev server's URL and adapt the viewport or full-page option to the task:

```bash
npx --yes playwright screenshot --viewport-size=390,844 --full-page http://127.0.0.1:8080 /tmp/page.png
```

Wait for the page's required content or state when needed. A fixed delay alone does not prove it is ready.

3. If capture fails because Chromium is missing, install the browser with the same Playwright version and retry:

```bash
npx --yes playwright install chromium
```

4. If the failure's source is unclear, capture a tiny static page to separate browser setup from application problems:

```bash
npx --yes playwright screenshot "data:text/html,%3Ch1%3EPlaywright%20screenshot%20works%3C%2Fh1%3E" /tmp/playwright-smoke.png
```

5. Check the output and inspect it with the available local image viewer when visual correctness matters:

```bash
file /tmp/page.png
```

## Constraints

- `npx` may need network access to fetch Playwright.
- `npx playwright install chromium` downloads browser binaries into the Playwright cache.
- Playwright controls a separate browser context; it does not automatically share the user's Chrome session.
- For authenticated apps, use app test credentials, a persistent browser profile, or exported Playwright storage state.
- Keep screenshots in `/tmp` unless the user asks for repo artifacts.

## Verification checklist

Before saying Playwright works, confirm:
- a screenshot command exits 0
- the output file is a valid non-empty PNG
- the image was inspected when visual correctness matters
