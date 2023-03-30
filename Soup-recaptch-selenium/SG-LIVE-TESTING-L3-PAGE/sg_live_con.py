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
cur.execute("SELECT url,cate_desc,meta_title,meta_desc FROM sg_live_test where meta_title_check is null ")
myresult = cur.fetchall()
for fetch in myresult:
    url = fetch[0]
    desc=fetch[1]
    tit=fetch[2]
    met=fetch[3]

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")


    for title in soup.find_all("title"):
        ti=(title.text)
        if(ti==tit):
            mt1=("meta title same")
            sql = (" UPDATE sg_live_test SET meta_title_check='" + str(mt1) + "'  WHERE url='" + str(url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")
        else:
            mt2=("meta title not same")
            sql = (" UPDATE sg_live_test SET meta_title_check='" + str(mt2) + "'  WHERE url='" + str(url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")
        for metadesc in soup.find_all("meta",attrs={'name':'description'}):
            des=metadesc.get("content")
            if(des==met):
                des1=("meat desc same")
                sql = (" UPDATE sg_live_test SET meta_desc_check='" + str(des1) + "'  WHERE url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            else:
                des2=("meta desc not same")
                sql = (" UPDATE sg_live_test SET meta_desc_check='" + str(des2) + "'  WHERE url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")


