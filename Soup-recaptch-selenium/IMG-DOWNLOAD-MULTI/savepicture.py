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
cur.execute("SELECT url_staging FROM parker  ")

myresult=cur.fetchall()
i=0
for fetch in myresult:
    i+=1
    product_url=fetch[0]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    for link in soup.find('div', class_="xzoom-container").find_all('a'):
        links = link.get("href")
        lin = (links)
        for h2q in soup.find_all('span', id="mpnnumber"):
            pname = h2q.text
        # if "https://www.raptorsupplies.com" in lin:
        #     print("if")
        # else:
        #     lin1 = "https://www.raptorsupplies.com" + lin
            # convert the num into string
            #converted_num = str(pname)
            # urllib.request.urlretrieve(lin1,"/dest/path/eee"+converted_num+".jpg")
            s=urllib.request.urlretrieve(lin,"D:/img/img-download"+str(i)+ ".jpg")
            print("pic Download successfully"+str(s))




