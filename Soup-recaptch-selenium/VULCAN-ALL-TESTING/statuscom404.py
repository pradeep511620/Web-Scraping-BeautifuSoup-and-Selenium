
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
cur.execute("SELECT url from testingcom404")
myresult=cur.fetchall()
for fetch in myresult:
    url=fetch[0]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    s=(page.status_code)
    h=(page.history)
    sql = ("UPDATE testingcom404 SET status='" + str(s) + "',response='" + str(h)+"'  WHERE url='" + str(url) + "' ")
    cur.execute(sql)
    mydb.commit()
    print(cur.rowcount, "record(s) affected")