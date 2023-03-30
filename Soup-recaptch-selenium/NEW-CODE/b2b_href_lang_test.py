import requests
from bs4 import BeautifulSoup
url=['https://www.raptorsupplies.dk/b/3m','https://www.raptorsupplies.dk/b/raxit','https://www.raptorsupplies.dk/b/dodge-bearings','https://www.raptorsupplies.dk/b/akro-mils']
for fetch in url:

    page=requests.get(fetch)
    soup=BeautifulSoup(page.content,"lxml")
    for lang in soup.find_all("link",rel='try'):
        print(lang)
        print('-----')