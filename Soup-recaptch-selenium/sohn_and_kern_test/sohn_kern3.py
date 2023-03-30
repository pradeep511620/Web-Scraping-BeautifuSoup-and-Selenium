
from bs4 import BeautifulSoup
import math
import mysql.connector
import requests

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raptor_supplies_com"
)
cur=mydb.cursor()
cur.execute("SELECT product_url,price from sohn_and_kern_uk where price_test ='price not same'")
myresult=cur.fetchall()
for fetch in myresult:
    url=fetch[0]

    price1=float(fetch[1])
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    a=0
    for price in soup.find("div", class_="realprice").find_all("span"):
        a+=1
        if(a==6):
            pr=float(price.text)

            p=(price1/.7)
            p1=round(p,4)
            p2=(p1*1.2)
            p3=round(p2,2)
            p4=(p3*.95)
            pr1=math.trunc(p4)
            print(pr1)
            """if(pr==pr1):
                pr2=("price same")
                sql = (" UPDATE sohn_and_kern_uk SET price_test='" + str(pr2) + "',product_price='"+str(pr)+"'  WHERE product_url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            else:
                pr3=("price not same")
                sql = (" UPDATE sohn_and_kern_uk SET price_test='" + str(pr3) + "',product_price='"+str(pr)+"' WHERE product_url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
                print(pr)
                print(pr1)"""











