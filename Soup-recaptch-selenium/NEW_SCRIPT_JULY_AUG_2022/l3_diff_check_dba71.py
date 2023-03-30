# live com onb test data (l3,item,parent,product_title)

from bs4 import BeautifulSoup
import mysql.connector
import requests
import html

mydb = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="Testing_Automation_Data"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,l3_name FROM `cat_diff_update_dba71` where l3_test is null ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    l3_name = fetch[1]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")

    a = 0
    for bread in soup.find("ul", class_="items breadcrumb").find_all("span"):
        a += 1
        if a == 10:
            l3 = bread.text
            if l3.lower().strip() == l3_name.lower().strip():
                l3_n = "l3_name same"
                sql = ("UPDATE `cat_diff_update_dba71` SET l3_test ='" + str(
                    l3_n) + "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                l3_n1 = "l3_name not same"
                sql = ("UPDATE `cat_diff_update_dba71` SET l3_test ='" + str(
                    l3_n1) + "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
