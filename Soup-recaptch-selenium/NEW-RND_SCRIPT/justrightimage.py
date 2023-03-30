
from io import BytesIO

import cv2
from PIL import Image
from bs4 import BeautifulSoup

import mysql.connector
import requests

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur=mydb.cursor()
cur.execute("SELECT product_url,img_url FROM justrite_img where id=60")

myresult=cur.fetchall()
for fetch in myresult:
    product_url=fetch[0]
    img_url = fetch[1]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    for link in soup.find('div', class_="xzoom-container").find_all('a'):
        links = link.get("href")
        lin = (links)


        url4=(img_url)
        response =( requests.get(lin))
        res =(requests.get(url4))
        img = Image.open(BytesIO(response.content))
        img1 = Image.open(BytesIO(res.content))

        cv2.waitKey(1)
        if img==img1:
            a=("image is same")
        else:
            b=("image is not same")

        sql = (" UPDATE justrite_img SET image='" + str(a) + "',status='"+str(response)+"'  WHERE img_url='" + str(url4) + "'")

        cur.execute(sql)

        mydb.commit()

        print(cur.rowcount, "record(s) affected")


