import requests
from bs4 import BeautifulSoup
import re

url = ["https://www.raptorsupplies.com/pd/krytox/fpg-182-ce4trb"]

for fetch in url:
    page_url = fetch

    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, "html.parser")
    a = 0
    for crum in soup.find("ul", class_="items breadcrumb").find_all("li"):
        a += 1

        if a == 1:
            s = crum.text
            s1 = s.split('\n')
            s2 = "".join(s1)
            print("Home- ", s2)
        elif a == 2:
            print("l1-  ", crum.text)
        elif a == 3:
            print("l2- ", crum.text)
        elif a == 4:
            print("l3- ", crum.text)
        elif a == 5:
            print("mother- ", crum.text)
