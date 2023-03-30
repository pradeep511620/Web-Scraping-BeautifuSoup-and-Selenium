
from bs4 import BeautifulSoup

import mysql.connector
import requests
from lxml import html
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raptor_supplies_com"
)
cur = mydb.cursor()
cur.execute("SELECT model_no, product_url,brand, product_title,l3_name,parent_name FROM dectron_on_boarding_co_uk")
myresult = cur.fetchall()
for fetch in myresult:
    model_no = fetch[0]
    product_url=fetch[1]
    brand=fetch[2]
    product_title = fetch[3]
    l3_name=fetch[4]
    parent_name=fetch[5]

    page = requests.get(product_url)
    soup = html.fromstring(page.content, "lxml")
    #soup=BeautifulSoup(page.content,"lxml")
    tree = soup.getroottree()
    a=0
    """for breadcrumb in soup.xpath('/html/body/ul/li[4]/a/span'):

        b=(breadcrumb.text)

        if(l3_name.lower().strip()==b.lower().strip()):
            l3=("l3_name same")
            sql = (" UPDATE dectron_on_boarding_co_uk SET l3_test='" + str(l3) + "'  WHERE product_url='" + str(product_url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")
        else:
            e=("not same")
            sql = (" UPDATE dectron_on_boarding_co_uk SET l3_test='" + str(e) + "'  WHERE product_url='" + str(product_url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")"""
    for breadcrumb in soup.xpath('/html/body/ul/li[5]/a/span'):
            p=(breadcrumb.text)
            if (parent_name.lower().strip() == p.lower().strip()):
                p=("parent_name same")
                sql = (" UPDATE dectron_on_boarding_co_uk SET parent_test='" + str(p) + "'  WHERE product_url='" + str(product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            else:
                p1=("parent not same")
                sql = (" UPDATE dectron_on_boarding_co_uk SET parent_test='" + str(p1) + "'  WHERE product_url='" + str(product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
    """for title in soup.find("div", class_="col-sm-7").find_all("h1"):
        t=(title.text)
        if(product_title.lower().strip()==t.lower().strip()):
            tit=("product title same")
            sql = (" UPDATE dectron_on_boarding_co_uk SET product_test='" + str(tit) + "'  WHERE product_url='" + str(product_url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")
        else:
            tit1=("product title not same")
            sql = (" UPDATE dectron_on_boarding_co_uk SET product_test='" + str(tit1) + "'  WHERE product_url='" + str(product_url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")"""




