from bs4 import BeautifulSoup
import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="Testing_Automation_Data"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,com_price,id FROM price_dba81  limit 20")
my_result = cur.fetchall()
for fetch in my_result:
    url = fetch[0]
    pd_url = url.replace('//stage.','//s5.').replace('.com/','.com.au/')
    product_url = pd_url
    print(product_url)
    pr = (fetch[1])
    id = fetch[2]
    price = float(pr.replace('$', '').replace(',',""))
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")
    a = 0
    for pd in soup.find("div", class_="priceInnerwrap").find_all('span'):
        a += 1
        if a == 1:
            s = pd.text
            stripped = s.split(" ", 1)[0]
            price1 = stripped.replace('A$', '').replace(',',"")
            pri2 = float(price1)
            rs = round(pri2, 2)

            rs1 = round(price, 2)
            # print(rs1)
            price2 = rs1
            price1 = round(price2, 2)
            price3 = price1 * 1.50 * 1.1
            price4 = round(price3, 2)

            print(price4)
            print(rs)

            """if rs == price1:
                pri = "price same"
                sql = ("UPDATE price_dba81 SET price_test ='" + str(pri) + "',product_price='" + str(
                    rs) + "',calculate_price='" + str(price1) + "' WHERE   id='" + str(id) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                pri1 = "price not same"
                sql = ("UPDATE price_dba81 SET price_test ='" + str(pri1) + "',product_price='" + str(
                    rs) + "',calculate_price='" + str(price1) + "' WHERE   id='" + str(id) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
                print(rs)
                print(price1)"""
