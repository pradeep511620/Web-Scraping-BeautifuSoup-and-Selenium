from bs4 import BeautifulSoup

import mysql.connector
import requests
import urllib.request
from hurry.filesize import size

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur = mydb.cursor()
cur.execute("SELECT url from brand_l3_sg_live where id >18078")
myresult = cur.fetchall()
for fetch in myresult:
    url = fetch[0]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    s = (page.status_code)
    # r = urllib.request.urlopen(url)
    # s = (len(r.read()))
    # t = 0
    # if (s > t):
    #     z=(r.getcode())
    sql = (" UPDATE brand_l3_sg_live SET status='" + str(s) + "'  WHERE url='" + str(url) + "' ")
    cur.execute(sql)
    mydb.commit()
    print(cur.rowcount, "record(s) affected")
    # else:
    #     b=("Blank Page")
    #     sql = (" UPDATE brand_l3_sg_liveSET blank_check='" + str(b) + "'  WHERE url='" + str(url) + "' ")
    #     cur.execute(sql)
    #     mydb.commit()
    #     print(cur.rowcount, "record(s) affected")
