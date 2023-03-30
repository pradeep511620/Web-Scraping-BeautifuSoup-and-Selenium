
from bs4 import BeautifulSoup
from hurry.filesize import size
import mysql.connector
import requests

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur=mydb.cursor()
cur.execute("SELECT brand_url,l3_url FROM brandtol3 where id between 18789 and 18804")
myresult=cur.fetchall()
for fetch in myresult:
    brand_url=fetch[0]
    categories_url = fetch[1]
    page = requests.get(brand_url)
    soup = BeautifulSoup(page.content, "lxml")

    for link in soup.find('div', class_="filterGridRight").find_all('a'):
        li = link.get("href")

        url4=(categories_url)
        respon = (requests.get(url4))
        response=(respon.status_code)

        if li==url4 :
            b= ("exist")

            sql = (" UPDATE brandtol3 SET status='" + str(response) + "',existance='"+str(b)+"'  WHERE l3_url='" + str(categories_url) + "' ")

            cur.execute(sql)

            mydb.commit()

            print(cur.rowcount, "record(s) affected")



