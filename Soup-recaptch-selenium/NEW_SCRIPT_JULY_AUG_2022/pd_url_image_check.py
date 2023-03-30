from bs4 import BeautifulSoup
import mysql.connector
import requests
import time

mydb = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="Rahul_data_eng"
)

cur = mydb.cursor()
cur.execute("SELECT url FROM `pd_url` where url not in (select distinct product_url from product_image_scrape) limit 1")
my_result = cur.fetchall()

for fetch in my_result:
    try:
        pd_url = fetch[0]
        # print(pd_url)
        # a = (bytearray(pd_url, encoding='utf-8'))
        product_url = pd_url.decode('utf-8')
        page = requests.get(product_url, 'html.parser')
        # print(page.text)
        # exit()
        # req = requests.get(url, )
        soup = BeautifulSoup(page.content,'html.parser')
        print(soup)
        title = soup.find_all("img")
        for tit in title:
            try:
                img_src = tit.get("src")
                status = requests.get(img_src)
                st = status.status_code
                sql = "INSERT INTO product_image_scrape (product_url,image_url,status) VALUES (%s, %s,%s)"
                val = (product_url, img_src, st)
                cur.execute(sql, val)
                mydb.commit()
                print(cur.rowcount, "record inserted.")
            except:
                pass

    except AttributeError:

        pass
