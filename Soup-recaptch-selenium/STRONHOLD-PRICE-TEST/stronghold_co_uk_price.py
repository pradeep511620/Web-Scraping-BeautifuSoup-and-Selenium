
from bs4 import BeautifulSoup

import mysql.connector
import requests

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur=mydb.cursor()
cur.execute("SELECT product_url,sheet_price,shiping_charge  FROM stronghold_co_uk_price ")
myresult=cur.fetchall()
for fetch in myresult:
    product_url=fetch[0]
    sheet_price=fetch[1]
    shiping_charge = fetch[2]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")

    a = 0
    rate=float(sheet_price)
    cal=float(shiping_charge)
    for price in soup.find("div", class_="realprice").find_all("span"):
        a += 1
        if (a == 2):
            z = float(price.text)

            h = ((((rate/0.7) + cal) * 1.2) * 0.95)
            r = (round(h, 2))


            if (r == z):
                pri =("Price same")
                sql = ("UPDATE stronghold_co_uk_price SET check_price='" + str(pri) + "'  WHERE product_url='" + str(product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            else:
                el = ("Price not same")

                sql = ("UPDATE stronghold_co_uk_price SET check_price='" + str(el) + "'  WHERE product_url='" + str(product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")

