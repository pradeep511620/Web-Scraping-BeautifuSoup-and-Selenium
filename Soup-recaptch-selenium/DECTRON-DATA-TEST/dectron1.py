from bs4 import BeautifulSoup
import math
import mysql.connector
import requests
import decimal
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raptor_supplies_com"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,item_name,country_org FROM dectron_on_boarding_co_uk")
myresult = cur.fetchall()
for fetch in myresult:

    product_url=fetch[0]
    item_name=fetch[1]
    country_ori=fetch[2]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    a=0
    for specs in soup.find("div", class_="productshing").find_all("td"):
        a+=1
        s=(specs.text).strip()
        if(a==2):
            if(country_ori==s):
                c=("same")

                sql = (" UPDATE dectron_on_boarding_co_uk SET country_test='" + str(c) + "'  WHERE product_url='" + str(product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            else:
                c1=("not same")

                sql = (" UPDATE dectron_on_boarding_co_uk SET country_test='" + str(c1) + "'  WHERE product_url='" + str(product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            b=0
            for item in soup.find("div", class_="prodcutspec").find_all("td"):
                b+=1
                if(b==2):
                    i=(item.text)
                    if(i==item_name):
                        i1=("item_name same")
                        sql = (" UPDATE dectron_on_boarding_co_uk SET item_test='" + str(i1) + "'  WHERE product_url='" + str(product_url) + "' ")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "record(s) affected")
                    else:
                        i2=("item_name not same")
                        sql = (" UPDATE dectron_on_boarding_co_uk SET item_test='" + str(i2) + "'  WHERE product_url='" + str(product_url) + "' ")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "record(s) affected")






