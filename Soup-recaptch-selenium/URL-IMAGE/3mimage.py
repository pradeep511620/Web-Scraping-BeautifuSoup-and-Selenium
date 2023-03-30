import urllib
from PIL import Image
from bs4 import BeautifulSoup
from hurry.filesize import size
import mysql.connector
import requests

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur=mydb.cursor()
cur.execute("SELECT image_url FROM 3mimage ")

myresult=cur.fetchall()
for fetch in myresult:
    image_url=fetch[0]
    page = requests.get(image_url)
    soup = BeautifulSoup(page.content, "lxml")
    response=requests.get(image_url)
    rs=(response.status_code)
    size1 = requests.get(image_url).content
    y = (len(size1))
    z = (size(y))
    image = Image.open(urllib.request.urlopen(image_url))
    width, height = image.size
    p = (width, height)



    sql = (" UPDATE 3mimage SET image_size='"+str(z)+"',response_status='" + str(rs) + "',image_pixels='"+str(p)+"'  WHERE image_url='" + str(image_url) + "'")

    cur.execute(sql)

    mydb.commit()

    print(cur.rowcount, "record(s) affected")


