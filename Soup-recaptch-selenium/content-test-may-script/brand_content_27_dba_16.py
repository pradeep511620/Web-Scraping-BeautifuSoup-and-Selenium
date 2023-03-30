
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
cur.execute('select brand_url,brand_desc,short_desc,meta_desc,id from `brand_content_27_dba16` where id>28 and  meta_desc_test is null ')
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    description = fetch[1]
    short_desc = fetch[2]
    meta_desc = fetch[3]
    # cross_ref = fetch[4]
    # why_us = fetch[5]
    # shipping = fetch[6]
    id = fetch[4]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    flag = 0

    for desc in soup.find('p', class_='about-the-brand'):

        d = str(desc).replace('<a href="#more_about_brand">Read More</a>','')
        d1 = d.split('\n')
        d2 = " ".join(d1)
        t = short_desc
        t1 = t.split('\n')
        t2 = "".join(t1)
        if t2.strip() == d2.strip():
            flag = 1
            break
    if flag == 1:
        short1 = 'short desc same'
        sql = ("UPDATE `brand_content_27_dba16` SET short_desc_test ='" + str(short1) + "' WHERE   id='" + str(
            id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    else:
        short2 = 'short desc not same'
        sql = ("UPDATE `brand_content_27_dba16` SET short_desc_test ='" + str(short2) + "' WHERE   id='" + str(
            id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")

    for pd in soup.find("div", class_='brand-description-col brandGap').find_all('p'):
        pro = str(pd).replace('<p>','').replace('</p>','').replace('<p id="">','').replace('<br/>','<br>')
        pro1 = html.unescape(pro)
        # print(pro1)
        # print(description)

        if pro1.strip() == description.strip():
            mt_desc2 = 'brand desc same'
            sql = ("UPDATE `brand_content_27_dba16` SET brand_desc_test ='" + str(
                mt_desc2) + "' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            mt_desc = 'brand desc not same'
            sql = ("UPDATE `brand_content_27_dba16` SET brand_desc_test ='" + str(
                mt_desc) + "' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        title = soup.find("meta", attrs={'name': 'description'})
        meta = (title["content"] if title else "No meta title given")
        if meta == meta_desc:
            st1 = 'meta desc same'
            sql = ("UPDATE `brand_content_27_dba16` SET meta_desc_test ='" + str(
                st1) + "' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")

        else:
            st2 = 'meta desc not same'
            sql = ("UPDATE `brand_content_27_dba16` SET meta_desc_test ='" + str(
                st2) + "' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        """a = 0
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
                    sql = ("UPDATE `brand_content_27_dba16` SET cross_ref_test ='" + str(
                        cr) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
                else:
                    cr1 = 'cross ref not same'
                    sql = ("UPDATE `brand_content_27_dba16` SET cross_ref_test ='" + str(
                        cr1) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
            elif a == 2:
                why_us1 = why_us
                if why_us1.strip() == pro.strip():
                    wu = 'why us same'
                    sql = ("UPDATE `brand_content_27_dba16` SET why_us_test ='" + str(
                        wu) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
                else:
                    wu1 = 'why us not same'
                    sql = ("UPDATE `brand_content_27_dba16` SET why_us_test ='" + str(
                        wu1) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
            elif a == 3:
                shipping1 = shipping
                if shipping1.strip() == pro.strip():
                    sh = 'shipping same'
                    sql = ("UPDATE `brand_content_27_dba16` SET shipping_test ='" + str(
                        sh) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
                else:
                    sh1 = 'shipping not same'
                    sql = ("UPDATE `brand_content_27_dba16` SET shipping_test ='" + str(
                        sh1) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")"""



