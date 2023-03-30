from bs4 import BeautifulSoup
import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_dat"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,attribute_value,id FROM dba_216_upc  ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    upc = fetch[1].replace('rp_', '').replace('upc:','')
    id = fetch[2]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")
    a = 0
    loc = 0
    label = ""
    flag = 0
    val = ''
    # s=dict()
    # s[product_url]=soup.find("div",class_="prodcutspec").find_all("td")
    m = 0
    for attr in soup.find("div", class_="productDetailsLeft half-collomn").find_all("td"):
        m += 1
        a += 1
        if (a % 2 != 0 and attr.text == 'UPC'):
            loc = a + 1
            label = attr.text
        if (a == loc and upc == attr.text):
            flag = 1
            val = attr.text
            # print("yes")
            break
    if (flag == 1):
        par = ("attribute found")
        sql = ("UPDATE `dba_216_upc` SET upc_test ='" + str(par) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        print("Found Same" + label + " :: " + val + " with " + "UPC" + " = " + upc)
    else:
        par1 = ("attribute not found")
        sql = ("UPDATE `dba_216_upc` SET upc_test ='" + str(par1) + "' WHERE   id='" + str(id) + "' ")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        print("Not Found" + "UPC" + " = " + upc)