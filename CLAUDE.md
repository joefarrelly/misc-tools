# misc-tools

Flask web app serving a collection of utility tools at `tools.fazz.uk`.

## Stack

- **Python 3.13** + Flask + Gunicorn
- **Docker** — no venvs, ever. All Python work runs in Docker.
- **Bootstrap 5** + Bootstrap Icons via CDN — no build step, no bundler
- **Default: all tool logic is client-side JavaScript** — Flask only serves templates
- **Exception: tools requiring native binaries** use a server-side POST endpoint (e.g. `/image-ocr/extract` uses pytesseract). Keep these minimal — one endpoint per tool, JSON in/out, no sessions or state.

## Running locally

```bash
docker compose up --build
```

App is at `http://localhost:5002`.

## Project structure

```
app.py                        # Flask routes (GET per tool; POST /image-ocr/extract for OCR)
templates/
  base.html                   # Shared layout: navbar, Bootstrap CDN links, shared CSS
  index.html                  # Home page — tool cards organised by category
  image_ocr.html              # Image to text (OCR via pytesseract server-side)
  dedupe.html                 # De-dupe list
  list_compare.html           # Compare two lists
  epoch.html                  # Epoch ↔ date converter
  json_formatter.html         # JSON pretty-print / minify
  base64.html                 # Base64 encode/decode
  url_encode.html             # URL encode/decode
  jwt_decoder.html            # JWT decoder (no verification)
  case_converter.html         # Text case converter (12 formats)
  regex_tester.html           # Regex tester with live highlighting
  uuid_generator.html         # UUID v4 generator
  base_converter.html         # Number base converter (dec/bin/oct/hex)
  cron_explainer.html         # Cron expression explainer
  csv_json.html               # CSV ↔ JSON converter
Dockerfile
docker-compose.yml            # Local dev only — port 5002, flask --debug
requirements.txt
.github/workflows/deploy.yml
```

## Adding a new tool

1. Add a route in `app.py`
2. Create `templates/<name>.html` extending `base.html`
3. Add a card to `index.html` under the appropriate category section
4. Add a nav item to the relevant dropdown in `base.html`

Processing should happen in JavaScript inside the template where possible. Use a server-side POST endpoint only when a native binary is required (e.g. tesseract for OCR). Keep endpoints stateless: accept multipart or JSON, return JSON.

## Branch structure

- `dev` — active development; all feature branches target here
- `main` — production; triggers deploy on push

Only `dev` can merge into `main` (enforced by `restrict-main-merges.yml`).

## Deployment

Handled by `.github/workflows/deploy.yml` on push to `main`. Connects via SSH, pulls, rebuilds, and restarts the container.

The production service block lives in `~/apps/docker-compose.yml` on the server (not in this repo). It uses gunicorn and the external `web` Docker network so Caddy can proxy it.

Required GitHub secrets: `SERVER_HOST`, `SERVER_USER`, `SERVER_SSH_KEY`, `GH_PAT`.
