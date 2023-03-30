from bs4 import BeautifulSoup

import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur = mydb.cursor()
cur.execute("SELECT url,cat_desc FROM sg_desc_test1 where cat_desc_test is null")
myresult = cur.fetchall()
for fetch in myresult:
    url = fetch[0]
    cat=fetch[1]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    s1=soup.find("div", class_="l3content_desk l3content").find_all("p")
    for l3con in soup.find("div", class_="l3content_desk l3content").find_all("p"):
        con = str(l3con)
        t=(con[3:-4])
        p=(t.replace("&amp;", "&"))
        q=(cat.replace("'",'"'))
        if(p.lower().split()==q.lower().split()):
            d1=("desc same ")
            sql = (" UPDATE sg_desc_test1 SET cat_desc_test='" + str(d1) + "'  WHERE url='" + str(url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")

        else:
            d2=("desc not same")
            sql = (" UPDATE sg_desc_test1 SET cat_desc_test='" + str(d2) + "'  WHERE url='" + str(url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")



