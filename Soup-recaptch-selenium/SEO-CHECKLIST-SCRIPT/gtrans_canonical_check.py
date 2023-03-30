import requests
from bs4 import BeautifulSoup

url = ["https://fi.raptorsupplies.com/pd/krytox/fpg-182-ce4trb",
       "https://fi.raptorsupplies.com/b/dupont-krytox",
       "https://fi.raptorsupplies.com/l1/abrasives",
       "https://fi.raptorsupplies.com/l2/abrasive-accessories",
       "https://fi.raptorsupplies.com/p/krytox/240aa-series-grease",
       "https://fi.raptorsupplies.com/c/greases",
       "https://fi.raptorsupplies.com/",
       "https://fi.raptorsupplies.com/b/3m",
       "https://fi.raptorsupplies.com/b/raxit",
       "https://fi.raptorsupplies.com/b/char-lynn",
       "https://fi.raptorsupplies.com/login",
       "https://fi.raptorsupplies.com/grainger-finland-distributor",
       "https://fi.raptorsupplies.com/b/mcm-alternative-finland",
       "https://fi.raptorsupplies.com/contact"
       ]

for fetch in url:
    page_url = fetch

    page = requests.get(page_url)
    soup = BeautifulSoup(page.content,"html.parser")
    flag = 0
    for x in soup.find_all('link'):
        s = x.get("rel")[0]
        check = x.get('href')
        if s == "canonical":
            print("yes")
            if check == page_url:
                flag = 1
    if flag == 1:
        print("Yes canonical correct of page_url")
        print(page_url)
    else:
        print("No canonical not correct","\n",page_url)
