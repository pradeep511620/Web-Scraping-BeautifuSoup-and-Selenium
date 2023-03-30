from bs4 import BeautifulSoup

import mysql.connector
import requests
from decimal import localcontext, Decimal, ROUND_HALF_UP

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)

cur = mydb.cursor()
cur.execute("SELECT product_url,price_usd,get_ship  FROM lyon_co_uk")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    sheet_price = fetch[1]
    shiping_charge = fetch[2]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")

    a = 0
    rate = float(sheet_price)
    cal = float(shiping_charge)
    for price in soup.find("div", class_="realprice").find_all("span"):
        a += 1

        if (a == 6):

            z = float(price.text)
            h = ((((rate / 0.7) + cal) * 1.2) * 0.95)

            r1 = (round(h, 2))
            r = (round(h, 2))

            if (r == z):
                pri = ("Price same")
                sql = (" UPDATE lyon_co_uk SET price_test='" + str(pri) + "',product_price='"+str(r)+"'  WHERE product_url='" + str(
                    product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")


            else:
                el =("Price not same")
                sql = (" UPDATE lyon_co_uk SET price_test='" + str(el) + "',product_price='"+str(r)+"'  WHERE product_url='" + str(
                    product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")




