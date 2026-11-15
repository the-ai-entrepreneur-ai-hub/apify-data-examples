// LinkedIn Company Finder by Domain, Domain to LinkedIn URL. Costs at most about $0.0245 with this input.
//
// npm install apify-client
// APIFY_TOKEN=your_token node run.mjs
import { ApifyClient } from 'apify-client';

if (!process.env.APIFY_TOKEN) throw new Error('Set APIFY_TOKEN first');
const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('george.the.developer/linkedin-company-by-domain').call({
    "domains": [
        "stripe.com",
        "vercel.com",
        "gitlab.com"
    ]
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(JSON.stringify(items, null, 2));
