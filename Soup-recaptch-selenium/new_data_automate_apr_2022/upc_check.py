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
cur.execute("SELECT product_url,upc,sno FROM `thomas_betts_1441` where  upc_test is null ")
myresult = cur.fetchall()

for fetch in myresult:
    url = fetch[0]
    b = bytearray(url)
    product_url = b.decode('utf-8')
    upc1 = fetch[1]
    id = fetch[2]
    upc = upc1
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")
    a = 0
    loc = 0
    label = ""
    flag = 0
    val = ''
    for attr in soup.find("div",class_="productDetailsLeft half-collomn").find_all("td"):

        a += 1
        if a%2!=0 and attr.text == 'UPC':
            loc = a+1
            label = attr.text
        if a == loc and upc == attr.text:
            flag = 1
            val = attr.text
            break
    if flag == 1:
        par = "upc found same"
        sql = ("UPDATE `thomas_betts_1441` SET upc_test ='" + str(par) + "' WHERE   sno='" + str(id)+"'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        print("Found Same" + label + " :: " + val + " with " + 'upc' + " = " + upc)
    else:
        par1 = "upc found not same"
        sql = ("UPDATE `thomas_betts_1441` SET upc_test ='" + str(par1) + "' WHERE   sno='" + str(id)+"' ")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        print("Not Found" + 'upc' + " = " + upc)


