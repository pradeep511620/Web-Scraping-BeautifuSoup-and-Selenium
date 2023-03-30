# live com onb test data (l3,item,parent,product_title)
import time

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
cur.execute(
    "SELECT mother_url,short_desc,feature,working_mec,desc_asc,standard,id FROM mother_content_dba_219 where id>44 ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    description = fetch[1]
    feature = fetch[2]
    working_mec = fetch[3]
    compatible_acc = fetch[4]
    standard = fetch[5]
    id = fetch[6]
    page = requests.get(product_url)
    st = (page.status_code)
    try:
        if st == 200:
            soup = BeautifulSoup(page.content, "html.parser")
            if soup.find("div", class_='mother_newsection').find_all('h4'):
                for x in soup.find("div", class_='mother_newsection').find_all('h4'):
                    y = x.text
                    print(y)
                    if y == "Working Mechanism":
                        c = str(x.find_next())
                        c1 = c.replace('<ul>', '').replace('</ul>', '').replace('<p>', '').replace('</p>', '').replace(
                            "</li> <li>", '</li><li>')
                        c2 = html.unescape(c1)
                        working_mec = working_mec.replace('</li> ', '</li>')
                        # print(c2)
                        # print('--')
                        # print(working_mec)
                        if c2.strip() == working_mec.strip():
                            c3 = 'working mechanism same'
                            sql = ("UPDATE mother_content_dba_219 SET working_mec_test ='" + str(
                                c3) + "' WHERE   id='" + str(
                                id) + "'")
                            cur.execute(sql)
                            mydb.commit()
                            print(cur.rowcount, "records successful Done in db")
                        else:
                            c4 = 'working mechanism not same'
                            sql = ("UPDATE mother_content_dba_219 SET working_mec_test ='" + str(
                                c4) + "' WHERE   id='" + str(
                                id) + "'")
                            cur.execute(sql)
                            mydb.commit()
                            print(cur.rowcount, "records successful Done")

                    elif y == "Features":
                        w = str(x.find_next())
                        w1 = w.replace('<ul>', '').replace('</ul>', '').replace('<p>', '').replace('</p>', '').replace(
                            "</li> <li>", '</li><li>').replace('</li></li>', "</li>")
                        w2 = html.unescape(w1)
                        feature = feature.replace('</li> ', '</li>')
                        # print(w2)
                        # print('----')
                        # print(feature)
                        if w2.strip() == feature.strip():
                            f3 = 'feature same'
                            sql = ("UPDATE mother_content_dba_219 SET feature_test ='" + str(
                                f3) + "' WHERE   id='" + str(
                                id) + "'")
                            cur.execute(sql)
                            mydb.commit()
                            print(cur.rowcount, "records successful Done")
                        else:
                            f4 = 'feature not same'
                            sql = ("UPDATE mother_content_dba_219 SET feature_test ='" + str(
                                f4) + "' WHERE   id='" + str(
                                id) + "'")
                            cur.execute(sql)
                            mydb.commit()
                            print(cur.rowcount, "records successful Done")
                            # print(w2)
                            # print(feature)
                    elif y == "Compatible Accessories":
                        co = str(x.find_next())
                        co1 = co.replace('<ul>', '').replace('</ul>', '').replace('<p>','').replace('</p>','').replace("</li> <li>", '</li><li>')
                        co2 = html.unescape(co1)
                        # print(co2)
                        # print('---')
                        # print(compatible_acc)
                        if co2.strip() == compatible_acc.strip():
                            com1 = 'compatible accessories same'
                            sql = ("UPDATE mother_content_dba_219 SET comp_acc_test ='" + str(
                                com1) + "' WHERE   id='" + str(
                                id) + "'")
                            cur.execute(sql)
                            mydb.commit()
                            print(cur.rowcount, "records successful Done")

                        else:
                            com2 = 'compatible accessories not same'
                            sql = ("UPDATE mother_content_dba_219 SET comp_acc_test ='" + str(
                                com2) + "' WHERE   id='" + str(
                                id) + "'")
                            cur.execute(sql)
                            mydb.commit()
                            print(cur.rowcount, "records successful Done")
                    elif y == "Standards and Approvals":
                        s = str(x.find_next())

                        s1 = s.replace('<ul>', '').replace('</ul>', '')
                        s2 = html.unescape(s1)
                        if s2.strip() == standard.strip():
                            st1 = 'standard  same'
                            sql = ("UPDATE mother_content_dba_219 SET standard_test ='" + str(
                                st1) + "' WHERE   id='" + str(
                                id) + "'")
                            cur.execute(sql)
                            mydb.commit()
                            print(cur.rowcount, "records successful Done")
                        else:
                            st2 = 'standard not same'
                            sql = ("UPDATE mother_content_dba_219 SET standard_test ='" + str(
                                st2) + "' WHERE   id='" + str(
                                id) + "'")
                            cur.execute(sql)
                            mydb.commit()
                            print(cur.rowcount, "records successful Done")
            else:
                print('not find')
        else:
            print("404", product_url)
    except:
        pass