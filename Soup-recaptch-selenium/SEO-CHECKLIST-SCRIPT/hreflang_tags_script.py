import requests
from bs4 import BeautifulSoup
import re
url = ["https://www.raptorsupplies.com/pd/krytox/fpg-182-ce4trb"
       # "https://www.raptorsupplies.com/b/dupont-krytox",
       # "https://www.raptorsupplies.com/p/krytox/240aa-series-grease",
       # "https://www.raptorsupplies.com/c/greases",
       # "https://www.raptorsupplies.com/"
       ]

for fetch in url:
    page_url = fetch

    page = requests.get(page_url)
    soup = BeautifulSoup(page.content,"html.parser")
    flag = 0
    # s = []
    for x in soup.find_all('head'):
        c = str(x)
        s = "\<[a-zA-Z]+.*?\>|\</[a-zA-Z]+.*?\>"
        new_results = re.findall(s, c)
        print(new_results)