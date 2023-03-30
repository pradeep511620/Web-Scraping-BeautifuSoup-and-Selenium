
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
b=' where faq_test1 ="Answer not same"'
cur.execute('select mother_url,question,answer,id from `mother_faq_dba_219` where faq_test1 ="Answer not same"')
myresult = cur.fetchall()
for fetch in myresult:
    mother_url = fetch[0]
    ques= fetch[1]
    answer = fetch[2]
    id = fetch[3]
    page = requests.get(mother_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        a = 0
        loc = 0
        label = ""
        flag = 0
        val = ''
        """for attr in soup.find("div", class_="mother_faq").find_all("h3"):
            se = str(attr.text)
            s1 = se.split()
            s = " ".join(s1)
            question = ques[3:]


            if s.lower().strip() == question.lower().strip():
                flag = 2
                label = attr.text

        if flag == 2:
            s2 = ('Question same')
            sql = ("UPDATE `mother_faq_dba_219` SET faq_test ='" + str(s2) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            s3 = ('Question not same')
            sql = ("UPDATE `mother_faq_dba_219` SET faq_test ='" + str(s3) + "' WHERE   id='" + str(id) + "'")
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
            print(ans2)
            print('--')
            print(x3)
            if x3 == ans2:
                flag = 1
                label1 = x
        if flag == 1:
            s4 = ('Answer same')
            sql = ("UPDATE `mother_faq_dba_219` SET faq_test1 ='" + str(s4) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            s5 = ('Answer not same')
            sql = ("UPDATE `mother_faq_dba_219` SET faq_test1 ='" + str(s5) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
            # print(label1)
            # print(answer)"""
        label1 = ""
        flag = 0
        for attr1 in soup.find("div", class_="mother_faq").find_all("ul"):
            z = attr1

            h1 = str(z)[4:-5]
            x = html.unescape(h1)
            y = x.split()
            z = " ".join(y)
            # print(z)
            ans = answer[3:]
            ans1 = ans.split()
            ans2 = " ".join(ans1)
            ans3 = ans2
            print(z)
            print(ans3)
            if z.strip() == ans3.strip():
                flag = 1
                label1 = x
        if flag == 1:
            s2 = ('Answer same')
            sql = ("UPDATE `mother_faq_dba_219` SET faq_test1 ='" + str(s2) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            s3 = "Answer not same"
            sql = ("UPDATE `mother_faq_dba_219` SET faq_test1 ='" + str(s3) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
                       
    except:
        pass
""" label1 = ""
                        # flag = 0
                        for attr1 in soup.find("div", class_="mother_faq").find_all("ul"):
                            z = attr1

                            h1 = str(z)[4:-5]
                            x = html.unescape(h1)
                            y = x.split()
                            z = " ".join(y)
                            # print(z)
                            ans = answer[3:]
                            ans1 = ans.split()
                            ans2 = " ".join(ans1)
                            ans3 = ans2
                            print(z)
                            print(ans3)
                            if z.strip() == ans3.strip():
                                flag = 1
                                label1 = x
                        if flag == 1:
                            s2 = ('Answer same')
                            sql = ("UPDATE `mother_faq_dba_219` SET faq_test1 ='" + str(s2) + "' WHERE   id='" + str(id) + "'")
                            cur.execute(sql)
                            mydb.commit()
                            print(cur.rowcount, "records successful Done")
                        else:
                            s3 = "Answer not same"
                            sql = ("UPDATE `mother_faq_dba_219` SET faq_test1 ='" + str(s3) + "' WHERE   id='" + str(id) + "'")
                            cur.execute(sql)
                            mydb.commit()
                            print(cur.rowcount, "records successful Done")"""



