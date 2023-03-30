
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
cur.execute("SELECT product_url,model_no,attribute_value FROM salsboury_co_uk order by model_no ")
myresult=cur.fetchall()
for fetch in myresult:
    url=fetch[0]
    model=fetch[1]
    attr=fetch[2]

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")


    for link in soup.find("div",class_="col-sm-6 productdetailleft").find_all("td"):

        l1=(link.text)
        if(attr==l1) :
            a=("same")
            sql = ("UPDATE salsboury_co_uk SET specs_test='" + str(a) + "'  WHERE product_url='" + str(url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")
        else:
            b=("not same")












