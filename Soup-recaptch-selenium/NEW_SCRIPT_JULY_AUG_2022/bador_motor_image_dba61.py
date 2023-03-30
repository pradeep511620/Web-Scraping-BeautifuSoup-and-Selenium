
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
cur.execute("SELECT product_url,image_name FROM `baldor_sheet_dba61` where image_name !=''   ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    image_name = fetch[1]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")
    for img in soup.find("div",class_='producImg').find_all('a'):
        img1 = (img.get('href'))
        sta = requests.get(img1)
        status = sta.status_code
        # print(status)
        if status == 200:
            image_m = 'https://cdn.raptorsupplies.com/pub/media/catalog/product' + image_name
            if img1 == image_m :
                par = ('same')
                sql = ("UPDATE `baldor_sheet_dba61`    SET image_test ='" + str(
                    par) + "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                par2 = ("not same")
                sql = ("UPDATE `baldor_sheet_dba61`    SET image_test ='" + str(
                    par2) + "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
        else:
            print('something wrong')



