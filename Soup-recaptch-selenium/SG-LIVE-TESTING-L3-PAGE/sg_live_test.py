
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
cur.execute("SELECT url,cate_name,l1_name,l2_name FROM sg_live_test where id>1134")
myresult=cur.fetchall()
for fetch in myresult:
    url=fetch[0]
    cate_name = fetch[1]
    l1_name=fetch[2]
    l2_name=fetch[3]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    a=0
    for cat in soup.find("ul", class_="items").find_all("li"):

            a+=1
            if(a==2):
                l1=(cat.text).strip()
                if(l1_name.lower()==l1.lower()):
                    l1a=("l1_name  same")
                    sql = (" UPDATE sg_live_test SET l1_check='" + str(l1a) + "'  WHERE url='" + str(url) + "' ")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "record(s) affected")
                else:
                    l1b=("l1_name not same")
                    sql = (" UPDATE sg_live_test SET l1_check='" + str(l1b) + "'  WHERE url='" + str(url) + "' ")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "record(s) affected")
            elif(a==3):
                l2=(cat.text).strip()
                l2c=(l2_name).strip()
                if(l2_name.lower()==l2.lower()):
                    l2a=("l2_name same")

                    sql = (" UPDATE sg_live_test SET l2_check='" + str(l2a) + "'  WHERE url='" + str(url) + "' ")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "record(s) affected")
                else:
                    l2b=("l2_name not same")

                    sql = (" UPDATE sg_live_test SET l2_check='" + str(l2b) + "'  WHERE url='" + str(url) + "' ")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "record(s) affected")
            elif(a==4):
                b=(cat.text).strip()
                c=(cate_name).strip()
                if(b.lower()==cate_name.lower()):
                    c1=("cate_name same")
                    sql = (" UPDATE sg_live_test SET cate_check='" + str(c1) + "'  WHERE url='" + str(url) + "' ")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "record(s) affected")
                else:
                    c2=("cate_name not same")
                    sql = (" UPDATE sg_live_test SET cate_check='" + str(c2) + "'  WHERE url='" + str(url) + "' ")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "record(s) affected")


