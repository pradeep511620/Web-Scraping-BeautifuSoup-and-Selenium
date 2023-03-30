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
cur.execute("SELECT categories_url,categories_name FROM categories ")

myresult=cur.fetchall()
for fetch in myresult:
    categories_url=fetch[0]
    categories_name = fetch[1]
    page = requests.get(categories_url)
    soup = BeautifulSoup(page.content, "lxml")
    for link in soup.find('div', class_="l3pagehead").find_all('h1'):

        lin =print(len(link.text))
        url4=print(len(categories_name))
        #response =( requests.get(categories_url))
        #res =print (requests.get(url4))
        #img = Image.open(BytesIO(response.content))
        #img1 = Image.open(BytesIO(res.content))
        #img.show()
        #img1.show()
        #cv2.waitKey(1)
        """if lin==url4:
            a=("Name  is same")
        else:
            s=("Name is not same")

        sql = (" UPDATE categories SET response_status='" + str(response) + "'  WHERE categories_url='" + str(categories_url) + "'")

        cur.execute(sql)

        mydb.commit()

        print(cur.rowcount, "record(s) affected")"""


