
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
cur.execute('select product_url,question,answer,id from `faq_DBA2022_11` where id>164 ')
myresult = cur.fetchall()
for fetch in myresult:
    mother_url = fetch[0]
    ques= fetch[1]
    answer = fetch[2]
    id = fetch[3]
    page = requests.get(mother_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    a = 0
    loc = 0
    label = ""
    flag = 0
    val = ''
    for attr in soup.find("div", class_="mother_faq").find_all("h3"):
        se = str(attr.text)
        s1 = se.split()
        s = " ".join(s1)
        question = ques[3:]


        if s.lower().strip() == question.lower().strip():
            flag = 2
            label = attr.text

    if flag == 2:
        s2 = ('Question same')
        sql = ("UPDATE `faq_DBA2022_11` SET faq_test ='" + str(s2) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    else:
        s3 = ('Question not same')
        sql = ("UPDATE `faq_DBA2022_11` SET faq_test ='" + str(s3) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    label1 = ""
    for attr1 in soup.find("div", class_="mother_faq").find_all("p"):
        z = str(attr1)[3:-4]
        x = html.unescape(z)
        x1 = x.replace('<br/>', "<br>")
        x2 = x1.split()
        x3 = " ".join(x2)
        ans = answer[3:]
        ans1 = ans.split()
        ans2 = " ".join(ans1)
        # print(ans2)
        # print(x3)
        if x3 == ans2:
            flag = 1
            label1 = x
    if flag == 1:
        s4 = ('Answer same')
        sql = ("UPDATE `faq_DBA2022_11` SET faq_test1 ='" + str(s4) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    else:
        s5 = ('Answer not same')
        sql = ("UPDATE `faq_DBA2022_11` SET faq_test1 ='" + str(s5) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        print(label1)
        print(answer)


