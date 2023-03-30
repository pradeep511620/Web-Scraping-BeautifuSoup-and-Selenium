import requests
from bs4 import BeautifulSoup
url="https://www.raptorsupplies.com/l2/cabinets"
page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")
a=0
for count1 in soup.find("div",class_="subCat mthr_grp").find_all("h3"):
    d=(count1.text)
    a+=1
    b=0
    for count2 in soup.find("div",class_="subCat mthr_grp").find_all("span"):
        b+=1
        if(b==a):
            c=(count2.text)
            if (c=='()'):
                print("count is Zero")
                print(c)
                print(d)

