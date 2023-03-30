import itertools
import urllib.request

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
cur.execute("SELECT url_staging FROM parker where id=1 ")

myresult=cur.fetchall()
for fetch in myresult:
    product_url=fetch[0]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    for link in soup.find('div', class_="xzoom-container").find_all('a'):
        links = link.get("href")
        lin = (links)
        urllib.request.urlretrieve(lin, 'picture1.jpg')




