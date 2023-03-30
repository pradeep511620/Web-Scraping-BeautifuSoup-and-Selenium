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
# cur.execute('select product_url,question,answer,id from pd_content_faq_dba_118 where faq_test1 = "Answer not same"  ')
cur.execute('select product_url,question,answer,id from pd_content_faq_dba_118 where faq_test1 ="Answer not same" and id>2   ')

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
    for attr in soup.find("section", class_="specification").find_all('h3'):
        s = str(attr.text)

        q = question[3:]
        # print(s)
        # print(q)
        if s.strip() == q.strip():

            flag = 2
            label = attr.text
    if flag == 2:
        s2 = 'Question same'
        sql = ("UPDATE pd_content_faq_dba_118 SET faq_test ='" + str(s2) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    else:
        s3 = 'Question not same'
        sql = ("UPDATE pd_content_faq_dba_118 SET faq_test ='" + str(s3) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    questionAns = soup.find_all("div", class_="box")
    label1 = ""
    for b1 in questionAns:
        answer1 = b1.find('p')
        # print(answer1)
        for answer2 in [answer1.text.strip()]:
            # print(answer2)
            if answer2 is not '':
                h1 = str(answer2)
                x = html.unescape(h1)
                ans = answer[3:]
                # print(ans)
                # print(x)
                if x.strip() == ans.strip():
                    flag = 1
                    label1 = x
            else:
                para1 = b1.find('ul')
                para2 = str(para1)[4:-5]
                x = html.unescape(para2)
                ans1 = x.split()
                ans2 = " ".join(ans1)

                p2 = str(answer)[3:]
                a1 = p2.split()
                a2 = " ".join(a1)
                a3 = a2.replace('</li> <li>', '</li><li>')

                print(ans2)
                print(a3)
                # ans = answer[3:]
                if ans2 == a3:
                    flag = 1
                    label1 = answer2

    if flag == 1:
        s4 = 'Answer same'
        sql = ("UPDATE pd_content_faq_dba_118 SET faq_test1 ='" + str(s4) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    else:
        s5 = 'Answer not same'
        sql = ("UPDATE pd_content_faq_dba_118 SET faq_test1 ='" + str(s5) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")

