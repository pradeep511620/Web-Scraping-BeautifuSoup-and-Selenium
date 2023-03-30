
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
cur.execute('select url,heading,description,id from `brand_trade_dba_156` where trade_desc_test="trade desc not same" ')
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
    for x in soup.find('div', class_='trade-inner').find_all('p'):
        trade = x.text
        trade1 = trade.replace('...Read More', '').replace('...','')
        print(trade1)
        print(description)
        if trade1.strip() == description.strip():
            flag = 1
            break
    if flag == 1:
        s1 = ('trade desc same')
        sql = ("UPDATE `brand_trade_dba_156` SET trade_desc_test ='" + str(s1) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    else:
        s2 = ('trade desc not same')
        sql = ("UPDATE `brand_trade_dba_156` SET trade_desc_test ='" + str(s2) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    """flag = 0
    for x in soup.find('div', class_='trade-inner').find_all('h3'):
        trade = x.text
        if trade.strip() == heading.strip():
            flag = 1
            break
    if flag == 1:
        s3=('trade header same')
        sql = ("UPDATE `brand_trade_dba_156` SET trade_heading_test ='" + str(s3) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    else:
        s4 = ('trade header not same')
        sql = ("UPDATE `brand_trade_dba_156` SET trade_heading_test ='" + str(s4) + "' WHERE   id='" + str(
            id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")"""
