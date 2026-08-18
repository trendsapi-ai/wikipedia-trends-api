# Wikipedia page-view trends API

Wikipedia article attention via the Trends API. History, growth, and live trending pages as 0-100 scores.

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/trendsapi-wikipedia.svg)](https://pypi.org/project/trendsapi-wikipedia/)

Key: [trendsapi.ai/#get-key](https://trendsapi.ai/#get-key). Full contract: [trendsapi-ai/trendsapi](https://github.com/trendsapi-ai/trendsapi).

## Install

```bash
pip install trendsapi-wikipedia
```

```python
from trendsapi_wikipedia import TrendsAPI

client = TrendsAPI()  # TRENDSAPI_KEY
series = client.get_time_series("large language model")
growth = client.get_growth("large language model", percent_growth=["12M"])
hot = client.get_live(limit=10)
```

Keyword helpers default to `source: "wikipedia"`. Override `source=` for any other platform. Official full client: [`trendsapi`](https://pypi.org/project/trendsapi/).

## Call

| Field | Value |
|---|---|
| Endpoint | `POST https://api.trendsapi.ai/api` |
| Auth | `Authorization: Bearer $TRENDSAPI_KEY` |
| History | `source: wikipedia` with `get_time_series` or `get_growth` |
| Keyword | Article title or topic, e.g. large language model |
| Live `type` | Wikipedia Trending |

```bash
curl -sS -X POST https://api.trendsapi.ai/api \
  -H "Authorization: Bearer $TRENDSAPI_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mode":"get_time_series","source":"wikipedia","keyword":"large language model"}'
```

Titles are picky. `Java` vs `Java (programming language)` are different series.

Do not pass `source: wikipedia` on `get_top_trends`. Use `type: Wikipedia Trending`.

Site: [https://trendsapi.ai/trends/wikipedia-trends](https://trendsapi.ai/trends/wikipedia-trends). GitHub: [trendsapi-ai/wikipedia-trends-api](https://github.com/trendsapi-ai/wikipedia-trends-api).

## License

MIT. See [LICENSE](LICENSE).
