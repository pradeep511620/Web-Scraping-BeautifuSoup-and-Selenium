from bs4 import BeautifulSoup
import mysql.connector
import requests
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="staging_raptor_supplies"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,cross_ref FROM `main_filter_onb` where cross_ref_test is null ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url=fetch[0]
    cross_ref=fetch[1]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    a=0
    for ref in soup.find('div',class_='b_detail').find_all('li'):
        a+=1
        if(a==4):
            cross_refrence=(ref.text)
            cross=cross_refrence.split(' ')
            cross_r=cross[2]
            if(cross_r==cross_ref):
                prod=('cross ref same')
                sql = ("UPDATE `main_filter_onb` SET cross_ref_test ='" + str(prod) + "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                pri=('cross ref not same')

                sql = ("UPDATE `main_filter_onb` SET cross_ref_test ='" + str(pri) + "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")

