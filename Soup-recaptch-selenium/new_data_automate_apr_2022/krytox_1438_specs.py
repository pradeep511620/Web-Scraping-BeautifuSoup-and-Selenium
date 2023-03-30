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
cur.execute("SELECT product_url,attr_name,attr_value,id FROM `krytox_specs_1438` ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
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
    for attr in soup.find("div",class_="productDetailsLeft half-collomn").find_all("td"):
        a += 1
        if(a%2!=0 and attr.text.lower().strip() == attribute_name.lower().strip()):
            loc = a+1
            label = attr.text

        if (a == loc and attribute_value.lower().strip() == attr.text.lower().strip()):
            flag = 1
            val = attr.text
            break
    if(flag == 1):
        par = ("attribute found")
        sql = ("UPDATE `krytox_specs_1438` SET attr_test ='" + str(par) + "' WHERE   id='" + str(id)+"'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        print("Found Same" + label + " :: " + val + " with " + attribute_name + " = " + attribute_value)
    else:
        par1 = ("attribute not found")
        sql = ("UPDATE `krytox_specs_1438` SET attr_test ='" + str(par1) + "' WHERE   id='" + str(id)+"' ")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        print("Not Found"+ attribute_name + " = " + attribute_value)



