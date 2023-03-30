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
cur.execute("SELECT url,attribute_value,id FROM `upc_hs_ean_with_url1` WHERE attribute_name='HS Code' and hs_code_test='attribute not found' ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    hs_code = fetch[1].replace('rp_', '').replace(' ','')
    id = fetch[2]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")
    flag = 0
    ship1 = ''
    try:
        ship1 = soup.find("h3", id="shipping-info")
        ship = (ship1.text.strip() if ship1 else "not given")
        # print(ship)
    except:
        ship = "not given"
    if ship != "not given":
        ship2 = ship1.parent.find('div')
        prod = ship2.find_all("th")
        specs = ship2.find_all("td")
        # print(prod)
        # print(specs)
        i = 0
        while i < len(prod):
            j = 0
            while i < len(specs):
                z = (prod[i].text if prod else "not given")
                i += 1
                # print(z,i)
                x = (specs[j].text if specs else "not given")
                j += 1
                # print(x,j)
                # print(z.strip(),x.strip(),hs_code)
                if z.strip() == 'HS Code' and x.strip() == hs_code.strip():
                    # print("yes")
                    flag = 1
                    break
        if flag == 1:
            par = ("attribute found")
            sql = ("UPDATE `upc_hs_ean_with_url1` SET hs_code_test ='" + str(par) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")

        else:

            par1 = ("attribute not found")
            sql = ("UPDATE `upc_hs_ean_with_url1` SET hs_code_test ='" + str(par1) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")

