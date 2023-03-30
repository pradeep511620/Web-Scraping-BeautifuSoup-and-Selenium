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
cur.execute('select product_url,uses,feature,Compatible_Accessories,Standards_Approvals,Installation,FaQ from `new_content_aug` where faq_test ="faq content not same" and FaQ !=" " ')
myresult=cur.fetchall()
for fetch in myresult:
    product_url=fetch[0]
    uses=fetch[1]
    feature=fetch[2]
    compatible=fetch[3]
    standard=fetch[4]
    installation=fetch[5]
    faq=fetch[6]
    page=requests.get(product_url)
    soup=BeautifulSoup(page.content,'lxml')
    a=0
    for desc in soup.find('div',class_='prodetail').find_all('ul'):
        a+=1
        if(a==1):
            s=str(desc)
            use=(s[4:-5])
            use1 = use.replace('&amp;', "&")
            s1=uses.split('\n')
            s2=''.join(s1)
            if(s2==use1):
                u=('uses content is same')
                sql = ("UPDATE `new_content_aug`  SET uses_test ='" + str(u) + "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                u1=('uses content not same')
                sql = ("UPDATE `new_content_aug`  SET uses_test ='" + str(u1) + "' WHERE   product_url='" + str(
                    product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
        elif(a==2):
            s = str(desc)
            fet = (s[4:-5])
            fet1=fet.replace('&amp;',"&")
            s1 = feature.split('\n')
            s2 = ''.join(s1)
            if(s2==fet1):
                ft1=('feature content is same')
                sql = ("UPDATE `new_content_aug`  SET feature_test ='" + str(ft1) + "' WHERE   product_url='" + str(
                    product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                ft2=('feature content is not same')
                sql = ("UPDATE `new_content_aug`  SET feature_test ='" + str(ft2) + "' WHERE   product_url='" + str(
                    product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
                print(fet)
                print(s2)
        elif (a == 3):
            s = str(desc)
            comp = (s[4:-5])
            comp1 = comp.replace('&amp;', "&")
            s1 = compatible.split('\n')
            s2 = ''.join(s1)
            if (s2 == comp1):
                com1=('compatible content is same')
                sql = ("UPDATE `new_content_aug`  SET compatible_test ='" + str(com1) + "' WHERE   product_url='" + str(
                    product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                com2=('compatible content is not same')
                sql = ("UPDATE `new_content_aug`  SET compatible_test ='" + str(com2) + "' WHERE   product_url='" + str(
                    product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
        elif (a == 4):
            s = str(desc)
            s4=s.replace('amp;', '')
            sta= (s4[4:-5])
            s1 = standard.split('\n')
            s2 = ''.join(s1)

            if (s2 == sta):
                sta1=('standard content is same')
                sql = ("UPDATE `new_content_aug`  SET standard_test ='" + str(sta1) + "' WHERE   product_url='" + str(
                    product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                sta2=('standard content is not same')
                sql = ("UPDATE `new_content_aug`  SET standard_test ='" + str(sta2) + "' WHERE   product_url='" + str(
                    product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")

        elif (a == 5):
            s = str(desc)
            s4=s.replace('amp;', '')
            insta= (s4[4:-5])
            s1 = installation.split('\n')
            s2 = ''.join(s1)

            if (s2 == insta):
                insta1=('installation content is same')
                sql = ("UPDATE `new_content_aug`  SET installation_test ='" + str(insta1) + "' WHERE   product_url='" + str(
                    product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                insta2=('installation content is not same')
                sql = ("UPDATE `new_content_aug`  SET installation_test ='" + str(
                    insta2) + "' WHERE   product_url='" + str(
                    product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            a = 0
            for desc1 in soup.find_all('div', class_='productdetailbox'):
                a += 1
                d=str(desc1)
                d1=d.split('<b>')[1]
                d2=d1.replace('<br/><br/>','<br><br>')
                d3=d2[:-12]
                d4='<b>'+d3
                d5=d4.replace('&amp;',"&")
                s1 = faq.split('\n')
                s2 = ''.join(s1)
                if(s2==d5):
                    faq1=('faq content same')
                    sql = ("UPDATE `new_content_aug`  SET faq_test ='" + str(
                        faq1) + "' WHERE   product_url='" + str(
                        product_url) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
                else:
                    faq2=('faq content not same')
                    sql = ("UPDATE `new_content_aug`  SET faq_test ='" + str(
                        faq2) + "' WHERE   product_url='" + str(
                        product_url) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
                    print(desc1)
                    print(d5)
                    print(s2)



