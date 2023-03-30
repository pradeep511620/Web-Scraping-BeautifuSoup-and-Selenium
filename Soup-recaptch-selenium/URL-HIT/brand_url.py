
import mysql.connector
import requests
from bs4 import BeautifulSoup
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raptor_supplies_com"
)
cur=mydb.cursor()
cur.execute("SELECT url FROM b2b_brand_url where id=133 ")
myresult=cur.fetchall()
url="https://www.raptorsupplies.es/b/3m"

for fetch in myresult:
    brand_url=fetch[0]

    page = requests.get(brand_url)
    soup=BeautifulSoup(page.content,'xml.dom')
    soup.prettify()
    print(soup.find("div",class_="customRow"))
    for r in soup.find("div",class_="filterGridLeft grayBg").find_all("h3"):
        print(r.text)
        print(brand_url)


