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
cur.execute("SELECT product_url,b2b_price FROM `aurand_price`")
myresult = cur.fetchall()
for fetch in myresult:

    product_url=fetch[0]
    price=float(fetch[1])


    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    a=0
    for pd in soup.find("div", class_="realprice").find_all("span"):
        a+=1
        if (a == 2):
            price1 = (pd.text)
            price2= (price1.replace('€',""))
            price3= float(price2.replace(',',""))
            rate = (price*0.96)
            rs = round(rate, 2)
            if(rs==price3):
                pri=("price same")
                sql = ("UPDATE `aurand_price` SET b2b_price_test ='" + str(pri) + "',b2b_product_price='"+str(price1)+"',b2b_calculate_price='"+str(rs)+ "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                pri1=("price not same")
                sql = ("UPDATE `aurand_price`  SET b2b_price_test ='" + str(pri1) + "',b2b_product_price='" + str(price1) +"',b2b_calculate_price='"+str(rs)+ "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
                print(rs)
                print(price3)




