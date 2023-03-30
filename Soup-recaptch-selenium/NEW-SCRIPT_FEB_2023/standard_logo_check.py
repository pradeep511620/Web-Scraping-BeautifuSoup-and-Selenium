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
cur.execute("SELECT product_url,logo_link,id FROM `standard_logo` where logo_check is null ")
my_result = cur.fetchall()
for fetch in my_result:
    product_url = fetch[0]
    logo_link = fetch[1]
    id = fetch[2]

    page = requests.get(product_url)
    soup = BeautifulSoup(page.content, "html.parser")
    flag = 0
    a = []
    b = []
    logo = logo_link.split(',')
    l = 'https://cdn.raptorsupplies.com/pub/media/catalog/standards_logo/'
    link = soup.find("div", class_='accordion-content certificates').find_all('img')
    for x, y in zip(link, logo):
        src = x['src']
        a.append(src)
        b.append(l + y)

    if a == b:
        f3 = "logo same"
        sql = ("UPDATE `standard_logo`SET logo_check ='" + str(
            f3) + "' WHERE   id='" + str(
            id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
    else:
        f4 = "logo not same"
        sql = ("UPDATE `standard_logo`SET logo_check ='" + str(
            f4) + "' WHERE   id='" + str(
            id) + "'")
        cur.execute(sql)
        mydb.commit()
        print(cur.rowcount, "records successful Done")
