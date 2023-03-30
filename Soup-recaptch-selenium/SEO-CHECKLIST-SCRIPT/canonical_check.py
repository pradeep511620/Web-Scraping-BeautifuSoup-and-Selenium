import requests
from bs4 import BeautifulSoup

url = ["https://www.raptorsupplies.com/pd/krytox/fpg-182-ce4trb",
       "https://www.raptorsupplies.com/b/dupont-krytox",
       "https://www.raptorsupplies.com/p/krytox/240aa-series-grease",
       "https://www.raptorsupplies.com/c/greases",
       "https://www.raptorsupplies.com/"
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
            if check == page_url:
                flag = 1
    if flag == 1:
        print(page_url)
        print("canonical found correct")
    else:
        print("canonical not found correct")