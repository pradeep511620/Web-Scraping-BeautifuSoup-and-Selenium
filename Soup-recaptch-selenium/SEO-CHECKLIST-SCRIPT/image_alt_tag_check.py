import requests
from bs4 import BeautifulSoup

url = ["https://www.raptorsupplies.com/pd/morse-drum/86",
       "https://www.raptorsupplies.com/pd/krytox/fpg-182-ce4trb"]

for fetch in url:
    page_url = fetch

    page = requests.get(page_url)
    soup = BeautifulSoup(page.content,"html.parser")

    for x in soup.find('div',class_="producImg").find_all('img'):
        if x.get("alt"):
            alt = x.get("alt")
            print(alt)
            # print()
        else:
            print('alt tag not found')

