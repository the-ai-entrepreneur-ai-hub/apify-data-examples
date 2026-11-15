"""Telegram Channel Scraper and Telegram Keyword Search. Costs at most about $0.025 with this input.

pip install apify-client
APIFY_TOKEN=your_token python run.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("george.the.developer/telegram-channel-scraper").call(
    run_input={
        "channels": [
            "telegram"
        ],
        "maxMessages": 5
    }
)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(json.dumps(item, ensure_ascii=False))
