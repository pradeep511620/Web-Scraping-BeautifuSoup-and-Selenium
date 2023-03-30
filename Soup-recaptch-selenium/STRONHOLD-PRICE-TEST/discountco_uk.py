
from bs4 import BeautifulSoup

import mysql.connector
import requests
import decimal

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)

decimal.getcontext().rounding = decimal.ROUND_DOWN
cur=mydb.cursor()
cur.execute("SELECT product_url,sheet_price,shiping_charge  FROM stronghold_co_uk_price ")
myresult=cur.fetchall()
for fetch in myresult:
    product_url=fetch[0]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")

    a = 0

    for price in soup.find("div", class_="realprice").find_all("span"):
        a += 1
        if(a==3):
            p=(price.text)

            sql = ("UPDATE stronghold_co_uk_price SET price_after_discount='" + str(p) + "'  WHERE product_url='" + str(product_url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")






