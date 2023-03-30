
from bs4 import BeautifulSoup
import mysql.connector
import requests
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="new_stage_data"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,country,id FROM `genral_pipe_cleaner` where country_test is null   ")
myresult = cur.fetchall()
try:
    for fetch in myresult:

        product_url=fetch[0]
        country = fetch[1]
        id=fetch[2]

        page = requests.get(product_url)
        soup = BeautifulSoup(page.content, "html.parser")
        a=0
        loc = 0
        label = ""
        flag = 0
        val = ''
        for attr in soup.find("div",class_="productDetailsLeft half-collomn").find_all("td"):

            a+=1
            if(a%2!=0 and attr.text == 'Country of Origin'):
                loc = a+1
                label = attr.text
            if (a == loc and country == attr.text):
                flag = 1
                val = attr.text
                break
        if(flag == 1):
            par = ("country name  found")
            sql = ("UPDATE `genral_pipe_cleaner` SET country_test ='" + str(par) + "' WHERE   id='" + str(id)+"'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
            print("Found Same" + label + " :: " + val + " with " + 'Country of Origin' + " = " + country)
        else:
            par1 = ("country name  not found")
            sql = ("UPDATE `genral_pipe_cleaner` SET country_test ='" + str(par1) + "' WHERE   id='" + str(id)+"' ")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
            print("Not Found"+ 'Country of Origin' + " = " + country)
except:
    pass

