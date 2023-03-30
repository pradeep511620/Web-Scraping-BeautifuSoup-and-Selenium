
from bs4 import BeautifulSoup

import mysql.connector
import requests

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raptor_supplies_com"
)
cur=mydb.cursor()
cur.execute("SELECT product_url,l3_name,parent_name,product_title from sohn_and_kern_uk where l3_test is null ")
myresult=cur.fetchall()
for fetch in myresult:
    url=fetch[0]
    l3_name=fetch[1]
    parent_name=fetch[2]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    a = 0
    for l3 in soup.find("ul", itemtype="https://schema.org/BreadcrumbList").find_all("span"):
        a += 1

        if (a == 4):
            l3a = (l3.text)
            if (l3_name.lower().split() == l3a.lower().split()):
                l3b = ("l3_name is same")
                sql = (" UPDATE sohn_and_kern_uk SET l3_test='" + str(l3b) + "' WHERE product_url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")

            else:
                ln = ("l3_name is not same")
                sql = (" UPDATE sohn_and_kern_uk SET l3_test='" + str(ln) + "' WHERE product_url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")


        elif (a == 5):
            l4 = (l3.text)
            if (parent_name.lower().split() == l4.lower().split()):
                l4a = ("parent_name is same")
                sql = (" UPDATE sohn_and_kern_uk SET parent_test='" + str(l4a) + "' WHERE product_url='" + str(
                    url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")

            else:
                l4b = ("parent_name is not same")
                sql = (" UPDATE sohn_and_kern_uk SET parent_test='" + str(l4b) + "' WHERE product_url='" + str(
                    url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")