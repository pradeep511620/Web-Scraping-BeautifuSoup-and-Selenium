
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
cur.execute("SELECT brands_url,categories_url FROM brand where id between 1433 and 1521")
myresult=cur.fetchall()
for fetch in myresult:
    brand_url=fetch[0]
    categories_url = fetch[1]
    page = requests.get(brand_url)
    soup = BeautifulSoup(page.content, "lxml")

    for link in soup.find('div', class_="catItem").find_all('a'):
        li = link.get("href")



        url4=(categories_url)
        response = (requests.get(li))

        if li==url4 :
            b= ("exist")

            sql = (" UPDATE brand SET status='" + str(response) + "',existance='"+str(b)+"'  WHERE categories_url='" + str(categories_url) + "' ")

            cur.execute(sql)

            mydb.commit()

            print(cur.rowcount, "record(s) affected")



