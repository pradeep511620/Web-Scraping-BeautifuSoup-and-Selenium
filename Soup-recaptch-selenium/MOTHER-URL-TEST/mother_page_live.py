
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
cur.execute("SELECT url from mother_url_live where id between 29007 and 42238 ")
myresult=cur.fetchall()
for fetch in myresult:
    url=fetch[0]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    status=(page.status_code)
    st=(page.reason)

    sql = (" UPDATE mother_url_live SET status='" + str(status) + "',testing='"+str(st)+"'  WHERE url='" + str(url) + "' ")
    cur.execute(sql)
    mydb.commit()
    print(cur.rowcount, "record(s) affected")




