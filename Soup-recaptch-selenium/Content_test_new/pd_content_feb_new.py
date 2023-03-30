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
cur = mydb.cursor()
cur.execute("SELECT product_url,description,feature,working_mech,compatible_acc,standard,meta_desc,id FROM "
            " pd_content_dba_219  ")
myresult = cur.fetchall()
working = 0
not_working = 0
location = 0
for fetch in myresult:
    location += 1
    try:
        product_url = fetch[0]
        description = fetch[1]
        feature = fetch[2]
        working_mec = fetch[3]
        compatible_acc = fetch[4]
        standard = fetch[5]
        meta_desc=fetch[6]
        id = fetch[7]
        page = requests.get(product_url)
        soup = BeautifulSoup(page.content, "html.parser")
        title = soup.find("meta", attrs={'name': 'description'})
        meta = (title["content"] if title else "No meta title given")

        meta_d = meta_desc + " - Pay in EUR/USD | Delivery across Europe, Middle East, Africa / SE Asia | +44 203 287 5224 | sales@raptorsupplies.com"

        s = meta_d.split('\n')
        meta_d1 = "".join(s)
       
        if meta.strip() == meta_d1.strip():
            d1 = ('desc same')
            sql = ("UPDATE  pd_content_dba_219 SET meta_desc_test ='" + str(
                d1) + "' WHERE   id='" + str(
                id) + "'")

            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            d1 = ('desc not same')
            sql = ("UPDATE  pd_content_dba_219 SET meta_desc_test ='" + str(
                d1) + "' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        if soup.find_all("h3", {"id": "product-detail"}):
            values = soup.find_all("h3", {"id": "product-detail"})
            for x in values:
                y = str(x.find_next_sibling('div'))
                feat = html.unescape(y)
                fe = feat.replace('<div class="accordion-content">', '').replace('<ul>', '').replace('</div>',
                                                                                                     '').replace(
                    '</ul>', '').replace('<p>','').replace('</p>','').strip()
                desc = str(description).replace('</li>  ', '</li>').replace('</li> ', '</li>').replace(' <li>', '<li>')
                print(fe)
                print("----------")
                print(desc)
                if fe.strip() == desc.strip():
                    f3 = 'desc same'
                    # print(f3)
                    sql = ("UPDATE  pd_content_dba_219 SET desc_test ='" + str(
                        f3) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
                else:
                    f4 = 'desc not same'
                    sql = ("UPDATE  pd_content_dba_219 SET desc_test ='" + str(
                        f4) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
        else:
            print("desc not available")
        if soup.find_all("h3",{"id":"features"}):
            values = soup.find_all("h3",{"id":"features"})
            for x in values:
                y = str(x.find_next_sibling('div'))
                feat = html.unescape(y)
                fe = feat.replace('<div class="accordion-content">','').replace('<ul>','').replace('</div>','').replace('</ul>','').strip()
                feature= str(feature).replace('</li>  ','</li>').replace('</li> ','</li>').replace(' <li>','<li>')
                # print(fe)
                # print("----------")
                # print(feature)
                if fe.strip() == feature.strip():
                    f3 = 'feature same'
                    # print(f3)
                    sql = ("UPDATE  pd_content_dba_219 SET feature_test ='" + str(
                        f3) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
                else:
                    f4 = 'feature not same'
                    sql = ("UPDATE  pd_content_dba_219 SET feature_test ='" + str(
                        f4) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
        else:
            print("feature not available")
        if soup.find_all("h3",{"id":"working-mechanism"}):
            values = soup.find_all("h3",{"id":"working-mechanism"})
            for x in values:
                y = str(x.find_next_sibling('div'))
                feat = html.unescape(y)
                fe = feat.replace('<div class="accordion-content">','').replace('<ul>','').replace('</div>','').replace('</ul>','').strip()
                work= str(working_mec).replace('</li>  ','</li>').replace('</li> ','</li>').replace(' <li>','<li>').replace('’',"'")
                print(fe)
                print("----------")
                print(work)
                if fe.strip() == work.strip():
                    f3 = 'working_mec same'
                    # print(f3)
                    sql = ("UPDATE  pd_content_dba_219 SET working_mec_test ='" + str(
                        f3) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
                else:
                    f4 = 'working_mec not same'
                    sql = ("UPDATE  pd_content_dba_219 SET working_mec_test ='" + str(
                        f4) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
        else:
            print("working_mec not available")
        if soup.find_all("h3",{"id":"compatible-accessories"}):
            values = soup.find_all("h3",{"id":"compatible-accessories"})
            for x in values:
                y = str(x.find_next_sibling('div'))
                feat = html.unescape(y)
                fe = feat.replace('<div class="accordion-content">','').replace('<ul>','').replace('</div>','').replace('</ul>','').replace('</li></li>','').strip()
                comp= str(compatible_acc).replace('</li>  ','</li>').replace('</li> ','</li>').replace(' <li>','<li>')
                # print(fe)
                # print("----------")
                # print(comp)
                if fe.strip() == comp.strip():
                    f3 = 'compatible same'
                    # print(f3)
                    sql = ("UPDATE  pd_content_dba_219 SET comp_acc_test ='" + str(
                        f3) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
                else:
                    f4 = 'compatible not same'
                    sql = ("UPDATE  pd_content_dba_219 SET comp_acc_test ='" + str(
                        f4) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
        else:
            print("compatible_acc not available")
        if soup.find_all("h3",{"id":"standards-and-approvals"}):
            values = soup.find_all("h3",{"id":"standards-and-approvals"})
            for x in values:
                y = str(x.find_next_sibling('div'))
                feat = html.unescape(y)
                fe = feat.replace('<div class="accordion-content">','').replace('<ul>','').replace('</div>','').replace('</ul>','').replace('</li></li>','').strip()
                stan= str(standard).replace('</li>  ','</li>').replace('</li> ','</li>').replace(' <li>','<li>')
                print(fe)
                print("----------")
                print(stan)
                if fe.strip() == stan.strip():
                    f3 = 'standard same'
                    # print(f3)
                    sql = ("UPDATE  pd_content_dba_219 SET standard_test ='" + str(
                        f3) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
                else:
                    f4 = 'standard not same'
                    sql = ("UPDATE  pd_content_dba_219 SET standard_test ='" + str(
                        f4) + "' WHERE   id='" + str(
                        id) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
        else:
            print("standard not available")
    except AttributeError:

        pass
