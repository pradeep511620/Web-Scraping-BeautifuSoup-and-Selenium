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
cur.execute("SELECT url,m_brand,heading_name,l1_name,l2_name,l3_name FROM sg_mother_live_test where id>27172")
myresult = cur.fetchall()
for fetch in myresult:
    url = fetch[0]
    brand=fetch[1]
    heading_name=fetch[2]
    l1_name=fetch[3]
    l2_name=fetch[4]
    l3_name=fetch[5]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")

    for brand1 in soup.find("div", class_="l3pagehead").find_all("h1"):
        b=(brand1.text)
        b1=(heading_name)
        if(b.lower().split()==b1.lower().split()):
            b2=("heading same")
            sql = (" UPDATE sg_mother_live_test SET heading_test='" + str(b2) + "'  WHERE url='" + str(url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")
        else:
            b3=("heading not same")
            sql = (" UPDATE sg_mother_live_test SET heading_test='" + str(b3) + "'  WHERE url='" + str(url) + "' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")
        for an in soup.find("div", class_="l3pagehead").find_all("a"):
            a=(an.text)
            c=(brand)
            if (a.lower()==c.lower()):
                a1=("brand same")
                sql = (" UPDATE sg_mother_live_test SET brand_test='" + str(a1) + "'  WHERE url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            else:
                a2=("not same")
                sql = (" UPDATE sg_mother_live_test SET brand_test='" + str(a2) + "'  WHERE url='" + str(url) + "' ")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")
            z=0
            for breadcrumb in soup.find("ul", class_="items").find_all("li"):
                z+=1
                l1=(breadcrumb.text)
                if(z==2):
                    if(l1.lower().split()==l1_name.lower().split()):
                        l1a=("l1_name same")
                        sql = (" UPDATE sg_mother_live_test SET l1_test='" + str(l1a) + "'  WHERE url='" + str(url) + "' ")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "record(s) affected")

                    else:
                        l1b=("l1_name not same")
                        sql = (" UPDATE sg_mother_live_test SET l1_test='" + str(l1b) + "'  WHERE url='" + str(url) + "' ")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "record(s) affected")
                elif(z==3):
                    l2 = (breadcrumb.text)
                    if (l2.lower().split() == l2_name.lower().split()):
                        l2a=("l2_name same")
                        sql = (" UPDATE sg_mother_live_test SET l2_test='" + str(l2a) + "'  WHERE url='" + str( url) + "' ")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "record(s) affected")
                    else:
                        l2b=("l2_name not same")
                        sql = (" UPDATE sg_mother_live_test SET l2_test='" + str(l2b) + "'  WHERE url='" + str(url) + "' ")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "record(s) affected")
                elif(z==4):
                    l3=(breadcrumb.text)
                    if (l3.lower().split() == l3_name.lower().split()):
                        l3a=("l3_name same")
                        sql = (" UPDATE sg_mother_live_test SET l3_test='" + str(l3a) + "'  WHERE url='" + str(url) + "' ")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "record(s) affected")
                    else:
                        l3b=("l3_name not same")
                        sql = (" UPDATE sg_mother_live_test SET l3_test='" + str(l3b) + "'  WHERE url='" + str(url) + "' ")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "record(s) affected")








