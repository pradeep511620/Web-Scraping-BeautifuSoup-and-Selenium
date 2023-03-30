
from bs4 import BeautifulSoup

import mysql.connector
import requests

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raptor_supplies_com"
)
cur=mydb.cursor()
cur.execute("SELECT distinct l2_url from l2_url_count_check")
myresult=cur.fetchall()
for fetch in myresult:
    url=fetch[0]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    a = 0
    for count1 in soup.find("div", class_="subCat mthr_grp").find_all("h3"):
        d = (count1.text)
        a += 1
        b = 0
        for count2 in soup.find("div", class_="subCat mthr_grp").find_all("span"):
            b += 1
            if (b == a):
                c =print (count2.text)
                print(url)
                if (c == '()'):
                    print("count is Zero")
                    print(c)
                    print(d)







