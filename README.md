# 1,000 YouTube transcripts cost $1, and five more datasets you can pull with one command

Runnable Python, Node and curl examples for six Apify actors that return LinkedIn company data, Google Scholar papers, YouTube transcripts and Telegram channel posts as JSON. Every example uses a small limit, so a test run costs cents.

You need a free [Apify account](https://apify.com) and its API token in the `APIFY_TOKEN` environment variable. No other key, no login cookies.

## The six actors

| Actor | What goes in | What comes out | Price |
|---|---|---|---|
| [LinkedIn Company Employees Scraper With Decision Makers](https://apify.com/george.the.developer/linkedin-company-employees-scraper) | LinkedIn company URL or company name | Public employee profiles with name, headline, location, profile URL and a decision maker flag | $0.01 per profile plus $0.05 per run |
| [Google Scholar Scraper, Papers, Citations and Authors](https://apify.com/george.the.developer/google-scholar-scraper) | Search query or Google Scholar author ID | Papers with title, authors, year, venue, citation count, link and abstract | $0.008 per paper |
| [LinkedIn Company Finder by Domain, Domain to LinkedIn URL](https://apify.com/george.the.developer/linkedin-company-by-domain) | Website domains | The LinkedIn company page for each domain with confidence, employee count and followers | $0.0075 per resolved company plus $0.002 per run |
| [YouTube Video Transcript and Subtitles Scraper API](https://apify.com/george.the.developer/youtube-transcript-scraper) | YouTube video, playlist or channel URLs | Transcript text with video ID, title, channel name and language | $0.001 per transcript plus $0.0001 per run |
| [Telegram Channel Scraper and Telegram Keyword Search](https://apify.com/george.the.developer/telegram-channel-scraper) | Public Telegram channel names or URLs, optional keywords | Messages with text, date, view count and message URL | $0.005 per message |
| [LinkedIn Decision Makers Finder](https://apify.com/george.the.developer/linkedin-decision-makers-finder) | LinkedIn company URL or company name | Owners, founders, C level, VPs and directors with seniority band, department and profile URL | $0.022 per decision maker plus $0.00005 per run |

Prices were read from the public Apify API on November 15 2026 and can change. The actor page always shows the current price. You pay per result, so a run that finds nothing costs only the run fee where one is listed.

## How it works

```
+-------------+      +------------------+      +----------------+
| your script | ---> |  Apify actor run | ---> | dataset (JSON) |
| or curl     |      |  in the cloud    |      | rows you keep  |
+-------------+      +------------------+      +----------------+
       ^                                               |
       |                                               |
       +-------------- rows come back -----------------+
```

Your code sends one input object. The actor runs on Apify, writes rows to a dataset, and the client reads them back. Nothing runs on your machine except the call.

## Run an example

Python needs version 3.10 or newer.

```bash
pip install -r requirements.txt
export APIFY_TOKEN=your_token
python examples/youtube-transcript-scraper/run.py
```

Node needs version 18 or newer.

```bash
npm install
export APIFY_TOKEN=your_token
node examples/youtube-transcript-scraper/run.mjs
```

Each folder in `examples` holds three files. `run.py` and `run.mjs` use the official `apify-client` and send the same input. `sample-output.json` shows the field names of one row with made up placeholder values, no real people or companies.

## One curl call per actor

Each call starts the actor, waits for it to finish and prints the rows. The sync endpoint waits up to five minutes, which is plenty for these small inputs.

### LinkedIn Company Employees Scraper With Decision Makers

LinkedIn company URL or company name in. Public employee profiles with name, headline, location, profile URL and a decision maker flag out. This input costs at most about $0.1.

```bash
curl -s -X POST "https://api.apify.com/v2/acts/george.the.developer~linkedin-company-employees-scraper/run-sync-get-dataset-items" -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" -d '{"companies": ["https://www.linkedin.com/company/stripe/"], "maxEmployees": 5}'
```

Scripts and a sample row live in [examples/linkedin-company-employees-scraper](examples/linkedin-company-employees-scraper). The actor page is [https://apify.com/george.the.developer/linkedin-company-employees-scraper](https://apify.com/george.the.developer/linkedin-company-employees-scraper).

### Google Scholar Scraper, Papers, Citations and Authors

Search query or Google Scholar author ID in. Papers with title, authors, year, venue, citation count, link and abstract out. This input costs at most about $0.04.

```bash
curl -s -X POST "https://api.apify.com/v2/acts/george.the.developer~google-scholar-scraper/run-sync-get-dataset-items" -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" -d '{"query": "large language models", "maxResults": 5, "sortBy": "relevance"}'
```

Scripts and a sample row live in [examples/google-scholar-scraper](examples/google-scholar-scraper). The actor page is [https://apify.com/george.the.developer/google-scholar-scraper](https://apify.com/george.the.developer/google-scholar-scraper).

### LinkedIn Company Finder by Domain, Domain to LinkedIn URL

Website domains in. The LinkedIn company page for each domain with confidence, employee count and followers out. This input costs at most about $0.0245.

```bash
curl -s -X POST "https://api.apify.com/v2/acts/george.the.developer~linkedin-company-by-domain/run-sync-get-dataset-items" -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" -d '{"domains": ["stripe.com", "vercel.com", "gitlab.com"]}'
```

Scripts and a sample row live in [examples/linkedin-company-by-domain](examples/linkedin-company-by-domain). The actor page is [https://apify.com/george.the.developer/linkedin-company-by-domain](https://apify.com/george.the.developer/linkedin-company-by-domain).

### YouTube Video Transcript and Subtitles Scraper API

YouTube video, playlist or channel URLs in. Transcript text with video ID, title, channel name and language out. This input costs at most about $0.0011.

```bash
curl -s -X POST "https://api.apify.com/v2/acts/george.the.developer~youtube-transcript-scraper/run-sync-get-dataset-items" -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" -d '{"urls": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"], "maxVideos": 1, "language": "en", "outputFormat": "full-text"}'
```

Scripts and a sample row live in [examples/youtube-transcript-scraper](examples/youtube-transcript-scraper). The actor page is [https://apify.com/george.the.developer/youtube-transcript-scraper](https://apify.com/george.the.developer/youtube-transcript-scraper).

### Telegram Channel Scraper and Telegram Keyword Search

Public Telegram channel names or URLs, optional keywords in. Messages with text, date, view count and message URL out. This input costs at most about $0.025.

```bash
curl -s -X POST "https://api.apify.com/v2/acts/george.the.developer~telegram-channel-scraper/run-sync-get-dataset-items" -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" -d '{"channels": ["telegram"], "maxMessages": 5}'
```

Scripts and a sample row live in [examples/telegram-channel-scraper](examples/telegram-channel-scraper). The actor page is [https://apify.com/george.the.developer/telegram-channel-scraper](https://apify.com/george.the.developer/telegram-channel-scraper).

### LinkedIn Decision Makers Finder

LinkedIn company URL or company name in. Owners, founders, C level, VPs and directors with seniority band, department and profile URL out. This input costs at most about $0.06605.

```bash
curl -s -X POST "https://api.apify.com/v2/acts/george.the.developer~linkedin-decision-makers-finder/run-sync-get-dataset-items" -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" -d '{"companies": ["https://www.linkedin.com/company/stripe/"], "maxDecisionMakersPerCompany": 3}'
```

Scripts and a sample row live in [examples/linkedin-decision-makers-finder](examples/linkedin-decision-makers-finder). The actor page is [https://apify.com/george.the.developer/linkedin-decision-makers-finder](https://apify.com/george.the.developer/linkedin-decision-makers-finder).

## Use the actors from Claude, Cursor or any MCP client

The [Apify MCP server](https://docs.apify.com/platform/integrations/mcp) exposes each actor as a tool. Put this in your MCP client config and replace the token. The same block is saved as [mcp.json](mcp.json).

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=george.the.developer/linkedin-company-employees-scraper,george.the.developer/google-scholar-scraper,george.the.developer/linkedin-company-by-domain,george.the.developer/youtube-transcript-scraper,george.the.developer/telegram-channel-scraper,george.the.developer/linkedin-decision-makers-finder",
      "headers": {
        "Authorization": "Bearer YOUR_APIFY_TOKEN"
      }
    }
  }
}
```

## Honest limits

Public data only. No logins, no private groups, no private profiles. LinkedIn results come from publicly indexed pages, so coverage varies by company and some rows can be stale. Google Scholar stops at about 1,000 results per search. Auto captions on YouTube contain mistakes. The sample outputs show the shape of a row and are not real data.

## License

MIT. See [LICENSE](LICENSE).
