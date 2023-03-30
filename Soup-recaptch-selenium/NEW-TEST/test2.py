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
cur.execute("SELECT url from test where id between 93 and 264")
myresult=cur.fetchall()
for fetch in myresult:
    mother_url=fetch[0]

    time.sleep(1)
    page = requests.get(mother_url)
    soup = BeautifulSoup(page.content, "lxml")
    t=(page.status_code)
    s=(page.history[0].status_code)
    print(s)





