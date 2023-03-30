import html

import mysql.connector
import requests
from bs4 import BeautifulSoup

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='new_stage_data'
)
cur = mydb.cursor()
cur.execute(
    'select product_url,uses,feature,com_acess,standard,installation from `destaco_new_content_1377` where com_acess !=" " ')
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    uses = fetch[1]
    feature = fetch[2]
    compatible = fetch[3]
    standard = fetch[4]
    installation = fetch[5]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    a = 0
    for desc in soup.find('div', class_='product-description').find_all('p'):
        a += 1
        if (a == 2):
            s = str(desc)
            use = s
            use1 = html.unescape(use)

            s1 = uses.split('\n')
            s2 = ''.join(s1)
            if (s2 == use1):
                u = ('uses content is same')
                sql = ("UPDATE `destaco_new_content_1377`  SET uses_test ='" + str(u) + "' WHERE   product_url='" + str(
                    product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                u1 = ('uses content not same')
                sql = ("UPDATE `destaco_new_content_1377`  SET uses_test ='" + str(
                    u1) + "' WHERE   product_url='" + str(
                    product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            a = 0
            for desc in soup.find('div', class_='product-description').find_all('ul'):
                a += 1
                if (a == 1):
                    s = str(desc)

                    fet = (s[4:-5])
                    fet1 = html.unescape(fet)
                    fet2 = fet1.split('\n')
                    fet3 = ''.join(fet2)
                    s1 = feature.split('\n')
                    s2 = ''.join(s1)
                    if s2 == fet3:
                        ft1 = ('feature content is same')
                        sql = ("UPDATE `destaco_new_content_1377`  SET feature_test ='" + str(
                            ft1) + "' WHERE   product_url='" + str(
                            product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                    else:
                        ft2 = ('feature content is not same')
                        sql = ("UPDATE `destaco_new_content_1377`  SET feature_test ='" + str(
                            ft2) + "' WHERE  product_url='" + str(
                            product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                        # print(fet)
                        # print(s2)
                elif (a == 2):
                    s = str(desc)
                    comp = (s[4:-5])
                    comp1 = html.unescape(comp)
                    comp2 = comp1.split('\n')
                    comp3 = ''.join(comp2)
                    s1 = compatible.split('\n')
                    s2 = ''.join(s1)
                    if s2 == comp3:
                        com1 = ('compatible content is same')
                        sql = ("UPDATE `destaco_new_content_1377`  SET comp_test ='" + str(
                            com1) + "' WHERE  product_url='" + str(
                            product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")

                    else:
                        com2 = ('compatible content is not same')
                        sql = ("UPDATE `destaco_new_content_1377`  SET comp_test ='" + str(
                            com2) + "' WHERE  product_url='" + str(
                            product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")

                elif a == 3:
                    s = str(desc)
                    s4 = html.unescape(s)
                    sta = (s4[4:-5])
                    sta1 = sta.split('\n')
                    sta2 = ''.join(sta1)
                    s1 = standard.split('\n')
                    s2 = ''.join(s1)

                    if s2 == sta:
                        sta1 = ('standard content is same')
                        sql = ("UPDATE `destaco_new_content_1377`  SET standard_test ='" + str(sta1) + "' WHERE   product_url='" + str(
                            product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                    else:
                        sta2 = ('standard content is not same')
                        sql = ("UPDATE `destaco_new_content_1377`  SET standard_test ='" + str(sta2) + "' WHERE   product_url='" + str(
                            product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")

                elif (a == 4):
                    s = str(desc)
                    s4=s.replace('amp;', '')
                    insta= (s4[4:-5])
                    s1 = installation.split('\n')
                    s2 = ''.join(s1)

                    if (s2 == insta):
                        insta1=('installation content is same')
                        sql = ("UPDATE `destaco_new_content_1377`  SET installation_test ='" + str(insta1) + "' WHERE   product_url='" + str(
                            product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                    else:
                        insta2=('installation content is not same')
                        sql = ("UPDATE `destaco_new_content_1377`  SET installation_test ='" + str(
                            insta2) + "' WHERE   product_url='" + str(
                            product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
