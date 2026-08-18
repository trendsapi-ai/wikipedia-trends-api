from trendsapi_wikipedia import TrendsAPI

client = TrendsAPI()  # TRENDSAPI_KEY
series = client.get_time_series('large language model')
print(series[-1])
growth = client.get_growth('large language model', percent_growth=["12M"])
print(growth["results"][0]["growth"], growth["results"][0]["direction"])
hot = client.get_live(limit=5)
print(hot["data"])
