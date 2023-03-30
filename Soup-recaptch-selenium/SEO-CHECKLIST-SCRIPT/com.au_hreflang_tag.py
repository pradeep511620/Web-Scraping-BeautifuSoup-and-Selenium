import requests
from bs4 import BeautifulSoup

url = [
    "https://www.raptorsupplies.com.au/pd/krytox/fpg-182-ce4trb",
    "https://www.raptorsupplies.com.au/b/dupont-krytox",
    "https://www.raptorsupplies.com.au/l1/abrasives",
    "https://www.raptorsupplies.com.au/l2/abrasive-accessories",
    "https://www.raptorsupplies.com.au/p/krytox/240aa-series-grease",
    "https://www.raptorsupplies.com.au/c/greases",
    "https://www.raptorsupplies.com.au/",
    "https://www.raptorsupplies.com.au/b/3m",
    "https://www.raptorsupplies.com.au/b/raxit",
    "https://www.raptorsupplies.com.au/b/char-lynn",
    "https://www.raptorsupplies.com.au/login",
    "https://www.raptorsupplies.com.au/grainger-australia",
    "https://www.raptorsupplies.com.au/b/mcmaster-australia",
    "https://www.raptorsupplies.com.au/contact"
]

# "https://www.raptorsupplies.com.au.sg/quotecart",

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
