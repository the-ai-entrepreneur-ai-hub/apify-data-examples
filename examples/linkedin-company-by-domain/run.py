"""LinkedIn Company Finder by Domain, Domain to LinkedIn URL. Costs at most about $0.0245 with this input.

pip install apify-client
APIFY_TOKEN=your_token python run.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("george.the.developer/linkedin-company-by-domain").call(
    run_input={
        "domains": [
            "stripe.com",
            "vercel.com",
            "gitlab.com"
        ]
    }
)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(json.dumps(item, ensure_ascii=False))
