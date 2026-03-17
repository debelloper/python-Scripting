import requests # pip install requests

sites = ["https://google.com", "https://github.com"] # Add more sites to check here

for site in sites:
    try:
        r = requests.get(site)
        print(site, "UP")
    except:
        print(site, "DOWN")
        