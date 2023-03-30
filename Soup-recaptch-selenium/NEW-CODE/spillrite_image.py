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
cur.execute("SELECT product_url,image_name FROM `spillrite_onb`")
myresult = cur.fetchall()
for fetch in myresult:
    product_url=fetch[0]
    image_name=fetch[1]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")
    for pd in soup.find("div", class_="xzoom-container").find_all("a"):
        url=pd.get('href')
        image="https://cdn.raptorsupplies.com/pub/media/catalog/product"+image_name
        if(image==url):
            print('image_same')
        else:
            print('image not same')








