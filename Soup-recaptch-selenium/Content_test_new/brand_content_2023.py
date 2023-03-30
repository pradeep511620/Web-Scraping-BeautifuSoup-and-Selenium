
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
cur.execute('select url,description,short_desc,meta_desc,cross_ref,why_us,shipping,id from brand_content_dba_156  ')
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    description = fetch[1]
    short_desc = fetch[2]
    meta_desc = fetch[3]
    cross_ref = fetch[4]
    why_us = fetch[5]
    shipping = fetch[6]
    id = fetch[7]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    flag = 0
    for pd in soup.find("section", class_='about-brand').find_all('p'):
        pro = str(pd).replace('<p>','').replace("</p>",'')
        pro1 = html.unescape(pro)

        if pro1.strip() == description.strip():
            mt_desc2 = 'brand desc same'
            sql = ("UPDATE brand_content_dba_156 SET brand_desc_test ='" + str(
                mt_desc2) + "' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)

        else:
            mt_desc = 'brand desc not same'
            sql = ("UPDATE brand_content_dba_156 SET brand_desc_test ='" + str(
                mt_desc) + "' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)

        title = soup.find("meta", attrs={'name': 'description'})
        meta = (title["content"] if title else "No meta title given")
        if meta == meta_desc:
            st1 = 'meta desc same'
            sql = ("UPDATE brand_content_dba_156 SET meta_desc_test ='" + str(
                st1) + "' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)

        else:
            st2 = 'meta desc not same'
            sql = ("UPDATE brand_content_dba_156 SET meta_desc_test ='" + str(
                st2) + "' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)
        values = soup.find("div", class_='consider-inner d-flex').find_all('h3')
        values1 = soup.find("div", class_='consider-inner d-flex').find_all('p',class_='tr1')
        for x,y in zip(values,values1):
            heading = x.text
            par = str(y).replace('<p class="tr1">','').replace('</p>', '')
            para = html.unescape(par)
            cross_ref=cross_ref.replace('’',"'")
            if heading == 'Cross-Reference Alternatives' :
                if para.strip() == cross_ref.strip():
                    cr = "content same"
                    sql = ("UPDATE brand_content_dba_156 SET cross_ref_test ='" + str(
                        cr) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                else:
                    cr1 = "content not same"
                    sql = ("UPDATE brand_content_dba_156 SET cross_ref_test ='" + str(
                        cr1) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
            if heading == 'Why Us?':
                print(why_us)
                print('--')
                print(para)
                if para.strip() == why_us.strip():
                    wu = "content same"
                    sql = ("UPDATE brand_content_dba_156 SET why_us_test ='" + str(
                        wu) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                else:
                    wu1 = "content not same"
                    sql = ("UPDATE brand_content_dba_156 SET why_us_test ='" + str(
                        wu1) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
            if heading == 'Shipping':
                if para.strip() == shipping.strip():
                    sh = "content same"
                    sql = ("UPDATE brand_content_dba_156 SET shipping_test ='" + str(
                        sh) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                else:
                    sh1 = "content not same"
                    sql = ("UPDATE brand_content_dba_156 SET shipping_test ='" + str(
                        sh1) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)

    mydb.commit()
    print(cur.rowcount, "records successful Done")

