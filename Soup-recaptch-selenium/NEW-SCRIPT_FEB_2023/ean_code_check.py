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
cur.execute("SELECT url,attribute_value,id FROM `upc_hs_ean_with_url` WHERE attribute_name ='EAN Code'   ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    hs_code = fetch[1].replace('rp_', '')
    id = fetch[2]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")
    flag = 0
    a = 0
    loc = 0
    label = ""
    val = ''
    prod = soup.find("div", class_="accordion-content d-flex").find_all("th")
    specs = soup.find("div", class_="accordion-content d-flex").find_all("td")
    for a, b in zip(prod, specs):
        attr_n = a.text
        attr_v = b.text
        # print(attr_n,attr_v)
        # print(attribute_name,attribute_value)
        if attr_n == 'EAN' and hs_code == attr_v:
            flag = 1
            break
    if flag == 1:
        par = ("attribute found")
        # print(par)
        sql = ("UPDATE `upc_hs_ean_with_url` SET ean_test ='" + str(par) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")

    else:

        par1 = ("attribute not found")
        print(par1)
        sql = ("UPDATE `upc_hs_ean_with_url` SET ean_test ='" + str(par1) + "' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")

