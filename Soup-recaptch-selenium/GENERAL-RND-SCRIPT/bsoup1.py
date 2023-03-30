import username as username
from bs4 import BeautifulSoup
import requests
import csv
url="https://www.grainger.com/category/abrasives/abrasive-blasting/abrasive-blasting-accessories?analytics=nav"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
page=requests.get(url,headers=headers)
soup=BeautifulSoup(page.content,"html.parser")
print(soup.find("p",class_="view-more__content").text)


for detail in soup.find_all("div",class_="product__details-container"):
    for price in soup.find_all("span", class_="pricing__price"):
        print("Detail="+detail.text.strip("  "))
        print("price="+price.text.strip())



