from bs4 import BeautifulSoup
from hurry.filesize import size
import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur = mydb.cursor()
cur.execute("SELECT url,description FROM co_uk1")
myresult = cur.fetchall()
for fetch in myresult:
    brand_url = fetch[0]
    meta_desc = fetch[1]

    page = requests.get(brand_url)
    soup = BeautifulSoup(page.content, "lxml")

    for link in soup.find_all('p',class_="comment more"):
        li=(link.text)

        if li == meta_desc:
            a = ("same")

            sql = (" UPDATE co_uk1 SET desc_match='" + str(a) + "'  WHERE url='" + str(brand_url) + "' ")
            cur.execute(sql)




            mydb.commit()

            print(cur.rowcount, "record(s) affected")





