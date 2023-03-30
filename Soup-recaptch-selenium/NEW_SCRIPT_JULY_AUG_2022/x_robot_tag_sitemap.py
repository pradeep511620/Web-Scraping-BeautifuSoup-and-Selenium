import requests
from bs4 import BeautifulSoup

import mysql.connector

mydb = mysql.connector.connect(
    host="rpt-m24-development.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="Rahul_seo_checklist"
)
cur = mydb.cursor()
url = ["https://www.raptorsupplies.com/robots.txt"]
for fetch in url:
    flag = 0
    page = requests.get(fetch)
    soup = BeautifulSoup(page.content,'html.parser')
    s = soup.prettify()
    z = s.split("\n")
    this_di = []
    for x in z:
        a = x
        b = a.split(" ")
        c = " ".join(b)

        if c != "":
            d = c.split(" ")
            d1 = d[0].split(":")
            e = "".join(d1)

            this_dict = {
                            e: d[1]
                        }
            this_di.append(this_dict)
            if e == 'Sitemap':
                flag = 1
    if flag == 1:

        sitemap_url = d[1]
        page1 = requests.get(sitemap_url)
        soup = BeautifulSoup(page1.content, 'html.parser')
        for site in soup.find_all('loc'):
            xml_gz_url = site.text
            page2 = requests.get(xml_gz_url)
            print(page2.status_code)
            print(xml_gz_url)
    else:
        print("Sitemap not exist")









