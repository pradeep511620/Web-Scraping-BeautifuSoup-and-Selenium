
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
cur.execute("SELECT url,title_name FROM chris_lynuk where id between 2000 and 2230 ")
myresult=cur.fetchall()
for fetch in myresult:
    url=fetch[0]
    title_name = fetch[1]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")

    for link in soup.find_all('h1'):
        li = (link.text)

        url4=(title_name)

        if li==url4 :
            b = ("same")
            sql = ("UPDATE chris_lynuk SET title_check='" + str(b) + "'  WHERE title_name='" + str(url4) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")
        else:
            e = ("Not same")
            sql1=("UPDATE chris_lynyk SET check1='" + str(e) +"' WHERE title_name='"+str(url4)+"' ")
            cur.execute(sql1)
            mydb.commit()
            print(cur.rowcount,"records affected")







