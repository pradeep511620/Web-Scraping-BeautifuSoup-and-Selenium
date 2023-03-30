# live com onb test data (l3,item,parent,product_title)

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
    "SELECT mother_url,meta_desc,short_desc,id from mother_content_dba_219  where short_desc_test is null ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    meta_desc = fetch[1]
    short_desc = fetch[2]
    id = fetch[3]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    st = page.status_code
    flag = 0
    try:
        if st == 200:
            for short in soup.find("div", class_='showmorewrap').find_all('p'):
                sh: str = str(short).replace('<p><br/>', '').replace('</p>', '').replace(
                    '<span id="dots">...</span><span id="more">', '').replace(
                    '<a href="javascript:void(0)" onclick="sortCatDesc('"'S'"')">...Read More</a>', '').replace('<p><p>',
                                                                                                                '').strip(
                    '\n').replace(' <a href="javascript:void(0)" onclick="sortCatDesc('"'L'"')">Read Less</a>','').replace('<p id="catdescFullRow" style="display:none">','')
                sh1 = html.unescape(sh)
                print(sh1)
                print('--')
                print(short_desc)
                if sh1.strip() == short_desc.strip():
                    flag = 1
                    break
            if flag == 1:
                print(flag)
                st = 'short desc same'
                sql = ("UPDATE mother_content_dba_219 SET short_desc_test ='" + str(
                    st) + "' WHERE   id='" + str(
                    id) + "'")

                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                print(flag)
                st1 = 'short desc not same'
                sql = ("UPDATE mother_content_dba_219 SET short_desc_test ='" + str(
                    st1) + "' WHERE   id='" + str(
                    id) + "'")

                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")

            """title = soup.find("meta", attrs={'name': 'description'})
            meta = (title["content"] if title else "No meta title given")
            # print(meta)
            # print(meta_desc)
            if meta.strip() == meta_desc.strip():
                d1 = ('desc same')
                sql = ("UPDATE mother_content_dba_219 SET meta_desc_test ='" + str(
                    d1) + "' WHERE   id='" + str(
                    id) + "'")
        
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                d1 = ('desc not same')
                sql = ("UPDATE mother_content_dba_219 SET meta_desc_test ='" + str(
                    d1) + "' WHERE   id='" + str(
                    id) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")"""
        else:
            print('404')
    except:
        pass
