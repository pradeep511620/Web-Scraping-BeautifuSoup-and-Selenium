import html
import mysql.connector
import requests
from bs4 import BeautifulSoup
import itertools
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='new_stage_data'
)
cur = mydb.cursor()
cur.execute('select product_url,question,answer,id from `faq_1377` where faq_test is null  ')
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    question = fetch[1]
    answer = fetch[2]
    id = fetch[3]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    a = 0
    loc = 0
    label = ""
    flag = 0
    val = ''
    for attr in soup.find("div", class_="product-description").find_all("h3"):
        s = str(attr.text)
        if s == question:
            flag = 2
            label = attr.text
    if flag == 2:
        s2 = ('Question same')
        sql = ("UPDATE `faq_1377` SET faq_test ='" + str(s2) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    else:
        s3 = ('Question not same')
        sql = ("UPDATE `faq_1377` SET faq_test ='" + str(s3) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    label1 = ""
    for attr1 in soup.find("div", class_="product-description").find_all("p"):
        z = str(attr1)[3:-4]
        x = html.unescape(z)
        if x == answer:
            flag = 1
            label1 = x
    if flag == 1:
        s4 = ('Answer same')
        sql = ("UPDATE `faq_1377` SET faq_test1 ='" + str(s4) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    else:
        s5 = ('Answer not same')
        sql = ("UPDATE `faq_1377` SET faq_test1 ='" + str(s5) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        print(label1)
        print(answer)


