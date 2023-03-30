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
cur.execute("SELECT product_url,PRODUCT_price,country FROM accushim_onb where id>120 ")
myresult = cur.fetchall()
for fetch in myresult:

    product_url=fetch[0]
    price=float(fetch[1])
    country=fetch[2]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    a=0
    for pd in soup.find("div", class_="realprice").find_all("span"):
        a+=1
        if (a == 6):
            price1 = float(pd.text)
            #(price) * ROUND(1 - 60 / 100, 2)) / 0.7, 4)*0.95
            rate = (price*1.2)
            rs = round(rate, 2)
            if(rs==price1):
                pri=("price same")
                sql = ("UPDATE accushim_onb SET uk_price_test ='" + str(pri) + "',uk_product_price='"+str(price1)+"' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                pri1=("price not same")
                sql = ("UPDATE accushim_onb  SET uk_price_test ='" + str(pri1) + "',uk_product_price='" + str(price1) + "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
                print(rs)
                print(price1)
        elif (a == 3):
            dis_price = float(pd.text)
            sql = ("UPDATE accushim_onb  SET discount_price ='" + str(dis_price) + "' WHERE   product_url='" + str(product_url) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")

            b=0
            for cou in soup.find("div",class_="productshing").find_all("td"):
                b+=1
                if(b==2) or (b==4) or (b==6) or (b==8) or (b==10) or (b==12) or (b==14):
                    coun=(cou.text)
                    if(coun.strip()==country.strip()):
                        coun1=("country name same")
                        sql = ("UPDATE accushim_onb  SET country_name_test ='" + str(coun1) + "' WHERE   product_url='" + str(product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                    else:
                        coun2=("country not same ")
                        sql = ("UPDATE accushim_onb SET country_name_test ='" + str(coun2) + "' WHERE   product_url='" + str(product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")


