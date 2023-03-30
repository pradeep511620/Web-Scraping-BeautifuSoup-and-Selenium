from bs4 import BeautifulSoup
import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="TESTING"
)
cur = mydb.cursor()
cur.execute("SELECT url,h1_tag,meta_title,meta_desc,id FROM slug_url_apr_l3 where id>56")
myresult = cur.fetchall()
for fetch in myresult:
    mother_url = "https://s5.raptorsupplies.com.sg/" + fetch[0]
    title_name = fetch[1]
    meta_title = fetch[2]
    meta_desc = fetch[3]
    id = fetch[4]
    page = requests.get(mother_url)
    soup = BeautifulSoup(page.content, "html.parser")
    for x in soup.find_all('h1', class_='category_l2_title category_l3_title'):
        y = x.text
        title = title_name
        # print(y)
        # print(title)
        if y.strip() == title.strip():
            par = ('same')
            sql = ("UPDATE slug_url_apr_l3 SET h1_tag_test ='" + str(par) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:

            par1 = 'not same'
            sql = ("UPDATE slug_url_apr_l3 SET h1_tag_test ='" + str(par1) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        for tag in soup.find_all("title")[0]:
            # title1 = tag.split('')
            # title2 = "".join(title1)
            tit = tag.text
            meta = meta_title + " Singapore"

            if tit.strip() == meta.strip():
                par2 = ('same')
                sql = ("UPDATE slug_url_apr_l3 SET meta_title_test ='" + str(par2) + "' WHERE   id='" + str(id) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                par3 = ('not same')
                sql = ("UPDATE slug_url_apr_l3 SET meta_title_test ='" + str(par3) + "' WHERE   id='" + str(id) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
                print(tit)
                print(meta)
            if meta_desc != '':
                for meta_d in soup.find_all('meta', attrs={'name': 'description'}):
                    meta = (meta_d.get('content'))
                    if meta.strip() == meta_desc.strip():
                        de = 'meta_desc same'
                        sql = ("UPDATE slug_url_apr_l3 SET meta_desc_test ='" + str(de) + "' WHERE   id='" + str(
                            id) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                    else:
                        de1 = 'meta_desc not same'
                        sql = ("UPDATE slug_url_apr_l3 SET meta_desc_test ='" + str(de1) + "' WHERE   id='" + str(
                            id) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
            else:
                de2 = 'meta_desc blank is db'
                sql = ("UPDATE slug_url_apr_l3 SET meta_desc_test ='" + str(de2) + "' WHERE   id='" + str(
                    id) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
