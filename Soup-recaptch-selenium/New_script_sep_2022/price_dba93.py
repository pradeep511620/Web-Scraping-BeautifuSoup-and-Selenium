from bs4 import BeautifulSoup
import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_data_automation"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,final_price,id FROM price_dba_100 where price_test is null  ")
my_result = cur.fetchall()
for fetch in my_result:
    product_url = fetch[0]
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
            price1 = stripped.replace('$', '').replace(',',"")
            pri2 = float(price1)
            rs = round(pri2, 2)
            # price2 = price / 0.55
            price1 = round(price, 2)

            if rs == price1:
                pri = "price same"
                sql = ("UPDATE price_dba_100 SET price_test ='" + str(pri) + "',product_price='" + str(
                    rs) + "',calculate_price='" + str(price1) + "' WHERE   id='" + str(id) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                pri1 = "price not same"
                sql = ("UPDATE price_dba_100 SET price_test ='" + str(pri1) + "',product_price='" + str(
                    rs) + "',calculate_price='" + str(price1) + "' WHERE   id='" + str(id) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
                print(rs)
                print(price1)
