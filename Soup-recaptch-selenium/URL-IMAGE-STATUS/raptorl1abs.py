
from bs4 import BeautifulSoup
import requests

url="https://www.raptorsupplies.com/c/ac-motors?page=2"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
page=requests.get(url,headers=headers)

soup=BeautifulSoup(page.content,"html.parser")
with open('raptorcdisc.csv','w') as f:
    for links1 in soup.find_all("img",class_="lazy"):
        link1=links1.get("data-src")

        print(link1)
        f.write(link1 +'\n')
