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
cur.execute('select product_url,product_specs,title_tag,meta_desc,product_title from `old_pd_content_aug` where meta_title_test="meta_title not same"')
myresult=cur.fetchall()
for fetch in myresult:
    product_url=fetch[0]
    description=fetch[1]
    meta_title=fetch[2]
    meta_desc=fetch[3]
    pd_title=fetch[4]

    page=requests.get(product_url)
    soup=BeautifulSoup(page.content,'lxml')

    for desc in soup.find('div',class_='prodetail').find_all('ul'):
        d=str(desc)
        d1=(d[4:-5])
        d2=d1.replace('&amp;',"&")
        # d1=d.split('\n')
        # d2=" ".join(d1)
        t1 = description.split('\n')
        t2 = "".join(t1)

        if(d2.split()==t2.split()):
            desc1=('desc is same')
            sql = ("UPDATE `old_pd_content_aug`  SET desc_test ='" + str(desc1) + "' WHERE   product_url='" + str(product_url) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            desc2=('desc is not same')
            sql = ("UPDATE `old_pd_content_aug` SET desc_test ='" + str(desc2) + "' WHERE   product_url='" + str(
                product_url) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
            print(t2)
            print(d2)
        for title in soup.find_all('title'):
            tit=(title.text)
            title1=meta_title+' | Raptor Supplies'
            if(tit.split()==title1.split()):
                tit1=('meta_title same')

                sql = ("UPDATE `old_pd_content_aug`  SET meta_title_test ='" + str(tit1) + "' WHERE   product_url='" + str(
                    product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                tit2=('meta_title not same')
                sql = ("UPDATE `old_pd_content_aug`  SET meta_title_test ='" + str(tit2) + "' WHERE   product_url='" + str(
                    product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
                print(tit)
                print(title1)

            for meta_d in soup.find_all('meta',attrs={'name':'description'}):
                meta=(meta_d.get('content'))
                meta_des=meta_desc+" - Pay in EUR/USD | Delivery across Europe, Middle East, Africa / SE Asia | +44 203 287 5224 | sales@raptorsupplies.com"
                if(meta==meta_des):
                    mt_desc1=("meta desc is same")
                    sql = ("UPDATE `old_pd_content_aug` SET meta_desc_test ='" + str(mt_desc1) + "' WHERE   product_url='" + str(
                        product_url) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
                else:
                    mt_desc2 = "meta desc is same"
                    sql = ("UPDATE `old_pd_content_aug`  SET meta_desc_test ='" + str(mt_desc2) + "' WHERE   product_url='" + str(
                        product_url) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")

                for pd in soup.find("div", class_="col-sm-7").find_all("h1"):
                    pro = (pd.text)
                    pro1=pro.split(' ')
                    pro2=pro1[2:]
                    pro3=' '.join(pro2)
                    if(pro3.split()==pd_title.split()):
                        mt_desc2=('product title same')
                        sql = ("UPDATE `old_pd_content_aug`  SET product_name_test ='" + str(
                            mt_desc2) + "' WHERE   product_url='" + str(
                            product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                    else:
                        mt_desc=('product_title not same')
                        sql = ("UPDATE `old_pd_content_aug`  SET product_name_test='" + str(
                            mt_desc) + "' WHERE   product_url='" + str(
                            product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                        print(pro3)
                        print(pd_title)
