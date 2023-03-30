
from io import BytesIO

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

cur.execute("SELECT url_com,url_staging FROM parker where  id between 1682 and 40382 ")

myresult=cur.fetchall()
for fetch in myresult:
    url_com=fetch[0]

    url_staging= fetch[1]

    page = requests.get(url_com)
    soup = BeautifulSoup(page.content, "lxml")

    page1 = requests.get(url_staging)
    soup1 = BeautifulSoup(page1.content, "lxml")

    for link in soup.find('div', class_="xzoom-container").find_all('a'):
        links = link.get("href")
        lin =(links)

    for link1 in soup1.find('div', class_="xzoom-container").find_all('a'):
        links1 = link1.get("href")
        lin1 = (links1)

        response = (requests.get(lin))
        img = Image.open(BytesIO(response.content))

        res =(requests.get(lin1))
        img1 = Image.open(BytesIO(res.content))
        

        if img==img1:
            a=("image is same")

            sql = (" UPDATE parker SET img_match='" + str(a) + "'  WHERE url_com='" + str(url_com) + "'")

            cur.execute(sql)

            mydb.commit()

            print(cur.rowcount, "record(s) affected")
        else:
            s=("image is not same")

            sql = (" UPDATE parker SET img_match='" + str(s) + "'  WHERE url_com='" + str(url_com) + "'")

            cur.execute(sql)

            mydb.commit()

            print(cur.rowcount, "record(s) affected")


