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
cur.execute("SELECT product_url FROM stagingurl")

myresult=cur.fetchall()


with open(r'C:/Users/ashish/Documents/lovejoy.csv','rt')as f:
        data = csv.reader(f)
        for row in itertools.islice(data,0,11):
            st=row[0]
            page = requests.get(st)
            soup = BeautifulSoup(page.content, "html.parser")
            for link in soup.find_all('img', class_="xzoom center-block"):
                links = link.get("xoriginal")
                li=(links)
                li1=(list(li.split("http://")))
                li2=print(li1)
"""        for fetch in myresult:
            url=fetch[0]
            url1=(list(url.split("http://")))
            url2=print(url1)"""
"""           for check in url2:

                for check1 in li2:

                            response = requests.get(check)
                            res = requests.get(check1)
                            img = Image.open(BytesIO(response.content))
                            img1 = Image.open(BytesIO(res.content))

                            

                            if img == img1:
                                print(check,check1+"image is same")
                            else:
                                print(check,check1+"image is not same")"""






