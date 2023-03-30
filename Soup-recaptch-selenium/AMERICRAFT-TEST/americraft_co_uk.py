from bs4 import BeautifulSoup
import mysql.connector
import requests
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raptor_supplies_com"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,l3_name,parent_name,item_name,product_title FROM americraft_co_uk")
myresult = cur.fetchall()
for fetch in myresult:

    product_url=fetch[0]
    l3_name=fetch[1]
    parent_name=fetch[2]
    item_name=fetch[3]
    product_title=fetch[4]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    for pd in soup.find("div",class_="col-sm-7").find_all("h1"):
        pro=(pd.text)
        if(pro==product_title):
            prod=("product_title_same")
            sql=("UPDATE americraft_co_uk SET product_name_test ='"+str(prod)+"' WHERE   product_url='"+str(product_url)+"'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount , "records successful Done")
        else:
            prod1 = ("product_title_same")
            sql = ("UPDATE americraft_co_uk SET product_name_test ='" + str(prod1) + "' WHERE   product_url='" + str(
                product_url) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")

        a=0
        for bread in soup.find("ul",itemtype="https://schema.org/BreadcrumbList").find_all("span"):
            a+=1

            if(a==4):
                l3=(bread.text)
                if(l3.lower().strip()==l3_name.lower().strip()):
                    l3_n=("l3_name same")
                    sql = ("UPDATE americraft_co_uk SET l3_test ='" + str(l3_n) + "' WHERE   product_url='" + str(product_url) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
                else:
                    l3_n1=("l3_name not same")
                    sql = ("UPDATE americraft_co_uk SET l3_test ='" + str(l3_n1) + "' WHERE   product_url='" + str(product_url) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
            elif(a==5):
                par=(bread.text)
                if(par.lower().strip()==parent_name.lower().strip()):
                    par1=("parent_name same")
                    sql = ("UPDATE americraft_co_uk SET parent_test ='" + str(par1) + "' WHERE   product_url='" + str(product_url) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
                else:
                    par2=("parent_name not same")
                    sql = ("UPDATE americraft_co_uk SET parent_test ='" + str(par2) + "' WHERE   product_url='" + str(product_url) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")

                b=0
                for item in soup.find("div",class_="prodcutspec").find_all("td"):
                    b+=1
                    if(b==2):
                        it1=(item.text)
                        if(item_name.lower().strip()==it1.lower().strip()):
                            item1=("item_name same")
                            sql = ("UPDATE americraft_co_uk SET item_test ='" + str(item1) + "' WHERE   product_url='" + str(product_url) + "'")
                            cur.execute(sql)
                            mydb.commit()
                            print(cur.rowcount, "records successful Done")
                        else:
                            item2=("item_name nort same")
                            sql = ("UPDATE americraft_com SET item_test ='" + str(item2) + "' WHERE   product_url='" + str(product_url) + "'")
                            cur.execute(sql)
                            mydb.commit()
                            print(cur.rowcount, "records successful Done")

