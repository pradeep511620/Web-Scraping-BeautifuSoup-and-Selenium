
from bs4 import BeautifulSoup
import mysql.connector
import requests
mydb = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="TESTING"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,new_image,id FROM `48k_image_update_MIBT0_54`  where id>576 and img_test is null ")
myresult = cur.fetchall()
for fetch in myresult:
    url = fetch[0]
    image_name = fetch[1]
    id = fetch[2]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    for pd in soup.find("div", class_="producImg").find_all('a'):
        pd_image = pd.get('href')

        image = 'https://cdn.raptorsupplies.com/pub/media/catalog/product'+image_name

        if pd_image == image:
            par = 'image name found'
            sql = ("UPDATE `48k_image_update_MIBT0_54` SET img_test ='" + str(par) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        else:
            par1 = "image name not found"
            sql = ("UPDATE `48k_image_update_MIBT0_54` SET img_test ='" + str(par1) + "' WHERE   id='" + str(id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")


