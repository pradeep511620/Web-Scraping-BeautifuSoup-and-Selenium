from bs4 import BeautifulSoup
import mysql.connector
import requests
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="raptor_supplies_com"
)
cur = mydb.cursor()
cur.execute("SELECT product_url,is_bullet FROM martin_onb_com where is_bullet !=' ' ")
myresult = cur.fetchall()
for fetch in myresult:

    product_url=fetch[0]
    bullet=fetch[1]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "lxml")

    for bt in soup.find_all("div",class_='prodetail'):
        bt1=(bt.text)
        if(bt1==bullet):
            print("same")
        else:
            print("not same")



