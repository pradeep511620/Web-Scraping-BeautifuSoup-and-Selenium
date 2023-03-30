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
cur.execute("SELECT product_url,description,feature,working_mech,compatible_acc,standard,id FROM "
            " `pd_content_dba_188` where standard !='' and standard_test ='standard not same' ")
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
        id = fetch[6]
        page = requests.get(product_url)
        soup = BeautifulSoup(page.content, "html.parser")
        values = soup.find_all("div", class_='accordion-div')
        try:
            work1 = soup.find("h3", id="working-mechanism")
            work = (work1.text.strip() if work1 else "not given")
            # print(work)
        except:
            work = "not given"
        if work != "not given":
            work2 = values[3]
            # print(work2)
            # work_ = (work2.text.replace('\n', ' | ').strip() if work2 else "not given")
            # print(work_)
        else:
            print("continue")

        print('*********Features***********')
        try:
            fea1 = soup.find("h3", id="features")
            fea = (fea1.text.strip() if fea1 else "not given")
            print(fea)
        except:
            fea = "not given"
        if fea != "not given":
            fea2 = values[-4].find('ul')
            fea_1 = str(fea2 if fea2 else "not given")
            i = fea_1.replace('<ul>','').replace('</ul>','')
            f = html.unescape(i)
            # print(fea2)
            # print("---")
            # print(feature)
            if f.strip() == feature.strip():
                f3 = 'feature same'
                # print(f3)
                sql = ("UPDATE  `pd_content_dba_188` SET feature_test ='" + str(
                    f3) + "' WHERE   id='" + str(
                    id) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                f4 = 'feature not same'
                sql = ("UPDATE  `pd_content_dba_188` SET feature_test ='" + str(
                    f4) + "' WHERE   id='" + str(
                    id) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
        else:
            print("continue")

        print('*********Compatible Accessories***********')
        try:
            com1 = soup.find("h3", id="compatible-accessories")
            com = (com1.text.strip() if com1 else "not given")
            print(com)
        except:
            com = "not given"
        if com != "not given":
            com2 = values[-3].find('ul')
            com_ = (com2.text.strip() if com2 else "not given")
            print(com_)
        else:
            print("continue")

        print('*********Standards and Approvals***********')
        try:
            stand1 = soup.find("h3", id="standards-and-approvals")
            stand = (stand1.text.strip() if stand1 else "not given")
            # print(stand)
        except:
            stand = "not given"
        if stand != "not given":
            stand2 = values[-2].find('ul')
            stand_ = str(stand2 if stand2 else "not given")
            st = stand_.replace('<ul>','').replace('</ul>','')
            if st.strip() == standard.strip():
                st1 = ("standard same")
                sql = ("UPDATE  `pd_content_dba_188` SET standard_test ='" + str(
                    st1) + "' WHERE   id='" + str(
                    id) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                st2 = 'standard not same'
                sql = ("UPDATE  `pd_content_dba_188` SET standard_test ='" + str(
                    st2) + "' WHERE   id='" + str(
                    id) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
                print(st)
                print(standard)

        else:
            print("continue")


    except AttributeError:

        pass
""" print('*********Shipping Information***********')
        try:
            ship1 = soup.find("h3", id="shipping-info")
            ship = (ship1.text.strip() if ship1 else "not given")
            print(ship)
        except:
            ship = "not given"
        if ship != "not given":
            ship2 = values[2].find_all('table')
            shipLst = []
            shipLst_ = []
            for sh1 in ship2:
                shipLst.append(sh1.text.strip() if sh1 is not None else sh1 is "not given")
            shipLst_ = list(filter(None, shipLst))
            print(shipLst_)
        else:
            print("continue")"""

"""try:
            spec1 = soup.find("h3", id="specification1")
            spec = (spec1.text.strip() if spec1 else "not given")
            print(spec)
        except:
            spec = "not given"
        if spec != "not given":
            spec2 = values[0].find('tr')
            spec_ = (spec2.text.strip() if spec2 else "not given")
            print(spec_)
        else:
            print("continue")

        print('*********Product Details***********')
        try:
            prod1 = soup.find("h3", id="specification1")
            prod = (prod1.text.strip() if prod1 else "not given")
            print(prod)
        except:
            prod = "not given"
        if prod != "not given":
            prod2 = values[1].find('p')
            prod_ = (prod2.text.strip() if prod2 else "not given")
            print(prod_)
        else:
            print("continue")"""




            # save_details: TextIO = open("spec2.txt", "a+", encoding="utf-8")
            # save_details.write("\n"  + z + "\t" + x)
            # save_details.close()
            # print("\n**Record stored into txt file.**")