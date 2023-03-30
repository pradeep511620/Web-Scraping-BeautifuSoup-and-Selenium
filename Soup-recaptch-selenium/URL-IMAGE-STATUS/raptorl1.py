
from bs4 import BeautifulSoup
import requests

url="https://www.raptorsupplies.com/l1"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
page=requests.get(url,headers=headers)

soup=BeautifulSoup(page.content,"html.parser")
with open('raptorl1.csv','w') as f:
    for links in soup.find("div",class_="container").find_all('a'):
        link=links.get("href")
        print("https://www.raptorsupplies.com"+link)
        f.write("https://www.raptorsupplies.com" + link + '\n')