import itertools
from io import BytesIO
from PIL import Image
import cv2
from PIL import Image
from bs4 import BeautifulSoup
from hurry.filesize import size
import mysql.connector
import requests
import csv
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur=mydb.cursor()
cur.execute("SELECT product_url,image_url FROM imgcompare ")

myresult=cur.fetchall()
for fetch in myresult:
    product_url=fetch[0]
    image_url = fetch[1]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    for link in soup.find('div', class_="xzoom-container").find_all('a'):
        links = link.get("href")
        lin = (links)

        #url2=(lin)
        url4=(image_url)
        response =( requests.get(lin))
        res =(requests.get(url4))
        img = Image.open(BytesIO(response.content))
        img1 = Image.open(BytesIO(res.content))
        #img.show()
        #img1.show()
        cv2.waitKey(1)
        if img==img1:
            a=("image is same")
        else:
            s=("image is not same")
        sql = (" UPDATE imgcompare SET image='" + str(a) + "'  WHERE image_url='" + str(url4) + "'")

        cur.execute(sql)

        mydb.commit()

        print(cur.rowcount, "record(s) affected")


