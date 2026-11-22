#!/usr/bin/env python3
"""Entry program: writes the chosen plan text to /output/entry.txt.

The plan: sell verified local lead lists to US roofing firms that have
no website, using only public data, free-tier enrichment and Stripe.
"""

import os

ENTRY = "Day 1: scrape Google Maps for 400 US roofers with no website; find owner emails via Apollo free tier. Email each offering 20 verified local leads for $99 via Stripe link; leads from permit filings. Send 200/day, reinvest in Apollo credits. Likely 3-8 sales in 30 days: $300-$800."

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= 280:
        raise ValueError("entry must be 1-280 Unicode code points")


def main() -> None:
    text = ENTRY
    validate(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
