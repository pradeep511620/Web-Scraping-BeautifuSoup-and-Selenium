import requests
from bs4 import BeautifulSoup
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    username='root',
    password='',
    database='staging_raptor_supplies'
)
cur=mydb.cursor()
cur.execute("select product_url from `b2b_pd_test` where random_product is null")
myresults=cur.fetchall()
for fetch in myresults:
    url=fetch[0]
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'lxml')
    a=0
    for ran in soup.find('ul',class_="productListing").find_all('li'):
        a+=1
        ran_product=(ran.text)
    if(a>0):
        y=('yes')
        sql = ("UPDATE `b2b_pd_test` SET random_product ='" + str(y) + "' WHERE   product_url='" + str(url) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    else:
        n=('no')
        sql = ("UPDATE `b2b_pd_test` SET random_product ='" + str(n) + "' WHERE   product_url='" + str(url) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")