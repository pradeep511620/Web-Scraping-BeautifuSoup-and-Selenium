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
cur.execute("SELECT url,co_uk_price  FROM issu1115_co_uk where price_test is  null")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    uk_price = fetch[1]


    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")

    a = 0
    rate = float(uk_price)


    for price in soup.find("div", class_="realprice").find_all("span"):
        a += 1

        if (a == 6):

            z = float(price.text)
            r1=(rate * 1.20 )
            r2=(round(r1,4))
            r3=(r2 * 0.95)
            r4=(round(r3,2))
            if (r4 == z):
                pri = ("Price same")
                sql = (" UPDATE issu1115_co_uk SET price_test='" + str(pri) + "',product_price='"+str(z)+"'  WHERE url='" + str(product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
                # print(r4)
                # print(z)
            else:
                el =("Price not same")
                sql = (" UPDATE issu1115_co_uk SET price_test='" + str(el) + "',product_price='"+str(z)+"'  WHERE url='" + str(product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
                print(r4)
                print(z)
        elif(a==3):
            dis=(price.text)
            sql = (" UPDATE issu1115_co_uk SET after_dis_price='" + str(dis) + "' WHERE url='" + str(product_url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")
