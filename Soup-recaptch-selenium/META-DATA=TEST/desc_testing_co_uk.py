from bs4 import BeautifulSoup

# import html
from html import unescape
import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raptor_supplies_com"
)
cur = mydb.cursor()
cur.execute("SELECT url,desc1 FROM desc_testing_03_03_cat ")
myresult = cur.fetchall()
for fetch in myresult:
    url = fetch[0]
    desc=fetch[1]


    # cat=str(fetch[1])
    # cat=cat.replace('&amp;','&')
    # cat = unescape(cat)

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    """for title1 in soup.find_all("title"):
        print(title1.text)"""


    for head in soup.find("div",class_="l3content_desk l3content").find_all("p"):
        h=(head)
        s=(desc.replace("\n",""))

        if(h==s):
            ti1=print("same")
            print(h)
            print(s)

            """sql = (" UPDATE desc_testing_03_03 SET mother_desc_test='" + str(ti1) + "'  WHERE url='" + str(url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")"""
        else:
            ti2=print("not same")
            print(h)
            print(s)

            """sql = (" UPDATE desc_testing_03_03 SET mother_desc_test='" + str(ti2) + "'  WHERE url='" + str(url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")"""
            # print(h)
            # print(s)

    """for l3con in soup.find_all('meta', attrs={'name':'description'}):
        con = l3con.get("content")
        s=meta_des.replace("\n","")
        if(con==s):
            ti1=("meta_desc same")
            sql = (" UPDATE desc_testing_03_03_cat SET meta_desc_test='" + str(ti1) + "'  WHERE url='" + str(url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")
        else:
            ti2=("meta_desc not same")
            sql = (" UPDATE desc_testing_03_03_cat SET meta_desc_test='" + str(ti2) + "'  WHERE url='" + str(url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")
            print(con)
            print(meta_des)"""













