
from bs4 import BeautifulSoup
import requests

url="https://www.raptorsupplies.com/p/leeson/3ph-motors-totally-enclosed-general-purpose-standard"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
page=requests.get(url,headers=headers)

soup=BeautifulSoup(page.content,"html.parser")
#test=(soup.find_all("div",class_="prdtls_wrp"),soup.find("a"))
with open('raptorm.csv','w') as f:
    for links1 in soup.find("a"):

        link1=links1.get('href')
        print(str(link1))
        f.write(link1 +'\n')
