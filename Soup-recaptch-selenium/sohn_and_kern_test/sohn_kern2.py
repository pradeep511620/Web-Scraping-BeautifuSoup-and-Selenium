
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
cur.execute("SELECT product_url,item_name from sohn_and_kern_uk where item_name_test is null")
myresult=cur.fetchall()
for fetch in myresult:
    url=fetch[0]
    item_name=fetch[1]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    a=0
    for title in soup.find("div", class_="prodcutspec").find_all("td"):
        a+=1
        if(a==2):
            tit=(title.text)
            if(tit.lower().split()==item_name.lower().split()):
                tit1=("item_name same")
                sql = ("UPDATE sohn_and_kern_uk SET item_name_test='" + (tit1) + "' WHERE product_url='" + str(url)+"'")

                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            else:
                tit2=("product_title not same")
                sql = (" UPDATE sohn_and_kern_uk SET item_name_test='" + str(tit2) + "' WHERE product_url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount,"record(s) affected")










