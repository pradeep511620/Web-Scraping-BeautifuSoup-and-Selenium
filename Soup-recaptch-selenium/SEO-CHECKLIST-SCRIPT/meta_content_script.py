from bs4 import BeautifulSoup
import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="new_stage_data"
)
cur = mydb.cursor()
cur.execute("SELECT url,title_tag,description FROM `product_content_meta_1423` ")
my_result = cur.fetchall()
for fetch in my_result:
    url = fetch[0]
    tag = fetch[1]
    meta_desc =fetch[2]
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")
    for title in soup.find_all('title'):
        tit = (title.text)
        title1 =tag
        if tit == title1:
            tit1 = ('meta_title same')
            sql = ("UPDATE mother_content_may_dba16 SET meta_title_test ='" + str(
                tit1) + "' WHERE   id='" + str(
                id) + "'")

            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            tit2 = "meta title not same"
            sql = ("UPDATE mother_content_may_dba16 SET meta_title_test ='" + str(
                tit2) + "' WHERE   id='" + str(
                id) + "'")

            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        title = soup.find("meta", attrs={'name': 'description'})
        meta = (title["content"] if title else "No meta title given")

        if meta == meta_desc:
            d1 = ('desc same')
            sql = ("UPDATE mother_content_may_dba16 SET meta_desc_test ='" + str(
                d1) + "' WHERE   id='" + str(
                id) + "'")

            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            d1 = ('desc not same')
            sql = ("UPDATE mother_content_may_dba16 SET meta_desc_test ='" + str(
                d1) + "' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
