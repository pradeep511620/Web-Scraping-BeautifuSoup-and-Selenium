
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
cur.execute("SELECT url,price FROM oeitiker_test ")
myresult=cur.fetchall()
for fetch in myresult:
    product_url=fetch[0]
    product_price=fetch[1]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    for title in soup.find("div", class_="col-sm-7").find_all("h1"):
        s = (title.text)
        a = 0
        rate=float(product_price)
        for price in soup.find("div", class_="realprice").find_all("span"):
            a += 1
            if (a == 2):
                z = float(price.text)

                h = (rate)  * (0.95)
                r = (round(h, 2))
                if (r == z):
                    pri=("Price same")
                    sql = ("UPDATE oeitiker_test SET price_check='" + str(pri) + "',product_price='"+str(z)  +"'  WHERE url='" + str(product_url) + "' ")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "record(s) affected")
                else:
                    el=("Price not same")
                    sql=("UPDATE oeitiker_test SET price_check='" + str(el) + "' where url='" + str(product_url) +"' ")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount,"records affected")
