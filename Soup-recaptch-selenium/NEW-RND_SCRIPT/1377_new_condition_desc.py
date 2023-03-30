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
cur.execute('select product_url,description,title_tag,meta_desc,product_title from `destaco_new_content_1377` where desc_test = "desc is not same"  ')
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    description = fetch[1]
    meta_title = fetch[2]
    meta_desc = fetch[3]
    pd_title = fetch[4]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    s = []
    for desc in soup.find('div', class_='product-description').find_all('p')[0]:
        d = str(desc)
        s.append(d)
    z = (s)
    listToStr = ''.join([str(elem) for elem in z])
    st = (listToStr.replace('<br/> ',"<br>"))
    st1 = (description[3:-4])
    st2 = st1.split('\n')
    st3 = "".join(st2)
    if (st) == st3:
        desc1 = ('desc is same')
        sql = ("UPDATE `destaco_new_content_1377` SET desc_test ='" + str(desc1) + "' WHERE   product_url='" + str(
            product_url) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    else:
        desc2 = ('desc is not same')
        sql = ("UPDATE `destaco_new_content_1377` SET desc_test ='" + str(desc2) + "' WHERE   product_url='" + str(
            product_url) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
        print(st)
        print(st3)