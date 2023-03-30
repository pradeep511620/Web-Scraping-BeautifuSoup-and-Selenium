
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
cur.execute("SELECT url from mother_url where status='404' ")
myresult=cur.fetchall()
for fetch in myresult:
    url=fetch[0]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    status=(page.status_code)
    sql = (" UPDATE mother_url SET status='" + str(status) + "'  WHERE url='" + str(url) + "' ")
    cur.execute(sql)
    mydb.commit()
    print(cur.rowcount, "record(s) affected")
    # for heading in soup.find("div", class_="AttrHead").find_all("b"):
    #     print(heading.text)


