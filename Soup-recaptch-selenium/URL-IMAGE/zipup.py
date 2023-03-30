import urllib
from tkinter import Image

import mysql.connector
from bs4 import BeautifulSoup
import requests
from hurry.filesize import size
from PIL import Image
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur=mydb.cursor()
cur.execute("SELECT url FROM raptorcabs where id between 370 and 466")

myresult=cur.fetchall()

for fetch in myresult:

    url=fetch[0]

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    b = (url)

    a = urllib.request.urlopen(url)
    c = (a.getcode())
    """st1=page.status_code
    c=print(st1)"""

    image = Image.open(urllib.request.urlopen(url))
    width, height = image.size
    p=(width, height)

    """size1=requests.get(url).content
    s=(len(size1))
    z=print(size(s))"""




    sql=(" UPDATE raptorcabs SET status='"+str(c)+"',pixels='"+str(p)+"'  WHERE url='"+str(b)+"'")

    cur.execute(sql)

    mydb.commit()

    print(cur.rowcount, "record(s) affected")