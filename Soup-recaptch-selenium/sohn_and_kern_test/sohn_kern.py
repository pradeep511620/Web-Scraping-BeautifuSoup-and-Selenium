
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
cur.execute("SELECT product_url,l3_name,parent_name,product_title from sohn_and_kern_uk where id>1337")
myresult=cur.fetchall()
for fetch in myresult:
    url=fetch[0]
    l3_name=fetch[1]
    parent_name=fetch[2]
    product_title=fetch[3]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    for title in soup.find("div", class_="col-sm-7").find_all("h1"):
        tit=(title.text)
        if(tit.lower().split()==product_title.lower().split()):
            tit1=("product_title same")
            sql = (" UPDATE sohn_and_kern_uk SET product_title_test='" + str(tit1) + "' WHERE product_url='" + str(url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")
            print(tit)
            print(product_title)

        else:
            tit2=("product_title not same")
            sql = (" UPDATE sohn_and_kern_uk SET product_title_test='" + str(tit2) + "' WHERE product_url='" + str(url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")










