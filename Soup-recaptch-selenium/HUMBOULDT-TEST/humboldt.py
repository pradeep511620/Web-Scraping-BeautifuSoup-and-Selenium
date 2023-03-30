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
cur.execute("SELECT product_url,parent_name,product_title FROM humboldt")
myresult = cur.fetchall()
for fetch in myresult:

    product_url=fetch[0]
    parent_name=fetch[1]
    product_title=fetch[2]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    """for pd in soup.find("div",class_="col-sm-7").find_all("h1"):
        pro=(pd.text)
        if(pro.lower().strip()==product_title.lower().strip()):
            prod=("product_title_same")
            sql=("UPDATE humboldt SET product_name_test ='"+str(prod)+"' WHERE   product_url='"+str(product_url)+"'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount , "records successful Done")
        else:
            prod1 = ("product_title_same")
            sql = ("UPDATE humboldt SET product_name_test ='" + str(prod1) + "' WHERE   product_url='" + str(
                product_url) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")"""
    a=0
    for parent in soup.find("ul", itemtype="https://schema.org/BreadcrumbList").find_all("span"):
        a+=1

        if(a==5):
            pr=(parent.text)
            if (pr.lower().strip() == parent_name.lower().strip()):
                prod = ("parent name same")
                sql = ("UPDATE humboldt SET parent_test ='" + str(prod) + "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")



