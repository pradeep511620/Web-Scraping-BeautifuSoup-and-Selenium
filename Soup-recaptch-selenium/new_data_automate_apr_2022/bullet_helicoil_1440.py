from bs4 import BeautifulSoup
import mysql.connector
import requests
import html
mydb = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="TESTING"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,correct_bullet,id FROM `bullet_akro_mills_1440` where  bullet_test ='product detail not found'  ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    bullet = fetch[1]
    id = fetch[2]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")

    for bt in soup.find("div", class_='productDetailsRight half-collomn').find_all("ul"):
        bt1 = str(bt)
        bt2 = html.unescape(bt1)
        s = bt2.replace('="', "=").replace('">', ">")
        print(s)
        print(bullet)
        if s == bullet:
            par = "product detail found"
            sql = ("UPDATE `bullet_akro_mills_1440` SET bullet_test ='" + str(par) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            par1 = "product detail not found"
            sql = ("UPDATE `bullet_akro_mills_1440` SET bullet_test ='" + str(par1) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
            print(product_url)
