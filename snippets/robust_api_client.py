"""HTTP helper with exponential backoff for Multilogin API rate limits."""

import time

import requests


def robust_get(url, headers, max_retries=5, timeout=10):
    for attempt in range(max_retries):
        resp = requests.get(url, headers=headers, timeout=timeout)
        if resp.ok:
            return resp.json()
        if resp.status_code == 429:
            wait = 2 ** attempt
            print(f"Rate limited, retrying in {wait}s...")
            time.sleep(wait)
            continue
        print(f"Error: {resp.status_code} - {resp.text}")
        break
    return None


def robust_post(url, headers, json_body=None, max_retries=5, timeout=10):
    for attempt in range(max_retries):
        resp = requests.post(url, headers=headers, json=json_body, timeout=timeout)
        if resp.ok:
            return resp.json()
        if resp.status_code == 429:
            wait = 2 ** attempt
            print(f"Rate limited, retrying in {wait}s...")
            time.sleep(wait)
            continue
        print(f"Error: {resp.status_code} - {resp.text}")
        break
    return None
