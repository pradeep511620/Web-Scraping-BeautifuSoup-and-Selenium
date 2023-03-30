from bs4 import BeautifulSoup

import mysql.connector
import requests
from decimal import localcontext, Decimal, ROUND_HALF_UP

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raptor_supplies_com"
)
cur = mydb.cursor()
cur.execute("SELECT url,sheet_price  FROM issu_1115 where id > 7204")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    sheet_price = fetch[1]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")

    a = 0
    rate = float(sheet_price)

    for price in soup.find("div", class_="realprice").find_all("span"):
        a += 1

        if (a == 2):

            z = float(price.text)
            h = (rate / 0.7 * 0.95)
            r = (round(h, 2))

            if (r == z):
                pri = ("Price same")
                sql = (" UPDATE issu_1115 SET price_test='" + str(pri) + "',product_price='"+str(r)+"'  WHERE url='" + str(product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
                # print(r)
                # print(z)
            else:
                el =("Price not same")
                sql = (" UPDATE issu_1115 SET price_test='" + str(el) + "',product_price='"+str(r)+"'  WHERE url='" + str(product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
                print(r)
                print(z)