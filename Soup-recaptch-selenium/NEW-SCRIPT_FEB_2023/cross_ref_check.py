# live com onb test data (l3,item,parent,product_title)

from bs4 import BeautifulSoup
import mysql.connector
import requests
import html

mydb = mysql.connector.connect(
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_dat"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,cross_reference,id FROM `dba_182_justrite_corss` ")
myresult = cur.fetchall()
for fetch in myresult:
    product_url = fetch[0]
    cross_ref = fetch[1]
    id = fetch[2]
    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")

    try:
        cro1 = soup.find("div", class_="product-info d-flex").find_all('div')
        crossref1 = [c1.text.strip() for c1 in cro1 if c1.text.strip() is not None]

        print(crossref1[-1])
        print("Cross Ref: "+cross_ref)
        # print(crossref1)
        # print(cross_ref)
        # crossref = crossref[3].split(': ')[1]
        # if crossref == cross_ref:
        #     print("same")
        # else:
        #     print('not same')
    except:
        crossref = []





