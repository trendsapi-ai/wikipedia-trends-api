# Wikipedia page-view trends API

Same class of signal as Wikimedia AQS, inside the Trends API envelope so it joins Google / Amazon on `date` and `value`. Use AQS if you need `en.wikipedia` vs `de.wikipedia`, spider filters, or raw integers with no 0-100 scale.

Key: [trendsapi.ai/#get-key](https://trendsapi.ai/#get-key). Contract: [trendsapi-ai/trendsapi](https://github.com/trendsapi-ai/trendsapi).

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Source](https://img.shields.io/badge/source-wikipedia-lightgrey.svg)](https://trendsapi.ai/trends/wikipedia-trends)

## Call

| Field | Value |
|---|---|
| Endpoint | `POST https://api.trendsapi.ai/api` |
| Auth | `Authorization: Bearer $TRENDSAPI_KEY` |
| History | `source: wikipedia` with `get_time_series` or `get_growth` |
| Keyword | Article title or topic, e.g. `large language model` |
| Live `type` | `Wikipedia Trending` |

```bash
curl -sS -X POST https://api.trendsapi.ai/api \
  -H "Authorization: Bearer $TRENDSAPI_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mode":"get_time_series","source":"wikipedia","keyword":"large language model"}'
```

Points typically include `date`, `value`, `volume`, `keyword`, `datatype` (not always `source`).

Titles are picky. `Java` vs `Java (programming language)` are different series. 404 or a tourism-looking series means the wrong sense. This API does not disambiguate.

Do not pass `source: wikipedia` on `get_top_trends`.

Site: [trendsapi.ai/trends/wikipedia-trends](https://trendsapi.ai/trends/wikipedia-trends).

## License

MIT. See [LICENSE](LICENSE).
