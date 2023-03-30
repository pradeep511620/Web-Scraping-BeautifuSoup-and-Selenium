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
cur.execute("SELECT product_url,description,id FROM "
            "`pd_content_dba_122` WHERE description !='' and id>22 ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    description = fetch[1]
    id = fetch[2]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")

    a = 0
    for x in soup.find_all('div', class_='accordion-content')[1].find_next():
        a += 1
        y = str(x).strip()
        de1 = html.unescape(y)
        print(de1)
        print("------")
        # print(description)

        if de1.strip() == description.strip():
            f3 = 'Description same'
            # print(f3)
            sql = ("UPDATE `pd_content_dba_122` SET desc_test ='" + str(
                f3) + "' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            f4 = 'Description not same'
            # print(f4)
            sql = ("UPDATE `pd_content_dba_122` SET desc_test ='" + str(
                f4) + "' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")

