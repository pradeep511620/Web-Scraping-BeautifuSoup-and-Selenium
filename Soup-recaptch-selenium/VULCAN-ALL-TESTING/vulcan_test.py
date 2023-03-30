
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
cur.execute("SELECT product_url,l3_name,item_name,parent_name FROM vulcan_test where id>11109")
myresult=cur.fetchall()
for fetch in myresult:
    url=fetch[0]
    l3_name = fetch[1]
    item_name=fetch[2]
    parent_name=fetch[3]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    a=0
    for link in soup.find('ul',class_="items breadcrumb").find_all("a"):
        a+=1
        if (a==4):
            l3 = (link.text)
            if (l3.lower()==l3_name.lower()):
                s=("same")
                sql = ("UPDATE vulcan_test SET l3_check='" + str(s) + "'  WHERE product_url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            else:
                q=("not same")
                sql = ("UPDATE vulcan_test SET l3_check='" + str(q) + "'  WHERE product_url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
        elif(a==5):
            p = (link.text)
            if(p.lower()==parent_name.lower()):
                p1=("same")
                sql = ("UPDATE vulcan_test SET parent_check='" + str(p1) + "'  WHERE product_url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            else:
                p2=("not same")
                sql = ("UPDATE vulcan_test SET parent_check='" + str(p2) + "'  WHERE product_url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
    b=0
    for title in  soup.find('div',class_="prodcutspec").find_all("td"):
        b+=1
        if(b==2):
            t=title.text
            if(t.lower()==item_name.lower()):
                t=("same")
                sql = ("UPDATE vulcan_test SET item_check='" + str(t) + "'  WHERE product_url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            else:
                i=("not same")
                sql = ("UPDATE vulcan_test SET item_check='" + str(t) + "'  WHERE product_url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")














