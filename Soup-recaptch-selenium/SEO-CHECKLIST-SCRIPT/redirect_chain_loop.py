
from bs4 import BeautifulSoup
import requests

url = ["https://www.raptorsupplies.com/pd/skf-bearings/15796"]

for fetch in url:
    url = fetch
    r = requests.get(url)
    print(r.status_code)
    print(r.url)
