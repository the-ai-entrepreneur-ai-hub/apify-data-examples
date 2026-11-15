// Telegram Channel Scraper and Telegram Keyword Search. Costs at most about $0.025 with this input.
//
// npm install apify-client
// APIFY_TOKEN=your_token node run.mjs
import { ApifyClient } from 'apify-client';

if (!process.env.APIFY_TOKEN) throw new Error('Set APIFY_TOKEN first');
const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('george.the.developer/telegram-channel-scraper').call({
    "channels": [
        "telegram"
    ],
    "maxMessages": 5
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(JSON.stringify(items, null, 2));
