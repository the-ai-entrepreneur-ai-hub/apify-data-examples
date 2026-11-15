"""YouTube Video Transcript and Subtitles Scraper API. Costs at most about $0.0011 with this input.

pip install apify-client
APIFY_TOKEN=your_token python run.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("george.the.developer/youtube-transcript-scraper").call(
    run_input={
        "urls": [
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        ],
        "maxVideos": 1,
        "language": "en",
        "outputFormat": "full-text"
    }
)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(json.dumps(item, ensure_ascii=False))
