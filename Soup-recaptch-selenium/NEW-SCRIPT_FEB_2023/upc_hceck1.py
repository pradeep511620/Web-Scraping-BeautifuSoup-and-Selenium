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
cur.execute("SELECT product_url,FIXED,id FROM `gsm_dba_154` WHERE issue_title LIKE '%gtin%' AND FIXED !='' ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    upc = fetch[1].replace('rp_', '')
    id = fetch[2]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")
    flag = 0
    try:
        ship1 = soup.find("h3")
        ship = (ship1.text.strip() if ship1 else "not given")
        # print(ship)
    except:
        ship = "not given"
    if ship != "not given":
        ship2 = ship1.parent.find('div')
        prod = ship2.find_all("th")
        specs = ship2.find_all("td")
        i = 0
        while i < len(prod):
            j = 0
            while j < len(specs):
                z = (prod[i].text if prod else "not given")
                # print(z)
                i += 1
                x = (specs[j].text if specs else "not given")
                # print(x)
                j += 1
                # print(upc)

                if z.strip() == 'UPC' and x.strip() == upc:
                    flag = 1
                    break
        if flag == 1:
            par = ("attribute found")
            sql = ("UPDATE `gsm_dba_154` SET upc_test ='" + str(par) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")

        else:

            par1 = ("attribute not found")
            sql = ("UPDATE `gsm_dba_154` SET upc_test ='" + str(par1) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")

