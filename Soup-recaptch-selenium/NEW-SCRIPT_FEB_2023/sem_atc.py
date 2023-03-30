from bs4 import BeautifulSoup
import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_dat"
)
cur = mydb.cursor()
cur.execute("SELECT url FROM `sem_atc` where remarks_ship_blank is null")
my_result = cur.fetchall()
for fetch in my_result:
    product_url = fetch[0]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")
    if soup.find("div", class_="priceInnerwrap").find_all('span'):
        a = 0
        for pd in soup.find("div", class_="priceInnerwrap").find_all('span'):
            a += 1
            if a == 1:
                s = pd.text
                stripped = s.split(" ", 1)[0]
                price1 = stripped.replace('$', '').replace(',', "")
                pri2 = float(price1)
                if pri2 <= 300.00 :
                    flag = 0
                    try:
                        ship1 = soup.find("h3", id="shipping-info")
                        ship = (ship1.text.strip() if ship1 else "not given")
                    except:
                        ship = "not given"
                    if ship != "not given":
                        prod1 = ("yes shipping info found")
                        sql = ("UPDATE `sem_atc` SET remarks_ship_blank ='" + str(
                            prod1) + "' WHERE   url='" + str(
                            product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                    else:
                        prod1 = ("shipping ifo not found")
                        sql = ("UPDATE `sem_atc` SET remarks_ship_blank ='" + str(
                            prod1) + "' WHERE   url='" + str(
                            product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")


                else:
                    prod = ("Yes more 300")
                    sql = ("UPDATE `sem_atc` SET remark_more_300 ='" + str(
                        prod) + "' WHERE   url='" + str(
                        product_url) + "'")
                    cur.execute(sql)
                    mydb.commit()
                    print(cur.rowcount, "records successful Done")
    else:
        pro = ("price zero")
        sql = ("UPDATE `sem_atc` SET remark_zero_price ='" + str(
            pro) + "' WHERE   url='" + str(
            product_url) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")