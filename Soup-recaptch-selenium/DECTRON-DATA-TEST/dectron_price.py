from bs4 import BeautifulSoup
import math
import mysql.connector
import requests
import decimal
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raptor_supplies_com"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,price FROM dectron_on_boarding_co_uk where id>36")
myresult = cur.fetchall()
for fetch in myresult:

    product_url=fetch[0]
    price_usd=float(fetch[1])
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    a=0

    for price in soup.find("div", class_="pricebox").find_all("span"):
        a+=1
        if(a==6):
            b1=float(price.text)
            pr=float(((price_usd / 0.7) * 1.2) * 0.95)
            p=round(pr,2)
            pri=round(pr,4)
            if(b1==p):
                p1=("price same ")

                sql = (" UPDATE dectron_on_boarding_co_uk SET price_test='" + str(p1) + "',product_price='"+str(b1)+"' WHERE  product_url='" + str(product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            else:
                p2=("price not same")
                print(b1)
                print(p)

                sql = (" UPDATE dectron_on_boarding_co_uk SET price_test='" + str(pri) + "',product_price='"+str(b1)+"'  WHERE  product_url='" + str(product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")









