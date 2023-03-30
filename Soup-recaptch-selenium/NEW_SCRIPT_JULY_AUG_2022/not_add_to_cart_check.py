
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
cur.execute("SELECT product_url FROM not_add_to_cart_check_dba49 where add_to_cart_check is null ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")

    for x in soup.find("div",class_="btn_wrp c_p_setrfqadd").find_all('div',style=True):
        s = (x.get('style'))
        if s == "display:none":
            prod = 'Found "diplay:none" means add to cart not show '
            sql = ("UPDATE not_add_to_cart_check_dba49 SET add_to_cart_check ='" + str(prod) + "' WHERE   product_url='" + str(
                product_url) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            prod1 = "add to cart show"
            sql = ("UPDATE not_add_to_cart_check_dba49 SET add_to_cart_check ='" + str(prod1) + "' WHERE   product_url='" + str(
                product_url) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
