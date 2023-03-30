import urllib
import mysql.connector
from bs4 import BeautifulSoup


import requests

from hurry.filesize import size
from PIL import Image
#headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur=mydb.cursor()

cur.execute("SELECT url FROM raptoracmoters")

myresult=cur.fetchall()


for row in myresult:

    image_url = row[0]

    result = requests.get(image_url)

    print(result.status_code)

    print(image_url)


