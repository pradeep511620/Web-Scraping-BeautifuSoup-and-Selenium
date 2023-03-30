
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
cur.execute('select brand_url,Question,Answer,id from `brand_faq_27_dba16` ')
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
    for attr in soup.find("div", class_="faqWrap").find_all("h3"):
        s = str(attr.text)
        ques = question[3:]

        if s.strip() == ques.strip():
            flag = 2
            label = attr.text

    if flag == 2:
        s2 = ('Question same')
        sql = ("UPDATE `brand_faq_27_dba16` SET faq_test ='" + str(s2) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    else:
        s3 = ('Question not same')
        sql = ("UPDATE `brand_faq_27_dba16` SET faq_test ='" + str(s3) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    label1 = ""
    for attr1 in soup.find("div", class_="faqWrap").find_all("p"):
        z = str(attr1)[3:-4]
        x = html.unescape(z)
        ans = answer[3:]
        if x.strip() == ans.strip():
            flag = 1
            label1 = x
    if flag == 1:
        s4 = ('Answer same')
        sql = ("UPDATE `brand_faq_27_dba16` SET faq_test1 ='" + str(s4) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    else:
        s5 = ('Answer not same')
        sql = ("UPDATE `brand_faq_27_dba16` SET faq_test1 ='" + str(s5) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        print(label1)
        print(answer)
