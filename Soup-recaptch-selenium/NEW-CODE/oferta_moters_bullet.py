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
cur.execute("SELECT product_url,is_bullet FROM `oferta_moters`  where is_bullet !=' '  ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url=fetch[0]
    bullet=fetch[1]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    for bul in soup.find("div",'productDetailsRight half-collomn').find_all('li'):
        prod=(bul.text)
        if(prod==bullet):
            prin=('bullet are same')
            sql = ("UPDATE `oferta_moters` SET bullet_test ='" + str(prin) + "' WHERE   product_url='" + str(
                product_url) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            pri=('bullet not same')
            sql = ("UPDATE `oferta_moters` SET bullet_test ='" + str(pri) + "' WHERE   product_url='" + str(product_url) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")