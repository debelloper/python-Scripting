# $ pip install newsapi-python
from newsapi import NewsApiClient # type: ignore

newsapi = NewsApiClient(api_key='3a51f959d978424fa0cf2e82e94a6675')
print("Fetching top headlines...", end="\n\n")
print(newsapi)
# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(language='en', country='in')

if top_headlines:
    for article in top_headlines["articles"]:
        title = article["title"]
        print(f"Title: {title}\n")
else:
    print("No articles found.")

