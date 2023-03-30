import urllib.request
import time
import mysql.connector
import requests
from bs4 import BeautifulSoup

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur=mydb.cursor()
cur.execute("SELECT mother_url from mothertest where id >= 22630")
myresult=cur.fetchall()
for fetch in myresult:
    mother_url=fetch[0]

    page = requests.get(mother_url)
    soup = BeautifulSoup(page.content, "lxml")


    aw = mother_url
    a = 0
    for crumb in soup.find("ul", class_="items").find_all("span"):
        a += 1
        #time.sleep(3)
        if (a == 2):
            b = (crumb.text)
        elif (a == 3):
            c = (crumb.text)
        elif (a == 4):
            d = (crumb.text.strip())
            sql = ("UPDATE mothertest SET status_code='" + str(page) + "',l1_name='"+str(b)+"',l2_name='"+str(c)+"',l3_name='"+str(d)+"'  WHERE mother_url='" + str(aw) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")
