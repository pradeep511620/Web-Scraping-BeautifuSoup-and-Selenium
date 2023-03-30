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
cur.execute("SELECT product_url,attr_name,attr_value,id FROM `rub_valves_attr` ")
myresult = cur.fetchall()
for fetch in myresult:

    product_url=fetch[0]
    attribute_name=fetch[1]
    attribute_value=fetch[2]
    id=fetch[3]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    a=0
    loc = 0
    label = ""
    flag = 0
    val = ''
    # s=dict()
    # s[product_url]=soup.find("div",class_="prodcutspec").find_all("td")
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
        sql = ("UPDATE `rub_valves_attr` SET attr_test ='" + str(par) + "' WHERE   id='" + str(id)+"'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        print("Found Same" + label + " :: " + val + " with " + attribute_name + " = " + attribute_value)
    else:
        par1 = ("attribute not found")
        sql = ("UPDATE `rub_valves_attr` SET attr_test ='" + str(par1) + "' WHERE   id='" + str(id)+"' ")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        print("Not Found"+ attribute_name + " = " + attribute_value)


