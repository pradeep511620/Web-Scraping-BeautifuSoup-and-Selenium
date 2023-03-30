
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
cur.execute('select cat_url,one_liner,id from `brand_new_oneliner_dba_11` ')
myresult = cur.fetchall()
for fetch in myresult:
    cat_url = fetch[0]
    one_liner = fetch[1]
    id = fetch[2]
    page = requests.get(cat_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for s in soup.find('div',class_='oneliner').find_all('p'):
        one = (s.text)
        if one.strip() == one_liner.strip():
            one_l = ('one liner same')
            sql = ("UPDATE `brand_new_oneliner_dba_11` SET one_liner_test ='" + str(one_l) + "' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            one_l1 = ('one liner not same')
            sql = ("UPDATE `brand_new_oneliner_dba_11` SET one_liner_test ='" + str(one_l1) + "' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")