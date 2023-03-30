# live com onb test data (l3,item,parent,product_title)

from bs4 import BeautifulSoup
import mysql.connector
import requests
import html

mydb = mysql.connector.connect(
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_dat"
)
cur = mydb.cursor()
cur.execute("SELECT mother_url,mp_header,mp_name,id FROM `mother_page_header` WHERE mother_url LIKE '%.com/p/dickson/%' ")
myresult = cur.fetchall()
b = 0

flag = 0
for fetch in myresult:
    mother_url = fetch[0]
    mp_header = fetch[1]
    mp_name = fetch[2]
    id = fetch[3]
    page = requests.get(mother_url)
    soup = BeautifulSoup(page.content, "html.parser")
    a = mp_header.split('|')
    c = a
    d = []
    for x in soup.find('div', class_='scroll-table').find_all('th'):
        d.append(x.text)

    site_header = d[2:-2]
    site_header1 = d[2:-1]
    sheet_header = c
    price = d[-2]
    # print(price)
    if price == 'Price':
        if sheet_header == site_header:
            par = "same"
            sql = ("UPDATE `mother_page_header` SET mother_header_test ='" + str(par) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            par1 = 'not same'
            sql = ("UPDATE `mother_page_header` SET mother_header_test ='" + str(par1) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
            print("sheet_header", sheet_header)
            print("site_header", site_header)
    else:
        if sheet_header == site_header1:
            par = "same"
            sql = ("UPDATE `mother_page_header` SET mother_header_test ='" + str(par) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            par1 = 'not same'
            sql = ("UPDATE `mother_page_header` SET mother_header_test ='" + str(par1) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
            print("sheet_header", sheet_header)
            print("site_header", site_header)
