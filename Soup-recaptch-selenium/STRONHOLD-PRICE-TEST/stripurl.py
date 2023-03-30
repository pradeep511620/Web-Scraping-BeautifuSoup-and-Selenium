import requests
from bs4 import BeautifulSoup

url="https://staging.raptorsupplies.com/pd/strong-hold/46-bb-240-1"
page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")
t="STRONG HOLD 46-BB-240/1 Bin Cabinet, 78 x 48 x 24 Inch Size"
p=float(1601.2)
for title in soup.find("div",class_="col-sm-7").find_all("h1"):
    s=(title.text)
    a = 0
    for price in soup.find("div", class_="realprice").find_all("span"):
        a += 1
        if (a == 2):
            z = float(price.text)
            h = (z) * (0.7) / (0.95)
            r=(round(h,2))
            if(r==p):
                print("same")
                print(r)
            else:
                print("Not same")
                print(r)

            if(s==t):
                print("same")
                print(s)
            else:
                print("not same")
