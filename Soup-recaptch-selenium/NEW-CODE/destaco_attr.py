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
cur.execute("SELECT product_url,attribute_value FROM `destaco_attr` where uk_attr_test is null")
myresult = cur.fetchall()
for fetch in myresult:
    product_url=fetch[0]
    #attribute_name=fetch[1]
    attribute_value=fetch[1]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    a=0
    for attr in soup.find("div",class_="prodcutspec").find_all("td"):
        a+=1
        if(a==4) or (a==6) or (a==8) or (a==10) or (a==12) or (a==14) or (a==16) or (a==18) or (a==20) or (a==22) or (a==24):
            blade=(attr.text)
            if(attribute_value.lower().strip()==blade.lower().strip()):
                attr1=("same")
                sql = ("UPDATE `destaco_attr` SET uk_attr_test ='" + str(attr1) + "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")



