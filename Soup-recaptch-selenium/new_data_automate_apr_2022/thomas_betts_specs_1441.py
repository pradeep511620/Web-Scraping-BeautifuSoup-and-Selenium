from bs4 import BeautifulSoup
import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="TESTING"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,attribute_name,attribute_value,sno FROM `attr_1441` where attr_test is null")
myresult = cur.fetchall()
for fetch in myresult:
    url = fetch[0]
    b = bytearray(url)
    product_url = b.decode('utf-8')
    attribute_name = fetch[1]
    attribute_value = fetch[2]
    id = fetch[3]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")
    a = 0
    loc = 0
    label = ""
    flag = 0
    val = ''
    for attr in soup.find("div", class_="productDetailsLeft half-collomn").find_all("td"):
        a += 1
        if a % 2 != 0 and attr.text.lower().strip() == attribute_name.lower().strip():
            loc = a + 1
            label = attr.text

        if a == loc and attribute_value.lower().strip() == attr.text.lower().strip():
            flag = 1
            val = attr.text
            break
    if flag == 1:
        par = ("attribute found")
        sql = ("UPDATE `attr_1441` SET attr_test ='" + str(par) + "' WHERE   sno='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        print("Found Same" + label + " :: " + val + " with " + attribute_name + " = " + attribute_value)
    else:
        par1 = ("attribute not found")
        sql = ("UPDATE `attr_1441` SET attr_test ='" + str(par1) + "' WHERE   sno='" + str(id) + "' ")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        print("Not Found" + attribute_name + " = " + attribute_value)
