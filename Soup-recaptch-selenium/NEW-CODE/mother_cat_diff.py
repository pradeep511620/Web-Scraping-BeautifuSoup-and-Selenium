import requests
from bs4 import BeautifulSoup
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    username='root',
    password='',
    database='db1'
)
cur=mydb.cursor()
cur.execute("select product_url from `mother_cat_diff` where l3_name_uk is null ")
myresults=cur.fetchall()
for fetch in myresults:
    product_url=fetch[0]
    page=requests.get(product_url)
    soup=BeautifulSoup(page.content,'lxml')
    a = 0
    for bread in soup.find("ul", itemtype="https://schema.org/BreadcrumbList").find_all("span"):
        a += 1
        if (a == 4):
            l3 = (bread.text)
            sql = ("UPDATE `mother_cat_diff` SET l3_name_uk ='" + str(l3) + "' WHERE   product_url='" + str(
                product_url) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")