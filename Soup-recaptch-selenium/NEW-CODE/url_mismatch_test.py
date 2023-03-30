import requests
import time
from bs4 import BeautifulSoup
url='https://hu.raptorsupplies.com/b/mcmaster-carr-hungary'
page=requests.get(url)
soup=BeautifulSoup(page.content,'lxml')
for link in soup.find_all('link',rel='alternate'):
    mc_url=link.get('href')
    url1=mc_url.split('/b/')
    url_mc_master=(url1[1])
    base_url='https://hu.raptorsupplies.com/b/'+url_mc_master
    page1=requests.get(base_url)
    print(page1)

    print("make_url="+base_url)
    print("site_url="+mc_url)



