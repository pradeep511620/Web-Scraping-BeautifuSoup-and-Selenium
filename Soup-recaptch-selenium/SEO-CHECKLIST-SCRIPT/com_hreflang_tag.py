import requests
from bs4 import BeautifulSoup

url = [
       "https://www.raptorsupplies.com/pd/krytox/fpg-182-ce4trb",
       "https://www.raptorsupplies.com/b/dupont-krytox",
       "https://www.raptorsupplies.com/l1/abrasives",
       "https://www.raptorsupplies.com/l2/abrasive-accessories",
       "https://www.raptorsupplies.com/p/krytox/240aa-series-grease",
       "https://www.raptorsupplies.com/c/greases",
       "https://www.raptorsupplies.com/",
       "https://www.raptorsupplies.com/b/3m",
       "https://www.raptorsupplies.com/b/raxit",
       "https://www.raptorsupplies.com/b/char-lynn",
       "https://www.raptorsupplies.com/login",
       "https://www.raptorsupplies.com/ww-grainger-dealer",
       "https://www.raptorsupplies.com/contact",
       "https://www.raptorsupplies.com/c/fasteners/c3/fully-threaded-studs",
       "https://www.raptorsupplies.com/c/fasteners/p/screw-assortments",
        "https://www.raptorsupplies.com/c/fasteners/c4/steel-fully-threaded-studs",
        "https://www.raptorsupplies.com/c/fasteners/c5/grade-2-steel-fully-threaded-studs",
       ]

for fetch in url:
    page_url = fetch

    page = requests.get(page_url)
    soup = BeautifulSoup(page.content,"html.parser")
    flag = 0
    a = 0
    for x in soup.find_all('link'):
        if x.get('hreflang') :
            a += 1
            hg = x.get('href')
            hj = requests.get(hg)
            print(x.get('hreflang'),"href= ",hg,hj)
    print("page url := ", page_url)
    print("number of href lang=",a)
    print('\n')


