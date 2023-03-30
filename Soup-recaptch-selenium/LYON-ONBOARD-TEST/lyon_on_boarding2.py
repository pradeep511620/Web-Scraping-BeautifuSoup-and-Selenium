from bs4 import BeautifulSoup
import math
import mysql.connector
import requests
import decimal
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,item_name,price_usd FROM lyon_on_boarding WHERE price_test='price not same' ")
myresult = cur.fetchall()
for fetch in myresult:

    product_url=fetch[0]
    item_name=fetch[1]
    price_usd=float(fetch[2])


    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    a=0
    for specs in soup.find("div", class_="prodcutspec").find_all("td"):
        a+=1
        if(a==2):
            s=specs.text
            if(s.lower().strip()==item_name.lower().strip()):
                i=("item name same")
                sql = (" UPDATE lyon_on_boarding SET item_test='" + str(i) + "'  WHERE product_url='" + str(product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            else:
                i1=("print not same")
                sql = (" UPDATE lyon_on_boarding SET item_test='" + str(i1) + "'  WHERE product_url='" + str(product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            b=0
            for price in soup.find("div", class_="pricebox").find_all("span"):
                b+=1
                if(b==2):
                    b1=float(price.text)
                    pr=float(price_usd/0.7*0.95)
                    p=round(pr,2)
                    if(b1==p):
                        p1=("price same ")
                        sql = (" UPDATE lyon_on_boarding SET price_test='" + str(p1) + "'  WHERE product_url='" + str(product_url) + "' ")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "record(s) affected")
                    else:
                        p2=("price not same")
                        sql = (" UPDATE lyon_on_boarding SET price_test='" + str(p2) + "'  WHERE product_url='" + str(product_url) + "' ")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "record(s) affected")
                        print(p)
                        print(b1)








