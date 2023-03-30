import urllib
from tkinter import Image

import mysql.connector
from bs4 import BeautifulSoup
import requests

from PIL import Image
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur=mydb.cursor()
cur.execute("SELECT url FROM raptorcdisc where id between 236 and 242 ")

myresult=cur.fetchall()

for fetch in myresult:

    url=fetch[0]

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    b = (url)

    #st = page.history
    #a= (st)
    st1=page.status_code
    c=(st1)
    """image = Image.open(urllib.request.urlopen(url))
    width, height = image.size
    print(width, height)"""
    size=requests.get(url).content
    s=(len(size))



    sql=(" UPDATE raptorcdisc SET status='"+str(c)+"',size='"+str(s)+"'  WHERE url='"+str(b)+"'")

    cur.execute(sql)

    mydb.commit()

    print(cur.rowcount, "record(s) affected")