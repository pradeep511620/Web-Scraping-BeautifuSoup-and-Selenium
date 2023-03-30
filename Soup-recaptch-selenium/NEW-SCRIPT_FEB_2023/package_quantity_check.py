# live com onb test data (l3,item,parent,product_title)

from bs4 import BeautifulSoup
import mysql.connector
import requests
import html

mydb = mysql.connector.connect(
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_dat"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,package_quantity FROM `dba_182_justrite`  ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    pkg_qua = fetch[1]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")
    for pa in soup.find('div',{"id":"quantity"}).find_all("input",class_='qty'):
        qty = pa['value']
        if qty.lower().strip() == pkg_qua.lower().strip():
            prod = "qty same"
            sql = ("UPDATE `dba_182_justrite` SET qty_test ='" + str(prod) + "' WHERE   product_url='" + str(
                product_url) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            prod1 = "qty not same"
            sql = ("UPDATE `dba_182_justrite` SET qty_test ='" + str(prod1) + "' WHERE   product_url='" + str(
                product_url) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")

