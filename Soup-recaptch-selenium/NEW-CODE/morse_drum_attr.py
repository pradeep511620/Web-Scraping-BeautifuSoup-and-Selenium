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
cur.execute("SELECT product_url,weight,shipping_len,shipping_wi,shipping_hei,price FROM `morse_drum_attr`  ")
myresult = cur.fetchall()
for fetch in myresult:

    product_url=fetch[0]
    weight = float(fetch[1])
    shipping_l = float(fetch[2])
    shipping_w = float(fetch[3])
    shipping_h = float(fetch[4])
    price = float(fetch[1])

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    a = 0
    for pd in soup.find("div", class_="realprice").find_all("span"):
        a += 1
        if a == 2:
            price1 = float(pd.text)
            rate1 = (price * 0.95)
            rate = (rate1)

            rs = round(rate, 2)
            if (rs == price1):
                pri = ("price same")
                sql = ("UPDATE `morse_drum_attr` SET price_test ='" + str(pri) + "',product_price='" + str(
                    price1) + "',calculate_price='" + str(rs) + "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
            else:
                pri1 = ("price not same")
                sql = ("UPDATE `morse_drum_attr` SET price_test ='" + str(pri1) + "',product_price='" + str(
                    price1) + "',calculate_price='" + str(rs) + "' WHERE   product_url='" + str(product_url) + "'")
                cur.execute(sql)
                mydb.commit()
                print(cur.rowcount, "records successful Done")
                print(rs)
                print(price1)
            a=0
            for attr in soup.find("div", class_="productshing").find_all("td"):
                a += 1

                if a == 2:
                    we = float(attr.text)
                    we1 = (weight*0.45)
                    we2 = round(we1,2)
                    if we2 == we:
                        weight_check = ("weight same")
                        sql = ("UPDATE `morse_drum_attr` SET weight_test ='" + str(weight_check) + "' WHERE   product_url='" + str(product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                    else:
                        weight_check1 = ("weight not same")
                        sql = ("UPDATE `morse_drum_attr` SET weight_test ='" + str(weight_check1) + "' WHERE   product_url='" + str(product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                        print(we)
                        print(we2)
                elif a == 4:
                    h = float(attr.text)
                    h1 = (shipping_h * 2.54)
                    h2 = round(h1, 2)
                    if h2 == h:
                        hi_check = ("height same")
                        sql = ("UPDATE `morse_drum_attr` SET height_test ='" + str(hi_check) + "' WHERE   product_url='" + str(product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                    else:
                        hi_check1 = ("height not same")
                        sql = ("UPDATE `morse_drum_attr` SET height_test ='" + str(hi_check1) + "' WHERE   product_url='" + str(product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                        print(h)
                        print(h2)
                elif a == 6:
                    l = float(attr.text)
                    l1 = (shipping_l * 2.54)
                    l2 = round(l1, 2)
                    if l2 == l:
                        le_check = ("length same")
                        sql = ("UPDATE `morse_drum_attr` SET length_test ='" + str(le_check) + "' WHERE   product_url='" + str(product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                    else:
                        le_check1 = ("length not same")
                        sql = ("UPDATE `morse_drum_attr` SET length_test ='" + str(le_check1) + "' WHERE   product_url='" + str(product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                        print(l)
                        print(l2)
                elif a == 8:
                    w = float(attr.text)
                    w1 = (shipping_w * 2.54)
                    w2 = round(w1, 2)
                    if w2 == w:
                        w_check = ("width same")
                        sql = ("UPDATE `morse_drum_attr` SET width_test ='" + str(w_check) + "' WHERE   product_url='" + str(product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                    else:
                        w_check1 = ("width not same")
                        sql = ("UPDATE `morse_drum_attr` SET width_test ='" + str(w_check1) + "' WHERE   product_url='" + str(product_url) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                        print(w)
                        print(w2)
