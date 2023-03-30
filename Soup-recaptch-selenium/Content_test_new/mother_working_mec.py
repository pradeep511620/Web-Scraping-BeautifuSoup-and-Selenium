# live com onb test data (l3,item,parent,product_title)
import time

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
cur = mydb.cursor(buffered=True)
cur.execute(
    "SELECT url,short_desc,working_mec,id FROM `mother_content_dba_156` where working_mec !='' ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    description = fetch[1]
    working_mec = fetch[2]
    id = fetch[3]
    page = requests.get(product_url)
    st = (page.status_code)
    if st == 200:
        soup = BeautifulSoup(page.content, "html.parser")
        if soup.find("div", class_='mother_newsection').find_all('h4'):
            for x in soup.find("div", class_='mother_newsection').find_all('h4'):
                y = x.text
                print(y)
                if y == "Working Mechanism":
                    c = str(x.find_next())
                    c1 = c.replace('<ul>', '').replace('</ul>', '').replace('<p>', '').replace('</p>', '').replace(
                        "</li> <li>", '</li><li>')
                    c2 = html.unescape(c1)
                    working_mec = working_mec.replace('</li> ', '</li>')
                    # print(c2)
                    # print('--')
                    # print(working_mec)
                    if c2.strip() == working_mec.strip():
                        c3 = 'working mechanism same'
                        sql = ("UPDATE `mother_content_dba_156` SET working_mec_test ='" + str(
                            c3) + "' WHERE   id='" + str(
                            id) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done in db")
                    else:
                        c4 = 'working mechanism not same'
                        sql = ("UPDATE `mother_content_dba_156` SET working_mec_test ='" + str(
                            c4) + "' WHERE   id='" + str(
                            id) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
        else:
            print('not find')
    else:
        print("404", product_url)
