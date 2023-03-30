import requests
from bs4 import BeautifulSoup
url=['https://www.raptorsupplies.com',
     'https://www.raptorsupplies.com/l1/abrasives',
     'https://www.raptorsupplies.com/l2/abrasive-accessories',
     'https://www.raptorsupplies.com/c/abrasive-mandrels',
     'https://www.raptorsupplies.com/p/merit/bore-polisher-extension-mandrel',
     'https://www.raptorsupplies.com/pd/merit/08834154463',
     'https://www.raptorsupplies.com/b/3m',
     'https://www.raptorsupplies.com/b/raxit',
     'https://www.raptorsupplies.com/b/dodge-bearings']
for s in url:
    link=s
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "lxml")
    for fetch in soup.find_all('meta',attrs={'name':'robots'}):
        index_test=fetch.get('content')

        print(index_test)
    print('----------')
