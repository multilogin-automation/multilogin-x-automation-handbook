# Snippets

Ready-to-run Python scripts for Multilogin X automation. Set environment variables before running:

```bash
export MULTILOGIN_API_URL="http://127.0.0.1:35000"
export MULTILOGIN_API_TOKEN="your_token_here"
```

## Scripts

| File | Description |
| ---- | ----------- |
| [`get_ids_multilogin_api.py`](get_ids_multilogin_api.py) | List profiles, folders, workspaces, and users via the local launcher API |
| [`get_token_playwright.py`](get_token_playwright.py) | Extract session token from `app.multilogin.com` using Playwright |
| [`robust_api_client.py`](robust_api_client.py) | `robust_get` / `robust_post` helpers with retry on HTTP 429 |

## Setup

```bash
pip install -r ../requirements.txt
playwright install chromium   # only needed for get_token_playwright.py
```

## Usage

```bash
python get_ids_multilogin_api.py
python get_token_playwright.py
```

Never commit real tokens. Use `.env` locally (see `.gitignore`).

More scripts and coupons: [@Multilogin_Scripts_Bot](https://t.me/Multilogin_Scripts_Bot)
