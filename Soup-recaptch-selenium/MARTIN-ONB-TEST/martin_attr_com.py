from bs4 import BeautifulSoup
import mysql.connector
import requests
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raptor_supplies_com"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,attr_name,attr_value FROM martin_attr")
myresult = cur.fetchall()
for fetch in myresult:

    product_url=fetch[0]
    attribute_name=fetch[1]
    attribute_value=fetch[2]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    a=0
    for attr in soup.find("div",class_="col-sm-6 productdetailleft").find_all("td"):
        a+=1
        if(a==4) or (a==6) or (a==8) or (a==10) or (a==12) or (a==14) or (a==16):
            blade=(attr.text)
            if(attribute_value.lower().strip()==blade.lower().strip()):
                attr1=("same")

                sql = ("UPDATE martin_attr SET attr_test ='" + str(attr1) + "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")



