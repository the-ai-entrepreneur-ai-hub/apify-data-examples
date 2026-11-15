"""LinkedIn Decision Makers Finder. Costs at most about $0.06605 with this input.

pip install apify-client
APIFY_TOKEN=your_token python run.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("george.the.developer/linkedin-decision-makers-finder").call(
    run_input={
        "companies": [
            "https://www.linkedin.com/company/stripe/"
        ],
        "maxDecisionMakersPerCompany": 3
    }
)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(json.dumps(item, ensure_ascii=False))
