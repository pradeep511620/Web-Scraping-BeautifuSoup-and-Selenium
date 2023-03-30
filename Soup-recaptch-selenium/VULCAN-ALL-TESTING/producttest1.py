
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
cur.execute("SELECT product_url,title_name FROM vulcanh1 where id between 11450 and 11493")
myresult=cur.fetchall()
for fetch in myresult:
    product_url=fetch[0]
    title_name = fetch[1]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")

    for heading in soup.find("div",class_="col-sm-7").find_all("h1"):
        h=(heading.text)
        s=(title_name)
        if(h==s):
            t=("same")
            sql = ("UPDATE vulcanh1 SET title_check='" + str(t) + "'  WHERE title_name='" + str(s) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")
        else:
            e=("Not same")
            sql = ("UPDATE vulcanh1 SET title_check='" + str(e) + "'  WHERE title_name='" + str(s) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")















