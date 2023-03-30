from bs4 import BeautifulSoup

# import html
from html import unescape
import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur = mydb.cursor()
cur.execute("SELECT url,desc_mp FROM sg_mother_live_test3 where desc_mp_test='desc not same '")
myresult = cur.fetchall()
for fetch in myresult:
    url = fetch[0]

    cat=str(fetch[1])
    cat=cat.replace('&amp;','&')
    cat = unescape(cat)

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")

    for l3con in soup.find("div", class_="l3content_desk l3content").find_all("p"):
        con = (l3con.text)
        #t=(con[3:-4])
        #p=(t.replace("&amp;", "&"))
        #z=(p.replace("<br/>","<br>"))
        # p=html.unescape(cat)
        # t = html.unescape(t)

        if(con.lower().split()==cat.lower().split()):
            d1=("desc same ")
            print(con)
            print(cat)

            sql = (" UPDATE sg_mother_live_test3 SET desc_mp_test='" + str(d1) + "'  WHERE url='" + str(url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")
        else:
            d2=("desc not same")
            print(con)
            print(cat)


            sql = (" UPDATE sg_mother_live_test3 SET desc_mp_test='" + str(d2) + "'  WHERE url='" + str(url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")



