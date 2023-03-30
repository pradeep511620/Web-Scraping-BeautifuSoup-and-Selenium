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
cur.execute('select product_url,title_tag,meta_desc,category_desc from `category_content_aug`')
myresult=cur.fetchall()
for fetch in myresult:
    product_url=fetch[0]
    meta_title=fetch[1]
    meta_desc=fetch[2]
    category_desc=fetch[3]
    page=requests.get(product_url)
    soup=BeautifulSoup(page.content,'lxml')

    # for desc in soup.find('div',class_='l3content_desk l3content').find_all('p'):
    #     d=str(desc)
    #     d1=(d[3:-4])
    #     d2=d1.replace('<br/> ',"<br>")
    #     d3=d2.replace('&amp;',"&")
    #     t1 = category_desc.split('\n')
    #     t2 = "".join(t1)
    #     if(d3.strip()==t2.strip()):
    #         desc1=print('desc is same')
    #     #     sql = ("UPDATE `category_content_aug`  SET desc_test ='" + str(desc1) + "' WHERE   product_url='" + str(product_url) + "'")
    #     #     cur.execute(sql)
    #     #     mydb.commit()
    #     #     print(cur.rowcount, "records successful Done")
    #     else:
    #         desc2=('desc is not same')
    #     #     sql = ("UPDATE `category_content_aug` SET desc_test ='" + str(desc2) + "' WHERE   product_url='" + str(
    #     #         product_url) + "'")
    #     #     cur.execute(sql)
    #     #     mydb.commit()
    #     #     print(cur.rowcount, "records successful Done")
    #         print(t2)
    #         print(d3)
    # for title in soup.find("div",'l3pagehead').find_all('h1'):
    #     tit=(title.text)
    #     title1=meta_title
    #     if(tit.split()==title1.split()):
    #         tit1=print('meta_title same')
    #
    #     #     sql = ("UPDATE `mother_content_aug`  SET meta_title_test ='" + str(tit1) + "' WHERE   product_url='" + str(
    #     #         product_url) + "'")
    #     #     cur.execute(sql)
    #     #     mydb.commit()
    #     #     print(cur.rowcount, "records successful Done")
    #     # else:
    #         tit2=('meta_title not same')
    #         # sql = ("UPDATE `mother_content_aug`  SET meta_title_test ='" + str(tit2) + "' WHERE   product_url='" + str(
    #         #     product_url) + "'")
    #         # cur.execute(sql)
    #         # mydb.commit()
    #         # print(cur.rowcount, "records successful Done")
    #         print(tit)
    #         print(title1)

    for meta_d in soup.find_all('meta',attrs={'name':'description'}):
        meta=(meta_d.get('content'))
        meta_des=meta_desc
        if(meta==meta_des):
            mt_desc1=print("meta desc is same")
        #     sql = ("UPDATE `mother_content_aug` SET meta_desc_test ='" + str(mt_desc1) + "' WHERE   product_url='" + str(
        #         product_url) + "'")
        #     cur.execute(sql)
        #     mydb.commit()
        #     print(cur.rowcount, "records successful Done")
        # else:
            mt_desc2 =print( "meta desc is same")
            # sql = ("UPDATE `mother_content_aug`  SET meta_desc_test ='" + str(mt_desc2) + "' WHERE   product_url='" + str(
            #     product_url) + "'")
            # cur.execute(sql)
            # mydb.commit()
            # print(cur.rowcount, "records successful Done")

    # for pd in soup.find("div", class_="l3pagehead").find_all("h1"):
    #     pro = (pd.text)
    #     pro1=pro.split(' ')
    #     pro2=pro1[1:]
    #     pro3=' '.join(pro2)
    #     if(pro3.split()==pd_title.split()):
    #         mt_desc2=('product title same')
    #         sql = ("UPDATE `mother_content_aug`  SET product_name_test ='" + str(
    #             mt_desc2) + "' WHERE   product_url='" + str(
    #             product_url) + "'")
    #         cur.execute(sql)
    #         mydb.commit()
    #         print(cur.rowcount, "records successful Done")
    #     else:
    #         mt_desc=('product_title not same')
    #         sql = ("UPDATE `mother_content_aug`  SET product_name_test='" + str(
    #             mt_desc) + "' WHERE   product_url='" + str(
    #             product_url) + "'")
    #         cur.execute(sql)
    #         mydb.commit()
    #         print(cur.rowcount, "records successful Done")
    #         print(pro3)
    #         print(pd_title)
