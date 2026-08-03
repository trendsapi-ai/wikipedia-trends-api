# Wikipedia Trends API - page view trends as JSON

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE) [![API v1](https://img.shields.io/badge/API-v1-blue.svg)](https://trendsapi.ai) [![MCP compatible](https://img.shields.io/badge/MCP-compatible-blueviolet.svg)](https://modelcontextprotocol.io) [![Free tier](https://img.shields.io/badge/free%20tier-100%20req%2Fmo-orange.svg)](https://trendsapi.ai/#pricing)

> **Wikipedia trend data as clean JSON: page view time series for any topic, growth rates and the live most-viewed articles feed from one REST endpoint. A clean proxy for public attention.**
>
> One endpoint. One API key. One normalized 0-100 trend score you can compare against 14 other platforms.

**Docs:** [https://trendsapi.ai/#quickstart](https://trendsapi.ai/#quickstart) · **llms.txt:** [https://trendsapi.ai/llms.txt](https://trendsapi.ai/llms.txt) · **Free API key (100 req/mo):** [https://trendsapi.ai/#get-key](https://trendsapi.ai/#get-key)

---

## What a call looks like

```bash
curl -X POST https://api.trendsapi.ai/api \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mode": "get_growth", "source": "wikipedia", "keyword": "artificial intelligence", "percent_growth": ["3M", "12M"]}'
```

```json
{
  "keyword": "artificial intelligence",
  "source": "wikipedia",
  "growth": { "3M": 41.8, "12M": 212.4 },
  "timestamp": "2026-08-03T12:00:00Z"
}
```

## Quickstart (60 seconds)

**1. Get a free API key** at [https://trendsapi.ai/#get-key](https://trendsapi.ai/#get-key) - 100 requests/month, no credit card.

**2. Make your first call:**

```bash
curl -X POST https://api.trendsapi.ai/api \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mode": "get_time_series", "source": "wikipedia", "keyword": "artificial intelligence"}'
```

**Python:**

```python
import requests

res = requests.post(
    "https://api.trendsapi.ai/api",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
    json={"mode": "get_growth", "source": "wikipedia", "keyword": "artificial intelligence",
          "percent_growth": ["3M", "12M"]},
)
print(res.json())
```

**Node.js:**

```js
const res = await fetch("https://api.trendsapi.ai/api", {
  method: "POST",
  headers: {
    Authorization: "Bearer YOUR_API_KEY",
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ mode: "get_growth", source: "wikipedia", keyword: "artificial intelligence",
                          percent_growth: ["3M", "12M"] }),
});
console.log(await res.json());
```

---

## The three modes

| Mode | What it returns | Needs a keyword? |
|---|---|---|
| `get_time_series` | Historical page views as a normalized 0-100 series | yes |
| `get_growth` | Growth % over 3M / 6M / 12M / 5Y windows | yes |
| `get_top_trends` | Live trending feeds (21 of them) | no |

## Why teams switch

|  | Wikimedia Pageviews API | Trends API |
|---|---|---|
| Normalization | raw counts, DIY | 0-100 score, done |
| Growth rates | compute yourself | 3M/6M/12M/5Y built in |
| Trending feed | separate endpoint | included, one call |
| Cross-source compare | no | same scale as 14 other sources |
| Free tier | free (rate limited) | 100 requests/month |

## Use cases

- **Investment research:** rising page views on a company or technology as an attention signal
- **PR measurement:** did the press coverage actually move public attention?
- **Research:** track when a topic enters public consciousness
- **Editorial:** find what the world is looking up right now

---

## Use it from your AI assistant (MCP)

The same API key powers the Trends API MCP server, so Claude, Cursor, VS Code, ChatGPT and any MCP-compatible client can query this data in natural language.

[**+ Add to Cursor (one click)**](cursor://anysphere.cursor-deeplink/mcp/install?name=trendsapi&config=eyJ1cmwiOiAiaHR0cHM6Ly9hcGkudHJlbmRzYXBpLmFpL21jcCIsICJoZWFkZXJzIjogeyJBdXRob3JpemF0aW9uIjogIkJlYXJlciBZT1VSX0FQSV9LRVkifX0=)

**Cursor / Windsurf / Cline** (`~/.cursor/mcp.json` or equivalent):

```json
{
  "mcpServers": {
    "trendsapi": {
      "url": "https://api.trendsapi.ai/mcp",
      "transport": "http",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    }
  }
}
```

**VS Code / GitHub Copilot** (`.vscode/mcp.json`):

```json
{
  "servers": {
    "trendsapi": {
      "type": "http",
      "url": "https://api.trendsapi.ai/mcp",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    }
  }
}
```

**Claude Desktop** (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "trendsapi": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://api.trendsapi.ai/mcp", "--header", "Authorization:${AUTH_HEADER}"],
      "env": { "AUTH_HEADER": "Bearer YOUR_API_KEY" }
    }
  }
}
```

**Claude.ai (browser):** Settings -> Connectors -> Add custom connector -> `https://api.trendsapi.ai/mcp`

Then ask things like:

```
How did "creatine gummies" grow on TikTok vs Google over the last 12 months?
What is trending on YouTube right now?
```

---

## Every source on the same key

| Source | `source` value | What it measures |
|---|---|---|
| Google Search | `google search` | Search volume |
| Google Images | `google images` | Image search volume |
| Google News | `google news` | News search volume |
| Google Shopping | `google shopping` | Shopping search volume |
| YouTube | `youtube` | Search volume |
| TikTok | `tiktok` | Hashtag volume |
| Reddit | `reddit` | Subreddit subscribers |
| Amazon | `amazon` | Product search volume |
| Wikipedia | `wikipedia` | Page views |
| News volume | `news volume` | Article mention volume |
| News sentiment | `news sentiment` | Positive / negative score |
| App downloads | `app downloads` | Android downloads (AppBrain) |
| App rankings | `app rankings` | Android chart position |
| npm | `npm` | Weekly package downloads |
| Steam | `steam` | Concurrent players (monthly) |

### Live feeds (`get_top_trends`, no keyword needed)

| Feed | `type` value |
|---|---|
| Google Trends | `Google Trends` |
| Google News Top News | `Google News Top News` |
| TikTok Trending Hashtags | `TikTok Trending Hashtags` |
| TikTok Trending Searches | `TikTok Trending Searches` |
| TikTok Shop Hot Products | `TikTok Shop Hot Products` |
| YouTube Trending | `YouTube Trending` |
| X (Twitter) Trending | `X (Twitter) Trending` |
| Reddit Hot Posts | `Reddit Hot Posts` |
| Reddit World News | `Reddit World News` |
| Wikipedia Trending | `Wikipedia Trending` |
| Amazon Best Sellers Top Rated | `Amazon Best Sellers Top Rated` |
| Amazon Best Sellers by Category | `Amazon Best Sellers by Category` |
| App Store Top Free | `App Store Top Free` |
| App Store Top Paid | `App Store Top Paid` |
| Google Play | `Google Play` |
| Top Websites | `Top Websites` |
| Spotify Top Podcasts | `Spotify Top Podcasts` |
| Steam Most Played | `Steam Most Played` |
| GitHub Trending Repos | `GitHub Trending Repos` |
| IMDb MOVIEmeter | `IMDb MOVIEmeter` |
| Open Library Trending Books | `Open Library Trending Books` |

---

## FAQ

### What Wikipedia data does Trends API provide?

Page view volume for any article or topic as a normalized time series, growth percentages over 3M/6M/12M/5Y windows, and the live Wikipedia Trending feed of most-viewed articles today.

### Why use this instead of the Wikimedia Pageviews API?

The Wikimedia API returns raw counts you must normalize and window yourself. Trends API returns a rescaled 0-100 series with growth already computed, in the same shape as 14 other sources - so cross-platform attention comparisons take one line of code.

### Is Wikipedia attention a good proxy for real-world interest?

It is one of the cleaner ones: page views are driven by active curiosity rather than algorithmic feeds, so spikes usually reflect genuine public attention events.

### How fresh is the trending feed?

Updated through the day. Every response includes its own timestamp.

### Can I compare a topic's Wikipedia attention with Google search interest?

Yes - query both sources with the same keyword and compare normalized scores directly.

---

## Links

- **Docs & quickstart:** [https://trendsapi.ai/#quickstart](https://trendsapi.ai/#quickstart)
- **llms.txt (machine-readable API reference):** [https://trendsapi.ai/llms.txt](https://trendsapi.ai/llms.txt)
- **Pricing (free tier: 100 requests/month):** [https://trendsapi.ai/#pricing](https://trendsapi.ai/#pricing)
- **Get an API key:** [https://trendsapi.ai/#get-key](https://trendsapi.ai/#get-key)

## License

MIT - see [LICENSE](LICENSE). Data is served by [Trends API](https://trendsapi.ai); usage of the API itself is subject to the plan limits on your key.
