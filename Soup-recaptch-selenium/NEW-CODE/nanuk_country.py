from bs4 import BeautifulSoup
import mysql.connector
import requests
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raptor_staging"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,price FROM `sklonik_onb` ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url=fetch[0]
    price=float(fetch[1])
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")

    a = 0
    for pd in soup.find("div", class_="realprice").find_all("span"):
        a += 1
        if (a == 2):
            price1 = float(pd.text)
            rate = (price/0.7*0.95)
            rs = round(rate, 2)
            if (rs == price1):
                pri = ("price same")
                sql = ("UPDATE `sklonik_onb` SET price_test ='" + str(pri) + "',product_price='" + str(
                    price1) + "',calculate_price='" + str(rs) + "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                pri1 = ("price not same")
                sql = ("UPDATE `sklonik_onb` SET price_test ='" + str(pri1) + "',product_price='" + str(
                    price1) + "',calculate_price='" + str(rs) + "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
                print(rs)
                print(price1)