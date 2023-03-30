
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
cur.execute('select url,heading,description,id from `brand_competative_dba_156` where id>8 ')
myresult = cur.fetchall()
for fetch in myresult:
    brand_url = fetch[0]
    heading = fetch[1]
    description = fetch[2]
    id = fetch[3]
    page = requests.get(brand_url)
    soup = BeautifulSoup(page.content,'html.parser')
    flag = 0
    a = ''
    for x in soup.find('section', class_='major-trade competitivee').find_all('p'):
        comp = x.text
        comp1 = comp.replace('...Read More', '').replace('...','')
        # print(comp1)
        # print('---')
        # print(description)
        if comp1.strip() == description.strip():
            flag = 1
            break
    if flag == 1:
        s1 = ('comp adv. same')
        sql = ("UPDATE `brand_competative_dba_156` SET comp_desc_test ='" + str(s1) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    else:
        s2 = ('comp adv. not same')
        sql = ("UPDATE `brand_competative_dba_156` SET comp_desc_test ='" + str(s2) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    flag = 0
    for x in soup.find('section', class_='major-trade competitivee').find('div', class_='trade-inner').find_all('h3'):
        trade = x.text
        # print(trade)
        # print('---')
        # print(heading)
        if trade.strip() == heading.strip():
            flag = 1
            break
    if flag == 1:
        s3=('comp header same')
        sql = ("UPDATE `brand_competative_dba_156` SET comp_heading_test ='" + str(s3) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    else:
        s4 = ('comp header not same')
        sql = ("UPDATE `brand_competative_dba_156` SET comp_heading_test ='" + str(s4) + "' WHERE   id='" + str(
            id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")