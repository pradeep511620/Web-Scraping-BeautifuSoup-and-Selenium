
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
cur.execute("SELECT product_url,product_price FROM oetikar  ")
myresult=cur.fetchall()
for fetch in myresult:
    product_url=fetch[0]
    product_price=fetch[1]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")

    a = 0
    rate=float(product_price)

    for price in soup.find("div", class_="realprice").find_all("span"):
        a += 1
        if (a == 6):
            z = float(price.text)
            h = (rate*1.2*0.95)
            r = decimal.Decimal(h)
            r=(round(r,2))

        elif(a == 3):
            e = (price.text)
            sql = ("UPDATE oetikar SET price_after_discount='" + e + "'  WHERE product_url='" + str(product_url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")









