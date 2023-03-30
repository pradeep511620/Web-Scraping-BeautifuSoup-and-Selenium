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

# for s in url:
#     link=s
#     page = requests.get(link)
#     soup = BeautifulSoup(page.content, "lxml")
#     a = dict()
#     t = dict()
#     count = 0
#     for tex in soup.find_all('link', rel='alternate'):
#         s = (tex.get('href'))
#         z = (tex.get('hreflang'))
#         print(s)
#         print(z)
#     print('------')
        # count += 1
        # a[count] = s
        # t[s] = count
    # print(a)
    # print(t)
    # print(str(a))
for s in url:
    link=s
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "lxml")
    try:
        for fetch in soup.find('div',class_='footer-right').find_all('a'):
            footer_url=fetch.get('href')
            page1 = requests.get(footer_url)
            print(footer_url)
            print(page1.status_code)
        print('----------')
    except:
        pass








