
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
cur.execute("SELECT product_url,parent_name FROM salsboury_parent where id between 29610 and 3000")
myresult=cur.fetchall()
for fetch in myresult:
    url=fetch[0]
    parent=fetch[1]


    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")

    a=0
    for link in soup.find("ul",class_="items breadcrumb").find_all("a"):
        a+=1
        if (a==5):
            l1=(link.text)
            url2=(parent)
            if (l1.lower()==url2.lower()) :
                b =("same")
                sql = ("UPDATE salsboury_parent SET parent_check='" + str(b) + "'  WHERE product_url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            else:
                s=("not same")
                sql = ("UPDATE salsboury_parent SET parent_check='" + str(s) + "'  WHERE product_url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")













