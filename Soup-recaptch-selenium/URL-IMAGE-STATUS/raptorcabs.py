import urllib
from tkinter import Image

from bs4 import BeautifulSoup
import requests
from PIL import Image
from hurry.filesize import size

url="https://www.raptorsupplies.com/p/leeson/3ph-motors-totally-enclosed-general-purpose-standard"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
page=requests.get(url,headers=headers)

soup=BeautifulSoup(page.content,"html.parser")
with open('raptorcdisc.csv','w') as f:
    for links1 in soup.find_all("img"):
        link=links1.get('src')
        print(link)
        f.write(link + '\n')


