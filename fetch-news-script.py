# $ pip install newsapi-python
from newsapi import NewsApiClient # type: ignore

newsapi = NewsApiClient(api_key='5cdaafe1b65b8b79ec0b91884e575256')
# needed a correct api key for this script to work
print("Fetching top headlines...", end="\n\n")
print(newsapi)
# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(language='en', country='in')
print(top_headlines)

if top_headlines:
    def main():
        for article in top_headlines["articles"]:
            title = article["title"]
            print(f"Title: {title}\n")
else:
    print("top_headlines is not functioning properly.")


if __name__ == "__main__":
    main() # to call main function