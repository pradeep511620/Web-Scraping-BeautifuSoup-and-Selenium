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
cur.execute('select mother_url,mother_desc,title_tag,meta_desc,mg_title from `mother_content_1377` where meta_title_test ="meta_title not same" ')
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    description = fetch[1]
    meta_title = fetch[2]
    meta_desc = fetch[3]
    pd_title = fetch[4]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for desc in soup.find('div', class_='mothernew1').find_all('p')[0]:
        d = str(desc)
        d1 = d.split('\n')
        d2 = " ".join(d1)
        t = description
        t1 = t.split('\n')
        t2 = "".join(t1)
        if (d2.split() == t2.split()):
            desc1 = ('desc is same')
            sql = ("UPDATE `mother_content_1377` SET desc_test ='" + str(desc1) + "' WHERE   mother_url='" + str(
                product_url) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            desc2 = ('desc is not same')
            sql = ("UPDATE `mother_content_1377` SET desc_test ='" + str(desc2) + "' WHERE   mother_url='" + str(
                product_url) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
            print(t2)
            print(d2)
        for title in soup.find_all('title'):
            tit = (title.text)
            title1 = meta_title + ' | Raptor Supplies'
            if tit.lower().split() == title1.lower().split():
                tit1 = ('meta_title same')

                sql = ("UPDATE `mother_content_1377` SET meta_title_test ='" + str(
                    tit1) + "' WHERE   mother_url='" + str(
                    product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                tit2 = ('meta_title not same')
                sql = ("UPDATE `mother_content_1377` SET meta_title_test ='" + str(
                    tit2) + "' WHERE   mother_url='" + str(
                    product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
                print(tit)
                print(title1)

            for meta_d in soup.find_all('meta', attrs={'name': 'description'}):
                meta = (meta_d.get('content'))
                meta_des = meta_desc + " - Pay in EUR/USD | Delivery across Europe, Middle East, Africa / SE Asia | +44 203 287 5224 | sales@raptorsupplies.com"
                if (meta == meta_des):
                    mt_desc1 = ("meta desc is same")
                    sql = ("UPDATE `mother_content_1377`SET meta_desc_test ='" + str(
                        mt_desc1) + "' WHERE   mother_url='" + str(
                        product_url) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
                else:
                    mt_desc2 = "meta desc is same"
                    sql = ("UPDATE `mother_content_1377` SET meta_desc_test ='" + str(
                        mt_desc2) + "' WHERE   mother_url='" + str(
                        product_url) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")

                for pd in soup.find_all("h1", {"id": "motherTitle"}):
                    pro = (pd.text)
                    pro1 = pro.split(' ')
                    pro2 = pro1[1:]
                    pro3 = ' '.join(pro2)
                    if (pro3.lower().split() == pd_title.lower().split()):
                        mt_desc2 = ('product title same')
                        sql = ("UPDATE `mother_content_1377` SET product_name_test ='" + str(
                            mt_desc2) + "' WHERE   mother_url='" + str(
                            product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                    else:
                        mt_desc = 'product_title not same'
                        sql = ("UPDATE `mother_content_1377` SET product_name_test='" + str(
                            mt_desc) + "' WHERE   mother_url='" + str(
                            product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                        print(pro3)
                        print(pd_title)
