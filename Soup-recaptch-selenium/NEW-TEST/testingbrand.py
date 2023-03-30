
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
cur.execute("SELECT url FROM checkl3 where id >953")
myresult=cur.fetchall()
for fetch in myresult:
    brand_url=fetch[0]
    url1=(brand_url)
    page = requests.get(brand_url)
    soup = BeautifulSoup(page.content, "lxml")

    for link in soup.find('div', class_="filterGridRight").find_all('a'):
        li = print(link.get("href"))
    a = 0
    max = 0
    if (soup.find('ul', class_="pagination")):
        for links in soup.find('ul', class_="pagination").find_all('a'):
            li2 = (links.get("href"))
            tmp = int(li2.split('=')[1])
            if (max < tmp):
                max = tmp

        for x in range(2, max + 1):
            url =url1
            url = url + "?page=" + str(x)

            page = requests.get(url)
            soup = BeautifulSoup(page.content, "lxml")

            for link in soup.find('div', class_="filterGridRight").find_all('a'):
                li =print (link.get("href"))

    else:
        print("pagination not found")





