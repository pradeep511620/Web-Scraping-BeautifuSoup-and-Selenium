from bs4 import BeautifulSoup
import mysql.connector
import requests
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raptor_staging"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,attr_name,attr_value FROM `oferta_moters_attr` where product_url is not null")
myresult = cur.fetchall()
for fetch in myresult:

    product_url=fetch[0]
    attribute_name=fetch[1]
    attribute_value=fetch[2]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    a=0
    loc = 0
    label = ""
    flag = 0
    val = ''
    m=0
    for attr in soup.find("div",class_="productDetailsLeft half-collomn").find_all("td"):
        m+=1
        a+=1
        if(a%2!=0 and attr.text == attribute_name):
            loc = a+1
            label = attr.text
        if (a == loc and attribute_value == attr.text):
            flag = 1
            val = attr.text
            break
    if(flag == 1):
        par = ("attribute found")
        sql = ("UPDATE `oferta_moters_attr` SET attr_test ='" + str(par) + "' WHERE   product_url='" + str(
            product_url) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        print("Found Same" + label + " :: " + val + " with " + attribute_name + " = " + attribute_value)
    else:
        par1 = ("attribute not found")
        sql = ("UPDATE `oferta_moters_attr` SET attr_test ='" + str(par1) + "' WHERE   product_url='" + str(
            product_url) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        print("Not Found"+ attribute_name + " = " + attribute_value)


