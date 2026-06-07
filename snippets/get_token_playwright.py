"""Extract Multilogin session token from browser sessionStorage via Playwright."""

from playwright.sync_api import sync_playwright

MULTILOGIN_APP_URL = "https://app.multilogin.com"


def get_session_token(headless=False):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page()
        page.goto(MULTILOGIN_APP_URL)
        print("Log in manually if needed, then press Enter to continue...")
        input()
        token = page.evaluate("window.sessionStorage.getItem('token')")
        browser.close()
        return token


if __name__ == "__main__":
    token = get_session_token()
    if token:
        print("Token retrieved (first 8 chars):", token[:8] + "...")
    else:
        print("No token found in sessionStorage. Try logging in again.")
