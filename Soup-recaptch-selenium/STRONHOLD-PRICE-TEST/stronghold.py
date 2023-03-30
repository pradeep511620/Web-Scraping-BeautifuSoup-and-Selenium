
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
cur.execute("SELECT product_url,product_title,product_price FROM stronghold_test ")
myresult=cur.fetchall()
for fetch in myresult:
    product_url=fetch[0]
    product_title=fetch[1]
    product_price=fetch[2]
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
                h = (z) * (0.7) / (0.95)
                r = (round(h, 2))
                if (r == rate):
                    pri=("Price same")
                    sql = ("UPDATE stronghold_test SET price_check='" + str(pri) + "'  WHERE product_url='" + str(product_url) + "' ")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "record(s) affected")
                else:
                    el=("Price not same")
                    sql=("UPDATE stronghold_test SET price_check='" + str(el) + "' where product_url='" + str(product_url) +"' ")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount,"records affected")
                if (s == product_title):
                    tit=("same")
                    sql=("UPDATE stronghold_test SET title_check='"+ str(tit) +"' WHERE product_url='" + str(product_url) +"'  ")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount,"records affected")
                else:
                    tie=("not same")
                    sql=("UPDATE stronghold_test SET title_check='" + str(tie)+ "' WHERE product_url='" + str(product_url)+"' ")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount,"records affected")
