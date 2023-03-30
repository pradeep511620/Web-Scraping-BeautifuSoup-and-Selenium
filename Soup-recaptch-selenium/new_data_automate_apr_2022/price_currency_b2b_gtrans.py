
from bs4 import BeautifulSoup
import mysql.connector
import requests
mydb = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="TESTING"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,eur FROM `b2b_gtrans_currency_price_check_live` ")
my_result = cur.fetchall()
for fetch in my_result:
    product_url = fetch[0]
    price = (fetch[1])
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")
    a = 0
    for pd in soup.find("div", class_="priceInnerwrap").find_all('span'):
        a += 1
        if a == 1:
            s = pd.text
            stripped = s.split(" ", 1)[0]

            price1 = stripped.replace('€', '').replace(',', '').replace('/đơn vị ','EUR')
            pri2 = (price1)
            price2 = price
            print(pri2)
            print(price2)
            print('-----')

            """if rs == price1:
                pri = "price same"
                sql = ("UPDATE `b2b_gtrans_currency_price_check` SET price_test ='" + str(pri) + "',product_price='" + str(
                    rs) + "',calculate_price='" + str(price1) + "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                pri1 = "price not same"
                sql = ("UPDATE `b2b_gtrans_currency_price_check` SET price_test ='" + str(pri1) + "',product_price='" + str(
                    rs) + "',calculate_price='" + str(price1) + "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
                print(rs)
                print(price1)"""
