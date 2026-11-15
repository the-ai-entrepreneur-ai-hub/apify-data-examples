"""Google Scholar Scraper, Papers, Citations and Authors. Costs at most about $0.04 with this input.

pip install apify-client
APIFY_TOKEN=your_token python run.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("george.the.developer/google-scholar-scraper").call(
    run_input={
        "query": "large language models",
        "maxResults": 5,
        "sortBy": "relevance"
    }
)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(json.dumps(item, ensure_ascii=False))
