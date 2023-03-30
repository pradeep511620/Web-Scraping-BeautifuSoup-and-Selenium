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
cur.execute("SELECT product_url,com_price FROM `aurand_price` where id>527 ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url=fetch[0]
    price=float(fetch[1])
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    a=0
    for pd in soup.find("div", class_="priceInnerwrap").find_all('span'):
        a += 1
        if (a == 1):
            s = (pd.text)
            sep = ' '
            stripped = s.split(sep, 1)[0]
            price1 = stripped.replace('$', '')
            price2 = float(price1)
            pr = (price2)
            rs = round(pr, 2)
            pri=(price)
            price1=round(pri,2)

            if(rs==price1):
                pri=("price same")
                sql = ("UPDATE `aurand_price` SET price_test ='" + str(pri) + "',product_price='"+str(rs)+"',calculate_price='"+str(price1)+"' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                pri1=("price not same")
                sql = ("UPDATE `aurand_price` SET price_test ='" + str(pri1) + "',product_price='" + str(rs) + "',calculate_price='"+str(price1)+ "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
                print(rs)
                print(price1)





