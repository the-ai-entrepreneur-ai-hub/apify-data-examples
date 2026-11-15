// YouTube Video Transcript and Subtitles Scraper API. Costs at most about $0.0011 with this input.
//
// npm install apify-client
// APIFY_TOKEN=your_token node run.mjs
import { ApifyClient } from 'apify-client';

if (!process.env.APIFY_TOKEN) throw new Error('Set APIFY_TOKEN first');
const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('george.the.developer/youtube-transcript-scraper').call({
    "urls": [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    ],
    "maxVideos": 1,
    "language": "en",
    "outputFormat": "full-text"
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(JSON.stringify(items, null, 2));
