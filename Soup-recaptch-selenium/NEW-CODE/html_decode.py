from bs4 import BeautifulSoup
import re
import html
from html import unescape
import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="new_stage_data"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,desc_tag,title_tag,description,id  FROM `new_content_1351` where desc_name_test ='not same' limit 1")
myresult = cur.fetchall()
for fetch in myresult:
    url = fetch[0]
    # mother_desc=fetch[1]
    meta_desc=fetch[1]
    title1=fetch[2]
    desc_name=fetch[3]
    id = fetch [4]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    a = 0
    for head in soup.find("div",class_="product-description").find_all("p"):
        a += 1
        if a == 1:
            h = str(head)
            z1 = (h[3:-4])
            z2 = (html.unescape(z1))
            z = z2.lower().split()
            s = desc_name.replace("\n", "").replace("<ahref=","<a href=")
            if z == s:
                print("same")
            else:
                print("not same")
                print(z)
                print(s)














