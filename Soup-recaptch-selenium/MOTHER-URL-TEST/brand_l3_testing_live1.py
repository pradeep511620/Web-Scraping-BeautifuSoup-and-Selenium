
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
cur.execute("SELECT url from brand_l3_testing_live where id>9800")
myresult=cur.fetchall()
for fetch in myresult:
    url=fetch[0]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    status=(page.status_code)
    st=(page.reason)
    a=0
    for l3 in soup.find('div',class_="l3pagehead").find_all("h1"):

        l3=(l3.text)
        sql = (" UPDATE brand_l3_testing_live SET status='" + str(status) + "',testing='"+str(st)+"' WHERE url='" + str(url) + "' ")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "record(s) affected")




