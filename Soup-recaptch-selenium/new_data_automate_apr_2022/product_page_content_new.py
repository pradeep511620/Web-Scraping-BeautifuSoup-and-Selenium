# live com onb test data (l3,item,parent,product_title)

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
cur.execute("SELECT product_url,description,feature,working_mech,compatible_acc,standard,id FROM "
            "product_content_check_dba11 limit 5 ")
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
    soup = BeautifulSoup(page.content, "html.parser")
    for x in soup.find_all("div",class_='product-description'):
        de = str(x).split('<h2>')[0].replace('<div class="product-description">','')
        de1 = html.unescape(de)
        if de1.strip() == description.strip():
            prod = "description same"
            sql = ("UPDATE product_content_check_dba11 SET desc_test ='" + str(prod) + "' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            prod1 = "description not same"
            sql = ("UPDATE product_content_check_dba11 SET desc_test ='" + str(prod1) + "' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")

        for x in soup.find("div", class_='productDetailsRight half-collomn').find_all('h2'):
            y = x.text
            if y == "Working Mechanism:":
                c = str(x.find_next())
                c1 = c.replace('<ul>','').replace('</ul>','').replace('<p>','').replace('</p>','')
                c2 = html.unescape(c1)
                if c2.strip() == working_mec.strip():
                    c3 = 'working mechanism same'
                    sql = ("UPDATE product_content_check_dba11 SET working_mec_test ='" + str(c3) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
                else:
                    c4 = 'working mechanism not same'
                    sql = ("UPDATE product_content_check_dba11 SET working_mec_test ='" + str(
                        c4) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
            elif y == "Features:":
                w = str(x.find_next())
                w1 = w.replace('<ul>', '').replace('</ul>', '').replace('<p>','').replace('</p>','')
                w2 = html.unescape(w1)
                if w2.strip() == feature.strip():
                    f3 = 'feature same'
                    sql = ("UPDATE product_content_check_dba11 SET feature_test ='" + str(
                        f3) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
                else:
                    f4 = 'feature not same'
                    sql = ("UPDATE product_content_check_dba11 SET feature_test ='" + str(
                        f4) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
            elif y == "Compatible Accessories:":
                co = str(x.find_next())
                co1 = co.replace('<ul>', '').replace('</ul>', '').replace('<p>','').replace('</p>','')
                co2 = html.unescape(co1)
                if co2.strip() == compatible_acc.strip():
                    com1 = 'compatible accessories same'
                    sql = ("UPDATE product_content_check_dba11 SET comp_acc_test ='" + str(
                        com1) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")

                else:
                    com2 = 'compatible accessories not same'
                    sql = ("UPDATE product_content_check_dba11 SET comp_acc_test ='" + str(
                        com2) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
            elif y == "Standards and Approvals:":
                s = str(x.find_next())
                s1 = s.replace('<ul>', '').replace('</ul>', '').replace('<p>','').replace('</p>','')
                s2 = html.unescape(s1)
                if s2.strip() == standard.strip():
                    st1 = 'standard  same'
                    sql = ("UPDATE product_content_check_dba11 SET standard_test ='" + str(
                        st1) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
                else:
                    st2 = 'standard not same'
                    sql = ("UPDATE product_content_check_dba11 SET standard_test ='" + str(
                        st2) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")



