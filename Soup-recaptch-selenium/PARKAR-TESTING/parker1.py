
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
cur.execute("SELECT url,item_name FROM parker_test where id between 4001 and 4382 ")
myresult=cur.fetchall()
for fetch in myresult:
    url=fetch[0]
    title_name = fetch[1]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")

    a = 0
    for link in soup.find("tr"):
        a += 1
        if (a == 2):
            l1=(link.text)
            url4 = (title_name)
            if (l1==url4) :
                b =("same")
                sql = ("UPDATE parker_test SET item_check='" + str(b) + "'  WHERE url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            else:
                s=("not same")
                sql = ("UPDATE parker_test SET item_check='" + str(s) + "'  WHERE url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")








