import requests
from bs4 import BeautifulSoup
import time

myresults=['https://productcatalog.martinsprocket.com/views/productinfo.aspx?Part_Number=40A26&Website_CategoryName=Sprockets&Website_Code=SP1']
print(len(myresults))

for result in myresults:
    try:
        url = result
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'lxml')
        time.sleep(3)

        for menu in soup.find_all('a', {'class': 'menu-link'}):
            a =(menu.text.strip() if menu else "not given")
            print(a)
        # for menu2 in soup.find_all("span", {'class': "widget block block - category - link - inline"}):
        #     b = (menu2.text.strip() if menu2 else "not given")
        #     print(b)


    except AttributeError:
        pass