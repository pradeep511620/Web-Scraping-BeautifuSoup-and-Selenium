import itertools

import mysql.connector
from bs4 import BeautifulSoup
import requests
import csv
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur=mydb.cursor()


with open(r'C:\Users\ashish\Downloads\b2b_redirects.csv','rt')as f:
        data = csv.reader(f)

        for row in itertools.islice(data,1,252):
            st=row[0]
            page = requests.get(st)
            soup = BeautifulSoup(page.content, "html.parser")
            s=(page.status_code)
            h=(page.history[0].status_code)

            cur = mydb.cursor()
            sql = ("INSERT INTO b2btesting (url,response) VALUES (%s,%s)")
            val = (st,h,)
            cur.execute(sql, val)
            mydb.commit()
            print(cur.rowcount, "record(s) affected")









