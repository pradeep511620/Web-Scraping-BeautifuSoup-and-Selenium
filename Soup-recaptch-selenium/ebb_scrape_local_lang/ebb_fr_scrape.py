import time

import requests
from bs4 import BeautifulSoup
from typing import TextIO
import re

import mysql.connector

mydb = mysql.connector.connect(
    host="production-b2b.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_scrape_google_feed"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,id FROM  `raptor_scrape_google_feed`.`ebb_url` WHERE STATUS IS NULL")
my_result = cur.fetchall()

for fetch in my_result:
    url1 = fetch[0]
    url = url1.replace('//gtrans.','//www.').replace('.com/','.fr/')
    id = fetch[1]

    try:
        product_url = url
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
        result = requests.get(product_url, headers=headers)
        soup = BeautifulSoup(result.content, 'html.parser')

        title1 = soup.find("div", class_="productInfoRight half-collomn").find('h1')
        title = (title1.text.strip().replace('\n','') if title1 else "not given")

        brand1 = soup.find("div", class_="product-brand-wrap").find('a', class_='product-brand')
        brand = (brand1.text.strip() if brand1 else "not given")
        itemId=''
        modelNo=''
        crosRef=''
        try:
            cro1 = soup.find("div", class_="item-model-crossref").find_all('span')
            crossref = [c1.text.strip() for c1 in cro1 if c1.text.strip() is not None]
            crossref.pop(1)

            itemId = crossref[0].split(': ')[1]
            modelNo = crossref[1].split(': ')[1]
            crosRef = crossref[2].split(': ')[1]

        except:
            crossref = []

        det1 = ''
        det = ''
        desc = ''
        try:
            det1 = soup.find("div", class_="productDetailsRight half-collomn").find('h2')
            det = (det1.text.strip() if det1 else "not given")
            desc = det
            # print(desc)
        except:
            desc = "not given"
        if (soup.find("div", class_="product-description")):
            desccc = soup.find("div", class_="product-description")

            if '<h2>' in str(desccc):
                print('yes')
                x = str(desccc).split('<h2>')[0]
                y = x.strip('<div class="product-description">')
                d2 = y.replace('"', "'")
                desc = det + ">" + d2
            else:
                d1 = desccc.text
                d2 = d1.replace('"', "'")
                desc = det + ">" + d2

        else:
            desc = 'pd specs not exist'
        breadcrum1 = soup.find("ul", class_="items breadcrumb").find_all('span')
        breadcrum = [br.text.strip() for br in breadcrum1 if br.text.strip() is not None]
        breadcrum.pop(1)
        b = '->'.join(breadcrum)

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
                i += 1

                x = (spec_i[j] if spec_i else "not given")
                j += 1

                sql = "INSERT INTO `raptor_scrape_google_feed`.ebb_fr_pd_specs(product_url,brand,model_no,attribute_name,attribute_value,attr_count) VALUES (%s, %s ,%s ,%s, %s,%s)"
                val = (product_url, brand, modelNo, z, x, i)
                cur.execute(sql, val)
                mydb.commit()
                # print(cur.rowcount, "record(s) affected")

        sql = "INSERT INTO `raptor_scrape_google_feed`.ebb_fr_pd_detail(product_url,brand,product_title,item_id,model_no,cross_ref,breadcrum,pd_detail) VALUES (%s, %s ,%s ,%s, %s,%s,%s,%s)"
        val = (product_url, brand, title, itemId, modelNo,crosRef,b,desc)
        cur.execute(sql, val)
        mydb.commit()
        print(cur.rowcount, "record(s) affected")
        sql = ("UPDATE `raptor_scrape_google_feed`.`ebb_url` SET status ='yes' WHERE   id='" + str(id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    except AttributeError:
        pass
