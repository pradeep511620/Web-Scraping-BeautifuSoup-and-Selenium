from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests

url='https://www.raptorsupplies.com/b/3m'
page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")
a=0
for url in soup.find_all('link'):
    a += 1
    url_fetch = url.get('href')

    final_url = url_fetch.replace('cdn', "www")
    s = final_url.split('https://www.raptorsupplies.com')
    if(len(s) > 1):
        if (s[1] != '' and len(s[1]) >= 5):
            main_url=(s[1])
            make_url="https://www.raptorsupplies.com"+main_url
            make1 = make_url.split('/')
            f1 = (make1[0:-1])
            string1 = '/'.join(f1)
            p = urlparse(string1)
            print(p.path)
            page = requests.get(string1)
            print(page)
        else:
            main_e=('---')

for url1 in soup.find_all('img'):
    img=url1.get('src')
    final_url1 = img.replace('cdn', "www")
    s1=final_url1.split('https://www.raptorsupplies.com')

    if (len(s1) > 1):
        if (s1[1] != '' and len(s1[1]) >= 5):
            img_url=(s1[1])
            make_url1 = "https://www.raptorsupplies.com" + img_url
            make=make_url1.split('/')
            f = (make[0:-1])
            string = '/'.join(f)
            p = urlparse(string)
            print(p.path)
            page = requests.get(string)
            print(page)
        else:
            img_e=('---')
for url1 in soup.find('div','filterGridRight').find_all('img',class_='lazy'):
    # url=url1.find('img')
    img=url1.get('data-src')

    final_url1 = img.replace('cdn', "www")
    s1=final_url1.split('https://www.raptorsupplies.com')

    if (len(s1) > 1):
        if (s1[1] != '' and len(s1[1]) >= 5):
            img_url=(s1[1])
            make_url1 = "https://www.raptorsupplies.com" + img_url
            make=make_url1.split('/')
            f = (make[0:-1])
            string = '/'.join(f)
            p = urlparse(string)
            print(p.path)
            page = requests.get(string)
            print(page)
        else:
            img_e=('---')








