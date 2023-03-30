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
cur.execute("SELECT mother_url,h1_tag,meta_title,id FROM `slug_url_apr` ")
myresult = cur.fetchall()
for fetch in myresult:
    mother_url = "https://b2b.raptorsupplies.com/" + fetch[0]
    title_name = fetch[1]
    meta_title = fetch[2]

    id = fetch[3]
    page = requests.get(mother_url)
    soup = BeautifulSoup(page.content, "html.parser")
    for x in soup.find_all('h1',id='motherTitle'):
        y = x.text
        title = title_name
        # print(y)
        # print(title)
        if y.strip() == title.strip():
            par=('same')
            sql = ("UPDATE `slug_url_apr` SET title_test ='" + str(par) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:

            par1 =('not same')
            sql = ("UPDATE `slug_url_apr` SET title_test ='" + str(par1) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        for tag in soup.find_all("title")[0]:
            # title1 = tag.split('')
            # title2 = "".join(title1)
            tit = tag.text
            meta = meta_title


            if tit.strip() == meta.strip():
                par2= ('same')
                sql = ("UPDATE `slug_url_apr` SET tag_test ='" + str(par2) + "' WHERE   id='" + str(id) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                par3 = ('not same')
                sql = ("UPDATE `slug_url_apr` SET tag_test ='" + str(par3) + "' WHERE   id='" + str(id) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
                print(tit)
                print(meta)
