# live com onb test data (l3,item,parent,product_title)

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
cur.execute("SELECT mother_url,meta_desc,short_desc,id from  mother_content_may_dba16 WHERE short_desc_test = 'short desc not same' ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    meta_desc = fetch[1]
    short_desc = fetch[2]
    id = fetch[3]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content,'html.parser')

    for short in soup.find("div",class_='showmorewrap').find_all('p'):
        sh: str = str(short).replace('<p><br/>','').replace('</p>','').replace('<span id="dots">...</span><span id="more">','').replace('</span><span id="myBtn" onclick="myFunction()" style="display:inline;">Read more</span>','')
        sh1 = html.unescape(sh)
        print(sh1)
        print(short_desc)
        if sh1.strip() == short_desc.strip():
            st = 'short desc same'
            sql = ("UPDATE mother_content_may_dba16 SET short_desc_test ='" + str(
                st) + "' WHERE   id='" + str(
                id) + "'")

            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            st1 = 'short desc not same'
            sql = ("UPDATE mother_content_may_dba16 SET short_desc_test ='" + str(
                st1) + "' WHERE   id='" + str(
                id) + "'")

            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")


        title = soup.find("meta", attrs={'name': 'description'})
        meta = (title["content"] if title else "No meta title given")

        if meta == meta_desc:
            d1 = ('desc same')
            sql = ("UPDATE mother_content_may_dba16 SET meta_desc_test ='" + str(
                d1) + "' WHERE   id='" + str(
                id) + "'")

            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            d1 = ('desc not same')
            sql = ("UPDATE mother_content_may_dba16 SET meta_desc_test ='" + str(
                d1) + "' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")

