import requests
from bs4 import BeautifulSoup
import mysql.connector
import time


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="grainger_fastner"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT DISTINCT alternate_url FROM `alternate_product_power` WHERE check1 IS NULL AND brand = alternate_brand")

myresult = mycursor.fetchall()

for row in myresult:

 try:

    product_url = row[0]

    #page = requests.get(product_url)

    headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}

    result = requests.get(product_url, headers=headers)

    if result.status_code == 200:

        print("site woking")

    else:

        print("site not working"+result.status_code)

    #a = (result.content.decode())

    soup = BeautifulSoup(result.content,'html.parser')

    #print(soup.prettify())

    title = soup.find("h1",class_="product-detail__heading")

    bread = soup.find("ul",class_="breadcrumb__container")

    brand = soup.find("p",class_="product-detail__brand")

    model = soup.find_all("span",class_="product-detail__product-identifiers-description")

    price = soup.find("span",class_="pricing__price")

    # qnt = (soup.prettify().replace('data-ship-pack-quantity="', "raptor:").split("raptor:")[1].split('"')[0])

    #weight = soup.find("div",class_="rta sidebar__shipping-pane")

    country = soup.find("span",class_="product-detail__country")

    #detail = soup.find("div",class_="copyTextSection textSection")

    image = soup.find("img",class_="image enhanced-content__carousel-main-image image--loaded")

    a = (title.text.strip() if title else "not given")

    b = (bread.text.strip() if bread else "not given")

    c = (product_url)

    d = (brand.text if brand else "not given")

    e = (model[0].text if model else "not given")

    f = (model[1].text if model else "not given")

    g = (model[2].text if model else "not given")

    h = (model[3].text if model else "not given")

    u = (price.text if price else "not given")

    #v = print(weight.text)

    k = (country.text if country else "not given")

    #m = (detail.text.strip())

    y = (image.get("src") if image else "not given")
    #
    # zxqw = qnt

    prod = soup.find_all("span",class_="specifications__description")

    specs = soup.find_all("span",class_="specifications__value")

    i = 0

    while i < len(prod):

        j = 0

        while j < len(specs):

            z = (prod[i].text if prod else "not given")

            i += 1

            x = (specs[j].text if specs else "not given")

            j += 1

            mycursor = mydb.cursor()

            sql = ('INSERT INTO power_new_data9(title,bread_crumb,brand,item,model_no,catalog_page,unspsc,prod,specs,price,country,image_url,product_url) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')

            mycursor.execute(sql, (a,b,d,e,f,g,h,z,x,u,k,y,c,))

            print(mycursor.rowcount, "under process")

            mydb.commit()



 except AttributeError:

   pass
