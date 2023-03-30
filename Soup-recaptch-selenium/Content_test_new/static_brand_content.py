
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
cur.execute('select brand_url,description,title_tag,meta_desc,id from `dba_188_static_b`  ')
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    description = fetch[1]
    meta_title = fetch[2]
    meta_desc = fetch[3]
    id = fetch[4]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("meta", attrs={'name': 'description'})
    meta = (title["content"] if title else "No meta title given")
    if meta == meta_desc:
        st1 = 'meta desc same'
        # print(st1)
        sql = ("UPDATE `dba_188_static_b` SET meta_desc_test ='" + str(
            st1) + "' WHERE   id='" + str(
            id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    else:
        st2 = 'meta desc not same'
        sql = ("UPDATE `dba_188_static_b` SET meta_desc_test ='" + str(
            st2) + "' WHERE   id='" + str(
            id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    flag = 0
    for pd in soup.find("div", class_='lets-talk').find_all('p')[0:1]:
        pro = str(pd).replace('<p>','').replace("</p>",'').replace('<br/>','<br>')
        pro1 = html.unescape(pro)
        # print(pro1)
        # print(description)

        if pro1.strip() == description.strip():
            mt_desc2 = 'brand desc same'
            sql = ("UPDATE `dba_188_static_b` SET brand_desc_test ='" + str(
                mt_desc2) + "' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            mt_desc = 'brand desc not same'
            sql = ("UPDATE `dba_188_static_b` SET brand_desc_test ='" + str(
                mt_desc) + "' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
