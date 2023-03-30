import requests
from bs4 import BeautifulSoup
from typing import TextIO
import re

import mysql.connector

mydb = mysql.connector.connect(
    host="rpt-m24-b2b-live.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="rpt_m241"
)
cur = mydb.cursor()
cur.execute("SELECT url,id FROM `z`  WHERE scrap_data IS NULL ")
my_result = cur.fetchall()
working = 0
not_working = 0
location = 0
for fetch in my_result:
    url = fetch[0]
    pd_url = url.replace('//b2b.','//www.').replace('.com/','.it/')
    id = fetch[1]

    location += 1
    print("\n \n URL : ", location)

    try:
        product_url = pd_url
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
        result = requests.get(product_url, headers=headers)

        if result.status_code == 200:
            print("\n site working")
            working += 1
        else:
            print("\n site not working" + str(result.status_code))
            not_working += 1
        print("WORKING ", working)
        print("NOT WORKING ", not_working)
        # a = (result.content.decode())

        soup = BeautifulSoup(result.content, 'html.parser')
        # print(soup.prettify())
        print('******PRODUCT_URL******')
        print(product_url)

        print("******TITLE******")
        title1 = soup.find("div", class_="productInfoRight half-collomn").find('h1')
        title = (title1.text.strip().replace('\n','') if title1 else "not given")
        print(title)

        print("******BRANDNAME******")
        brand1 = soup.find("div", class_="product-brand-wrap").find('a', class_='product-brand')
        brand = (brand1.text.strip() if brand1 else "not given")
        print(brand)

        print("******CROSSREF******")
        try:
            cro1 = soup.find("div", class_="item-model-crossref").find_all('span')
            crossref = [c1.text.strip() for c1 in cro1 if c1.text.strip() is not None]
            crossref.pop(1)
            # print(crossref)
            itemId = crossref[0].split(': ')[1]
            modelNo = crossref[1].split(': ')[1]
            crosRef = crossref[2].split(': ')[1]
            # print(itemId)
            # print(modelNo)
            # print(crosRef)
        except:
            crossref = []

        print("****** Description:******")
        if (soup.find("div", class_="product-description")):
            desccc = soup.find("div", class_="product-description")
            desc=desccc.text
            print(desccc)
        else:
            desc='pd specs not exist'
        print("******Technical Specifications: ******")
        prod = soup.find("div", class_="productDetailsLeft half-collomn").find_all('td')
        prod_spec_lst = [p1.text.strip() for p1 in prod if p1.text.strip() is not None]
        # print(prod_spec_lst)
        prod_i = []
        spec_i = []
        for i in range(0, len(prod_spec_lst)):
            if i % 2:
                spec_i.append(prod_spec_lst[i])
            else:
                prod_i.append(prod_spec_lst[i])
        i = 0
        while i < len(prod_i):
            j = 0
            while j < len(spec_i):
                z = (prod_i[i] if prod_i else "not given")
                print(z)

                i += 1

                x = (spec_i[j] if spec_i else "not given")
                print(x)

                j += 1

                sql = "INSERT INTO it_pd_specs(product_url,brand,model_no,attribute_name,attribute_value) VALUES (%s, %s ,%s ,%s, %s)"
                val = (product_url, brand, modelNo, z, x)
                cur.execute(sql, val)
                mydb.commit()
                print(cur.rowcount, "record(s) affected")

        sql = "INSERT INTO it_pd_detail(product_url,brand,product_title,item_id,model_no,cross_ref,pd_detail) VALUES (%s, %s ,%s ,%s, %s,%s,%s)"
        val = (product_url, brand, title, itemId, modelNo,crosRef,desc)
        cur.execute(sql, val)
        mydb.commit()
        print(cur.rowcount, "record(s) affected")
        sql = ("UPDATE `z` SET scrap_data ='yes' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    except AttributeError:
        pass
