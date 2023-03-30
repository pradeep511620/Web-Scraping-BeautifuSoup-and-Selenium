import urllib.request
import time
import mysql.connector
import requests
from bs4 import BeautifulSoup

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rahul"
)
cur=mydb.cursor()
cur.execute("SELECT product_url,weigth_size from weigthsab where id between 2938 and 3000 ")
myresult=cur.fetchall()
for fetch in myresult:
    url=fetch[0]
    weigth=fetch[1]
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "lxml")


    for crumb in soup.find("div", class_="productshing").find_all("td"):
        c =(crumb.text.strip())
        if (c == weigth):
            w=("same")
            sql = ("UPDATE weigthsab SET check_weigth='" + str(w) + "'  WHERE product_url='" + str(url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")
