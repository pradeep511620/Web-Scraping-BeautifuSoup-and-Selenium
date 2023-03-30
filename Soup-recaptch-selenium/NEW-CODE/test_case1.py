import mysql.connector
import requests
from bs4 import BeautifulSoup
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='raptor_staging'
)
cur=mydb.cursor()
cur.execute('select brand_url,description,meta_title,meta_description from new_brand_desc ')
myresult=cur.fetchall()
for fetch in myresult:
    brand_url=fetch[0]
    description=fetch[1]
    meta_title=fetch[2]
    meta_desc=fetch[3]
    page=requests.get(brand_url)
    soup=BeautifulSoup(page.content,'lxml')
    for desc in soup.find('div',class_='paddin').find_all('p'):
        d=(desc.text)
        d1=d.split('\n')
        d2=" ".join(d1)
        t=description.replace('<br>',' ')
        t1 = t.split('\n')
        t2 = "".join(t1)
        if(d2.split()==t2.split()):
            desc1=('desc is same')
            sql = ("UPDATE new_brand_desc  SET desc_test ='" + str(desc1) + "' WHERE   brand_url='" + str(brand_url) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            desc2=('desc is not same')
            sql = ("UPDATE new_brand_desc  SET desc_test ='" + str(desc2) + "' WHERE   brand_url='" + str(
                brand_url) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
            print(t2)
            print(d2)
        for title in soup.find_all('title'):
            tit=(title.text)
            if(tit==meta_title):
                tit1=('meta_title same')
                sql = ("UPDATE new_brand_desc  SET meta_title_test ='" + str(tit1) + "' WHERE   brand_url='" + str(
                    brand_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                tit2=('meta_title not same')
                sql = ("UPDATE new_brand_desc  SET meta_title_test ='" + str(tit2) + "' WHERE   brand_url='" + str(
                    brand_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")

            for meta_d in soup.find_all('meta',attrs={'name':'description'}):
                meta=(meta_d.get('content'))
                if(meta==meta_desc):
                    mt_desc1="meta desc is same"
                    sql = ("UPDATE new_brand_desc  SET meta_desc_test ='" + str(mt_desc1) + "' WHERE   brand_url='" + str(
                        brand_url) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
                else:
                    mt_desc2 = "meta desc is same"
                    sql = ("UPDATE new_brand_desc  SET meta_desc_test ='" + str(mt_desc2) + "' WHERE   brand_url='" + str(
                        brand_url) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
