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
cur.execute("SELECT cat_url,name,sort_order,id FROM `mother_page_order` where brand='DICKSON'   ")
myresult = cur.fetchall()
a = dict()
b = 0
c = []
flag = 0
for fetch in myresult:
    cat_url = fetch[0]
    mother_name = fetch[1]
    sort_order = fetch[2]
    id = fetch[3]
    page = requests.get(cat_url)
    soup = BeautifulSoup(page.content, "html.parser")

    for x in soup.find('div', class_='filterGridRight').find_all('h2', class_='category_l2_title'):
        b += 1
        c = x.text
        if b == int(sort_order) and mother_name.strip() == c.strip():
            flag = 1
            break

    if flag == 1:
        par = "same"
        sql = ("UPDATE `mother_page_order` SET mother_order_test ='" + str(par) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    else:
        par1 = 'not same'
        sql = ("UPDATE `mother_page_order` SET mother_order_test ='" + str(par1) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")

