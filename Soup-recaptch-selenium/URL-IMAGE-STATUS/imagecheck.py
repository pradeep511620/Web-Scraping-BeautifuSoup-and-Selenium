import urllib
from tkinter import Image
import httplib2

http = httplib2.Http()
import mysql.connector
from bs4 import BeautifulSoup
import requests
from hurry.filesize import size
from PIL import Image
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur=mydb.cursor()
cur.execute("SELECT url FROM raptorl1abs  ")

myresult=cur.fetchall()

for fetch in myresult:

    url=fetch[0]

    page = requests.get(url,headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    b = (url)

    st1=(page.status_code)
    c=print(st1)

    image = Image.open(urllib.request.urlopen(url))
    width, height = image.size
    p=(width, height)

    size1=requests.get(url).content
    s=(len(size1))
    z=(size(s))


"""
    sql=(" UPDATE raptorl1abs SET status='"+str(c)+"',pixels='"+str(p)+"',size='"+str(z)+"'  WHERE url='"+str(b)+"'")

    cur.execute(sql)

    mydb.commit()

    print(cur.rowcount, "record(s) affected")
"""