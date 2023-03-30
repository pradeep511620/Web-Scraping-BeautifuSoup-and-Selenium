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
cur.execute("SELECT product_url,price,country FROM americraft_com where country_name_test='country not same '")
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
        if(a==2):
            price1=float(pd.text)
            rate=(price/0.7*0.95)
            rs=round(rate,2)
            if(rs==price1):
                pri=("price same")
                sql = ("UPDATE americraft_com SET price_test ='" + str(pri) + "',product_price='"+str(price1)+"' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                pri1=("price not same")
                sql = ("UPDATE americraft_com SET price_test ='" + str(pri1) + "',product_price='" + str(price1) + "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
                print(rs)
                print(price1)
            b=0
            for cou in soup.find("div",class_="col-sm-6 productdetailright").find_all("td"):
                b+=1
                if(b==2):
                    coun=(cou.text)
                    if(coun.strip()==country.strip()):
                        coun1=("country name same")
                        sql = ("UPDATE americraft_com SET country_name_test ='" + str(coun1) + "',product_price='" + str(price1) + "' WHERE   product_url='" + str(product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                    else:
                        coun2=("country not same ")
                        sql = ("UPDATE americraft_com SET country_name_test ='" + str(coun2) + "',product_price='" + str(price1) + "' WHERE   product_url='" + str(product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")


