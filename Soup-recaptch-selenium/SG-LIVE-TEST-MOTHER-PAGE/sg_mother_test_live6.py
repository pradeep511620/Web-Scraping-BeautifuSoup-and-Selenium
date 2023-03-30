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
cur.execute("SELECT url,desc_mp,meta_title,meta_desc FROM sg_mother_live_test2 where id>41039")
myresult = cur.fetchall()
for fetch in myresult:
    url = fetch[0]
    desc_mp=fetch[1]
    meta_title=fetch[2]
    meta_desc=fetch[3]

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")

    for title in soup.find_all("title"):
        ti = (title.text)
        if (ti == meta_title):
            mt1 = ("meta title same")
            sql = (" UPDATE sg_mother_live_test2 SET meta_title_check='" + str(mt1) + "'  WHERE url='" + str(url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")
        else:
            mt2 = ("meta title not same")
            sql = (" UPDATE sg_mother_live_test2 SET meta_title_check='" + str(mt2) + "'  WHERE url='" + str(url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")
        for metadesc in soup.find_all("meta", attrs={'name': 'description'}):
            des = metadesc.get("content")

            if (des == meta_desc):
                des1 = ("meat desc same")

                sql = (" UPDATE sg_mother_live_test2 SET meta_desc_check='" + str(des1) + "'  WHERE url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            else:
                des2 = ("meta desc not same")

                sql = (" UPDATE sg_mother_live_test2 SET meta_desc_check='" + str(des2) + "'  WHERE url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")








