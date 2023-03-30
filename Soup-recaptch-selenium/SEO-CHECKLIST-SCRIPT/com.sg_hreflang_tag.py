import requests
from bs4 import BeautifulSoup

url = [
    "https://www.raptorsupplies.com.sg/pd/krytox/fpg-182-ce4trb",
    "https://www.raptorsupplies.com.sg/b/dupont-krytox",
    "https://www.raptorsupplies.com.sg/l1/abrasives",
    "https://www.raptorsupplies.com.sg/l2/abrasive-accessories",
    "https://www.raptorsupplies.com.sg/p/krytox/240aa-series-grease",
    "https://www.raptorsupplies.com.sg/c/greases",
    "https://www.raptorsupplies.com.sg/",
    "https://www.raptorsupplies.com.sg/b/3m",
    "https://www.raptorsupplies.com.sg/b/raxit",
    "https://www.raptorsupplies.com.sg/b/char-lynn",
    "https://www.raptorsupplies.com.sg/login",
    "https://www.raptorsupplies.com.sg/grainger-singapore",
    "https://www.raptorsupplies.com.sg/b/mcmaster-carr-singapore",
    "https://www.raptorsupplies.com.sg/contact"
]
# "https://www.raptorsupplies.com.sg.sg/quotecart",
for fetch in url:
    page_url = fetch

    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, "html.parser")
    flag = 0
    a = 0
    for x in soup.find_all('link'):
        if x.get('hreflang'):
            a += 1
            hg = x.get('href')
            hj = requests.get(hg)
            print(x.get('hreflang'), "href= ", hg, hj)
    print("page url := ", page_url)
    print("number of href lang=", a)
    print('\n')
