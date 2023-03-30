from bs4 import BeautifulSoup
import requests

url="https://staging.raptorsupplies.com/pd/strong-hold/45fshd-sc-flp-3"

page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
a=0
for price in soup.find("div",class_="realprice").find_all("span"):
    a+=1
    if(a==2):

        p=float(price.text)
        s=(p)*(0.7)/(0.95)
        print(round(s,2))
