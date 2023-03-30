
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
cur.execute("SELECT url from l3_testing_live where id>4393")
myresult=cur.fetchall()
for fetch in myresult:
    url=fetch[0]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    status=(page.status_code)
    st=(page.reason)
    a=0
    for l3 in soup.find('ul',class_="items").find_all("span"):
        a+=1
        if(a==4):
            l3=(l3.text)
            sql = (" UPDATE l3_testing_live SET status='" + str(status) + "',testing='"+str(st)+"',l3_name='"+str(l3)+"' WHERE url='" + str(url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")




