from bs4 import BeautifulSoup

import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur = mydb.cursor()
cur.execute("SELECT model_no, product_url,brand, l3_name,parent_name,product_title FROM lyon_on_boarding")
myresult = cur.fetchall()
for fetch in myresult:
    model_no = fetch[0]
    product_url=fetch[1]
    brand=fetch[2]
    l3_name=fetch[3]
    parent_name=fetch[4]
    product_title=fetch[5]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    a=0
    for breadcrumb in soup.find("ul", class_="items breadcrumb").find_all("li"):
        a+=1
        if(a==4):
            b=(breadcrumb.text)
            if(l3_name.lower().strip()==b.lower().strip()):
                l3=("l3_name same")
                sql = (" UPDATE lyon_on_boarding SET l3_test='" + str(l3) + "'  WHERE product_url='" + str(product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            else:
                e=("not same")
                sql = (" UPDATE lyon_on_boarding SET l3_test='" + str(e) + "'  WHERE product_url='" + str(product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
        elif(a==5):
            p=(breadcrumb.text)
            if (parent_name.lower().strip() == p.lower().strip()):
                p=("parent_name same")
                sql = (" UPDATE lyon_on_boarding SET parent_test='" + str(p) + "'  WHERE product_url='" + str(product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            else:
                p1=("not same")
                sql = (" UPDATE lyon_on_boarding SET parent_test='" + str(p1) + "'  WHERE product_url='" + str(product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            for title in soup.find("div", class_="col-sm-7").find_all("h1"):
                t=(title.text)
                if(product_title.lower().strip()==t.lower().strip()):
                    tit=("product title same")
                    sql = (" UPDATE lyon_on_boarding SET product_test='" + str(tit) + "'  WHERE product_url='" + str(product_url) + "' ")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "record(s) affected")
                else:
                    tit1=("product title not same")
                    sql = (" UPDATE lyon_on_boarding SET l3_test='" + str(tit1) + "'  WHERE product_url='" + str(product_url) + "' ")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "record(s) affected")




