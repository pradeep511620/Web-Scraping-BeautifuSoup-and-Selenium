
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
cur.execute("SELECT url,item_name FROM chris_lynuk where id between 2000 and 2230")
myresult=cur.fetchall()
for fetch in myresult:
    url=fetch[0]
    item_name = fetch[1]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    a=0
    for link in soup.find("tr"):
        a += 1
        if (a == 2):
            s=(link.text)


            url4=(item_name)
            if s==url4:
                b=("Same")
                sql = ("UPDATE chris_lynuk SET item_check='" + str(b) + "'  WHERE url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            else:
                e=("Not same")
                sql1 = ("UPDATE chris_lynuk SET item_check='" + str(e) + "'  WHERE url='" + str(url) + "' ")
                cur.execute(sql1)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")







