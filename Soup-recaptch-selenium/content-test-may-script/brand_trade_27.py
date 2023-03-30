
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
cur.execute('select brand_url,heading,description,id from `brand_trade_27_dba16` where trade_desc_test is null ')
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
    for x in soup.find('div', class_='majorTradeNames').find_all('p'):
        trade = x.text
        trade1 = trade.replace('...Read More', '')
        if trade1.strip() == description.strip():
            flag = 1
            break
    if flag == 1:
        s1 = ('trade desc same')
        sql = ("UPDATE `brand_trade_27_dba16` SET trade_desc_test ='" + str(s1) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    else:
        s2 = ('trade desc not same')
        sql = ("UPDATE `brand_trade_27_dba16` SET trade_desc_test ='" + str(s2) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    flag = 0
    for x in soup.find('div', class_='majorTradeNames').find_all('h4'):
        trade = x.text
        if trade.strip() == heading.strip():
            flag = 1
            break
    if flag == 1:
        s3=('trade header same')
        sql = ("UPDATE `brand_trade_27_dba16` SET trade_heading_test ='" + str(s3) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    else:
        s4 = ('trade header not same')
        sql = ("UPDATE `brand_trade_27_dba16` SET trade_heading_test ='" + str(s4) + "' WHERE   id='" + str(
            id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")




"""
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
cur.execute('select brand_url,cross_ref,why_us,shipping,id from brand_content_trade_27_dba_16 where cross_ref_test = "cross ref not same" ')
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    # description = fetch[1]
    # short_desc = fetch[2]
    # meta_desc = fetch[3]
    cross_ref = fetch[1]
    why_us = fetch[2]
    shipping = fetch[3]
    id = fetch[4]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    flag = 0

    a = 0
    for pd in soup.find("div", class_='consider').find_all('p', class_='tr1'):
        pr = str(pd).replace('<p class="tr1">', '').replace('</p>', '')
        pro = html.unescape(pr)
        a += 1
        if a == 1:
            cross_re = cross_ref
            # print(cross_re)
            # print(pro)
            if cross_re.strip() == pro.strip():
                cr = 'cross reef same'
                sql = ("UPDATE brand_content_trade_27_dba_16 SET cross_ref_test ='" + str(
                    cr) + "' WHERE   id='" + str(
                    id) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                cr1 = 'cross ref not same'
                sql = ("UPDATE brand_content_trade_27_dba_16 SET cross_ref_test ='" + str(
                    cr1) + "' WHERE   id='" + str(
                    id) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
        elif a == 2:
            why_us1 = why_us
            if why_us1.strip() == pro.strip():
                wu = 'why us same'
                sql = ("UPDATE brand_content_trade_27_dba_16 SET why_us_test ='" + str(
                    wu) + "' WHERE   id='" + str(
                    id) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                wu1 = 'why us not same'
                sql = ("UPDATE brand_content_trade_27_dba_16 SET why_us_test ='" + str(
                    wu1) + "' WHERE   id='" + str(
                    id) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
        elif a == 3:
            shipping1 = shipping
            if shipping1.strip() == pro.strip():
                sh = 'shipping same'
                sql = ("UPDATE brand_content_trade_27_dba_16 SET shipping_test ='" + str(
                    sh) + "' WHERE   id='" + str(
                    id) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                sh1 = 'shipping not same'
                sql = ("UPDATE brand_content_trade_27_dba_16 SET shipping_test ='" + str(
                    sh1) + "' WHERE   id='" + str(
                    id) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")



"""