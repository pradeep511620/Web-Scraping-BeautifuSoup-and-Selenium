from bs4 import BeautifulSoup
import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="Rahul_data_eng"
)

cur = mydb.cursor()
cur.execute("SELECT url,image_url,status_check,id FROM `pd_url` where status_check is null and id>5000 and id<10000")
my_result = cur.fetchall()

for fetch in my_result:
    pd_url = fetch[0]
    b = bytearray(pd_url)
    product_url = b.decode('utf-8')
    image_url = fetch[1]
    status_check = fetch[2]
    id = fetch[3]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content,'html.parser')

    for img in soup.find('div' , class_='producImg').find_all('a'):
        x = img.get("href")
        par = x

        x1 = requests.get(x)
        x2 = x1.status_code

        sql = ("UPDATE `pd_url` SET image_url ='" + str(x) + "',status_check='" + str(x2) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
