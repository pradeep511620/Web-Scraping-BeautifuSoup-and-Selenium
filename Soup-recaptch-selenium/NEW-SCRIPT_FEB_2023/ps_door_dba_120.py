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
cur.execute("SELECT product_url,l3_name,parent_name,item_name,product_title,model_no,brand FROM `dba_186_magliner` where product_name_test is null")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    l3_name = fetch[1]
    parent_name = fetch[2]
    item_name = fetch[3]
    product_title = fetch[4]
    model_no = fetch[5]
    brand = fetch[6]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")

    for pd in soup.find("div", class_="about-product").find_all("h1"):
        pr = pd.text
        pr1 = pr.split()
        pro = " ".join(pr1)
        product = brand + " " + model_no + " " + product_title
        prod = product.split()
        product_title = " ".join(prod)

        # print(product_title)
        # print(pro)
        if pro.lower().strip() == product_title.lower().strip():
            prod = "product_title_same"
            sql = ("UPDATE `dba_186_magliner`SET product_name_test ='" + str(prod) + "' WHERE   product_url='" + str(
                product_url) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            prod1 = "product_title not same"
            sql = ("UPDATE `dba_186_magliner`SET product_name_test ='" + str(prod1) + "' WHERE   product_url='" + str(
                product_url) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")

        b = 0
        for item in soup.find("div", class_="accordion-div").find_all("td"):
            b += 1
            # print(item)
            # print(b)
            if b == 1:
                it1 = item.text
                if (item_name.lower().strip() == it1.lower().strip()):
                    item1 = ("item_name same")
                    sql = ("UPDATE `dba_186_magliner`SET item_test ='" + str(item1) + "' WHERE   product_url='" + str(
                        product_url) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
                else:
                    item2 = ("item_name not same")
                    sql = ("UPDATE `dba_186_magliner`SET item_test ='" + str(item2) + "' WHERE   product_url='" + str(
                        product_url) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")

                a = 0
                for bread in soup.find("ul", class_="items breadcrumb").find_all("span"):
                    a += 1

                    if (a == 10):
                        l3 = (bread.text)
                        if (l3.lower().strip() == l3_name.lower().strip()):
                            l3_n = ("l3_name same")
                            sql = ("UPDATE `dba_186_magliner`SET l3_test ='" + str(
                                l3_n) + "' WHERE   product_url='" + str(product_url) + "'")
                            cur.execute(sql)
                            mydb.commit()
                            print(cur.rowcount, "records successful Done")
                        else:
                            l3_n1 = ("l3_name not same")
                            sql = ("UPDATE `dba_186_magliner`SET l3_test ='" + str(
                                l3_n1) + "' WHERE   product_url='" + str(product_url) + "'")
                            cur.execute(sql)
                            mydb.commit()
                            print(cur.rowcount, "records successful Done")
                    elif a == 13:
                        par = bread.text
                        if par.lower().strip() == parent_name.lower().strip():
                            par1 = "parent_name same"
                            sql = ("UPDATE `dba_186_magliner`SET parent_test ='" + str(
                                par1) + "' WHERE   product_url='" + str(product_url) + "'")
                            cur.execute(sql)
                            mydb.commit()
                            print(cur.rowcount, "records successful Done")
                        else:
                            par2 = "parent_name not same"
                            sql = ("UPDATE `dba_186_magliner`   SET parent_test ='" + str(
                                par2) + "' WHERE   product_url='" + str(product_url) + "'")
                            cur.execute(sql)
                            mydb.commit()
                            print(cur.rowcount, "records successful Done")
