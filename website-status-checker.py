import requests # pip install requests

sites = ["https://google.com", "https://github.com"] # Add more sites to check here

def check_website_status(site):
    try:
        r = requests.get(site)
        return True
    except:
        return False
for site in sites:
    if check_website_status(site):
        print(site, "UP")
    else:
        print(site, "DOWN")

if __name__ == "__main__":
    print("Website status check completed.")