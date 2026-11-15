"""LinkedIn Company Employees Scraper With Decision Makers. Costs at most about $0.1 with this input.

pip install apify-client
APIFY_TOKEN=your_token python run.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("george.the.developer/linkedin-company-employees-scraper").call(
    run_input={
        "companies": [
            "https://www.linkedin.com/company/stripe/"
        ],
        "maxEmployees": 5
    }
)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(json.dumps(item, ensure_ascii=False))
