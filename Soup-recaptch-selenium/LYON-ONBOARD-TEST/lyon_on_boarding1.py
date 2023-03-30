from bs4 import BeautifulSoup
import math
import mysql.connector
import requests
import decimal
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,weigth,shipping_len,shipping_width,country_ori FROM lyon_on_boarding  WHERE weigth_test='weight is not same'")
myresult = cur.fetchall()
for fetch in myresult:

    product_url=fetch[0]
    weigth=float(fetch[1])
    length=float(fetch[2])
    width=float(fetch[3])
    country_ori=fetch[4]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    a=0
    for specs in soup.find("div", class_="col-sm-6 productdetailright").find_all("td"):
        a+=1
        s=(specs.text).strip()
        if(a==2):
            w=(float(weigth*0.45))
            r1 = round(w,2)
            s1=float(s)
            if(r1==s1):
                we=("weight is same")
                sql = (" UPDATE lyon_on_boarding SET weigth_test='" + str(we) + "'  WHERE product_url='" + str(product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
                print(s1)
                print(r1)
            else:
                we1=("weight is not same")
                sql = (" UPDATE lyon_on_boarding SET weigth_test='" + str(we1) + "'  WHERE product_url='" + str(product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
                print(s1)
                print(r1)
        elif(a==4):
            l=float(s)
            l1=(float(length*2.54))
            l2=round(l1,2)
            if(l2==l):
                len=("length is same")
                sql = (" UPDATE lyon_on_boarding SET len_test='" + str(len) + "'  WHERE product_url='" + str(
                    product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")

            else:
                le1=("length is not same")
                sql = (" UPDATE lyon_on_boarding SET len_test='" + str(le1) + "'  WHERE product_url='" + str(
                    product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
        elif(a==6):
            w=float(s)
            w1 = (float(width* 2.54))
            w2 = round(w1, 2)
            if(w2==w):
                wd=("width same")
                sql = (" UPDATE lyon_on_boarding SET width_test='" + str(wd) + "'  WHERE product_url='" + str(
                    product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            else:
                wd1=("width not same")
                sql = (" UPDATE lyon_on_boarding SET width_test='" + str(wd1) + "'  WHERE product_url='" + str(
                    product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
        elif(a==8):
            if(country_ori==s):
                c=("same")
                sql = (" UPDATE lyon_on_boarding SET country_test='" + str(c) + "'  WHERE product_url='" + str(
                    product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            else:
                c1=("not same")
                sql = (" UPDATE lyon_on_boarding SET country_test='" + str(c1) + "'  WHERE product_url='" + str(
                    product_url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")






