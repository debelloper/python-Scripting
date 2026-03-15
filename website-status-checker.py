import requests

sites = ["https://google.com", "https://github.com"]

for site in sites:
    try:
        r = requests.get(site)
        print(site, "UP")
    except:
        print(site, "DOWN")