from bs4 import BeautifulSoup
import mysql.connector
import requests
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raptor_staging"
)
cur = mydb.cursor()
cur.execute("SELECT url,new_title_tag FROM `cross_ref_add_title_tag` where id>20000")
myresult = cur.fetchall()
for fetch in myresult:
    product_url=fetch[0]
    title_tag=fetch[1]
    page=requests.get(product_url)
    soup=BeautifulSoup(page.content,'lxml')
    for title in soup.find_all('title'):
        tit=(title.text)
        if(tit==title_tag):
            print('title tag is same')
        else:
            print('title tag is not same')
            print(tit)
            print(title_tag)
