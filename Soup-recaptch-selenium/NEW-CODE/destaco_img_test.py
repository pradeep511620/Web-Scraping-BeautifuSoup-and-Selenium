import mysql.connector
import requests
from bs4 import BeautifulSoup
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='raptor_staging'
)
cur=mydb.cursor()
cur.execute('select url,new_value from `destaco_image_test`')
myresult=cur.fetchall()
for fetch in myresult:
    product_url=fetch[0]
    img_url=fetch[1]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    for im in soup.find('div',class_='xzoom-container').find_all('a'):
        img=im.get('href')
        img_url1='https://cdn.raptorsupplies.co.uk/pub/media/catalog/product'+img_url
        if(img_url1==img):
            print('image same')
        else:
            print('image not same')
