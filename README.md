# Multilogin X — ID & Token Retrieval Tools

Step-by-step guides, automation snippets, and best practices for retrieving **profile IDs, folder IDs, workspace IDs, and API tokens** in Multilogin X. Built for developers, automation engineers, and teams running antidetect browser workflows at scale.

## Table of Contents

1. [Promo Codes & Scripts Hub](#-promo-codes--scripts-hub)
2. [Introduction](#introduction)
3. [Tutorials](#tutorials)
4. [Snippets](#snippets)
5. [Quick Troubleshooting](#-quick-troubleshooting-checklist)
6. [Comparison: Ways to Get Token/ID](#-comparison-ways-to-get-tokenid)
7. [Quick API Examples](#-quick-api-examples)
8. [Best Practices](#-advanced-multilogin-automation-tips--best-practices)
9. [FAQ](#-real-world-use-cases--faq)
10. [How to Contribute](#how-to-contribute)
11. [SEO Topics](#seo-topics)

---

## 🎁 Promo Codes & Scripts Hub

| Product | Code | Discount |
| ------- | ---- | -------- |
| Multilogin Antidetect Browser | `SAAS50` | 50% OFF |
| Multilogin Minutes | `MIN50` | 50% OFF |

Apply the code at checkout on [multilogin.com](https://multilogin.com). Codes may change — check the bot below for the latest offers.

Full details: [docs/promo-codes.md](docs/promo-codes.md)

📦 **Script library & fresh coupons:** [@Multilogin_Scripts_Bot](https://t.me/Multilogin_Scripts_Bot)

[![Telegram Scripts Bot](https://img.shields.io/badge/Telegram-Scripts%20%26%20Coupons-26A5E4?style=flat-square&logo=telegram)](https://t.me/Multilogin_Scripts_Bot)

---

## Introduction

This repository provides concise, step-by-step guides and automation snippets for Multilogin, focused on developer productivity and troubleshooting. Tutorials include screenshots and copy-paste code for quick reference.

## Tutorials

- [How to Get Profile, Folder, and Workspace IDs in DevTools](tutorials/how-to-get-profile-folder-workspace-ids-in-devtools.md)
- [How to Find a User ID in DevTools](tutorials/how-to-find-user-id-in-devtools.md)
- [How to Get API Tokens in DevTools](tutorials/how-to-get-api-tokens-in-devtools.md)
- [Multilogin X API Overview](tutorials/multilogin-x-api-overview.md)

## Snippets

Install dependencies: `pip install -r requirements.txt`

| Script | Description |
| ------ | ----------- |
| [`snippets/get_ids_multilogin_api.py`](snippets/get_ids_multilogin_api.py) | List profiles, folders, workspaces, and users via the local launcher API |
| [`snippets/get_token_playwright.py`](snippets/get_token_playwright.py) | Extract session token from the web app with Playwright |
| [`snippets/robust_api_client.py`](snippets/robust_api_client.py) | HTTP helpers with exponential backoff on rate limits |

See [`snippets/README.md`](snippets/README.md) for setup and usage.

---

## 🛠️ Quick Troubleshooting Checklist

Before asking for help, try these steps:

- [ ] Are you logged in with the correct account?
- [ ] Did you open the correct Network/Storage tab in DevTools?
- [ ] Did you reload the page after opening DevTools?
- [ ] Can't find token/ID? Try logging out and back in, or clear your browser cache.
- [ ] Did you check your API/token permissions?
- [ ] Did you try the sample scripts below?

If you still have issues, please open an issue with screenshots and the commands you tried.

---

## 📊 Comparison: Ways to Get Token/ID

| Method   | Pros                       | Cons                        | When to use?               |
| -------- | -------------------------- | --------------------------- | -------------------------- |
| DevTools | Fast, no extra install     | Manual, easy to miss a tab  | Quick one-time retrieval   |
| API      | Automatable, script-ready  | Needs token, rate limits    | Frequent/automated use     |
| CLI/Tool | Workflow/batch integration | Needs install, version bugs | Advanced/large-scale tasks |
| UI       | Easy, no tech skills needed| Not automatable             | Beginners, quick checks    |

---

## 🧩 Quick API Examples

Replace `<your_api_token>` and `<profile_id>` before running:

```python
import requests

API_TOKEN = "<your_api_token>"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# List users
print(requests.get("http://localhost:35000/api/v2/users", headers=headers).json())

# Get profile details
profile_id = "<profile_id>"
print(requests.get(f"http://localhost:35000/api/v2/profiles/{profile_id}", headers=headers).json())
```

For full scripts (ID retrieval, Playwright token extraction, retry logic), see [`snippets/`](snippets/).

---

## 🏆 Advanced Multilogin Automation Tips & Best Practices

### Expert Advice & Real-World Lessons

- **Always check API version compatibility.** Multilogin X changes endpoints and authentication flows frequently — read the changelog before updating scripts.
- **Use a dedicated automation account** with limited permissions for scripts. Never use your main admin account for automation.
- **Rotate tokens regularly** and never hardcode them in public repositories.
- **Batch profile creation:** Use async requests and handle rate limits with exponential backoff.
- **Profile backup/restore:** Script regular exports of profile configs and cookies for disaster recovery.
- **Monitoring:** Set up scripts to check profile health/status and alert on failures (Slack, email, etc.).
- **Store tokens in environment variables or secret managers, not in code.**
- **Log only non-sensitive data; mask tokens and IDs in logs.**
- **Review Multilogin's API changelog monthly.** Breaking changes are not always widely announced.
- **Use browser DevTools to inspect all network traffic, not just documented endpoints.** Sometimes undocumented APIs are exposed.
- **If API returns 429 (rate limit), implement retry logic with increasing delays.**
- **For strange errors, clear all cookies and local/session storage, then re-authenticate.**
- **For large teams, use workspace/folder IDs to segment automation and avoid conflicts.**
- **Use Docker or virtual environments to ensure consistent script execution across machines.**
- **Always test scripts in a staging environment before running on production data.**
- **Join Multilogin user forums and Discords.** Many API quirks are solved by the community before official docs are updated.
- **Share your scripts and improvements.** Open source benefits everyone.

For rate-limit handling, use [`snippets/robust_api_client.py`](snippets/robust_api_client.py).

### Checklist Before Running Automation

- [ ] API token is valid and not expired
- [ ] Script is running in a safe environment (not production by accident)
- [ ] All endpoints and parameters are up to date with latest docs
- [ ] Logging and error handling are enabled

---

## 📚 Real-World Use Cases & FAQ

- **Can't find token/ID?** → Usually caused by not reloading the page or an expired session.
- **API returns 401/403 error?** → Token is wrong or expired; get a new token.
- **Script runs but no result?** → Check endpoint, permissions, or try with another profile.

Found a new issue or useful tip? Please submit a PR or open an issue to help the community!

---

## How to Contribute

1. Add saved official Multilogin HTML under the project root.
2. Convert content into `/tutorials` with Overview, Step-by-step, and Technical Tips.
3. Create matching `/snippets` Python/Playwright API automation loaders.
4. Add SEO topics to this README.

## SEO Topics

- Multilogin X API automation
- How to get Multilogin profile ID
- Multilogin folder ID API
- Multilogin workspace ID retrieval
- Multilogin DevTools instructions
- Python Multilogin API script
- Playwright Multilogin automation
- Multilogin CLI vs API
- Multilogin token management
- Multilogin web interface automation
- Multilogin folder synchronization
- Multilogin team workspace setup
- Multilogin profile cloning
- Multilogin session handling
- Multilogin error troubleshooting
- Multilogin upgrade guide
- Multilogin Docker automation
- Multilogin browser profile lifecycle
- Multilogin best practices
- Multilogin endpoint security
- Multilogin promo code
- Multilogin antidetect browser discount

---
<p align="center">
  <img src="https://img.shields.io/badge/System_Status-Online-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/Last_Pulse-2026--03--29-blue?style=flat-square" />
</p>
